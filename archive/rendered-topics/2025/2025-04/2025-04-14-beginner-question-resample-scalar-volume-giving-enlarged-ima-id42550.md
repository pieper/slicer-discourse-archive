---
topic_id: 42550
title: "Beginner Question Resample Scalar Volume Giving Enlarged Ima"
date: 2025-04-14
url: https://discourse.slicer.org/t/42550
---

# Beginner question: Resample scalar volume giving enlarged image size

**Topic ID**: 42550
**Date**: 2025-04-14
**URL**: https://discourse.slicer.org/t/beginner-question-resample-scalar-volume-giving-enlarged-image-size/42550

---

## Post #1 by @Chamini (2025-04-14 05:21 UTC)

<p>Hi all, I used the ‘Resample Scalar Volume’ module to change the resolution of my dataset. However, the output volume has much higher dimensions than the original. How can I maintain the same image dimensions while only changing the voxel resolution? Thanks in advance!</p>

---

## Post #2 by @muratmaga (2025-04-14 06:07 UTC)

<p>You can’t. Image spacing and the dimensions of your original data defines a “volume in a physical world”. So unless you change that physical volume, you cannot change one without changing the other.</p>
<p>If your original image dimensions are 512x512x512 and resolution is 1.0x1.0x1.0mm, your volume represents a 51.2x51.2x51.2 cm cube. So if you decide to increase the spacing to 0.5x0.5x0.5, the dimensions of your volume needs to go up to 1024x1024x1024 to match the same physical volume. If you want your image dimensions to be 256x256x256, the spacing needs to be 2.0x2.0x2.0mm to map to the same physical volume.</p>
<p>You can of course arbitrarily change the spacing value to whatever you like, but then you also change the physical size of what your volume represents.</p>
<p>What are you trying to accomplish?</p>

---

## Post #3 by @Chamini (2025-04-14 22:47 UTC)

<p>Thanks for your reply. To clarify, I’m trying to normalize the resolution of my datasets. Since I’m calculating volume porosity from scans originally taken at different resolutions, I need to standardize them for accurate comparison. Does 3D Slicer offer any alternative methods for this specific task? TIA</p>

---

## Post #4 by @muratmaga (2025-04-14 22:54 UTC)

<aside class="quote no-group" data-username="Chamini" data-post="3" data-topic="42550">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/ecb155/48.png" class="avatar"> Chamini:</div>
<blockquote>
<p>volume porosity from scans originally taken at different resolutions,</p>
</blockquote>
</aside>
<p>If your scans have the correct spacing information, you do not have to do that. You will be measuring the porosity volume in the physical world dimensions. So no need to try to normalize for that.  (provided that your scans are high enough resolution to capture the porosity in the first place).</p>

---

## Post #5 by @Chamini (2025-04-14 23:04 UTC)

<p>My specific worry is that smaller pores might be detected in the higher resolution scans but missed entirely in the lower resolution ones. For a fair comparison between samples, I believe I need consistent resolution (taking the lowest resolution as the common for all) to ensure that pores of the same physical size are either detected or missed consistently across all samples.</p>

---

## Post #6 by @muratmaga (2025-04-15 00:12 UTC)

<aside class="quote no-group" data-username="Chamini" data-post="5" data-topic="42550">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/ecb155/48.png" class="avatar"> Chamini:</div>
<blockquote>
<p>believe I need consistent resolution (taking the lowest resolution as the common for all) to ensure that pores of the same physical size are either detected or missed consistently across all samples.</p>
</blockquote>
</aside>
<p>I think you should have done that during your imaging session, as opposed to after the fact.</p>
<p>Your lowest resolution should still be the lowest resolution to be able to detect pores. What if you end up degrading your data so that you can’t detect any difference? Are you sure your scan resolution has no confounding factor that will bias your results (e.g., big samples low resolution, small samples high resolution).</p>
<p>Anyways, these are things you need to decide for yourself.</p>
<p>If you want to resample data to a fixed resolution, you can easily do this by crop volume. E.g., if  you want all your samples to have 50 micron and one scan is 30 micron, you will enter the scaling value of 50/30=1.6667 to the crop volume. Output volume will have 50 micron resolution.</p>

---
