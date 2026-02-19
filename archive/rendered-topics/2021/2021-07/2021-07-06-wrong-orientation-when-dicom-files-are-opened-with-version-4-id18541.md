---
topic_id: 18541
title: "Wrong Orientation When Dicom Files Are Opened With Version 4"
date: 2021-07-06
url: https://discourse.slicer.org/t/18541
---

# Wrong orientation when DICOM files are opened with version 4.11

**Topic ID**: 18541
**Date**: 2021-07-06
**URL**: https://discourse.slicer.org/t/wrong-orientation-when-dicom-files-are-opened-with-version-4-11/18541

---

## Post #1 by @neginkho (2021-07-06 19:57 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.2/4.11</p>
<p>When I open my DICOM files with the newest version of Slicer (4.11.20200930), the orientation of the images and their coordinates have changed compared to the older version (4.10.2). As you can see in the images below, 2/3 of the views are upside down.</p>
<p>I have checked the Application Settings and they are identical in both versions. The only difference seems to be the Image Origin (see red arrows in the screenshots), but when I change this value to match, it does not solve the problem.</p>
<p>Has anyone had the same issue? how can I fix it? Thank you!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68d9d6f5d9e7148002984df35c1b0d27753a1666.png" data-download-href="/uploads/short-url/eXynkwEun11eHy2zJjqLpiYFt42.png?dl=1" title="410" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68d9d6f5d9e7148002984df35c1b0d27753a1666_2_690x373.png" alt="410" data-base62-sha1="eXynkwEun11eHy2zJjqLpiYFt42" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68d9d6f5d9e7148002984df35c1b0d27753a1666_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68d9d6f5d9e7148002984df35c1b0d27753a1666_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68d9d6f5d9e7148002984df35c1b0d27753a1666_2_1380x746.png 2x" data-dominant-color="6F6E76"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">410</span><span class="informations">1920×1040 235 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3f8e21fb987e5fd7d34140daee4de74e04bbec6.png" data-download-href="/uploads/short-url/rXEkSqRZPZhcj3tt6oemiw1BubY.png?dl=1" title="411" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3f8e21fb987e5fd7d34140daee4de74e04bbec6_2_690x373.png" alt="411" data-base62-sha1="rXEkSqRZPZhcj3tt6oemiw1BubY" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3f8e21fb987e5fd7d34140daee4de74e04bbec6_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3f8e21fb987e5fd7d34140daee4de74e04bbec6_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3f8e21fb987e5fd7d34140daee4de74e04bbec6_2_1380x746.png 2x" data-dominant-color="6E6D75"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">411</span><span class="informations">1920×1040 221 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-07-06 20:06 UTC)

<p>You need to use the DICOM module to load DICOM images.</p>
<p>We’ll soon remove the option of loading DICOM data via “Add data” to avoid potential complications (see <a href="https://github.com/Slicer/Slicer/issues/5726" class="inline-onebox">Disable DICOM import from "Add data" dialog · Issue #5726 · Slicer/Slicer · GitHub</a>).</p>

---
