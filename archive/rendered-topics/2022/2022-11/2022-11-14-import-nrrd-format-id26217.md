---
topic_id: 26217
title: "Import Nrrd Format"
date: 2022-11-14
url: https://discourse.slicer.org/t/26217
---

# Import NRRD format

**Topic ID**: 26217
**Date**: 2022-11-14
**URL**: https://discourse.slicer.org/t/import-nrrd-format/26217

---

## Post #1 by @seyang (2022-11-14 01:22 UTC)

<p>Someone can provide sample NRRD format for my case?<br>
I have raw sequence images as below.<br>
slice0000.raw , slice0001.raw , slice0002, slice0003.raw…240</p>
<p>I tried to load NRRD with the help of a good person, but an error occurred.</p>
<p><strong>[Error]</strong><br>
^ vtkMRMLStorageNode::ReadData: Failed to read node slice_1 (vtkMRMLScalarVolumeNode1) from filename=‘D:/2022.09.29 CT/slice.nrrd’<br>
^ void __cdecl qSlicerIOManager::showLoadNodesResultDialog(bool,class vtkMRMLMessageCollection *) Errors occurred while loading nodes: “Error: Loading D:/2022.09.29 CT/slice.nrrd -  load failed.\n”</p>
<p><strong>[Used NRRD format]</strong><br>
NRRD0004<br>
type: ushort<br>
dimension: 3<br>
sizes: 1000 800 240<br>
encoding: raw<br>
data file: ./slice0000<br>
./slice0001<br>
./slice0002<br>
./slice0003<br>
./slice0004</p>
<p>Could you please let me know what is wrong?<br>
It will be really helpful for me.</p>

---

## Post #2 by @seyang (2022-11-14 02:53 UTC)

<p>Here is detailed error message.</p>
<p>^ vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open D:/2022.09.29 CT/X-Plane.nhdr. ITK exception info: error in unknown:  Could not create IO object for reading file D:/2022.09.29 CT/X-Plane.nhdr<br>
^   Tried to create one of the following:<br>
^     BMPImageIO<br>
^     BioRadImageIO<br>
^     DCMTKImageIO<br>
^     GDCMImageIO<br>
^     GiplImageIO<br>
^     JPEGImageIO<br>
^     LSMImageIO<br>
^     MGHImageIO<br>
^     MINCImageIO<br>
^     MRCImageIO<br>
^     MetaImageIO<br>
^     NiftiImageIO<br>
^     NrrdImageIO<br>
^     PNGImageIO<br>
^     ScancoImageIO<br>
^     StimulateImageIO<br>
^     TIFFImageIO<br>
^     VTKImageIO<br>
^     MRMLIDImageIO<br>
^   You probably failed to set a file suffix, or<br>
^     set the suffix to an unsupported type.<br>
^ Algorithm vtkITKArchetypeDiffusionTensorImageReaderFile(00000141540D0BA0) returned failure for request: vtkInformation (00000141587B0120)<br>
^   Debug: Off<br>
^   Modified Time: 209976<br>
^   Reference Count: 1<br>
^   Registered Events: (none)<br>
^   Request: REQUEST_INFORMATION<br>
^   FORWARD_DIRECTION: 0<br>
^   ALGORITHM_AFTER_FORWARD: 1<br>
^ vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open D:/2022.09.29 CT/X-Plane.nhdr. ITK exception info: error in unknown:  Could not create IO object for reading file D:/2022.09.29 CT/X-Plane.nhdr<br>
^   Tried to create one of the following:<br>
^     BMPImageIO<br>
^     BioRadImageIO<br>
^     DCMTKImageIO<br>
^     GDCMImageIO<br>
^     GiplImageIO<br>
^     JPEGImageIO<br>
^     LSMImageIO<br>
^     MGHImageIO<br>
^     MINCImageIO<br>
^     MRCImageIO<br>
^     MetaImageIO<br>
^     NiftiImageIO<br>
^     NrrdImageIO<br>
^     PNGImageIO<br>
^     ScancoImageIO<br>
^     StimulateImageIO<br>
^     TIFFImageIO<br>
^     VTKImageIO<br>
^     MRMLIDImageIO<br>
^   You probably failed to set a file suffix, or<br>
^     set the suffix to an unsupported type.<br>
^ Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries(00000141540D43E0) returned failure for request: vtkInformation (00000141587BADF0)<br>
^   Debug: Off<br>
^   Modified Time: 211490<br>
^   Reference Count: 1<br>
^   Registered Events: (none)<br>
^   Request: REQUEST_INFORMATION<br>
^   FORWARD_DIRECTION: 0<br>
^   ALGORITHM_AFTER_FORWARD: 1<br>
^ vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open D:/2022.09.29 CT/X-Plane.nhdr. ITK exception info: error in unknown:  Could not create IO object for reading file D:/2022.09.29 CT/X-Plane.nhdr<br>
^   Tried to create one of the following:<br>
^     BMPImageIO<br>
^     BioRadImageIO<br>
^     DCMTKImageIO<br>
^     GDCMImageIO<br>
^     GiplImageIO<br>
^     JPEGImageIO<br>
^     LSMImageIO<br>
^     MGHImageIO<br>
^     MINCImageIO<br>
^     MRCImageIO<br>
^     MetaImageIO<br>
^     NiftiImageIO<br>
^     NrrdImageIO<br>
^     PNGImageIO<br>
^     ScancoImageIO<br>
^     StimulateImageIO<br>
^     TIFFImageIO<br>
^     VTKImageIO<br>
^     MRMLIDImageIO<br>
^   You probably failed to set a file suffix, or<br>
^     set the suffix to an unsupported type.<br>
^ Algorithm vtkITKArchetypeImageSeriesVectorReaderFile(00000141540D56A0) returned failure for request: vtkInformation (00000141587B00D0)<br>
^   Debug: Off<br>
^   Modified Time: 211597<br>
^   Reference Count: 1<br>
^   Registered Events: (none)<br>
^   Request: REQUEST_INFORMATION<br>
^   FORWARD_DIRECTION: 0<br>
^   ALGORITHM_AFTER_FORWARD: 1<br>
^ vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open D:/2022.09.29 CT/X-Plane.nhdr. ITK exception info: error in unknown:  Could not create IO object for reading file D:/2022.09.29 CT/X-Plane.nhdr<br>
^   Tried to create one of the following:<br>
^     BMPImageIO<br>
^     BioRadImageIO<br>
^     DCMTKImageIO<br>
^     GDCMImageIO<br>
^     GiplImageIO<br>
^     JPEGImageIO<br>
^     LSMImageIO<br>
^     MGHImageIO<br>
^     MINCImageIO<br>
^     MRCImageIO<br>
^     MetaImageIO<br>
^     NiftiImageIO<br>
^     NrrdImageIO<br>
^     PNGImageIO<br>
^     ScancoImageIO<br>
^     StimulateImageIO<br>
^     TIFFImageIO<br>
^     VTKImageIO<br>
^     MRMLIDImageIO<br>
^   You probably failed to set a file suffix, or<br>
^     set the suffix to an unsupported type.<br>
^ Algorithm vtkITKArchetypeImageSeriesScalarReader(00000141540D0BA0) returned failure for request: vtkInformation (00000141587BF580)<br>
^   Debug: Off<br>
^   Modified Time: 212406<br>
^   Reference Count: 1<br>
^   Registered Events: (none)<br>
^   Request: REQUEST_INFORMATION<br>
^   FORWARD_DIRECTION: 0<br>
^   ALGORITHM_AFTER_FORWARD: 1<br>
^ vtkMRMLStorageNode::ReadData: Failed to read node X-Plane (vtkMRMLMultiVolumeNode1) from filename=‘D:/2022.09.29 CT/X-Plane.nhdr’<br>
^ ReadData: This is not a nrrd file<br>
^ vtkMRMLStorageNode::ReadData: Failed to read node X-Plane (vtkMRMLDiffusionWeightedVolumeNode1) from filename=‘D:/2022.09.29 CT/X-Plane.nhdr’<br>
^ vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Cannot read file as a volume of type DiffusionTensorVolume [fullName = D:/2022.09.29 CT/X-Plane.nhdr]: FileFormatError. Number of files listed in the node = 0. File reader says it was able to read 1 files. File reader used the archetype file name of D:/2022.09.29 CT/X-Plane.nhdr [reader 0th file name = D:/2022.09.29 CT/X-Plane.nhdr].<br>
^ vtkMRMLStorageNode::ReadData: Failed to read node X-Plane (vtkMRMLDiffusionTensorVolumeNode1) from filename=‘D:/2022.09.29 CT/X-Plane.nhdr’<br>
^ ReadData: This is not a nrrd file<br>
^ vtkMRMLStorageNode::ReadData: Failed to read node X-Plane (vtkMRMLVectorVolumeNode1) from filename=‘D:/2022.09.29 CT/X-Plane.nhdr’<br>
^ vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Failed to instantiate a file reader<br>
^ vtkMRMLStorageNode::ReadData: Failed to read node X-Plane (vtkMRMLVectorVolumeNode2) from filename=‘D:/2022.09.29 CT/X-Plane.nhdr’<br>
^ vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Cannot read file as a volume of type Volume [fullName = D:/2022.09.29 CT/X-Plane.nhdr]: FileFormatError. Number of files listed in the node = 0. File reader says it was able to read 1 files. File reader used the archetype file name of D:/2022.09.29 CT/X-Plane.nhdr [reader 0th file name = D:/2022.09.29 CT/X-Plane.nhdr].<br>
^ vtkMRMLStorageNode::ReadData: Failed to read node X-Plane (vtkMRMLScalarVolumeNode1) from filename=‘D:/2022.09.29 CT/X-Plane.nhdr’<br>
^ void __cdecl qSlicerIOManager::showLoadNodesResultDialog(bool,class vtkMRMLMessageCollection *) Errors occurred while loading nodes: “Error: Loading D:/2022.09.29 CT/X-Plane.nhdr -  load failed.\n”</p>

---

## Post #3 by @lassoan (2022-11-14 20:37 UTC)

<p>I’ve just tried this and it works flawlessly.</p>
<p>I’ve used this <code>MRHead.nhdr</code> file:</p>
<pre><code class="lang-auto">NRRD0004
# Complete NRRD file format specification at:
# http://teem.sourceforge.net/nrrd/format.html
type: unsigned short
dimension: 3
space: left-posterior-superior
sizes: 256 256 130
space directions: (0,1,0) (0,0,-1) (-1.2999954223632812,0,0)
kinds: domain domain domain
endian: little
encoding: raw
space origin: (86.644897460937486,-133.92860412597656,116.78569793701172)
data file: MRHead%04d.raw 0 129 1
</code></pre>
<p>with filenames:</p>
<ul>
<li><code>MRHead0000.raw</code></li>
<li><code>MRHead0001.raw</code></li>
<li>
<code>MRHead0002.raw</code><br>
…</li>
<li><code>MRHead0129.raw</code></li>
</ul>
<p>All the files can be downloaded from <a href="https://github.com/lassoan/PublicTestingData/releases/download/data/20221114-MultiframeNrrd.zip">here</a>.</p>

---

## Post #5 by @seyang (2022-11-15 04:21 UTC)

<p>Thanks lassoan.</p>
<p>For your advice, i found solution with someone helping.</p>

---

## Post #6 by @lassoan (2022-11-15 12:16 UTC)

<p>Could you describe what was the problem and how you solved it (just to help the next person who may run into the same difficulty)? Thank you!</p>

---

## Post #7 by @seyang (2022-11-18 06:36 UTC)

<p>Hi, I edited text to use your attached nhdr file by notpad.<br>
After editing text, it require “Enter” key one by one.<br>
If i didn’t it, the error message occurs with [This is not Nhdr file]</p>
<p>NRRD0004 <strong>[Enter]</strong><br>
type: unsigned short <strong>[Enter]</strong><br>
dimension: 3 <strong>[Enter]</strong><br>
space: left-posterior-superior <strong>[Enter]</strong><br>
sizes: 1000 800 240 <strong>[Enter]</strong><br>
space directions: (0.0277307,0,0) (0,0.0277307,0) (0,0,0.0277307) <strong>[Enter]</strong><br>
endian: little <strong>[Enter]</strong><br>
encoding: raw <strong>[Enter]</strong><br>
datafile: slice%04d.raw 0 239 1  <strong>[Enter]</strong></p>
<p>In additionally, i made .bat file. It can make NHDR file  to refer original text file.</p>
<p><a href="https://humantek-my.sharepoint.com/:u:/g/personal/sykim_humantek_onmicrosoft_com/Ect3zZ9xFAdLpWdJEB9SlXABAIERAnopIY8j7SYOK9xb9w?e=9DoETe" class="onebox" target="_blank" rel="noopener nofollow ugc">https://humantek-my.sharepoint.com/:u:/g/personal/sykim_humantek_onmicrosoft_com/Ect3zZ9xFAdLpWdJEB9SlXABAIERAnopIY8j7SYOK9xb9w?e=9DoETe</a></p>

---
