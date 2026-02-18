# Separate and combine images/views/planes from different sequences

**Topic ID**: 12989
**Date**: 2020-08-13
**URL**: https://discourse.slicer.org/t/separate-and-combine-images-views-planes-from-different-sequences/12989

---

## Post #1 by @Fluvio_Lobo (2020-08-13 21:57 UTC)

<p>Hello,</p>
<p>I am working with three ‘haste’ sequences where each sequence has the highest resolution on 1/3 planes/views. I.e. one of the sequences has better coronal images than the other two and so on. Is it possible to extract the images corresponding to a specific view and re-combine them in a new volume?</p>
<p>The sequences have almost identical sizes and spacing.</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2020-08-14 00:36 UTC)

<p>There is no easy way to combine them. See more information here:</p>
<aside class="quote quote-modified" data-post="2" data-topic="2941">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941/2">Combining volumes - what am I missing?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    In general, these multiple low-resolution acquisitions are not well suited for any 3D processing, so the best would be to acquire proper 3D volume, with as isotropic spacing (cubic voxel shape) as possible. 
You may try to find toolkits that can create an isotropic super-resolution image from multiple low-resolution sweeps, but this is a difficult image reconstruction problem, so there are no standard solutions. Have a look at this post <a href="https://discourse.slicer.org/t/import-volume-by-projections/2871/6">Import volume by projections</a> for info on a toolkit that mig…
  </blockquote>
</aside>


---
