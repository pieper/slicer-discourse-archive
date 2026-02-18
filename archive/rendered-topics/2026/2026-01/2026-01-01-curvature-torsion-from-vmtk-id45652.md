# Curvature, torsion from VMTK

**Topic ID**: 45652
**Date**: 2026-01-01
**URL**: https://discourse.slicer.org/t/curvature-torsion-from-vmtk/45652

---

## Post #1 by @kuoi (2026-01-01 17:24 UTC)

<p>Hello, I am using the Extract Centerline module. I obtained one centerline and one table containing a single line with a pair of curvature and torsion values.</p>
<p>I noticed that curvature and torsion are reported in the exported table called “centerline quantification”. I assume these values are averages. As stated in the <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/Docs/ExtractCenterline.md" rel="noopener nofollow ugc">document</a>: “Geometrical properties (length, average radius, curvature, torsion, tortuosity)”. However, I also noticed that the <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/283a8520ae2669f1a25766dd00a3e4f4e907a5c0/ExtractCenterline/ExtractCenterline.py#L880" rel="noopener nofollow ugc">code comment</a> does not explicitly mention that these values are averages. Therefore, I am not sure whether my understanding is correct.</p>
<p>If these values are averages, could you advise on whether there are any approaches to estimate a fixed curvature and a fixed torsion value that best fit the currently extracted centerline?</p>
<p>I am considering using a sum of squared errors approach and fitting the parameters via the Python console to obtain these two values. Would this be a reasonable strategy?</p>
<p>Thanks a lot.</p>

---
