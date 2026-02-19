---
topic_id: 43319
title: "Slicer 5 9 0 With Libtorch"
date: 2025-06-11
url: https://discourse.slicer.org/t/43319
---

# Slicer 5.9.0 with libtorch

**Topic ID**: 43319
**Date**: 2025-06-11
**URL**: https://discourse.slicer.org/t/slicer-5-9-0-with-libtorch/43319

---

## Post #1 by @Haoyin_Zhou (2025-06-11 15:59 UTC)

<p>hi, I am developing a c++ module on Slicer 5.9.0. I have a lot of confusion to use libtorch together with Slicer. I can compile the code but when I call a libtorch function, such as torch::jit::load(path), it crashes without given any error message.</p>
<p>In the past I used an older version Slicer (4.13.0) and it works well with libtorch.</p>
<p>Do you have any success experience to use libtorch with Slicer 5.9.0? I have tried many versions of libtorch but none of them works.</p>
<p>Thanks.</p>

---

## Post #2 by @muratmaga (2025-06-11 18:13 UTC)

<p>Is this on Linux, and what version of torch? Perhaps you are hitting the ABI issue with torch 2.7?</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/8468">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/8468" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/8468" target="_blank" rel="noopener nofollow ugc">Request for PyTorch 2.7 Support in 3D Slicer for NVIDIA Blackwell GPUs</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2025-06-05" data-time="17:00:16" data-timezone="UTC">05:00PM - 05 Jun 25 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/rodrigoteixeira7" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/215039333?v=4" class="onebox-avatar-inline" width="20" height="20">
          rodrigoteixeira7
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Request for PyTorch 2.7 Support in 3D Slicer for NVIDIA Blackwell GPUs

System I<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">nformation:
- GPU: NVIDIA GeForce RTX 5070 Ti
- Architecture: NVIDIA Blackwell
- OS: Linux Unbutu 24.04.2 LTS

PyTorch version 2.7 introduces support for the Blackwell architecture, which is required for compatibility with this GPU. Earlier versions of PyTorch (≤2.6) do not support it, resulting in the following error:
- “The current PyTorch install supports CUDA capabilities sm_50 sm_60 sm_70 sm_75 sm_80 sm_86 sm_90.”

Unfortunately, the PyTorch version currently available in 3D Slicer is&nbsp;limited&nbsp;to&nbsp;2.6

xref https://discourse.slicer.org/t/pytorch-cuda-incompatibility-with-nvidia-rtx-5070-ti/43233</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Haoyin_Zhou (2025-06-11 18:33 UTC)

<p>Thanks for your reply. I am using Ubuntu 20.04 + CUDA 12.8. My CMakeLists.txt sets C++ 17.</p>
<p>I downloaded libtorch from the following link (may need to change number)<br>
<a href="https://download.pytorch.org/libtorch/cu126/" class="onebox" target="_blank" rel="noopener nofollow ugc">https://download.pytorch.org/libtorch/cu126/</a></p>
<p>I have tried the following libtorch versions:<br>
libtorch-cxx11-abi-shared-with-deps-2.7.0+cu128<br>
libtorch-cxx11-abi-shared-with-deps-1.13.0+cu117<br>
libtorch-cxx11-abi-shared-without-deps-1.13.0+cu117<br>
[libtorch-win-shared-with-deps-2.6.0%2Bcu126</p>
<p>Is there another version I should give a try? Thanks.</p>

---

## Post #4 by @muratmaga (2025-06-11 18:55 UTC)

<aside class="quote no-group" data-username="Haoyin_Zhou" data-post="3" data-topic="43319">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/haoyin_zhou/48/3420_2.png" class="avatar"> Haoyin_Zhou:</div>
<blockquote>
<p>libtorch-cxx11-abi-shared-with-deps-2.7.0+cu128</p>
</blockquote>
</aside>
<p>I don’t think this works with Slicer, which uses an older glibc then 2.7 and cu128 requires.</p>
<aside class="quote no-group" data-username="Haoyin_Zhou" data-post="3" data-topic="43319">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/haoyin_zhou/48/3420_2.png" class="avatar"> Haoyin_Zhou:</div>
<blockquote>
<p>[libtorch-win-shared-with-deps-2.6.0%2Bcu126</p>
</blockquote>
</aside>
<p>I think this is for windows, not linux?</p>
<p>For the rest, someone with more C++ knowledge needs to chime in.</p>

---

## Post #5 by @pieper (2025-06-11 19:07 UTC)

<aside class="quote no-group" data-username="Haoyin_Zhou" data-post="1" data-topic="43319">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/haoyin_zhou/48/3420_2.png" class="avatar"> Haoyin_Zhou:</div>
<blockquote>
<p>torch::jit::load(path)</p>
</blockquote>
</aside>
<p>You usually can’t mix and match C++ compiled libraries so it’s not surprising that this crashes.  It would be best if you could compile everything from source with the same compiler (i.e. look at compiling libtorch and your other code as a <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html">superbuild extension</a>).</p>
<p>But also using Python is the suggested method of accessing torch features.  Is there a reason you want to use C++?</p>

---

## Post #6 by @Haoyin_Zhou (2025-06-13 14:21 UTC)

<p>Thank you Steve. Because there are a large amount of algorithms were implemented using C++, it is not possible for me to convert the code to Python.</p>
<p>I tried to compile libtorch from source but there are many version conflicts.</p>

---

## Post #7 by @lassoan (2025-06-13 14:50 UTC)

<p>You could build a Python wheel that uses the same build environment as PyTorch, which would ensure ABI compatibility. I would recommend this if you want to distribute your solution as a Slicer extension.</p>
<p>For a custom application, it could be enough to build a standalone version of your software that runs in a separate process. Slicer can launch it using its original startup environment, so there would be no conflict with PyTorch or any other binaries. For non-interactive use cases you can simply pass all inputs as files and fetch output from files. For interactive use cases you can communicate with the started process via web requests (for 3D images or non-time-critical applications) or OpenIGTLink (for real-time processing of image streams). There are examples for all these in existing extensions.</p>

---
