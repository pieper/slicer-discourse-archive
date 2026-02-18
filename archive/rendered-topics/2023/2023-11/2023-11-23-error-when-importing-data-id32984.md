# Error when importing data

**Topic ID**: 32984
**Date**: 2023-11-23
**URL**: https://discourse.slicer.org/t/error-when-importing-data/32984

---

## Post #1 by @Lilyana (2023-11-23 17:45 UTC)

<p>why does my screen look like this when I import data? because my previous file was IMA type and I wanted to change it to DICOM type</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d4d8426a445f96bb188ed1fcead6f654ef60e50.png" data-download-href="/uploads/short-url/b1QQgidOTsID0kVMnkfSB117iW4.png?dl=1" title="Screenshot (1617)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d4d8426a445f96bb188ed1fcead6f654ef60e50_2_690x388.png" alt="Screenshot (1617)" data-base62-sha1="b1QQgidOTsID0kVMnkfSB117iW4" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d4d8426a445f96bb188ed1fcead6f654ef60e50_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d4d8426a445f96bb188ed1fcead6f654ef60e50_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d4d8426a445f96bb188ed1fcead6f654ef60e50_2_1380x776.png 2x" data-dominant-color="A3A2A5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (1617)</span><span class="informations">1920×1080 389 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-11-23 21:06 UTC)

<p>Your <code>.IMA</code> files are probably already DICOM files. DICOM standard does not specify what file extension should be used for saved files, so applications can arbitrarily choose anything.</p>
<p>If you load a single volume and it gets loaded into the scene as multiple single-slice volumes then most likely the image is not correctly anonymized or corrupted by some other processing. We can confirm if you share the file (upload somewhere and post the link here; make sure no patient information is included in the files).</p>

---
