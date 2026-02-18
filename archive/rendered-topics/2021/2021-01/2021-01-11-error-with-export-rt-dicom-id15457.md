# Error with export rt dicom

**Topic ID**: 15457
**Date**: 2021-01-11
**URL**: https://discourse.slicer.org/t/error-with-export-rt-dicom/15457

---

## Post #1 by @jeongsu (2021-01-11 15:37 UTC)

<p>hi, i`m js<br>
I want to get dicom files with my rt segmentation,<br>
data - Dicom export<br>
I did this procedure, but I got cracked files.<br>
How can I get solution about this error?<br>
please help me…<br>
thank you.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82c3fcd19319b26b797956c456bf82f4fb890a23.jpeg" data-download-href="/uploads/short-url/iENYiF0WDXx2ZYOFStkAiWa5dGb.jpeg?dl=1" title="KakaoTalk_20210111_233940503" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/82c3fcd19319b26b797956c456bf82f4fb890a23_2_379x500.jpeg" alt="KakaoTalk_20210111_233940503" data-base62-sha1="iENYiF0WDXx2ZYOFStkAiWa5dGb" width="379" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/82c3fcd19319b26b797956c456bf82f4fb890a23_2_379x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/82c3fcd19319b26b797956c456bf82f4fb890a23_2_568x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82c3fcd19319b26b797956c456bf82f4fb890a23.jpeg 2x" data-dominant-color="524A51"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">KakaoTalk_20210111_233940503</span><span class="informations">668×879 160 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5d2c1975f5fb1f57d25165edda6033852f68153.jpeg" data-download-href="/uploads/short-url/se1BuO68CLZMPtLidDCvyUxUqQ3.jpeg?dl=1" title="KakaoTalk_20210111_232749527" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c5d2c1975f5fb1f57d25165edda6033852f68153_2_358x500.jpeg" alt="KakaoTalk_20210111_232749527" data-base62-sha1="se1BuO68CLZMPtLidDCvyUxUqQ3" width="358" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c5d2c1975f5fb1f57d25165edda6033852f68153_2_358x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c5d2c1975f5fb1f57d25165edda6033852f68153_2_537x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5d2c1975f5fb1f57d25165edda6033852f68153.jpeg 2x" data-dominant-color="544D55"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">KakaoTalk_20210111_232749527</span><span class="informations">634×885 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-01-11 16:33 UTC)

<p>DICOM RT structure set is a legacy format for storing image segmentation for radiation therapy planning. It has several fundamental limitations (one of them that it is practically impossible to represent complex shapes with many internal holes) and so it is not suitable as a generic format for storing image segmentation.</p>
<p>If you need to save segmentation in DICOM then I would recommend to install QuantitativeReporting extension and export the segmentation as DICOM Segmentation Object.</p>

---

## Post #3 by @jeongsu (2021-01-12 16:05 UTC)

<p>thank you for reply,<br>
I installed QuantitativeReporting extension, and made segmentation.<br>
I clicked the button named save report, complete report.<br>
But I found not any change on my computer.<br>
Where are my dicom files?<br>
How can I get dicom files with my segmentation and RT structure in dicom format…?</p>
<p>please help me,</p>

---

## Post #4 by @lassoan (2021-01-12 16:51 UTC)

<p>I would recommend to use latest Slicer Preview Release for DICOM export. We have made the GUI more clear.</p>

---
