# Get cell data of a mesh at selected point positions

**Topic ID**: 8859
**Date**: 2019-10-22
**URL**: https://discourse.slicer.org/t/get-cell-data-of-a-mesh-at-selected-point-positions/8859

---

## Post #1 by @Saima (2019-10-22 01:28 UTC)

<p>Hi Andras,<br>
I have data points and want to map it on a brain mesh to get the cell values of brain mesh at data points. how can I do it. any suggestions?</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #2 by @lassoan (2019-10-22 13:17 UTC)

<p>You can use a vtkCellLocator to get closest point to each data point and then get the cell value from cell ID as shown in this example: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_scalar_values_at_surface_of_a_model" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_scalar_values_at_surface_of_a_model</a></p>

---

## Post #3 by @Saima (2019-11-05 05:55 UTC)

<p>Hi Andras,<br>
I am using the findcell based on fiducial points to select the cells but there are less number of cells selected as compared to fiducial points. I need all cells for each fiducial and nearby cells as well of the mesh. How would i be able to get this. any idea.</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>
<p>as in the image below you can see only few cells are selected.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fac33aa560e11ee297f0a797aefea041a5f0ff40.png" data-download-href="/uploads/short-url/zMlDVxcOCDP3diEPzSjKz7GTjhe.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fac33aa560e11ee297f0a797aefea041a5f0ff40.png" alt="image" data-base62-sha1="zMlDVxcOCDP3diEPzSjKz7GTjhe" width="690" height="434" data-dominant-color="4A2A61"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">737×464 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2019-11-05 14:16 UTC)

<p>The script that I’ve linked above works very robustly for me. If you can save your scene in a .mrb file, upload it somewhere, and post the link then I can have a look at it.</p>

---

## Post #5 by @Saima (2019-11-06 04:16 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="8859">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>ery robustly for m</p>
</blockquote>
</aside>
<p>Hi Andras,<br>
I uploaded it on googledrive. here is the link.</p>
<p><a href="https://drive.google.com/drive/folders/1WFGnfJRLm65MxF99JzKdnnvGyPLRhO-u?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1WFGnfJRLm65MxF99JzKdnnvGyPLRhO-u?usp=sharing</a></p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #6 by @lassoan (2019-11-06 05:41 UTC)

<p>Thanks, the scene file helped. The main issue was that the points were not on the surface of the model and the locator’s <code>FindCell</code> method required points to be on the surface (it uses 0 tolerance value for finding a cell).</p>
<p>I’ve updated the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Select_cells_of_a_using_markups_fiducial_points">example script</a> to find the closest cell and also updated the example to not recreate the selection array if it already exists (so that the code runs correctly even if you run it on a mesh where you’ve used it on already).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f8261af1125092ef1047c68237ecc5db9a2f6f2.png" data-download-href="/uploads/short-url/93Pq9HNdMNkBlUBaAnO0NE5q0pA.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f8261af1125092ef1047c68237ecc5db9a2f6f2.png" alt="image" data-base62-sha1="93Pq9HNdMNkBlUBaAnO0NE5q0pA" width="593" height="499" data-dominant-color="9F9D6E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">672×566 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @Saima (2019-11-06 05:52 UTC)

<p>Hi Andras,<br>
Thank you so much. Andras what should I do if I need to select the other neighbouring cells in between the selected cells.</p>
<p>Thankyou</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #8 by @lassoan (2019-11-06 12:42 UTC)

<p>See this example: <a href="https://lorensen.github.io/VTKExamples/site/Cxx/PolyData/CellPointNeighbors/">https://lorensen.github.io/VTKExamples/site/Cxx/PolyData/CellPointNeighbors/</a></p>

---

## Post #9 by @Saima (2019-11-07 06:27 UTC)

<p>Hi Andras,<br>
how can i use this within slicer. what will be the steps.</p>
<p>I am so sorry if I am asking a simple question because I do not understand how i am going to use it within slicer.</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #10 by @lassoan (2019-11-07 12:34 UTC)

<p>Look at the example to see what VTK classes and what methods of that classes are used to get cell neighbors.</p>

---

## Post #11 by @Saima (2019-11-14 04:04 UTC)

<p>Hi Andras,<br>
I was trying to do what you said. the program below is used to extract neighbouring cells relevant to a single cell for example; 2978 is the cell id of one of the cells in the mesh and it gets its cell point ids and based on the cell point ids it gets the neighouring cells. but my program is crashing. could you please tell me what is wrong what I am doing.</p>
<p>actually problem starts with line “trianglefilter.GetOutput().GetCellNeighbors(2978, idList, neighbourcells)`”" the second argument requires a vtk object. I am passing the vtklist object but dont understand what to do. Could you please advice what am i doing wrong.<br>
Thanks</p>
<p>modelNode = slicer.util.getNode(inputVolume.GetID())<br>
m = modelNode.GetMesh()</p>
<pre><code>trianglefilter = vtk.vtkTriangleFilter()

trianglefilter.SetInputData(m)
trianglefilter.Update()

cellPointIds = vtk.vtkIdList()

trianglefilter.GetOutput().GetCellPoints(2978, cellPointIds)

for i in range(0,3):
    print(cellPointIds.GetId(i))
    
neighbourcells = vtk.vtkIdList()

idList = vtk.vtkIdList()
idList.SetNumberOfIds(3)
idList.SetId(0,1552)
</code></pre>
<p><code>&gt;     trianglefilter.GetOutput().GetCellNeighbors(2978, idList, neighbourcells)</code></p>
<p>print(neighbourcells.GetNumberOfIds())</p>

---

## Post #12 by @Saima (2019-11-14 05:31 UTC)

<p>I figured out my mistake. Thank you andras.</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #13 by @Saima (2020-01-16 07:48 UTC)

<p>Hi Andras,<br>
I need to find the vertices for each selected cell in the above mesh. How would I be able to get it.<br>
Please help.</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #14 by @lassoan (2020-01-16 21:52 UTC)

<p><a href="https://vtk.org/doc/nightly/html/classvtkCell.html">vtkCell::GetPointIds</a> returns the list of point indices for a cell. You can get the cell object using <a href="https://vtk.org/doc/nightly/html/classvtkUnstructuredGrid.html#a0910469a383a022097d324c1f40fb831">GetCell</a>.</p>

---

## Post #15 by @Saima (2020-01-17 04:45 UTC)

<p>thanks andras.</p>
<p>another question how to get the x y z of pointids.</p>
<p>Thanks</p>

---

## Post #16 by @timeanddoctor (2020-01-17 13:11 UTC)

<p>Can I select the cells with a ball(paint brush in 3d view) not the point because of large model, and then saved as a polydata?</p>

---

## Post #17 by @lassoan (2020-01-17 13:37 UTC)

<aside class="quote no-group" data-username="timeanddoctor" data-post="16" data-topic="8859" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/timeanddoctor/48/5839_2.png" class="avatar"> timeanddoctor:</div>
<blockquote>
<p>Can I select the cells with a ball(paint brush in 3d view) not the point because of large model, and then saved as a polydata?</p>
</blockquote>
</aside>
<p>Please post your question as a new topic. Add some context and preferably illustrations, because from this sentence alone it is not clear what you are trying to achieve.</p>
<aside class="quote no-group" data-username="Saima" data-post="15" data-topic="8859">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>another question how to get the x y z of pointids.</p>
</blockquote>
</aside>
<p>You can find all these details in <a href="https://vtk.org/doc/nightly/html/">VTK API documentation</a> and <a href="https://lorensen.github.io/VTKExamples/site/">examples</a> of the corresponding class.</p>

---

## Post #18 by @Saima (2020-02-03 07:51 UTC)

<p>Hi Andras,<br>
I am getting the following error for the example script above. I do not understand what is the problem. I created fiducials and using fiducials i need to select the surface elements on brain mesh like previously. Could you please help.</p>
<p>Traceback (most recent call last):<br>
File “/home/saima/slicer/Slicer-4.11.0-2019-09-17-linux-amd64/ImageAsaModel/MeshNodesToFiducials/MeshNodesToFiducials.py”, line 73, in onApplyButton<br>
logic.run(self.ui.inputSelector.currentNode(), self.ui.outputSelector.currentNode(), imageThreshold, enableScreenshotsFlag)<br>
File “/home/saima/slicer/Slicer-4.11.0-2019-09-17-linux-amd64/ImageAsaModel/MeshNodesToFiducials/MeshNodesToFiducials.py”, line 207, in run<br>
arr = self.onPointsModified(selectionArray, markupsNode, cell)<br>
File “/home/saima/slicer/Slicer-4.11.0-2019-09-17-linux-amd64/ImageAsaModel/MeshNodesToFiducials/MeshNodesToFiducials.py”, line 141, in onPointsModified<br>
selectionArray.SetValue(closestCell, 100)<br>
ValueError: expects 0 &lt;= id &amp;&amp; id &lt; GetNumberOfValues()</p>

---

## Post #19 by @lassoan (2020-02-03 14:01 UTC)

<p><code>closestCell</code> value is out of range (there is no item with such index in <code>selectionArray</code>).</p>

---

## Post #20 by @Saima (2021-11-12 04:10 UTC)

<p>Hi Andras,<br>
Is it possible to get the neighboring cells for a vtkunstructured grid 2d.</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #21 by @lassoan (2021-11-16 00:17 UTC)

<p>It should be possible. Try some googling. For example this seems relevant: <a href="https://kitware.github.io/vtk-examples/site/Cxx/PolyData/CellPointNeighbors/">https://kitware.github.io/vtk-examples/site/Cxx/PolyData/CellPointNeighbors/</a></p>

---
