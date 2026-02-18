# Get world coordinate of maximum intensity voxel

**Topic ID**: 4168
**Date**: 2018-09-22
**URL**: https://discourse.slicer.org/t/get-world-coordinate-of-maximum-intensity-voxel/4168

---

## Post #1 by @shahrokh (2018-09-22 11:54 UTC)

<p>Hi<br>
Dear Developers and Users<br>
I want to create sphere model centerd in the voxel with maximum value.</p>
<p>Steps:<br>
<strong>1-</strong> Load PET images using “DICOM Browser”.<br>
<strong>2-</strong> Click on “Center Volume” in the module of “Volumes”.<br>
<strong>3-</strong> Enter the following commands:<br>
PETnode = slicer.util.getNode(‘PETnode’)<br>
PETnumpy = slicer.util.arrayFromVolume(PETnode)<br>
import numpy as np<br>
indices = np.where(PETnumpy == PETnumpy.max())<br>
sphere = vtk.vtkSphereSource()<br>
sphere.SetRadius(10.)<br>
sphere.SetCenter(indices)<br>
sphere.SetPhiResolution(30)<br>
sphere.SetThetaResolution(30)<br>
modelsLogic = slicer.modules.models.logic()<br>
model = modelsLogic.AddModel(sphere.GetOutput())<br>
model.GetDisplayNode().SetSliceIntersectionVisibility(True)<br>
model.GetDisplayNode().SetSliceIntersectionThickness(1)<br>
model.GetDisplayNode().SetColor(1,0,0)<br>
sphere.Update()</p>
<p>As mentioned in the following screen shot, the position of the sphere is not correct (out of body).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f75f780a6bb70811c419855bca601cd82c945ed2.png" data-download-href="/uploads/short-url/zimtxgixFQAriuklj7R78B4xyls.png?dl=1" title="Screenshot%20from%202018-09-22%2016-19-20" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f75f780a6bb70811c419855bca601cd82c945ed2_2_690x431.png" alt="Screenshot%20from%202018-09-22%2016-19-20" data-base62-sha1="zimtxgixFQAriuklj7R78B4xyls" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f75f780a6bb70811c419855bca601cd82c945ed2_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f75f780a6bb70811c419855bca601cd82c945ed2_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f75f780a6bb70811c419855bca601cd82c945ed2_2_1380x862.png 2x" data-dominant-color="9C9CAE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202018-09-22%2016-19-20</span><span class="informations">1440×900 88.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Please guide me. Where do I wrong it?<br>
Please guide me.<br>
Shahrokh</p>

---

## Post #2 by @lassoan (2018-09-22 12:20 UTC)

<p>Numpy returns (K, J, I) coordinates (voxel I, J, K coordinates in reverse order), while fiducials are defined in anatomical (R, A, S) coordinates.</p>
<p>(R, A, S) to (I, J, K) conversion is described <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_volume_voxel_coordinates_from_markup_fiducial_RAS_coordinates">here</a>, you need to perform the inverse of this operation. If you implemented the inverse script then please copy it here and we’ll post it to the script repository for future reference.</p>

---

## Post #3 by @shahrokh (2018-09-23 14:27 UTC)

<p>Dear Andras</p>
<p>Thanks a lot for your guidance. At now, I can center my sphere model in the voxel with maximum uptake. As mentioned you, firstly I changed indices array (indicesKJI, coordinates position of maximum uptake) from (K J I) to (I J K). After doing it, I calculate inverse matrix volumeRasToIjk with the name of volumeIjkToRas. Finally I applied volumeIjkToRas to indicesIJK.</p>
<p>Code written for doing it:</p>
<pre><code>#Load PET images with "DICOM" module
#Rename PET node in "Data" to PETnode
#Click on "Center Volume" in "Volumes" node
PETnode = slicer.util.getNode('PETnode')
PETnumpy = slicer.util.arrayFromVolume(PETnode)
#PETnumpy.max()
import numpy as np
indicesKJI = np.where(PETnumpy == PETnumpy.max())  
indicesIJK = [indicesKJI[2], indicesKJI[1], indicesKJI[0]]
indicesIJK = np.append(indicesIJK,1)
volumeNode = getNode('PETnode')
volumeRasToIjk = vtk.vtkMatrix4x4()
volumeNode.GetRASToIJKMatrix(volumeRasToIjk)
import numpy as np
from numpy.linalg import inv
volumeRasToIjk = np.array([[volumeRasToIjk.GetElement(0,0), volumeRasToIjk.GetElement(0,1), volumeRasToIjk.GetElement(0,2), volumeRasToIjk.GetElement(0,3)],[volumeRasToIjk.GetElement(1,0), volumeRasToIjk.GetElement(1,1), volumeRasToIjk.GetElement(1,2), volumeRasToIjk.GetElement(1,3)],[volumeRasToIjk.GetElement(2,0), volumeRasToIjk.GetElement(2,1), volumeRasToIjk.GetElement(2,2), volumeRasToIjk.GetElement(2,3)],[volumeRasToIjk.GetElement(3,0), volumeRasToIjk.GetElement(3,1), volumeRasToIjk.GetElement(3,2), volumeRasToIjk.GetElement(3,3)]])
volumeIjkToRas = inv(volumeRasToIjk)
indicesRAS = np.dot(volumeIjkToRas, indicesIJK)
sphere = vtk.vtkSphereSource()
sphere.SetRadius(10.)
sphere.SetCenter(indicesRAS[0], indicesRAS[1], indicesRAS[2])
sphere.SetPhiResolution(30)
sphere.SetThetaResolution(30)
modelsLogic = slicer.modules.models.logic()
model = modelsLogic.AddModel(sphere.GetOutput())
model.GetDisplayNode().SetSliceIntersectionVisibility(True)
model.GetDisplayNode().SetSliceIntersectionThickness(3)
model.GetDisplayNode().SetColor(1,0,0)
sphere.Update()
</code></pre>
<p>Screenshot result:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/5726ea77613f3d79e4b45521b93afeea38b5c5d9.png" data-download-href="/uploads/short-url/cqYUQhm3Njv6pjiOn0fjBHlO8Yh.png?dl=1" title="Screenshot%20from%202018-09-23%2018-53-35" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/5726ea77613f3d79e4b45521b93afeea38b5c5d9_2_690x431.png" alt="Screenshot%20from%202018-09-23%2018-53-35" data-base62-sha1="cqYUQhm3Njv6pjiOn0fjBHlO8Yh" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/5726ea77613f3d79e4b45521b93afeea38b5c5d9_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/5726ea77613f3d79e4b45521b93afeea38b5c5d9_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/5726ea77613f3d79e4b45521b93afeea38b5c5d9_2_1380x862.png 2x" data-dominant-color="D2D2D8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202018-09-23%2018-53-35</span><span class="informations">1440×900 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2018-09-23 22:37 UTC)

<p>Thanks for sharing your results.</p>
<p>You may consider adding markup fiducial points at these positions. You can set the markup shape to sphere and make it as large as you prefer, and you can easily jump to the point positions in Markups module by enabling “Click to jump slices” and clicking on a markup in the list.</p>

---
