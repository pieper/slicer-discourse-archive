---
topic_id: 14499
title: "Converting Dosxyz Output 3Ddose To Dicom Rt To Be Read In Pi"
date: 2020-11-09
url: https://discourse.slicer.org/t/14499
---

# Converting dosxyz output (.3ddose) to DICOM RT to be read in Pinncale and Eclipse

**Topic ID**: 14499
**Date**: 2020-11-09
**URL**: https://discourse.slicer.org/t/converting-dosxyz-output-3ddose-to-dicom-rt-to-be-read-in-pinncale-and-eclipse/14499

---

## Post #1 by @LMI (2020-11-09 03:04 UTC)

<p>Hello,<br>
I have a .3ddose file from dosxyx. I would like to convert it to Dicom format to import it to Pinnacle and Eclipse TPS. I loaded the dosxyz file in 3D Slicer and exported it as a Dicom file. But, it is not in the right format (Dicom RT). Also, I would like to scale the dose values so that I can compare it with the plan calculated by TPS. I’m not sure if there is any direct way to do this in 3DSlicer, Any thoughts?<br>
Thank you</p>

---

## Post #2 by @cpinter (2020-11-09 08:17 UTC)

<p>Since you were able to load the 3ddose file you probably have SlicerRT installed, so that’s good. To export the volume to dose, you will need to</p>
<ul>
<li>Make sure you have a patient and study under which you have</li>
<li>A CT or MR (unfortunately necessary), and the dose</li>
<li>Right-click the dose in the Data module and choose Convert to dose volume. You will be able to set the scaling there as well</li>
</ul>
<p>Let me know how it goes.</p>

---

## Post #3 by @LMI (2020-11-10 01:42 UTC)

<p>Thank you for your reply, I put the CT dicom images and the 3ddose file under a patient and a study. I right-clicked and did the scaling. For exporting, I selected the CT images, then the 3ddose file and selected the export type as RT.<br>
It gives the message that “Dicom dataset successfully exported to the DICOM database folder”. But, when I check the dicom files in the folder, they are series of CT images. It doesn’t contain dose (is not in RT format).<br>
Thanks</p>

---

## Post #4 by @cpinter (2020-11-10 08:22 UTC)

<p>Can you post a screenshot of the Subject hierarchy tree right before you click Export to DICOM?</p>

---

## Post #5 by @LMI (2020-11-10 12:44 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebbaaccad2c24d8a0782d5ae0699ee393126d684.png" data-download-href="/uploads/short-url/xDm9Bbf712GCULDz16SLGkWjByI.png?dl=1" title="3DSlicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebbaaccad2c24d8a0782d5ae0699ee393126d684_2_690x348.png" alt="3DSlicer" data-base62-sha1="xDm9Bbf712GCULDz16SLGkWjByI" width="690" height="348" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebbaaccad2c24d8a0782d5ae0699ee393126d684_2_690x348.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebbaaccad2c24d8a0782d5ae0699ee393126d684_2_1035x522.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebbaaccad2c24d8a0782d5ae0699ee393126d684_2_1380x696.png 2x" data-dominant-color="ACACAE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3DSlicer</span><span class="informations">1922×970 176 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @cpinter (2020-11-10 13:19 UTC)

<p>Thanks, this looks good. To see which further step may be the problem, can you please also post a screenshot about the DICOM export window before clicking export, and attach the log (About / Report a problem, and make sure you select the correct session), the whole thing in a gist or just the last few entries here?</p>

---

## Post #7 by @LMI (2020-11-10 22:02 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7a09380f4a76832eb6839508179712e2641f660.png" data-download-href="/uploads/short-url/stZ34k8Fp0gq15urZhfV14OCa08.png?dl=1" title="3dSlicer2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7a09380f4a76832eb6839508179712e2641f660_2_690x371.png" alt="3dSlicer2" data-base62-sha1="stZ34k8Fp0gq15urZhfV14OCa08" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7a09380f4a76832eb6839508179712e2641f660_2_690x371.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7a09380f4a76832eb6839508179712e2641f660_2_1035x556.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7a09380f4a76832eb6839508179712e2641f660_2_1380x742.png 2x" data-dominant-color="C7C8CC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3dSlicer2</span><span class="informations">1895×1020 228 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @LMI (2020-11-10 22:04 UTC)

<p>and here is the log file, thank you!</p>
<p>[ERROR][Python] 10.11.2020 17:00:53 [Python] (/home/lalageh/Slicer-4.11.20200930-linux-amd64/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/SegmentEditorSubjectHierarchyPlugin.py:124) - Invalid current item<br>
[CRITICAL][Qt] 10.11.2020 17:00:53 [] (unknown:0) - virtual void qSlicerSubjectHierarchyRegisterPlugin::showContextMenuActionsForItem(vtkIdType) : Invalid current item<br>
[CRITICAL][Stream] 10.11.2020 17:00:53 [] (unknown:0) - Invalid current item<br>
[CRITICAL][Qt] 10.11.2020 17:00:58 [] (unknown:0) - void qSlicerSubjectHierarchyDICOMPlugin::openDICOMExportDialog() : Invalid current item</p>

---

## Post #9 by @cpinter (2020-11-11 11:10 UTC)

<p>Instead of selecting the two series, please select the study.</p>

---

## Post #10 by @LMI (2020-11-12 03:26 UTC)

<p>Thank you!<br>
I selected the study this time, when I select the “Scalar Volume” for the export type, it creates two folders with a series of dicom images. It seems it is working.<br>
But when I select the export type as “RT”, it gives the same message that “DICOM dataset successfully exported to the DICOM database folder…” but it doesn’t create any dicom file. I’m not sure why</p>

---

## Post #11 by @lassoan (2020-11-12 06:19 UTC)

<p>You might find the DICOM export user interface a bit more intuitive in the latest Slicer Preview Release. There you can either select a folder (then all DICOM files will be exported there); or you don’t select a folder and then files are exported to Slicer’s DICOM database (and then you can send the data set to a DICOM server or export to files later).</p>

---

## Post #12 by @LMI (2020-11-13 02:43 UTC)

<p>Thank you both! I tried with the Slicer-4.13.0-2020. It is working, it creates the DICOM RT file.<br>
When I import it to Eclipse, it just gives some errors:<br>
S002: (F) 2020/11/12 21:39:27.841 [21960] Mandatory element contains no data (Element: (0008,1155) ‘Referenced SOP Instance UID’)<br>
Not sure, if this is something that I can edit in 3DSlicer</p>

---

## Post #13 by @lassoan (2020-11-13 03:36 UTC)

<p><a class="mention" href="/u/gcsharp">@gcsharp</a> could you have a look if this missing DICOM reference should be fixed in SlicerRT or in Plastimatch?</p>

---

## Post #14 by @LMI (2020-11-22 22:19 UTC)

<p>Hello,</p>
<p>In addition to the missing DICOM reference, I have another problem in the Data module when I am scaling:<br>
If I type 3E-16 (or 0.0000000000000003) in the scaling box, It doesn’t work. It is limited. Any idea?</p>
<p>Thank you</p>

---

## Post #15 by @cpinter (2020-11-23 08:36 UTC)

<p>The scaling parameter is not considered during export (see its absence in the <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/Logic/vtkSlicerDicomRtImportExportModuleLogic.cxx#L2608-L2639">code</a>). I think the reason we did not add it, is that we use it for import, so if we import a dose then export it without changes, then scaling would be applied twice.<br>
If anyone has a good suggestion that would be welcome.</p>

---
