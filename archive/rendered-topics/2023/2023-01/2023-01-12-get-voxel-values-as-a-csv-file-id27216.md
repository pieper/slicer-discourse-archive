# Get voxel values as a CSV file

**Topic ID**: 27216
**Date**: 2023-01-12
**URL**: https://discourse.slicer.org/t/get-voxel-values-as-a-csv-file/27216

---

## Post #1 by @Mmirzaa1 (2023-01-12 15:52 UTC)

<p>Dear Andras<br>
Could you please determine how (using the code above) we can extract the voxel values as a table? or a csv file? thank you very much</p>

---

## Post #2 by @Mmirzaa1 (2023-01-12 16:14 UTC)

<p>Dear Andras<br>
To be more clear about my previous question, would it be possible to extract each voxel value with the corresponding X,Y,Z numbers, meaning the possibility of tabulating each voxels value with the exact location of the voxel<br>
thank you very much</p>

---

## Post #3 by @lassoan (2023-01-12 17:51 UTC)

<p>You can get the voxels as a numpy array (<code>a=array('MyVolumeName')</code>) and then use standard numpy functions (see for example <a href="https://stackoverflow.com/questions/46852741/python-storing-values-in-a-3d-array-to-csv">here</a>).</p>
<p>However, I would not recommend doing this. Representing an image as a CSV file (one line per voxel) would be a horribly inefficient. Reading or processing would take several magnitudes longer time than using a standard 3D array representation (e.g., an operation that normally takes 0.1 second would take 100 seconds).</p>
<p>What would you like to compute from this CSV file?</p>

---
