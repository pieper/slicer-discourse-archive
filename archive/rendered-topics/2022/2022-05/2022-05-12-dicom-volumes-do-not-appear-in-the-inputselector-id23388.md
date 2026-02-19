---
topic_id: 23388
title: "Dicom Volumes Do Not Appear In The Inputselector"
date: 2022-05-12
url: https://discourse.slicer.org/t/23388
---

# Dicom volumes do not appear in the inputselector

**Topic ID**: 23388
**Date**: 2022-05-12
**URL**: https://discourse.slicer.org/t/dicom-volumes-do-not-appear-in-the-inputselector/23388

---

## Post #1 by @Linhsia_Noferini (2022-05-12 12:37 UTC)

<p>Operating system: windows<br>
Slicer version: 4.11<br>
Expected behavior: we are using the extension wizard, “create module”. The default generated inputselector should accept any volume from the scene, indipendently from the source file type (DICOM, nii,…)<br>
Actual behavior: the inputselector allows only volumes from NOT dicom files to be selected: dicom volumes do not appear in the list showed by the inputselector</p>

---

## Post #2 by @cpinter (2022-05-12 12:56 UTC)

<p>What modality is the DICOM you loaded and don’t find in the selector?</p>

---

## Post #3 by @Linhsia_Noferini (2022-05-12 13:01 UTC)

<p>They are MRI volume. We tried with CT and it works. The problem seems with mri.</p>

---

## Post #4 by @lassoan (2022-05-12 13:41 UTC)

<p>By default the volume selector accepts scalar volumes. Your MRI is a different type, for example an RGB image (typical for secondary captures, such as screenshots), tensor volume, or multi-volume (time sequence). You can specify multiple node classes for your node selector to display, or let the user know that only scalar volumes are accepted.</p>

---

## Post #5 by @Linhsia_Noferini (2022-05-12 13:55 UTC)

<p>By defoult the dicom importer set the DICOM volume as ‘DWI volume’ and not scalar.<br>
we have changed the property to scalr volume and now it works, so many thank for your quick and effective reply!</p>

---
