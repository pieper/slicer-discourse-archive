---
topic_id: 20309
title: "Increment Through Slices In Sliceviews Programatically"
date: 2021-10-23
url: https://discourse.slicer.org/t/20309
---

# Increment through slices in sliceviews programatically

**Topic ID**: 20309
**Date**: 2021-10-23
**URL**: https://discourse.slicer.org/t/increment-through-slices-in-sliceviews-programatically/20309

---

## Post #1 by @Sharada (2021-10-23 04:15 UTC)

<p>Hello,</p>
<p>I am trying to display N consecutive slices of a volume in separate slice views, with each of them showing progressively increasing slices. Something like below, without the green and yellow slices.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0c4e5d9a62ff6c74de12aef9d52da52ee828e6b.png" data-download-href="/uploads/short-url/pdLSXIgdvP338Bf9LnXhJKylZgv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0c4e5d9a62ff6c74de12aef9d52da52ee828e6b_2_677x500.png" alt="image" data-base62-sha1="pdLSXIgdvP338Bf9LnXhJKylZgv" width="677" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0c4e5d9a62ff6c74de12aef9d52da52ee828e6b_2_677x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0c4e5d9a62ff6c74de12aef9d52da52ee828e6b_2_1015x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0c4e5d9a62ff6c74de12aef9d52da52ee828e6b.png 2x" data-dominant-color="10100F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1233×910 82.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there a way to do this with Python?</p>
<p>Thank you,<br>
Sharada</p>

---

## Post #2 by @rbumm (2021-10-23 13:24 UTC)

<p>Not directly the answer to your question, but the “Screen Capture” module is capable of producing an output as “lightbox (contact image) mode” <a href="https://discourse.slicer.org/t/new-lightbox-contact-image-mode-in-screen-capture-module/10840">see Link</a> . This works nicely in stable and preview versions, see LungCTAnalyzer (PDF report) for an implementation.</p>

---

## Post #3 by @Sharada (2021-10-23 16:45 UTC)

<p>This is precisely what I want! Thank you so much.</p>

---
