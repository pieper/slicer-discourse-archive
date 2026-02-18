# Break ModelNode Rendering After Repeated Camera Reset and Zoom

**Topic ID**: 38321
**Date**: 2024-09-11
**URL**: https://discourse.slicer.org/t/break-modelnode-rendering-after-repeated-camera-reset-and-zoom/38321

---

## Post #1 by @park (2024-09-11 07:14 UTC)

<p>Hi all,</p>
<p>As shown below, my code resets the camera and performs zoom operations.</p>
<pre><code class="lang-auto">layoutManager = slicer.app.layoutManager()

threeDWidget = layoutManager.threeDWidget("View1")
threeDView = threeDWidget.threeDView()
threeDView.rotateToViewAxis(3) 
threeDView.resetFocalPoint()
threeDView.resetCamera()

cameraNode = slicer.modules.cameras.logic().GetViewActiveCameraNode(threeDView.mrmlViewNode())
cameraNode.GetCamera().Zoom(1.25)
</code></pre>
<p>However, when used this codes repeatedly, the render of the modelNode becomes distorted, as seen in the example.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5aad8fdc73cc6219326da977e8d0960bf9b58ad9.png" alt="aa" data-base62-sha1="cWaPhrKCGMnknbad73tOaUbSSDf" width="522" height="397"></p>
<p>I would greatly appreciate any insights into what might be causing this issue.</p>

---

## Post #2 by @pieper (2024-09-11 14:16 UTC)

<p>Hi Tae Young -</p>
<p>I’m not sure what this would be - possibly zbuffer resolution changes due to clipping planes or something.</p>
<p>It would be great if you could convert this into a simple to reproduce script that anyone could paste into their python console to replicate and experiment with. That is, use the methods in <code>slicer.util</code> to download and load an example model and then apply your manipulations in a loop to replicate the appearance changes you see.  Such a script can help you and everyone explore what you are seeing.</p>

---

## Post #3 by @Matteboo (2024-09-11 14:25 UTC)

<p>Hello,</p>
<p>What version of slicer are you using ?<br>
I had a similar issue with version 5.4 but it was fixed when I upgraded to 5.6.</p>

---

## Post #4 by @park (2024-09-11 14:30 UTC)

<p>Hi!</p>
<p>I tested this in various version 5.1, 5.6, and 5.7<br>
All versions show same issues to me ,</p>

---

## Post #5 by @lassoan (2024-09-11 21:11 UTC)

<p>I don’t see any distortion. Are you referring to the noise appering on the surface?</p>
<p>I’ve tried your script on some models that I have and could not reproduce what you show in the screenshot. Could you share a model (upload somewhere and post the link here) that demonstrates this problem?</p>

---

## Post #6 by @park (2024-09-13 01:53 UTC)

<p>I share the code that illustrates the issue. I believe the problem only occurs in flat interpolation with (<code>modeNode.GetDisplayNode().SetInterpolation(0)</code> → flat interpolation).</p>
<pre><code class="lang-auto">cylinder = vtk.vtkCylinderSource()
cylinder.SetHeight(60)
cylinder.SetRadius(20)
cylinder.SetResolution(50)

node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode")
node.SetPolyDataConnection(cylinder.GetOutputPort())
node.CreateDefaultDisplayNodes()
node.GetDisplayNode().SetColor(1,1,1)
node.GetDisplayNode().SetInterpolation(0)


################################################################

for i in range(50):
    layoutManager = slicer.app.layoutManager()

    threeDWidget = layoutManager.threeDWidget("View1")
    threeDView = threeDWidget.threeDView()
    threeDView.rotateToViewAxis(3) 
    threeDView.resetFocalPoint()
    threeDView.resetCamera()

    cameraNode = slicer.modules.cameras.logic().GetViewActiveCameraNode(threeDView.mrmlViewNode())
    cameraNode.GetCamera().Zoom(1.25)
</code></pre>

---

## Post #7 by @lassoan (2024-09-13 04:23 UTC)

<p>By zooming in by 1.25x 50 times, you completely messed up your camera.</p>
<p>You moved it out 10 kilometers away from the focal point:</p>
<pre data-code-wrap="python"><code class="lang-python">&gt;&gt;&gt; cam.GetDistance()
13302319.57321041
</code></pre>
<p>The model is still filling the field of view because you also reduced the field of view 1/10000th of a degree:</p>
<pre data-code-wrap="python"><code class="lang-python">&gt;&gt;&gt; cam.GetViewAngle()
0.00027403155699954446
</code></pre>
<p>I would recommend you to just not do this. Instead, set up your camera in a reasonable way, similarly to how you would set up a camera in real world. You can have the camera maybe a few meters away from the patient, but not try to look at the patient from a distance of 10+ kilometers, as you will run into numerical precision issues.</p>

---
