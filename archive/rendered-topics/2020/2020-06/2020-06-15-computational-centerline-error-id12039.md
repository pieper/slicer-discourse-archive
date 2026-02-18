# Computational Centerline Error

**Topic ID**: 12039
**Date**: 2020-06-15
**URL**: https://discourse.slicer.org/t/computational-centerline-error/12039

---

## Post #1 by @Madelene_Habib (2020-06-15 17:57 UTC)

<p>Hello,<br>
I’m running into this issue when I press “preview” in the SlicerVMTK Centerline Computation module.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f7524ff802905c1c5ba6ed7b1b362aee15d0c63.png" data-download-href="/uploads/short-url/93n3OSp4pHSbDvVu6fY804vvyqn.png?dl=1" title="Capture2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f7524ff802905c1c5ba6ed7b1b362aee15d0c63_2_690x282.png" alt="Capture2" data-base62-sha1="93n3OSp4pHSbDvVu6fY804vvyqn" width="690" height="282" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f7524ff802905c1c5ba6ed7b1b362aee15d0c63_2_690x282.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f7524ff802905c1c5ba6ed7b1b362aee15d0c63_2_1035x423.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f7524ff802905c1c5ba6ed7b1b362aee15d0c63_2_1380x564.png 2x" data-dominant-color="CDCEE5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture2</span><span class="informations">1882×771 62.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Fluvio_Lobo (2020-06-18 16:15 UTC)

<p>I am having the same issue.<br>
Weirdly enough, it is only happening in one of my two Win machines.<br>
I have tried re-installing everything multiple times with no success.</p>
<p>Has this issue been resolved?</p>

---

## Post #3 by @lassoan (2020-06-18 16:16 UTC)

<p>Do you use the exact same Slicer version on your two computers?</p>

---

## Post #4 by @Fluvio_Lobo (2020-06-18 16:17 UTC)

<p>I am running 4.10.2 r28257 on both</p>

---

## Post #5 by @lassoan (2020-06-18 16:20 UTC)

<p>Could you compare the content of <code>c:\Users\(yourusername)\AppData\Roaming\NA-MIC\Extensions-28257\SlicerVMTK</code> folders (and all subfolders)? Do you have the exact same files on the two computers?</p>

---

## Post #6 by @Fluvio_Lobo (2020-06-18 16:20 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>Thank you!<br>
Without inspecting too much, I just copied all of the directories and files from the working extension to the faulty one. I was just able to calculate a center-line on my model. <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=9" title=":grinning:" class="emoji" alt=":grinning:"></p>

---

## Post #7 by @lassoan (2020-06-20 21:39 UTC)

<p>Hi all, check out the new, completely reworked centerline extraction module in SlicerVMTK:</p>
<aside class="quote quote-modified" data-post="1" data-topic="12117">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-module-extract-centerline-in-slicervmtk-extension/12117">New module: Extract Centerline (in SlicerVMTK extension)</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    We added a completely new module that makes vessel (or airway or any other tree structure) centerline extraction much faster, flexible, and robust. It can quickly extract a network, determine branch endpoints automatically, allows editing of endpoints, computing centerlines, branches, and quantitative metrics (radius, curvature, torsion, etc). The new “Extract Centerline” module is available in SlicerVMTK extension for latest Slicer-4.11 release (it replaces the old “Centerline Computation” modu…
  </blockquote>
</aside>


---
