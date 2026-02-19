---
topic_id: 9834
title: "Modifying Metadata"
date: 2020-01-16
url: https://discourse.slicer.org/t/9834
---

# Modifying metadata

**Topic ID**: 9834
**Date**: 2020-01-16
**URL**: https://discourse.slicer.org/t/modifying-metadata/9834

---

## Post #1 by @arumiat (2020-01-16 12:27 UTC)

<p>Hi there community,</p>
<p>Am I right in thinking that there is not a way to edit DICOM metadata fields (like patient name etc) directly within Slicer?</p>
<p>I understand that some fields are protected and uneditable?</p>
<p>But I was hoping to be able to modify some of the fields where possible.</p>
<p>If it’s not possible within Slicer, it would be great if you have any recommendations for a simple GUI tool that could do so, on studies with multiple series.</p>
<p>Hope to hear,<br>
A</p>

---

## Post #2 by @pieper (2020-01-16 13:39 UTC)

<p>Typically it’s easier to script this than to use a GUI.  In Slicer we provide <a href="https://pydicom.github.io/pydicom/stable/getting_started.html">pydicom</a> via the console.  You can look at the source code of <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMPatcher/DICOMPatcher.py">the DICOMPatcher</a> for ideas.</p>
<p>If your goal is to deidentify, then I suggest <a href="http://www.dclunie.com/pixelmed/software/webstart/DicomCleanerUsage.html">DicomCleaner</a> for a nice GUI for batch operations.</p>

---

## Post #3 by @lassoan (2020-01-16 14:31 UTC)

<aside class="quote no-group" data-username="arumiat" data-post="1" data-topic="9834">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f05b48/48.png" class="avatar"> arumiat:</div>
<blockquote>
<p>But I was hoping to be able to modify some of the fields where possible.</p>
</blockquote>
</aside>
<p>There are software tools available for modification DICOM files (see <a class="mention" href="/u/pieper">@pieper</a>’s answer above) but in general you are not allowed to use them.</p>
<p>After you exported data to DICOM information object and attached a unique identifier (UID), the content of that object must not be changed, because it would violate an essential assumption of all DICOM software (that the same UID always refers to the exact same content) and could lead to data loss and corruption.</p>
<p>To make changes to any DICOM objects, you need to generate a modified copy (with new UID) and send out request to hide previous version of the object. The process is defined in IHE profiles such as  “IOCM” (Imaging Object Change Management).</p>
<p>Slicer only implements basic DICOM networking and does not support IOCM or similar IHE profiles, so if you need to make any changes, you need to do it manually (import and load an image, modify it, export it to DICOM, and import it back to the database).</p>

---
