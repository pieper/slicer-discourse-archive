# Enhanced DICOM question

**Topic ID**: 33648
**Date**: 2024-01-05
**URL**: https://discourse.slicer.org/t/enhanced-dicom-question/33648

---

## Post #1 by @Nathan (2024-01-05 23:18 UTC)

<p>Hello,</p>
<p>I have a weird request. We have one MRI scanner that only will upload data to PACs in “enhanced DICOM” format one file includes multiple images, and a different device that does not currently support this format (it wants individual DICOM image files).</p>
<p>I am looking for a way to convert enhanced DICOM to individual DICOM image files.</p>
<p>I can open the enhanced DICOM study in slicer and then export a DICOM series. This produces individual images, but all of the metadata is not included. Is there a way to export DICOM image files that retains the metadata?</p>
<p>-N</p>

---

## Post #2 by @pearsonm (2024-01-06 03:28 UTC)

<p>According to this post <a href="https://comp.protocols.dicom.narkive.com/cwh2glYg/split-multiframe-dicom-file" class="inline-onebox" rel="noopener nofollow ugc">split multiframe dicom file</a> dicom3tools by David Clunie should be able to split the MR enhanced file correctly.</p>
<p>Mark</p>

---
