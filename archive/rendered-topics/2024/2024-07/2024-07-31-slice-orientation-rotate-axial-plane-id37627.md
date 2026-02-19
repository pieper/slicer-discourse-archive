---
topic_id: 37627
title: "Slice Orientation Rotate Axial Plane"
date: 2024-07-31
url: https://discourse.slicer.org/t/37627
---

# Slice orientation Rotate Axial plane

**Topic ID**: 37627
**Date**: 2024-07-31
**URL**: https://discourse.slicer.org/t/slice-orientation-rotate-axial-plane/37627

---

## Post #1 by @Seokjun_Hwang (2024-07-31 00:34 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92e00766c4706ab816077a0862d218a351183d22.png" data-download-href="/uploads/short-url/kXjGNXmqaECdKP55TUfpS7YYTWW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92e00766c4706ab816077a0862d218a351183d22_2_606x500.png" alt="image" data-base62-sha1="kXjGNXmqaECdKP55TUfpS7YYTWW" width="606" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92e00766c4706ab816077a0862d218a351183d22_2_606x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92e00766c4706ab816077a0862d218a351183d22.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92e00766c4706ab816077a0862d218a351183d22.png 2x" data-dominant-color="62617F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">903×745 39.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49faa891c8b268a030f03db4af5401ceaafd563d.png" alt="image" data-base62-sha1="ayrT5XBuAwAofngeJJKC5uDmN0V" width="483" height="452"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a9ba027b0d4dee02cef162552da40c2df501be1.png" data-download-href="/uploads/short-url/1vQcsKjJvx7yNEBL3BPxRWfWeFr.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a9ba027b0d4dee02cef162552da40c2df501be1_2_690x498.png" alt="image" data-base62-sha1="1vQcsKjJvx7yNEBL3BPxRWfWeFr" width="690" height="498" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a9ba027b0d4dee02cef162552da40c2df501be1_2_690x498.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a9ba027b0d4dee02cef162552da40c2df501be1_2_1035x747.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a9ba027b0d4dee02cef162552da40c2df501be1.png 2x" data-dominant-color="39393E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1036×749 39.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I want to adjust the angle of the axial black cross-sectional plane to match the red plane as shown in the picture. This is the valve area of the aorta, and I am looking for a module or Python function that can automatically align the plane passing through the three specific points (F series). Ultimately, I want to automatically capture the cross-sectional view by aligning the plane passing through these three points.</p>

---

## Post #2 by @chir.set (2024-07-31 06:37 UTC)

<aside class="quote no-group" data-username="Seokjun_Hwang" data-post="1" data-topic="37627">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/seokjun_hwang/48/76745_2.png" class="avatar"> Seokjun_Hwang:</div>
<blockquote>
<p>or Python function</p>
</blockquote>
</aside>
<p>You may get some insight from <a href="https://gitlab.com/chir-set/RcHacks7/-/blob/master/00-Lib.py.txt?ref_type=heads#L125" rel="noopener nofollow ugc">here</a> and <a href="https://gitlab.com/chir-set/RcHacks7/-/blob/master/12-ResliceToAxis.py.txt?ref_type=heads#L64" rel="noopener nofollow ugc">here</a>. You may adapt your code accordingly, or simply install the <a href="https://gitlab.com/chir-set/RcHacks7#2-reslice-functions" rel="noopener nofollow ugc">reslice functions</a> of the project.</p>

---
