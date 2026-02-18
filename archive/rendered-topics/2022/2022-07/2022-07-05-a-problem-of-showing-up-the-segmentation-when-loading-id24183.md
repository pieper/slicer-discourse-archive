# A problem of showing up the segmentation when loading

**Topic ID**: 24183
**Date**: 2022-07-05
**URL**: https://discourse.slicer.org/t/a-problem-of-showing-up-the-segmentation-when-loading/24183

---

## Post #1 by @zkzk96871 (2022-07-05 12:30 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2c131f66592766aac800d2365cb3d99eaa04a58.jpeg" data-download-href="/uploads/short-url/pvkUkaNGobpE6c76WUXcXuFF7Ru.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b2c131f66592766aac800d2365cb3d99eaa04a58_2_690x431.jpeg" alt="image" data-base62-sha1="pvkUkaNGobpE6c76WUXcXuFF7Ru" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b2c131f66592766aac800d2365cb3d99eaa04a58_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b2c131f66592766aac800d2365cb3d99eaa04a58_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b2c131f66592766aac800d2365cb3d99eaa04a58_2_1380x862.jpeg 2x" data-dominant-color="7A797F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1200 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I loaded a nii label file segemented by others and i met a problem. As the image shows, teeth are segmented well in the 3D view, but in the three views the segmentations are gone. And I don’t know how to make it show up, please help me.</p>

---

## Post #2 by @lassoan (2022-07-05 16:19 UTC)

<p>If you drag-and-drop a segmentation to a view then it will only be displayed in that view (it is not displayed in <em>all</em> views anymore). You can drag-and-drop the segmentation to each view your want to see it in.</p>
<p>If you want to see the segmentation in 3D then you can right-click on it in Data module and choose “Create closed surface representation”.</p>

---

## Post #3 by @zkzk96871 (2022-07-06 07:11 UTC)

<p>Thanks for your response. Unfortunately, when i drag-and-drop the segmentation into a view, the annotations still cannot be seen except for 3D view. I am so confused how to show it in other three views(that is axial plane, coronal plane and sagittal plane).</p>

---

## Post #4 by @lassoan (2022-07-06 12:56 UTC)

<aside class="quote no-group" data-username="zkzk96871" data-post="3" data-topic="24183">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zkzk96871/48/15866_2.png" class="avatar"> zkzk96871:</div>
<blockquote>
<p>Thanks for your response. Unfortunately, when i drag-and-drop the segmentation into a view, the annotations still cannot be seen except for 3D view.</p>
</blockquote>
</aside>
<p>This is exactly the correct, expected behavior, as I described above. If you wan to show the segmentation only in specific views then drag-and-drop the segmentation in each view you want to see it in: not just drag-and-drop it into the 3D view but also drag-and-drop it into slice views where you want to see the segmentation in.</p>
<p>If you want to see the segmentation in all the views, including all 3D views then you can right-click on the segmentation in Data module and choose “Create closed surface representation”. Once you have a surface representation, the segmentation will appear in all 3D views (unless you chose to show segmentation in selected views only, by drag-and-dropping it into specific views).</p>

---

## Post #5 by @pieper (2022-07-06 13:19 UTC)

<p>Hard to tell from the description, but possibly you are seeing an issue like this one:</p>
<aside class="quote quote-modified" data-post="2" data-topic="24041">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-could-i-measure-the-mandibular-condyle-rotation-using-3d-slicer/24041/2">How could I measure the mandibular condyle rotation using 3D Slicer?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Probably you have an issue with the coordinate system conventions.  You can read up on RAS and LPS in the forum: <a href="https://discourse.slicer.org/search?q=lps%20ras" class="inline-onebox">Search results for 'lps ras' - 3D Slicer Community</a> 
You can change options when loading if needed: 
[image] 
The SlicerCMF team might be able to comment on your other questions.
  </blockquote>
</aside>


---
