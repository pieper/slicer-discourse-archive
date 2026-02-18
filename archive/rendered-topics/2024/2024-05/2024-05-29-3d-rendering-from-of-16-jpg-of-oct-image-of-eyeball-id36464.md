# 3D rendering from of 16 jpg of OCT image of eyeball

**Topic ID**: 36464
**Date**: 2024-05-29
**URL**: https://discourse.slicer.org/t/3d-rendering-from-of-16-jpg-of-oct-image-of-eyeball/36464

---

## Post #1 by @lisavier815 (2024-05-29 13:52 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31713a70c730a33eae7e9472c0f22ff53c954d26.jpeg" data-download-href="/uploads/short-url/73nZadMTWsEOrjTQE5jwzy7Mmqi.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31713a70c730a33eae7e9472c0f22ff53c954d26_2_510x500.jpeg" alt="1" data-base62-sha1="73nZadMTWsEOrjTQE5jwzy7Mmqi" width="510" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31713a70c730a33eae7e9472c0f22ff53c954d26_2_510x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31713a70c730a33eae7e9472c0f22ff53c954d26_2_765x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31713a70c730a33eae7e9472c0f22ff53c954d26_2_1020x1000.jpeg 2x" data-dominant-color="1C1C1C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">2008×1966 264 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8aa0e974e3f2b329e389906c58371b348eff2df.jpeg" data-download-href="/uploads/short-url/sD9Q383qIMM0GspqqlDy0rdEiyH.jpeg?dl=1" title="9" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8aa0e974e3f2b329e389906c58371b348eff2df_2_510x500.jpeg" alt="9" data-base62-sha1="sD9Q383qIMM0GspqqlDy0rdEiyH" width="510" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8aa0e974e3f2b329e389906c58371b348eff2df_2_510x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8aa0e974e3f2b329e389906c58371b348eff2df_2_765x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8aa0e974e3f2b329e389906c58371b348eff2df_2_1020x1000.jpeg 2x" data-dominant-color="1A1A1A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">9</span><span class="informations">2008×1966 252 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>the jpg like this</p>

---

## Post #2 by @lassoan (2024-05-29 14:32 UTC)

<p>Yes, sure, you can render even 16 slices in 3D. Are the slices parallel or rotated?</p>

---

## Post #3 by @lisavier815 (2024-05-29 15:33 UTC)

<p>Rotated,and I attempted to reconstruct based on the previous posts about OCT image reconstruction, but I’m not clear about the functionality of the extension modules. Should I use IGT or slicerhreat? If possible, could you provide a more detailed explanation? Thank you very much!</p>

---

## Post #4 by @lassoan (2024-05-29 16:21 UTC)

<p>16 slices for 180 degrees would be quite sparse (you have very high resolution slices with huge gaps between them), but depending on what you want to do, you might get a usable result.</p>
<p>SlicerHeart Reconstruct4DCineMRI module can serve as a good example of how to organize image a set of slices into a time sequence of 3D volumes, but since you only have a single timepoint, there is not a lot to use from there.</p>
<p>Instead, you can use <a href="https://discourse.slicer.org/t/segmentation-of-mitral-valve/14598/10">this code snippet</a> to put together a sequence of image slices, with each slice having a correct position and orientation and then reconstruct a volume from that.</p>
<p>Since your data is extremely sparse. you would end up with big gaps between them, which could make it difficult to interpret the 3D volume. You could fix that by adding interpolated slices (compute weighted average of neighbor slices and insert them between your original slices).</p>

---

## Post #5 by @lisavier815 (2024-05-31 03:39 UTC)

<p>I used the code snippet you provided, and when I reached the model reconstruction step, the CPU usage significantly increased, and then the slicer crashed. I tried multiple times, but even when it completed running, I couldn’t obtain the correct model. When importing JPG images, should I just import them from the folder to form a single model volume, or should I import them separately multiple times to get multiple model volumes?</p>

---

## Post #6 by @lassoan (2024-05-31 14:17 UTC)

<p>This sounds promising. The application crashed because it has ran out of memory. The volume reconstructor automatically allocates a memory buffer that is large enough to contain all the slices at the desired resolution, and if the the slices cover a large region and the spacing you have chosen for the reconstructed volume is small then this memory buffer will be larger than the amount of memory your computer has. The problem is either in how you set the image positions/orientations (you can verify this by browsing the generated image sequence using Sequence browser toolbar and show the slice positions by configuring Volume Reslice Driver module) or choose a larger output spacing (to begin with, use 10x or 100x larger output spacing then the spacing of your input image; if volume reconstruction is successful you can gradually decrease this value to see what is the smallest spacing your computer can handle).</p>

---

## Post #7 by @lassoan (2024-05-31 15:32 UTC)

<aside class="quote no-group" data-username="lisavier815" data-post="5" data-topic="36464">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lisavier815/48/76720_2.png" class="avatar"> lisavier815:</div>
<blockquote>
<p>I tried multiple times, but even when it completed running, I couldn’t obtain the correct model</p>
</blockquote>
</aside>
<p>The result of volume reconstruction is not a model (i.e., mesh), but an image (3D volume). You can see it in slice views or use Volume rendering module to show it in 3D.</p>
<aside class="quote no-group" data-username="lisavier815" data-post="5" data-topic="36464">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lisavier815/48/76720_2.png" class="avatar"> lisavier815:</div>
<blockquote>
<p>When importing JPG images, should I just import them from the folder to form a single model volume</p>
</blockquote>
</aside>
<p>The code snippet I linked is for getting slices from a single volume, so probably the easiest is to load the JPG stack as a single volume.</p>

---
