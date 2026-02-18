# Tracking of multiple objects to a reference

**Topic ID**: 27450
**Date**: 2023-01-24
**URL**: https://discourse.slicer.org/t/tracking-of-multiple-objects-to-a-reference/27450

---

## Post #1 by @MPeiffer (2023-01-24 20:52 UTC)

<p>Hi all,</p>
<p>I’ve been working with slicerIGT to create a surgical navigation tool for the ankle.<br>
In this tool, we want to track the position of the Fibula (calf bone) with respect to the reference Tibia (shin bone).</p>
<p>To try this, we have 3D printed STL models of the fibula and tibia, which we got from a CT scan.</p>
<p>We are yet able to track the tibia (which we have used as reference, similar to the neurosurgery tutorial) and the stylus. I’m having some difficulties however with tracking the fibula with respect to the tibia.</p>
<p>How should I perform the transformation matrix to align the fibula STL model also with respect to the reference tibia?</p>
<p>See below A picture of the setup, slicer view and current transforms, which shows a good tracking capability of the tibia and stylus, but the fibula is out of place.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a7d3e01d81aa4d97a948316a192c9c21a9ae17c5.jpeg" data-download-href="/uploads/short-url/nWFG4CZN4t4DeaVvDVhwfE0dKQt.jpeg?dl=1" title="thumbnail_image0" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a7d3e01d81aa4d97a948316a192c9c21a9ae17c5_2_666x500.jpeg" alt="thumbnail_image0" data-base62-sha1="nWFG4CZN4t4DeaVvDVhwfE0dKQt" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a7d3e01d81aa4d97a948316a192c9c21a9ae17c5_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a7d3e01d81aa4d97a948316a192c9c21a9ae17c5_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a7d3e01d81aa4d97a948316a192c9c21a9ae17c5.jpeg 2x" data-dominant-color="7F7C76"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">thumbnail_image0</span><span class="informations">1280×960 222 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d1fb8ea4984084189c2fe2b8567c4a00546dc93.png" data-download-href="/uploads/short-url/mpYVvNMrahn3Qpi2Gu23YQBU5Nh.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d1fb8ea4984084189c2fe2b8567c4a00546dc93_2_690x445.png" alt="image" data-base62-sha1="mpYVvNMrahn3Qpi2Gu23YQBU5Nh" width="690" height="445" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d1fb8ea4984084189c2fe2b8567c4a00546dc93_2_690x445.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d1fb8ea4984084189c2fe2b8567c4a00546dc93_2_1035x667.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d1fb8ea4984084189c2fe2b8567c4a00546dc93_2_1380x890.png 2x" data-dominant-color="989AD0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1744×1125 78.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/51887b5a779e8710cf6924688b8285e8def675ae.png" alt="image" data-base62-sha1="bDh5l2IGIQq1dAr27V3rdq32IKW" width="570" height="439"></p>
<p>Thank you!</p>

---

## Post #2 by @Sunderlandkyl (2023-01-25 17:57 UTC)

<p>“Reference” is the markers that are attached to the tibia?</p>
<p>If you want the tibia to remain static, while the fibula moves, I would add it to the transform hierarchy like so:</p>
<pre><code class="lang-auto">- ReferenceToRAS
  - FibulaToReference
    - FibulaRASToFibula
      - Fibula
</code></pre>
<p>FibulaRASToFibula will need to be calculated from fiducial registration wizard. From: Fibula model points, To: Fibula points. You can add StylusToFibula to the config file, reparent StylusTipToStylus to that transform, and use that for collecting points.</p>

---

## Post #3 by @MPeiffer (2023-01-25 20:43 UTC)

<p>Dear Kyle,</p>
<p>Thank you, I’m now able to track te fibula with respect to the reference (Tibia), which is great!</p>
<p>I was wondering if it was also possible to have a “surface matching” based on marking the surface of the printed model to align with the STL model in slicer, rather than only based on 3 (or more) fiducial points? I believe this would increase the accuracy</p>
<p>Thank you,</p>
<p>Matthias</p>

---

## Post #4 by @Sunderlandkyl (2023-01-26 05:07 UTC)

<p>Sure, take a look at the “Fiducials-Model Registration” module.</p>

---

## Post #5 by @MPeiffer (2023-01-26 15:22 UTC)

<p>Dear Kyle,</p>
<p>This is amazing and very useful, thank you.</p>
<p>I was wondering if I could have your opinion/suggestions on the following:</p>
<p>We are building towards a navigation system to increase the accuracy of surgical reduction (which means aligning the two bones - tibia and fibula back together during surgery), as nowadays there is 52% chance of malreduction when trying to align the two bones back together and fixing them during surgery. Surgical navigation (if feasible) would highly increase the accuracy of this surgery, while reducing the fluoroscopic burden on the patient/staff.</p>
<p>For this, it would be great if we could have some real-time measurements of the alignment between the tibia and fibula while repositioning them. These would be measurements (distance, angle) based on specified bony anatomical landmarks which have been predefined and move along with the bones (i.e. same transformation matrix). I was looking for such a tool/module in Slicer but I could not yet find one that is able to show the measurements and their change in real-time.</p>
<p>Do you have any idea what would be the best way to get these? building a seperate module?<br>
Unfortunately, I’m only familiar with coding in Matlab so I’m having some difficulties with making the module with Python.</p>
<p>Thank you in advance!</p>
<p>Matthias</p>

---

## Post #6 by @Sunderlandkyl (2023-01-27 16:05 UTC)

<p>I don’t think that there’s a module that will do this automatically. If you want to do this in real-time, you will probably need to implement your own module.</p>
<p>The SlicerScriptRepository is a useful resource for getting started and provides many examples:<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html</a></p>

---

## Post #7 by @MPeiffer (2023-01-27 18:28 UTC)

<p>Dear Kyle,</p>
<p>Okay, many thanks.<br>
I’m getting started with the Pyhton Interactor now to get this going, but i’m having the following issue.</p>
<p>I was able to get several distances (ATFD_R, …)  from several points (TibAntR, …) and put them into a table which can be viewed in the table module:</p>
<p>ATFD_R = np.linalg.norm(TibAntR - FibAntR)<br>
PTFD_R = np.linalg.norm(TibPostR - FibPostR)<br>
ATFD_L = np.linalg.norm(TibAntL - FibAntL)<br>
PTFD_L = np.linalg.norm(TibPostL - FibPostL)</p>
<p><span class="hashtag">#Make</span> Table<br>
Coltitle = vtk.vtkStringArray()<br>
Coltitle.SetName(“”)<br>
ColRight = vtk.vtkDoubleArray()<br>
ColRight.SetName(“Right”)<br>
ColLeft = vtk.vtkDoubleArray()<br>
ColLeft.SetName(“Left”)<br>
ColDiff = vtk.vtkDoubleArray()<br>
ColDiff.SetName(“Difference R-L”)<br>
Coltitle.InsertNextValue(‘ATFD’)<br>
Coltitle.InsertNextValue(‘PTFD’)<br>
ColRight.InsertNextValue(ATFD_R)<br>
ColRight.InsertNextValue(PTFD_R)<br>
ColLeft.InsertNextValue(ATFD_L)<br>
ColLeft.InsertNextValue(PTFD_L)<br>
ColDiff.InsertNextValue(ATFD_R - ATFD_L)<br>
ColDiff.InsertNextValue(PTFD_R - PTFD_L)<br>
resultTableNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLTableNode”, “Syndesmotic Distances”)<br>
resultTableNode.AddColumn(Coltitle)<br>
resultTableNode.AddColumn(ColRight)<br>
resultTableNode.AddColumn(ColLeft)<br>
resultTableNode.AddColumn(ColDiff)</p>
<p>This gives the following table:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/686c747f3c9d1c27d543b60368f30a2a105deccd.png" alt="image" data-base62-sha1="eTM1i5yH7oa1L4INMzgwGI6UsIl" width="425" height="146"></p>
<p>which is exxactly what i was looking for!</p>
<p>Then, I created a new point (FibAntRight, which was the same as FibAntR), from which I can get the updated position.</p>
<p><span class="hashtag">#Get</span> updated position of FibAnt<br>
def onMarkupChanged(caller,event):<br>
markupsNode = caller<br>
sliceView = markupsNode.GetAttribute(“Markups.MovingInSliceView”)<br>
movingMarkupIndex = markupsNode.GetDisplayNode().GetActiveControlPoint()<br>
if movingMarkupIndex &gt;= 0:<br>
pos = [0,0,0]<br>
markupsNode.GetNthControlPointPosition(movingMarkupIndex, pos)<br>
isPreview = markupsNode.GetNthControlPointPositionStatus(movingMarkupIndex) == slicer.vtkMRMLMarkupsNode.PositionPreview<br>
if isPreview:<br>
logging.info(“Point {0} is previewed at {1} in slice view {2}”.format(movingMarkupIndex, pos, sliceView))<br>
else:<br>
logging.info(“Point {0} was moved {1} in slice view {2}”.format(movingMarkupIndex, pos, sliceView))<br>
else:<br>
logging.info(“Points modified: slice view = {0}”.format(sliceView))</p>
<p>def onMarkupStartInteraction(caller, event):<br>
markupsNode = caller<br>
sliceView = markupsNode.GetAttribute(“Markups.MovingInSliceView”)<br>
movingMarkupIndex = markupsNode.GetDisplayNode().GetActiveControlPoint()<br>
logging.info(“Start interaction: point ID = {0}, slice view = {1}”.format(movingMarkupIndex, sliceView))</p>
<p>def onMarkupEndInteraction(caller, event):<br>
markupsNode = caller<br>
sliceView = markupsNode.GetAttribute(“Markups.MovingInSliceView”)<br>
movingMarkupIndex = markupsNode.GetDisplayNode().GetActiveControlPoint()<br>
logging.info(“End interaction: point ID = {0}, slice view = {1}”.format(movingMarkupIndex, sliceView))</p>
<p>FibAntRight = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLMarkupsFiducialNode”)<br>
FibAntRight.AddControlPoint(FibAntR[0],FibAntR[1],FibAntR[2])<br>
FibAntRight.AddObserver(slicer.vtkMRMLMarkupsNode.PointModifiedEvent, onMarkupChanged)<br>
FibAntRight.AddObserver(slicer.vtkMRMLMarkupsNode.PointStartInteractionEvent, onMarkupStartInteraction)<br>
FibAntRight.AddObserver(slicer.vtkMRMLMarkupsNode.PointEndInteractionEvent, onMarkupEndInteraction)</p>
<p>If I can calculate the updated distance from the new position of the point, is there a way I could automatically update this value in the table I previously created?</p>
<p>Thank you!</p>
<p>Matthias</p>

---
