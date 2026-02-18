# Add Data for VTK volume fails

**Topic ID**: 1572
**Date**: 2017-12-01
**URL**: https://discourse.slicer.org/t/add-data-for-vtk-volume-fails/1572

---

## Post #1 by @JBC (2017-12-01 12:14 UTC)

<p>Dears,</p>
<p>I have a VTI volume image which I use in Paraview and would like to use it in Slicer. Therefore, I exported it in Paraview to legacy VTK format. However, loading the file via ‘Add Data’ in Slicer fails.</p>
<p>The error log gives me the two messages listed below. Until now I could not identify the cause for this.<br>
Would be great if there is somebody who can help.</p>
<p>I am new to slicer and would like to use it due to its potentially better support for manual segmentation of 3D Volumes than provided by Paraview.</p>
<p>Thanks!</p>
<p>1.)<br>
Premature EOF in reading a line</p>
<p>Algorithm vtkITKArchetypeDiffusionTensorImageReaderFile(0x1300ab560) returned failure for request: vtkInformation (0x628000a74340)<br>
Debug: Off<br>
Modified Time: 1196867<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
ALGORITHM_AFTER_FORWARD: 1<br>
FORWARD_DIRECTION: 0</p>
<p>Premature EOF in reading a line</p>
<p>Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries(0x1300a5850) returned failure for request: vtkInformation (0x628000a66100)<br>
Debug: Off<br>
Modified Time: 1198427<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
ALGORITHM_AFTER_FORWARD: 1<br>
FORWARD_DIRECTION: 0</p>
<p>Premature EOF in reading a line</p>
<p>Algorithm vtkITKArchetypeImageSeriesVectorReaderFile(0x1300a7ec0) returned failure for request: vtkInformation (0x628000a6d840)<br>
Debug: Off<br>
Modified Time: 1198530<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
ALGORITHM_AFTER_FORWARD: 1<br>
FORWARD_DIRECTION: 0</p>
<p>2.)<br>
Premature EOF in reading a line</p>
<p>Algorithm vtkITKArchetypeImageSeriesScalarReader(0x13d734620) returned failure for request: vtkInformation (0x600000e7abc0)<br>
Debug: Off<br>
Modified Time: 1199340<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
ALGORITHM_AFTER_FORWARD: 1<br>
FORWARD_DIRECTION: 0</p>
<p>ReadData: This is not a nrrd file</p>
<p>ReadData: Cannot read file as a volume of type DiffusionTensorVolume[fullName = /Volumes/LaCie_RAID_0/Schutzwald/Scans_Export/Herrschaft_48347/regeneration_cluster/hs48347_nopole_005-to-010m_q1_res01_te1e-4_ryx05_rz3_syx1-35_sz11_ss3-5_sw_NCUT_CONSTRAINED_MRF_NOBGC_Mngroups_clusters.vtk]<br>
Number of files listed in the node = 0.<br>
File reader says it was able to read 1 files.<br>
File reader used the archetype file name of /Volumes/LaCie_RAID_0/Schutzwald/Scans_Export/Herrschaft_48347/regeneration_cluster/hs48347_nopole_005-to-010m_q1_res01_te1e-4_ryx05_rz3_syx1-35_sz11_ss3-5_sw_NCUT_CONSTRAINED_MRF_NOBGC_Mngroups_clusters.vtk [reader 0th file name = /Volumes/LaCie_RAID_0/Schutzwald/Scans_Export/Herrschaft_48347/regeneration_cluster/hs48347_nopole_005-to-010m_q1_res01_te1e-4_ryx05_rz3_syx1-35_sz11_ss3-5_sw_NCUT_CONSTRAINED_MRF_NOBGC_Mngroups_clusters.vtk]<br>
FileFormatError</p>
<p>ReadData: This is not a nrrd file</p>
<p>ReadData: Failed to instantiate a file reader</p>
<p>ReadData: Cannot read file as a volume of type Volume[fullName = /Volumes/LaCie_RAID_0/Schutzwald/Scans_Export/Herrschaft_48347/regeneration_cluster/hs48347_nopole_005-to-010m_q1_res01_te1e-4_ryx05_rz3_syx1-35_sz11_ss3-5_sw_NCUT_CONSTRAINED_MRF_NOBGC_Mngroups_clusters.vtk]<br>
Number of files listed in the node = 0.<br>
File reader says it was able to read 1 files.<br>
File reader used the archetype file name of /Volumes/LaCie_RAID_0/Schutzwald/Scans_Export/Herrschaft_48347/regeneration_cluster/hs48347_nopole_005-to-010m_q1_res01_te1e-4_ryx05_rz3_syx1-35_sz11_ss3-5_sw_NCUT_CONSTRAINED_MRF_NOBGC_Mngroups_clusters.vtk [reader 0th file name = /Volumes/LaCie_RAID_0/Schutzwald/Scans_Export/Herrschaft_48347/regeneration_cluster/hs48347_nopole_005-to-010m_q1_res01_te1e-4_ryx05_rz3_syx1-35_sz11_ss3-5_sw_NCUT_CONSTRAINED_MRF_NOBGC_Mngroups_clusters.vtk]<br>
FileFormatError</p>

---

## Post #2 by @pieper (2017-12-01 13:05 UTC)

<p>I’m guessing the exported file contains more than just a single scalar volume (slicer is trying to extract a tensor from it).  Probably in paraview you can find filters to export only the scalar you want to edit that would load directly in Slicer.  Or you could write a python script in Slicer to load the file and extract the part you want (same VTK filters would work in either program).  If you want to post an example file we could make suggestions.</p>

---

## Post #3 by @lassoan (2017-12-01 14:50 UTC)

<p>For saving images from Paraview, use either “Legacy VTK files(<em>.vtk)" or "Meta Image Files(</em>.mhd)”. Note: If you choose .vtk format then when you open the volume in Slicer, choose “Volume” in the Description column in “Add data…” dialog.</p>
<p>What do you need to do in Paraview? Paraview is great for mesh manipulation but rather limited for images: it ignores image orientation, cannot load compressed MetaIO image, NRRD, many other common image formats, rendering capabilities are very basic, no image editing, virtually no image filtering capabilities, reslicing is extremely slow, no orthogonal slice view, etc.</p>

---

## Post #4 by @JBC (2017-12-12 11:32 UTC)

<p>Thank you for your suggestions. The vtk file has only one data array of type double.<br>
It is a bit curious, but sometimes, after repeated trials to open the file, it is listed in the data module panel. However, I can not visualize it or do anything with it. I am using Slicer 4.8 on a Mac.<br>
I would like to upload a sample, but unfortunately only standard image formats (jpg, etc.) are allowed. Therefore, I copy the ASCII version of the sample vtk file below. At least in Paraview one can load it and export it as binary if required.</p>
<pre><code class="lang-auto"># vtk DataFile Version 4.2
vtk output
ASCII
DATASET STRUCTURED_POINTS
DIMENSIONS 11 11 11
SPACING 1 1 1
ORIGIN 0 0 0
CELL_DATA 1000
FIELD FieldData 1
image 1 1000 double
1 1 0 1 1 1 1 1 1 
1 1 1 0 0 1 1 1 1 
1 1 0 0 0 0 0 1 1 
1 1 1 0 0 0 0 0 0 
0 0 1 1 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
1 0 0 0 0 0 0 0 0 
0 1 0 0 0 1 1 1 1 
1 1 0 0 0 0 1 1 1 
1 1 1 0 0 0 0 0 1 
1 1 1 1 0 0 0 0 0 
0 1 1 1 1 0 0 0 0 
0 0 1 1 0 0 0 0 0 
0 0 0 1 1 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 1 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 1 0 0 0 1 1 1 
1 1 1 0 0 0 0 1 1 
1 1 1 1 0 0 0 0 1 
1 1 1 1 1 0 0 0 0 
0 1 1 1 1 0 0 0 0 
0 0 1 1 1 0 0 0 0 
0 0 0 0 1 1 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 1 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 1 1 
1 1 1 1 0 0 0 0 0 
0 0 0 0 1 0 0 0 0 
1 1 1 1 0 1 0 0 0 
0 1 1 1 1 0 0 0 0 
0 0 0 1 0 1 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 1 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
1 1 1 1 0 0 0 0 0 
0 0 0 1 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 1 0 1 1 0 0 
0 0 0 0 1 1 1 0 0 
0 0 0 0 0 1 0 0 0 
0 0 1 0 0 0 1 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 1 1 0 0 0 0 
0 0 0 1 1 1 1 0 1 
1 1 0 0 1 1 1 1 0 
1 1 1 1 1 1 0 1 0 
0 0 1 1 1 1 1 0 0 
0 0 0 0 0 0 0 1 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 1 1 0 0 0 
0 1 0 0 0 0 0 0 1 
0 1 1 1 1 1 0 0 0 
0 0 0 1 1 1 1 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 1 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 1 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 
METADATA
INFORMATION 0
</code></pre>

---

## Post #5 by @JBC (2017-12-12 12:07 UTC)

<p>Thanks for your help. I did everything as you described, except of the mhd format, which does not work to export from vti or vtk in Paraview. I wanted to test slicer for manually delineating single objects from a volumetric image. Paraview has some tools for voxel selection, but they are relatively basic and do not work well for accuate delineation of details.</p>

---

## Post #6 by @lassoan (2017-12-12 13:56 UTC)

<p>Have you found a solution for all your questions or there are still things that don’t work yet?</p>
<p>To share a large file, upload the file to dropbox and copy-paste the link into your post.</p>

---

## Post #7 by @JBC (2017-12-13 12:16 UTC)

<p>No, unfortunately still unsolved. The small ascii vtk file in my respond to Steve Pieper should work for demonstrating the problem.<br>
Note: A ‘number sign’ or ‘hash’ should be added as first character to the first line ‘vtk DataFile Version 4.2’ (/# vtk DataFile Version 4.2), which probably is just a comment for the vtk reader (I tried to ‘escape’ the symbol, but it seemed that it did not work).</p>

---

## Post #8 by @ihnorton (2017-12-13 20:26 UTC)

<p>I think that dataset can only be read by <code>vtkStructuredPointsReader</code>, which it looks like Slicer does not use (from a quick grep).</p>

---

## Post #9 by @JBC (2017-12-14 09:43 UTC)

<p>‘Structured Points’ is what Paraview exports me as legacy VTK after reading a VTI file. I do not have a choice. However, I discovered that after some filtering (thresholding) Paraview exports me an ‘unstrucered grid’ as legacy VTK from the same original file.<br>
Still, it cannot be read by Slicer.</p>
<p>Below I copy the ascii version of this type of VTK files (an even smaller subset as posted before):</p>
<pre><code># vtk DataFile Version 4.2
vtk output
ASCII
DATASET UNSTRUCTURED_GRID
POINTS 64 float
0 0 0 1 0 0 0 1 0 
1 1 0 0 0 1 1 0 1 
0 1 1 1 1 1 2 0 0 
2 1 0 2 0 1 2 1 1 
3 0 0 3 1 0 3 0 1 
3 1 1 0 2 0 1 2 0 
0 2 1 1 2 1 2 2 0 
2 2 1 3 2 0 3 2 1 
0 3 0 1 3 0 0 3 1 
1 3 1 2 3 0 2 3 1 
3 3 0 3 3 1 0 0 2 
1 0 2 0 1 2 1 1 2 
2 0 2 2 1 2 3 0 2 
3 1 2 0 2 2 1 2 2 
2 2 2 3 2 2 0 3 2 
1 3 2 2 3 2 3 3 2 
0 0 3 1 0 3 0 1 3 
1 1 3 2 0 3 2 1 3 
3 0 3 3 1 3 0 2 3 
1 2 3 2 2 3 3 2 3 
0 3 3 1 3 3 2 3 3 
3 3 3 
METADATA
INFORMATION 1
NAME L2_NORM_RANGE LOCATION vtkDataArray
DATA 2 0 5.19615 

CELLS 27 243
8 0 1 2 3 4 5 6 7 
8 1 8 3 9 5 10 7 11 
8 8 12 9 13 10 14 11 15 
8 2 3 16 17 6 7 18 19 
8 3 9 17 20 7 11 19 21 
8 9 13 20 22 11 15 21 23 
8 16 17 24 25 18 19 26 27 
8 17 20 25 28 19 21 27 29 
8 20 22 28 30 21 23 29 31 
8 4 5 6 7 32 33 34 35 
8 5 10 7 11 33 36 35 37 
8 10 14 11 15 36 38 37 39 
8 6 7 18 19 34 35 40 41 
8 7 11 19 21 35 37 41 42 
8 11 15 21 23 37 39 42 43 
8 18 19 26 27 40 41 44 45 
8 19 21 27 29 41 42 45 46 
8 21 23 29 31 42 43 46 47 
8 32 33 34 35 48 49 50 51 
8 33 36 35 37 49 52 51 53 
8 36 38 37 39 52 54 53 55 
8 34 35 40 41 50 51 56 57 
8 35 37 41 42 51 53 57 58 
8 37 39 42 43 53 55 58 59 
8 40 41 44 45 56 57 60 61 
8 41 42 45 46 57 58 61 62 
8 42 43 46 47 58 59 62 63 

CELL_TYPES 27
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11
11

CELL_DATA 27
FIELD FieldData 1
image 1 27 double
1 1 0 1 1 0 0 0 0 
1 0 0 0 0 0 0 0 0 
1 0 0 0 0 0 0 0 0 

METADATA
INFORMATION 0</code></pre>

---

## Post #10 by @JBC (2017-12-14 09:54 UTC)

<p>Ok, I’ve just detected, that the ‘unstructered grid’ type of my VTK file can be read as Model, but still not as Volume. I guess, this is not what I need, since I do not have access to the image array values. in Slicer software documentation legacy VTK is listed as supported file format for Volumes.</p>

---
