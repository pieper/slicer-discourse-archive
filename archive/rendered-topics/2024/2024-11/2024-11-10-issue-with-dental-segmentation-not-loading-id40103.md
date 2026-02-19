---
topic_id: 40103
title: "Issue With Dental Segmentation Not Loading"
date: 2024-11-10
url: https://discourse.slicer.org/t/40103
---

# Issue with dental segmentation not loading

**Topic ID**: 40103
**Date**: 2024-11-10
**URL**: https://discourse.slicer.org/t/issue-with-dental-segmentation-not-loading/40103

---

## Post #1 by @mohammed_alshakhas (2024-11-10 12:47 UTC)

<p>tried multiple times to re do the process but still same error</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a93181ff379938790e280844b0210158d65c3189.png" data-download-href="/uploads/short-url/o8KLgYbELGVf07dno9dYJn5ZAWB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a93181ff379938790e280844b0210158d65c3189_2_517x186.png" alt="image" data-base62-sha1="o8KLgYbELGVf07dno9dYJn5ZAWB" width="517" height="186" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a93181ff379938790e280844b0210158d65c3189_2_517x186.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a93181ff379938790e280844b0210158d65c3189_2_775x279.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a93181ff379938790e280844b0210158d65c3189_2_1034x372.png 2x" data-dominant-color="8F8D8D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1132×409 23.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-11-10 14:14 UTC)

<p>You may have run into this issue:</p>
<aside class="quote" data-post="7" data-topic="38142">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/totalsegmentator-failed-to-compute-results-returned-non-zero-exit-status-1/38142/7">TotalSegmentator Failed to compute results....returned non-zero exit status 1</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    It appears MIC-DFZ has messed up their packages with a recent new dependency release. See the following link below for details:
  </blockquote>
</aside>


---

## Post #3 by @mohammed_alshakhas (2025-01-24 12:59 UTC)

<p>is the problem solved now ?  sometime ago i downloaded more recent version of slicer and the issue wasn’t solved yet .</p>

---

## Post #4 by @jamesobutler (2025-01-24 15:57 UTC)

<p>Yes the issue was resolved on January 2nd.</p>
<aside class="quote" data-post="11" data-topic="38142">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/totalsegmentator-failed-to-compute-results-returned-non-zero-exit-status-1/38142/11">TotalSegmentator Failed to compute results....returned non-zero exit status 1</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Following up here I issued a PR to the SlicerNNUnet extension which is involved in installing acvl_utils and fixed the installation issues. So manually calling pip_install here is no longer needed as long as you have updated your extension to this latest version.
  </blockquote>
</aside>


---

## Post #5 by @mohammed_alshakhas (2025-02-04 16:14 UTC)

<p>still getting " cant load segmentation error in 5.9 version on pc<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd72e50f18b285135ad21f6c31ad72b63807c738.png" data-download-href="/uploads/short-url/Aa6XzKXRIYXAOrLEQ4We5BWxc7u.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd72e50f18b285135ad21f6c31ad72b63807c738_2_690x271.png" alt="image" data-base62-sha1="Aa6XzKXRIYXAOrLEQ4We5BWxc7u" width="690" height="271" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd72e50f18b285135ad21f6c31ad72b63807c738_2_690x271.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd72e50f18b285135ad21f6c31ad72b63807c738_2_1035x406.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd72e50f18b285135ad21f6c31ad72b63807c738.png 2x" data-dominant-color="BAB8B8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1168×460 23.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @mohammed_alshakhas (2025-02-05 16:24 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> any idea whats wrong  ?</p>

---
