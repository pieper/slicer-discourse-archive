# Fast segmentation of roots.

**Topic ID**: 28330
**Date**: 2023-03-12
**URL**: https://discourse.slicer.org/t/fast-segmentation-of-roots/28330

---

## Post #1 by @Dr_M (2023-03-12 16:30 UTC)

<ol>
<li>Can you efficiently and effectively segment dental roots?</li>
<li>From a single arch from cbct to stl?</li>
<li>In the range of 20 micron to 100 micron level of exactitude?</li>
</ol>
<p>Thanks to those who have already posted about this subject. Thanks to Andras Lasso and many others.</p>
<p>However I still struggle to segment roots. I am unable to use some modules displayed in the tutorials I have seen. Maybe they are not available in Mac. I have also tried in windows based slicer unsuccessfully.</p>
<p>What I have been able to achieve is a mesh quite “dirty” that seems to require a lot of extra work sculping and cutting of.</p>
<p>All the info you can provide will be much appreciated.</p>

---

## Post #2 by @tsehrhardt (2023-03-13 17:35 UTC)

<p>Can you post a pic of what you’re getting? Have you tried any smoothing tools in the Segment Editor?</p>

---

## Post #3 by @Dr_M (2023-03-15 06:22 UTC)

<p>So If I go with “Threshold” over it already jumps to select cortical Bone.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a36e010c162e90842fe5d3d27e2f90cd4b6bee3.jpeg" data-download-href="/uploads/short-url/61rCEy2Mw0cYzXY4e3vFwAlxAt5.jpeg?dl=1" title="Screenshot 2023-03-14 at 07.43.27" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a36e010c162e90842fe5d3d27e2f90cd4b6bee3_2_690x410.jpeg" alt="Screenshot 2023-03-14 at 07.43.27" data-base62-sha1="61rCEy2Mw0cYzXY4e3vFwAlxAt5" width="690" height="410" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a36e010c162e90842fe5d3d27e2f90cd4b6bee3_2_690x410.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a36e010c162e90842fe5d3d27e2f90cd4b6bee3_2_1035x615.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a36e010c162e90842fe5d3d27e2f90cd4b6bee3_2_1380x820.jpeg 2x" data-dominant-color="78787F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-03-14 at 07.43.27</span><span class="informations">1920×1142 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0e580444fbf98338d997a5cfc8c7b42f706b63c.png" data-download-href="/uploads/short-url/peTJMQHeKDDb69wORTX3ITcasfq.png?dl=1" title="Screenshot 2023-03-14 at 07.45.42" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0e580444fbf98338d997a5cfc8c7b42f706b63c_2_690x479.png" alt="Screenshot 2023-03-14 at 07.45.42" data-base62-sha1="peTJMQHeKDDb69wORTX3ITcasfq" width="690" height="479" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0e580444fbf98338d997a5cfc8c7b42f706b63c_2_690x479.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0e580444fbf98338d997a5cfc8c7b42f706b63c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0e580444fbf98338d997a5cfc8c7b42f706b63c.png 2x" data-dominant-color="ECEDED"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-03-14 at 07.45.42</span><span class="informations">1004×698 45.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @tsehrhardt (2023-06-07 11:56 UTC)

<p>You can try Grow with Seeds and paint 2 segments–bone and teeth. I have used it for separating teeth from bone in CBCTs. It might still require some cleanup but might give you better separation than thresholding.</p>

---
