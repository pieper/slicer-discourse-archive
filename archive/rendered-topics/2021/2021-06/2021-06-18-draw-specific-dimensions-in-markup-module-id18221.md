---
topic_id: 18221
title: "Draw Specific Dimensions In Markup Module"
date: 2021-06-18
url: https://discourse.slicer.org/t/18221
---

# Draw specific dimensions in markup module

**Topic ID**: 18221
**Date**: 2021-06-18
**URL**: https://discourse.slicer.org/t/draw-specific-dimensions-in-markup-module/18221

---

## Post #1 by @Aep93 (2021-06-18 19:16 UTC)

<p>Hello all,<br>
How can I use the markup module to draw closed shapes with specific dimensions? Such as a circle with a specific radius, or a rectangle with a specific width/height?<br>
Thanks in advance.</p>

---

## Post #2 by @lassoan (2021-06-18 21:15 UTC)

<p>There are many different approaches to implement this (use Create Models module in SlicerIGT extension, <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#define-edit-a-circular-region-of-interest-in-a-slice-viewer">write a few lines of Python code</a>, constrain markups ROI size, etc.). What would you like to achieve?</p>

---

## Post #3 by @Aep93 (2021-06-18 21:49 UTC)

<p>Thanks for your response <a class="mention" href="/u/lassoan">@lassoan</a>. Create Models module is for creating models, however, I want some closed curves, not models.<br>
I want to use these curves to assign a different label to a specific part of my model as I mentioned <a href="https://discourse.slicer.org/t/assign-label-to-selected-parts-of-a-surface-model/18210">here</a>.<br>
However, I want my curve to have a specific shape with exact dimensions.</p>

---

## Post #4 by @lassoan (2021-06-18 22:10 UTC)

<p>You can certainly use markups to place labels on a model, but those would be just markups fiducials. How do you plan to use a closed curve for labeling?</p>

---

## Post #5 by @Aep93 (2021-06-18 23:14 UTC)

<p>In fact, I want to choose a specific region ( that is a closed region such as a circle with a specific radius or a rectangle with a specific width/height) on my surface model, so that I can assign a label to that region in the next step.</p>

---

## Post #6 by @lassoan (2021-06-18 23:49 UTC)

<p>Cutting out a region from a surface using closed curve should work well and (in recent Slicer Preview releases) you can enable display of the node name on the curve. So, I think you should be all set.</p>
<p>By “drawing closed shapes with specific dimensions” do you mean you would like to set an absolute size for the markup control point? You can do that by clicking the “absolute” button in Markups module / Display / Glyph size.</p>

---

## Post #7 by @Aep93 (2021-06-19 01:29 UTC)

<p>Thanks for your response <a class="mention" href="/u/lassoan">@lassoan</a>.<br>
Yes, I can cut the surface as you mentioned and I am OK with it. My only problem now is the closed curve that I create in the Markups module. I want that closed curve to have a specific shape with a specific dimension (such as a circle with a specific radius).<br>
So my main question is this:<br>
How can I draw a circle with a specific radius using the Markup module?</p>
<p>I changed the glyph size that you mentioned, however, it seems that it only changes the size of the marker which is not what I want.</p>

---

## Post #8 by @lassoan (2021-06-19 02:16 UTC)

<p>If you want to cut with a specific shape then it is probably better to create that shape as a model with known dimensions, use transforms widget to move/rotate it, and cut with that (using Combine models module or Segment Editor).</p>

---

## Post #9 by @Aep93 (2021-06-20 16:18 UTC)

<p>Thanks for your response <a class="mention" href="/u/lassoan">@lassoan</a>. It is a good suggestion, however, I cannot use the segment editor for this aim. Because as I mentioned my current model is a surface (not a volume) and I found that segment editor cannot deal with intersecting a volumetric mode (such as a cube) with a surface. I am trying to Combine Models module that you mentioned, however, I cannot find it. Is it under another module?</p>

---

## Post #10 by @lassoan (2021-06-20 19:25 UTC)

<p>Combine models is available if you install Sandbox extension.</p>

---

## Post #11 by @Aep93 (2021-06-21 03:42 UTC)

<p>Thanks for your response <a class="mention" href="/u/lassoan">@lassoan</a>. I installed the Combine Models module. Also, I created a cube model with the Create Models module (green cube in the picture) and I want to find its intersection with my own model (which is a surface model and is the yellow model in the picture). However, when I do it in the Combine Models modules, the created model is empty. Do you have any suggestions on how to solve the problem?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15552251eeef6c37e50a9280f28747d3f83868e6.png" data-download-href="/uploads/short-url/32IqoEkuy3gMIeZX9Wp2YVEO3Bk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15552251eeef6c37e50a9280f28747d3f83868e6_2_690x206.png" alt="image" data-base62-sha1="32IqoEkuy3gMIeZX9Wp2YVEO3Bk" width="690" height="206" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15552251eeef6c37e50a9280f28747d3f83868e6_2_690x206.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15552251eeef6c37e50a9280f28747d3f83868e6_2_1035x309.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15552251eeef6c37e50a9280f28747d3f83868e6_2_1380x412.png 2x" data-dominant-color="95A09D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1833×548 85.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @lassoan (2021-06-21 03:53 UTC)

<p>Combine models module is for combining closed surfaces. Is the yellow model a closed surface?</p>
<p>Boolean operations are only feasible if the inputs do not have any non-manifold edges. How was they yellow model generated?</p>
<p>Create models module creates a cube with minimum number of triangles, which may result in extremely complex computations. You would probably get better results by subdividing the green model.</p>

---

## Post #13 by @Aep93 (2021-06-21 04:06 UTC)

<p>Thanks for your response <a class="mention" href="/u/lassoan">@lassoan</a>. The yellow model is a surface that was cut from another model.<br>
As far as I understood, I should use Combine Models module to find the intersection before I cut that surface. Is this correct?<br>
If yes, when I find the intersection before cutting the surface, there will be some other intersections of the green cube with other parts of the model that are not my interest. How can I delete those parts and only keep the part the lays on the yellow surface?</p>

---

## Post #14 by @lassoan (2021-06-21 04:08 UTC)

<aside class="quote no-group" data-username="Aep93" data-post="13" data-topic="18221">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aep93/48/5990_2.png" class="avatar"> Aep93:</div>
<blockquote>
<p>The yellow model is a surface that was cut from another model.</p>
</blockquote>
</aside>
<p>Combine models module is for combining closed surfaces. Is the yellow model a closed surface (a watertight surface that encloses non-zero-volume region inside)?</p>

---

## Post #15 by @Aep93 (2021-06-21 05:53 UTC)

<p>No, the yellow model is not a closed surface. I cut it from another closed surface model. However, the resulted surface (that is the yellow surface) is not a closed surface.</p>

---

## Post #16 by @lassoan (2021-06-21 11:47 UTC)

<p>Combine models is for Boolean operations on closed surfaces, so it is not applicable.</p>
<p>You can cut out a rectangular region from an open surface using Dynamic modeler module’s Clip with ROI tool. This tool is available in recent Slicer Preview Releases and you need to use Markups ROI as input.</p>

---

## Post #17 by @Aep93 (2021-06-21 14:47 UTC)

<p>Thanks for your response <a class="mention" href="/u/lassoan">@lassoan</a>. The dynamic Modeler module was the first thing I tried, however, the problem with it is that I cannot create specific closed curves with a specific dimension (such as a circle with a specific radius) with the markup module so that I can use it in the Dynamic modeler module.</p>

---

## Post #18 by @lassoan (2021-06-21 14:51 UTC)

<p>You only use the ROI for markups module. You can create the model using Markups to Model, Create Models, etc. modules or <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-a-simple-surface-mesh-as-a-model-node">directly using VTK filters</a>.</p>

---

## Post #19 by @Aep93 (2021-06-21 15:13 UTC)

<p>Sorry, <a class="mention" href="/u/lassoan">@lassoan</a>. I think did not completely understand your explanation. I already use the Markups modules for creating the closed curve and (I am not sure whether I use ROI or not). Is it possible to draw the shapes that I want in the Markups module?</p>

---

## Post #20 by @lassoan (2021-06-21 15:43 UTC)

<p>You can use Markups module for specifying the clipping ROI box (specify size numerically and/or modify the size/position/orientation in viewers).</p>
<p>You can also use markups to draw shapes (line, curve, plane, box) and by using Markups to Model module you can also draw a curved closed surface. You can also bring in Create models, Segment Editor, etc. - there are many tools and you can use them in many combinations.</p>
<p>Please describe your complete modeling workflow and then we may be able to provide more specific advice.</p>

---

## Post #21 by @Aep93 (2021-06-21 20:25 UTC)

<p>Thanks for your response <a class="mention" href="/u/lassoan">@lassoan</a>.<br>
These are the steps that I want to follow:<br>
Initially, I have a surface model that is closed. I cut a surface from that model and this new open surface model is what I want to study.<br>
I want to select a specific region (a circle with a specific radius) on this open surface model and assign a different label to this region.<br>
I appreciate your help.</p>

---

## Post #22 by @lassoan (2021-06-21 21:23 UTC)

<aside class="quote no-group" data-username="Aep93" data-post="21" data-topic="18221">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aep93/48/5990_2.png" class="avatar"> Aep93:</div>
<blockquote>
<p>I want to select a specific region (a circle with a specific radius) on this open surface model and assign a different label to this region.</p>
</blockquote>
</aside>
<p>Do you want to label the points or cells? What is the preferred behavior at the boundary (subdivide boundary cells to make the intersection boundary smooth; or keep the original cells and have crinkled boundary)? Do you want to measure the distance on the surface or simple Euclidean distance in 3D space?</p>
<p>What are you going to do with the result? Just color it differently or remove cells that are farther away? If you remove cells then do you need to keep the original point and cell IDs?</p>

---

## Post #23 by @Aep93 (2021-06-21 21:29 UTC)

<p>Thanks for your response <a class="mention" href="/u/lassoan">@lassoan</a>.<br>
I want to label cells. In the intersection region, I want to keep the original cell and have a crinkled boundary.<br>
I think I did not understand what you mean by measuring the distances. However, I want to fit a closed circular curve with a specific radius to this surface and then assign a different label to cells inside it.<br>
The purpose: I want to use these areas with different labels in my FEM analysis in the next steps. Also, I want to keep both regions outside, and inside of the circular curve. However, I do not need to keep the original cell IDs.</p>

---

## Post #24 by @lassoan (2021-06-21 23:01 UTC)

<p>You can create a “region” cell array like this:</p>
<pre><code class="lang-python">centerFid = getNode('F')
modelNode = getNode('MyModel')
distance = 15.0

# Create an array that contains the distances from the chosen center point
import numpy as np
centerPos = centerFid.GetNthControlPointPositionVector(0)
coords = slicer.util.arrayFromModelPoints(modelNode)
vectorsToCenter = coords - centerPos
distances = np.linalg.norm(vectorsToCenter, axis=1)

# Create a new "region" point data array that contains the region ID
regionArrayVtk = vtk.vtkDoubleArray()
regionArrayVtk.SetName('region')
regionArrayVtk.SetNumberOfValues(len(distances))
modelNode.GetPolyData().GetPointData().AddArray(regionArrayVtk)
regionArray = slicer.util.arrayFromModelPointData(modelNode, 'region')
regionArray[distances&lt;distance] = 0.0
regionArray[distances&gt;=distance] = 1.0
slicer.util.arrayFromModelPointDataModified(modelNode, 'region')  # indicate that we finished with the updates

# Visualize "region" point data
modelNode.GetDisplayNode().SetActiveScalar("region", vtk.vtkAssignAttribute.POINT_DATA)
modelNode.GetDisplayNode().SetAndObserveColorNodeID('vtkMRMLColorTableNodeFileViridis.txt')
modelNode.GetDisplayNode().SetScalarVisibility(True)

# Create cell data from "region" array
toCellData = vtk.vtkPointDataToCellData()
toCellData.SetInputData(modelNode.GetPolyData())
toCellData.PassPointDataOn()
toCellData.Update()
modelNode.SetAndObservePolyData(toCellData.GetOutput())
</code></pre>

---

## Post #25 by @pieper (2021-06-21 23:08 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> looks like theres a missing piece of the script just before the third from the last line.</p>

---

## Post #26 by @lassoan (2021-06-21 23:10 UTC)

<aside class="quote no-group" data-username="pieper" data-post="25" data-topic="18221">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>looks like theres a missing piece of the script just before the third from the last line.</p>
</blockquote>
</aside>
<p>Thank you, fixed. It was just an incompletely removed commented out line.</p>

---

## Post #27 by @Aep93 (2021-06-22 00:50 UTC)

<p>Thanks for the code <a class="mention" href="/u/lassoan">@lassoan</a>. It works great. However, I have two problems:</p>
<ol>
<li>
<p>When I run the code, the region is selected and appears in a different color. However, how can I export this region to a new model?</p>
</li>
<li>
<p>The code runs without error when the surface is closed. However, when I try it with an open surface (that is my interest) I get an error when I write the following part of the code:</p>
</li>
</ol>
<pre><code class="lang-auto">coords = slicer.util.arrayFromModelPoints(modelNode)
</code></pre>
<p>and the error is this:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "/home/user/Slicer-4.11.20210226-linux-amd64/bin/Python/slicer/util.py", line 1477, in arrayFromModelPoints
    pointData = modelNode.GetPolyData().GetPoints().GetData()
AttributeError: 'NoneType' object has no attribute 'GetPoints'
</code></pre>
<p>I greatly appreciate it if you can help me solve these two problems.</p>

---

## Post #28 by @lassoan (2021-06-22 02:57 UTC)

<aside class="quote no-group" data-username="Aep93" data-post="27" data-topic="18221">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aep93/48/5990_2.png" class="avatar"> Aep93:</div>
<blockquote>
<p>When I run the code, the region is selected and appears in a different color. However, how can I export this region to a new model?</p>
</blockquote>
</aside>
<p>It is saved in the model when you use a suitable format, such as VTK, VTP/VTU. For example, FEBio studio can read such files directly. Other software may not be able to read VTK file formats, so you need to convert to a suitable one, for example by using meshio Python package.</p>
<blockquote>
<p>The code runs without error when the surface is closed. However, when I try it with an open surface (that is my interest) I get an error when I write the following part of the code</p>
</blockquote>
<p>Good catch. We should replace <code>GetPolyData</code> by <code>GetMesh</code> in that file. You can make this change locally on your computer (just change the .py file, save it, and restart Slicer).</p>

---

## Post #29 by @Aep93 (2021-06-22 03:48 UTC)

<p>Thanks for your response <a class="mention" href="/u/lassoan">@lassoan</a>. I have to use meshio to convert the vtk file to the format that I want. The problem is this: now I can only export my model to vtk (polydata). However, it seems that meshio only reads vtk unstructured grid. How can I convert my polydata vtk to unstructured data vtk?</p>
<p>Also, I replaced the code as you mentioned in my computer, however, I still get the same error:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; coords = slicer.util.arrayFromModelPoints(modelNode)
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "/home/user/Slicer-4.11.20210226-linux-amd64/bin/Python/slicer/util.py", line 1477, in arrayFromModelPoints
    pointData = modelNode.GetMesh().GetPoints().GetData()
AttributeError: 'NoneType' object has no attribute 'GetPoints'
</code></pre>
<p>Your help is greatly appreciated.</p>

---

## Post #30 by @lassoan (2021-06-22 04:28 UTC)

<p>You can copy the points and cells of a polydata into an unstructured grid but maybe the meshio has problems with polygon cells. You can try to save as OBJ and PLY, too, and see what point/cell data arrays are preserved.</p>
<p>If <code>GetMesh()</code> returns <code>None</code> then most likely the model node is empty (are you sure you get the correct node from the scene?).</p>

---

## Post #31 by @Aep93 (2021-06-22 21:57 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a>. I will work more on the vtk format later. However, now I think I should get the code to work first. I tried several times, however, I still get that error related to the GetPoints for the opne surface model. This is what I do:<br>
I create a point using the Markups module (the point F in the code you sent me) and then I use your code. I do not think the problem is related to this point. Because, in my closed surface model, the code runs even when the point F is outside of the model.<br>
Can you please tell me how can I make sure whether I get the correct node from the scene?</p>

---

## Post #32 by @lassoan (2021-06-22 22:08 UTC)

<p>Can you save your scene in mrb file format, upload it somewhere and post the link here? Also copy here the Python script that you are executing.</p>

---

## Post #33 by @Aep93 (2021-06-22 22:46 UTC)

<p>Thanks for your response <span class="mention">@lassoan.I</span> tried several times again and eventually, I found that the problem is solved. I could not understand what was my mistake in the previous runs, however, it is working now.<br>
My only problem right now is the detection of the label. I found that vtk format can preserve this information. I say this because when I open the vtk file in a new slicer window and go to the Models module, I see that number of point scalars is equal to 2 and I assume that this means the region is saved in the file.<br>
Are these regions same as labels now? How can I assign each region to a new model/segmentation?<br>
I have uploaded one of my vtk models <a href="https://github.com/A-ep93/slicertest2/blob/main/finaluns.vtk" rel="noopener nofollow ugc">here</a>.<br>
Thanks in advance.</p>

---

## Post #34 by @lassoan (2021-06-22 23:05 UTC)

<p>You can use vtkThreshold filter to extract a part of the mesh based on point or cell scalar value.</p>

---

## Post #35 by @Aep93 (2021-06-22 23:46 UTC)

<p>Thanks for your response <a class="mention" href="/u/lassoan">@lassoan</a>. I am searching for it now, I just wanted to know whether you have any specific example in mind does the same thing or a similar task?</p>

---

## Post #36 by @lassoan (2021-06-23 00:09 UTC)

<p>There are tons of VTK Examples on the web. You can get the vtkPolyData object from the model node by calling <code>GetMesh()</code> method, then run the VTK filters, and then call <code>slicer.modules.models.logic().AddModel(...)</code> method to add a new model from the filter output.</p>

---

## Post #37 by @Aep93 (2021-06-23 15:53 UTC)

<p>Thanks for your response <a class="mention" href="/u/lassoan">@lassoan</a>. I got this code based on my search:</p>
<pre><code class="lang-auto">SMesh=getNode('Model').GetMesh()
tfil=vtk.vtkThreshold()
tfil.SetInputData(SMesh)
tfil.SetInputArrayToProcess(0, 0, 0, vtk.vtkDataObject.FIELD_ASSOCIATION_CELLS, vtk.vtkDataSetAttributes.SCALARS );
tfil.ThresholdByLower( 1 )
tfil.Update()
slicer.modules.models.logic().AddModel(tfil.GetOutput())


</code></pre>
<p>However, I get an error in the last step. Can you please let me know what is the problme with my code?<br>
<a href="https://github.com/A-ep93/slicertest2/blob/main/finaluns.vtk" rel="noopener nofollow ugc">This</a> is my sample as well.<br>
Thanks in advance,</p>

---

## Post #38 by @lassoan (2021-06-23 15:54 UTC)

<p>Without seeing the error message I have no chance of guessing what could go wrong.</p>

---

## Post #39 by @Aep93 (2021-06-23 15:55 UTC)

<p>This is the error:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
TypeError: arguments do not match any overloaded methods
</code></pre>
<p>Thanks</p>

---

## Post #40 by @Aep93 (2021-06-23 21:00 UTC)

<p>I managed to get two different models using the following code:</p>
<pre><code class="lang-auto">meshNode = getNode('Model')
mesh = meshNode.GetMesh()
cellData = mesh.GetCellData()
labelsRange = cellData.GetArray("region").GetRange()
for labelValue in range(int(labelsRange[0]), int(labelsRange[1]+1)):
    threshold = vtk.vtkThreshold()
    threshold.SetInputData(mesh)
    threshold.SetInputArrayToProcess(0, 0, 0, vtk.vtkDataObject.FIELD_ASSOCIATION_CELLS, "region")
    threshold.ThresholdBetween(labelValue, labelValue)
    threshold.Update()
    if threshold.GetOutput().GetNumberOfPoints() &gt; 0:
        modelNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode", "{0}_{1}".format(meshNode.GetName(), labelValue))
        modelNode.SetAndObserveMesh(threshold.GetOutput())
        modelNode.CreateDefaultDisplayNodes()

</code></pre>
<p>However, as shown in the picture below, a part of the main model near the region that I had chosen does not exist in the created models. What is the reason for this?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84a9002de42cc947057faf7c9c566bb99ed29f27.jpeg" data-download-href="/uploads/short-url/iVz6INOSu2xad99vwrlJYef7LF5.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/84a9002de42cc947057faf7c9c566bb99ed29f27_2_690x329.jpeg" alt="image" data-base62-sha1="iVz6INOSu2xad99vwrlJYef7LF5" width="690" height="329" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/84a9002de42cc947057faf7c9c566bb99ed29f27_2_690x329.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/84a9002de42cc947057faf7c9c566bb99ed29f27_2_1035x493.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84a9002de42cc947057faf7c9c566bb99ed29f27.jpeg 2x" data-dominant-color="4C8940"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1037×495 87.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Also, I do not know why the color of my model changes to this rainbow-like colorand I cannot change it in the slicer.<br>
My main model is <a href="https://github.com/A-ep93/slicertest2/blob/main/finaluns.vtk" rel="noopener nofollow ugc">This</a>.</p>

---

## Post #41 by @lassoan (2021-06-25 17:59 UTC)

<p>This looks good. The missing region is due to how you specify the threshold range - you need to pay attention to cells that have points above and below the threshold value. Probably the simplest is to call threshold filter twice: first with <code>InvertOff()</code> then with <code>InvertOn()</code>.</p>

---
