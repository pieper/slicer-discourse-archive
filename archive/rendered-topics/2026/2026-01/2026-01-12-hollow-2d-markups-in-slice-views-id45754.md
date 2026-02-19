---
topic_id: 45754
title: "Hollow 2D Markups In Slice Views"
date: 2026-01-12
url: https://discourse.slicer.org/t/45754
---

# Hollow 2d markups in slice views

**Topic ID**: 45754
**Date**: 2026-01-12
**URL**: https://discourse.slicer.org/t/hollow-2d-markups-in-slice-views/45754

---

## Post #1 by @TomOssability (2026-01-12 16:40 UTC)

<p>Hi, I understand support for 2D operations is limited due to this platform being mostly used for 3D tasks. However, I am developing a python extension that requires key point placement in single slice views, for which I would prefer the markup control point glyphs show as rings. I have a couple of questions:</p>
<ul>
<li>Has anyone had any success with showing markups in slice view without fill (circle2D, Square2D)</li>
<li>If this is not possible, can anyone recommend an approach to developing a custom markup to serve this purpose?</li>
</ul>
<p>Thanks,<br>
I would appreciate any help or similar experiences anyone can offer</p>

---

## Post #2 by @lassoan (2026-01-12 16:50 UTC)

<p>Currently, control point glyph filling is not controllable independently because filling it is used as a hint when fiducial projection is enabled (filling indicates if the point is in front of or behind the current slice).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6afb9d0800529ac6a1db9a183452c5bd51fee31b.jpeg" data-download-href="/uploads/short-url/fgpGQA0XLvrkHRS1nr0PHcTtRx1.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6afb9d0800529ac6a1db9a183452c5bd51fee31b_2_591x500.jpeg" alt="image" data-base62-sha1="fgpGQA0XLvrkHRS1nr0PHcTtRx1" width="591" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6afb9d0800529ac6a1db9a183452c5bd51fee31b_2_591x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6afb9d0800529ac6a1db9a183452c5bd51fee31b.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6afb9d0800529ac6a1db9a183452c5bd51fee31b.jpeg 2x" data-dominant-color="4C4C4D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">662×560 54.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can use Cross2D, StarBurst2D, CrossDot2D glyphs that do not occlude the center.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/407a74bca54412a81477a01df311d9a89d0826a8.jpeg" data-download-href="/uploads/short-url/9coUYcjY5xehHSIbeGiZz2Up6Zi.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/407a74bca54412a81477a01df311d9a89d0826a8_2_591x500.jpeg" alt="image" data-base62-sha1="9coUYcjY5xehHSIbeGiZz2Up6Zi" width="591" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/407a74bca54412a81477a01df311d9a89d0826a8_2_591x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/407a74bca54412a81477a01df311d9a89d0826a8.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/407a74bca54412a81477a01df311d9a89d0826a8.jpeg 2x" data-dominant-color="4C4C4C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">662×560 55.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @TomOssability (2026-01-13 00:28 UTC)

<p>Thanks for your quick reply. I have added a switcher in my module to toggle between CrossDot2D and “circle” glyphs, which I am showing by programatically shifting the control points behind the slice view and showing their projections in slice view with ‘outline behind slice pane’ enabled (Using the Circle2D glyph type).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aaa72e6edddac059b6dea59ff336cb6583d67c71.jpeg" data-download-href="/uploads/short-url/olFlYqqNzXFMZxctTWP9vsxdmYF.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aaa72e6edddac059b6dea59ff336cb6583d67c71_2_545x500.jpeg" alt="image" data-base62-sha1="olFlYqqNzXFMZxctTWP9vsxdmYF" width="545" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aaa72e6edddac059b6dea59ff336cb6583d67c71_2_545x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aaa72e6edddac059b6dea59ff336cb6583d67c71.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aaa72e6edddac059b6dea59ff336cb6583d67c71.jpeg 2x" data-dominant-color="494949"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">700×642 42.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/902b6ac5a78efdc0258bc27f6fd5b288b9f0adfc.jpeg" data-download-href="/uploads/short-url/kznM8vm0xR3v5UfMmx2NZjIduEs.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/902b6ac5a78efdc0258bc27f6fd5b288b9f0adfc_2_545x500.jpeg" alt="image" data-base62-sha1="kznM8vm0xR3v5UfMmx2NZjIduEs" width="545" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/902b6ac5a78efdc0258bc27f6fd5b288b9f0adfc_2_545x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/902b6ac5a78efdc0258bc27f6fd5b288b9f0adfc.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/902b6ac5a78efdc0258bc27f6fd5b288b9f0adfc.jpeg 2x" data-dominant-color="494949"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">700×642 42.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>While this brings a new challenge when moving to 3d space and forces a fill on the circles while dragging them, it is sufficient for my requirement.</p>
<p>Thanks for your assistance and eager support for those using your software <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=15" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
Cheers.</p>

---
