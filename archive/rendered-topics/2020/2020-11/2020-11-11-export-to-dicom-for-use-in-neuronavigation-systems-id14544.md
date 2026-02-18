# Export to dicom for use in neuronavigation systems

**Topic ID**: 14544
**Date**: 2020-11-11
**URL**: https://discourse.slicer.org/t/export-to-dicom-for-use-in-neuronavigation-systems/14544

---

## Post #1 by @Gaston (2020-11-11 14:51 UTC)

<p>Hello, I am trying to export an image with its corresponding segmentation to dicom. But it is not possible for me to do it in any other format than DICOM RT.<br>
The idea is to be able to paint or segment structures and generate marks, export them to dicom and be able to use them in a neuronavigation system.<br>
The DICOM RT format is not supported by the neuronavigation system.<br>
I understand that maybe it is a trivial query.</p>

---

## Post #2 by @lassoan (2020-11-11 15:43 UTC)

<p>BrainLab can import DICOM segmentation objects. You can export a segmentation to DICOM segmentation object from Slicer after installing QuantitativeReporting extension (right-click on the segmentation node in Data module, and click Export to DICOM, select the study element in Select node section, and click Export).</p>
<p>If you have Medtronic, Stryker, or other navigation systems then probably you need to resort to workarounds. For example, a common technique is to generate a fake CT image using “Mask volume” effect (provided by SegmentEditorExtraEffects extension): fill the volume with -1000 outside the segment, 1000 inside the segment, and export this volume to DICOM. Segmenting this volume in the planning software should take only a few clicks. Some navigation systems might also allow importing of surface meshes (STL files).</p>
<p>You can also ask your navigation system representative what import options your software has (maybe there are also extra upgrades that you can buy to have more options). We can then help you getting segmentation in that format from Slicer.</p>

---

## Post #3 by @Gaston (2020-11-13 23:20 UTC)

<p>Hello Andras, is there any type of export that generates a series of images with the merged segmentation?<br>
It is for use in an old brainlab neuronavigator .</p>

---

## Post #4 by @lassoan (2020-11-14 02:41 UTC)

<p>I can use Mask volume effect to burn segments into a volume that you can then easily segment any surgical planning software.</p>

---

## Post #5 by @kopachini (2020-11-14 08:19 UTC)

<p>What neuronavigation system do you have? EDIT: just saw that you have brainlab neuronavigation… Nevertheless, try as bellow</p>
<p>I have successfully imported segmentation as .nifti file to Medtronic StealthStation s8 and I saw somewhere that it is possible with s7, too.<br>
So, try like that… Good luck.</p>

---

## Post #6 by @lassoan (2020-11-14 18:28 UTC)

<p>Thanks for the information, it is good to know that the s8 can do that.</p>

---
