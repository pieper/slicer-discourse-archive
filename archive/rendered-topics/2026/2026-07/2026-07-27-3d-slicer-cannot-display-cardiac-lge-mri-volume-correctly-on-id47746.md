---
topic_id: 47746
title: "3D Slicer cannot display cardiac LGE MRI volume correctly – only a single line/slice is shown after DICOM import"
date: 2026-07-27
url: https://discourse.slicer.org/t/47746
last_bumped: 2026-07-27T11:12:33.097Z
---

# 3D Slicer cannot display cardiac LGE MRI volume correctly – only a single line/slice is shown after DICOM import

**Topic ID**: 47746
**Date**: 2026-07-27
**URL**: https://discourse.slicer.org/t/3d-slicer-cannot-display-cardiac-lge-mri-volume-correctly-only-a-single-line-slice-is-shown-after-dicom-import/47746

---

## Post #1 by @yennys (2026-07-27 11:12 UTC)

<p>Hello everyone,</p>
<p>I am using 3D Slicer for cardiac MRI (LGE/PSIR) image analysis. My goal is to perform registration and ROI-based analysis between pre- and post-procedure LGE images.</p>
<p>However, I encountered an issue when importing a cardiac PSIR LGE DICOM series.</p>
<p>After loading the DICOM series, 3D Slicer does not display the complete 3D volume correctly.</p>
<p>The problems are:</p>
<ul>
<li>The sagittal view shows part of the cardiac image;</li>
<li>The axial/coronal views only show a thin line or a single slice;</li>
<li>The 3D view does not display a normal cardiac volume.</li>
</ul>
<p>It seems that the DICOM series may not have been reconstructed correctly as a 3D volume.</p>
<p>My workflow:</p>
<ol>
<li>Imported the DICOM folder using the DICOM module;</li>
<li>Selected the PSIR 15 min LGE series;</li>
<li>Loaded the volume into Slicer.</li>
</ol>
<p>I would like to ask:</p>
<ol>
<li>Does this problem usually indicate that the DICOM series was not recognized correctly as a 3D volume?</li>
<li>Could this be related to incorrect slice ordering, slice spacing, or missing/incorrect Image Position Patient information?</li>
<li>What is the recommended workflow for importing short-axis cardiac PSIR LGE MRI datasets into 3D Slicer?</li>
<li>Are there any specific DICOM settings or plugins required for cardiac MRI reconstruction?</li>
</ol>
<p>I attached a screenshot of the issue.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/0516c8a5141a36be7331d8d89ba6c2d9296b1487.jpeg" data-download-href="/uploads/short-url/J1ctZOxMWkeuDE4KfeKIGrqVsX.jpeg?dl=1" title="402a16c5-efa6-4a3d-9ac0-c8a0f0067249" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/0516c8a5141a36be7331d8d89ba6c2d9296b1487_2_683x500.jpeg" alt="402a16c5-efa6-4a3d-9ac0-c8a0f0067249" data-base62-sha1="J1ctZOxMWkeuDE4KfeKIGrqVsX" width="683" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/0516c8a5141a36be7331d8d89ba6c2d9296b1487_2_683x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/0516c8a5141a36be7331d8d89ba6c2d9296b1487_2_1024x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/0516c8a5141a36be7331d8d89ba6c2d9296b1487_2_1366x1000.jpeg 2x" data-dominant-color="3A3941"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">402a16c5-efa6-4a3d-9ac0-c8a0f0067249</span><span class="informations">1760×1288 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you very much for your help!</p>

---
