# 3D slicer bogs down and crashes when upscaling segmentation geometry

**Topic ID**: 45240
**Date**: 2025-11-26
**URL**: https://discourse.slicer.org/t/3d-slicer-bogs-down-and-crashes-when-upscaling-segmentation-geometry/45240

---

## Post #1 by @msoum (2025-11-26 16:27 UTC)

<p>Hi all,</p>
<p>I’m new to 3D Slicer, I’m trying to create a high fidelity model of my own post-craniotomy skull and currently in the process of trying to eliminate “stepping” on the model by trying to use the segmentation geometry button to oversample to a point where the stepping is not significant. However, every time I approach a point around spacing of .1, Slicer bogs down and crashes on any edits to the segmentation. No crash warning, no window, just one minute Slicer is there and the next it isn’t.</p>
<p>I am running an i9 3.7gHz 10 core CPU, 32gb of RAM and a further 80 virtual RAM on my SSD, am I drawing up too much in the way of resources to achieve this on my machine, or is there another way to accomplish what I’m looking for?</p>
<p>I’ve attached a screenshot of the current very rough segmentation, I seem to be able to threshold it at this level but if I try to remove small islands or manually remove anything it spends a few minutes cranking away and then crashes.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22bfccc7a7789d039b7921a1c2a11aa17effca65.jpeg" data-download-href="/uploads/short-url/4Xpa8enZY6exseOC7EkA6n43zJH.jpeg?dl=1" title="Screenshot_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22bfccc7a7789d039b7921a1c2a11aa17effca65_2_678x500.jpeg" alt="Screenshot_2" data-base62-sha1="4Xpa8enZY6exseOC7EkA6n43zJH" width="678" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22bfccc7a7789d039b7921a1c2a11aa17effca65_2_678x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22bfccc7a7789d039b7921a1c2a11aa17effca65_2_1017x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22bfccc7a7789d039b7921a1c2a11aa17effca65_2_1356x1000.jpeg 2x" data-dominant-color="90919E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_2</span><span class="informations">1450×1068 580 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2025-11-26 16:51 UTC)

<p>If your original spacing is say 0.5mm, and you are changing this to 0.1mm, that’s a 5x5x5 = 125 fold increase in the data volume. Yes, probably slicer is crashing out of memory error.</p>
<p>You can’t really improve the staircase effects too much with oversampling, if your original data is of lower resolution. Oversampling will simply subdivide the voxels to smaller chunks. You should use smoothing (both at the labelmap and the 3D model level) to reduce the staircase effect. Where oversampling might be be helpful, is when you have thin bones (such as the orbital wall) and when you run the smoothing you might find the hole got bigger, if you do not oversample. But even than just use an oversampling of 2 or maybe 3, keeping in mind that the size of your data will increase by the cube of the oversampling factor you are using.</p>

---

## Post #3 by @msoum (2025-11-26 18:34 UTC)

<p>I’d love if I could get to 2 or 3, unfortunately it seems like 1.75 is about where I hit a wall. I’m able to get some good detail at this point, however I do still lose quite a bit of orbital wall even before applying smoothing. Is this something that access to more capable hardware might solve, or should I call this stage as about what I can expect to get with the data I have and farm it out to someone to touch up the model in Blender or whatever other tool?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/7150ebe470c88cd38193b12b50f09a3cdffd1085.jpeg" data-download-href="/uploads/short-url/garkjcRgE13ibEXfTyzOta4tEDr.jpeg?dl=1" title="Screenshot3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7150ebe470c88cd38193b12b50f09a3cdffd1085_2_392x500.jpeg" alt="Screenshot3" data-base62-sha1="garkjcRgE13ibEXfTyzOta4tEDr" width="392" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7150ebe470c88cd38193b12b50f09a3cdffd1085_2_392x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7150ebe470c88cd38193b12b50f09a3cdffd1085_2_588x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7150ebe470c88cd38193b12b50f09a3cdffd1085_2_784x1000.jpeg 2x" data-dominant-color="798E91"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot3</span><span class="informations">838×1068 224 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @muratmaga (2025-11-26 18:40 UTC)

<p>This is probably as good as you can expect from this data. There are some deep-learning supersampling techniques that might help with the orbital wall (you apply to the original volume), but I don’t know much about them, beyond that they exist…</p>

---

## Post #5 by @pieper (2025-11-26 19:34 UTC)

<p>The crashes are almost certainly due to memory issues.  While your machine sounds good for general purpose work, you can easily rent machines with more RAM from any of the cloud providers or get access for free if you have an academic affiliation.</p>
<p>If your goal is 3D printing, then upsampling should help you preserve details and smoothness that would otherwise be lost during segmentation.</p>
<p>If your goal is mainly to visualize the data, then using volume rendering is often a more effective solution.  You may also want to combine segmentation and volume rendering using the <a href="https://discourse.slicer.org/t/new-colorize-volume-module/32254">Colorize Volume</a> module in the Sandbox extension.</p>

---
