---
topic_id: 23516
title: "Why When Adding Point Using Pickn Paint Module It Add Too Ma"
date: 2022-05-21
url: https://discourse.slicer.org/t/23516
---

# Why when adding point using Pick'n paint module it add too many points?

**Topic ID**: 23516
**Date**: 2022-05-21
**URL**: https://discourse.slicer.org/t/why-when-adding-point-using-pickn-paint-module-it-add-too-many-points/23516

---

## Post #1 by @Moh_d_Al-Watary (2022-05-21 08:16 UTC)

<p>Operating system:Windows 10 Education<br>
Slicer version:4.13.0-2022-02-02<br>
Expected behavior: when adding a point using Pick’n paint module, it will add only one point in the specific area.<br>
Actual behavior: automatically a lot of point are added (as shown in the screen shot below)!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/932844a61fedbfc315d5a18e2830ed326c631c7e.png" data-download-href="/uploads/short-url/kZOsF2NzSDE3vLEkTlwsL5tiwDI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/932844a61fedbfc315d5a18e2830ed326c631c7e_2_690x387.png" alt="image" data-base62-sha1="kZOsF2NzSDE3vLEkTlwsL5tiwDI" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/932844a61fedbfc315d5a18e2830ed326c631c7e_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/932844a61fedbfc315d5a18e2830ed326c631c7e_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/932844a61fedbfc315d5a18e2830ed326c631c7e.png 2x" data-dominant-color="BDC1DA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×768 184 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2022-05-21 13:51 UTC)

<p>Probably this module has not been updated to work with recent Slicer versions.</p>
<p>In latest Slicer versions, the <code>Dynamic Modeler</code> module has a new tool <code>Select by points</code>, which can be used instead of Pick and Paint:</p>
<aside class="quote quote-modified" data-post="1" data-topic="22165">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-dynamic-modeler-tool-select-by-points/22165">New Dynamic Modeler Tool: Select by Points</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    <a href="https://www.youtube.com/watch?v=Klsi6x3F5D4" target="_blank" rel="noopener">
    [Select By Points Tool, Dynamic Modeler, 3D Slicer]
  </a>


Select by points tool is available on the Dynamic Modeler module since end of October 2021 Slicer Preview Release 
This tools allows you to create 2 types of output models from an input model, a fiducial list, a selection-distance and a selection-algorithm. 
One of the possible outputs is copy of the input model with selection scalars (unselected=0, selected=1) according to the selection-algorithm and selection-distance using the f…
  </blockquote>
</aside>


---

## Post #3 by @Moh_d_Al-Watary (2022-05-26 07:03 UTC)

<p>Thank you for your reply, but I still confused!<br>
I am measuring the distance between two models of the same region but on two time different CT, so I was using Pick’ n pain (to determine the ROI), distance to distance model (to calculate the distance between the two superimposed models) and the using Mesh statistics (to export the measurements in mm)!<br>
Now, I have loaded the models, opened the dynamic modeler: but could not use it (although seen the shared YouTube clip, still not clear)!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f03d7cbb0c42c6d4a46146100859b81cdd84a8b.png" data-download-href="/uploads/short-url/6HUFP9rXPZXnkxr07NGW0zlSNar.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f03d7cbb0c42c6d4a46146100859b81cdd84a8b_2_690x387.png" alt="image" data-base62-sha1="6HUFP9rXPZXnkxr07NGW0zlSNar" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f03d7cbb0c42c6d4a46146100859b81cdd84a8b_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f03d7cbb0c42c6d4a46146100859b81cdd84a8b_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f03d7cbb0c42c6d4a46146100859b81cdd84a8b.png 2x" data-dominant-color="C0C0D8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×768 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>a second question-please-: when I have do registration of T1 and T2 CT and saved them, when I reopened them they appear like this (disoriented) so how could this be solved?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3a93736b3bea87a63a23753ca9a8d0dc12e4bba.png" data-download-href="/uploads/short-url/wtYVzXPaTESM0bOYO9ssyaAeNRg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3a93736b3bea87a63a23753ca9a8d0dc12e4bba_2_690x387.png" alt="image" data-base62-sha1="wtYVzXPaTESM0bOYO9ssyaAeNRg" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3a93736b3bea87a63a23753ca9a8d0dc12e4bba_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3a93736b3bea87a63a23753ca9a8d0dc12e4bba_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3a93736b3bea87a63a23753ca9a8d0dc12e4bba.png 2x" data-dominant-color="9D9EAE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×768 219 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Thank you so much for valuable time and advices</p>
<p>Sincerely</p>

---
