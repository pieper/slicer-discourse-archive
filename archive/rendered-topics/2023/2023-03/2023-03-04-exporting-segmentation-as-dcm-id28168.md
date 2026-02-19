---
topic_id: 28168
title: "Exporting Segmentation As Dcm"
date: 2023-03-04
url: https://discourse.slicer.org/t/28168
---

# Exporting segmentation as dcm

**Topic ID**: 28168
**Date**: 2023-03-04
**URL**: https://discourse.slicer.org/t/exporting-segmentation-as-dcm/28168

---

## Post #1 by @Nadya_Shusharina (2023-03-04 16:19 UTC)

<p>Operating system: Windows 11 PRO<br>
Slicer version: 5.2.1<br>
Expected behavior: Export created segmentation to the DICOM database<br>
Actual behavior: No export</p>
<p>Hello,</p>
<p>I am creating segmentation in Segment Editor and exporting it to the DICOM database as dcm. When Slicer RT module was installed, the segmentation was recognized as RTSTRUCT and the export failed. After I uninstalled Slicer RT the segmentation was exported as expected. Am I missing something?</p>
<p>Thank you,<br>
Nadya</p>

---

## Post #2 by @lassoan (2023-03-06 05:28 UTC)

<p>SlicerRT provides plugin for exporting segmentation as DICOM RT structure set, so uninstalling it should make the RTSTRUCT export option disappear.</p>
<p>Have you installed some locally built SlicerRT?</p>
<p>How did you do your export DICOM RT structure set? How did it fail?</p>

---

## Post #3 by @Nadya_Shusharina (2023-03-06 19:48 UTC)

<p>SlicerRT was installed from the Extension Manager.<br>
Attached are snapshots of the Export to DICOM module with and without SlicerRT installed.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8af635a1ab279c80f416cbb6bc7d85e8f7639770.png" data-download-href="/uploads/short-url/jPjok9l1yOZvlk0Cl01DUXjpToY.png?dl=1" title="noslicerrt" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8af635a1ab279c80f416cbb6bc7d85e8f7639770_2_690x325.png" alt="noslicerrt" data-base62-sha1="jPjok9l1yOZvlk0Cl01DUXjpToY" width="690" height="325" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8af635a1ab279c80f416cbb6bc7d85e8f7639770_2_690x325.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8af635a1ab279c80f416cbb6bc7d85e8f7639770_2_1035x487.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8af635a1ab279c80f416cbb6bc7d85e8f7639770.png 2x" data-dominant-color="F1F3F2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">noslicerrt</span><span class="informations">1320×623 63.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/7771bda544859cce15a203daaee0097eeafc57e7.png" data-download-href="/uploads/short-url/h2EvsWCGiibE9ov46vP9wuup3Fl.png?dl=1" title="slicerrt" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/7771bda544859cce15a203daaee0097eeafc57e7_2_690x327.png" alt="slicerrt" data-base62-sha1="h2EvsWCGiibE9ov46vP9wuup3Fl" width="690" height="327" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/7771bda544859cce15a203daaee0097eeafc57e7_2_690x327.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/7771bda544859cce15a203daaee0097eeafc57e7_2_1035x490.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/7771bda544859cce15a203daaee0097eeafc57e7.png 2x" data-dominant-color="F3F5F3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicerrt</span><span class="informations">1313×624 41.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @Sunderlandkyl (2023-03-06 20:39 UTC)

<p>You need to export the study to DICOM that contains both the anatomical image and the segmentation, rather than just the segmentation.</p>

---

## Post #5 by @Nadya_Shusharina (2023-03-06 20:49 UTC)

<p>I believe this is what I am doing. The problem is there is no SEG object in the list.</p>

---

## Post #6 by @lassoan (2023-03-06 21:06 UTC)

<p>Do you want to save the segmentation as SEG or RTSTRUCT?</p>

---

## Post #7 by @Nadya_Shusharina (2023-03-06 21:16 UTC)

<p>I am just testing now. Would be good to have an option of either SEG or RTSTRUCT.</p>

---

## Post #8 by @Sunderlandkyl (2023-03-07 20:45 UTC)

<p>I discovered why both plugins were not being displayed. Should be fixed by this PR: <a href="https://github.com/Slicer/Slicer/pull/6863" class="inline-onebox" rel="noopener nofollow ugc">BUG: Allow multiple DICOM plugins for export with same mean confidence by Sunderlandkyl · Pull Request #6863 · Slicer/Slicer · GitHub</a>.</p>

---
