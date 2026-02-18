# 3 leaked semaphore objects to clean up at shutdown_MONAILabel

**Topic ID**: 29069
**Date**: 2023-04-23
**URL**: https://discourse.slicer.org/t/3-leaked-semaphore-objects-to-clean-up-at-shutdown-monailabel/29069

---

## Post #1 by @Spiros_Karkavitsas (2023-04-23 14:48 UTC)

<p>Operating system:Windows 10 Pro<br>
Slicer version: 5.12</p>
<p>Hello everyone,</p>
<p>I am using MONAI to train an algorithm. However, as I submit the labels and press the train button this message appeared today a couple of times on the log file (see attached).</p>
<p>The main message is ‘‘There appear 3 leaked semaphore objects to cleanup at shutdown’’</p>
<p>What is the cause of this error and did anyone encounter in the past such an issue?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a90876df79f15a818e02094ded0d5cfa0244f467.jpeg" data-download-href="/uploads/short-url/o7kPi5ACIS9kcnFtZxOjlTBpjnx.jpeg?dl=1" title="Screenshot_11" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a90876df79f15a818e02094ded0d5cfa0244f467_2_690x337.jpeg" alt="Screenshot_11" data-base62-sha1="o7kPi5ACIS9kcnFtZxOjlTBpjnx" width="690" height="337" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a90876df79f15a818e02094ded0d5cfa0244f467_2_690x337.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a90876df79f15a818e02094ded0d5cfa0244f467_2_1035x505.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a90876df79f15a818e02094ded0d5cfa0244f467_2_1380x674.jpeg 2x" data-dominant-color="0E0E0E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_11</span><span class="informations">1660×813 320 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thank you in advance for your replay</p>

---

## Post #2 by @Spiros_Karkavitsas (2023-06-21 19:04 UTC)

<p>Apparently, the solution to this was trivial.</p>
<p>I noticed if you submit to MONAI server, by accident non-labeled 3D volumes then this error occur.</p>

---
