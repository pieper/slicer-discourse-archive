---
topic_id: 47812
title: "Laptop requirements to do segmentation and volume rendering of wing imaginal discs"
date: 2026-08-05
url: https://discourse.slicer.org/t/47812
last_bumped: 2026-08-06T04:42:38.184Z
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
