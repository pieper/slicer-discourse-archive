---
topic_id: 36269
title: "How To Solve Pytorch Version Error In Totalsegmentator Using"
date: 2024-05-20
url: https://discourse.slicer.org/t/36269
---

# How to solve Pytorch version error in TotalSegmentator using CPU?

**Topic ID**: 36269
**Date**: 2024-05-20
**URL**: https://discourse.slicer.org/t/how-to-solve-pytorch-version-error-in-totalsegmentator-using-cpu/36269

---

## Post #1 by @Saulo (2024-05-20 03:17 UTC)

<p>I installed Slicer 5.6.2 on my MACBOOK 13-inch, 2019.<br>
I installed TOTAL SEGMENTATION and MONAIauto3DSeg to try to do reconstructions, but when starting with totalsegmentation the following message appears “Application is required to complete installation of required Python packages.<br>
Press OK to restart.” and when I try to use MONAIAuto3DSeg the following message appears "Failed to install required dependencies.<br>
PyTorch version 1.8.1 is not compatible with this module. Minimum required version is 1.12. You can use ‘PyTorch Util’ module to install PyTorch with version requirement set to: &gt;=1.12</p>
<p>I tried installing a more current PyTorch, but even after restarting and reinstalling all applications, it always loads version 1.8.1 and the error remains. Can anyone help?</p>

---

## Post #2 by @lassoan (2024-05-20 03:21 UTC)

<p>What is your TotalSegmentator extension version (it is displayed in the Extensions Manager).</p>
<p>Have you tried to follow the instruction you got and use <code>PyTorch Utils</code> module with version requirement set to <code>&gt;=1.12</code> ?</p>

---

## Post #3 by @Saulo (2024-05-21 00:52 UTC)

<p>Version 9f434a5 (2024-04-25)</p>
<p>Unfortunately I don’t know how to evaluate the requirements with version requirement set to &gt;=1.12 ?</p>

---

## Post #4 by @lassoan (2024-05-21 03:15 UTC)

<p>Please go to “Pytorch utils” module, type <code>&gt;=1.12</code> into the textbox, and click Install.</p>

---

## Post #5 by @jamesobutler (2024-05-21 03:24 UTC)

<p>This seems to be a recurring problem at least on macOS</p>
<aside class="quote quote-modified" data-post="3" data-topic="34995">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-solve-pytorch-version-error-in-totalsegmentator-using-cpu/34995/3">How to solve Pytorch version error in TotalSegmentator using CPU</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Himm this is interesting. I just tried on my Mac, and while it started downloading v 2.2.1, it ended up installing 1.8. Not sure why. <a class="mention" href="/u/lassoan">@lassoan</a> 
Install PyTorch using light-the-torch with arguments: ['install', 'torch', 'torchvision', '--pytorch-computation-backend=cpu']
Collecting torch
  Downloading https://download.pytorch.org/whl/cpu/torch-2.2.1-cp39-none-macosx_10_9_x86_64.whl (151.0 MB)

Collecting torchvision
  Using cached https://download.pytorch.org/whl/torchvision-0.9.1-cp39-cp39-macos…
  </blockquote>
</aside>


---

## Post #6 by @So-lets-code (2025-02-12 13:26 UTC)

<p>After you uninstall PyTorch, you need to restart Slicer, and then install the v2.2.1 in module ‘PyTorch utils’. This solved the issue for me (also using macOS).</p>

---
