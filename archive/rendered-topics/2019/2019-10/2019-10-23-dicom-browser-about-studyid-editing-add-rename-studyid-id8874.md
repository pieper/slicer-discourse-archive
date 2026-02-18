# [DICOM Browser] About StudyID Editing(Add&Rename StudyID)

**Topic ID**: 8874
**Date**: 2019-10-23
**URL**: https://discourse.slicer.org/t/dicom-browser-about-studyid-editing-add-rename-studyid/8874

---

## Post #1 by @lausiv (2019-10-23 12:54 UTC)

<p>Operating system: windows<br>
Slicer version: 4.10.2<br>
Expected behavior:<br>
Actual behavior:</p>
<p>HI <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p><strong>I want to add below function in DICOM Browser, Add StudyID, Rename StudyID.</strong></p>
<p>Anybody can help me hint about coding the call sequences (or sample codes)?<br>
Thank you</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/200dae075635ffea72f8b148194b0ebf67ee3c2d.png" data-download-href="/uploads/short-url/4zyArQx5qPuiHvNJccbyClQykbz.png?dl=1" title="studyediting" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/200dae075635ffea72f8b148194b0ebf67ee3c2d_2_632x500.png" alt="studyediting" data-base62-sha1="4zyArQx5qPuiHvNJccbyClQykbz" width="632" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/200dae075635ffea72f8b148194b0ebf67ee3c2d_2_632x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/200dae075635ffea72f8b148194b0ebf67ee3c2d_2_948x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/200dae075635ffea72f8b148194b0ebf67ee3c2d_2_1264x1000.png 2x" data-dominant-color="FDFEFE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">studyediting</span><span class="informations">2127×1682 33 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2019-10-23 13:15 UTC)

<p>You can create new/rename Patient/Study/Series in Data module in Subject hierarchy tab. When the study is completed you can export it to DICOM. If you enable import option then the exported study will be automatically imported into the DICOM database.</p>
<p>You can create new patient/study/series in the DICOM database by creating a DICOM dataset in memory or file and using it as input for ctkDICOMDatabase::insert().</p>
<p>DICOM standard does not allow you to modify any details of an instance after it is created, as the standard heavily relies on unique identifiers unambiguously identifying a complete data set. If you must modify data then you have to delete the original data set from the database and re-insert a new instance. If there is a chance that the original data set was exported from Slicer to external systems then you must generate a new UID (PACS behavior is undefined if it encounters modified data sets with the same UID).</p>

---

## Post #3 by @lausiv (2019-10-24 04:53 UTC)

<p>Thank you, I think 3D slicer is very powerful tools for medical image processing and other…</p>
<p>I will Study detailed about DICOM Spec and Slicer functions as you described</p>
<p><img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>2019년 10월 23일 (수) 오후 10:26, Andras Lasso via 3D Slicer Community <a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a>님이 작성:</p>

---

## Post #4 by @lausiv (2019-10-24 11:13 UTC)

<p>but, below sceanario, it doesn’t work at Data Module</p>
<ol>
<li>
<p>Add New Study</p>
</li>
<li>
<p>Import Existing DICOM to New Study(1)</p>
</li>
</ol>
<p>2019년 10월 24일 (목) 오후 1:53, 박촬리 <a href="mailto:lausiv@gmail.com">lausiv@gmail.com</a>님이 작성:</p>

---

## Post #5 by @lassoan (2019-10-24 15:20 UTC)

<p>If the study instance UID of the study folder that you created does not match the study instance UID stored in the imported DICOM series, then a new study folder will be created for the imported DICOM series.</p>

---

## Post #6 by @lausiv (2019-10-27 14:19 UTC)

<p>Thank you very much : )</p>

---
