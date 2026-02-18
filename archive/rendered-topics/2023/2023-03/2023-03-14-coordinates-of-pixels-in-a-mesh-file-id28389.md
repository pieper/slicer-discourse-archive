# Coordinates of pixels in a mesh file

**Topic ID**: 28389
**Date**: 2023-03-14
**URL**: https://discourse.slicer.org/t/coordinates-of-pixels-in-a-mesh-file/28389

---

## Post #1 by @ZSoltani (2023-03-14 23:13 UTC)

<p>Hello everyone,</p>
<p>I’m trying to get the coordinates of each voxel in my model through the following code:</p>
<p>volumeNode=slicer.util.getNode(“myfile.nrrd”)<br>
ijkToRas = vtk.vtkMatrix4x4()<br>
imageData=volumeNode.GetImageData()<br>
extent = imageData.GetExtent()<br>
for k in range(extent[4], extent[5]+1):<br>
for j in range(extent[2], extent[3]+1):<br>
for i in range(extent[0], extent[1]+1):<br>
position_Ijk=[i, j, k, 1]<br>
position_Ras=ijkToRas.MultiplyPoint(position_Ijk)<br>
print(position_Ras)</p>
<p>The position_Ras are in the range of (-61.955299377441435, -57.42440032958985, 2.3572499752044687, 1.0) to (-13.861799377441436, -19.522900329589852, 21.785749975204467, 1.0) with Spacing: [0.3185, 0.3185, 0.3185] and Dimensions: (151, 119, 61).</p>
<p>So far, everything looks fine. However, when I look at my mesh generated using exported stl file in Gmsh, the node coordinates are in the range of (15.73733139,  21.27777481, 2.123630524) to (61.77390289, 56.87292862, 21.68377686).</p>
<p>Does anyone know how I can correlate these two coordinates? I need to specify which voxels are inside of an element in my mesh.</p>
<p>Thank you for your help,<br>
Zahra</p>

---

## Post #2 by @RafaelPalomar (2023-03-15 05:53 UTC)

<p>Hello <a class="mention" href="/u/zsoltani">@ZSoltani</a>, the <code>ijkToRas</code> matrix does not seem to be set properly (it is only set to default values of the <code>vtkMatri4x4</code> at creation). <code>vtkMRMLVolumeNode</code> has the <code>GetIJKToRASMatrix()</code> that you can use to populate the <code>ijkToRas</code> matrix.</p>
<p>If I understand correctly, you are comparing the extent of an image with the extent of a 3D surface model derived from the image. Most likely, the model does not occupy the whole volume of the image, but a subvolume of it, so your values are probably not going to match.</p>

---

## Post #3 by @lassoan (2023-03-15 15:47 UTC)

<p>Also note that coordinates in all files (image files, mesh files, etc) are stored in LPS coordinate system by default. In Slicer, coordinates are in RAS coordinate system.</p>

---

## Post #4 by @ZSoltani (2023-03-15 16:18 UTC)

<p>Thank you <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> and <a class="mention" href="/u/lassoan">@lassoan</a> for your replies.</p>
<p>Using volumeArray = slicer.util.array(“my-stl-file.stl”) I can get the same node coordinates as what I get from Gmsh. The only difference is that x and y coordinates have opposite signs in 3Dslicer and Gmsh and z coordinates are exactly the same. Is it a general rule? And if not, how I can transfer between two coordinate systems for a general stl file? Is it like they have different origins?</p>
<p>My second question, is about finding the coordinates of voxels inside the stl model. Sorry I’m new to 3Dslicer, and not sure how I can apply your comment correctly. Could you please explain with a short script how to do that?</p>
<p>Thank you,<br>
Zahra</p>

---

## Post #5 by @pieper (2023-03-15 16:21 UTC)

<p>Here’s a description of LPS/RAS: <a href="https://www.slicer.org/wiki/Coordinate_systems" class="inline-onebox">Coordinate systems - Slicer Wiki</a></p>
<p>Yes, it’s just a matter of knowing the convention of the software you are using and flipping the signs on the first two coordinates to convert.</p>
<p>For your second question these scripts should help: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-volume-voxel-coordinates-from-markup-control-point-ras-coordinates">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-volume-voxel-coordinates-from-markup-control-point-ras-coordinates</a></p>

---

## Post #6 by @ZSoltani (2023-03-15 16:26 UTC)

<p>Thank you Steve for your help.</p>

---
