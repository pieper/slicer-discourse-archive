---
topic_id: 16805
title: "Export Segmentation In Dicom Rt Format"
date: 2021-03-28
url: https://discourse.slicer.org/t/16805
---

# Export Segmentation in DICOM-RT format

**Topic ID**: 16805
**Date**: 2021-03-28
**URL**: https://discourse.slicer.org/t/export-segmentation-in-dicom-rt-format/16805

---

## Post #1 by @Cody_Xie (2021-03-28 19:00 UTC)

<p>Dear all,</p>
<p>What I would like to do is to export a <strong>clipped region</strong> (from Dynamic Modeler) into a <strong>DICOM-RT</strong> file. I have searched throughout the Forum with no answer. It has bothered me for a long time. Any help from your side will be much appreciated.</p>
<p>Operating system: Windows 10<br>
Slicer version: 4.11.20210226<br>
Expected behavior: Export a <strong>Segmentation</strong> in <strong>DICOM-RT</strong> format<br>
Actual behavior:</p>
<p>My workflow is as follows:</p>
<ol>
<li>Imput a CT data set with some heart Segmentations (in RTSTRUCT format);</li>
<li>“Export visible segments to models”;</li>
<li>Generate a Segmentation (ClippedRegion) by Dynamic Modeler (using curve cut);</li>
<li>“Convert model to segmentation node”;</li>
<li>Right click this segmentation, then click “Export to DICOM…”;</li>
<li>Get the <strong>error message</strong> “Must export the primar anatomical (CT/MR) image” (see the screenshot below).</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbca539ab71316b7e8ccd1db6b7f96bb27676bfa.png" data-download-href="/uploads/short-url/vmm31iI71ErokC5JNTSFCjKpl3Q.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dbca539ab71316b7e8ccd1db6b7f96bb27676bfa_2_690x388.png" alt="2" data-base62-sha1="vmm31iI71ErokC5JNTSFCjKpl3Q" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dbca539ab71316b7e8ccd1db6b7f96bb27676bfa_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dbca539ab71316b7e8ccd1db6b7f96bb27676bfa_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dbca539ab71316b7e8ccd1db6b7f96bb27676bfa_2_1380x776.png 2x" data-dominant-color="D6D5D6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">2560×1440 844 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Could you give me some support?</p>
<p>Thank you so much!</p>

---

## Post #2 by @Cody_Xie (2021-03-28 22:02 UTC)

<p>And it seems that the new Segmentation is not “linked” to the primary CT data set? When I click the CT data set in this Export window, the label of the original segmentation with the CT will turn green. I guess this means the original segmentation is “linked” with the CT. This is maby another problem.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a638895c5e7f62b610cdfd3bea18d53aecec0a1a.png" data-download-href="/uploads/short-url/nIso7O4wiwag6JvB17D3kLrRwgi.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a638895c5e7f62b610cdfd3bea18d53aecec0a1a_2_610x500.png" alt="1" data-base62-sha1="nIso7O4wiwag6JvB17D3kLrRwgi" width="610" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a638895c5e7f62b610cdfd3bea18d53aecec0a1a_2_610x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a638895c5e7f62b610cdfd3bea18d53aecec0a1a_2_915x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a638895c5e7f62b610cdfd3bea18d53aecec0a1a_2_1220x1000.png 2x" data-dominant-color="EFF1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1327×1087 56.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @cpinter (2021-03-29 09:18 UTC)

<p>If I remember correctly, the segmentation needs to be a sibling of the CT under the study, and not under the CT. Please try that and let us know.</p>

---

## Post #4 by @Cody_Xie (2021-04-06 08:24 UTC)

<p>Hi Csaba, I have tried and it works now. Thanks for your support!</p>

---

## Post #5 by @lassoan (2021-04-06 13:12 UTC)

<p>It is great that it works now. <a class="mention" href="/u/cpinter">@cpinter</a> is there a specific reason why the segmentation must be a directly under the study item? Should we make the export mechanism more robust (e.g., do a recursive search from the study level)? If we don’t implement a fix right now then we should at least add an issue to the tracker to remember to work on this later.</p>

---

## Post #6 by @cpinter (2021-04-07 12:37 UTC)

<p>Accepting more valid scenarios would be nice indeed. I added an issue <a href="https://github.com/SlicerRt/SlicerRT/issues/185" class="inline-onebox">More robust item discovery for export · Issue #185 · SlicerRt/SlicerRT · GitHub</a></p>

---
