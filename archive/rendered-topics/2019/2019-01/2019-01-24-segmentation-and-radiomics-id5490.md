# Segmentation and radiomics

**Topic ID**: 5490
**Date**: 2019-01-24
**URL**: https://discourse.slicer.org/t/segmentation-and-radiomics/5490

---

## Post #1 by @marline19 (2019-01-24 00:26 UTC)

<p>Hello I have some questions about segmentation and radiomics programms. How I can create segmentation of  high grade glioma  and then use radiomics? I don’ t understand how its work  because when we do segmentation we must  take account of tumor+ necrosis and edema. Sorry for my english. Help me please.</p>
<p>Elena</p>

---

## Post #2 by @fedorov (2019-01-24 18:21 UTC)

<p>Once you install the Radiomics extension, you will be able to calculate radiomics features for every segment defined for your image. If you segment edema/necrosis separately, you will have separate set of features for each of those regions. If you want a single set of features for the whole tumor, then you will need to create a single segmentation segment that includes all of those. You can use “merge” functionality from the Segment Editor to merge multiple segments.</p>

---
