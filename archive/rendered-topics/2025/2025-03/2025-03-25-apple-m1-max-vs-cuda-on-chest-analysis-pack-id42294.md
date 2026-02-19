---
topic_id: 42294
title: "Apple M1 Max Vs Cuda On Chest Analysis Pack"
date: 2025-03-25
url: https://discourse.slicer.org/t/42294
---

# Apple M1 Max vs CUDA on chest analysis pack

**Topic ID**: 42294
**Date**: 2025-03-25
**URL**: https://discourse.slicer.org/t/apple-m1-max-vs-cuda-on-chest-analysis-pack/42294

---

## Post #1 by @kirion (2025-03-25 12:40 UTC)

<p>Hi, I am running the chest platform on a Mac M1 Max, but it seems too slow as it looks for CUDA instead of the MPS. Does anyone knows how to set it for apple M1 Max processors, please?</p>

---

## Post #2 by @jamesobutler (2025-03-25 15:31 UTC)

<p>You are using SlicerTotalSegmentator?</p>
<p>I have detailed some development work that is required to get full MPS support working and needs a developer to help champion this work:</p>
<aside class="quote quote-modified" data-post="2" data-topic="41611">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/gpu-not-detected-total-segmentation/41611/2">GPU not detected Total Segmentation</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    <a href="https://github.com/wasserth/TotalSegmentator" rel="noopener nofollow ugc">TotalSegmentator</a> appears to have added the option for MPS where your Mac Pro AMD Radeon Pro Vega II card supports the <a href="https://pytorch.org/docs/stable/notes/mps.html" rel="noopener nofollow ugc">mps</a> backend for PyTorch. 
It does seem to be a bit on the untested and new side as the following place in the readme hasn’t been updated to reflect the mps option although you can see that --device does allow the “mps” option. 


The SlicerTotalSegmentator utilizes the TotalSegmentator python package, but will need to be updated to handle the MPS option as right now if it doesn’t…
  </blockquote>
</aside>

<p>Also note that Slicer only provides x86_64 binaries, so on macOS you won’t be able to utilize latest PyTorch since the torch developers dropped support for x86_64. This means things may still not be optimized for your system. Building Slicer native arm64 builds for macOS is work still in progress by the Slicer developers.</p>

---

## Post #3 by @kirion (2025-04-14 09:56 UTC)

<p>Hi James,</p>
<p>I am not sure if you have received my prior reply to your message.</p>
<p>Yes I am trying to use totalsegmentator but it is too slow on my MAC and I would be really keen to get it adapted, as I do not want to change my computer, which should be fast enough if not relying on CUDA.</p>
<p>Kind regards</p>
<p>Klaus</p>

---
