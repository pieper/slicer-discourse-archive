---
topic_id: 9877
title: "Registration Lining Up Fiducials Into The Same Plane"
date: 2020-01-20
url: https://discourse.slicer.org/t/9877
---

# Registration - lining up fiducials into the same plane

**Topic ID**: 9877
**Date**: 2020-01-20
**URL**: https://discourse.slicer.org/t/registration-lining-up-fiducials-into-the-same-plane/9877

---

## Post #1 by @uwo27 (2020-01-20 04:58 UTC)

<p>I am registering histology and MRI images by using fiducials in the Markups module then performing initial rigid landmark registration, then going to the transforms module. I am having difficulty after transforming when aligning the 2 images (MRI and histology) so that they are in the same plane. I’ve succeeded by manually moving the 3D images but I am finding this to be very tedious, and very difficult at times. Is there anything that can automatically align the fiducials into one plane?</p>
<p>I’ve attached some sample images. The first image is one where I was able to manually align everything but case 2 I am still having difficulty and the fiducials are not all in one plane with the MRI and histology overlaying each other.</p>
<p>Case 1 (good):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94073f0be1db18972d624c8501b920293a9dafcd.jpeg" data-download-href="/uploads/short-url/l7wbP2X2Ml2eb0fcpUvMuQUfjqJ.jpeg?dl=1" title="ALSP_2_F_01_REG_BIELS" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/94073f0be1db18972d624c8501b920293a9dafcd_2_690x478.jpeg" alt="ALSP_2_F_01_REG_BIELS" data-base62-sha1="l7wbP2X2Ml2eb0fcpUvMuQUfjqJ" width="690" height="478" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/94073f0be1db18972d624c8501b920293a9dafcd_2_690x478.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/94073f0be1db18972d624c8501b920293a9dafcd_2_1035x717.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/94073f0be1db18972d624c8501b920293a9dafcd_2_1380x956.jpeg 2x" data-dominant-color="292828"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ALSP_2_F_01_REG_BIELS</span><span class="informations">1976×1370 275 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Case 2 (having problems!! bad!!):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92536b820a0faf115449ee75d0b7db13d20b4ce9.jpeg" data-download-href="/uploads/short-url/kSsr6fGEC4Bina22DN24LcvHFuF.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92536b820a0faf115449ee75d0b7db13d20b4ce9_2_681x500.jpeg" alt="Screenshot" data-base62-sha1="kSsr6fGEC4Bina22DN24LcvHFuF" width="681" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92536b820a0faf115449ee75d0b7db13d20b4ce9_2_681x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92536b820a0faf115449ee75d0b7db13d20b4ce9_2_1021x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92536b820a0faf115449ee75d0b7db13d20b4ce9_2_1362x1000.jpeg 2x" data-dominant-color="5B5B6D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1912×1402 557 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2020-01-20 08:42 UTC)

<p>Hi -</p>
<p>Sounds like an interesting use case and a workflow that would be nice to support.  If you are able to share a sample dataset and instructions for replicating the issue then I’ll bet there are some simple python commands that would help, like projecting the fiducials to a best fit plane.</p>

---

## Post #3 by @uwo27 (2020-01-20 17:01 UTC)

<p>Hi Steve -</p>
<p>I’ve uploaded a sample dataset you will be able to access here: <a href="https://www.dropbox.com/sh/n3exj9pqtb1vbhg/AADR6Aku-OnyvW9OWfncykDLa?dl=0" rel="nofollow noopener">https://www.dropbox.com/sh/n3exj9pqtb1vbhg/AADR6Aku-OnyvW9OWfncykDLa?dl=0</a>.</p>
<p>I’ve done everything prior to projecting the fiducials all into one plane, so you don’t need to worry about that. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>After loading the dataset into Slicer, double-check that ALSP_5_F_01_Biels is loaded as the foreground and 05_F_N4ITK is loaded as the background in the <strong>red slice</strong> view.</p>
<p>Thanks so much for your help and let me know if you need anything else!</p>

---

## Post #4 by @pieper (2020-02-05 19:09 UTC)

<p>Hi <a class="mention" href="/u/uwo27">@uwo27</a> -</p>
<p>Thanks for sharing the data - I finally had a chance to look at it and I am able to load it (looks like your Case 2 screenshot above). But I’m not really sure what I am looking at and what you need next.</p>
<p>In particular what is the 05_F_ALGN volume?  It looks like different slabs of brain stacked at random?  Maybe it would help to start if you could list out the nodes in the scene with a brief summary of what the data is and how you need to use it.</p>

---
