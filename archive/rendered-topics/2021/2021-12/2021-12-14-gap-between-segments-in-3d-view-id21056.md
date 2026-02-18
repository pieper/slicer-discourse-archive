# Gap between segments in 3D view

**Topic ID**: 21056
**Date**: 2021-12-14
**URL**: https://discourse.slicer.org/t/gap-between-segments-in-3d-view/21056

---

## Post #1 by @chir.set (2021-12-14 16:07 UTC)

<p>I noticed this gap between 2 segments in 3D view, while it does not exist in slice views.</p>
<p>Load any volume<br>
Create a new segmentation<br>
Paint a segment on a single slice<br>
Paint a second smaller segment inside the first one, with default masking options.</p>
<p>The result is as below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/8495b04699867fd98e4b5a326e53e53ae1515140.png" data-download-href="/uploads/short-url/iUTJpkHWSqPDP9PMh5dthxnNOJa.png?dl=1" title="gap" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/8495b04699867fd98e4b5a326e53e53ae1515140_2_276x500.png" alt="gap" data-base62-sha1="iUTJpkHWSqPDP9PMh5dthxnNOJa" width="276" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/8495b04699867fd98e4b5a326e53e53ae1515140_2_276x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/8495b04699867fd98e4b5a326e53e53ae1515140_2_414x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/8495b04699867fd98e4b5a326e53e53ae1515140.png 2x" data-dominant-color="585A4F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">gap</span><span class="informations">495×896 82.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It’s doubtful to be an expected result. Either the inner segment is too small, or the outer one has been trimmed.</p>
<p>A real concern is its impact on the reliability of segment statisics. Would one segment be under-estimated ?</p>
<p>Can someone comment on this ?</p>
<p>Thanks.</p>

---

## Post #2 by @jamesobutler (2021-12-14 17:30 UTC)

<p>Statistics is based on the segmentation labelmap as you are seeing in the 2D slice view. What you’re showing in the 3D view is the segmentation with a smoothing factor applied for display purposes only. It is not removing actual features in the segmentation.</p>
<p>See the below post from another thread</p>
<aside class="quote" data-post="3" data-topic="19750">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/whats-the-different-between-show3d-smooth-and-the-segments-smooth/19750/3">What's the different between show3D smooth and the segment's smooth?</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Surface smoothing is required for reconstructing a continuous surface mesh from discrete samples stored in a labelmap volume. This smoothing does not remove any details from the segmentation. If you set surface smoothing to 0 then you will see the discrete samples instead of the reconstructed surface (each voxel of the labelmap will appear as a cube). 
Smoothing effect is for removing irrelevant details (i.e., surface noise, speckled, small holes) from the segmentation.
  </blockquote>
</aside>


---

## Post #3 by @lassoan (2021-12-14 17:39 UTC)

<p>Segment Statistics module can compute metrics from both the binary labelmap and closed surface representations. Some metrics, such as surface area are better computer from the smoothed surface. Volume can be computed from both.</p>
<p>If you just want to compute surface area of a 2D area (and not a 3D structure) then it may be simpler to use Markups module: create a closed curve and enable “area” measurement in the Measurements section.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba17c47699112619647ac650c3bd3ef8e588b2eb.png" data-download-href="/uploads/short-url/qyfJjX9JWHHEHtQzSgtiRUnH26n.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba17c47699112619647ac650c3bd3ef8e588b2eb_2_679x499.png" alt="image" data-base62-sha1="qyfJjX9JWHHEHtQzSgtiRUnH26n" width="679" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba17c47699112619647ac650c3bd3ef8e588b2eb_2_679x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba17c47699112619647ac650c3bd3ef8e588b2eb_2_1018x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba17c47699112619647ac650c3bd3ef8e588b2eb_2_1358x998.png 2x" data-dominant-color="3E3F3E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1533×1128 277 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If you want to measure cross-sectional areas of 3D structures then you can find dedicated modules for that.</p>

---

## Post #4 by @chir.set (2021-12-14 18:34 UTC)

<p>Thanks, it displays without any gap after cancelling smoothing.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="21056">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Statistics is based on the segmentation labelmap as you are seeing in the 2D slice view</p>
</blockquote>
</aside>
<p>That’s important information.</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="21056">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>it may be simpler to use Markups module: create a closed curve</p>
</blockquote>
</aside>
<p>Yes, it’s an easy solution for surface area, thanks. I’m just tinkering again with other vague ideas.</p>

---

## Post #5 by @lassoan (2021-12-16 18:16 UTC)

<aside class="quote no-group quote-modified" data-username="chir.set" data-post="4" data-topic="21056">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="21056">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Statistics is based on the segmentation labelmap as you are seeing in the 2D slice view</p>
</blockquote>
</aside>
<p>That’s important information.</p>
</blockquote>
</aside>
<p>There are segment statistics computation plugins that use the binary labelmap representation and there are plugins that use the closed surface representation.</p>

---

## Post #6 by @jamesobutler (2021-12-16 19:20 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="21056">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Statistics is based on the segmentation labelmap as you are seeing in the 2D slice view.</p>
</blockquote>
</aside>
<p>Yes this is because I almost always use binary labelmap statistics plugins. If you the plugins those based on the closed surface then yes what you see in the 3D view is going to be used for statistics.</p>

---

## Post #7 by @chir.set (2021-12-16 20:13 UTC)

<p>Thank you all, that distinction between binary label map and closed surface sources, and its implications, were not immediately evident to me. I have better insight now.</p>

---
