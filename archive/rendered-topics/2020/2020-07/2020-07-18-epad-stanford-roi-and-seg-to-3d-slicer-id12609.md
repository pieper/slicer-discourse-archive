# EPAD Stanford ROI and SEG to 3D slicer

**Topic ID**: 12609
**Date**: 2020-07-18
**URL**: https://discourse.slicer.org/t/epad-stanford-roi-and-seg-to-3d-slicer/12609

---

## Post #1 by @Emmanuel_Salinas_Mir (2020-07-18 12:08 UTC)

<p>Hi.</p>
<p>Stanford software EPAD saves segmentations and ROIs as .json files.</p>
<p>Is there any possibility of using these files to create a standard nrrd segmentation or labelmap on 3D slicer ?</p>
<p>Regards</p>

---

## Post #2 by @pieper (2020-07-18 14:25 UTC)

<p>Sure, you should be able to write a simple parser in python and populate Slicer data structures.  I don’t think anyone has written code like that, but it would be a great contribution.</p>

---

## Post #3 by @lassoan (2020-07-18 14:43 UTC)

<p>Here is an example for Osirix ROI importer: <a href="https://github.com/PerkLab/SlicerSandbox/tree/master/ImportOsirixROI">https://github.com/PerkLab/SlicerSandbox/tree/master/ImportOsirixROI</a></p>
<p>Since then we have improved Slicer so that you can implement plugin that can load custom file formats right from the “Add data” window. See example here: <a href="https://github.com/SlicerHeart/SlicerHeart/tree/master/TomTecUcdPlugin">https://github.com/SlicerHeart/SlicerHeart/tree/master/TomTecUcdPlugin</a></p>
<p>If you are familiar with ePad file format and know a little Python programming then this should be really easy. We can help with mapping data objects to Slicer segmentation or markup nodes.</p>
<p>An alternative approach for ePad would be to move towards standard DICOM structured reports and segmentation objects. AIM made a lot of sense many years ago, when the effort was started, because at that time there was no good way of describing everything in DICOM. Also, AIM started out something that is simpler to use than DICOM. However, DICOM and related software have greatly improved, so now it is hard to justify investing into AIM support and seems to make more sense to converge to DICOM for data sharing and archiving.</p>

---

## Post #4 by @Emmanuel_Salinas_Mir (2020-07-19 13:49 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/pieper">@pieper</a> thanks a lot for your kind reply!</p>
<p>We will try the plugins. Unfortunately, we are not that familiar with the ePad file format.  But we will try. Hopefully, we will come out with the extension. That might be a nice bridge between ePad, which still attractive by its simple installation, web appearance, and use; and 3D slicer, which has no comparison (Just awesome!).</p>
<p>Regards</p>

---

## Post #5 by @pieper (2020-07-19 14:58 UTC)

<p>Hi <a class="mention" href="/u/emmanuel_salinas_mir">@Emmanuel_Salinas_Mir</a> - we <img src="https://emoji.discourse-cdn.com/twitter/heart.png?v=9" title=":heart:" class="emoji" alt=":heart:"> ePad too, and have <a href="https://projectweek.na-mic.org/PW33_2020_GranCanaria/Projects/ePadSlicer/">work together</a> on <a href="https://github.com/dcmjs-org/dicomweb-server">several</a> <a href="https://dicom4qi.readthedocs.io/en/latest/participants/">projects</a> but never did a native interface.</p>

---

## Post #6 by @lassoan (2020-07-19 17:21 UTC)

<p>As far as I remember ePad developers have been planning to provide DICOM Segmentation Object and Structured Report import/export features. Before investing too much time into AIM, ask them what is the status of this work. We have intent and funding for improving DICOM Seg and SR import/export in Slicer, so if ePad could use that then you would get full interoperability for free. It would also ensure that your data works with OHIF, Kheops, and many other DICOM compliant software.</p>

---
