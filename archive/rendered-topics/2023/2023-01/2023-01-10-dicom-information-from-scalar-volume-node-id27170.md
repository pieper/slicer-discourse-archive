---
topic_id: 27170
title: "Dicom Information From Scalar Volume Node"
date: 2023-01-10
url: https://discourse.slicer.org/t/27170
---

# DICOM Information from Scalar Volume Node

**Topic ID**: 27170
**Date**: 2023-01-10
**URL**: https://discourse.slicer.org/t/dicom-information-from-scalar-volume-node/27170

---

## Post #1 by @kleingeo (2023-01-10 16:26 UTC)

<p>I have a <code>vtkMRMLScalarVolumeNode</code> that is imported from a DICOM database. Is there a way to obtain the DICOM information from the scalar volume node? It seems like all DICOM information is lost in the volume itself, but I am unaware about how to get it back.</p>

---

## Post #2 by @pieper (2023-01-10 18:26 UTC)

<p>Yes, the list of instance UIDs (per-slice) is stored as an attribute on the volume node.  You can query the database or open the original instances to get all the data.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#access-top-level-tags-of-dicom-images-imported-into-slicer" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#access-top-level-tags-of-dicom-images-imported-into-slicer</a></p>

---

## Post #3 by @cpinter (2023-01-11 13:53 UTC)

<p>Also there is DICOM information in the subject hierarchy items created.</p>
<p>For example this is the study level DICOM information, but you have info on the patient, series, and instance levels too, clicking on the other items.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1568d7066ffb26c5d9880be361f8311c4b9aa76.png" alt="image" data-base62-sha1="piNWUkqnEwwsPxIYnty3p3uM2vI" width="483" height="499"></p>

---
