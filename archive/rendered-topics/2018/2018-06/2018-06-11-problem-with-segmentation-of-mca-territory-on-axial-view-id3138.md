---
topic_id: 3138
title: "Problem With Segmentation Of Mca Territory On Axial View"
date: 2018-06-11
url: https://discourse.slicer.org/t/3138
---

# Problem with segmentation of MCA territory on axial view

**Topic ID**: 3138
**Date**: 2018-06-11
**URL**: https://discourse.slicer.org/t/problem-with-segmentation-of-mca-territory-on-axial-view/3138

---

## Post #1 by @mag (2018-06-11 16:23 UTC)

<p>Hello,</p>
<p>I think I have a similar problem to what described in this post</p><aside class="quote quote-modified" data-post="1" data-topic="1950">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/masteling/48/13587_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/creating-a-new-volume-from-a-rotated-plane/1950">Creating a new volume from a rotated plane</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi everyone, 
My main goal is to segment/label map a anatomical feature in a rotated plane. 
I’m using MRI and I’m rotating the plane using Reformat to rotate a slice to a given angle. Then I want to segment an anatomical feature in that rotated plane.  If I do it directly there, the plane either changes back to it’s original position or I have the “stair case effect”, with the segmentation spread about different slices. 
I would like to know if it is possible to create a new volume of the rotat…
  </blockquote>
</aside>
<p>
but I don’t understand how to use Crop Volume to solve the issue.</p>
<p>My aim is to mark the 3D territory of the middle cerebral artery on CT angiography scans. In order to do so I am using some axial reference pictures:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e99eb422b19a7988bb94f7814c8c130156f7a06.png" data-download-href="/uploads/short-url/4mI5PlJRSXivFkuXY6HfQicq3QO.png?dl=1" title="MCA" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e99eb422b19a7988bb94f7814c8c130156f7a06_2_690x413.png" alt="MCA" data-base62-sha1="4mI5PlJRSXivFkuXY6HfQicq3QO" width="690" height="413" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e99eb422b19a7988bb94f7814c8c130156f7a06_2_690x413.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e99eb422b19a7988bb94f7814c8c130156f7a06.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e99eb422b19a7988bb94f7814c8c130156f7a06.png 2x" data-dominant-color="BBB0B1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">MCA</span><span class="informations">1032×619 685 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Therefore I would like to tilt my scans to display them in the same view as the reference images (at the same tilting angle which is good for recognising the MCA territory on the axial view),  so that I could mark the MCA territory by simply “imitating” what is displayed on the reference. Then I would like to use “fill in between slices” to obtain the 3D vascular territory and refine manually with the erase tool or further drawing where required.</p>
<p>The problem is that if I rotate my volume and then use the draw tool in segment editor I get the artifacts described in other posts:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e9462537275e8c7dcd97a1a9dda2d42ccd1b043.png" data-download-href="/uploads/short-url/mCRlOciRHeZIQ9j9roct5DfBDoL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e9462537275e8c7dcd97a1a9dda2d42ccd1b043_2_690x388.png" alt="image" data-base62-sha1="mCRlOciRHeZIQ9j9roct5DfBDoL" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e9462537275e8c7dcd97a1a9dda2d42ccd1b043_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e9462537275e8c7dcd97a1a9dda2d42ccd1b043_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e9462537275e8c7dcd97a1a9dda2d42ccd1b043_2_1380x776.png 2x" data-dominant-color="7A7A80"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 506 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And I have tried to use the Crop Volume module but I don’t see any difference, the artifacts are still there. Or maybe I didn’t understand what I’m supposed to do in Crop Volume. Can you help?</p>
<p>Thank you</p>

---

## Post #2 by @mag (2018-06-12 16:02 UTC)

<p>I think I have actually solved my problem thanks to the reply to this post.</p><aside class="quote quote-modified" data-post="3" data-topic="3123">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/f14d63/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/segments-created-in-segment-editor-are-a-collection-of-unconnected-stripes/3123/3">Segments created in segment editor are a collection of unconnected stripes</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi Csaba 
Thank you for the response. I did actually also try the nightly build and the behavior was the same. I was using the sample “MR US prostate” data and that data was indeed rotated in the axial view. However after rotating it as you suggest, I cannot contour it. the moment I right-click or type “a” the contour disappears. Is that behavior expected? 
Kind regards, 
Bo 
PS. I would not have bothered you had I only had problem with the ultrasound data.The stripey phenomenon was also a probl…
  </blockquote>
</aside>
<p>
Now I first create a ROI, rotate my volume but not the ROI and then crop so the new cropped volume is aligned to the slicer axis and the segmentation tools work fine.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/682fa612a91e6ddbad8c76dfbd57283d0f8d9c7b.jpeg" data-download-href="/uploads/short-url/eRFK7kGculjZhvlbOyDaxusqVK3.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/682fa612a91e6ddbad8c76dfbd57283d0f8d9c7b_2_690x388.jpeg" alt="image" data-base62-sha1="eRFK7kGculjZhvlbOyDaxusqVK3" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/682fa612a91e6ddbad8c76dfbd57283d0f8d9c7b_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/682fa612a91e6ddbad8c76dfbd57283d0f8d9c7b_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/682fa612a91e6ddbad8c76dfbd57283d0f8d9c7b_2_1380x776.jpeg 2x" data-dominant-color="818188"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 366 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Sorry for my first post, that was really easy in the end.</p>

---

## Post #3 by @timeanddoctor (2018-06-14 13:13 UTC)

<p>interesting and usful</p>

---

## Post #4 by @lassoan (2018-06-14 21:52 UTC)

<p>We’ve added a button to Segment editor that appears when slices are misaligned and clicking that automatically aligns them to the segmentation (available in nightly builds from tomorrow).</p>

---
