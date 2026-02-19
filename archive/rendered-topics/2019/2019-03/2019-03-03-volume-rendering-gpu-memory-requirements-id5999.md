---
topic_id: 5999
title: "Volume Rendering Gpu Memory Requirements"
date: 2019-03-03
url: https://discourse.slicer.org/t/5999
---

# Volume rendering GPU memory requirements

**Topic ID**: 5999
**Date**: 2019-03-03
**URL**: https://discourse.slicer.org/t/volume-rendering-gpu-memory-requirements/5999

---

## Post #1 by @hherhold (2019-03-03 21:52 UTC)

<p>One of our more recent datasets clocks in at just under 32GB. I was wondering if it would be possible to volume-render this using Slicer - does a volume need to be resident in the GPU’s on board memory in order to be volume-rendered? i.e., do you need a 32GB video card to do volume rendering on large datasets? Does it use texture memory? I was able to volume-render this on a setup using VG Studio Max 3 with a 16GB video card, but I think it was using isosurface rendering - presumably the algorithm used would matter?</p>
<p>Sorry for the pretty elementary questions, and thanks in advance for any help!</p>
<p>-Hollister</p>
<p>PS - This is not meant to start a VG Studio Max vs Slicer (or anything else) thread. I only mention it as the setup was only 16GB but the dataset is larger. Thanks!!</p>

---

## Post #2 by @muratmaga (2019-03-03 22:09 UTC)

<p>It has been more than 10 years I used VG Studio max, so do take it with a grain of salt. As I recall, it was doing volume rendering, but recasting the data range/type to something that it would fit to the GPU memory.</p>
<p>If you have 16GB card, I think you should be able render this volume in Slicer as well. I think volume renderer adjusts the level of detail to match the available GPU. But someone more qualified than me needs to answer this.</p>
<p>I am curious to learn more about this. Did you actually try?</p>

---

## Post #3 by @pieper (2019-03-04 14:45 UTC)

<p>You should be able to use CPU volume rendering with any data that fits on your machine.  For the GPU it’s harder to predict, since they memory on the card is used for many things (modern window systems use video memory for a lot of things).</p>
<p>You could use the ImageMaker to create test volumes and see what sizes succeed and fail for different graphics cards.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/Extensions/ImageMaker" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/Extensions/ImageMaker</a></p>
<p>And of course you can use CropVolume to resample the volume to a size that works for you.</p>

---
