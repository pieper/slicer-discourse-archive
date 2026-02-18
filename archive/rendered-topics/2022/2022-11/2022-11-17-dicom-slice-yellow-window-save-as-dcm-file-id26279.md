# DICOM Slice (yellow window) save as .dcm file?

**Topic ID**: 26279
**Date**: 2022-11-17
**URL**: https://discourse.slicer.org/t/dicom-slice-yellow-window-save-as-dcm-file/26279

---

## Post #1 by @OJay (2022-11-17 10:14 UTC)

<p>Hi <span class="mention">@all</span>,</p>
<p>how can i save a DICOM Slice (yellow window) as a .dcm file?</p>
<p>Thanks for your help!<br>
Ole</p>

---

## Post #2 by @pieper (2022-11-17 19:55 UTC)

<p>You can use Orient Scalar Volume to rearrange the pixels and the export the result to dicom.</p>

---

## Post #3 by @OJay (2022-11-17 20:59 UTC)

<p>i´ve try it but cant get the sagittal slice (yellow) exported as .dcm file. Can you help me please?</p>
<p>Thank you!<br>
Ole</p>

---

## Post #4 by @pieper (2022-11-17 23:37 UTC)

<p>Here are the basic steps - you should be able to find tutorials and documentation that explain each step but if there’s a specific step you don’t understand post back with what you tried and what didn’t work as you expected:</p>
<ol>
<li>load your volume using the DICOM module</li>
<li>go to the Orient Scalar Volume module and pick Sagittal conversion, pick your input volume and create a new output volume, then click Apply</li>
<li>in the Data module right click the output volume and choose to export to DICOM</li>
</ol>

---
