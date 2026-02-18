# Segment edit creat surface does work for inner ear segmentation

**Topic ID**: 830
**Date**: 2017-08-05
**URL**: https://discourse.slicer.org/t/segment-edit-creat-surface-does-work-for-inner-ear-segmentation/830

---

## Post #1 by @yakeworld (2017-08-05 10:13 UTC)

<p>When we use the Editor module to segment inner ear from CT data,it works well.But when using the segment edit module,the 3D view by creat surface is quite different from the stl module create by Editor module.<br>
I find that：<br>
1.segment edit creat surface 3D view is smoother，but lost details<br>
2.Paint with size &lt;%1 diameter will not work<br>
3. Does some parameter that can adjust exist?</p>

---

## Post #2 by @yakeworld (2017-08-05 10:20 UTC)

<p>In segmentations module,i export modules,and it is just as segment edit creat surface 3D view .Than i export Labelmap,and make moduleeffect in Edit module,the 3D view is quite different.</p>

---

## Post #3 by @lassoan (2017-08-05 12:44 UTC)

<aside class="quote no-group" data-username="yakeworld" data-post="1" data-topic="830">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/b4bc9f/48.png" class="avatar"> yakeworld:</div>
<blockquote>
<p>1.segment edit creat surface 3D view is smoother，but lost details</p>
</blockquote>
</aside>
<p>While you can tune surface generation parameters (by clicking <code>Update</code> button for <code>Closed surface</code> representation in Segmentations module), losing details is most likely due to large voxel size: if your voxels are large then you either have staircase artifacts or smooth surface. I would suggest to reduce voxel size of the original master volume using <code>Crop volume</code> module.</p>
<aside class="quote no-group" data-username="yakeworld" data-post="1" data-topic="830">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/b4bc9f/48.png" class="avatar"> yakeworld:</div>
<blockquote>
<p>2.Paint with size &lt;%1 diameter will not work</p>
</blockquote>
</aside>
<p>Brush size has to be at least as big as the voxel size.</p>
<aside class="quote no-group" data-username="yakeworld" data-post="1" data-topic="830">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/b4bc9f/48.png" class="avatar"> yakeworld:</div>
<blockquote>
<ol start="3">
<li>Does some parameter that can adjust exist?</li>
</ol>
</blockquote>
</aside>
<p>Could you please explain what do you mean?</p>

---

## Post #4 by @lassoan (2017-08-05 12:48 UTC)

<p>Default surface generation parameters (more precisely, Binary labelmap to Closed surface conversion rule paramters) in Segmentations are set up for creating surface without staircase artifacts. If you prefer having these artifacts then change conversion parameters.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e35ac406d611388fc219830dc931c41fcaa4b28c.png" data-download-href="/uploads/short-url/wrgQJcQjWSi5EpTTuxzObh7dVZW.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e35ac406d611388fc219830dc931c41fcaa4b28c_2_660x500.png" alt="image" data-base62-sha1="wrgQJcQjWSi5EpTTuxzObh7dVZW" width="660" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e35ac406d611388fc219830dc931c41fcaa4b28c_2_660x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e35ac406d611388fc219830dc931c41fcaa4b28c_2_990x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e35ac406d611388fc219830dc931c41fcaa4b28c_2_1320x1000.png 2x" data-dominant-color="C3C1C1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1765×1337 286 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @yakeworld (2017-08-06 09:53 UTC)

<p>Thanks for your replay, It helps me a lot. By set Smoothing factor to 0, it works. But still there is some bug exits. I upload the video for better explain.<br>
<a href="https://pan.baidu.com/s/1qYylKE4" class="onebox" target="_blank" rel="nofollow noopener">https://pan.baidu.com/s/1qYylKE4</a></p>

---
