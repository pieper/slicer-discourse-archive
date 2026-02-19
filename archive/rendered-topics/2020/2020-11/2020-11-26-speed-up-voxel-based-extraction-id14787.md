---
topic_id: 14787
title: "Speed Up Voxel Based Extraction"
date: 2020-11-26
url: https://discourse.slicer.org/t/14787
---

# Speed up Voxel based extraction

**Topic ID**: 14787
**Date**: 2020-11-26
**URL**: https://discourse.slicer.org/t/speed-up-voxel-based-extraction/14787

---

## Post #1 by @Alessio_Romita (2020-11-26 22:15 UTC)

<p>Hey guys I was wondering if there is any way to speed up the voxel based extraction ? I’m trying to parallelise the extraction for multiple images and It works.But, the speed is too slow and of course if I parallelise too much images I run out of memory  .<br>
Thanks for any suggestion.</p>

---

## Post #2 by @JoostJM (2020-11-27 07:09 UTC)

<p>If you extract feature maps using masks that span the entire image, consider using masks only detailing the ROI, this will significantly reduce time. On the area of parallelisation, PyRadiomics has built-in paralellisation (using the <code>--jobs</code> argument), but besides that there really isn’t anything easy I can think of.</p>
<p>Significant efforts have already been made to increase performance as much as possible for now, including paralellisation of cases and C extensions for the largest bottlenecks, but also batch-calculation of multiple voxels (making optimum use of numpy’s optimization, and reducing number of iterations made in python loops).</p>
<p>Keep in mind that calculating voxel-based radiomics simply is a very computational expensive operation, essentially the same as calculating segment-based radiomics, but once <em>for every voxel in the ROI</em>.</p>
<p>In the future, enhancements may be possible if we manage to make use of GPU accelerated calculations, but this is quite complex and not available at the moment.</p>

---

## Post #3 by @ivanzhovannik (2021-04-07 13:58 UTC)

<p>Hi <a class="mention" href="/u/joostjm">@JoostJM</a> and <a class="mention" href="/u/alessio_romita">@Alessio_Romita</a>,</p>
<p>Is there a stride analog of a deep learning convolution stride to skip some voxels? I think this would have been of some use to us not to calculate radiomics with a step of size 1.</p>
<p>Could you also point the source code of the voxel-wise extraction please?</p>
<p>Thanks in advance!</p>
<hr>
<p>Ivan</p>

---

## Post #4 by @JoostJM (2021-04-12 07:44 UTC)

<p>Hello <a class="mention" href="/u/ivanzhovannik">@ivanzhovannik</a>,</p>
<p>There is no stride analog in PyRadiomics’ voxel based calculation. If you want to skip certain voxels, exclude them from the mask. If you then set <code>maskedKernel=False</code>, all voxels within the kernel will be included for feature calculation, regardless of whether they belong to the input mask or not.</p>

---

## Post #5 by @Hruthik0x (2025-04-07 09:41 UTC)

<p>Hi <a class="mention" href="/u/joostjm">@JoostJM</a>,</p>
<p>Does the latest version of PyRadiomics support GPU acceleration for feature extraction? If not, I’d be interested in contributing to add this functionality.</p>
<p>I came across a couple of related projects that could serve as inspiration:</p>
<ul>
<li><a href="https://github.com/jiaoyining/cuRadiomics" class="inline-onebox" rel="noopener nofollow ugc">GitHub - jiaoyining/cuRadiomics: Extracting Radiomic Features using CUDA for GPU-acceleration</a></li>
<li><a href="https://github.com/lyhyl/pytorchradiomics" class="inline-onebox" rel="noopener nofollow ugc">GitHub - lyhyl/pytorchradiomics: PyTorch implementation of PyRadiomics Extractor</a></li>
</ul>
<p>I’d love to hear your thoughts on this. If you think it’s a worthwhile direction, I can start working on a prototype and potentially open a pull request.</p>

---
