---
topic_id: 15981
title: "How Can I Make A Plane From 3 Midsagittal Fiducials"
date: 2021-02-13
url: https://discourse.slicer.org/t/15981
---

# How can I make a plane from 3 midsagittal fiducials?

**Topic ID**: 15981
**Date**: 2021-02-13
**URL**: https://discourse.slicer.org/t/how-can-i-make-a-plane-from-3-midsagittal-fiducials/15981

---

## Post #1 by @ebryson (2021-02-13 20:56 UTC)

<p>Hi,</p>
<p>I’m trying to place fiducials and open curves on a juvenile skull’s fontanelle (the unfused place where there’s no bone), so it’s landmarking an open/negative space not on the actual model. To do that I want to create a mid-sagittal slice that’s based on 3 fiducials that I make along the midline of the skull.</p>
<p>So I’m wondering: How do I make a slice/cut-plane based on my own fiducials?</p>
<p>Does anyone know how to do that?<br>
Thanks!</p>

---

## Post #2 by @muratmaga (2021-02-13 21:04 UTC)

<p>Create a blank MarkupsPlane node and copy and paste those three points from the MarkupFiducial into the Plane one (right click on the Control Points table)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a4e4a7e6a2b3cc5fe35f5ca4efe6a7debacb281.png" data-download-href="/uploads/short-url/hrXZjZ9Db9DrLHhrOeMP2iWrICl.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a4e4a7e6a2b3cc5fe35f5ca4efe6a7debacb281_2_325x500.png" alt="image" data-base62-sha1="hrXZjZ9Db9DrLHhrOeMP2iWrICl" width="325" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a4e4a7e6a2b3cc5fe35f5ca4efe6a7debacb281_2_325x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a4e4a7e6a2b3cc5fe35f5ca4efe6a7debacb281_2_487x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a4e4a7e6a2b3cc5fe35f5ca4efe6a7debacb281.png 2x" data-dominant-color="3A3F48"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">597×916 45.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @lassoan (2021-02-13 21:09 UTC)

<p>You might also find ACPC Transform module useful, which can reorient an image to make the midsagittal plane exactly aligned with the sagittal view.</p>
<p>Short demo/tutorial video:</p>
<aside class="quote quote-modified" data-post="5" data-topic="15762">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/acpc-transform-for-mri-scans-slicer-4-11/15762/5">ACPC Transform for MRI scans- Slicer 4.11</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I did a quick recording of how ACPC alignment works in latest Slicer Preview Release: 

  <a href="https://www.youtube.com/watch?v=sdrRv3JrgTU" target="_blank" rel="noopener">
    [acpcdemo]
  </a>


It would be great if you could create a nice description/tutorial of how to use it (with a few screenshots). Slicer documentation is now in markdown format, which is the format that this forum uses, so you can write this as a new post in this topic and I will move it to the Slicer documentation when it is ready.
  </blockquote>
</aside>

<p>Documentation:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/ACPCTransform" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/ACPCTransform</a></p>

---

## Post #4 by @ebryson (2021-02-15 02:29 UTC)

<p>Thank you so much for the quick reply, I’m checking with my supervisor to see if this is what she had in mind but it looked good when I tried it out.</p>
<p>Another quick question, on my adult skulls I resample my open-curves landmarks to the model surface so they’re evenly spaced. Since I’m moving points into the open space over the fontanelle to measure that curve I can’t resample (because they want to jump to the bone surface). Because they won’t be evenly spaced will that mess up my final comparison between adults and juveniles?</p>
<p>Thank you!</p>

---

## Post #5 by @lassoan (2021-02-15 03:03 UTC)

<p>You can resample without snapping to surface.</p>
<p>If you compare curves (not control point positions) then it might not matter if control points are spaced equally.</p>
<p>I don’t know if it helps you, but in recent Slicer Preview Release you can choose not to snap points to visible surface when you are moving control points in a 3D view (initial placement is still done on the surface, but you can simply skip the fontanelle and then later insert points along the curve using Ctrl + Left-click).</p>

---

## Post #6 by @ebryson (2021-02-15 14:51 UTC)

<p>I forgot you could do that, thank you!</p>
<p>And I didn’t know about the shortcut for adding points that’s going to be really helpful.</p>

---
