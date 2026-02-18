# Integration of External Toolkit in Slicer

**Topic ID**: 41508
**Date**: 2025-02-05
**URL**: https://discourse.slicer.org/t/integration-of-external-toolkit-in-slicer/41508

---

## Post #1 by @alientex (2025-02-05 03:53 UTC)

<p>Hello,</p>
<p>I have built MITK v2024.12 locally. Is it possible to integrate this toolkit into Slicer to extend segmentation and image processing functionalities?</p>
<p>Thank you for any suggestions.</p>

---

## Post #2 by @RafaelPalomar (2025-02-05 07:43 UTC)

<p>MITK is a great toolkit and comes with functionality that overlaps with 3D Slicer. I don’t see, however, what type of integration could be useful and possible; could you explain what would be your idea for integration? I would think that it makes sense to use either MITK or 3D Slicer.</p>

---

## Post #3 by @alientex (2025-02-05 07:57 UTC)

<p>I know that MITK has its own workbench, so it does make sense to use either MITK or 3D Slicer. However, the main idea behind integrating this toolkit into Slicer is its <strong>interaction functionalities</strong> (e.g., Contour Utilities) that are available on top of VTK, rather than having to develop these functionalities from scratch in Slicer. I believe <strong>data conversion between Slicer and MITK</strong> should not be an issue since both rely on VTK.</p>
<p>Since I encountered many errors when building an older version of MITK to make it compatible with Slicer and its other libraries, I decided to build the latest version instead. So, I was wondering if there is any way to use functions from this toolkit in Slicer by integrating it as an <strong>external project, a Slicer extension, or a module</strong>, perhaps.</p>

---

## Post #4 by @RafaelPalomar (2025-03-04 13:51 UTC)

<p><a class="mention" href="/u/alientex">@alientex</a>, I don’t  see an easy way for integrating functionality involving interaction from MITK to Slicer (interaction in MITK and Slicer are probably very different). Extending the segmentation/markups functionality of 3D Slicer through your own extension would be the way to go, if you would like to port some of the functionality of MITK.</p>
<p>It might be worth for you checking on the large pool of extension 3D Slicer offers. Maybe you find similar functionality already implemented in an extension.</p>

---
