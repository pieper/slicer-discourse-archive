# Only one of 28  segments is showing in 3d

**Topic ID**: 28934
**Date**: 2023-04-15
**URL**: https://discourse.slicer.org/t/only-one-of-28-segments-is-showing-in-3d/28934

---

## Post #1 by @Tobias (2023-04-15 20:17 UTC)

<p>I downloaded a dataset with maps of arterial regions in the brain. It usually works very well to load them as segments and that step worked well. However, when i try and show it in 3D only once of the segments show. I have checked everything I can think of and i can not see any difference between the segmentations in any setting.</p>
<p>Operating system: win 11<br>
Slicer version: 5.2.2 and slicer 4.11<br>
Expected behavior: All segments should show<br>
Actual behavior: only one show<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68687faba941ad3bf8510063fd025dd3ac19d7dc.jpeg" data-download-href="/uploads/short-url/eTDxKCEmPBgH4qDskpslwLaotZy.jpeg?dl=1" title="slicer problem" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68687faba941ad3bf8510063fd025dd3ac19d7dc_2_690x398.jpeg" alt="slicer problem" data-base62-sha1="eTDxKCEmPBgH4qDskpslwLaotZy" width="690" height="398" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68687faba941ad3bf8510063fd025dd3ac19d7dc_2_690x398.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68687faba941ad3bf8510063fd025dd3ac19d7dc_2_1035x597.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68687faba941ad3bf8510063fd025dd3ac19d7dc.jpeg 2x" data-dominant-color="484C4F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer problem</span><span class="informations">1248×720 85 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-04-15 20:20 UTC)

<p>Check in Data module, maybe you have multiple segmentations and only one is shown in 3D. You can adjust visibility and opacity of each segment separately in Segmentations module, maybe something is set there.</p>
<p>If you cannot figure it out then please save the scene as .mrb and share it with us (upload it to dropbox/onedrive/google drive and post the link here) and we’ll have a look.</p>

---

## Post #3 by @Tobias (2023-04-15 20:41 UTC)

<p>Hi Andras.<br>
I checked the data modul and all segments look the same and should be visible.</p>
<p>here is the file as a .mrb</p><aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1n4WnSm4mNIZgPY1dLDaIVZdsCI5RSVs9/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1n4WnSm4mNIZgPY1dLDaIVZdsCI5RSVs9/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1n4WnSm4mNIZgPY1dLDaIVZdsCI5RSVs9/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1n4WnSm4mNIZgPY1dLDaIVZdsCI5RSVs9/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">Segment probleme.mrb</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Thank you for the help</p>

---

## Post #4 by @lassoan (2023-04-16 13:55 UTC)

<p>Thank you for sharing the file. The problem is that the file stores voxels as floating-point value (<code>float</code> type) instead of an integer type. Using floating-point values uses 4-8x more memory than necessary and there can be issues when computing equality between values, therefore Slicer never does this. However, it seems that Slicer does not prevent importing of images of this type as segmentation.</p>
<p>We’ll probably just disable loading of float volumes as segmentations into Slicer (see <a href="https://github.com/Slicer/Slicer/issues/6941" class="inline-onebox">Segmentation closed surface representation generation fails for float voxels · Issue #6941 · Slicer/Slicer · GitHub</a>).</p>
<p>To fix your problem, you need to set the voxel type to <code>unsigned char</code> (if you have more than 255 segments then <code>unsigned short</code>) when you create a segmentation file. How did you create this .seg.nrrd file?</p>

---

## Post #5 by @Tobias (2023-04-16 20:20 UTC)

<p>Hi i downloaded this dataset<br>
<a href="https://www.nitrc.org/doi/landing_page.php?table=groups&amp;id=1498&amp;doi=" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.nitrc.org/doi/landing_page.php?table=groups&amp;id=1498&amp;doi=</a><br>
and then loaded the atlas file as a segmentation.</p>
<p>Tried with a different version and then it worked.</p>
<p>Thank you for the help!</p>

---
