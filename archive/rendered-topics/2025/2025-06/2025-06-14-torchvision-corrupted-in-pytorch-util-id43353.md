---
topic_id: 43353
title: "Torchvision Corrupted In Pytorch Util"
date: 2025-06-14
url: https://discourse.slicer.org/t/43353
---

# Torchvision "corrupted" in Pytorch Util

**Topic ID**: 43353
**Date**: 2025-06-14
**URL**: https://discourse.slicer.org/t/torchvision-corrupted-in-pytorch-util/43353

---

## Post #1 by @chz31 (2025-06-14 02:25 UTC)

<p>My Pytorch Util module showed TorchVision corrupted<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e4d6be8933e91fa213a2c12fe33887ea54cc7ff.png" data-download-href="/uploads/short-url/kiRFT9XLH8ZT245JUwnvlqED80n.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e4d6be8933e91fa213a2c12fe33887ea54cc7ff.png" alt="image" data-base62-sha1="kiRFT9XLH8ZT245JUwnvlqED80n" width="562" height="243"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">562×243 29.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am using Ubuntu 22.04. I have reinstalled pytorch in Pytorch Util multiple times. The Dental Segmentator &amp; Total Segmentator both used the GPU well.</p>
<p>nvidia-smi printed out the gpu information well. Install torch in a conda environment can also access GPU.</p>
<p>Should I just ignore it? Thanks!</p>

---

## Post #2 by @muratmaga (2025-06-14 02:45 UTC)

<p>This happens to be on Linux as well, and I wasn’t able to find a solution.<br>
If you don’t need the torchvision, you can ignore it. If you need the torchvision (e.g., Photogrammetry extension), you will have to use a different cuda version. 11.8 works for me.</p>

---

## Post #3 by @pieper (2025-06-14 14:17 UTC)

<p>There’s a discussion here: <a href="https://github.com/dalcalab/SlicerMultiverSeg/issues/34" class="inline-onebox">Can't install on Slicer 5.9.0 2025-05-18 on ubuntu 24.04 · Issue #34 · dalcalab/SlicerMultiverSeg · GitHub</a></p>
<p>Ultimately, installing torchvision manually with pip as suggested on the pytorch page worked.</p>
<p>It would be great if someone could figure out how to fix PyTorchUtils.</p><aside class="onebox githubissue" data-onebox-src="https://github.com/fepegar/SlicerPyTorch/issues/19">
  <header class="source">

      <a href="https://github.com/fepegar/SlicerPyTorch/issues/19" target="_blank" rel="noopener">github.com/fepegar/SlicerPyTorch</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/fepegar/SlicerPyTorch/issues/19" target="_blank" rel="noopener">Corrupted torchvision installed on ubuntu machine</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2025-06-06" data-time="20:52:24" data-timezone="UTC">08:52PM - 06 Jun 25 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/pieper" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Details are in this issue: https://github.com/dalcalab/SlicerMultiverSeg/issues/<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">34</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @chz31 (2025-06-15 03:27 UTC)

<p>Thanks! <code>/PythonSlicer -m pip install torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cu124</code> worked for me.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36441dee9e1f1721e60b416e91f55b4cef7d1a27.png" alt="image" data-base62-sha1="7K3IQ7EXa5RcCkt9lxRJsS9Jal1" width="478" height="94"></p>

---
