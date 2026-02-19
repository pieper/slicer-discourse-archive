---
topic_id: 597
title: "Help With Smoothing Models"
date: 2017-06-29
url: https://discourse.slicer.org/t/597
---

# Help with smoothing models

**Topic ID**: 597
**Date**: 2017-06-29
**URL**: https://discourse.slicer.org/t/help-with-smoothing-models/597

---

## Post #1 by @kminars (2017-06-29 14:19 UTC)

<p>Good morning everyone! I’m looking for some help with Slicer. I’m working with someone who has provided me with a CT scan of a kidney with a tumor on it. My goal is to make an .stl 3D model of the kidney and the vasculature coming off of it, that will be 3D printed.</p>
<p>I’ve managed to learn the basics and use the volume rendering and crop model modules to make a very nice looking render. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/980b5d0b03b2c7ea297d355595d11af04b81f505.jpeg" data-download-href="/uploads/short-url/lH2V8zMnQafFAtMqXHf33NVU9F3.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/980b5d0b03b2c7ea297d355595d11af04b81f505_2_464x500.jpeg" alt="image" data-base62-sha1="lH2V8zMnQafFAtMqXHf33NVU9F3" width="464" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/980b5d0b03b2c7ea297d355595d11af04b81f505_2_464x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/980b5d0b03b2c7ea297d355595d11af04b81f505_2_696x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/980b5d0b03b2c7ea297d355595d11af04b81f505.jpeg 2x" data-dominant-color="9B8F7B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">800×861 201 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’ve also managed to learn how to use the editor for label mapping to create and save an .stl file of this. The problem I’m having is that my models always come out looking like this: <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc30cb6d9c815c6dc0003eb537195a4980d3c2e4.jpeg" data-download-href="/uploads/short-url/qQOj073Icfd8XwC9RNaAIAAwsjq.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc30cb6d9c815c6dc0003eb537195a4980d3c2e4.jpeg" alt="image" data-base62-sha1="qQOj073Icfd8XwC9RNaAIAAwsjq" width="690" height="376" data-dominant-color="696866"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">700×382 52.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’ve tried using the label map smoothing module, but it doesn’t seem to actually do much.</p>
<p>Does anyone know of a good way to get models to be less jagged, and looking in the back like they’re being dragged out?</p>
<p>Thanks much!</p>

---

## Post #2 by @lassoan (2017-06-29 22:10 UTC)

<p>When you crop the volume, check <code>Isotropic spacing</code> checkbox to have cubic voxels and so avoid staircase artifacts. Then open <code>Volume information</code> section and make sure to have adjust <code>Spacing scale</code> parameter to have Cropped volume <code>Dimensions</code> values in the range of 200-500 (the higher the value is the finer details you can preserve in your model, but computation time and memory need will be increased).</p>
<p>After that, I would recommend to try the new Segment editor module instead of the legacy Editor module. Segment editor has many more effects, sophisticated smoothing methods, etc. See a tutorial about using Segment editor for 3D printing here: <a href="https://na-mic.org/w/images/a/a6/SegmentationFor3DPrinting_TutorialContestWinter2017.pdf">https://na-mic.org/w/images/a/a6/SegmentationFor3DPrinting_TutorialContestWinter2017.pdf</a></p>

---

## Post #3 by @kminars (2017-06-30 17:29 UTC)

<p>I’ll give that a try. Thank you very much for your reply!</p>

---
