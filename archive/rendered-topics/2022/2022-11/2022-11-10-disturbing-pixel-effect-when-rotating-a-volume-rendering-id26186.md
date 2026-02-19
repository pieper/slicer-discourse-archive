---
topic_id: 26186
title: "Disturbing Pixel Effect When Rotating A Volume Rendering"
date: 2022-11-10
url: https://discourse.slicer.org/t/26186
---

# Disturbing pixel effect when rotating a volume rendering

**Topic ID**: 26186
**Date**: 2022-11-10
**URL**: https://discourse.slicer.org/t/disturbing-pixel-effect-when-rotating-a-volume-rendering/26186

---

## Post #1 by @rbumm (2022-11-10 16:56 UTC)

<p>What is this pixel effect that you see when rotating a volume rendering with the mouse?<br>
Can it be avoided?</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf17d914149eee0d9f952e81c04b63bd10517cec.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf17d914149eee0d9f952e81c04b63bd10517cec.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf17d914149eee0d9f952e81c04b63bd10517cec.mp4</a>
    </source></video>
  </div><p></p>
<p>Thanks.</p>

---

## Post #2 by @pieper (2022-11-10 17:11 UTC)

<p>That happens when the adaptive mode tries to maintain frames per second while moving.</p>
<p>You can try different options in the Advanced Techniques tab.  Maximum will turn off any of the optimizations.  Turning on Surface smoothing may also help since those wood grain patterns are due to undersampling of rapid shading changes.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/8959e37a5869d8c92af608a1ce6edcf0e04ba3ea.png" data-download-href="/uploads/short-url/jB3ZVBOMUbY2oiE1IHnnnizpddE.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/8959e37a5869d8c92af608a1ce6edcf0e04ba3ea_2_517x182.png" alt="image" data-base62-sha1="jB3ZVBOMUbY2oiE1IHnnnizpddE" width="517" height="182" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/8959e37a5869d8c92af608a1ce6edcf0e04ba3ea_2_517x182.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/8959e37a5869d8c92af608a1ce6edcf0e04ba3ea.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/8959e37a5869d8c92af608a1ce6edcf0e04ba3ea.png 2x" data-dominant-color="E6E6E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">755×266 32.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Note <a class="mention" href="/u/rbumm">@rbumm</a> that the scene I sent you the other day has Maximum mode enabled, but if you switch to Normal you see a little less detail but it renders much faster.</p>

---

## Post #3 by @rbumm (2022-11-10 17:48 UTC)

<p>Thank you <a class="mention" href="/u/pieper">@pieper</a> I do not see it on my desktop and will check the laptop again tomorrow with different settings.</p>

---

## Post #4 by @muratmaga (2022-11-10 19:53 UTC)

<p>Normal usually gives quite good performance even on laptop gpus, unless the scene is very complex.</p>

---

## Post #5 by @rbumm (2022-11-11 08:10 UTC)

<p>It turns out that on the laptop (Nvidia RTX 1060) setting “Maximum” avoids the wood grain pattern but reduces fps. I’ll probably stick to “Normal”.</p>

---
