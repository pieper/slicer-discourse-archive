# Export Segmentation in DICOM-RT format in ver 5.6.1

**Topic ID**: 35595
**Date**: 2024-04-18
**URL**: https://discourse.slicer.org/t/export-segmentation-in-dicom-rt-format-in-ver-5-6-1/35595

---

## Post #1 by @MASAMA (2024-04-18 11:36 UTC)

<p>Dear everyone,</p>
<p>What I would like to do is export the DICOM CT data using MONAI with segmented regions to her DICOM-RT file. I tried the answer with # <a href="https://discourse.slicer.org/t/export-segmentation-in-dicom-rt-format/16805">Export Segmentation in DICOM-RT format</a> before. However, I received the same error message “Must export the primary anatomical (CT/MR) image” as shown in the figure. .</p>
<p>Operating system: Windows 10<br>
Slicer version: 5.6.1<br>
Expected behavior: Export segmentation in DICOM-RT format<br>
Actual operation:</p>
<p>My workflow is as follows.</p>
<p>・ Enter the CT data set.<br>
・Perform segmentation using extended MONAI.<br>
・Right-click study and select Export to dicom.<br>
・Select RT in select export type and execute export.</p>
<p>However, the error shown in the figure occurs.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/846685dc49648511853153f35b2eb4f19f82dc84.png" data-download-href="/uploads/short-url/iTgGborSVRUWUSd8YsntyXn8Gt6.png?dl=1" title="3dslicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/846685dc49648511853153f35b2eb4f19f82dc84_2_475x500.png" alt="3dslicer" data-base62-sha1="iTgGborSVRUWUSd8YsntyXn8Gt6" width="475" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/846685dc49648511853153f35b2eb4f19f82dc84_2_475x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/846685dc49648511853153f35b2eb4f19f82dc84_2_712x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/846685dc49648511853153f35b2eb4f19f82dc84_2_950x1000.png 2x" data-dominant-color="CBCAD0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3dslicer</span><span class="informations">1043×1097 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As answered in # <a href="https://discourse.slicer.org/t/export-segmentation-in-dicom-rt-format/16805">Export Segmentation in DICOM-RT format</a> , segmentation is not placed under the CT, but at the same level as the CT under investigation.<br>
I also have SlicerRT and Quantitative reporting installed.</p>
<p>Could you give me some support?</p>
<p>Thank you so much!</p>

---

## Post #2 by @cpinter (2024-04-22 13:50 UTC)

<p>There is no CT in the whole scene, there is only a dose volume (the cube is colored vs all gray). Have you accidentally converted the CT to dose? We don’t have a UI option to convert a dose back to CT, so please load the volume again as CT and try exporting again.</p>

---
