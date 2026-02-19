---
topic_id: 10091
title: "Slicerfab Incomplete Export Of Volume"
date: 2020-02-03
url: https://discourse.slicer.org/t/10091
---

# SlicerFab - Incomplete Export of Volume

**Topic ID**: 10091
**Date**: 2020-02-03
**URL**: https://discourse.slicer.org/t/slicerfab-incomplete-export-of-volume/10091

---

## Post #1 by @KTing (2020-02-03 14:55 UTC)

<p>Hello,</p>
<p>I’m fairly new to the Slicer community and am using SlicerFab to export my volume rendering to a stack of PNG’s.</p>
<p>Currently the PNG’s appear to just be multiple copies of one “layer”. It also stops after exporting only a small portion of my model. I’ve verified under the Volume Rendering module that the ROI contains the full model. I have also tried adjusting the layer thickness, but so far this only results in more/fewer of the copies being generated.</p>
<p>I’m currently using 3D Slicer 4.11.0-2019-11-19<br>
I’d appreciate any troubleshooting tips you might have for me.</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2020-02-03 15:23 UTC)

<p>Hi -</p>
<p>Thanks for the report - I’m not sure how much that module gets used/tested, but I just tried on my local build and it worked.  It’s very slow at high resolution and the image may not look much different, but if you watch the output directory you should see files being written.</p>
<p>I tested by downloading the MRHead from SampleData, turning on Volume Rendering, and then exporting bitmaps at 100dpi and 1mm layer thickness.  Does that same process work for you?  Does it stop working at higher resolution or behave differently with your data?</p>

---

## Post #3 by @KTing (2020-02-03 15:53 UTC)

<p>Thanks for your quick reply Steve.</p>
<p>I tried the process you described, exporting at 100 dpi and 1mm layer thickness. From the bitmap generator window I see the ROI moving through my model and the PNG’s being generated as expected, but when I view the images they all look the same.</p>
<p>The model has quite a few different colours throughout, so the images should all look pretty unique. When I try a larger layer thickness it creates PNG’s of a different section of my model, but those PNG’s also appear identical to each other.</p>
<p>May I ask where I can find the sample data you used?<br>
Thank you again.</p>

---

## Post #4 by @pieper (2020-02-03 16:09 UTC)

<p>Thanks for testing - I doublechecked and my pngs are all different and look correct.  A few examples below.</p>
<p>I used the SampleData module (you can get to it via the File menu).  Just click the MRHead button and it should download and show in Slicer.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c3af8ec1c059d27d4e989bedd3e19ccd148d2e3.jpeg" data-download-href="/uploads/short-url/k0xbZZprwtbBissmlkXEVPV3X6H.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c3af8ec1c059d27d4e989bedd3e19ccd148d2e3_2_253x250.jpeg" alt="image" data-base62-sha1="k0xbZZprwtbBissmlkXEVPV3X6H" width="253" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c3af8ec1c059d27d4e989bedd3e19ccd148d2e3_2_253x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c3af8ec1c059d27d4e989bedd3e19ccd148d2e3_2_379x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c3af8ec1c059d27d4e989bedd3e19ccd148d2e3_2_506x500.jpeg 2x" data-dominant-color="F5F5F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1024×1008 43.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72d103c9ec4e28ab4e8b8ee146287916bfbd7c90.jpeg" data-download-href="/uploads/short-url/gnIf74jcdHZCLDfpIuduqqF3Qt2.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72d103c9ec4e28ab4e8b8ee146287916bfbd7c90_2_253x250.jpeg" alt="image" data-base62-sha1="gnIf74jcdHZCLDfpIuduqqF3Qt2" width="253" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72d103c9ec4e28ab4e8b8ee146287916bfbd7c90_2_253x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72d103c9ec4e28ab4e8b8ee146287916bfbd7c90_2_379x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72d103c9ec4e28ab4e8b8ee146287916bfbd7c90_2_506x500.jpeg 2x" data-dominant-color="F7F7F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1024×1008 47.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @lassoan (2020-02-03 18:54 UTC)

<aside class="quote no-group" data-username="KTing" data-post="1" data-topic="10091">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/ebca7d/48.png" class="avatar"> KTing:</div>
<blockquote>
<p>I’m currently using 3D Slicer 4.11.0-2019-11-19</p>
</blockquote>
</aside>
<p>Try with the latest Slicer preview release. 3 months is very old for a Slicer Preview Release (we fix and improves things almost every day).</p>

---

## Post #6 by @KTing (2020-02-06 14:08 UTC)

<p>Thanks Steve and Andras for your help.</p>
<p>I realized the data I was using was actually a segmentation node and not a volume node, I exported them to labelmaps and that fixed my problem. I am also now using the latest Slicer release. Thanks for your patience.</p>

---
