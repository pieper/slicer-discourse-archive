---
topic_id: 47812
title: "Laptop requirements to do segmentation and volume rendering of wing imaginal discs"
date: 2026-08-05
url: https://discourse.slicer.org/t/47812
last_bumped: 2026-08-06T15:34:24.088Z
---

# Laptop requirements to do segmentation and volume rendering of wing imaginal discs

**Topic ID**: 47812
**Date**: 2026-08-05
**URL**: https://discourse.slicer.org/t/laptop-requirements-to-do-segmentation-and-volume-rendering-of-wing-imaginal-discs/47812

---

## Post #1 by @FlylabCHG (2026-08-05 20:14 UTC)

<p>I would like to know if anyone is using 3-D Slicer to segment wing imaginal discs of Drosophila larvae. I take images of discs that are too small to be isolated out of the larvae. They are labelled with gfp expression and the images are taken using a Zeiss micrsocope fitted with Apotome. The images are in the form of TIFF stacks, upto about 77 slices (each slice is 968x728 pixels) and about 100MB in size. I can do the segmentation either using interpolater or seed grower.</p>
<p>I have tried it on a standard laptop and find it hangs frequently. I need to know what the system requirements are.</p>

---

## Post #2 by @mikebind (2026-08-06 02:34 UTC)

<p>You might try using SlicerMorph on your current laptop.  There are easy-to-use ways to load your tiff stack at 1/2 resolution (1/8th memory required because you get three factors of two reduction in voxels), and then you can use that to decide on a tighter crop box which contains the region of interest for segmentation.  You may then be able to load and work with the segmenting the cropped version at full resolution.</p>
<p>In terms of hardware requirements, the suggestion I’ve seen elsewhere on the forum is a comfortable amount of RAM is 10x the size of the image volume memory footprint (in your case, 77x928x728x(bytes per pixel); or, if the whole stack is approx 100MB, then ~1 GB of memory should work fine).  If the whole stack is (100MB x 77), then the rule of thumb would suggest  ~77 GB of memory. I think the rule of thumb is based on the idea that you might temporarily have two copies of your data (or two images open) during processing, plus a complex segmentation might add up to approximately another copy of your data, plus a comfortable amount of processing overhead so that it would be very rare to completely run out of available memory.</p>

---

## Post #3 by @muratmaga (2026-08-06 04:42 UTC)

<aside class="quote no-group" data-username="FlylabCHG" data-post="1" data-topic="47812">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/f4b2a3/48.png" class="avatar"> FlylabCHG:</div>
<blockquote>
<p>77 slices (each slice is 968x728 pixels)</p>
</blockquote>
</aside>
<p>968x728x77 is only 100MB (assuming 16 bit tiff, or 200MB is it is RGBA). Any modern laptop should be able handle that fairly easily. You don’t really need any powerful computer. Depending on where it hangs (e.g., volume rendering), this might be more of a driver issue, or possibly a quite slow and old integrated GPU or using wrong rendering technique (e.g., do not use MultiVolume or CPURaycasting, make sure it is GPURaycasting). You didn’t tell what laptop and specs you are using, so hard to guess.</p>
<p>What version of Slicer  are you using?</p>

---

## Post #4 by @FlylabCHG (2026-08-06 05:54 UTC)

<p>Dear Murat and Mike,</p>
<p>I apologise for misleading you. My image file is actually approximately 900MB in size. I can reduce the file size by cropping the image and removing a proportion of the slices in the stack. So, the final size could be about 928x350x65 pixels.</p>
<p>I am currently using a laptop with the following specs:<br>
Storage: 477GB, (200GB used)<br>
Graphics Card: 128MB, Intel(R) Iris(R) Xe Graphics<br>
Installed RAM: 16 GB, Speed 2667 MT/s<br>
Processor; 13th Gen Intel(R) Core™ i5-1334U, Speed is 1.30GHz</p>
<p>The problem may be that the processor speed is too slow and it does not have a dedicated NVIDIA GeForce GTX graphics card. I am considering buying the following laptop:</p>
<p>HP Victus, 14th Gen Intel Core i5-14450HX, with the following relevant specs:</p>
<ul>
<li>Processor, Memory &amp; Storage: Intel Core i5-14450HX (up to 4.8 GHz with Intel Turbo Boost Technology, 20 MB L3 cache, 10 cores, 16 threads)| Memory: 24 GB DDR5-5600 MT/s (1 x 24 GB)| Storage: 512 GB PCIe NVMe M.2 SSD</li>
<li>Graphics: NVIDIA GeForce RTX 3050 6GB<br>
It has Windows 11 installed.</li>
</ul>
<p>However, if the laptop I already have can do the job, but with better use of the software, then I could consider not buying this new laptop.</p>
<p>Thank you so much for your help in this matter.</p>
<p>Best wishes,</p>
<p>Carmen.</p>
<p>Look forward to your response.</p>
<p>Thank you very much.</p>

---

## Post #5 by @muratmaga (2026-08-06 15:34 UTC)

<p>I dont have experience with those Intel integrated gpus, but specs on your existing laptop seems low. You will probably have much better performance on the new one, particularly with that dedicated gpu.</p>

---
