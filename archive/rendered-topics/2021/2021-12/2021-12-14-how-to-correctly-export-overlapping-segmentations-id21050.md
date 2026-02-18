# How to correctly export overlapping segmentations?

**Topic ID**: 21050
**Date**: 2021-12-14
**URL**: https://discourse.slicer.org/t/how-to-correctly-export-overlapping-segmentations/21050

---

## Post #1 by @jlvahldiek (2021-12-14 12:52 UTC)

<p>Operating system: MacOS, Windows<br>
Slicer version: 4.13.0</p>
<p>Actual behavior: Several segmentations are drawn overlapping. These are exported to a nrrd file using the segmentations module (‘export to files’). When loading back this file as segmentation overlaps are lost and the segmentations are flattened.</p>
<p>Expected behavior: Overlaps/layers are preserved.</p>
<p>What is the correct way to export overlapping segmentations?</p>
<p>Thanks you, kind regards,<br>
Janis</p>

---

## Post #2 by @cpinter (2021-12-14 13:43 UTC)

<p>What do you want to load the exported files into?</p>
<p>Normal NRRD does not support overlapping segments because it is a single-layer 3D image, nothing more. If you want to save your segmentation for later use in Slicer, save it in our segmentation format, .seg.nrrd. Otherwise you may want to export each segment into its own file.</p>

---

## Post #3 by @jlvahldiek (2021-12-14 19:47 UTC)

<p>Thank you for the clarification.</p>
<p>I am exploring Project-MONAI/MONAILabel and their Slicer extension in order to simplify annotation workflows of large datasets. I will have several overlapping segmentations in 2D and 3D images that need to be saved to one single file that is transferred to the MONAILabel server.<br>
Most of these segmentation files need to be re-imported into Slicer at a later stage. Some other of these segmentation files will be used directly to train segmentation models.</p>
<p>Thanks to your reply I have already found a workaround to save several overlapping segmentations into a single .seg.nrrd file via the MONAILabel extension. I will probably raise a PR on MONAILabel fixing overlapping segmentations.</p>

---
