---
topic_id: 46580
title: "Merging Patients In Dicom Database"
date: 2026-03-26
url: https://discourse.slicer.org/t/46580
---

# Merging Patients in DICOM Database

**Topic ID**: 46580
**Date**: 2026-03-26
**URL**: https://discourse.slicer.org/t/merging-patients-in-dicom-database/46580

---

## Post #1 by @Lesh3203 (2026-03-26 16:31 UTC)

<p>Is there a way to merge patients in the DICOM Database? This patient had imaging done at different facilities, and therefore has different patient IDs. As it’s all the same patient, I would love to merge them into one patient in the list.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/458ea695e637e74751615ec0e4dd3eae2a9cad01.png" data-download-href="/uploads/short-url/9VkzxuAA6jvSBykavMIPJbXVMch.png?dl=1" title="Screenshot 2026-03-25 at 12.01.58 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/458ea695e637e74751615ec0e4dd3eae2a9cad01.png" alt="Screenshot 2026-03-25 at 12.01.58 PM" data-base62-sha1="9VkzxuAA6jvSBykavMIPJbXVMch" width="682" height="154"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-03-25 at 12.01.58 PM</span><span class="informations">682×154 12.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2026-03-26 20:18 UTC)

<p>It is generally not allowed to modify attributes of a stored DICOM object. If you need to modify patient name, ID, etc. then the clean way is to create new DICOM objects with the corrected data with new SOP instance UIDs. For audit trail, the modified object should have reference to the original.</p>
<p>The closest that you can relatively easily achieve in Slicer is to load in image and then export it to DICOM with the desired patient name, ID, and birth date (these are used to decide in Slicer’s DICOM browser if two patients are the same). However, non-essential metadata may be lost when you import and re-export, so if you want to preserve all data then you need to do these modifications using some DICOM anonymizer or processor tool, or you can ask an AI chatbot to generate Python script that implements this.</p>

---
