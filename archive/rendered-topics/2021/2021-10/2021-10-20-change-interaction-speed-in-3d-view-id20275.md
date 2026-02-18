# Change interaction speed in 3D view

**Topic ID**: 20275
**Date**: 2021-10-20
**URL**: https://discourse.slicer.org/t/change-interaction-speed-in-3d-view/20275

---

## Post #1 by @keri (2021-10-20 20:39 UTC)

<p>Hi,</p>
<p>I’m looking for a way to change view movement/rotation speed.<br>
The problem is that when I change camera aspect ratio in 3D view (by adding transform-&gt;scale to camera) I can see that interaction along scaled axis becomes slower (rotation/movement), I guess proporsionally to scale factor set.</p>
<p>I need to compensate this speed change.</p>

---

## Post #2 by @lassoan (2021-10-22 18:01 UTC)

<p>Have a look at vtkMRMLCameraWidget and see if you can come up with a solution that works for both equal and distorted view aspect ratios.</p>
<p>I’m surprised that the rotation is impacted, because mouse event position changes are evaluated in display coordinate system and scaled with <code>this-&gt;Renderer-&gt;GetRenderWindow()-&gt;GetSize()</code> and I would have thought that none of them is impacted by your changes. How did you change the camera aspect ratio? Did it result in change of renderwindow size or display coordinates?</p>

---

## Post #3 by @keri (2021-10-22 19:12 UTC)

<p>Hi,</p>
<p>Thank you for reply, I will take a look at <code>vtkCameraWidget</code> soon.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="20275">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>How did you change the camera aspect ratio? Did it result in change of renderwindow size or display coordinates?</p>
</blockquote>
</aside>
<p>All I do is set transform to camera node. <a href="https://github.com/tierra-colada/Seismic/blob/2d30eabe3567b0473fa07ba278cce014ddf6ca27/Zoom/Logic/vtkSlicerZoomLogic.cxx#L97-L108" rel="noopener nofollow ugc">Here is the code, it’s pretty simple</a><br>
So it doesn’t change renderwindow.</p>

---

## Post #4 by @lassoan (2021-10-23 22:53 UTC)

<p>They code is indeed just a few lines, but it modifies the camera at a very low level. We do not anticipate such changes when we implement Slicer core features. I’m surprised that this rotation speed is the only side effect that you encountered.</p>

---

## Post #5 by @keri (2021-10-24 01:44 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="20275">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’m surprised that this rotation speed is the only side effect that you encountered.</p>
</blockquote>
</aside>
<p>Probably there are more I just haven’t noticed them yet <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @keri (2021-10-26 02:13 UTC)

<p>It seems that <code>vtkMRMLCameraWidget</code> can’t control interaction speed.</p>
<p>Does VTK in general provide API to control spin/move speed? Can’t find this information in the internet</p>

---

## Post #7 by @lassoan (2021-10-26 02:36 UTC)

<p>The interaction speed is controlled in the vtkMRMLCameraWidget. See for example how rotation speed is determined:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/887ca1bcf002c8968164fd5fe66b970217191b04/Libs/MRML/DisplayableManager/vtkMRMLCameraWidget.cxx#L618-L624">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/887ca1bcf002c8968164fd5fe66b970217191b04/Libs/MRML/DisplayableManager/vtkMRMLCameraWidget.cxx#L618-L624" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/887ca1bcf002c8968164fd5fe66b970217191b04/Libs/MRML/DisplayableManager/vtkMRMLCameraWidget.cxx#L618-L624" target="_blank" rel="noopener">Slicer/Slicer/blob/887ca1bcf002c8968164fd5fe66b970217191b04/Libs/MRML/DisplayableManager/vtkMRMLCameraWidget.cxx#L618-L624</a></h4>



  <pre class="onebox">    <code class="lang-cxx">
      <ol class="start lines" start="618" style="counter-reset: li-counter 617 ;">
          <li>int *size = this-&gt;Renderer-&gt;GetRenderWindow()-&gt;GetSize();</li>
          <li>
          </li>
<li>double delta_elevation = -20.0 / size[1];</li>
          <li>double delta_azimuth = -20.0 / size[0];</li>
          <li>
          </li>
<li>double rxf = (double)dx * delta_azimuth * this-&gt;MotionFactor;</li>
          <li>double ryf = (double)dy * delta_elevation * this-&gt;MotionFactor;</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @keri (2021-11-02 00:41 UTC)

<p>Thank you for the hint,</p>
<p>To fix interaction issue when aspect ratio is changed it is enough to modify the function <code>bool vtkMRMLCameraWidget::ProcessTranslate(vtkMRMLInteractionEventData* eventData)</code> by multyplying each translation (dx, dy, dz) by scaling factor from the matrix:</p>
<pre><code class="lang-cpp">  // Camera motion is reversed

  vtkMatrix4x4* M = camera-&gt;GetModelTransformMatrix(); 
  double motionVector[3] =
    {
    (oldPickPoint[0] - newPickPoint[0]) * M-&gt;GetElement(0,0),
    (oldPickPoint[1] - newPickPoint[1]) * M-&gt;GetElement(1,1),
    (oldPickPoint[2] - newPickPoint[2]) * M-&gt;GetElement(2,2)
    };
</code></pre>
<p>I don’t know whether Slicer community need that to be implemented via PR?</p>
<p>Also <code>vtkMRMLViewDisplayableManager::AxisLabelTexts</code> shown in the picture are affected by aspect ratio (I have set Z scale to 20 in the picture). I don’t know how to fix that but for <code>vtkCubeAxesActor</code> <a href="https://discourse.vtk.org/t/scaling-a-rendering-scene/173/7?u=kerim" rel="noopener nofollow ugc">the solution is provided here</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/613fec23d04804798ba877dc2e560906f8aa8f43.jpeg" data-download-href="/uploads/short-url/dSjgBnQ93FDvdDJXp3NQbOdH7Oj.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/613fec23d04804798ba877dc2e560906f8aa8f43_2_690x390.jpeg" alt="image" data-base62-sha1="dSjgBnQ93FDvdDJXp3NQbOdH7Oj" width="690" height="390" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/613fec23d04804798ba877dc2e560906f8aa8f43_2_690x390.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/613fec23d04804798ba877dc2e560906f8aa8f43_2_1035x585.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/613fec23d04804798ba877dc2e560906f8aa8f43.jpeg 2x" data-dominant-color="9496BD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1086×615 83.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @lassoan (2021-11-02 13:05 UTC)

<aside class="quote no-group" data-username="keri" data-post="8" data-topic="20275">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>To fix interaction issue when aspect ratio is changed it is enough to modify the function <code>bool vtkMRMLCameraWidget::ProcessTranslate(vtkMRMLInteractionEventData* eventData)</code> by multyplying each translation (dx, dy, dz) by scaling factor from the matrix</p>
</blockquote>
</aside>
<p>Nice progress. You can submit a pull request for the interaction scaling issue. Instead of using only the diagonal elements of the camera matrix, you need to use the column norm.</p>
<aside class="quote no-group" data-username="keri" data-post="8" data-topic="20275">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>Also <code>vtkMRMLViewDisplayableManager::AxisLabelTexts</code> shown in the picture are affected by aspect ratio (I have set Z scale to 20 in the picture). I don’t know how to fix that</p>
</blockquote>
</aside>
<p>One option is to add an option to show axis codes in top/down/left/right annotations instead of painting those on the 3D cube sides (this would be a very useful orientation marking option anyway):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ecaf6e99328e6f0038f9a2601f0404bc5fedd477.jpeg" data-download-href="/uploads/short-url/xLOxKHgEx2ttYSBG2Jlzq4JZWpp.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ecaf6e99328e6f0038f9a2601f0404bc5fedd477_2_690x390.jpeg" alt="image" data-base62-sha1="xLOxKHgEx2ttYSBG2Jlzq4JZWpp" width="690" height="390" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ecaf6e99328e6f0038f9a2601f0404bc5fedd477_2_690x390.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ecaf6e99328e6f0038f9a2601f0404bc5fedd477_2_1035x585.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ecaf6e99328e6f0038f9a2601f0404bc5fedd477.jpeg 2x" data-dominant-color="9596BB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1086×615 98.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You may also use orientation markers in the lower-right corner.</p>
<p>You can fix the issue by using the using the camera transform to adjust the AxisLabelText transforms in vtkMRMLViewDisplayableManager (you need to experiment with how exactly).</p>
<p>It would be important to add a Python-scripted test that adjusts the scale of a 3D view the same way as you do in your application and performs basic checks. This would ensure that the changes that you contribute remain functional as Slicer code evolves. It would also make it easier for anyone to enable the distorted rendering, in case they want to test if some changes are compatible with this rendering mode.</p>

---

## Post #10 by @keri (2021-11-02 16:55 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="20275">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Instead of using only the diagonal elements of the camera matrix, you need to use the column norm.</p>
</blockquote>
</aside>
<p>Yes, you should be right (I guess we are talking about matrix multiplication) and I think it could be rewritten in the following way:</p>
<pre data-code-wrap="cpp"><code class="lang-cpp">  // Camera motion is reversed

  double motionVector[3] =
    {
    oldPickPoint[0] - newPickPoint[0],
    oldPickPoint[1] - newPickPoint[1],
    oldPickPoint[2] - newPickPoint[2]
    };

  // If any transform is applied to the camera then we need to
  // take that into account
  vtkMatrix4x4* M = camera-&gt;GetModelTransformMatrix();
  motionVector[0] =
      motionVector[0]*M-&gt;GetElement(0,0) +
      motionVector[1]*M-&gt;GetElement(1,0) +
      motionVector[2]*M-&gt;GetElement(2,0);
  motionVector[1] =
      motionVector[0]*M-&gt;GetElement(0,1) +
      motionVector[1]*M-&gt;GetElement(1,1) +
      motionVector[2]*M-&gt;GetElement(2,1);
  motionVector[2] =
      motionVector[0]*M-&gt;GetElement(0,2) +
      motionVector[1]*M-&gt;GetElement(1,2) +
      motionVector[2]*M-&gt;GetElement(2,2);
</code></pre>
<p>Is that correct now?<br>
I don’t use intermal <code>vtkMatrix4x4</code> methods to multiply values as I don’t want to introduce new vector variable.</p>
<p>It is easy to understand what behaviour should interaction have when we simply want to scale the camera (as I do). But what if user want to apply some rotation for example (even though I don’t know why)? How the interaction should behave now?<br>
Here is a python code that can be used to try that (probably it should be used in pair with <code>vtkMRMLCameraWidget::PocessTranslate()</code> modification applied):</p>
<pre data-code-wrap="python"><code class="lang-python">#-------PREPARING DATA-------
# Prepare data for volume
nodeName = "MyNewVolume"
imageSize = [10, 10, 10]
imageOrigin = [0.0, 0.0, 0.0]
imageSpacing = [1.0, 1.0, 1.0]

scalars = vtk.vtkDoubleArray()
scalars.SetName("my_scalars")

for i in range(0, imageSize[0]*imageSize[1]*imageSize[2]):
    v = scalars.InsertNextValue(i)

# Create an image volume
imageData = vtk.vtkImageData()
imageData.SetDimensions(imageSize)
imageData.GetPointData().SetScalars(scalars)

# Create volume node
volumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", nodeName)
volumeNode.SetOrigin(imageOrigin)
volumeNode.SetSpacing(imageSpacing)
volumeNode.SetAndObserveImageData(imageData)
volumeNode.CreateDefaultDisplayNodes()
volumeNode.CreateDefaultStorageNode()

#-------PREPARING CAMERA-------
# Getting camera from 3D view
layoutManager = slicer.app.layoutManager()
view = layoutManager.threeDWidget(0).threeDView()
threeDViewNode = view.mrmlViewNode()
cameraNode = slicer.modules.cameras.logic().GetViewActiveCameraNode(threeDViewNode)

# Getting camera
renderWindow = view.renderWindow()
renderers = renderWindow.GetRenderers()
renderer = renderers.GetItemAsObject(0)
camera = cameraNode.GetCamera()

#-------PREPARING CAMERA TRANSFORM-------
# Rotate camera in 90 degree in LR
# 1 0 0
# 0 0 -1
# 0 1 0
m = camera.GetModelTransformMatrix()
m.SetElement(0,0, 1)
m.SetElement(0,1, 0)
m.SetElement(0,2, 0)
m.SetElement(1,0, 0)
m.SetElement(1,1, 0)
m.SetElement(1,2, -1)
m.SetElement(2,0, 0)
m.SetElement(2,1, 1)
m.SetElement(2,2, 0)

camera.SetModelTransformMatrix(m)
</code></pre>
<p>Thus if we apply scale to the camera then everything is fine.<br>
But when we apply rotation then it is difficult to understand what is going on when we try to translate the volume. I think this is important for Slicer community</p>
<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="20275">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It would be important to add a Python-scripted test that adjusts the scale of a 3D view the same way as you do in your application and performs basic checks.</p>
</blockquote>
</aside>
<p>I completely agree but I don’t have experience of writing tests in Slicer so far. Is there any test examples close to my task? I will try to look in Slicer documentation and find information how to write tests.</p>
<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="20275">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>One option is to add an option to show axis codes in top/down/left/right annotations instead of painting those on the 3D cube sides (this would be a very useful orientation marking option anyway):</p>
</blockquote>
</aside>
<p>Thank you!<br>
I like the idea how you labeled axes near window boundaries. I will refer to that labeling staff in the future (for now this is not the most important thing, I need to work now on foundamental staff)</p>

---

## Post #11 by @mau_igna_06 (2021-11-02 17:55 UTC)

<p>Did you try the code below? I don’t know if it would work but I think you are using the transpose of the rotation matrix instead of the rotation matrix.</p>
<pre><code class="lang-auto">// Camera motion is reversed

  double motionVector[3] =
    {
    oldPickPoint[0] - newPickPoint[0],
    oldPickPoint[1] - newPickPoint[1],
    oldPickPoint[2] - newPickPoint[2]
    };

  // If any transform is applied to the camera then we need to
  // take that into account
  vtkMatrix4x4* M = camera-&gt;GetModelTransformMatrix();
  motionVector[0] =
      motionVector[0]*M-&gt;GetElement(0,0) +
      motionVector[1]*M-&gt;GetElement(0,1) +
      motionVector[2]*M-&gt;GetElement(0,2);
  motionVector[1] =
      motionVector[0]*M-&gt;GetElement(1,0) +
      motionVector[1]*M-&gt;GetElement(1,1) +
      motionVector[2]*M-&gt;GetElement(1,2);
  motionVector[2] =
      motionVector[0]*M-&gt;GetElement(2,0) +
      motionVector[1]*M-&gt;GetElement(2,1) +
      motionVector[2]*M-&gt;GetElement(2,2);
</code></pre>

---

## Post #12 by @keri (2021-11-02 18:32 UTC)

<p>Thank you for response,</p>
<p>I’m not 100% sure but I think according to matrix multiplication rule if we want to multiply a vector to a matrix we can write that in the form:</p>
<pre><code class="lang-auto"># v = motionVector; M - transform matrix
v * M = [x, y, z] * [a00, a01, a02; a10, a11, a12; a20, a21, a22] # `a21` means element at second row and first col. Symbol `;` (semicolon) is a row delimiter, `,` (comma) is a column delimiter

# multiplying vector to each column gives:
v * M = [x*a00 + y*a10 + z*a20, x*a01 + y*a11 + z*a21, x*a02 + y*a12 + z*a22]
</code></pre>
<p>As I understand you propose to multiply matrix <code>M</code> to a vector <code>motionVector</code>. Maybe that is correct but I have some doubts <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Anyway I just tried your proposition and the behaviour is still hardly predictable when I apply rotation transform to the camera</p>

---

## Post #13 by @lassoan (2021-11-02 18:57 UTC)

<p>To ensure that the computations are correct, please use good names for variables. Add the coordinate system name as a suffix to vector variables. For example, <code>motionVector_RAS</code> (or <code>motionVector_World</code>) instead of just <code>motionVector</code>. Transforms must be named based on the coordinate system names they transform between. For example instead of <code>M</code> you must use something like <code>worldToSliceTransform</code> (I’m not sure if M is actually a transform between these, just an example).</p>
<aside class="quote no-group" data-username="keri" data-post="10" data-topic="20275">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>I don’t use intermal <code>vtkMatrix4x4</code> methods to multiply values as I don’t want to introduce new vector variable.</p>
</blockquote>
</aside>
<p>Please, use multiply method in <code>vtkMatrix4x4</code>. For a single mouse move, you perform hundreds of memory allocations and thousands of multiplications, so reducing readability and risk of introducing bugs is just not worth it. It is only acceptable to reimplement basic methods like this if you can prove with performance profiling data that it leads to significant performance improvement (&gt;10%).</p>

---

## Post #14 by @keri (2021-11-03 01:53 UTC)

<p><a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> you were right about matrix multiplication, I checked that. Thank you!</p>
<p>I have written a test in python but I’m not sure where should I put that test. I can see that <code>d/slicersources-src/Libs/MRML/DisplayableManager</code> has subfolder <code>Testing</code> but now it only contains <code>Cxx</code> tests.<br>
Is it ok if I add <code>Python</code> folder with my test there?</p>
<pre><code class="lang-python"># Get all necesssary objects
threeDViewWidget = slicer.app.layoutManager().threeDWidget(0)
view = threeDViewWidget.threeDView()
viewNode = view.mrmlViewNode()
renderer = view.renderWindow().GetRenderers().GetItemAsObject(0)
camera = renderer.GetActiveCamera()
cameraDisplayableManager = view.displayableManagerByClassName("vtkMRMLCameraDisplayableManager")
cameraWidget = cameraDisplayableManager.GetCameraWidget()


# Automatically send events to make a translation like user usually do interactively
def do_translate():
    # Process CLICK ON (click mouse 1 btn)
    ev = slicer.vtkMRMLInteractionEventData()
    ev.SetRenderer(renderer)
    ev.SetViewNode(viewNode)
    ev.SetType(12)
    ev.SetKeySym("Shift_L")
    ev.SetModifiers(1)	# Shift btn
    ev.SetMouseMovedSinceButtonDown(False)
    ev.SetWorldPosition([0, 0, 0]) 
    ev.SetDisplayPosition([0, 0])
    cameraWidget.ProcessInteractionEvent(ev)
    
    # Process DRAG
    ev = slicer.vtkMRMLInteractionEventData()
    ev.SetRenderer(renderer)
    ev.SetViewNode(viewNode)
    ev.SetType(26)
    ev.SetKeySym("Shift_L")
    ev.SetModifiers(1)	# Shift btn
    ev.SetMouseMovedSinceButtonDown(True)
    ev.SetWorldPosition([0, 0, 10])
    ev.SetDisplayPosition([0, 100])
    cameraWidget.ProcessInteractionEvent(ev)
    
    # Process CLICK OFF (release the mouse 1 btn)
    ev = slicer.vtkMRMLInteractionEventData()
    ev.SetRenderer(renderer)
    ev.SetViewNode(viewNode)
    ev.SetType(13)
    ev.SetKeySym("Shift_L")
    ev.SetModifiers(1)	# Shift btn
    ev.SetMouseMovedSinceButtonDown(True)
    ev.SetWorldPosition([0, 0, 10])
    ev.SetDisplayPosition([0, 100])
    cameraWidget.ProcessInteractionEvent(ev)


# list_out = list_a - list_b
def substract_lists(a: list, b: list) -&gt; list:
    if len(a) != len(b):
        return
    out = [0] * len(a)
    for i in range(0, len(a)):
        out[i] = a[i]-b[i]
    return out


# Calculate `delta_cam_pos` before changing aspect ratio
cam_pos_old = camera.GetPosition()
do_translate()
cam_pos_new = camera.GetPosition()
delta_cam_pos = substract_lists(cam_pos_new, cam_pos_old)

# Change aspect ratio
transform = vtk.vtkTransform()
transform.Scale(1, 1, 10)
camera.SetModelTransformMatrix(transform.GetMatrix())

# Calculate `delta_translated_cam_pos` after changing aspect ratio
translated_cam_pos_old = camera.GetPosition()
do_translate()
translated_cam_pos_new= camera.GetPosition()
delta_translated_cam_pos = substract_lists(translated_cam_pos_new, translated_cam_pos_old)


# return `True` if `list_a` contains almost the same elements as `list_b`
def compare_lists(a: list, b: list) -&gt; bool:
    if len(a) != len(b):
        return
    from math import isclose
    out = True
    for i in range(0, len(a)):
        out = out and isclose(a[i], b[i])
    return out


# Delta translations calculated before scaling camera and after that should be equal
compare_lists(delta_cam_pos, delta_translated_cam_pos)
</code></pre>

---

## Post #15 by @keri (2021-11-03 23:31 UTC)

<p>I added a <a href="https://github.com/Slicer/Slicer/pull/5987" rel="noopener nofollow ugc">PR with the C++ test</a>.</p>
<p>Also could someone check my <a href="https://github.com/Slicer/Slicer/pull/5950" rel="noopener nofollow ugc">another PR</a>. It hangs on for almost three weeks</p>

---
