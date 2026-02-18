# Segmentation wizard installation

**Topic ID**: 17635
**Date**: 2021-05-15
**URL**: https://discourse.slicer.org/t/segmentation-wizard-installation/17635

---

## Post #1 by @RO786 (2021-05-15 22:09 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.2020</p>
<p>Hello</p>
<p>I tried to download the segmentation wizard module using the extension browser. It does not successfully install after restarting the software. I get a note saying it has not loaded. Is there any way I can get this extension for slicer 4.11.2020?</p>
<p>Many thanks</p>

---

## Post #2 by @lassoan (2021-05-16 00:46 UTC)

<p>As far as I remember, this extension just makes a few steps of a very specific segmentation workflow a little bit more convenient. I would recommend to use Segment Editor module instead. If you have any questions about how to segment something then let us know.</p>

---

## Post #3 by @RO786 (2021-05-16 16:52 UTC)

<p>Thank you. I have developed a method using segmentation wizard so would be keen to try an add this extension if possible? But if not, I will of course try segment editor. Thank you very much for your help</p>

---

## Post #4 by @lassoan (2021-05-16 20:31 UTC)

<p>Can you describe your workflow?based on that we could decide if it is worth spending time with reviving Segmentation Wizard, or it is simpler to just use core modules.</p>

---

## Post #5 by @RO786 (2021-05-17 09:23 UTC)

<p>My workflow involves DICOM load, ROI mark up in axial and coronal images (the zoom tool is particularly helpful at areas of PVE), thresholding, paint and erase pixels on review, save segmentation and import threshold ROI to label statistics for volume calculation.<br>
It’s a very easy and pretty fast method for the large dataset. I wanted to avoid re-segmenting everything so far if possible. The 4.11.2020 has a lovely way of displaying the scans and series in ‘loaded data’ which is easy to flick between and view. In 4.8 I don’t have this feature and have to repeatedly switch between examine and load data to find the correct series which takes a bit of time. I was hoping to combine the best of both worlds<br>
Thank you very much for all your help</p>

---

## Post #6 by @lassoan (2021-05-17 13:02 UTC)

<p>All the steps that you described are very simple to do in recent Slicer versions, without using any extensions.</p>
<p>You don’t need to segment anything again. When you load a labelmap volume, in “Add data” window’s Description column choose “Segmentation”.</p>
<p>You can learn more about segmentation <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">here</a>.</p>

---

## Post #7 by @RO786 (2021-05-17 16:06 UTC)

<p>Thank you very much!</p>

---
