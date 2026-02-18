# Combining registered volumes from different perspectives for improved resolution

**Topic ID**: 43960
**Date**: 2025-08-04
**URL**: https://discourse.slicer.org/t/combining-registered-volumes-from-different-perspectives-for-improved-resolution/43960

---

## Post #1 by @sulli419 (2025-08-04 22:04 UTC)

<p>Say I have two MR volumes of the same brain; one coronal and one sagittal.  The axial z resolution is ~5x poorer volume.  I imagine there must be some way (after registering the volumes) to create a new “average” volume that only uses pixels from the higher res (theoretically sharper) planes (xy) from each perspective.  Is there any feature built into slicer that does this? Any terms to search for?  I’m tempted to also use it for microscopy data.  Not sure if deconvolution / point-spread information is required to squeeze more resolution out of the image.</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2025-08-04 22:15 UTC)

<p>Yes, this comes up from time to time.  Here’s a thread with some more info.  I don’t think we have a standardized tool for this yet but with all the recent AI stuff probably there are better methods available somewhere.</p>
<aside class="quote quote-modified" data-post="1" data-topic="15847">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/guy_ma/48/9776_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/trying-to-take-three-different-volumes-to-create-one-3d-model-beginner-of-3d-slicer/15847">Trying to take three different volumes to create one 3d model (beginner of 3d slicer)</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    Operating system:Windows 10 
Slicer version: Latest 
Expected behavior: I want to use the views that I set in the panels for the 3d model 
Actual behavior: Only uses one volume, which makes the 3d model poor quality (because the other two views are pixelated 
Im not sure exactly how to do this. I had an MRI recently, and I want to make an interactive model with the scans I got. But when I set it at only one of the volumes, only one of the views is good quality. So I tried setting the other two w…
  </blockquote>
</aside>


---

## Post #3 by @sulli419 (2025-08-04 23:01 UTC)

<p>Thanks.  Yes, I stumbled on <a href="https://github.com/gift-surg/NiftyMIC#niftymic-applied-to-fetal-brain-mri" rel="noopener nofollow ugc">NiftyMIC</a> as well (also discussed in your example forum).  It sounds like it requires segmentations in each perspective as landmarks?  I’m an amateur at this, but I can picture how something like a point spread function could fall out of how the segments are distorted by different perspectives.  Maybe this is hope that it could work on things other than what it was designed for (MR of fetal brains)?  Anyone know the latest overall sentiment on the generalizability of NiftyMIC?</p>
<p>If anyone knows of more recent easy to use pipelines please chime in.</p>
<p>Cheers</p>

---
