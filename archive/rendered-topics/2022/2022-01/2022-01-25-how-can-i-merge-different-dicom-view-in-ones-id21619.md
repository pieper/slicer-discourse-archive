# How can I merge different DICOM view in ones? 

**Topic ID**: 21619
**Date**: 2022-01-25
**URL**: https://discourse.slicer.org/t/how-can-i-merge-different-dicom-view-in-ones/21619

---

## Post #1 by @AndreaChiericati (2022-01-25 12:44 UTC)

<p>Hi all,<br>
Do you know if I could merge different DICOM that have a good quality on one view, but in the others not? Do you know how can I merge it all together?</p>

---

## Post #2 by @Juicy (2022-01-25 22:01 UTC)

<p>As far as I am aware there is no effective way of doing this on 3D Slicer. Basically, you have to acquire the scan in high resolution (minimal field of view (FOV) and small slice thickness/interval) at the point of acquisition i.e. when taking the CT scan. Depending on the acquisition parameters used you may be able to reconstruct the CT scan with smaller slice thicknesses/intervals or FOV if you have access to the original CT machine and the scan is still on the machine (if it was taken recently). Have a read of these related posts:</p>
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

## Post #3 by @stevenagl12 (2022-01-25 22:04 UTC)

<p>you could do this programmatically, by reading in the first DICOM, and (so long as you know the slices or regions) indexing into the image to change the values themselves to the new values from the new file (so long as spatial dimensions, direction, and such are preserved, especially if you have them registered together).</p>

---

## Post #4 by @lassoan (2022-01-25 23:53 UTC)

<aside class="quote no-group" data-username="stevenagl12" data-post="3" data-topic="21619">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>so long as spatial dimensions, direction, and such are preserved</p>
</blockquote>
</aside>
<p>I don’t think this is the case. <a class="mention" href="/u/andreachiericati">@AndreaChiericati</a> would like to merge 3 sets of slices, each set with a different orientation, and fill in the blanks in between the slices that are quite far from each other (slice spacing is huge compared to in-slice pixel spacing). That is an extremely hard task and it cannot be solved in a general way, but you need to have some model that knows how to fill in the gaps. Nowadays this would be implemented by a well-trained deep learning model.</p>

---

## Post #5 by @pieper (2022-01-25 23:58 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="21619">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Nowadays this would be implemented by a well-trained deep learning model.</p>
</blockquote>
</aside>
<p>SynthSR is an example of doing this in the brain.  It would be great if people made similar tools for other parts of the body.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/BBillot/SynthSR">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/BBillot/SynthSR" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/43f9f45f4392e27b3dea923d8dd870c491fbe5a53d51c43ee0d7bea0602869d1/BBillot/SynthSR" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/BBillot/SynthSR" target="_blank" rel="noopener">GitHub - BBillot/SynthSR: A framework for joint super-resolution and image...</a></h3>

  <p>A framework for joint super-resolution and image synthesis, without requiring real training data - GitHub - BBillot/SynthSR: A framework for joint super-resolution and image synthesis, without requ...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @stevenagl12 (2022-01-26 12:50 UTC)

<p>Couldn’t you also register the models, resample them to a set voxel dimension, and then insert these slices into the appropriately interpolated regions?</p>

---

## Post #7 by @pieper (2022-01-26 12:53 UTC)

<p>Typically the problem is there is missing data.  If you have widely spaced slices in one direction they are like lines on ruled writing paper with empty space between.  If you have two directions they are like lines on graph paper and the problem is that you don’t know how to fill in the boxes with accurate data.</p>

---
