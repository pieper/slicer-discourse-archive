---
topic_id: 9571
title: "Low Fps For Transforming Surfaces"
date: 2019-12-20
url: https://discourse.slicer.org/t/9571
---

# Low FPS for transforming surfaces

**Topic ID**: 9571
**Date**: 2019-12-20
**URL**: https://discourse.slicer.org/t/low-fps-for-transforming-surfaces/9571

---

## Post #1 by @rprueckl (2019-12-20 12:52 UTC)

<p>We want to transform 3D models in ‘real time’ in 3D Slicer with data coming from outside. The problem is, that the frame rate we currently reach is very low. Below is some demonstration code to show our approach:</p>
<p>hpp:</p>
<pre><code class="lang-auto">QTimer fpsTestUpdateTimer;
vtkSmartPointer&lt;vtkTransform&gt; fpsTestTransform;
vtkMRMLTransformNode* fpsTestTransformNode;
</code></pre>
<p>cpp:</p>
<pre><code class="lang-auto">{
    ...
    connect(&amp;fpsTestUpdateTimer, &amp;QTimer::timeout, this, &amp;MovementDemo::fpsTestTimerCallback);
    ...
}

//----------------------------------------------------------------------------
void MovementDemo::startStopFpsTest(bool enable, int fps)
{
    if (!enable)
    {
        fpsTestUpdateTimer.stop();
    }
    else if(!trackingUpdateTimer.isActive())
    {
        qSlicerApplication* app = qSlicerApplication::application();
        fpsTestTransform = vtkSmartPointer&lt;vtkTransform&gt;::New();
        fpsTestTransform-&gt;RotateZ(1);
        fpsTestTransformNode = vtkMRMLTransformNode::SafeDownCast(app-&gt;mrmlScene()-&gt;GetFirstNodeByName("FpsTestTransform"));
        fpsTestUpdateTimer.start(1000 / fps);
    }
}

//----------------------------------------------------------------------------
void MovementDemo::fpsTestTimerCallback()
{
    fpsTestTransformNode-&gt;ApplyTransform(fpsTestTransform);
}
</code></pre>
<p>The transform is applied to a model with about 1600 vertices.<br>
On a screen with a resolution of 1920x1080, where the 3D view occupies about half of the screen space, we get about 10-20 fps (according to the fps display of the 3D viewer).<br>
When I activate the ‘3D view rock’ <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78114c9d4f9a4d77516a8b8b65e415c769d0266c.png" alt="image" data-base62-sha1="h8amjLpX54qxNhoCah8FWWESkY4" width="37" height="35">.</p>
<p>Here are two videos for illustration (and because of the season):<br>
Change transform:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d083a4d1997bcf7d081677756c946d8cd55ebf53.gif" alt="v15" data-base62-sha1="tKBmhHxTUNyfzbWSURiwbaxBFWX" width="400" height="360"></p>
<p>Rock animation:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5fe527adc2f2a02987c6be52a353e1afebfcad2c.gif" alt="v60" data-base62-sha1="dGkjXMUMHpTKs6uSEXsp0jKTCCo" width="400" height="360"></p>
<p>Any help regarding optimization possibilities is greatly appreciated.<br>
Happy holidays!</p>

---

## Post #2 by @lassoan (2019-12-20 13:51 UTC)

<p><code>ApplyTransform</code> modifies the polydata in each iteration, which is time-consuming and in the long term even some error in the point coordinates may accumulate.</p>
<p>If you want to rotate the viewpoint then modify the camera position (this is done when you activate 3D view rock feature). If you want to modify an object pose then set its parent transform once, then modify the matrix in the transform node at each iteration.</p>

---

## Post #3 by @rprueckl (2019-12-20 14:47 UTC)

<p>Thank you Andras, I adapted my code to the following:</p>
<pre><code class="lang-auto">//----------------------------------------------------------------------------
void MovementDemo::fpsTest(bool enable, int fps)
{
    if (!enable)
    {
        fpsTestUpdateTimer.stop();
    }
    else if(!trackingUpdateTimer.isActive())
    {
        qSlicerApplication* app = qSlicerApplication::application();

        fpsTestUpdateTimer.start(1000 / fps);
        fpsTestTransformNode = vtkMRMLLinearTransformNode::SafeDownCast(app-&gt;mrmlScene()-&gt;GetFirstNodeByName("FpsTestTransform"));
        fpsTestTransform = vtkTransform::SafeDownCast(fpsTestTransformNode-&gt;GetTransformToParent());
    }
}

//----------------------------------------------------------------------------
void MovementDemo::fpsTestTimerCallback()
{
    fpsTestTransform-&gt;RotateZ(1);
    fpsTestTransformNode-&gt;Modified();
}
</code></pre>
<p>The results are better - some data:</p>
<p>fps setting (= 1000 / timer callback rate) --&gt; displayed fps<br>
30  --&gt; 20<br>
40  --&gt; 30<br>
50  --&gt; 30<br>
60  --&gt; 30<br>
80  --&gt; 33<br>
100 --&gt; 35<br>
120 --&gt; 33<br>
200 --&gt; 40<br>
300 --&gt; 40<br>
500 --&gt; 40</p>
<p>I don’t quite understand the connection between my timer repetition rate and the resulting frame rate. Can it be connected with vsync? Just for information: the CPU load during the test (fps setting 120) is around 5%, the GPU load at around 10%.</p>
<p>I really would like to reach a refresh rate of 60Hz for this simple example. Are there any more suggestions for what I could try to do? Would it help to call ‘forceRender’ like it is done in the rock animation? <a href="https://github.com/commontk/CTK/blob/78341abaf1c56bbdcc70372ffefed91e2a940d32/Libs/Visualization/VTK/Widgets/ctkVTKRenderView.cpp#L190" rel="nofollow noopener">https://github.com/commontk/CTK/blob/78341abaf1c56bbdcc70372ffefed91e2a940d32/Libs/Visualization/VTK/Widgets/ctkVTKRenderView.cpp#L190</a></p>

---

## Post #4 by @lassoan (2019-12-20 15:25 UTC)

<p>vsync caps the refresh rate at 60Hz (probably on a simple rendering you could do hundreds of fps).</p>
<p><code>scheduleRender</code> mechanism in <a href="https://github.com/commontk/CTK/blob/master/Libs/Visualization/VTK/Widgets/ctkVTKAbstractView.h#L110-L131">ctkVTKAbstractView</a> optimizes number of actual renderings in response to <code>scheduleRender</code> requests. By default refresh rate is capped at 60Hz and up to 1 frame latency is introduced, but it is a small price to pay considering that it eliminates unnecessary re-renderings.</p>
<p>For replaying animations at a fixed frame rate you may circumvent scheduleRender mechanism and issue forceRender calls at regular time intervals. This should not be a problem as long as there is only one component that does this (if you had multiple sources of forceRender then your application could slow down due to many unnecessary re-renderings).</p>

---

## Post #5 by @rprueckl (2020-01-08 16:48 UTC)

<p>just to share my experiences here:</p>
<p><code>scheduleRender</code> clearly would be the desired solution, however, I never managed to reach a frame rate &gt; 40 (according to the fps display of the 3d view), when calling <code>scheduleRender</code> 80-500 times a second with an empty scene and with the window sized such that the 3d view has 300x400px. As said, the rock animation renders with 60 fps.</p>

---

## Post #6 by @lassoan (2020-01-08 17:15 UTC)

<p>One possible reason you do not reach the maximum target refresh rate (60fps by default) is that transforming a node is a costly operation (in contrast what “3D view rock” does - just rotating the camera). It may also trigger update of multiple views, which may further slow down the rendering. You can build in RelWithDebInfo and run the code with a profiler to get definitive answer.</p>

---

## Post #7 by @rprueckl (2020-01-08 17:30 UTC)

<p>Oh, I forgot to mention, I commented out any transform manipulation in my last test - so only the following code reaches a maximum of 40 fps:</p>
<pre><code class="lang-auto">void MovementDemo::fpsTestTimerCallback()
{
    if (!animationIntervalMs)
    {
        return;
    }

    threeDView-&gt;scheduleRender();

    QTimer::singleShot(animationIntervalMs, this, SLOT(fpsTestTimerCallback()));
}
</code></pre>
<p>When I use <code>forceRender</code>, the 60 fps can be reached.<br>
I am currently thinking about updating the view constantly with 60 Hz using <code>forceRender</code> and performing the updates of the transforms with another timer.</p>

---
