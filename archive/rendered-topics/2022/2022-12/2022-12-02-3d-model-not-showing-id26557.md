---
topic_id: 26557
title: "3D Model Not Showing"
date: 2022-12-02
url: https://discourse.slicer.org/t/26557
---

# 3D model not showing

**Topic ID**: 26557
**Date**: 2022-12-02
**URL**: https://discourse.slicer.org/t/3d-model-not-showing/26557

---

## Post #1 by @snykamp (2022-12-02 19:44 UTC)

<p>I am trying to create some 3D models for teaching.  I have imported the CT and figured out how to paint or segment the ROI’s but I cannot see the 3D model and when I try to grow a seed nothing happens either.  Any ideas?</p>
<p>Thanks<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44b91858ba57c0b167ffd2696205d1c996ed572c.jpeg" data-download-href="/uploads/short-url/9NX20CZoz0bwovJQgGCKaI1WGhC.jpeg?dl=1" title="Screenshot 2022-12-02 at 1.09.33 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44b91858ba57c0b167ffd2696205d1c996ed572c_2_690x471.jpeg" alt="Screenshot 2022-12-02 at 1.09.33 PM" data-base62-sha1="9NX20CZoz0bwovJQgGCKaI1WGhC" width="690" height="471" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44b91858ba57c0b167ffd2696205d1c996ed572c_2_690x471.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44b91858ba57c0b167ffd2696205d1c996ed572c_2_1035x706.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44b91858ba57c0b167ffd2696205d1c996ed572c_2_1380x942.jpeg 2x" data-dominant-color="383D45"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-12-02 at 1.09.33 PM</span><span class="informations">1920×1313 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-12-02 19:49 UTC)

<p>You can click <code>Apply</code> and then click <code>Show 3D</code>.</p>
<p>There are lots of segmentation tutorials, both slides and youtube videos, that may help with getting started (see <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html#tutorials">here</a>), but if you get stuck then feel free to ask more questions here. All questions are helpful for us because then we can learn from that what parts of the application should be made simpler, or should be better covered by our documentation or tutorials.</p>

---

## Post #3 by @snykamp (2022-12-02 20:38 UTC)

<p>Thanks.  I have watched a lot of the tutorials and they are helpful.  The problem is when I select apply and show 3D nothing happens.  I cannot do a volume rendering or anything else in 3D.  I did not have this issue last time and made models and the CT is a standard DICOM set so I am not sure what to try next.</p>

---

## Post #4 by @pieper (2022-12-02 21:58 UTC)

<p>You may need to use the Center 3D View button.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#d-view" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#d-view</a></p>

---

## Post #5 by @snykamp (2022-12-03 20:20 UTC)

<p>That did the trick. Thanks</p>

---
