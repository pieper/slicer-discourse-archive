# 3D Volume not rendering

**Topic ID**: 31687
**Date**: 2023-09-14
**URL**: https://discourse.slicer.org/t/3d-volume-not-rendering/31687

---

## Post #1 by @rishab (2023-09-14 03:38 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 5.4<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi,</p>
<p>I have loaded a .tiff stack using the Image Stack module. I have entered the spacing (0.012mm or 12 micron) data from my .vgi files and my images show in all windows except in the 3D window in the Volume Rendering module I have a big grey cube, where my objects of interest aren’t visible.</p>
<p>I have clicked the FOV button near the push pin, and the eye icon near the volume I have loaded is open. But, when I toggle the ‘Shift’ bar to the right, everything in my 3D objects gradually disappears, including the bones I am interested in.</p>
<p>When I try and load the stack using ‘Add data’, when I click Show options I don’t have the option to ‘Untick single file’.</p>
<p>Could some one please suggest why this might be happening?</p>
<p>Thanks!</p>

---

## Post #2 by @cpinter (2023-09-14 09:06 UTC)

<p>Volume rendering depends on the selected transfer function a lot. The transfer function presets are for standard data types, such as CT, MRI, etc. Reconstructing a volume from tiff files is a special case, so you probably either need to edit the transfer functions, or “calibrate” your volume to have the values similar to the original modality. What is the modality, and what is the scalar range of your volume? Also would help to know about what values do you have for bone, air, soft tissue, etc.</p>

---

## Post #3 by @rishab (2023-09-15 01:01 UTC)

<p>Thanks for the response, Csaba.</p>
<p>The modality is micro-CT (non-medical) where I have a group of 4 bones  in gel caps that I am trying to segment. I was hoping to replicate this</p>
<div class="youtube-onebox lazy-video-container" data-video-id="3hQ7bkIym_Y" data-video-title="Importing Data into 3D Slicer with ImageStacks" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=3hQ7bkIym_Y" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/3hQ7bkIym_Y/hqdefault.jpg" title="Importing Data into 3D Slicer with ImageStacks" width="" height="">
  </a>
</div>

<p>Sorry but I am not sure about the other parameters you asked for, and couldn’t find them in the info files.</p>
<p>Thanks for the help!</p>

---

## Post #4 by @lassoan (2023-09-15 01:36 UTC)

<p>MicroCTs are often uncalibrated and so of voxels values are not in Hounsfield unit but in some arbitrary range. Try the uCT presets (towards the end of the preset lists), which are designed for some commonly occurring intensity ranges.</p>

---
