# How does 3d slicer calculate the segmentation volume of dicom image？

**Topic ID**: 28596
**Date**: 2023-03-27
**URL**: https://discourse.slicer.org/t/how-does-3d-slicer-calculate-the-segmentation-volume-of-dicom-image/28596

---

## Post #1 by @lyh-ecnu (2023-03-27 12:23 UTC)

<p>hello,I have a project that requires a lot of calculations about the segmentation volume of dicom image.Firstly I tried to use python’s simpleitk library to calculate it,My code looks roughly like this：<br>
file = sitk.ReadImage(f’{path}{file}')<br>
spacing = file.GetSpacing()<br>
file = sitk.GetArrayFromImage(file)<br>
file=np.array(file)<br>
file = file.astype(int)<br>
<span class="hashtag">#print</span>(spacing)<br>
sum=file.sum()<br>
<span class="hashtag">#print</span>(sum)<br>
v=sum*spacing[0]*spacing[1]*spacing[2]/1000<br>
print(v)<br>
But the volume calculated in this way is not the same as the volume calculated by slicer，Where is my code going wrong? Or is there where I can see the source code for slicer to do this?thanks</p>

---

## Post #2 by @lassoan (2023-03-27 15:28 UTC)

<p>Segment statistics volume in Slicer can compute volume from binary labelmap and closed surface representations. Probably you are interested in the binary labelmap representation, from that the volume for each segment is computed by multiplying the number of voxels in the segment by the voxel size.</p>
<p>The error in your code is that the sum of label values is used instead count the number of non-zero voxels (or number of voxels that have a certain label value). I would also recommend to include the unit name in the variable names (e.g., spacing_mm, volume_mm3 or volume_cm3) to make the code more readable, safer, and easier to explain magic numbers, such as the 1000. Using <code>file</code> for so many unrelated this is quite confusing, too.</p>

---

## Post #3 by @lyh-ecnu (2023-03-28 05:06 UTC)

<p>thanks for you answer</p>

---
