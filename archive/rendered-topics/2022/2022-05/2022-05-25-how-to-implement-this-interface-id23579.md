---
topic_id: 23579
title: "How To Implement This Interface"
date: 2022-05-25
url: https://discourse.slicer.org/t/23579
---

# How to implement this interface

**Topic ID**: 23579
**Date**: 2022-05-25
**URL**: https://discourse.slicer.org/t/how-to-implement-this-interface/23579

---

## Post #1 by @wanghao1 (2022-05-25 01:55 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93b33072ad293523d6bcd56f42fa0dc6e27132e4.jpeg" data-download-href="/uploads/short-url/l4C69UDVO8Ebze4OuSbj2jwBGjG.jpeg?dl=1" title="Snipaste_2022-05-25_09-51-06" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/93b33072ad293523d6bcd56f42fa0dc6e27132e4_2_690x327.jpeg" alt="Snipaste_2022-05-25_09-51-06" data-base62-sha1="l4C69UDVO8Ebze4OuSbj2jwBGjG" width="690" height="327" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/93b33072ad293523d6bcd56f42fa0dc6e27132e4_2_690x327.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93b33072ad293523d6bcd56f42fa0dc6e27132e4.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93b33072ad293523d6bcd56f42fa0dc6e27132e4.jpeg 2x" data-dominant-color="18181A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snipaste_2022-05-25_09-51-06</span><span class="informations">991×470 42.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I saw this example on the Plus website.This is a simple test application to visualize all the tracker tools and the numerical values of the acquired transforms. The visualized data can be optionally saved into file.Is the source code available?Thank you very much!</p>

---

## Post #2 by @ungi (2022-05-25 21:49 UTC)

<p>You can create model nodes in Slicer and transform them using the transform nodes coming from PLUS. That will visualize the coordinate systems in 3D. There is a Create Models module in the SlicerIGT extension.<br>
The values of the transformation matrix can be viewed in the Transforms module.<br>
Time sequences can be recorded in the Sequences module of Slicer. Sequences are saved and reloaded with Slicer scenes.</p>

---

## Post #3 by @wanghao1 (2022-05-30 07:03 UTC)

<p>Thank you very much!</p>

---
