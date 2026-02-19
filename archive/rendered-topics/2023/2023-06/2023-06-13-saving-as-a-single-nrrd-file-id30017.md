---
topic_id: 30017
title: "Saving As A Single Nrrd File"
date: 2023-06-13
url: https://discourse.slicer.org/t/30017
---

# Saving as a single NRRD File

**Topic ID**: 30017
**Date**: 2023-06-13
**URL**: https://discourse.slicer.org/t/saving-as-a-single-nrrd-file/30017

---

## Post #1 by @SuperArmySoldiers (2023-06-13 17:19 UTC)

<p>Hey,</p>
<p>I am new medical files etc. I am trying to convert my CT scan into an nrrd file to eventually 3D print.<br>
In the Slicer I am struggling to save the DICOM data to a single nrrd file.</p>
<p>You can see on the attached image that its not saving as a single nrrd file.</p>
<p>Any help would be greatly apricated!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8e5fc7dbdedef37983a683c11b7b6d9bd9e0d9f.png" data-download-href="/uploads/short-url/xejw1rO78deA1ZsHoCgkuoHY0Gz.png?dl=1" title="SlicerApp-real_2023-06-13_15-02-32" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8e5fc7dbdedef37983a683c11b7b6d9bd9e0d9f_2_690x444.png" alt="SlicerApp-real_2023-06-13_15-02-32" data-base62-sha1="xejw1rO78deA1ZsHoCgkuoHY0Gz" width="690" height="444" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8e5fc7dbdedef37983a683c11b7b6d9bd9e0d9f_2_690x444.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8e5fc7dbdedef37983a683c11b7b6d9bd9e0d9f_2_1035x666.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8e5fc7dbdedef37983a683c11b7b6d9bd9e0d9f.png 2x" data-dominant-color="4C4E57"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerApp-real_2023-06-13_15-02-32</span><span class="informations">1343×866 203 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-06-13 17:22 UTC)

<p>It seems that the DICOM series is corrupted. Most likely the issue is that different series instance UID was set for each frame. It may be due to incorrect anonymization or incorrectly implemented DICOM export. You may be able to fix it using the <code>DICOM Patcher</code> module in the <code>Force same series instance UID in each directory</code> option.</p>

---
