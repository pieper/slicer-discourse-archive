---
topic_id: 27270
title: "Use Amd Rocm For Totalsegmentator"
date: 2023-01-16
url: https://discourse.slicer.org/t/27270
---

# Use AMD ROCm for TotalSegmentator

**Topic ID**: 27270
**Date**: 2023-01-16
**URL**: https://discourse.slicer.org/t/use-amd-rocm-for-totalsegmentator/27270

---

## Post #1 by @Alex_Vergara (2023-01-16 12:57 UTC)

<p>Is there a way to use AMD cards with ROCM? I am thinking of supported cards with the <a href="https://aur.archlinux.org/packages/python-pytorch-rocm" rel="noopener nofollow ugc">AUR (en) - python-pytorch-rocm (archlinux.org)</a> package or card specific wheels like <a href="https://github.com/xuhuisheng/rocm-gfx803" rel="noopener nofollow ugc">xuhuisheng/rocm-gfx803 (github.com)</a></p>

---

## Post #2 by @muratmaga (2023-01-16 17:21 UTC)

<p>Looks like auto-installation with the light the torch is only for the CUDA based GPUs. <a href="https://pypi.org/project/light-the-torch/" class="inline-onebox" rel="noopener nofollow ugc">light-the-torch · PyPI</a></p>
<p>Torch already supports those GPUs, so you should be able to manually install those.</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://pytorch.org/blog/pytorch-for-amd-rocm-platform-now-available-as-python-package/">
  <header class="source">
      <img src="https://pytorch.org/favicon.ico?" class="site-icon" width="32" height="32">

      <a href="https://pytorch.org/blog/pytorch-for-amd-rocm-platform-now-available-as-python-package/" target="_blank" rel="noopener nofollow ugc">pytorch.org</a>
  </header>

  <article class="onebox-body">
    <img src="https://pytorch.org/assets/images/pytorch-logo.png" class="thumbnail onebox-avatar" width="500" height="500">

<h3><a href="https://pytorch.org/blog/pytorch-for-amd-rocm-platform-now-available-as-python-package/" target="_blank" rel="noopener nofollow ugc">PyTorch</a></h3>

  <p>An open source machine learning framework that accelerates the path from research prototyping to production deployment.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2023-01-16 18:58 UTC)

<p>Light-the-torch supports CPU, CUDA, ROCm backends. Therefore, all ROCm versions that pytorch supports should work well in Slicer.</p>

---
