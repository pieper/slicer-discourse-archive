---
topic_id: 42032
title: "Aligning A Markup Plane To World Coordinate System With Orth"
date: 2025-03-08
url: https://discourse.slicer.org/t/42032
---

# Aligning a markup plane to world coordinate system, with orthogonal planes

**Topic ID**: 42032
**Date**: 2025-03-08
**URL**: https://discourse.slicer.org/t/aligning-a-markup-plane-to-world-coordinate-system-with-orthogonal-planes/42032

---

## Post #1 by @kat_b (2025-03-08 19:44 UTC)

<p>I am relatively new to 3D Slicer, and haven’t programmed in Python for a while, so please bear with me. In my Slicer environment, I have placed a scapular model (“Model”), and a markup plane (“P”) with associated points “P1”, “P2”, and “P3.”</p>
<p>I have two aims:</p>
<ol>
<li>Align the current markup plane “P” with the existing world coordinate system X and Y axes such that when I navigate to different views in Slicer (e.g. superior or inferior), they are consistent with my markup plane</li>
<li>Create an orthogonal transverse plane that passes through P1 and P2 and is representative of the Z axis</li>
</ol>
<p>Please see the accompanied annotated image to better describe what I am looking to do.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/763c6e87456053f34298cecd9f9bfe1d611cd873.png" data-download-href="/uploads/short-url/gRXOAucNPbGcx9Vz95T6xk4oGY3.png?dl=1" title="AnnotatedScapula" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/763c6e87456053f34298cecd9f9bfe1d611cd873_2_558x500.png" alt="AnnotatedScapula" data-base62-sha1="gRXOAucNPbGcx9Vz95T6xk4oGY3" width="558" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/763c6e87456053f34298cecd9f9bfe1d611cd873_2_558x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/763c6e87456053f34298cecd9f9bfe1d611cd873_2_837x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/763c6e87456053f34298cecd9f9bfe1d611cd873.png 2x" data-dominant-color="AB9DB3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">AnnotatedScapula</span><span class="informations">857×767 99.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have read a number of articles on this forum, and I believe that I’ll need to do some transformations and apply them to both the model and the plane(s), but I am unsure on how to move forward with this from a script perspective. Manual registration is unfortunately not accurate enough for what I am doing.</p>
<p>Thank you in advance for any assistance that anyone is able to provide!</p>

---

## Post #2 by @chir.set (2025-03-08 20:26 UTC)

<p>If i have well understood your requirement, this <a href="https://discourse.slicer.org/t/how-rotate-the-axial-slice-in-script-to-make-it-parallel-with-the-plane-across-3-specified-points/41187/2">reply</a> to a <em>more or less</em> similar question may be helpful. If you <a href="https://gitlab.com/chir-set/RcHacks7/-/tree/900664b75fca04210a065f1324d7fae0214eb559#2-reslice-functions" rel="noopener nofollow ugc">copy and paste</a> the reference codes in your <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#application-startup-file" rel="noopener nofollow ugc">application startup file</a>, you’ll get a nice GUI as a toolbar to perform such reslicing.</p>

---
