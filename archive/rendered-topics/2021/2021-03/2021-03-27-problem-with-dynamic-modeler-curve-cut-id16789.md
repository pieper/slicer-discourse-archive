---
topic_id: 16789
title: "Problem With Dynamic Modeler Curve Cut"
date: 2021-03-27
url: https://discourse.slicer.org/t/16789
---

# Problem with Dynamic Modeler Curve Cut

**Topic ID**: 16789
**Date**: 2021-03-27
**URL**: https://discourse.slicer.org/t/problem-with-dynamic-modeler-curve-cut/16789

---

## Post #1 by @Cody_Xie (2021-03-27 17:52 UTC)

<p>Dear all,</p>
<p>I have encountered a problem while using the <strong>Dynamic Modeler</strong> (<strong>curve cut</strong>) .</p>
<p>My workflow is as follows:</p>
<ol>
<li>Import a DICOM-RT Structure with the corresponding CT data set;</li>
<li>Export the DICOM-RT Structure to a obj file (since the DICOM_RT Structure cannot be use as an input nodes in Dynamic Model);</li>
<li>Import the obj file created in step 2;</li>
<li>Generate a Closed Curve on the model’s surface;</li>
<li>(Follow the tutorial workflow in this Dynamic Modeler tutorial video <a href="https://www.youtube.com/watch?v=F6fNMQTxD-4" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=F6fNMQTxD-4</a>);</li>
</ol>
<p>However, after this workflow, I cannot get the result like the result in the video. The new clipped file is always invisible. I guess these four screenshots are self explanatory.</p>
<p><strong>The expected result:</strong></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/0806eaa741557b3e506d264cc3d9b71ff20b3317.jpeg" data-download-href="/uploads/short-url/190DAyrXiI3wZ89gzJvsXBlxVZ5.jpeg?dl=1" title="3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0806eaa741557b3e506d264cc3d9b71ff20b3317_2_690x370.jpeg" alt="3" data-base62-sha1="190DAyrXiI3wZ89gzJvsXBlxVZ5" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0806eaa741557b3e506d264cc3d9b71ff20b3317_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0806eaa741557b3e506d264cc3d9b71ff20b3317_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0806eaa741557b3e506d264cc3d9b71ff20b3317_2_1380x740.jpeg 2x" data-dominant-color="928DA5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3</span><span class="informations">1804×969 223 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f3c12c864988378faba06ced63c06d11d30ac1c.jpeg" data-download-href="/uploads/short-url/6JR99Od8N7Rxgjid8CewKas2NyI.jpeg?dl=1" title="4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2f3c12c864988378faba06ced63c06d11d30ac1c_2_690x373.jpeg" alt="4" data-base62-sha1="6JR99Od8N7Rxgjid8CewKas2NyI" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2f3c12c864988378faba06ced63c06d11d30ac1c_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2f3c12c864988378faba06ced63c06d11d30ac1c_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2f3c12c864988378faba06ced63c06d11d30ac1c_2_1380x746.jpeg 2x" data-dominant-color="9795B6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">4</span><span class="informations">1799×973 208 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><strong>The actual result:</strong></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a7b32fbf5f0cba53c88df9ea490da6cd1049245.jpeg" data-download-href="/uploads/short-url/8llE4ewFoXzzdfrD8CNeQTfLQAB.jpeg?dl=1" title="5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a7b32fbf5f0cba53c88df9ea490da6cd1049245_2_690x388.jpeg" alt="5" data-base62-sha1="8llE4ewFoXzzdfrD8CNeQTfLQAB" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a7b32fbf5f0cba53c88df9ea490da6cd1049245_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a7b32fbf5f0cba53c88df9ea490da6cd1049245_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a7b32fbf5f0cba53c88df9ea490da6cd1049245_2_1380x776.jpeg 2x" data-dominant-color="A8AAA9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">5</span><span class="informations">2560×1440 529 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54a396bd008434f2c3a58ca8e16207cf37f76a78.jpeg" data-download-href="/uploads/short-url/c4KASZxgmOgB0VUqntYmhwh4DzO.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/54a396bd008434f2c3a58ca8e16207cf37f76a78_2_690x388.jpeg" alt="1" data-base62-sha1="c4KASZxgmOgB0VUqntYmhwh4DzO" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/54a396bd008434f2c3a58ca8e16207cf37f76a78_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/54a396bd008434f2c3a58ca8e16207cf37f76a78_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/54a396bd008434f2c3a58ca8e16207cf37f76a78_2_1380x776.jpeg 2x" data-dominant-color="A8AAA9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">2560×1440 578 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83c0b4b0c658efb367a3326a307a162e8fcaeaab.jpeg" data-download-href="/uploads/short-url/iNxpYriST2oVWH6d6PelGA3nbmP.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/83c0b4b0c658efb367a3326a307a162e8fcaeaab_2_690x388.jpeg" alt="2" data-base62-sha1="iNxpYriST2oVWH6d6PelGA3nbmP" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/83c0b4b0c658efb367a3326a307a162e8fcaeaab_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/83c0b4b0c658efb367a3326a307a162e8fcaeaab_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/83c0b4b0c658efb367a3326a307a162e8fcaeaab_2_1380x776.jpeg 2x" data-dominant-color="A8A9AD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">2560×1440 534 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Should you need more information or screenshorts, please inform me.<br>
Any help from your side will be much appreciated!</p>
<p>Best,<br>
Cody</p>

---

## Post #2 by @lassoan (2021-03-27 18:49 UTC)

<aside class="quote no-group" data-username="Cody_Xie" data-post="1" data-topic="16789">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cody_xie/48/10261_2.png" class="avatar"> Cody_Xie:</div>
<blockquote>
<p>Export the DICOM-RT Structure to a obj file (since the DICOM_RT Structure cannot be use as an input nodes in Dynamic Model);</p>
</blockquote>
</aside>
<p>There is no need for file export and import. Instead, you can go to Data module, right-click on the segmentation, and choose “Export visible segments to model node”.</p>
<aside class="quote no-group" data-username="Cody_Xie" data-post="1" data-topic="16789">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cody_xie/48/10261_2.png" class="avatar"> Cody_Xie:</div>
<blockquote>
<p>The new clipped file is always invisible. I guess these four screenshots are self explanatory.</p>
</blockquote>
</aside>
<p>You can go to Data module and click on the eye icon of the original (non-clipped surface) to hide it.</p>

---

## Post #3 by @Cody_Xie (2021-03-27 18:58 UTC)

<p>Hi Andras,</p>
<p>many thanks for your help and support! I will try it under your guidance.</p>
<p>Have a nice weekend,<br>
Cody</p>

---

## Post #7 by @Cody_Xie (2021-03-27 22:11 UTC)

<p>Hi Andras,</p>
<p>many thanks for your support!</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="16789">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>There is no need for file export and import. Instead, you can go to Data module, right-click on the segmentation, and choose “Export visible segments to model node”.</p>
</blockquote>
</aside>
<p>This method works well!</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="16789">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can go to Data module and click on the eye icon of the original (non-clipped surface) to hide it.</p>
</blockquote>
</aside>
<p>However, this problem still exists. And I found that it was because the place of the Markups. Sometimes the ClippedRegion can be shown correctly, but if I move one of the Markups slightly, the ClippedRegion will becomes invisible again (please refer to the two screenshots below).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d949df6e7c88d1cf07f2fd7edb4d3523d2bc1d2.jpeg" data-download-href="/uploads/short-url/dlQOy3eY4dTyuQIlad0NCsNuewW.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d949df6e7c88d1cf07f2fd7edb4d3523d2bc1d2_2_690x388.jpeg" alt="1" data-base62-sha1="dlQOy3eY4dTyuQIlad0NCsNuewW" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d949df6e7c88d1cf07f2fd7edb4d3523d2bc1d2_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d949df6e7c88d1cf07f2fd7edb4d3523d2bc1d2_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d949df6e7c88d1cf07f2fd7edb4d3523d2bc1d2_2_1380x776.jpeg 2x" data-dominant-color="A6A8A6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">2560×1440 548 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2cd1097b78c74bc3ed11c63cf7f1bd4733a678d.jpeg" data-download-href="/uploads/short-url/pvKl1qdMkFs0m9SAUzYwEkREMtT.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b2cd1097b78c74bc3ed11c63cf7f1bd4733a678d_2_690x388.jpeg" alt="2" data-base62-sha1="pvKl1qdMkFs0m9SAUzYwEkREMtT" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b2cd1097b78c74bc3ed11c63cf7f1bd4733a678d_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b2cd1097b78c74bc3ed11c63cf7f1bd4733a678d_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b2cd1097b78c74bc3ed11c63cf7f1bd4733a678d_2_1380x776.jpeg 2x" data-dominant-color="A6A7A8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">2560×1440 541 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Do you know why this happens?</p>
<p>Many thanks in advance!</p>

---

## Post #8 by @lassoan (2021-03-28 14:37 UTC)

<p>Similarly to most other complex computational geometry algorithms that operate on polygonal meshes, this tool is somewhat sensitive to the quality of the input mesh and curve. If processing fails then you can do the following:</p>
<ul>
<li>improve input curve:
<ul>
<li>constrain the curve to the mesh: in Markups module/Curve settings, choose Curve type → Shortest distance on surface, Surface / Model node → the surface you wan to cut</li>
<li>resample the curve: in Markups module/Resample click Resample curve</li>
</ul>
</li>
<li>improve mesh quality (subdivide mesh if the original, mesh resolution is too coarse; remesh cells of the mesh are ill-shaped, etc.)</li>
</ul>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> do yo have any other suggestion?</p>

---

## Post #9 by @Cody_Xie (2021-03-28 18:16 UTC)

<p>Dear Andras,</p>
<p>thank you so much for your help and support!</p>

---

## Post #10 by @dimitris (2025-04-05 17:04 UTC)

<p>Dear Andras,</p>
<p>I am trying to work with ‘Curve cut’ option of ‘dynamic modeler’ module in python. The workflow I follow are: Import a stl model, Fill it, Decimate it, Draw a closed curve which is resampled and then constrained it to the model, Add a fiducial on the inside area.<br>
Next I try to work with ‘Curve cut’ option. Using the above inputs, in the GUI of 3D Slicer, everything goes fine and both models(positive and negative) are generated.<br>
But after running the code I get no points for both.<br>
What am I doing wrong? Can you help?<br>
Here is the code:<br>
<span class="hashtag-raw">#1</span>.Fill the scan Model</p>
<p>def fill_holes_in_model(modelNode, holeSize=1000.0):<br>
“”"<br>
Fills holes in the input modelNode using vtkFillHolesFilter.<br>
:param modelNode: vtkMRMLModelNode<br>
:param holeSize: Maximum hole size to fill (in mm^2)<br>
:return: New vtkMRMLModelNode with holes filled<br>
“”"<br>
polyData = modelNode.GetPolyData()</p>
<pre><code>fillHoles = vtk.vtkFillHolesFilter()
fillHoles.SetInputData(polyData)
fillHoles.SetHoleSize(holeSize)
fillHoles.Update()

filledModel = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode", modelNode.GetName() + "_FilledModel")
filledModel.SetAndObservePolyData(fillHoles.GetOutput())

filledDisplay = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelDisplayNode")
slicer.mrmlScene.AddNode(filledDisplay)
filledModel.SetAndObserveDisplayNodeID(filledDisplay.GetID())
filledDisplay.Copy(modelNode.GetDisplayNode())

return filledModel
</code></pre>
<p>originalModel = slicer.util.getNode(“patientX_scan”)<br>
filledModel = fill_holes_in_model(originalModel, holeSize=1000.0)</p>
<p><span class="hashtag-raw">#2</span>. Decimate the filled model</p>
<p>inputModel = slicer.util.getNode(‘patientX_scan_FilledModel’)</p>
<p>inputPolyData = inputModel.GetPolyData()</p>
<p>decimateFilter = vtk.vtkDecimatePro()<br>
decimateFilter.SetTargetReduction(0.5)  # This will reduce the number of polygons by 50%<br>
decimateFilter.SetInputData(inputPolyData)<br>
decimateFilter.PreserveTopologyOn()  # Preserve topology to avoid self-intersections<br>
decimateFilter.Update()</p>
<p>simplifiedPolyData = decimateFilter.GetOutput()</p>
<p>outputModel = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLModelNode’, ‘DecimatedModel’)<br>
outputModel.SetAndObservePolyData(simplifiedPolyData)</p>
<p>outputModel.CreateDefaultDisplayNodes()</p>
<p>outputModel.GetDisplayNode().SetVisibility(True)</p>
<p><span class="hashtag-raw">#3</span>. Respample the closed Curve</p>
<p>slicer.util.getNode(‘CC’).ResampleCurveWorld(0.5)</p>
<p><span class="hashtag-raw">#4</span>. Constrain the closed curve to the model</p>
<p>curveNode = slicer.util.getNode(‘CC’)  # Closed curve node<br>
surfaceNode = slicer.util.getNode(‘DecimatedModel’)  # Model to constrain to</p>
<p>curveNode.SetCurveTypeToShortestDistanceOnSurface()</p>
<p>curveNode.SetAndObserveShortestDistanceSurfaceNode(surfaceNode)</p>
<p><span class="hashtag-raw">#5</span>. Trying to Curve cut in Dynamic Modeler</p>
<p>inputModel = slicer.util.getNode(‘DecimatedModel’)<br>
inputCurve = slicer.util.getNode(‘CC’)<br>
insidePoint = slicer.util.getNode(‘F’)</p>
<p>outputPositive = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLModelNode”, “CutModel_Positive”)<br>
outputPositive.CreateDefaultDisplayNodes()<br>
outputNegative = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLModelNode”, “CutModel_Negative”)<br>
outputNegative.CreateDefaultDisplayNodes()</p>
<p>modelerNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLDynamicModelerNode”)<br>
modelerNode.SetToolName(“Curve cut”)<br>
modelerNode.SetNodeReferenceID(“InputModel”, inputModel.GetID())<br>
modelerNode.SetNodeReferenceID(“InputCurve”, inputCurve.GetID())<br>
modelerNode.SetNodeReferenceID(“InsidePoint”, insidePoint.GetID())<br>
modelerNode.SetNodeReferenceID(“OutputPositiveModel”, outputPositive.GetID())<br>
modelerNode.SetNodeReferenceID(“OutputNegativeModel”, outputNegative.GetID())</p>
<p>modelerNode.SetAttribute(“StraightCut”, “true”)<br>
modelerNode.SetAttribute(“Operation”,  “Split”)<br>
modelerNode.SetAttribute(“InsideSurface”, “true”)<br>
modelerNode.SetAttribute(“OutsideSurface”, “true”)</p>
<p>slicer.modules.dynamicmodeler.logic().RunDynamicModelerTool(modelerNode)<br>
slicer.app.processEvents()</p>
<p>outputPositive.GetDisplayNode().SetVisibility(1)<br>
outputNegative.GetDisplayNode().SetVisibility(1)</p>
<p>print(“Positive output points:”, outputPositive.GetMesh().GetNumberOfPoints() if outputPositive.GetMesh() else 0)<br>
print(“Negative output points:”, outputNegative.GetMesh().GetNumberOfPoints() if outputNegative.GetMesh() else 0)</p>
<p>And here is the Output:<br>
Positive output points: 0<br>
Negative output points: 0</p>
<p>Thanks!!</p>

---

## Post #11 by @dimitris (2025-04-10 17:51 UTC)

<p>Hi ,</p>
<p>Finally, I found the solution in the following videos:</p>
<ol>
<li>Extract one side of a closed surface mesh</li>
</ol>
<div class="youtube-onebox lazy-video-container" data-video-id="nLva95ZF4ko" data-video-title="Extract one side of a closed surface mesh" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=nLva95ZF4ko" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/nLva95ZF4ko/maxresdefault.jpg" title="Extract one side of a closed surface mesh" width="690" height="388">
  </a>
</div>

<ol start="2">
<li>Drawing curves on surface mesh</li>
</ol>
<div class="youtube-onebox lazy-video-container" data-video-id="UeGhzSGUZOA" data-video-title="Drawing curves on surface mesh" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=UeGhzSGUZOA" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/UeGhzSGUZOA/maxresdefault.jpg" title="Drawing curves on surface mesh" width="690" height="388">
  </a>
</div>


---
