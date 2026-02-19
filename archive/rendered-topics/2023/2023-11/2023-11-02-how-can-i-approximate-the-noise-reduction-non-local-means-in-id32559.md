---
topic_id: 32559
title: "How Can I Approximate The Noise Reduction Non Local Means In"
date: 2023-11-02
url: https://discourse.slicer.org/t/32559
---

# How can I approximate the Noise Reduction Non-Local Means in Amira?

**Topic ID**: 32559
**Date**: 2023-11-02
**URL**: https://discourse.slicer.org/t/how-can-i-approximate-the-noise-reduction-non-local-means-in-amira/32559

---

## Post #1 by @Tan (2023-11-02 14:22 UTC)

<p>I’ve tried in-build four denoising tools for my micro-ct data, but the results were not ideal. Sometimes the results are even mixed with noise outside the organization. This is my default setting in Amira. How should I approximate the same function? Thanks.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb668841c4531536ae7f65faf920593b1055248e.png" alt="default" data-base62-sha1="t1mBfDhvH5qScJtFdPxaujnQ7iC" width="644" height="290"></p>

---

## Post #2 by @lassoan (2023-11-02 14:39 UTC)

<p><code>Simple Filters</code> module provides many noise reduction filters. For example, there is a non-local means filter called <code>PatchBasedDenoisingImageFilter</code>. You can find its documentation <a href="https://itk.org/Doxygen/html/classitk_1_1PatchBasedDenoisingImageFilter.html">here</a>. There are a lot of things to scroll through, but you should be able to find description of  the method and exaplanation of all its parameters. If something is not clear about the algorithm or you would need advice on other image noise reduction filters then you can ask on the <a href="https://discourse.itk.org/">ITK forum</a>.</p>

---

## Post #3 by @Tan (2023-11-03 03:08 UTC)

<p>Thank you for your help! I’ll try it.</p>

---
