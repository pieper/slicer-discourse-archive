# Set Pivot value to the model

**Topic ID**: 2581
**Date**: 2018-04-13
**URL**: https://discourse.slicer.org/t/set-pivot-value-to-the-model/2581

---

## Post #1 by @anandmulay3 (2018-04-13 10:22 UTC)

<p>How can i set pivot point to 3D model, normal segment exportation model pivot is far away from the actual model,it should be center of the model.</p>

---

## Post #2 by @lassoan (2018-04-13 13:15 UTC)

<p>Model is exported in the original patient coordinate system. You can change the position of a model by applying a transform to the node (in Transforms module, create a linear transform, apply to the model or segmentation, and adjust sliders; or enable Display / Interaction / Visible in 3D view and drag-and-drop the box in 3D view).</p>

---

## Post #3 by @pieper (2018-04-13 13:59 UTC)

<p>If you just want to be able to easily view the model you can also center the view with the button in the controller bar:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/MainApplicationGUI#3D_Viewer" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/MainApplicationGUI#3D_Viewer</a></p>

---

## Post #4 by @anandmulay3 (2018-04-13 14:51 UTC)

<p>Yeah that make sense , it comes from patient coordinate system. i’m using scriptable module to process it though batch file, but do we have any code to adjust pivot to the center of the model, or we have to adjust it manually.</p>

---

## Post #5 by @lassoan (2018-04-13 18:41 UTC)

<p>You can easily access and modify model points using numpy. For example you can “re-center” a model using this code snippet:</p>
<pre><code># Get point coordinates from model
modelNode = getNode('Segment_2')
points = arrayFromModelPoints(modelNode)

# Compute new coordinates and update them in-place
import numpy as np
centroid = np.mean(points, 0)
points[:] = points[:] - centroid

# Indicate that point modifications are completed and trigger re-render
modelNode.GetPolyData().GetPoints().GetData().Modified()
modelNode.GetDisplayNode().Modified()</code></pre>

---

## Post #6 by @anandmulay3 (2018-05-07 13:50 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="2581">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>points = arrayFromModelPoints(modelNode)</p>
</blockquote>
</aside>
<p>Traceback:<br>
‘MRMLCorePython.vtkMRMLScalarVolumeNode’ object has no attribute ‘GetPolyData’</p>

---

## Post #7 by @lassoan (2018-05-09 04:23 UTC)

<p>Try with latest nightly version of Slicer. There has been a related fix recently.</p>

---

## Post #8 by @anandmulay3 (2018-05-09 10:22 UTC)

<p>i have updated my slicer to latest Nightly build, so now what i’m doing is to get the poly data i think model is necessary.<br>
so i’m exporting segmentation to modelHirarchy &gt; using above code with the segment to set it at the center &gt; importing this model hierarchy to segmentation . using this i can able to set and export model successfully to center of the pivot point.</p>
<p>now the issue is in python interactor it is working fine , but when i try to run that code using my scriptable module app stop working error comes up and app crashes ,</p>
<p>i think this code is causing the problem <code>slicer.modules.segmentations.logic().ExportAllSegmentsToModelHierarchy(segmentationNode,modelNode)</code></p>

---

## Post #9 by @lassoan (2018-05-14 03:44 UTC)

<p>Could you please copy-paste the complete script here? The <code>modelNode</code> variable name indicates that you might try to export into a model node instead of a model hierarchy node (see <a href="http://apidocs.slicer.org/master/classvtkSlicerSegmentationsModuleLogic.html#afce3df1cc98a515ecf29cb190b12d66f">http://apidocs.slicer.org/master/classvtkSlicerSegmentationsModuleLogic.html#afce3df1cc98a515ecf29cb190b12d66f</a>).</p>
<p>Note that you can also export directly to files using <a href="http://apidocs.slicer.org/master/classvtkSlicerSegmentationsModuleLogic.html#a9578121589a3b5e20a05aa8dce33c642"><code>ExportSegmentsClosedSurfaceRepresentationToFiles()</code></a> method.</p>

---

## Post #10 by @VivianTetzner (2020-12-22 01:37 UTC)

<p>I’m having the same problem. Using this script or other similar code, they all return an AttributeError, like these:<br>
**1 → ** Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “/home/vivian/Sources/Slicer/Slicer-SuperBuild-Debug/Slicer-build/bin/Python/slicer/util.py”, line 1273, in arrayFromModelPoints<br>
pointData = modelNode.GetPolyData().GetPoints().GetData()<br>
AttributeError: ‘MRMLCorePython.vtkMRMLScalarVolumeNode’ object has no attribute ‘GetPolyData’</p>
<p>**2 → ** &gt;&gt;&gt; n=getNode(‘T1’)</p>
<blockquote>
<blockquote>
<blockquote>
<p>n<br>
(MRMLCorePython.vtkMRMLScalarVolumeNode)0x7f070983cca8<br>
nD=n.getDisplayNode()<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
AttributeError: ‘MRMLCorePython.vtkMRMLScalarVolumeNode’ object has no attribute ‘getDisplayNode’</p>
</blockquote>
</blockquote>
</blockquote>
<p>The version of Slicer is 4.13, from the nightly build</p>

---

## Post #11 by @lassoan (2020-12-22 04:42 UTC)

<p>The script above is for model nodes, which is not directly applicable to a volume node. Anyway, probably this is not needed anymore. If you want to rotate a node then you can now do it easily using GUI:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="bbikx7Edv4g" data-video-title="Transforming objects using Data module in 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=bbikx7Edv4g" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/bbikx7Edv4g/hqdefault.jpg" title="Transforming objects using Data module in 3D Slicer" width="" height="">
  </a>
</div>

<p>If you want to align nodes then I would recommend to use <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#semi-automatic-registration">semi-automatic registration</a>.</p>

---

## Post #12 by @VivianTetzner (2020-12-22 13:58 UTC)

<p>Actually, I’m trying to use the python interactor, but it doesn’t seen to work. I’m following the script from the " <a href="https://spujol.github.io/SlicerProgrammingTutorial/" rel="noopener nofollow ugc">Slicer Programming tutorial</a>" from the T1.nrrd image, and the following script:</p>
<p>n = getNote(‘T1’)<br>
nD = n.getDisplayNode()<br>
nD.InterpolateOff()</p>
<p>The first line works, but running the second line, this is what returns:</p>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
AttributeError: ‘MRMLCorePython.vtkMRMLScalarVolumeNode’ object has no attribute ‘getDisplayNode’</p>

---

## Post #13 by @pieper (2020-12-22 14:50 UTC)

<aside class="quote no-group" data-username="VivianTetzner" data-post="12" data-topic="2581">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/viviantetzner/48/9296_2.png" class="avatar"> VivianTetzner:</div>
<blockquote>
<p>getDisplayNode</p>
</blockquote>
</aside>
<p>Sorry, yes, that’s a typo in the tutorial - it should be <code>GetDisplayNode</code>.</p>
<p>There’s an updated version of the tutorial linked from here, with the typo fixed: <a href="https://docs.google.com/document/d/1WJFxbZrCCOGLi6_lqKrI5lfxwfdwP01Wkv-5YDBXq4g/edit" class="inline-onebox">Slicer Development Course 2020-12-15 - Google Docs</a></p>

---
