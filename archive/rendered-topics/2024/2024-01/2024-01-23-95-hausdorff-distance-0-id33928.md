# 95% Hausdorff distance 0

**Topic ID**: 33928
**Date**: 2024-01-23
**URL**: https://discourse.slicer.org/t/95-hausdorff-distance-0/33928

---

## Post #1 by @Young_Wang (2024-01-23 15:13 UTC)

<p>Hi there,</p>
<p>I’m working on an imaging fusion project that combines a small-FOV image with finer details and a large-FOV image with better description of surrounding anatomical structures.</p>
<p>To evaluate the performance ( reproducibility), I did the following:</p>
<ol>
<li>Add two scalar volumes after a rigid transform of one volume while keeping one fixed to get a fused image(volume)</li>
<li>Intensity based segmentation A of the fused image(volume)</li>
<li>Repeat step 1-2 to get the second segmentation B.</li>
<li>Calculate the image metric with Hausdorff and DICE.</li>
</ol>
<p>Here is the question. I noticed that both mean and maximum of Hausdorff distance values are reasonable but 95% is 0.  I wonder if it’s something I am doing is not correct or that’s what I should expect? I came across a previous post mentioning the 95% could be 0.</p>
<p>Thank you for your time and help in advance.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b217fea8de8bbdda6b999becf3d1727c52b13a8.png" data-download-href="/uploads/short-url/hzgv65iIDDRjy5z7JG2K6SOICU0.png?dl=1" title="1000016459" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b217fea8de8bbdda6b999becf3d1727c52b13a8_2_225x500.png" alt="1000016459" data-base62-sha1="hzgv65iIDDRjy5z7JG2K6SOICU0" width="225" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b217fea8de8bbdda6b999becf3d1727c52b13a8_2_225x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b217fea8de8bbdda6b999becf3d1727c52b13a8_2_337x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b217fea8de8bbdda6b999becf3d1727c52b13a8_2_450x1000.png 2x" data-dominant-color="363535"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1000016459</span><span class="informations">1080×2400 398 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5bc76ba8f4d9e64211a7dc490d191dea73061c5.jpeg" data-download-href="/uploads/short-url/nEayZCXJisbMTYu7cuK39UhfDZb.jpeg?dl=1" title="1000016458" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5bc76ba8f4d9e64211a7dc490d191dea73061c5_2_364x500.jpeg" alt="1000016458" data-base62-sha1="nEayZCXJisbMTYu7cuK39UhfDZb" width="364" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5bc76ba8f4d9e64211a7dc490d191dea73061c5_2_364x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5bc76ba8f4d9e64211a7dc490d191dea73061c5_2_546x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5bc76ba8f4d9e64211a7dc490d191dea73061c5_2_728x1000.jpeg 2x" data-dominant-color="3D3D3D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1000016458</span><span class="informations">1130×1550 176 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-01-23 23:05 UTC)

<p>If HD 95% is 0 then it means that 95% or more surface points have 0.0mm (or less than one voxel) error. This is possible if you use synthetic data and the alignment is nearly perfect.</p>

---

## Post #3 by @Young_Wang (2024-01-25 11:00 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thank you for the reply!</p>

---
