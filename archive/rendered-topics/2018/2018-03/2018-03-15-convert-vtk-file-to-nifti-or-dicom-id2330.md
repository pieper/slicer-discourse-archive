---
topic_id: 2330
title: "Convert Vtk File To Nifti Or Dicom"
date: 2018-03-15
url: https://discourse.slicer.org/t/2330
---

# Convert VTK file to NIFTI or DICOM

**Topic ID**: 2330
**Date**: 2018-03-15
**URL**: https://discourse.slicer.org/t/convert-vtk-file-to-nifti-or-dicom/2330

---

## Post #1 by @Kirk_Geier (2018-03-15 14:57 UTC)

<p>HI!</p>
<p>I have the same issue (trying to convert VTK files to NIFTI or DICOM). However the solution here doesn’t seem to work for me as I’m loading in a VTK file someone else made.</p>
<p>Any solutions to how to convert these file formats without getting the same errors as above would be much appreciated!</p>
<p>Thanks<br>
Kirk</p>

---

## Post #2 by @lassoan (2018-03-15 18:23 UTC)

<p>VTK files can be anything (surface mesh, volume, volumetric mesh, etc).</p>
<p>If it is a volume file, then load it into Slicer and in the Save data dialog, choose nifti file format. You can also use the DICOM module to export to DICOM format.</p>
<p>If it is a surface mesh, you can import to into a segmentation node and export to a labelmap node using Segmentations module, then save as a volume file as described above.</p>

---

## Post #3 by @lassoan (2018-08-23 04:57 UTC)

<p>A post was split to a new topic: <a href="/t/convert-unstructured-grid-model-to-volume/3867">Convert unstructured grid model to volume</a></p>

---

## Post #4 by @elahe_heydari (2019-09-30 08:38 UTC)

<p>Hi Andras,<br>
I have this problem. I want to convert a .vtk file to .nrrd or .nifti file. I do following steps in slicer, but it doesn’t convert correctly.</p>
<ol>
<li>load data (that it dosen’t show anything)</li>
<li>use segmentation module and import model , it make a segmentation node</li>
<li>export as label map and save as nrrd</li>
</ol>
<p>when I open .nrrd file in slicer, it dosen’t show anything. I would be appreciated if you help me.<br>
Thanks<br>
Elahe</p>

---

## Post #5 by @Chris_Rorden (2019-09-30 19:41 UTC)

<p>As Andras noted, VTK files can specify meshes or they can specify volumes. They can be in a legacy format or a recent (but less popular) XML format.</p>
<p>In the event that your VTK files are volumes in legacy format, you could convert them to NIfTI using the command line <a href="https://github.com/rordenlab/i2nii" rel="nofollow noopener">i2nii</a>. Alternatively, you could view them with the graphical <a href="https://www.nitrc.org/plugins/mwiki/index.php/mricrogl:MainPage" rel="nofollow noopener">MRIcroGL</a> and then choose File/SaveNifti.</p>
<p>If they are mesh files in legacy format, you could open these using the graphical interface of <a href="https://www.nitrc.org/plugins/mwiki/index.php/surfice:MainPage" rel="nofollow noopener">Surfice</a> and use Advanced/SaveMesh to save the mesh as obj, ply, gifti format.</p>

---

## Post #6 by @lassoan (2019-09-30 20:56 UTC)

<aside class="quote no-group" data-username="elahe_heydari" data-post="4" data-topic="2330">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/elahe_heydari/48/4841_2.png" class="avatar"> elahe_heydari:</div>
<blockquote>
<p>load data (that it dosen’t show anything)</p>
</blockquote>
</aside>
<p>If nothing is shown then don’t even continue. Choose the correct content type (Volume for volume; Segmentation or Model for surface meshes) in “Add data” window in “Description” column.</p>

---

## Post #7 by @rasunag27 (2020-06-25 04:19 UTC)

<p>Hi Chris_Rorden,</p>
<p>I am actually working on a medical simulation in OpenFoam where the VTK file is obtained from Paraview. I wanted to show that into 3D Slicer for medical purpose.</p>
<p>I saw this page and tried to go with the procedure given by you. With respect to this, I have installed i2nii and tried to convert the .vtk file to NifTi format. I am getting the following error.</p>
<p><strong>Only able to read binary VTK files, not "ASCII"</strong><br>
<strong>Unable to interpret header "simulation_100.vtk"</strong></p>
<p>Here my file name is “simulation_100.vtk” . Could you please help me how to go foward with this?</p>
<p>Thanks and Regards,</p>
<p>Sunag R A.</p>

---

## Post #8 by @Chris_Rorden (2020-06-29 18:59 UTC)

<p>@ <a href="/u/rasunag27">rasunag27</a> feel free to send me a google drive or dropbox link to my personal email (you can use Discourse to send me a message if you do not know my email). I should be able to extend my software to support ASCII.</p>
<p>In general, when using a tool like Paraview to save data you should always choose to export as “binary” rather than ASCII. ASCII is inefficient in terms of disk space and read/write speed. If your data is floating point, rather than integer, one can experience rounding errors that would not be encountered if you save in the native binary format.</p>

---

## Post #9 by @lassoan (2020-07-01 01:57 UTC)

<p>I would not recommend using .vtk file format for medical images. The limitation that instantly disqualifies this file format from serious use for medical imaging that it cannot store image axis directions (it always assumes image IJK axes are the same as patient LPS axes). Also, the format can only store 4D images (so you, cannot store a 3D+t color volume) and there is no way to specify what the 4th dimension contains (color, displacement, etc.). Finally, we already have 3 other widely used file formats (nrrd, nifti, and mha), so you really don’t want to complicate things with bringing in yet another one. ParaView can read/write .mhd and read .nrrd, so if you use ParaView a lot then you may prefer to use .mhd file format.</p>
<p>You can of course convert any image formats to anything else using Slicer using the GUI (load the data set into Slicer then choose a different format when you save the data); or running this Python command:</p>
<pre><code>slicer.util.saveNode(loadVolume('/path/to/input.vtk'), '/path/to/output.nrrd')
</code></pre>
<p>but it makes your life simpler if you use the same file format across all software in your workflow.</p>

---

## Post #10 by @hui (2023-04-19 16:27 UTC)

<p>Generating dicom/nifti from vtk is easy. But this issue is how to match back to the original dicom where the vtk is made from.</p>

---
