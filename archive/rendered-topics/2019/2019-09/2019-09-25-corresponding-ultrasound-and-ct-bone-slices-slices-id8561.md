---
topic_id: 8561
title: "Corresponding Ultrasound And Ct Bone Slices Slices"
date: 2019-09-25
url: https://discourse.slicer.org/t/8561
---

# Corresponding Ultrasound and CT (bone slices) slices

**Topic ID**: 8561
**Date**: 2019-09-25
**URL**: https://discourse.slicer.org/t/corresponding-ultrasound-and-ct-bone-slices-slices/8561

---

## Post #1 by @hripat (2019-09-25 13:23 UTC)

<p>We are trying to use the slicer (or plus) libraries to simulate ultrasound data from 3d bone models. We were wondering once the ultrasound slice is simulated, can a corresponding slice also be extracted from the bone model? For example, having corresponding ultrasound and ct slices(or bone model slices)? Our aim is to segment the bone surface,visible in ultrasound scan,from the bone model or ct slice.</p>
<p>We are also wondering if CT data can be used to simulate ultrasound scan rather than a segmented bone model?</p>

---

## Post #2 by @lassoan (2019-09-25 19:14 UTC)

<p>Bone segmentation in ultrasound is a very widely studied topic. It is still not a solved problem yet (although deep learning shows good potential), but we have lots of experience on how to generate “ground truth”.</p>
<aside class="quote no-group" data-username="hripat" data-post="1" data-topic="8561">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/5f8ce5/48.png" class="avatar"> hripat:</div>
<blockquote>
<p>We were wondering once the ultrasound slice is simulated, can a corresponding slice also be extracted from the bone model?</p>
</blockquote>
</aside>
<p>Yes. PLUS generates simulated images in any coordinate system you specify. You can see that the input 3D models and the generated simulated images are well aligned in 3D:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="2Oc_tCu_uzs" data-video-title="Simulated ultrasound" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=2Oc_tCu_uzs" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/2Oc_tCu_uzs/maxresdefault.jpg" title="Simulated ultrasound" width="" height="">
  </a>
</div>

<p>However, simulated ultrasound images are only useful for verifying correct image geometry (that you got image position, orientation, spacing, etc. right) but it would not likely to be usable as training data for bone segmentation (artifacts, noise patterns, etc. are just not realistic enough).</p>
<aside class="quote no-group" data-username="hripat" data-post="1" data-topic="8561">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/5f8ce5/48.png" class="avatar"> hripat:</div>
<blockquote>
<p>We are also wondering if CT data can be used to simulate ultrasound scan rather than a segmented bone model?</p>
</blockquote>
</aside>
<p>CT and US images are generated using so different principles that traditional simple automatic CT-&gt;US image generators did not create very realistic images. You may use some of your training data to set up a network that simulates US from CT, which may produce better-looking images but that is not an easy problem to solve in itself (and would consume lots of your data sets, which you could not use then for training or validation of the bone segmenter).</p>
<p>Because of these difficulties, our current approach is to generate training data sets by manual labeling of ultrasound images. You can find Slicer and Jupyter based tools for this here: <a href="https://github.com/SlicerIGT/aigt" class="inline-onebox">GitHub - SlicerIGT/aigt: Deep learning software modules for image-guided medical procedures</a></p>
<p>You can further improve on this workflow if you also have access to CT images of the same patient. You can then register the CT to the ultrasound and get the ground truth bone surface more reliably from the CT.</p>

---

## Post #3 by @hripat (2019-09-26 14:32 UTC)

<p>Thank you for your reply!</p>

---
