---
topic_id: 21996
title: "3 Hi Res Are In Different Volumes"
date: 2022-02-16
url: https://discourse.slicer.org/t/21996
---

# 3 Hi Res are in different volumes

**Topic ID**: 21996
**Date**: 2022-02-16
**URL**: https://discourse.slicer.org/t/3-hi-res-are-in-different-volumes/21996

---

## Post #1 by @Alejandro_Terrado (2022-02-16 15:41 UTC)

<p>Hi, once again I’m facing with this issue that I couldn’t surpass before. Even following all the indications in other posts similar to this.<br>
Can someone help on having the 3 hi resolution axes in one master. This is for later segmentation and 3D printing for a cirjury.<br>
This is the full CT, buy I only need the head.</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://owncloud.cemep.com.ar/s/KG2jRwQ6R7KZJqY">
  <header class="source">
      <img src="https://owncloud.cemep.com.ar/apps/theming/favicon?v=1" class="site-icon" width="128" height="128">

      <a href="https://owncloud.cemep.com.ar/s/KG2jRwQ6R7KZJqY" target="_blank" rel="noopener nofollow ugc">Nextcloud</a>
  </header>

  <article class="onebox-body">
    <img src="https://owncloud.cemep.com.ar/apps/theming/icon?v=1" class="thumbnail onebox-avatar" width="500" height="500">

<h3><a href="https://owncloud.cemep.com.ar/s/KG2jRwQ6R7KZJqY" target="_blank" rel="noopener nofollow ugc">1.2.840.113619.2.278.3.2831205601.992.1639738207.808.zip</a></h3>

  <p>Nextcloud - a safe home for all your data</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
Please help!</p>

---

## Post #2 by @lassoan (2022-02-18 05:10 UTC)

<p>Can you describe what you tried (and link the relevant posts)?</p>

---

## Post #3 by @Alejandro_Terrado (2022-03-03 01:59 UTC)

<p>This are some of the topics I read:</p><aside class="quote quote-modified" data-post="2" data-topic="2941">
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
<aside class="quote quote-modified" data-post="6" data-topic="2871">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/import-volume-by-projections/2871/6">Import volume by projections</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    OK, so you actually have cross-sectional images. Not projections. I guess you have those kind of volumes where you have high-resolution slices with huge gaps between them (spacing between slices is a magnitude larger than pixel spacing within the slice). 
Unfortunately, it is a very difficult problem to create high-resolution data from these sparse slices, since in general you have no way of knowing what is between slices. If you have a priori information about the image content then you may be …
  </blockquote>
</aside>

<p>But none of them actually helped me.<br>
Can you please take a look and give me an orientation on how to obtain a master volume to do a segmentation.<br>
Thanl you!</p>

---

## Post #4 by @lassoan (2022-03-14 22:00 UTC)

<p>You have found the relevant posts. The simplest solution is described <a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941/2">here</a>:</p>
<blockquote>
<p>You may also try to use your volumes for segmentation one by one (since you can swap the master volume any time): Create a high-resolution isotropic volume from any of the input volumes, using Crop volume module. Then create a segmentation node using this isotropic volume as master volume. After this you can switch between master volumes - the segmentation node’s internal binary labelmap representation will remain high-resolution and isotropic. For example, you can segment the structure of interest based on one image, then switch master volume and make adjustments in the segmentation as needed. Unfortunately, this is a manual, iterative process.</p>
</blockquote>
<p>All other solutions would require you to set up image reconstruction tools (download or build the tool, figure out how to use it, apply it on your data, and see if it can improve the image quality).</p>

---
