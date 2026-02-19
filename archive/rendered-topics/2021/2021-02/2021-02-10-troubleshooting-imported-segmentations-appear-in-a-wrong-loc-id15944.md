---
topic_id: 15944
title: "Troubleshooting Imported Segmentations Appear In A Wrong Loc"
date: 2021-02-10
url: https://discourse.slicer.org/t/15944
---

# Troubleshooting: Imported segmentations appear in a wrong location

**Topic ID**: 15944
**Date**: 2021-02-10
**URL**: https://discourse.slicer.org/t/troubleshooting-imported-segmentations-appear-in-a-wrong-location/15944

---

## Post #1 by @rumugam (2021-02-10 23:02 UTC)

<p>Dear 3D Slicer Community,</p>
<p>I am currently facing problems with my segmentations. After exporting them as a Labelmap (-label) and reimporting they appear a few slices lower than expected (comparison of original and reimport as images attached)</p>
<p>Has anyone faced the same problem? Many thanks in advance for your help.</p>
<p>Best,<br>
Arumugam</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b197aa8fbda41efd445ea538c9f8694a7d1fa872.jpeg" data-download-href="/uploads/short-url/pl3sfNLXdcYQDNTgnexn82KX6RY.jpeg?dl=1" title="Bild von iOS-2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b197aa8fbda41efd445ea538c9f8694a7d1fa872_2_375x500.jpeg" alt="Bild von iOS-2" data-base62-sha1="pl3sfNLXdcYQDNTgnexn82KX6RY" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b197aa8fbda41efd445ea538c9f8694a7d1fa872_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b197aa8fbda41efd445ea538c9f8694a7d1fa872_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b197aa8fbda41efd445ea538c9f8694a7d1fa872_2_750x1000.jpeg 2x" data-dominant-color="5E5350"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bild von iOS-2</span><span class="informations">3024×4032 676 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a9f5a97d521b6f53084056152fe243263f52c8c.jpeg" data-download-href="/uploads/short-url/8mB6EPUgdWtfyExCCTR0o97aDko.jpeg?dl=1" title="Bild von iOS" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a9f5a97d521b6f53084056152fe243263f52c8c_2_375x500.jpeg" alt="Bild von iOS" data-base62-sha1="8mB6EPUgdWtfyExCCTR0o97aDko" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a9f5a97d521b6f53084056152fe243263f52c8c_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a9f5a97d521b6f53084056152fe243263f52c8c_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a9f5a97d521b6f53084056152fe243263f52c8c_2_750x1000.jpeg 2x" data-dominant-color="5F5757"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bild von iOS</span><span class="informations">3024×4032 722 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-02-11 00:01 UTC)

<p>It seems that you have highly anisotropic volume (large space between slices) and the volume axes are not aligned with default slice view axes (because before recent Slicer-4.13 versions, by default slice view axes were aligned to anatomical axes and not to the volume axes).</p>
<p>You can either hit <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">“Rotate to volume plane”</a> button in the slice view controller or use latest Slicer Preview Release (because that aligns slice views with volume axes by default).</p>

---
