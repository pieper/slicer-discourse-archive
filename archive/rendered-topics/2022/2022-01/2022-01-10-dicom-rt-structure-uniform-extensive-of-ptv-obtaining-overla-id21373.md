# DICOM, rt structure, uniform extensive of PTV, obtaining overlap volume between PTV and the organ

**Topic ID**: 21373
**Date**: 2022-01-10
**URL**: https://discourse.slicer.org/t/dicom-rt-structure-uniform-extensive-of-ptv-obtaining-overlap-volume-between-ptv-and-the-organ/21373

---

## Post #1 by @Arash_Ebrahimi (2022-01-10 02:32 UTC)

<p>Hi to all,<br>
I am a medical researcher and my current project is about IMRT and machine learning.<br>
To get prepared the input data for Neural network model, I need to enlarge or shorten the PTV volume and calculate overlap volume between the PTV and one of the organ at risks.<br>
Is it possible to do it with Slicer? Or should I follow python coding?</p>

---

## Post #2 by @cpinter (2022-01-10 10:41 UTC)

<p>You can add or remove margin using the <code>Margin</code> tool of the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html">Segment Editor</a> module.</p>
<p>Calculating overlap can be done using the <code>Logical operators</code> tool of the same module, after which you can calculate the volume of the intersection segment in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html">Segment Statistics</a> module.</p>
<p>Please note you’ll need to install SlicerRT in the Extension manager in order to be able to load DICOM-RT data.</p>

---

## Post #3 by @Arash_Ebrahimi (2022-01-10 12:45 UTC)

<p>Thank u for your help.<br>
I found also two other modules named segment morphology and contour morphology.<br>
How can I use them?</p>

---

## Post #4 by @Arash_Ebrahimi (2022-01-10 12:59 UTC)

<p>Can not find contour morphology to install it.</p>

---

## Post #5 by @cpinter (2022-01-10 13:01 UTC)

<p>Contour morphology is deprecated, it was replaced by Segment morphology. Most of the functionality in Segment morphology has been integrated into Segment Editor (see Logical operators effect), but it should be still functional.</p>

---
