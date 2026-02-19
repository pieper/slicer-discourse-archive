---
topic_id: 26802
title: "Totalsegmentator Problem Macbook M1 Max"
date: 2022-12-18
url: https://discourse.slicer.org/t/26802
---

# TotalSegmentator problem - Macbook M1 Max

**Topic ID**: 26802
**Date**: 2022-12-18
**URL**: https://discourse.slicer.org/t/totalsegmentator-problem-macbook-m1-max/26802

---

## Post #1 by @miklontzas (2022-12-18 13:11 UTC)

<p>Hi there,</p>
<p>I have been trying to use the Totalsegmentator extension in a MacBook M1 Max. The extension gets installed properly but when trying to run a segmentation for the first time, it starts installing some python packages. During the installation it gives the following error and stops “Failed to compute results. “git” is required to install TotalSegmentator”.</p>
<p>Any idea how to solve this problem?</p>

---

## Post #2 by @lassoan (2022-12-18 13:29 UTC)

<p>The message is correct, if you don’t have git on your computer already then you need to install it.</p>
<p>You can either install <a href="https://desktop.github.com/">Github desktop</a> or follow <a href="https://git-scm.com/downloads">these instructions</a>.</p>

---

## Post #3 by @miklontzas (2022-12-18 18:36 UTC)

<p>Thank you. Problem solved. Any idea if it is using the M1 Max gpu or cpu?</p>

---

## Post #4 by @rbumm (2022-12-19 09:27 UTC)

<p>TotalSegmentator will <a href="https://github.com/wasserth/TotalSegmentator/blob/9358889410a3687f3a49953f7184f8c9cd021374/README.md#usage">automatically use a CUDA-compatible GPU</a> if available, otherwise CPU.</p>
<p>As far as I see, the ARM-based M1 Max can not enable CUDA.</p>
<p>For orientation: The “total” process (–fast option) takes 47.43 seconds on an RTX 1060 Windows laptop with CUDA enabled and in GPU mode (CTChest demo dataset).</p>

---

## Post #5 by @lassoan (2022-12-19 16:08 UTC)

<p>Yes, macOS does not support either NVIDIA’s CUDA or the vendor-independent OpenCL interface. Apple has made its own proprietary metal performance shader (MPS) API available but it arrived very late to the party and it takes a while for frameworks and tools to adopt it.</p>
<p>Apple MPS is already supported at the level of AI frameworks, such as in pytorch. However, it is not supported (yet) in medical image computing frameworks (nnunet, MONAI, etc.). It is probably not a huge work for adding supporting for Apple MPS at higher levels, so it will eventually happen. I’ve submitted an issue to track the status of this in TotalSegmentator:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/wasserth/TotalSegmentator/issues/39">
  <header class="source">

      <a href="https://github.com/wasserth/TotalSegmentator/issues/39" target="_blank" rel="noopener">github.com/wasserth/TotalSegmentator</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/wasserth/TotalSegmentator/issues/39" target="_blank" rel="noopener">GPU acceleration on macOS</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-12-19" data-time="16:04:08" data-timezone="UTC">04:04PM - 19 Dec 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Many users are asking about GPU acceleration on macOS. Pytorch officially suppor<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ts MPS acceleration for MacOS 12.3+.  Do you know if there is a plan for nn-unet to support MPS for prediction?

I guess only a number of small changes would be needed at the same places where you added support for CPU for prediction.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
