---
topic_id: 6252
title: "How To Read Data From A Vtkmrmlscalarvolumenode"
date: 2019-03-23
url: https://discourse.slicer.org/t/6252
---

# How to read data from a vtkMRMLScalarVolumeNode

**Topic ID**: 6252
**Date**: 2019-03-23
**URL**: https://discourse.slicer.org/t/how-to-read-data-from-a-vtkmrmlscalarvolumenode/6252

---

## Post #1 by @ZiyunLiang (2019-03-23 10:13 UTC)

<p>Hi all,<br>
I’m having some problem reading data in .nii format in a vtkMRMLScalarVolumeNode in python scripted module.<br>
I currently use</p>
<blockquote>
<p>data ,header= load(‘/‘directoryodmydata’/Sag.nii.gz’)</p>
</blockquote>
<p>to read data from my dataset, and since I have loaded my image in Slicer, I want to use a different approach by reading data from the node.<br>
Is there any way to  read both the data and the header  from  the vtkMRMLScalarVolumeNode? I tried but my code didn’t  work. Does anyone know the way of implementing this?</p>
<p>Thanks for your time!<br>
Andrea</p>

---

## Post #2 by @cpinter (2019-03-23 13:33 UTC)

<p>I typically load volumes like this:</p>
<p><code>slicer.util.loadVolume('/path/to/volume')</code></p>

---

## Post #3 by @ZiyunLiang (2019-03-23 14:05 UTC)

<p>Hi, thanks for reply and sorry for I didn’t make my question clear. I know how to load a Volume, but I have problem reading data from the node. For instance, I loaded a .nii file as a volume, then I want to read the data and header data from that volume. I don’t know which function to use. Can someone help with this?</p>

---

## Post #4 by @cpinter (2019-03-23 15:14 UTC)

<p>Please specify what you mean by “reading” data from the node.</p>

---

## Post #5 by @ZiyunLiang (2019-03-23 15:24 UTC)

<p>sorry for my poor english. I mean I can achieve things like <a href="http://loli.github.io/medpy/_modules/medpy/io/load.html" rel="nofollow noopener">this.</a><br>
to load the data and header from a .nii file</p>

---

## Post #6 by @lassoan (2019-03-23 17:43 UTC)

<p>You can <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromVolume" rel="nofollow noopener">get voxels as numpy array</a> or <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Running_an_ITK_filter_in_Python_using_SimpleITK" rel="nofollow noopener">get the volume as SimpleITK image</a> as shown in several examples in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" rel="nofollow noopener">script repository</a>.</p>

---

## Post #7 by @Saima (2021-08-18 08:12 UTC)

<p>Hi Andras,<br>
If I load a vtkScalarVolume in Slicer. How can I read the header of this loaded volume within slicer if I dont want to read using nrrd.read(). I can get the data of volume using<br>
slicer.util.arrayFromVolume( <em>volumeNode</em> )<br>
but how can the header be read directly using vtkMRMLscalarvolume</p>
<p>regards,<br>
Saima Safdar</p>

---

## Post #8 by @Saima (2021-08-23 05:12 UTC)

<p>Hi Andras,<br>
If I load a vtkScalarVolume in Slicer. How can I read the header of this loaded volume within slicer if I dont want to read using nrrd.read(). I can get the data of volume using<br>
slicer.util.arrayFromVolume( <em>volumeNode</em> )<br>
but how can the header be read directly using vtkMRMLscalarvolume</p>
<p>regards,<br>
Saima Safdar</p>

---

## Post #9 by @lassoan (2021-08-23 16:35 UTC)

<p>You can get the image geometry (origin, spacing, and axis directions), voxel type, number of components, image type from the volume node. If you store other metadata in the header then you probably need to parse the header using pynrrd or similar packages.</p>
<p>What data do you need from the nrrd header?</p>

---
