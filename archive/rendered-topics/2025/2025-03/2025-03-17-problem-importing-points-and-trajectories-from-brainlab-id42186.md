# Problem importing points and trajectories from BrainLab

**Topic ID**: 42186
**Date**: 2025-03-17
**URL**: https://discourse.slicer.org/t/problem-importing-points-and-trajectories-from-brainlab/42186

---

## Post #1 by @Shirly_Someck (2025-03-17 15:15 UTC)

<p>Hi,<br>
I have exported data from BrainLab station, and managed to import the MRI scans and object segmentation. When I try to upload the points and trajectories, slicer gives the following error:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1ad70eae2b897d32a88a45555d872590599579f.png" data-download-href="/uploads/short-url/rDlKlNk9Gl92KVPtlbYbOjEl6Fx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1ad70eae2b897d32a88a45555d872590599579f.png" alt="image" data-base62-sha1="rDlKlNk9Gl92KVPtlbYbOjEl6Fx" width="690" height="190" data-dominant-color="ECEBE6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">777×215 9.55 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I am using Slicer version 5.6.2 on Windows 10</p>
<p>Would appreciate any help!<br>
Thanks</p>

---

## Post #2 by @pieper (2025-03-17 15:59 UTC)

<p>You might have the same issue discussed here:</p>
<aside class="quote quote-modified" data-post="1" data-topic="41971">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/arber_demi/48/79554_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/unable-to-load-landmark-points-from-dicom-surface-segmentation-created-by-brainlab-origin/41971">Unable to load landmark points from DICOM Surface Segmentation created by BrainLab Origin</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello everyone, 
I’m trying to load some DICOM segmentation file, similar to <a href="https://discourse.slicer.org/t/unable-to-load-dicom-segmentation-file/15134">“Unable to load DICOM segmentation file”</a>. I am running into the same issue of not being able to load these files. The files do have reference images that I also have, with the correct UID references, but it makes no difference with loading. (I assume it would only matter for their positioning in any case) 
However my problem seems to be one option mentioned by issakomi, where the SEG here has SOPClassUID = 1.2.840.10008…
  </blockquote>
</aside>


---
