---
topic_id: 30679
title: "Creating 3D Model Of Rat Leg Ct Scans"
date: 2023-07-19
url: https://discourse.slicer.org/t/30679
---

# Creating 3D model of rat leg µCT scans

**Topic ID**: 30679
**Date**: 2023-07-19
**URL**: https://discourse.slicer.org/t/creating-3d-model-of-rat-leg-ct-scans/30679

---

## Post #1 by @Roro82 (2023-07-19 15:51 UTC)

<p>Hello everyone,<br>
in our project we have to realize 3D modeling of a defect created on a rat leg based to µCT scans.<br>
This kind of modeling have already been done successfuly for other studies. However, the previous scans were only made in a transversal view and the µCT scans for this study were made in another way (the engine rotated around the leg). Therefore, instead of getting the 2D plans, I get a 3D view in the wrong place (in an area that shoud show a 2D view; see the screenshots below).</p>
<p>What I would like to do is getting my 3D model thanks to the segment editor (just as before).<br>
Does anyone know how to fix this issue? I have uploaded<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4db4bd1a4fbd9bed62ffe49a8f73890d29f957c.png" data-download-href="/uploads/short-url/pNVMDOZtWFUcJAbhjhgX9z2jopC.png?dl=1" title="Capture10" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4db4bd1a4fbd9bed62ffe49a8f73890d29f957c_2_690x290.png" alt="Capture10" data-base62-sha1="pNVMDOZtWFUcJAbhjhgX9z2jopC" width="690" height="290" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4db4bd1a4fbd9bed62ffe49a8f73890d29f957c_2_690x290.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4db4bd1a4fbd9bed62ffe49a8f73890d29f957c_2_1035x435.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4db4bd1a4fbd9bed62ffe49a8f73890d29f957c.png 2x" data-dominant-color="53525B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture10</span><span class="informations">1338×563 178 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f10c477bad555e9484efca43b15073b1e8260dd.jpeg" data-download-href="/uploads/short-url/29h5lbA7vkUDcUc7TbH3HTuuwW1.jpeg?dl=1" title="176 fantom" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f10c477bad555e9484efca43b15073b1e8260dd_2_690x450.jpeg" alt="176 fantom" data-base62-sha1="29h5lbA7vkUDcUc7TbH3HTuuwW1" width="690" height="450" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f10c477bad555e9484efca43b15073b1e8260dd_2_690x450.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f10c477bad555e9484efca43b15073b1e8260dd_2_1035x675.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f10c477bad555e9484efca43b15073b1e8260dd.jpeg 2x" data-dominant-color="9D9992"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">176 fantom</span><span class="informations">1338×874 95.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
screenshots of what i would like to get and the current issue.<br>
Thanks a lot for your answers and have a nice day,<br>
Romain</p>

---

## Post #2 by @pieper (2023-07-19 19:04 UTC)

<p>This probably means that whoever made the scan skipped the volume reconstruction step.  There are ways to do it with other software but usually it’s best to do it on the equipment where the scan was acquired.</p>

---

## Post #3 by @Roro82 (2023-07-20 09:51 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> Thank you very much for your answer. Do you know maybe some (free) softwares that I could use in order to do this?</p>

---

## Post #4 by @pieper (2023-07-20 12:37 UTC)

<p>You can try <a href="https://www.openrtk.org/">https://www.openrtk.org/</a></p>

---

## Post #5 by @Roro82 (2023-07-24 13:36 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> thank you for your answer. I tried to create the ITK software thanks to the CMake tool. Therefore, I uploaded the ITK sources in the CMake software (as showed in tutorials on youtube,<a href="https://youtu.be/f79joU6FTFQ" class="inline-onebox" rel="noopener nofollow ugc">ITK Install Tutorial - YouTube</a>). However, I always get an error message (see capture below); what am I doing wrong? I also precise that I use an old version (the same as the one in the tutorial) but that was exactly the same problem with the brand new version.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/324c643a61d427125b89dc0c3160d018ad6c1e2c.png" data-download-href="/uploads/short-url/7aXxzS8qP4OMx1DumYRxI4ckYWg.png?dl=1" title="error cmake and ITK" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/324c643a61d427125b89dc0c3160d018ad6c1e2c_2_632x500.png" alt="error cmake and ITK" data-base62-sha1="7aXxzS8qP4OMx1DumYRxI4ckYWg" width="632" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/324c643a61d427125b89dc0c3160d018ad6c1e2c_2_632x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/324c643a61d427125b89dc0c3160d018ad6c1e2c_2_948x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/324c643a61d427125b89dc0c3160d018ad6c1e2c_2_1264x1000.png 2x" data-dominant-color="FAF9F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error cmake and ITK</span><span class="informations">1302×1030 21.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @pieper (2023-07-28 00:42 UTC)

<p>I’m not sure.  Probably best to ask this on the ITK forum.</p>

---

## Post #7 by @jcfr (2023-07-28 02:16 UTC)

<p>Instead of building, you could look into using the associated python package. See <a href="https://pypi.org/project/itk-rtk" class="inline-onebox">itk-rtk · PyPI</a></p>

---
