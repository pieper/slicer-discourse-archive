# Coloring individual triangles in triangulated surface model of segmentation

**Topic ID**: 10279
**Date**: 2020-02-15
**URL**: https://discourse.slicer.org/t/coloring-individual-triangles-in-triangulated-surface-model-of-segmentation/10279

---

## Post #1 by @ifried01 (2020-02-15 18:22 UTC)

<p>Hi Everyone,</p>
<p>I am wondering if it is possible to color individual triangles in the triangulated surface model of a segmentation? In other words, when I click “w” in Slicer and I see my segmentation as a triangulated mesh, can I color individual triangles.</p>
<p>Thanks</p>
<p>Operating system: OSX<br>
Slicer version: 4.10.2</p>

---

## Post #2 by @lassoan (2020-02-15 18:32 UTC)

<p>There is an example in the script repository does exactly this: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Select_cells_of_a_model_using_markups_fiducial_points">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Select_cells_of_a_model_using_markups_fiducial_points</a></p>

---

## Post #3 by @ifried01 (2020-02-16 19:47 UTC)

<p>Thank you very much for the quick response. I am taking a look through the example and will post if I have any questions</p>
<p>Thanks!</p>

---

## Post #4 by @ifried01 (2020-02-17 17:20 UTC)

<p>Thanks again for the pointer, I got the code to work (I had to switch to 4.11 for the “arrayFromMarkupsControlPoints” functionality).</p>
<p>I am playing around with SegmentMesher and the Models module, but am having difficulty reducing the mesh to just be the actual segmented object as opposed to a rectangle encompassing it. Is there any way to get the mesh to actually be on the airway like in the second image (obtained by pressing ‘w’ in the 3D view).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50f974efa9ab76c339104a04daf113c795b7947f.png" data-download-href="/uploads/short-url/bykEGUXbgFw5bCtfCRMl24SwmOH.png?dl=1" title="Screenshot from 2020-02-17 12-15-39" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/50f974efa9ab76c339104a04daf113c795b7947f_2_690x420.png" alt="Screenshot from 2020-02-17 12-15-39" data-base62-sha1="bykEGUXbgFw5bCtfCRMl24SwmOH" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/50f974efa9ab76c339104a04daf113c795b7947f_2_690x420.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/50f974efa9ab76c339104a04daf113c795b7947f_2_1035x630.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/50f974efa9ab76c339104a04daf113c795b7947f_2_1380x840.png 2x" data-dominant-color="959769"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-02-17 12-15-39</span><span class="informations">1934×1178 254 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0dcdf0ddacf52c1800e943fcfddf665777aa6200.png" data-download-href="/uploads/short-url/1Y7qS4wq4xjPs7Kr7aAm99wI7pm.png?dl=1" title="Screenshot from 2020-02-17 12-17-53" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0dcdf0ddacf52c1800e943fcfddf665777aa6200_2_690x419.png" alt="Screenshot from 2020-02-17 12-17-53" data-base62-sha1="1Y7qS4wq4xjPs7Kr7aAm99wI7pm" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0dcdf0ddacf52c1800e943fcfddf665777aa6200_2_690x419.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0dcdf0ddacf52c1800e943fcfddf665777aa6200_2_1035x628.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0dcdf0ddacf52c1800e943fcfddf665777aa6200_2_1380x838.png 2x" data-dominant-color="656880"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-02-17 12-17-53</span><span class="informations">1954×1189 833 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks!</p>

---

## Post #5 by @lassoan (2020-02-18 01:59 UTC)

<p>A background mesh is often very useful because you can simulate embedding of the object in another material, but if you don’t need then then enable “Cleaver remove background mesh” option in Advanced section.</p>

---

## Post #6 by @ifried01 (2020-02-19 20:28 UTC)

<p>Thank you, that’s exactly what I was looking for</p>

---

## Post #7 by @ifried01 (2020-02-26 15:29 UTC)

<p>Thanks again for the previous help. I am now able to get cell identifiers for triangles on the surface mesh and color them / their neighbors.</p>
<p>I have no issues when the markup point is outside the mesh or on the exterior surface, but I am unsuccessful when the markup is slightly inside the surface mesh. I have experimented with hollowing out the segmentation before generating the model, but that has not solved the issue.</p>
<p>Based on my experiments, it looks like the surface mesh is not only on the surface. If this is the case, is there a way to always/only get triangles on the exterior surface using cell.FindClosestPoint? The 1st image below identifies a cell with two internal vertices as the closest cell to MarkupsFiducial_1.</p>
<p>Additionally, is the mesh not actually a triangle mesh? Each cell has a 4th vertex which seems to be internal to the surface (2nd image below).</p>
<p>I apologize if the screenshots are difficult to interpret in 2D. Let me know if I can clarify anything.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd64f25e1c81035c6d0ba73baa5f93bcfe3a8149.png" data-download-href="/uploads/short-url/tj09QDbSYwBgapg87XNxcpEYcWd.png?dl=1" title="Screenshot from 2020-02-26 10-05-42" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd64f25e1c81035c6d0ba73baa5f93bcfe3a8149.png" alt="Screenshot from 2020-02-26 10-05-42" data-base62-sha1="tj09QDbSYwBgapg87XNxcpEYcWd" width="636" height="500" data-dominant-color="8D7DA4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-02-26 10-05-42</span><span class="informations">1309×1029 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f2cb0e4d30ce8376e44fca2616469fdedb77261.png" data-download-href="/uploads/short-url/mI7Fp3EcgHgbWCtLi148KHA97Oh.png?dl=1" title="Screenshot from 2020-02-26 10-08-21" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9f2cb0e4d30ce8376e44fca2616469fdedb77261_2_690x367.png" alt="Screenshot from 2020-02-26 10-08-21" data-base62-sha1="mI7Fp3EcgHgbWCtLi148KHA97Oh" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9f2cb0e4d30ce8376e44fca2616469fdedb77261_2_690x367.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9f2cb0e4d30ce8376e44fca2616469fdedb77261_2_1035x550.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9f2cb0e4d30ce8376e44fca2616469fdedb77261_2_1380x734.png 2x" data-dominant-color="A32832"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-02-26 10-08-21</span><span class="informations">1945×1037 938 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here is the code I used to identify cells and vertices:</p>
<pre><code>meshModelNode        = slicer.util.getNode('Model_1')
selectionArray, cell = initializeMeshArray(meshModelNode)
markupsNode          = slicer.util.getNode('MarkupsFiducial')
markupPoints         = slicer.util.arrayFromMarkupsControlPoints(markupsNode)
markupIndex          = 0
markupPoint          = markupPoints[markupIndex]
# find the closest cell to markupPoint
closestPoint = [0.0, 0.0, 0.0]
cellObj      = vtk.vtkGenericCell()
cellId       = vtk.mutable(0)
subId        = vtk.mutable(0)
dist2        = vtk.mutable(0.0)
cell.FindClosestPoint(markupPoint, closestPoint, cellObj, cellId, subId, dist2)
# find the number of vertices for the cell (output is 4)
cellObj.GetPoints().GetData().GetNumberOfTuples()
# find the vertex RAS coordinates
np.array(cellObj.GetPoints().GetData().GetTuple(0) + cellObj.GetPoints().GetData().GetTuple(1) + cellObj.GetPoints().GetData().GetTuple(2) + cellObj.GetPoints().GetData().GetTuple(3)).reshape(4,3)
# output is array([[ 43.90499878,   9.22570038, -78.88699341],
                   [ 44.46899414,   9.83119965, -79.45799255],
                   [ 44.1309967 ,   8.99890137, -79.11399841],
                   [ 43.90499878,   9.22570038, -79.48599243]])
</code></pre>

---

## Post #8 by @ifried01 (2020-02-26 19:12 UTC)

<p>I am guessing that triangles are 3D objects in the mesh, hence the 4th vertex, which would be the answer to my second question from the previous post. If that’s true, my updated question is if its possible to only consider the 2D triangle objects that reside on the exterior surface?</p>

---

## Post #9 by @lassoan (2020-02-26 19:28 UTC)

<p>Segment mesher creates a volumetric mesh, so you have tetrahedral elements (defined by 4 points). You get a surface mesh (with triangle elements) when you exporting the segment to a model using Segmentations module.</p>

---

## Post #10 by @ifried01 (2020-02-26 22:58 UTC)

<p>perfect, thank you very much</p>

---
