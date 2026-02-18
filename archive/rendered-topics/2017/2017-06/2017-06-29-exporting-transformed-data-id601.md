# Exporting transformed data

**Topic ID**: 601
**Date**: 2017-06-29
**URL**: https://discourse.slicer.org/t/exporting-transformed-data/601

---

## Post #1 by @faraz1368 (2017-06-29 19:09 UTC)

<p>Operating system: Windows<br>
Slicer version:4.6.2<br>
Expected behavior: Transform location of an ROI (label) and export the transformed data as a DICOM<br>
Actual behavior: Exported ROI is at the same location.</p>
<p>Hello,<br>
I am trying to create ROI on multiple different phases of MRI that are taken at the same time. Since images are not in the same orientation, I need to move the original ROI to align it to subsequent phases. Here is the procedure that I follow.<br>
Create ROI (label-1) via Editor module on the first phase, save DICOM using subject hierarchy. Go to next MRI phase and align the ROI(label-1) to it using transform module. Harden the transform in in data. Resample image using BRAINS module with following specifications:<br>
Image to wrap : label-1<br>
Reference Image: label-1<br>
Output: create new label map as…<br>
Next I export the new output image (which is the transformed label) as a DICOM using subject hierarchy.<br>
Loading both DICOMs to image J, I see the mask at the same location, meaning original ROI got exported not the transformed version.<br>
PS: I am pretty new to Slicer, there might even be an easier way to moving a label and saving it as a new mask.<br>
I also have feel like there could be a problem with the software that I use to lead the DICOMs (Image J), because when I load them to Slicer, the transformation has been applied.<br>
Sincerely<br>
Faraz</p>

---

## Post #2 by @cpinter (2017-06-30 08:48 UTC)

<p>Hi Faraz,</p>
<p>A few suggestions:</p>
<ul>
<li>Please use the latest nightly, there have been many improvements</li>
<li>Use Segment Editor module instead of Editor, it has more advanced functionality, and more robust data handling</li>
</ul>
<p>What DICOM modality are you exporting to? This is very important to know so that we know which exporter you use exactly.</p>

---

## Post #3 by @faraz1368 (2017-06-30 16:58 UTC)

<p>Thank you for your response Csaba,<br>
I use subject hierarchy, I drag the label under the corresponding study and use the default setting to Export DICOM by right clicking on the label.<br>
I will try the nightly version. Meanwhile do you know of any other way that I could do this: Creating a label and exporting it as a mask (DICOM), then moving the label and exporting another mask.<br>
Best<br>
Faraz</p>

---

## Post #4 by @faraz1368 (2017-07-11 17:28 UTC)

<p>Using Resample scalar/vector… module (instead of BRAINS) will allow you to select the transform and apply it to the desired output volume.</p>

---
