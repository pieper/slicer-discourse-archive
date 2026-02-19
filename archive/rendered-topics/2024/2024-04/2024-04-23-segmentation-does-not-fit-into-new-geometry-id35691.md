---
topic_id: 35691
title: "Segmentation Does Not Fit Into New Geometry"
date: 2024-04-23
url: https://discourse.slicer.org/t/35691
---

# Segmentation does not fit into new geometry

**Topic ID**: 35691
**Date**: 2024-04-23
**URL**: https://discourse.slicer.org/t/segmentation-does-not-fit-into-new-geometry/35691

---

## Post #1 by @SHMMU (2024-04-23 17:54 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/220fa9b040d88bed1903ac0cfbb189f94143b86a.jpeg" data-download-href="/uploads/short-url/4RjN4tALYZeKzeIuOfhOG1zUDVM.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/220fa9b040d88bed1903ac0cfbb189f94143b86a_2_375x500.jpeg" alt="image" data-base62-sha1="4RjN4tALYZeKzeIuOfhOG1zUDVM" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/220fa9b040d88bed1903ac0cfbb189f94143b86a_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/220fa9b040d88bed1903ac0cfbb189f94143b86a_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/220fa9b040d88bed1903ac0cfbb189f94143b86a_2_750x1000.jpeg 2x" data-dominant-color="5C5851"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1440×1920 190 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have used total segmentator to aquire liver volume. However, when I go to export the file as NIFTI I get this error message, “the current segmentation does not completely fit into the new geometry. Do you want to crop the segmentation”. I do not want to crop the area as I need the entire segmentation.  Any help would be greatly appreciated.</p>

---

## Post #2 by @muratmaga (2024-04-23 23:11 UTC)

<p>Segmentation geometry should have a “pad” option. Make sure it is checked and then rertry.</p>

---

## Post #3 by @dvijay (2025-11-26 23:29 UTC)

<p>Can you elaborate what is meant by ‘pad’ options here? I am facing the same issue but unable to find any such option.</p>

---

## Post #4 by @muratmaga (2025-11-27 00:01 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd40c8dd5316ed11e75352247e8aa59b719534bc.jpeg" data-download-href="/uploads/short-url/thKGh5EOxwiBEtVP0xW9eWU3RQE.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd40c8dd5316ed11e75352247e8aa59b719534bc_2_690x324.jpeg" alt="image" data-base62-sha1="thKGh5EOxwiBEtVP0xW9eWU3RQE" width="690" height="324" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd40c8dd5316ed11e75352247e8aa59b719534bc_2_690x324.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd40c8dd5316ed11e75352247e8aa59b719534bc_2_1035x486.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd40c8dd5316ed11e75352247e8aa59b719534bc.jpeg 2x" data-dominant-color="C9CAD7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1222×574 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @dvijay (2025-12-04 22:05 UTC)

<p>Thanks for the quick response! I’ll try this out. One more small q., how did you get that dialog box?</p>

---

## Post #6 by @muratmaga (2025-12-04 22:31 UTC)

<p>It is the cube icon above the green arrow.</p>

---
