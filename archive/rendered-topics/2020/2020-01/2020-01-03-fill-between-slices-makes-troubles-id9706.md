# Fill between slices, makes troubles!

**Topic ID**: 9706
**Date**: 2020-01-03
**URL**: https://discourse.slicer.org/t/fill-between-slices-makes-troubles/9706

---

## Post #1 by @NoobForSlicer (2020-01-03 16:15 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/cac653b9f559103c87dcd5668cc6adb2e1a5dde2.png" data-download-href="/uploads/short-url/sVPmuyMNa8NfLYtCyIwMnxh5vsm.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/cac653b9f559103c87dcd5668cc6adb2e1a5dde2_2_247x499.png" alt="1" data-base62-sha1="sVPmuyMNa8NfLYtCyIwMnxh5vsm" width="247" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/cac653b9f559103c87dcd5668cc6adb2e1a5dde2_2_247x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/cac653b9f559103c87dcd5668cc6adb2e1a5dde2_2_370x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/cac653b9f559103c87dcd5668cc6adb2e1a5dde2.png 2x" data-dominant-color="7A8C94"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">485×979 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So here we see the segmenatin before the “fill between slices” and after I applied “fill between the slices”</p>
<p>IT appears to me that this does not only fill the empty slices that were not segmented, but instead changes the shape of already painted segmentation of slices.</p>
<p>How does it do so? What is the logic behind this?</p>
<p>If the slice has already been segmented, and the slice above and the slice above. Why does this function change them if it says "fill BETWEEN slices?</p>
<p>I assume it would fill an empty slice between the two existing segmentations of slices, not change the two existing ones?? Am I wrong?</p>
<p>How does it work?</p>

---

## Post #2 by @muratmaga (2020-01-03 17:46 UTC)

<p>I wonder if this is somewhat related to the previous discussion about slice increments?</p><aside class="quote" data-post="4" data-topic="9087">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/view-displays-lag-if-pixel-spacing-is-small/9087/4">View displays lag if pixel-spacing is small</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    <a class="mention" href="/u/lassoan">@lassoan</a>, I tried and think the lag is no much due to change in the units, but simply the slider has only 0.001 mm increments, so slices do not get changed until the units incremented more than 0.001 mm (which will take 10 slices in this scenario). We will encounter small voxel data more and more through SlicerMorph. I wonder if it possible to tie the precision of the slice views (current seems only three significant digits), to image precision of the volume being displayed?
  </blockquote>
</aside>


---

## Post #3 by @lassoan (2020-01-03 18:30 UTC)

<p>“Fill between slices” effect fills between parallel slices (along any of the 3 axes). See detailed description of the algorithm <a href="http://insight-journal.org/browse/publication/977">here</a>.</p>
<p><em>Any</em> editing operation in the Segment Editor will resample all the segments to the common labelmap geometry. If you have just imported a segment from another segmentation that had different geometry (higher resolution, different origin, or axis directions) then the segment will change upon the first editing operation. Segments are not immediately forced to the common image geometry to allow lossless moving/copying of segments between segmentations.</p>

---

## Post #4 by @lassoan (2022-11-23 22:08 UTC)

<p>3 posts were split to a new topic: <a href="/t/resample-segments-in-segmentation-using-python-scripting/26411">Resample segments in segmentation using Python scripting</a></p>

---
