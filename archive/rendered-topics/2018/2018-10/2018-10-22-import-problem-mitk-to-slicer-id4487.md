---
topic_id: 4487
title: "Import Problem Mitk To Slicer"
date: 2018-10-22
url: https://discourse.slicer.org/t/4487
---

# Import problem - MITK to Slicer

**Topic ID**: 4487
**Date**: 2018-10-22
**URL**: https://discourse.slicer.org/t/import-problem-mitk-to-slicer/4487

---

## Post #1 by @Maciej84 (2018-10-22 14:18 UTC)

<p>Operating system: Win 10<br>
Slicer version: 4.9.0<br>
Expected behavior: Trying to import segmentations I made in MITK into slicer<br>
Actual behavior: Segmentations become ‘jaggedy’ -  see screen grab below, particularly occipital and temporal lobes.  Would greatly appreciate help with this as I don’t want to manually fix all these contours <img src="https://emoji.discourse-cdn.com/twitter/roll_eyes.png?v=12" title=":roll_eyes:" class="emoji" alt=":roll_eyes:" loading="lazy" width="20" height="20">  Any ideas what I might be doing wrong?  I’m thinking the axis of the MRI is different from the axis of the segmentations.  Is that something I can change in slicer?</p>
<p>Many thanks!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0df4192761b1a88da80078f2f6ec471a0a601338.jpeg" data-download-href="/uploads/short-url/1ZrbtZ4YCfITEPB8V11Yxxt3bWE.jpeg?dl=1" title="MITK" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0df4192761b1a88da80078f2f6ec471a0a601338_2_585x500.jpeg" alt="MITK" data-base62-sha1="1ZrbtZ4YCfITEPB8V11Yxxt3bWE" width="585" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0df4192761b1a88da80078f2f6ec471a0a601338_2_585x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0df4192761b1a88da80078f2f6ec471a0a601338_2_877x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0df4192761b1a88da80078f2f6ec471a0a601338.jpeg 2x" data-dominant-color="5F616A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">MITK</span><span class="informations">1018×869 89.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2018-10-22 14:19 UTC)

<p>How did you save the segmentation in MITK? As an image volume or as a surface meshes? Would you like to just visualize segmentation or further edit it?</p>

---

## Post #3 by @Maciej84 (2018-10-23 11:04 UTC)

<p>I did a bit more general digging and noticed this button:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b2a382931b726094b5a2e6b289d1cd782e4c748.jpeg" data-download-href="/uploads/short-url/d0tU4yLOxZr19fsuDRYpAwP3wOk.jpeg?dl=1" title="aligned" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b2a382931b726094b5a2e6b289d1cd782e4c748.jpeg" alt="aligned" data-base62-sha1="d0tU4yLOxZr19fsuDRYpAwP3wOk" width="690" height="325" data-dominant-color="D1D4CF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">aligned</span><span class="informations">711×335 41.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Problem fixed with a single click!  Wish it was a bit more emphasised <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
