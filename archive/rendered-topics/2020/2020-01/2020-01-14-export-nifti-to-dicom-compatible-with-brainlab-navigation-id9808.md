# Export nifti to DICOM compatible with Brainlab navigation

**Topic ID**: 9808
**Date**: 2020-01-14
**URL**: https://discourse.slicer.org/t/export-nifti-to-dicom-compatible-with-brainlab-navigation/9808

---

## Post #1 by @dan.lewis1112 (2020-01-14 15:50 UTC)

<p>Hi all,</p>
<p>I am trying to use Slicer 4.10.1 to convert  a nifti file to a DICOM file format compatible with Brainlab navigation system. It appears the DICOM IMG files are being generated but I cant view them on the Brainlab interface. The problem seems to be I cant generate a DICOM directory text file. Does anyone know how I can do this?</p>
<p>Thanks for any help</p>

---

## Post #2 by @lassoan (2020-01-15 02:03 UTC)

<p>DICOM directory text file (DICOMDIR) is optional, it shouldn’t be a problem that you don’t have it. If you want, you can create one using the <a href="https://support.dcmtk.org/docs/dcmmkdir.html">dcmmkdir tool</a> of the free DCMTK toolkit.</p>
<p>What kind of file are you trying to export from Slicer and load into Brainlab?</p>
<p>You may also be able to push DICOM files from Slicer directly to the navigation system using DICOM networking (C-store SCP).</p>
<p>If you have license for OpenIGTLink communication in Brainlab then you can even stream tracking data, images, and landmark points in real-time between Slicer and BrainLab during a procedure.</p>
<p>Use most latest stable or recent preview release of Slicer. I would recommend the latest preview release, as the DICOM browser and networking are much more robust, faster, and easier to use.</p>

---
