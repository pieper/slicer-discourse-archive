---
topic_id: 22056
title: "Best Data Import Practices For Microscopy"
date: 2022-02-18
url: https://discourse.slicer.org/t/22056
---

# Best data import practices for microscopy

**Topic ID**: 22056
**Date**: 2022-02-18
**URL**: https://discourse.slicer.org/t/best-data-import-practices-for-microscopy/22056

---

## Post #1 by @muratmaga (2022-02-18 19:58 UTC)

<p>We are testing whether we can use Slicer for a project that relies on confocal stacks and I wanted to hear people’s experience.</p>
<p>First step is figuring out the data import. The original data comes in Leica’s proprietary format, we can read it into Fiji. From Fiji we can either export a multichannel TIFF (in this case two channels), or we can make a composite RGB image and export it as TIFF.</p>
<p>First option is more flexible (as we can potentially manipulate volumes individually), but as far as I can tell, it doesn’t import correctly into Slicer. Slicer simply show one slice from one volume followed by the slice from the second volume.</p>
<p>I am assuming we need to import each channel separately, if we want to process them individually?</p>
<p>If I do import RGB image, how to we control the rendering (eg., I only want to see what’s in G channel for screenshot, follwoed by joint)?</p>

---

## Post #2 by @pieper (2022-02-18 20:49 UTC)

<p>I don’t have a lot of experience with microscopy in Slicer, but I did need to load some big images one time and needed to install a python tiff library to open them and then did some manipulations to make them work cleanly with Slicer.  I would say we either need to extend ImageStacks or make a new custom module that works with the various specific formats, like SlicerHeart has for ultrasounds.</p>
<p>Some of the popular microscopy file format libraries are GPL, so we could make hooks and have the user install the packages but that shouldn’t be a big deal.  As I understand it there are dozens if not hundreds of weird proprietary variants to consider so using an external converter tools is probably the way to go.</p>

---

## Post #3 by @lassoan (2022-02-18 23:08 UTC)

<p><a href="https://ngff.openmicroscopy.org/latest/">OME-Zarr (NGFF)</a> is expected to clean up the microscopy data format mess and we plan to support that in Slicer, as a general-purpose, Python and web friendly, modern biomedical image file format.</p>
<p>Some work will still be needed to properly visualize multi-channel images, because currently we mostly expect scalar volumes (and there is some support for RGB/RGBA volumes). Sequences could be a potential data representation, as it can expose any number of channels in the scene, each as a separate scalar volume. Or we could create a new module, which could add a new displayable manager, which could show arbitrary number of layers from a multichannel image; or make the current vtkMRMLSlicerLogic smarter to support any number of channels. This all would probably require dedicated funding.</p>

---

## Post #4 by @muratmaga (2022-02-19 02:45 UTC)

<p>these all sounds great. Looking forward to it.</p>
<p>At the moment, actually importing each channel as their own volume and using the multi-volume rendering works really good. I am pleased to see shading support in multi-gpu rendering. Hopefully crop will come soon too!</p>
<p>My colleagues were quite impressed, particularly the ease of 3D navigation.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f94b75d25740d4eb82112686fc5e9529523099a3.jpeg" data-download-href="/uploads/short-url/zzmyU1D2Ws2Ei3tUiHaJKbaMYF5.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f94b75d25740d4eb82112686fc5e9529523099a3_2_525x500.jpeg" alt="image" data-base62-sha1="zzmyU1D2Ws2Ei3tUiHaJKbaMYF5" width="525" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f94b75d25740d4eb82112686fc5e9529523099a3_2_525x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f94b75d25740d4eb82112686fc5e9529523099a3_2_787x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f94b75d25740d4eb82112686fc5e9529523099a3_2_1050x1000.jpeg 2x" data-dominant-color="4F474C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1449×1380 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @muratmaga (2023-05-11 04:27 UTC)

<p>Has there been any progress in ome-zarr support, beyond a gist <a class="mention" href="/u/pieper">@pieper</a> shared a year ago? Some microscopy folks around here are interested in using Slicer, but their data is in zarr.</p>

---

## Post #6 by @pieper (2023-05-11 13:24 UTC)

<p>There’s this new extension: <a href="https://github.com/gaoyi/SlicerBigImage" class="inline-onebox">GitHub - gaoyi/SlicerBigImage: Large (GB and above) scale microscopic image computing using 3D Slicer</a></p>

---
