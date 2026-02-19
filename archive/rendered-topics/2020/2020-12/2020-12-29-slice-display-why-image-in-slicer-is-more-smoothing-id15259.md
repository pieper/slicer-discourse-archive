---
topic_id: 15259
title: "Slice Display Why Image In Slicer Is More Smoothing"
date: 2020-12-29
url: https://discourse.slicer.org/t/15259
---

# Slice display - why image in slicer is more smoothing

**Topic ID**: 15259
**Date**: 2020-12-29
**URL**: https://discourse.slicer.org/t/slice-display-why-image-in-slicer-is-more-smoothing/15259

---

## Post #1 by @czj1989 (2020-12-29 03:28 UTC)

<p>Hello! It is not a bug. I just wonder something about the slice display in Slicer. when I used vtk6.2 to display image with vtkImageReslice::SetInterpolationModeToLinear() and vtkImageActor:InterpolateOn(), I got Figure A which was not smoothing. But I load the same image in Slicer, then I got Figure B which was very smoothing. I tried to set output spacing of vtkImageReslice as 0.25 x original spacing, and then I got the result as slicer’s. However, I found it became slower when I paged down, and there was no this problem in slicer.</p>
<p>Can you tell me the additional operations has done by Slicer? Thank you very much!</p>
<p>Figure A<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e25f7335fedfc5a078fd59262c56b4d0a053a4f2.jpeg" alt="image" data-base62-sha1="wiApmyJdz0D34RTFb2ZUAvTjKOC" width="669" height="386"><br>
Figure B<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b75ef5d25e5870e0de4793b65be31c95a3ac0672.jpeg" data-download-href="/uploads/short-url/qaaPmDL9bNsfyb326Wst3UdAIbE.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b75ef5d25e5870e0de4793b65be31c95a3ac0672_2_690x340.jpeg" alt="image" data-base62-sha1="qaaPmDL9bNsfyb326Wst3UdAIbE" width="690" height="340" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b75ef5d25e5870e0de4793b65be31c95a3ac0672_2_690x340.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b75ef5d25e5870e0de4793b65be31c95a3ac0672.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b75ef5d25e5870e0de4793b65be31c95a3ac0672.jpeg 2x" data-dominant-color="808080"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">805×397 31.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-12-29 18:52 UTC)

<p>Answer from <a class="mention" href="/u/pieper">@pieper</a>:</p>
<blockquote>
<p>Maybe the difference is that Slicer uses vtkImageReslice to resample the images to screen space (pixels on your monitor) but when you use a vtkImageActor it uses the original image as a texture.</p>
</blockquote>

---

## Post #3 by @czj1989 (2020-12-31 09:12 UTC)

<p>Thank you for answering my question. Does Slicer use ImageActor to display image or use other actor?</p>

---

## Post #4 by @lassoan (2020-12-31 17:33 UTC)

<p>vtkImageActor is good for simple use cases but we need many more features in 3D Slicer. Therefore, we prepare all data using VTK filter pipelines and  render it by a simple actor and polydata mapper, displaying texture on a rectangle.</p>

---

## Post #5 by @czj1989 (2021-01-04 01:11 UTC)

<p>Thank you very much! This is very useful for me.  I wil try it.</p>

---
