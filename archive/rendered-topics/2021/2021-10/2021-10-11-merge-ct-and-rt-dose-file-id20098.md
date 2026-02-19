---
topic_id: 20098
title: "Merge Ct And Rt Dose File"
date: 2021-10-11
url: https://discourse.slicer.org/t/20098
---

# Merge CT and RT Dose File

**Topic ID**: 20098
**Date**: 2021-10-11
**URL**: https://discourse.slicer.org/t/merge-ct-and-rt-dose-file/20098

---

## Post #1 by @Cody_Xie (2021-10-11 09:58 UTC)

<p>Hi to all,</p>
<p>I have three files: a <strong>CT data set</strong>, a <strong>RS structures file</strong> and a <strong>RT Dose file</strong>. After importing these three data into Slicer, I found that the CT and Dose data cannot be visualized at the same time (see the picture below). What I want to do is to <strong>visualize the Dose on CT</strong>.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7d82f211a54e9215515154a9f9ec7d3d6218687.png" data-download-href="/uploads/short-url/svUbIbK6VHFz2zHAEX4D6b0Xjef.png?dl=1" title="Slicer-Original" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7d82f211a54e9215515154a9f9ec7d3d6218687_2_690x370.png" alt="Slicer-Original" data-base62-sha1="svUbIbK6VHFz2zHAEX4D6b0Xjef" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7d82f211a54e9215515154a9f9ec7d3d6218687_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7d82f211a54e9215515154a9f9ec7d3d6218687_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7d82f211a54e9215515154a9f9ec7d3d6218687_2_1380x740.png 2x" data-dominant-color="84C086"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer-Original</span><span class="informations">1920×1030 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I read the manual SlicerVisualizationTutorial (<a href="https://spujol.github.io/SlicerVisualizationTutorial/" class="inline-onebox" rel="noopener nofollow ugc">SlicerVisualizationTutorial</a>) and used the Volume Rendering feature. However, I <strong>still cannot visualize the CT and Dose at the same time</strong>, although the two “eyes” can be opened simultaneously (see the picture below).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e52f25cce5fd077f11f096826678ee74b2cd9ce.jpeg" data-download-href="/uploads/short-url/6BNFVgjNyhveSCpaAbxHhbRid66.jpeg?dl=1" title="Slicer-Volume Rendering" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e52f25cce5fd077f11f096826678ee74b2cd9ce_2_690x370.jpeg" alt="Slicer-Volume Rendering" data-base62-sha1="6BNFVgjNyhveSCpaAbxHhbRid66" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e52f25cce5fd077f11f096826678ee74b2cd9ce_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e52f25cce5fd077f11f096826678ee74b2cd9ce_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e52f25cce5fd077f11f096826678ee74b2cd9ce_2_1380x740.jpeg 2x" data-dominant-color="8E9091"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer-Volume Rendering</span><span class="informations">1920×1030 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Could anyone give me some instructions on how to merge the CT and Dose? Any help from your side will be much appreciated!</p>

---

## Post #2 by @lassoan (2021-10-11 13:46 UTC)

<p>On a recent Slicer Preview Release, you can select the dose and CT at the same time (using Ctrl+Click) and drag-and-drop them to a view.</p>
<p>Alternatively, you can <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumes.html#overlay-two-volumes">use the slice view controls to select what volumes are shown in a view</a>.</p>

---

## Post #3 by @Cody_Xie (2021-10-11 14:04 UTC)

<p>Thank you so much Andras! I solved this problem following your guidance.</p>

---
