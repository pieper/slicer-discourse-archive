---
topic_id: 24311
title: "Whats Is The Best Volume Rendering Present For The Human Bro"
date: 2022-07-14
url: https://discourse.slicer.org/t/24311
---

# Whats is the best volume rendering present for the human bronchus

**Topic ID**: 24311
**Date**: 2022-07-14
**URL**: https://discourse.slicer.org/t/whats-is-the-best-volume-rendering-present-for-the-human-bronchus/24311

---

## Post #1 by @mohammed_toro (2022-07-14 12:13 UTC)

<p>Whats is the best volume rendering present for the human bronchus</p>

---

## Post #2 by @rbumm (2022-07-14 15:21 UTC)

<p>CT-Air is a good preset:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/3049b5533fd5275706cfec923c56243183f49f58.jpeg" alt="image" data-base62-sha1="6TaPWQtsV2op6NDFjU8vh36Tmkw" width="458" height="270"></p>
<p>(volume from public dataset)</p>

---

## Post #3 by @mohammed_toro (2022-07-14 16:06 UTC)

<p>Thanks, i have tried using different dicom images but could not get a clear presentation like this. Do you have any Images for the chest that can be this clear?</p>

---

## Post #4 by @rbumm (2022-07-14 16:51 UTC)

<p>Sure, an option would be to use the CTChest from “Sample Data”:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4ed0a5e9dc26797aa784b31e898287c04203370.jpeg" data-download-href="/uploads/short-url/s65rlMux0sWqKV8fOgX29JW3iVO.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c4ed0a5e9dc26797aa784b31e898287c04203370_2_517x136.jpeg" alt="image" data-base62-sha1="s65rlMux0sWqKV8fOgX29JW3iVO" width="517" height="136" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c4ed0a5e9dc26797aa784b31e898287c04203370_2_517x136.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c4ed0a5e9dc26797aa784b31e898287c04203370_2_775x204.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c4ed0a5e9dc26797aa784b31e898287c04203370_2_1034x272.jpeg 2x" data-dominant-color="7A9094"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×507 97 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>or the DemoChestCT dataset from “Sample Data”:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2741c8fb465f2175ee3b1e7c6d511519f4149a1.jpeg" data-download-href="/uploads/short-url/nb87jYnUygY7b1SU4vC3Qxp3ylH.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a2741c8fb465f2175ee3b1e7c6d511519f4149a1_2_517x183.jpeg" alt="image" data-base62-sha1="nb87jYnUygY7b1SU4vC3Qxp3ylH" width="517" height="183" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a2741c8fb465f2175ee3b1e7c6d511519f4149a1_2_517x183.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a2741c8fb465f2175ee3b1e7c6d511519f4149a1_2_775x274.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a2741c8fb465f2175ee3b1e7c6d511519f4149a1_2_1034x366.jpeg 2x" data-dominant-color="788B8F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×682 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @rbumm (2022-07-14 17:01 UTC)

<p>But be aware: lungs will always be “in your way”. You could consider doing a real airway segmentation in order to see more details.</p>

---

## Post #6 by @mohammed_toro (2022-07-15 11:45 UTC)

<p>Still having issues getting a very good volume rendered output. Was that the output u got?. Can u send an stl file</p>

---

## Post #7 by @rbumm (2022-07-15 12:35 UTC)

<p>Yes, those were outputs I got after careful “shift” slider movements in the Volume Rendering module (3D Slicer 5). The slider is very sensitive.</p>
<p>Volume renderings do not create models or segmentations that could be transformed into STL files.<br>
Please <a href="https://discourse.slicer.org/t/save-volume-rendering-as-stl-file/524/6">see here</a> for an explanation.</p>
<p>If your end goal is to have an STL file of the airways, I would really recommend you do a proper airway <strong>segmentation</strong> with your data. Segmentation tools are available ins Slicer (see “Segment Editor”), and semiautomatic AW segmentation can be done with the Lung CT Segmenter, part of the Lung CT Analyzer extension.<br>
If that is not your end goal, pls describe it.</p>

---

## Post #8 by @mohammed_toro (2022-07-15 12:47 UTC)

<p>My end goal is to get the bronchus, as my research is related to that. I just need a clearer image, Just like the one you sent to me.</p>

---

## Post #9 by @rbumm (2022-07-15 14:48 UTC)

<p>Here is a short video, slowly on purpose, subtitles may follow:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="DjZzy5THfTE" data-video-title="Lung volume rendering in 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=DjZzy5THfTE" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/DjZzy5THfTE/maxresdefault.jpg" title="Lung volume rendering in 3D Slicer" width="" height="">
  </a>
</div>


---

## Post #10 by @mohammed_toro (2022-07-15 15:49 UTC)

<p>This Just did it!, Thanks a million. Truly appreciate.</p>

---
