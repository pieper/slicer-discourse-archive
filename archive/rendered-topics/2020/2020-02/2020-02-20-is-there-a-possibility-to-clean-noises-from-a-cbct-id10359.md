# Is there a possibility to clean noises from a CBCT?

**Topic ID**: 10359
**Date**: 2020-02-20
**URL**: https://discourse.slicer.org/t/is-there-a-possibility-to-clean-noises-from-a-cbct/10359

---

## Post #1 by @Avri_Lev (2020-02-20 03:35 UTC)

<p>Hi guys,<br>
I got this segmentation of the Maxilla. It got “noises” especially around the front teeth from URC to ULC, as you can see in the photo.<br>
Is there a way to eliminate/reduce that noise?</p>
<p>TIA<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8ae20e6435d7c9f48dda9b8a53f01f94ed20e6f3.jpeg" alt="Max Noise" data-base62-sha1="jOCdh7JkkjPfU2QfGBTMy5pg2ZR" width="483" height="392"></p>

---

## Post #2 by @lassoan (2020-02-20 04:50 UTC)

<p>You can try various noise filters of Simple Filters module (e.g., anisotropic diffusion filters) before segmentation. Then, after segmenting (using Threshold or Grow from seeds effects) you can use Smoothing effect in Segment Editor</p>

---

## Post #3 by @manjula (2020-02-20 12:10 UTC)

<p>I think you can segment this area very nicely simply through the segment editor.</p>
<p>Use simple threshold and  then keep the largest island (island effects) apply a smoothing (Median)  also you can fill holes and then apply the smoothing.</p>
<p>have a look at the tutorials ,</p>
<div class="lazyYT" data-youtube-id="MKLWzD0PiIc" data-youtube-title="Tutorial: Preparing Data for 3D Printing Using 3D Slicer" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<div class="lazyYT" data-youtube-id="KYeaj9FX7EU" data-youtube-title="DICOM to STL Conversion Tutorial with Segment Editor" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---

## Post #4 by @lassoan (2020-08-06 16:08 UTC)

<p>2 posts were merged into an existing topic: <a href="/t/re-scale-cbct-to-mdct-hu/12876/2">re scale CBCT to MDCT HU  </a></p>

---
