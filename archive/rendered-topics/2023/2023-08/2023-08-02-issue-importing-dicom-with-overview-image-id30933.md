---
topic_id: 30933
title: "Issue Importing Dicom With Overview Image"
date: 2023-08-02
url: https://discourse.slicer.org/t/30933
---

# Issue Importing DICOM with overview image

**Topic ID**: 30933
**Date**: 2023-08-02
**URL**: https://discourse.slicer.org/t/issue-importing-dicom-with-overview-image/30933

---

## Post #1 by @gendex (2023-08-02 13:49 UTC)

<p>We just started using Slicer and ran into the following issues:</p>
<p><strong>Slicer 4.10.2 Tests</strong></p>
<p>-loaded image stack without overview image (both with and without “apply regularization transform”)</p>
<p>-get error: <em>Irregular volume geometry detected, but maximum error non-zero but is within tolerance (maximum error of 1.34414e-05 mm, tolerance threshold is 0.001 mm).</em></p>
<p>-loaded full image stack with overview image</p>
<p>-selected only volume without overview image (as per this post: <a href="https://discourse.slicer.org/t/problems-during-dicom-import/9060/12" class="inline-onebox">Problems during Dicom import - #12 by lassoan</a>)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e570bbe222a5cb27e38e120474e451934b80b74c.png" data-download-href="/uploads/short-url/wJIS47MUxBK9YekeY4BIFFPjVMg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e570bbe222a5cb27e38e120474e451934b80b74c_2_690x423.png" alt="image" data-base62-sha1="wJIS47MUxBK9YekeY4BIFFPjVMg" width="690" height="423" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e570bbe222a5cb27e38e120474e451934b80b74c_2_690x423.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e570bbe222a5cb27e38e120474e451934b80b74c_2_1035x634.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e570bbe222a5cb27e38e120474e451934b80b74c_2_1380x846.png 2x" data-dominant-color="E9F0F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1437×881 31.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>-still get error Irregular volume geometry detected which suggests there is an issue with other images</p>
<p>-checked image Metadata image, ImageOrientationPatient seems to be constant for all slices except overview slice as expected</p>
<p>-ImagePositionPatient seems to be consistent between slices except in Z axis as expected</p>
<p><strong>Slicer 5.2.2</strong></p>
<p>-image stack without overview image causes Slicer to crash</p>
<p>-image stack with overview image, then selecting only volume without overview image for loading also causes Slicer to crash</p>
<p>Unfortunately we cannot share the image stack at this time.</p>
<p>Thank you,<br>
Dennis</p>

---

## Post #2 by @lassoan (2023-08-02 14:25 UTC)

<p>This is very surprising, as un recent years we have not had any reports of Slicer crashing when attempting to load DICOM data.</p>
<p>Please try the latest Slicer Preview Release, as we continuously make improvements to the software.</p>
<p>If you still experience any DICOM loading issues then please send us (upload somewhere and post the link here) the application log where a crash occurred. You can retrieve application log of previous sessions in menu: Help / Report a bug. You can inspect the text before uploading and remove and patient information from it (do not remove complete messages, just replace any identifiers by some placeholder text).</p>

---

## Post #3 by @gendex (2023-08-02 16:14 UTC)

<p>Thanks for the quick reply.</p>
<p>I installed the latest Slicer Preview Release (5.3.0) and now sometimes the DICOM files load successfully and in about 30% of times Slicer crashes.</p>
<p>You can find two application logs in the link below. One is a crash log, the other a log of when it loaded successfully. The read me file describes which log is which case.</p>
<p><a href="https://drive.google.com/drive/folders/1rDZ2-4hWyEgC6XKkgWUrpIxQiJ2z0eb6?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1rDZ2-4hWyEgC6XKkgWUrpIxQiJ2z0eb6?usp=sharing</a></p>

---

## Post #4 by @lassoan (2023-08-02 17:05 UTC)

<p>The logs shiw that the images were anonymized incorrectly (patient ID is a required field and it is not allowed to be empty). It indicates that inappropriate software or settings were used or they were used incorrectly, which may have caused unexpected errors during loading. You may consider ask for the data set again, making sure that the person is doing it has the necessary expertise.</p>
<p>What is the size of the image you are loading (in voxels)? Does s the crash occur when the import is finished or later, when you try to load the image?</p>

---

## Post #5 by @evaherbst (2023-08-03 07:35 UTC)

<p>Thank you Andras.<br>
I am working together with Dennis on this project.</p>
<p>Good point about the patient ID field. I got the scan from a surgeon and I am not sure how he removed the patient ID. I will ask him to redo the deidentification and replace the patient ID with a random number instead.</p>
<p>The crash occurs after import, when trying to load the files.<br>
This happens on Dennis’s machine (CPU only) and I also tested it on my work and personal laptop (both have GPU and different ones). The file size is not that large anyway. So I think we can rule out any computer specific issues.</p>

---

## Post #6 by @evaherbst (2023-08-03 09:55 UTC)

<p>Hi again.</p>
<p>I just used <a href="https://www.microdicom.com/" rel="noopener nofollow ugc">https://www.microdicom.com/</a> to adjust the patient ID.<br>
(upload image, go to View &gt; Dicom tags, edit ID, then  ‘apply’ making sure ‘patient’ rather than ‘image’ is selected)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98cee7d21d954b7aaa73e338f0f95dd825095736.png" alt="image" data-base62-sha1="lNNRQUKdourrBcuSI6R0HgWF0xw" width="550" height="37"></p>
<p><strong>please note this operation is destructive (it will directly change your files) so make sure to first make a copy of your image stack!</strong></p>
<p>The dataset now loads in 5.2.2 (I tested it with the overview image removed, but I think it would also work with the overview image).</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> would it be possible to add some sort of dicom tag editing support in future versions of Slicer? I imagine this could be useful for image deidentification too.</p>
<p>Thanks!<br>
Eva</p>

---

## Post #7 by @lassoan (2023-08-04 02:05 UTC)

<p>Anonymization is an extremely complex topic, as you need to be very careful in removing all protected health information while still keeping the data sets usable. For example, you cannot simply replace the patient birth date with some random number but you need to add a random offset to the patient birth date and all study creation/series acquisition date fields, consistently in all studies of that patient. You cannot simply remove unique identifiers but you need to replace them with study-specific identifiers and store the mapping in access-controlled files. You need to inspect image content - remove all burnt-in annotations (typical in secondary captures), remove/blur patient face or other unique features that can identify a patient, all that in a way to not interfere with proper use of the inage. You need to pay close attention to private fields - simply removing them can make the data set unusable, so you need to investigate what each field contains (in DICOM conformance statements of each vendor) and consult with users of the data to determine what is needed and what needs to be changed or removed.</p>
<p>So, proper anonymization requires not just simple editing of some DICOM fields, but it requires complex software suite and significant expertise to operate it.</p>

---

## Post #8 by @gendex (2023-08-04 11:32 UTC)

<p>Thank you for pointing that out.</p>
<p>That’s likely the reason why on my machine, I can’t get the files to successfully load consistently. Neither adding a patient ID with MicroDicom nor “re-cleaning” the data with DicomCleaner (default settings) did the trick. The files were likely corrupted during the initial anonymization. We’ll make sure that we’ll get correctly anonymized DICOM files from the clinic in the future.</p>
<p>However, I noticed two interesting phenomena:</p>
<ul>
<li>Immediately after testing if I could load the corrupt files consistently (crashed 40% of times), Slicer crashed while loading a publicly available DICOM dataset. After the initial crash, the dataset successfully loaded consistently.</li>
<li>The first time I tried to load the “re-cleaned” (with DicomCleaner) dataset, it loaded the publicly available DICOM dataset, even though I had previously deleted that from the DICOM database in Slicers “Add DICOM data” module.</li>
</ul>

---

## Post #9 by @evaherbst (2023-08-08 14:24 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a><br>
We have spoken to the clinicans and they will ensure the anonymization is done properly in the future.</p>
<p>Regaring the issues loading the scans, could it be possible that some data is somehow saved in the SlicerDicomDatabase or some other cache and that is somehow trying to load a previous dataset?<br>
Maybe that could explain the issues Dennis was having with the visible human dataset (<a href="https://medicine.uiowa.edu/mri/facility-resources/images/visible-human-project-ct-datasets" class="inline-onebox" rel="noopener nofollow ugc">Visible Human Project CT Datasets | Magnetic Resonance Research Facility</a>) and the loading of the wrong files.</p>
<p>Thank you,<br>
Eva</p>

---

## Post #10 by @lassoan (2023-08-08 17:05 UTC)

<p>Yes, it is possible to pollute the database with corrupted data. DICOM is not a file format, but a distributed database. Data objects can be stored in files and cross-referenced with unique identifiers. If you modify a file (e.g., remove patient name) then you must update the unique identifier of that object in the file. If any other DICOM object referenced the modified object by UID then that object must be updated as well (and a new UID must be generated for it, and any object that referenced these modified objects must be updated as well, etc.). Slicer (and most other DICOM software) will ignore any new file that have the same UID as a previously indexed file.</p>
<p>If you only have images (you don’t have any segmentations, treatment plans, etc. referring to those images) then you may not need to update any references. However, you still need to replace the UIDs in all modified objects. Typically, you need to regenerate patient ID, study instance UID, frame of reference UID and use them for all the series in the study; regenerate series instance UID and use it in all files of the series; and regenerate new SOP instance UID for each DICOM file.</p>
<p>DICOM is very complex, but it also provides a lot of functionality (data provenance, metadata, references, etc), so it may worth investing time into learning it and setting up data processing workflows properly.</p>

---
