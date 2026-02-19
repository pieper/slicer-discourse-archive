---
topic_id: 4439
title: "Difficulty Loading Dicom Data"
date: 2018-10-17
url: https://discourse.slicer.org/t/4439
---

# Difficulty loading DICOM data

**Topic ID**: 4439
**Date**: 2018-10-17
**URL**: https://discourse.slicer.org/t/difficulty-loading-dicom-data/4439

---

## Post #1 by @rsherwood (2018-10-17 16:05 UTC)

<p>Operating system: windows<br>
Slicer version:4.9.0-2018-10-16<br>
Expected behavior: to import dicom folder to allow model to be viewed<br>
Actual behavior: to import data set</p>
<p>Hello, Ive worked with slicer a little in the past to create anatomically correct 3d printed models for surgeons. i currently have a CT of a ‘dental stone’ mask of a patient who we hope to create a prosthetic for using meshmixer/3d printing ect…</p>
<p>When i load the data set it appears in the DICOM browser then when i go to load the data set i get a error</p>
<p>Could not load: 1: LOC XCT - 1 as a Scalar Volume</p>
<p>I then went on and read similar posts on the forums that described using the DICOM patcher. When i try to ‘patch’ i get this message</p>
<p>DICOM patching started…</p>
<p>Examining .\DIRFILE…</p>
<p>Unexpected error: Dataset does not have attribute ‘OffsetOfReferencedLowerLevelDirectoryEntity’.</p>
<p>Im sure there is something obvious but looking for any help at all!</p>
<p>Many thanks</p>
<p>Ross</p>

---

## Post #2 by @pieper (2018-10-17 16:22 UTC)

<p>Sounds like you’ve already done some background research, but did you try everything in the FAQ?</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM</a></p>

---

## Post #3 by @lassoan (2018-10-17 17:44 UTC)

<p>You can try deleting DIRFILE and re-import the data set.</p>

---

## Post #4 by @rsherwood (2018-12-20 10:07 UTC)

<p>Hello</p>
<p>Sorry for the late reply. I’ve been out of the office for a while on a project. We never got to the exact root of the problem but using a different CT scanner with the same models resulted in a DICOM data set that was readable by slicer. I asked the medical physist to explain why it would not work and this is what she said for anyone who is interested</p>
<p>‘The CTs that don’t work as well are part of hybrid systems (SPECT-CT systems) and the purpose of the CT is not to achieve fine resolution but for attenuation correction and localisation. As a result low dose (and therefore poor image quality) is perfectly adequate for this purpose, but isn’t giving the required resolution on the models. Our ability to vary parameters for the CT scan is quite restricted as these are not standalone CT systems.’</p>

---

## Post #5 by @lassoan (2018-12-20 11:33 UTC)

<p>Thanks for the update. It may be possible that the system exports the CT-like volume in a way that it cannot be loaded as an image to prevent using it as a diagnostic CT scan. If it is important for you to be able to load such scans into Slicer then we would need you to share at least one sample data set (anonymized patient or of some test object).</p>

---
