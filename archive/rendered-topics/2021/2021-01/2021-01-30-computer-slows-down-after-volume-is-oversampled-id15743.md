---
topic_id: 15743
title: "Computer Slows Down After Volume Is Oversampled"
date: 2021-01-30
url: https://discourse.slicer.org/t/15743
---

# Computer slows down after volume is oversampled

**Topic ID**: 15743
**Date**: 2021-01-30
**URL**: https://discourse.slicer.org/t/computer-slows-down-after-volume-is-oversampled/15743

---

## Post #1 by @Jason_Wong (2021-01-30 06:38 UTC)

<p>I think I’ve managed to oversample the volume. Although, it seems that whenever I try to do so, the panels turn blank on a relatively strong computer but lags my computer intensely when I use a weaker computer. Is it possible to create the segmentation mask then oversample the volume? Thanks.</p>

---

## Post #2 by @lassoan (2021-01-30 12:39 UTC)

<p>It is recommended to also always crop the volume to the minimum necessary size when you oversample, to keep the memory usage reasonable - using Crop volume.</p>
<p>You can also conserve memory by casting the volume to use the smallest necessary scalar type - using Cast scalar volume. For example, if you store your voxels as double-precision float then it takes 8 bytes, while if you use a short int then it just uses 2 bytes.</p>
<aside class="quote no-group" data-username="Jason_Wong" data-post="1" data-topic="15743">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jason_wong/48/9637_2.png" class="avatar"> Jason_Wong:</div>
<blockquote>
<p>Is it possible to create the segmentation mask then oversample the volume?</p>
</blockquote>
</aside>
<p>Segmentation will internally create a resampled copy of the master volume if you use any operation that relies on image intensity, so you will not save much memory this way.</p>

---

## Post #3 by @Jason_Wong (2021-01-31 20:14 UTC)

<p>Somehow I’m still getting blank panels after I’ve cropped the volume significantly.</p>
<p>I’ve tried this on several different computers and I’m getting the same results.</p>
<p>Cropped ROI<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a066fec47b337b09cb34b9c8e06be177e7507c9e.png" data-download-href="/uploads/short-url/mSZ3OaGAD3J0TXIKMhYV8ggaCo6.png?dl=1" title="capture 1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a066fec47b337b09cb34b9c8e06be177e7507c9e_2_689x346.png" alt="capture 1" data-base62-sha1="mSZ3OaGAD3J0TXIKMhYV8ggaCo6" width="689" height="346" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a066fec47b337b09cb34b9c8e06be177e7507c9e_2_689x346.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a066fec47b337b09cb34b9c8e06be177e7507c9e_2_1033x519.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a066fec47b337b09cb34b9c8e06be177e7507c9e.png 2x" data-dominant-color="343441"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">capture 1</span><span class="informations">1346×675 61.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Volume after oversampling by a ratio of 2</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e925ef6af25bb274512a9f4e2a6358e1d909548.png" data-download-href="/uploads/short-url/klfoKdM1s5phtBzyuuZcT4gkMwE.png?dl=1" title="capture 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e925ef6af25bb274512a9f4e2a6358e1d909548_2_690x443.png" alt="capture 2" data-base62-sha1="klfoKdM1s5phtBzyuuZcT4gkMwE" width="690" height="443" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e925ef6af25bb274512a9f4e2a6358e1d909548_2_690x443.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e925ef6af25bb274512a9f4e2a6358e1d909548_2_1035x664.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e925ef6af25bb274512a9f4e2a6358e1d909548.png 2x" data-dominant-color="2E2E3A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">capture 2</span><span class="informations">1197×769 16.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2021-01-31 20:17 UTC)

<p>Which Slicer version do you use?<br>
Is the volume under a transform? (if you are not sure, attach a screenshot of Data module)<br>
What are the dimensions and scalar type of the original volume? (if you are not sure, attach a screenshot of Volumes module, with Volume information section open)</p>

---

## Post #5 by @Jason_Wong (2021-02-01 00:13 UTC)

<p>I’m using 4.11.20200930 and I’m getting similar results from the unstable version 4.13</p>
<p>Window from Data module</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/831b993c767faef0da9b625fdcd343d9f5c8c4e6.png" data-download-href="/uploads/short-url/iHPG3qzvzW5fYSOzlum4wZVsCdo.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/831b993c767faef0da9b625fdcd343d9f5c8c4e6_2_523x500.png" alt="image" data-base62-sha1="iHPG3qzvzW5fYSOzlum4wZVsCdo" width="523" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/831b993c767faef0da9b625fdcd343d9f5c8c4e6_2_523x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/831b993c767faef0da9b625fdcd343d9f5c8c4e6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/831b993c767faef0da9b625fdcd343d9f5c8c4e6.png 2x" data-dominant-color="F4F7F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">620×592 22.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Window from Volume modules</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8c42664bb0cfd4c072fa1490291a37e467e0a0d.png" data-download-href="/uploads/short-url/xd91oAGcF1YXoHNi5Vg2hsRciJL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8c42664bb0cfd4c072fa1490291a37e467e0a0d.png" alt="image" data-base62-sha1="xd91oAGcF1YXoHNi5Vg2hsRciJL" width="581" height="500" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">626×538 10.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>the actual volume is proportionally smaller by scale of 100.<br>
Do I need to convert the volume to label map?</p>

---

## Post #6 by @muratmaga (2021-02-01 01:53 UTC)

<p>Assuming dimensions reported above are before cropping/oversampling, your volume is about 256MB in size. If you are cropping with option 0.5, the volume of your data is going to increase 8 folds to 2GB. And if you checked the ‘isotropic option’, then then the data volume will increase almost 100 folds (to about 25GB) which may cause slowdown on your computer with lower memory since the Slicer would need to use virtual memory.</p>

---

## Post #7 by @lassoan (2021-02-01 02:09 UTC)

<p>The volume is not transformed (good), not very big (good). However, the volume is very sparse (voxel size is 1x1x20, which is a shape like a needle, instead of an ideal cube shape) and the scalar range is quite unusual, too (normally we have a range of a few thousands). Despite these unusual properties, the volume should be still usable, but some default processing parameters may need to be adjusted. For example, as <a class="mention" href="/u/muratmaga">@muratmaga</a> indicated above, if you are not careful then you can end up with an enormous volume.</p>
<p>Can you show this Volume Information section for the <strong>cropped volume</strong>?</p>
<p>It would be also useful to see the image histogram (bottom section in Volumes module) for both the original and cropped volume.</p>

---

## Post #8 by @Jason_Wong (2021-02-01 02:39 UTC)

<p>Here is the image histogram:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a09fa889316b6c91c8b39679586e0a4413902d08.png" alt="image" data-base62-sha1="mUWsCKQhMwZKMPLulJ1dzFdyCzm" width="678" height="192"></p>
<p>The cropped volume size:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/884436285d85483befaa014dd495c8df807849bb.png" data-download-href="/uploads/short-url/jrt4RZ79aAV6kA17SJwxjTp2xKP.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/884436285d85483befaa014dd495c8df807849bb.png" alt="image" data-base62-sha1="jrt4RZ79aAV6kA17SJwxjTp2xKP" width="690" height="266" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">724×280 6.18 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks all of you. Really appreciate the help.</p>

---

## Post #9 by @Jason_Wong (2021-02-02 04:56 UTC)

<p>Here’s an update of what I’ve tried.<br>
The switching to older versions of 3D Slicer doesn’t seem to cut it. Still getting the same results.</p>
<p>I’ve also tried using the sample data: <a href="https://www.slicer.org/wiki/SampleData" class="inline-onebox" rel="noopener nofollow ugc">SampleData - Slicer Wiki</a></p>
<p>I’ve tested the oversampling on MR-head, CT-chest, and DTI-Brain and I’m still getting the same.</p>
<p>I think I might be skipping some preliminary steps before I can oversample. I’m also noticing that I am not able to oversample the volume if the volume has been selected on drop down of “Master Volume”.<br>
So this is what my window looks like just before I start oversampling.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd14522ecd28c5374c735a9fc0e2bd7df39c8a10.png" data-download-href="/uploads/short-url/qYFMkrVr7qDnrQYzNY7Zuh8nj8I.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd14522ecd28c5374c735a9fc0e2bd7df39c8a10_2_690x309.png" alt="image" data-base62-sha1="qYFMkrVr7qDnrQYzNY7Zuh8nj8I" width="690" height="309" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd14522ecd28c5374c735a9fc0e2bd7df39c8a10_2_690x309.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd14522ecd28c5374c735a9fc0e2bd7df39c8a10.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd14522ecd28c5374c735a9fc0e2bd7df39c8a10.png 2x" data-dominant-color="E7E8E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">982×441 37.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @lassoan (2021-02-02 05:05 UTC)

<aside class="quote no-group" data-username="Jason_Wong" data-post="9" data-topic="15743">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jason_wong/48/9637_2.png" class="avatar"> Jason_Wong:</div>
<blockquote>
<p>I’ve tested the oversampling on MR-head, CT-chest, and DTI-Brain and I’m still getting the same.</p>
</blockquote>
</aside>
<p>Do you mean that oversampling slows down Slicer? That is expected. Oversampling factor of 2.0 increases memory usage and amount of computation by 8x, but if it makes you run out of physical RAM and your computer starts swapping, it won’t be just 8x slower but hundreds times slower.</p>
<p>If you cannot switch to a strong desktop computer with lots of RAM then I would recommend to always crop the volume when you resample, so that you keep the number of voxels about a few hundred along each axis.</p>
<p>How much RAM and what CPU do you have?</p>

---

## Post #11 by @Jason_Wong (2021-02-02 05:11 UTC)

<p>For larger volumes, it does lag slicer, but when the lag is no longer apparent, I end up with 3 blank panels like this (my computer doesn’t seem to slow down afterwards):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bde2e99a10d2ca63a2506076735b1d7d6835f038.png" data-download-href="/uploads/short-url/r5OoMwhmgozf5eIhliVQHFVoxSM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bde2e99a10d2ca63a2506076735b1d7d6835f038_2_690x393.png" alt="image" data-base62-sha1="r5OoMwhmgozf5eIhliVQHFVoxSM" width="690" height="393" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bde2e99a10d2ca63a2506076735b1d7d6835f038_2_690x393.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bde2e99a10d2ca63a2506076735b1d7d6835f038_2_1035x589.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bde2e99a10d2ca63a2506076735b1d7d6835f038.png 2x" data-dominant-color="2D2D39"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1373×783 14.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
(so to clarify, this is post-oversampling)</p>
<p>Currently have a PC with 16 gb of RAM.</p>
<p>I’ve also tried to crop it down significantly and it gives me the exact same results just without the lag following the execution.</p>

---

## Post #12 by @lassoan (2021-02-02 05:12 UTC)

<p>What CPU and graphics do you have?</p>

---

## Post #13 by @Jason_Wong (2021-02-02 05:15 UTC)

<p>Intel Xeon 6148 with 2.40 GHz and NVIDIA GRID M10-2Q</p>

---

## Post #14 by @lassoan (2021-02-02 05:23 UTC)

<p>OK, this CPU, graphics, and RAM should be sufficient to handle something like CTChest oversampled 2x along each axis.</p>
<p>The blank image is just a misunderstanding. That is generated for your convenience when you specify geometry without selecting a master volume (for the case when you don’t have any input volume but you want to create a segmentation by just free painting). If you have a volume to segment then select it as a master volume.</p>

---

## Post #15 by @Jason_Wong (2021-02-02 05:31 UTC)

<p>Oh. Haven’t thought of that. Lemme try that out.</p>

---

## Post #16 by @Jason_Wong (2021-02-02 07:06 UTC)

<p>Hmmm… when I try to oversample the master volume, nothing happens (the spacing between each image is not reduced).</p>

---

## Post #17 by @muratmaga (2021-02-02 07:32 UTC)

<p>Can try these steps in a blank scene:</p>
<ol>
<li>Load MRHead sample data.</li>
<li>Go to segment Editor and click on segment geometry button, and from the Source Geometry drop down choose ‘MRHead’. Set the oversampling to 2. Do you see something like this?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce026338b207fd5ec08164a0063e1c5565d0a4f4.png" alt="image" data-base62-sha1="tortp9WNdSWqaKhTPLqkn0sKWwY" width="432" height="300"></li>
<li>Hit OK.</li>
<li>Create a blank segment, and then threshold effect with 69.75-258.00 range and hit apply.</li>
<li>Go to Segmentation Geometry again, and this time choose the segmentation as your source geometry. Confirm that you are seeing:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e1524f2773c474f2433102a77530930544cec94.png" alt="image" data-base62-sha1="b8KxJUxf7ltJoqtYsfJCtEw0416" width="432" height="300"></li>
</ol>
<p>This oversampling of 2 for MRhead should not cause any noticeable delay or lag on your computer at all. If these work out, try with your data.</p>

---

## Post #18 by @Jason_Wong (2021-02-03 04:07 UTC)

<p>The strange part is I’m not able to threshold.</p>
<p>This is what I get:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da9500ac7e62f4cb9e4703a7ada3e2d418e9a23f.png" data-download-href="/uploads/short-url/vbFkaaa7GJJBoM3gRa5NJKmEN1t.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da9500ac7e62f4cb9e4703a7ada3e2d418e9a23f_2_690x394.png" alt="image" data-base62-sha1="vbFkaaa7GJJBoM3gRa5NJKmEN1t" width="690" height="394" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da9500ac7e62f4cb9e4703a7ada3e2d418e9a23f_2_690x394.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da9500ac7e62f4cb9e4703a7ada3e2d418e9a23f_2_1035x591.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da9500ac7e62f4cb9e4703a7ada3e2d418e9a23f.png 2x" data-dominant-color="919195"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1066×609 37 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Notice the threshold range is 0.</p>
<p>Also, to clarify, nothing changes when selecting the master volume as “MRHead”  prior to oversampling.</p>

---

## Post #19 by @muratmaga (2021-02-03 04:25 UTC)

<p>You are doing something wrong. Your master volume should have been MRHead in this step.</p>
<p>First read the documentation about the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html" rel="noopener nofollow ugc">segment editor</a></p>
<p>and then complete <a href="https://github.com/SlicerMorph/S_2020/blob/master/Day_2/Segmentation/Segmentation_tutorial.md" rel="noopener nofollow ugc">this tutorial</a></p>

---

## Post #20 by @Jason_Wong (2021-02-04 05:05 UTC)

<p>Thanks! It’s working now. Oversampling the segmentation works after applying threshold and then creating another threshold segmentation.</p>
<p>Also, are there any peer-reviewed journals or articles where the oversampling algorithm was first introduce?</p>

---

## Post #21 by @lassoan (2021-02-05 04:15 UTC)

<aside class="quote no-group" data-username="Jason_Wong" data-post="20" data-topic="15743">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jason_wong/48/9637_2.png" class="avatar"> Jason_Wong:</div>
<blockquote>
<p>Also, are there any peer-reviewed journals or articles where the oversampling algorithm was first introduce?</p>
</blockquote>
</aside>
<p>Oversampling is fairly straightforward (simple image resampling). It is probably mentioned in this segmentation infrastructure paper:</p>
<p>Pinter, C., Lasso, A., &amp; Fichtinger, G. (2019). Polymorph segmentation representation for medical image computing. Computer Methods and Programs in Biomedicine, 171, 19–26. <a href="https://doi.org/10.1016/j.cmpb.2019.02.011" class="inline-onebox">Redirecting</a></p>

---
