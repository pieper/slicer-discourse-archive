# Fail to export geometry based on DTI images to .stl file

**Topic ID**: 3171
**Date**: 2018-06-13
**URL**: https://discourse.slicer.org/t/fail-to-export-geometry-based-on-dti-images-to-stl-file/3171

---

## Post #1 by @Kewei (2018-06-13 16:04 UTC)

<p>Hi,<br>
I have generated the geometry of the brain fibers based on DTI, but when I saved the file as the *.stl file and opened it in another 3D software, I saw nothing. How can I solve this problem?<br>
Thanks,<br>
Kewei</p>

---

## Post #2 by @ihnorton (2018-06-13 16:38 UTC)

<p>Please try the <code>Export tractography to PLY (mesh)</code> module, available in the SlicerDMRI extension since early April.</p>
<p>Note that we use PLY specifically because it supports color.</p>
<p>Most software with STL import also supports PLY, but if you specifically need OBJ (supports color) or STL (no color) you can <a href="https://github.com/SlicerDMRI/SlicerDMRI/wiki/How-to-export-atlas-or-tractography-for-visualization-in-Blender">convert in MeshLab</a>.</p>

---

## Post #3 by @Kewei (2018-06-13 17:15 UTC)

<p>Hi Isaiah,<br>
Thanks for your reply. I tried based on your advice, however, when I opened the *ply file exported from 3D slicer in the MeshLab. I just saw points (not the geometry of the fibers), and the *.stl file converted from the MeshLab still contained nothing.<br>
Thanks,<br>
Kewei</p>

---

## Post #4 by @ihnorton (2018-06-13 17:36 UTC)

<p>Hi Kewei. I’ve used this module with a variety of tractography, on a mac, and meshlab 2016.12. If you want to send me a small, sample .vtk file, I can take a quick look. Save it from the vtkMRMLFiberBundleNode with the usual Save Data interface.</p>
<details>
<summary>
email</summary>
<p><code>inorton -at- partners -.- org</code></p>
</details>

---

## Post #5 by @Kewei (2018-06-13 17:41 UTC)

<p>Hi isaiah,<br>
Thanks for your advice. I need to get the permission to send my file to you. I will tell you since I get the permission done.<br>
Thanks,<br>
Kewei</p>

---

## Post #6 by @ihnorton (2018-06-13 18:10 UTC)

<p>You can test this with public data:</p>
<ul>
<li>go to Sample Data module, download <code>DTI Brain</code>
</li>
<li>use Tractography Seeding module, place a seed point (fiducial) inside the brain to generate a fiberbundle <a href="http://dmri.slicer.org/tutorials/neurosurgical_planning_dti">see this tutorial, page 59</a>
</li>
<li>export the resulting vtkMRMLFiberBundle as PLY and load to MeshLab.</li>
</ul>
<p>If the above steps don’t work, then send me the VTK from the sample data. Also please mention the OS, Slicer version, and MeshLab version.</p>

---

## Post #7 by @Kewei (2018-06-13 19:25 UTC)

<p>Kewei Bian ÒÑÓëÄã¹²Ïí OneDrive for Business ÎÄ¼þ¡£ÈôÒª²é¿´£¬Çëµ¥»÷ÏÂÃæµÄÁ´½Ó¡£</p>
<p><a href="https://uwoca-my.sharepoint.com/:u:/g/personal/kbian2_uwo_ca/EVqTnampVQFJuhDe7C0duU8BRPdb6jdybCx99qNyPIt_Vw" rel="noopener nofollow ugc"><br>
</a><br>
<a href="https://uwoca-my.sharepoint.com/:u:/g/personal/kbian2_uwo_ca/EVqTnampVQFJuhDe7C0duU8BRPdb6jdybCx99qNyPIt_Vw" rel="noopener nofollow ugc"><img width="20" src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/7/73a0286f78f4681e26d6ba244599d6b8ae97e7a8.png" height="20"></a></p>
<p><a href="https://uwoca-my.sharepoint.com/:u:/g/personal/kbian2_uwo_ca/EVqTnampVQFJuhDe7C0duU8BRPdb6jdybCx99qNyPIt_Vw" rel="noopener nofollow ugc">FiberBundle.stl</a></p>
<p><a href="https://uwoca-my.sharepoint.com/:u:/g/personal/kbian2_uwo_ca/EWxPtKQWnYtGkPVO2tr4CogBLydsMR6m1nFFwKF7z-Mtlw" rel="noopener nofollow ugc"><br>
</a><br>
<a href="https://uwoca-my.sharepoint.com/:u:/g/personal/kbian2_uwo_ca/EWxPtKQWnYtGkPVO2tr4CogBLydsMR6m1nFFwKF7z-Mtlw" rel="noopener nofollow ugc"><img width="20" src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/7/73a0286f78f4681e26d6ba244599d6b8ae97e7a8.png" height="20"></a></p>
<p><a href="https://uwoca-my.sharepoint.com/:u:/g/personal/kbian2_uwo_ca/EWxPtKQWnYtGkPVO2tr4CogBLydsMR6m1nFFwKF7z-Mtlw" rel="noopener nofollow ugc">FiberBundle.ply</a></p>
<p>Hi Isaiah,</p>
<p>I have attached the geometry based on part of sample case in *.ply and *.stl format. There are points in MeshLab when I open *.ply, which is the same as I met of my own file; the *.stl is still 1 kb, same as that of my data as well.</p>

---

## Post #8 by @ihnorton (2018-06-13 19:47 UTC)

<p>I can reproduce this kind of result if I use Save Data, then select “.stl” or “.ply” as the output format in the dropdown.</p>
<p>However, I have just tested the <code>Export tractography to PLY (mesh)</code> tool again in the latest Slicer nightly (2018-06-11), and it works as expected. I include a screenshot below; please make sure you are using that module.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75b1c696e22aaad357ed00adbd619d6a8aeeb9e8.png" alt="image" data-base62-sha1="gNaKiJmwypZiuUW3LxsdTIG9ZAA" width="445" height="436"></p>

---

## Post #9 by @Kewei (2018-06-13 20:39 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="8" data-topic="3171">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p><code>Export tractography to PLY (mesh)</code> tool</p>
</blockquote>
</aside>
<p>Hi Isaiah ,<br>
I will try the way you suggested. However, where can we get the Export tractography to PLY (mesh) tool? I can’t find it in the slicer (4.8.1, 4.9.0 and 4.5.0-1).<br>
Thanks,<br>
Kewei</p>

---

## Post #10 by @ihnorton (2018-06-13 20:52 UTC)

<aside class="quote no-group" data-username="Kewei" data-post="9" data-topic="3171">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/ee7513/48.png" class="avatar"> Kewei:</div>
<blockquote>
<p>where can we get the Export tractography to PLY (mesh) tool</p>
</blockquote>
</aside>
<p>Hi Kewei, it is available in the SlicerDMRI extension in nightly builds since early April. Sorry for the confusion, I thought it was installed already based on earlier discussion. Please see install instructions <a href="http://dmri.slicer.org/download/">here</a>.</p>

---

## Post #11 by @Kewei (2018-06-14 13:21 UTC)

<p>Hi Isaiah,<br>
I have successfully gotten the geometry based on the way you suggested.<br>
Thanks for your help!<br>
Kewei</p>

---
