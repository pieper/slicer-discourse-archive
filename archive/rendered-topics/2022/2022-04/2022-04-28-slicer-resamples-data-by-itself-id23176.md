# slicer resamples data by itself

**Topic ID**: 23176
**Date**: 2022-04-28
**URL**: https://discourse.slicer.org/t/slicer-resamples-data-by-itself/23176

---

## Post #1 by @Berkay (2022-04-28 16:46 UTC)

<p>Dear all,</p>
<p>Data I’m trying to use is in “nii.gz” format and it includes axial data.</p>
<p>Normally it has 21 slices in total. After loading data using “data loading” module, program shows maybe 100 slices. When I check properties of data, as you can see from image, I see 21 slices and I want to segment images, so I just want to segment 21 slices instead of hundreds.</p>
<p>I couldn’t find a way to fix this.</p>
<p>Thanks in advnace for your help.</p>
<p>Berkay<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a7eee89a5799be964d3f4fd0f90c5a1fba733ca.png" data-download-href="/uploads/short-url/aD1hxwqlEaBvhesxMHgAx8NWBE6.png?dl=1" title="Screenshot from 2022-04-28 13-51-54" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a7eee89a5799be964d3f4fd0f90c5a1fba733ca_2_690x284.png" alt="Screenshot from 2022-04-28 13-51-54" data-base62-sha1="aD1hxwqlEaBvhesxMHgAx8NWBE6" width="690" height="284" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a7eee89a5799be964d3f4fd0f90c5a1fba733ca_2_690x284.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a7eee89a5799be964d3f4fd0f90c5a1fba733ca.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a7eee89a5799be964d3f4fd0f90c5a1fba733ca.png 2x" data-dominant-color="EDEDED"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-04-28 13-51-54</span><span class="informations">746×308 30.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @muratmaga (2022-04-28 19:47 UTC)

<p>Your image will have 21 slices only in Axial plane. Coronal and Sagittal views should have 384 slices.</p>
<p>Possibly you are not looking at the right plane?</p>

---

## Post #3 by @Berkay (2022-04-29 02:27 UTC)

<p>Thanks Murat. I’m looking at axial plane. It is easy to differentiate axial and other planes</p>

---

## Post #4 by @lassoan (2022-04-29 04:16 UTC)

<p>When you browse slices using the arrow keys (or page up/down keys) then the slice jumps as much as the slice spacing along that axis. So, if you wave 21 slices then you should be able to step through it in 21 steps. If you can share with us a screen recording video that demonstrates what you experienced; or you save the scene as a .mrb file and share with us (upload somewhere and post the link here) then it may give us an idea why the software did not behave as you expected.</p>
<aside class="quote no-group" data-username="Berkay" data-post="1" data-topic="23176">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/berkay/48/15119_2.png" class="avatar"> Berkay:</div>
<blockquote>
<p>program shows maybe 100 slices</p>
</blockquote>
</aside>
<p>This is interesting, because it should not be possible to see slice boundaries (by default image interpolation is enabled, so pixel edges should not be visible). How did you determine that about 100 slices are shown? Can you maybe attach a screenshot and show it there?</p>
<aside class="quote no-group" data-username="Berkay" data-post="1" data-topic="23176">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/berkay/48/15119_2.png" class="avatar"> Berkay:</div>
<blockquote>
<p>I just want to segment 21 slices instead of hundreds</p>
</blockquote>
</aside>
<p>Usually it does not matter much how many slices you have, as manual segmentation on each and every slice would be too time-consuming and unnecessary anyway.</p>
<p>Instead, you can draw a few scribbles in each segment on a few orthogonal slices and let <code>Grow from seeds</code> effect create a complete 3D segmentation from it. See a very simple example here:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="cybL5A0w3hw" data-video-title="Brain tumor segmentation on MRI in 1 minute" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=cybL5A0w3hw" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/cybL5A0w3hw/maxresdefault.jpg" title="Brain tumor segmentation on MRI in 1 minute" width="" height="">
  </a>
</div>

<p>If there is no significant contrast between neighbor regions but you can separate regions based on your anatomical knowledge, then you can use <code>Fill between slices</code> effect. You can segment on a small number of parallel slices, and the effect automatically computes segmentation on slices between them by smooth interpolation. This works very efficiently for elongated structures that do not change a lot between nearby slices (for example muscles or long bones, resliced along their long axis). See this short demo:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="u93kI1MG6Ic" data-video-title="Quick manual segmentation with contour interpolation" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=u93kI1MG6Ic" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/u93kI1MG6Ic/maxresdefault.jpg" title="Quick manual segmentation with contour interpolation" width="" height="">
  </a>
</div>


---

## Post #5 by @Josefa_Garcia (2022-06-17 13:45 UTC)

<p>Hi Andras, quick question, when you interpolate the images using <em>ResampleScalarVolume</em>, it should change the pixel size and the distance between slices? it works as resampling and interpolation? Thanks.</p>

---

## Post #6 by @lassoan (2022-06-17 14:22 UTC)

<p>Once an image is loaded into Slicer, we have a 3D volume consisting of voxels. When the image is resampled then all axes are treated the same way - I would not say we change pixel sizes and slice spacing but change voxel size. Resampling happens using the chosen interpolation kernel (linear, bspline, sinc, etc.).</p>

---
