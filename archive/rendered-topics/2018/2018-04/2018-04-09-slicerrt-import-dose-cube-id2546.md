# SlicerRT Import Dose Cube

**Topic ID**: 2546
**Date**: 2018-04-09
**URL**: https://discourse.slicer.org/t/slicerrt-import-dose-cube/2546

---

## Post #1 by @giancu (2018-04-09 16:02 UTC)

<p>Hi everyone.<br>
I’m trying to visualize a modified dose cube. I succed in loading it, but the cube is displayed in the original format (like short: from 0 to 65536 values). I am wondering why is the DICOM Tag “(3004,000e)” aka DoseGridScaling ignored. I thought this should rescale the values into dose.</p>
<p>Thank you.<br>
Cheers Gheorghe</p>

---

## Post #2 by @gcsharp (2018-04-09 17:37 UTC)

<p>Hi Gheorghe,</p>
<p>My first suspicion is that your object is being interpreted by the Slicer DICOM image loader rather than the SlicerRT DICOM dose loader.  This would explain your symptoms.</p>
<p>Would it be possible for you to post your error log?</p>
<p>Greg</p>

---

## Post #3 by @cpinter (2018-04-09 17:50 UTC)

<p>Do you have the SlicerRT extension installed?</p>

---

## Post #4 by @giancu (2018-04-09 17:56 UTC)

<p>Here is the log text:</p>
<p>Loaded volume from file: /home/george/test.dcm. Dimensions: 512x512x105. Number of components: 1. Pixel type: unsigned short.</p>
<p>“Volume” Reader has successfully read the file “/home/george/test.dcm” “[0.69s]”</p>
<p>Can I “convince” SlicerRT to interpret the input?</p>

---

## Post #5 by @giancu (2018-04-09 17:57 UTC)

<p>Yes I have the extension installed. I am using slicer under Ubuntu.</p>

---

## Post #6 by @cpinter (2018-04-09 18:28 UTC)

<p>Based on the log it seems that you use the Add data dialog. Please use the DICOM browser instead. Click on the DCM button in the top left corner, import your study folder, and load from the patient browser. You need to use the DICOM browser to load all DICOM files.</p>

---

## Post #7 by @giancu (2018-04-10 05:46 UTC)

<p>Yes it did work. Thank you. I tried to visualize a dose distribution recalculated with another TPS, inserting the recalculated dose into the dicom of the original dose. Because of the same IDs the original dose was overwritten in the dicom database…</p>

---

## Post #8 by @gcsharp (2018-04-10 13:20 UTC)

<p>Next time, try generating a new SOP Instance UID for your new dose.  I guess that would allow both objects to appear in the browser.  Good luck!</p>

---
