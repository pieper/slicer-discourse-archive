---
topic_id: 7753
title: "Select Cells Of A 3D Model"
date: 2019-07-25
url: https://discourse.slicer.org/t/7753
---

# Select cells of a 3D model

**Topic ID**: 7753
**Date**: 2019-07-25
**URL**: https://discourse.slicer.org/t/select-cells-of-a-3d-model/7753

---

## Post #1 by @Saima (2019-07-25 08:50 UTC)

<p>how to create a mouse event inside the 3d slicer view. Need to pick cells from a mesh object from within the 3d slice view of the slicer.</p>
<p>Need help</p>

---

## Post #2 by @lassoan (2019-07-25 12:47 UTC)

<p>You can get 3D position from views as shown in these examples:</p>
<ul>
<li>Slice views: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_current_mouse_coordinates_in_a_slice_view" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_current_mouse_coordinates_in_a_slice_view</a>
</li>
<li>3D views: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_scalar_values_at_surface_of_a_model" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_scalar_values_at_surface_of_a_model</a>
</li>
</ul>
<p>If you want to select several cells, you can use markups fiducials : drop a fiducials on the cells you want to select and then use <a href="https://vtk.org/doc/nightly/html/classvtkCellLocator.html" rel="nofollow noopener">FindCell</a> to get the cell IDs. If you don’t want the fiducials to stay there then you can remove them immediately after you retrieved their position. In recent Slicer Preview builds, markups points slide on visible surfaces, so you can make position adjustments quite easily.</p>

---

## Post #3 by @Saima (2019-07-26 09:05 UTC)

<p>Hi andras,<br>
I wrote the following to get the cell using fiducial</p>
<p>def onMouseMoved(self, observer,eventid):<br>
ras=[0,0,0]<br>
crosshairNode.GetCursorPositionRAS(ras)<br>
if markupsNode.GetNumberOfFiducials() == 0:<br>
markupsNode.AddFiducial(*ras)<br>
else:<br>
markupsNode.SetNthFiducialPosition(0,*ras)<br>
closestCell = cell.FindCell(ras)<br>
closestPointValue = modelPointValues.GetTuple(closestCell)<br>
print("RAS = " + repr(ras) + "    value = " + repr(closestPointValue))</p>
<p>calling this within a scripted module in the run function as<br>
global cell, modelPointValues, crosshairNode, markupsNode<br>
modelNode = slicer.util.getNode(‘Model_1’)<br>
<span class="hashtag">#modelPointValues</span> = modelNode.GetPolyData().GetPointData().GetArray(“Normals”)<br>
modelPointValues = modelNode.GetMesh().GetCells()<br>
markupsNode = slicer.util.getNode(‘F’)</p>
<pre><code>if not markupsNode:
 markupsNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode","F")

#pointsLocator = vtk.vtkPointLocator() # could try using vtk.vtkStaticPointLocator() if need to optimize
#pointsLocator.SetDataSet(modelNode.GetPolyData())
#pointsLocator.BuildLocator()

cell = vtk.vtkCellLocator()
cell.SetDataSet(modelNode.GetMesh())
cell.BuildLocator

crosshairNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLCrosshairNode")
crosshairNodeObserverTag = crosshairNode.AddObserver(slicer.vtkMRMLCrosshairNode.CursorPositionModifiedEvent, self.onMouseMoved)
</code></pre>
<p>The application stoped working. although there was no error. the mouse cursor was paused. Could you tell me whats wrong with the code.</p>

---

## Post #4 by @Saima (2019-07-28 11:12 UTC)

<p>I replaced the crosshair node part with</p>
<p>crosshairNode=slicer.util.getNode(‘Crosshair’)<br>
crosshairNodeObserverTag = crosshairNode.AddObserver(slicer.vtkMRMLCrosshairNode.CursorPositionModifiedEvent, self.onMouseMoved)</p>
<p>but still the program doessnt work. What is wrong in the code. could you please tell me. because the program haults and then the slicer application closes.</p>

---

## Post #5 by @lassoan (2019-07-29 04:01 UTC)

<p>Modify crosshair examples of the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" rel="nofollow noopener">script repository</a> step by step. If you encounter any problems then post the script, describe what you do, what you expect to happen, and what happens instead.</p>

---

## Post #6 by @Saima (2019-07-29 08:12 UTC)

<p>I need cells to be selected with mouse of the mesh in attached pic. The script gives me the position of mousecursor. I defined the celllocator and using the findcell to locate the cell. Could you please guide in this respect. What I need to look at.</p>
<p>I need to get the pcoords of tetra cell rather then the mousecursorpoint. what should I do.</p>
<pre data-code-wrap="python"><code class="lang-python">global cell, modelPointValues, crosshairNode, markupsNode
modelNode = slicer.util.getNode('Model_1')
modelPointValues = modelNode.GetMesh().GetCells().GetData()

cell = vtk.vtkCellLocator()
cell.SetDataSet(modelNode.GetMesh())
cell.BuildLocator

crosshairNode=slicer.util.getNode('Crosshair')
crosshairNodeObserverTag = crosshairNode.AddObserver(slicer.vtkMRMLCrosshairNode.CursorPositionModifiedEvent, self.onMouseMoved)

def onMouseMoved(self, observer, eventid):  
        ras=[0,0,0]
        crosshairNode.GetCursorPositionRAS(ras)
        if markupsNode.GetNumberOfFiducials() == 0:
         markupsNode.AddFiducial(*ras)
        else:
         markupsNode.SetNthFiducialPosition(0,*ras)
        closestCell = cell.FindCell(ras) /**//Problem starts here
        print("inside mouse event")
        #closestPointValue = modelPointValues.GetTuple(closestCell)
        print("RAS = " + repr(ras) )#+ "    value = " + repr(closestPointValue))
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35bd9b8106e6aae846036e6e2d919969df9a5d5f.jpeg" data-download-href="/uploads/short-url/7Fpxm3k6Jirp1CYKBfrf3M6Wm99.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35bd9b8106e6aae846036e6e2d919969df9a5d5f_2_690x377.jpeg" alt="image" data-base62-sha1="7Fpxm3k6Jirp1CYKBfrf3M6Wm99" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35bd9b8106e6aae846036e6e2d919969df9a5d5f_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35bd9b8106e6aae846036e6e2d919969df9a5d5f_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35bd9b8106e6aae846036e6e2d919969df9a5d5f_2_1380x754.jpeg 2x" data-dominant-color="B8B9C8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1051 280 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2019-07-29 13:52 UTC)

<p>The code crashed because you did not build the locator. <code>cell.BuildLocator</code> just prints the address of the <code>BuildLocator</code> method. You need to add <code>()</code> to call the method: <code>cell.BuildLocator()</code>.</p>
<p>Another issue is that you mix two approaches: getting point coordinates from markups and crosshair. If you use markups then you don’t need to use crosshair, as you can get 3D positions from the markup points.</p>
<p>See a complete working example here (requires recent Preview Release of Slicer): <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Select_cells_of_a_using_markups_fiducial_points" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Select_cells_of_a_using_markups_fiducial_points</a></p>

---

## Post #8 by @Saima (2019-08-22 05:50 UTC)

<p>Hi Andras,<br>
Is there a way to select cells on the surface of mesh using onMouseClicked event.</p>
<p>Please suggest.</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #9 by @lassoan (2019-08-22 16:05 UTC)

<aside class="quote no-group" data-username="Saima" data-post="8" data-topic="7753">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>Is there a way to select cells on the surface of mesh using onMouseClicked event.</p>
</blockquote>
</aside>
<p>It should be possible, but the example script that I linked above can already add markups and thus select cells on mouse click.</p>

---

## Post #10 by @Saima (2019-08-23 02:51 UTC)

<p>Andras I need to use only the mouse clicks to select the cells of a mesh without using the fiducials.<br>
I understand adding three fiducial points to locate the cell will be not feasible.</p>
<p>I would want to select may cells from the surface of the brain where I can apply force. the craniotomy induced part I need to select and it will be different for each MRI. So I need to select the area by mouse. Any suggestions how can I do it?</p>
<p>Thank you so much for replies.</p>
<p>Looking forward to your answer.</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #11 by @lassoan (2019-08-23 03:34 UTC)

<p>Can you write a bit more about what exactly you would like to achieve?</p>
<p>What is your input data? 3D volumes? Segmentations? Surface scans?</p>
<p>What would you like to do with the data? What would you like to get as end results?</p>

---

## Post #12 by @Saima (2019-08-23 09:11 UTC)

<p>Data = 3D volumetric brain Mesh<br>
What would you like to do with the data? Need to select the surface cells from the brain portion where craniotomy was induced. I will be using the preoperative mri images.<br>
What would you like to get as end results? after selecting cells I will save those cells in a file and will pass those cells along with the complete brain mesh to external Meshless algorithm to compute the craniotomy induced brain shift.</p>

---

## Post #13 by @lassoan (2019-08-23 16:28 UTC)

<aside class="quote no-group" data-username="Saima" data-post="12" data-topic="7753">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>Need to select the surface cells from the brain portion where craniotomy was induced. I will be using the preoperative mri images.</p>
</blockquote>
</aside>
<p>We have very good tool to mark regions in volumetric images: Segment Editor module. You can get cell IDs that overlap the craniotomy region by following these steps:</p>
<ul>
<li>segment the craniotomy region on the image using Segment Editor</li>
<li>export segmentation to a labelmap volume</li>
<li>use “Probe volume with model” to label all mesh points with 1/0 (corresponding to overlap / does not overlap with the segmented region)</li>
<li>find cell IDs corresponding to points that are labelled with “1” - you can use VTK filters (similarly to <a href="https://www.paraview.org/Wiki/VTK/Examples/Cxx/PolyData/ExtractCellsUsingPoints">this</a>) or just by iterating through all the cells and see if any of its points are labelled with “1”</li>
</ul>

---

## Post #14 by @Saima (2019-09-02 08:36 UTC)

<p>Hi Andras,<br>
Can above be done through scripting. Please help</p>
<p>thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #15 by @Saima (2019-09-02 14:06 UTC)

<p>Hi ANdras, I used the steps you told me in 3d slicer its producing the following results instead of only highlighting the segmented volume portion.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54798555ed7e95d52e6ae2e63d934361f88f1bcb.png" data-download-href="/uploads/short-url/c3isOodFxUOv48TrTcrGBWW1o3p.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54798555ed7e95d52e6ae2e63d934361f88f1bcb_2_690x371.png" alt="image" data-base62-sha1="c3isOodFxUOv48TrTcrGBWW1o3p" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54798555ed7e95d52e6ae2e63d934361f88f1bcb_2_690x371.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54798555ed7e95d52e6ae2e63d934361f88f1bcb_2_1035x556.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54798555ed7e95d52e6ae2e63d934361f88f1bcb_2_1380x742.png 2x" data-dominant-color="BDBEC1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1034 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What am I doing wrong.</p>
<p>I loaded the skull stripped volume.<br>
created a segmentation using scissors and mask volume effect.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3ca8c44288bbdbf4cd114ec3d2571006b0baf48.png" data-download-href="/uploads/short-url/rW33WEaxL8Vxy2INvbCv7B6sKec.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3ca8c44288bbdbf4cd114ec3d2571006b0baf48_2_690x371.png" alt="image" data-base62-sha1="rW33WEaxL8Vxy2INvbCv7B6sKec" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3ca8c44288bbdbf4cd114ec3d2571006b0baf48_2_690x371.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3ca8c44288bbdbf4cd114ec3d2571006b0baf48_2_1035x556.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3ca8c44288bbdbf4cd114ec3d2571006b0baf48_2_1380x742.png 2x" data-dominant-color="C3C4C7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1034 218 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
new volume generated<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be7a01eddd9064a3fc67bf3b5ec4da248b5e9592.png" data-download-href="/uploads/short-url/rb27oGx1Bms4Hczyu66r9CKHCXE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be7a01eddd9064a3fc67bf3b5ec4da248b5e9592_2_690x371.png" alt="image" data-base62-sha1="rb27oGx1Bms4Hczyu66r9CKHCXE" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be7a01eddd9064a3fc67bf3b5ec4da248b5e9592_2_690x371.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be7a01eddd9064a3fc67bf3b5ec4da248b5e9592_2_1035x556.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be7a01eddd9064a3fc67bf3b5ec4da248b5e9592_2_1380x742.png 2x" data-dominant-color="BDBEC1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1034 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
exported segmentation as labelmap volume.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0a78839b60fa5b137a23f5fd59a20108b0eacad.png" data-download-href="/uploads/short-url/ykVwMRTWZsFYo2y4QZbIYApBTop.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f0a78839b60fa5b137a23f5fd59a20108b0eacad_2_690x371.png" alt="image" data-base62-sha1="ykVwMRTWZsFYo2y4QZbIYApBTop" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f0a78839b60fa5b137a23f5fd59a20108b0eacad_2_690x371.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f0a78839b60fa5b137a23f5fd59a20108b0eacad_2_1035x556.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f0a78839b60fa5b137a23f5fd59a20108b0eacad_2_1380x742.png 2x" data-dominant-color="C2C1C3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1034 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>used the new volume for input in probe volume model.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5cb74bf40a45d5776b5e8c5b9c5d389a99af8f99.png" data-download-href="/uploads/short-url/decDAUkfBmb7t2cZ37QEFwDVFxf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cb74bf40a45d5776b5e8c5b9c5d389a99af8f99_2_690x371.png" alt="image" data-base62-sha1="decDAUkfBmb7t2cZ37QEFwDVFxf" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cb74bf40a45d5776b5e8c5b9c5d389a99af8f99_2_690x371.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cb74bf40a45d5776b5e8c5b9c5d389a99af8f99_2_1035x556.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cb74bf40a45d5776b5e8c5b9c5d389a99af8f99_2_1380x742.png 2x" data-dominant-color="BDBFC2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1034 95.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
one time I click on the model it looks like below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22fa5709f339ee4495f0d50cd214b4e3d5743d8c.png" data-download-href="/uploads/short-url/4ZqAgARw5Oj98KaA7TI5RV0QYQ4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22fa5709f339ee4495f0d50cd214b4e3d5743d8c_2_690x371.png" alt="image" data-base62-sha1="4ZqAgARw5Oj98KaA7TI5RV0QYQ4" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22fa5709f339ee4495f0d50cd214b4e3d5743d8c_2_690x371.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22fa5709f339ee4495f0d50cd214b4e3d5743d8c_2_1035x556.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22fa5709f339ee4495f0d50cd214b4e3d5743d8c_2_1380x742.png 2x" data-dominant-color="BFC0C3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1034 93.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
other time I click on the same model eye open eye close it looks like below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5cb66c5e977b4d27ef13c8431eb3765d2429fdce.png" data-download-href="/uploads/short-url/deaLA22Y4auqShjG7RiN6qkrwFU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cb66c5e977b4d27ef13c8431eb3765d2429fdce_2_690x371.png" alt="image" data-base62-sha1="deaLA22Y4auqShjG7RiN6qkrwFU" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cb66c5e977b4d27ef13c8431eb3765d2429fdce_2_690x371.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cb66c5e977b4d27ef13c8431eb3765d2429fdce_2_1035x556.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cb66c5e977b4d27ef13c8431eb3765d2429fdce_2_1380x742.png 2x" data-dominant-color="BFC0C2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1034 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Could you please guide me what am I doing wrong I need only the segmented volume region to be selected on the model.</p>
<p>Please help.</p>
<p>Also I need to do all this through scripting.</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #16 by @Saima (2019-09-04 07:58 UTC)

<p>Hi andras,<br>
I applied the probe volume with model filter. Got the cell ids using the script below:</p>
<pre><code class="lang-python">for cellIndex in range(ncells):
        cellpoints = mesh.GetCellPoints(cellIndex,idList)
        scalarArray = mesh.GetPointData().GetArray(0)
        #print(scalarArray)
        numPoints = idList.GetNumberOfIds()
        #print(numPoints)
        for pointIndex in range(numPoints):
            value = scalarArray.GetValue(idList.GetId(pointIndex))
            if(value == 1):
               print(cellIndex)
</code></pre>
<p>could you please tell me how could I get those cells coloured differently on the model.</p>
<p>Looking forward to your reply.</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>
<p>P.S. Also please tell me how can i use the probe volume with model using script. thankyou</p>

---

## Post #17 by @lassoan (2019-09-04 14:42 UTC)

<p>While the VTK code above that gives you point IDs that have a certain scalar value is correct, you may find it easier to get the point data as numpy array and use numpy for processing:</p>
<pre data-code-wrap="python"><code class="lang-python">import numpy as np
voxelValues = slicer.util.arrayFromModelPointData(getNode('Output Model'), 'NRRDImage')
pointIDs = np.where(voxelValues == 1)
</code></pre>
<aside class="quote no-group" data-username="Saima" data-post="16" data-topic="7753">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>could you please tell me how could I get those cells coloured differently on the model</p>
</blockquote>
</aside>
<p>You can use Models module / Display / Scalars section to color a model by a selected scalar.</p>
<aside class="quote no-group" data-username="Saima" data-post="16" data-topic="7753">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>please tell me how can i use the probe volume with model using script</p>
</blockquote>
</aside>
<p>“Probe volume with model” module is a CLI module, so you can run it from Python as described <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python">here</a>.</p>

---

## Post #18 by @Saima (2019-09-05 03:38 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="17" data-topic="7753">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>voxelValues = slicer.util.arrayFromModelPointData(getNode(‘Output Model’), ‘NRRDImage’)</p>
</blockquote>
</aside>
<p>n = getNode(“Output Model_1”)</p>
<blockquote>
<blockquote>
<blockquote>
<p>n<br>
(MRMLCorePython.vtkMRMLModelNode)0000023BCBDE8E28<br>
voxelValues = slicer.util.arrayFromModelPointData(n, ‘NRRDImage’)<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\22374464\AppData\Local\NA-MIC\Slicer 4.11.0-2019-07-06\bin\Python\slicer\util.py”, line 1009, in arrayFromModelPointData<br>
arrayVtk = modelNode.GetPolyData().GetPointData().GetArray(arrayName)<br>
AttributeError: ‘NoneType’ object has no attribute ‘GetPointData’</p>
</blockquote>
</blockquote>
</blockquote>
<p>getting the above error. Why dont understand?</p>

---

## Post #19 by @Saima (2019-09-05 04:59 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="17" data-topic="7753">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can use Models module / Display / Scalars section to color a model by a selected scalar.</p>
<p><img src="https://avatars.discourse.org/v4/letter/s/9d8465/40.png" alt="" width="20" height="20" role="presentation"> Saima:</p>
</blockquote>
</aside>
<p>I need to color the selected cells. For example I want to color the cell in the model. I am getting the location of that cell then using that location to set the activescalar. is it right. I dont know how to color. Any help?</p>
<p>nn = slicer.util.getNode(outputVolume.GetID())<br>
d = nn.GetModelDisplayNode()<br>
l = nn.GetMesh().GetCellLocationsArray()<br>
v = l.GetValue(4740)<br>
d.SetActiveScalar(‘R’,v)<br>
d.SetAndObserveColorNodeID(‘FullRainbow’)<br>
d.ScalarVisibilityOn()<br>
d.AutoScalarRangeOn()</p>

---

## Post #20 by @Saima (2019-09-12 09:20 UTC)

<p>Hi Andras,<br>
Is there a way to change the color for different cells in a 3d volumetric mesh by scripting. i know cell ids I need to change the color for those cells. How can I do it. please guide</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #21 by @lassoan (2019-09-12 17:26 UTC)

<p>To different color for each cell, you can add a new array to the cell data of the polydata (see this <a href="https://vtk.org/Wiki/VTK/Examples/Cxx/PolyData/MiscCellData" rel="nofollow noopener">VTK example</a>) and enable scalar visibility in the model display node.</p>

---

## Post #22 by @lassoan (2019-10-22 13:14 UTC)

<p>A post was split to a new topic: <a href="/t/get-cell-data-of-a-mesh-at-selected-point-positions/8859">Get cell data of a mesh at selected point positions</a></p>

---
