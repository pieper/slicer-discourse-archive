---
topic_id: 21037
title: "Slicer Radiomics With Vtksegment"
date: 2021-12-13
url: https://discourse.slicer.org/t/21037
---

# Slicer radiomics with vtkSegment

**Topic ID**: 21037
**Date**: 2021-12-13
**URL**: https://discourse.slicer.org/t/slicer-radiomics-with-vtksegment/21037

---

## Post #1 by @Nello_Nepi (2021-12-13 20:19 UTC)

<p>Hi all.<br>
I am trying to use the radiomics lib but i cannot understand how to invoke the extractor.execute(image, mask) starting from a vtkSegment.<br>
My problem is that the mask is a segment of a segmentationNode, i cannot convert it to a simpleitk image.</p>
<p>Thanks in advantage</p>

---

## Post #2 by @lassoan (2021-12-14 14:19 UTC)

<p>You can export a volume from a segmentation as shown in these <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-labelmap-node-from-segmentation-node">examples in the script repository</a>. If needed, you can get a SimpleITK image from the exported volume as shown <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#running-an-itk-filter-in-python-using-simpleitk">here</a>.</p>

---
