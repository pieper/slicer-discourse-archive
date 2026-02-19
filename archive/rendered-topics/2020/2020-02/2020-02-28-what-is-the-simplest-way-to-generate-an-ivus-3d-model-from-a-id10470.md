---
topic_id: 10470
title: "What Is The Simplest Way To Generate An Ivus 3D Model From A"
date: 2020-02-28
url: https://discourse.slicer.org/t/10470
---

# What is the simplest way to generate an IVUS 3D model from a set of pictures or an avi?

**Topic ID**: 10470
**Date**: 2020-02-28
**URL**: https://discourse.slicer.org/t/what-is-the-simplest-way-to-generate-an-ivus-3d-model-from-a-set-of-pictures-or-an-avi/10470

---

## Post #1 by @gbolaga (2020-02-28 15:44 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c586ccdfcb944aa4448bb164f2a6d767375d001.jpeg" data-download-href="/uploads/short-url/mj5VYAIjWa6h9QbGRClA36ONepz.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c586ccdfcb944aa4448bb164f2a6d767375d001_2_447x500.jpeg" alt="image" data-base62-sha1="mj5VYAIjWa6h9QbGRClA36ONepz" width="447" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c586ccdfcb944aa4448bb164f2a6d767375d001_2_447x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c586ccdfcb944aa4448bb164f2a6d767375d001.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c586ccdfcb944aa4448bb164f2a6d767375d001.jpeg 2x" data-dominant-color="696B6B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">543×607 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-02-28 16:41 UTC)

<p>If you <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ#How_to_load_data_from_a_sequence_of_jpg.2C_tif.2C_or_png_files.3F">load a set of pictures into Slicer</a>, it will be interpreted as a 3D volume by default. You can slice through it volume render it, etc.</p>
<p>What kind of visualization or analysis would you like to do?</p>

---

## Post #3 by @gbolaga (2020-03-02 10:41 UTC)

<p>I want to be able to 3D render a vessel and its plaques from IVUS and from there being able to quantify the amount of calcium</p>

---

## Post #4 by @lassoan (2020-03-03 02:56 UTC)

<p>This should all work. After you imported your image stack as a 3D volume, go to Volumes module and set pixel size of the 2D images and distance between slices in Volume Information / Image Spacing.</p>

---

## Post #5 by @gbolaga (2020-03-03 10:17 UTC)

<p>Yes,</p>
<p>but what if I have an AVI sequence? Would this still be possible?</p>
<p>Also the next step is trying to recognize by using pixel analysis fat from calcium etc…</p>
<p>Regards,</p>
<p>Gaia Gbola</p>

---

## Post #6 by @pieper (2020-03-03 16:21 UTC)

<p>You can find lots of tools that will convert AVI files to a stack of png or jpg file, and those will load in Slicer.  Note that AVI can be a low-res format and also doesn’t store spacing information so you’ll need to fix that if you want to do anything quantitative.  As for getting out fat and calcium, you can do segmentation in Slicer.  A lot will depend on the quality of the images.  It would be better if you could get the highest possible quality images from your scanner (e.g. dicom and not AVI).</p>

---

## Post #7 by @gbolaga (2020-03-05 16:31 UTC)

<p>Thanks for the suggestion, I was able to transform the AVI file into PNG format with MATLAB, now I am trying to transfer it over to Slicer. There are around 3000 frames, so it is really taking a long time to load. Hopefully the result will be positive.</p>
<p>Regards</p>
<p>Gaia Gbola</p>

---

## Post #8 by @pieper (2020-03-05 20:28 UTC)

<p>The <a href="https://github.com/pieper/SlicerImageStacks">ImageStacks</a> module might help.  It’s still in development, but you can either install it using the instructions on the website or it comes with the <a href="https://slicermorph.github.io/">SlicerMorph</a> extension.</p>

---

## Post #9 by @gbolaga (2020-03-06 14:09 UTC)

<p>Hello,</p>
<p>could you give me any directions on how to download the image stacks module?</p>
<p>I pasted the code I found on github in my nightly but it seems not to work at all.</p>
<p>Thanks for the attention,</p>
<p>Sincerely</p>
<p>Gaia Gbola</p>

---

## Post #10 by @pieper (2020-03-06 14:33 UTC)

<p>Maybe the easiest is to get it as part of SlicerMorph:</p>
<p><a href="https://slicermorph.github.io/#two" class="onebox" target="_blank">https://slicermorph.github.io/#two</a></p>

---
