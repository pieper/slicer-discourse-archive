# Obj file segmentation

**Topic ID**: 34529
**Date**: 2024-02-25
**URL**: https://discourse.slicer.org/t/obj-file-segmentation/34529

---

## Post #1 by @gokcetaniyan (2024-02-25 15:48 UTC)

<p>I have data in obj format. I want to segment the bones in this data. In “Data” module, I right clicked my data and selected “convert model to segmentation mode”. Then I went to the “segment editor” section. None of the segmentation tools were active in this section. I was asked to select the source volume, but I don’t know what to choose in this section. When I clicked on source volume, there was no object to select. Could you give information about how to segment from a data in obj format?</p>

---

## Post #2 by @muratmaga (2024-02-25 17:48 UTC)

<p>For segment editor to work, it needs to have a master volume. The step you descrbed only created the segmentation. To create a scalar volume, right click on the segmentation you just created in Data module, and choose “export as a label map” option. Then you can specify that label map as the source volume in the segment editor and use the tools.</p>

---

## Post #3 by @gokcetaniyan (2024-02-27 10:54 UTC)

<p>Thank you very much!</p>

---
