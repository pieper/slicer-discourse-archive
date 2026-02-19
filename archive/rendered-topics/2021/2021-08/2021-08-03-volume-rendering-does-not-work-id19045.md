---
topic_id: 19045
title: "Volume Rendering Does Not Work"
date: 2021-08-03
url: https://discourse.slicer.org/t/19045
---

# Volume Rendering does not work

**Topic ID**: 19045
**Date**: 2021-08-03
**URL**: https://discourse.slicer.org/t/volume-rendering-does-not-work/19045

---

## Post #1 by @Jakob_Timme (2021-08-03 16:16 UTC)

<p>Hello everyone! I am using Slicer to find 3D anatomical landmarks on lungs and was trying to use the volume rendering option, but it is not letting me use my file with this feature. Does my computer not support volume rendering or is there a certain extension I need or something else? Thanks for any help.</p>

---

## Post #2 by @muratmaga (2021-08-04 04:03 UTC)

<p>Can you tell the version of your slicer, the OS and the specs of the computer? If your gpu (or it is driver) is old, it may not render. Did you try the CPU raycasting?</p>
<p>See the documentation. <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html" class="inline-onebox" rel="noopener nofollow ugc">Volume rendering — 3D Slicer documentation</a></p>

---

## Post #3 by @Jakob_Timme (2021-08-04 20:09 UTC)

<p>I am using 3D Slicer 4.11.20210226. My OS is 64-bit operating system, x64-based processor. I have Windows 10 Home. I am trying to use binary stl files in the volume form but am not able to. I have not looked in to CPU raycasting yet but will do so! Thank you for the documentation I appreciate it.</p>

---

## Post #4 by @muratmaga (2021-08-04 20:16 UTC)

<p>STL files are 3D polygonial models. Volume Rendering is a technique that’s available only for voxel data (or volumes as it is called in Slicer), and wouldn’t be applicable to STL files. Any 3D model you load into Slicer should appear in the 3D viewer window immediately. If not, click the center 3D view button.<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#d-view" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#d-view</a></p>
<p>If the STL files shows up in your Data module but still not displayed, then it might be an issue with your computer about outdated drivers or opengl libraries.</p>

---

## Post #5 by @Jakob_Timme (2021-08-04 20:24 UTC)

<p>The STL files are displayed on my screen when I choose the model option (The options are model, segmentation, or volume). However, if I try to upload it with the volume option I get a pop up stating that an error has occured. So, STL files cannot be used with volume rendering unless they are converted to scalar volumes?</p>

---

## Post #6 by @muratmaga (2021-08-04 20:31 UTC)

<p>Yes, volume rendering is only for volumes (can be both scalar and vector).</p>

---

## Post #7 by @Jakob_Timme (2021-08-04 20:41 UTC)

<p>Got it. Thanks for your time. Is there any way to convert my STL files so that the can be rendered this way? (i.e. nrrd files)</p>

---

## Post #8 by @muratmaga (2021-08-04 22:42 UTC)

<p>If you derived these models from volumetric data via segmentation, you can bring the original data into Slicer and use the volume rendering module.</p>
<p>If these are models that are given to you, you can try to play with the materials properties (models module) along with lights module (available via sandbox extension)</p>
<p>These two will give you better rendering then converting the STL to a binary labelmap and trying to volume rrbder it.</p>

---

## Post #9 by @cpinter (2021-08-05 12:42 UTC)

<p><a class="mention" href="/u/jakob_timme">@Jakob_Timme</a> To understand better the available data formats and their purpose and possibilities, I suggest taking a look at the diagram here:<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#review-loaded-data" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#review-loaded-data</a></p>

---
