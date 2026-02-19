---
topic_id: 608
title: "Dwiconvert Usage"
date: 2017-06-30
url: https://discourse.slicer.org/t/608
---

# DWIConvert usage

**Topic ID**: 608
**Date**: 2017-06-30
**URL**: https://discourse.slicer.org/t/dwiconvert-usage/608

---

## Post #1 by @Felix_Navarro_Guirad (2017-06-30 14:36 UTC)

<p>Hello everyone!</p>
<p>I’m trying to convert the scan files from DICOM to NIFTI using DWIConvert. Since the files come from the reformatting process of a sagittal scan the folder contains, as first slice, a schematic representation of the process showing where the axial slices were located.</p>
<p>Using dcm2niix or mcverter two NIFTI files are generated, one for this first slice and the other one for the volume. When I repeat the process using DWIConvert a strange volume is generated due to the DICOM tags of this first file, I guess.</p>
<p>Do you know if there is a workaround for this? This conversion is a step of an automated pipeline which cannot detect the first disturbing slice.</p>
<p>Thank you beforehand for your comments!!</p>
<p>Regards.</p>

---

## Post #2 by @ihnorton (2017-06-30 16:36 UTC)

<p>For the moment the best bet is probably to sort the files in a temp directory and run DWIConvert on that. DWIConvert examines every file in a directory and doesn’t do much general sorting or validation, so the program behavior is basically undefined if you have mixed series or non-DICOM data in the directory. Sometimes it just crashes.  <a href="https://discourse.slicer.org/t/slicer-dicom-scalar-volume-plugin-relies-on-old-gdcm-why-do-we-not-use-dcmtk/354/11?u=ihnorton">See this related comment about CLI file communication</a>.</p>

---

## Post #3 by @Felix_Navarro_Guirad (2017-06-30 16:49 UTC)

<p>Thanks <a class="mention" href="/u/ihnorton">@ihnorton</a>, I’ll keep this information in mind when I use DWIConvert.</p>
<p>Best regards.</p>

---
