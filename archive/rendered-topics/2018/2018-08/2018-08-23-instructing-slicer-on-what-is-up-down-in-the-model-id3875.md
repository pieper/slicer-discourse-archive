# Instructing Slicer on what is up/down in the model

**Topic ID**: 3875
**Date**: 2018-08-23
**URL**: https://discourse.slicer.org/t/instructing-slicer-on-what-is-up-down-in-the-model/3875

---

## Post #1 by @Trident (2018-08-23 19:30 UTC)

<p>Dear Slicer Users!</p>
<p>I am currently segmenting the pelvis of a woman and I realised that in my model Slicer has a wrong Z axis on my data. In short, Slicer thinks what is cranial/up is actually caudal/down and that results in my segmentations to be left instead of right etc. (see Image: In my Segmentation the M. psoas major is actually on the left in the axial view but it shows it as right on the 3D model or the Aorta is actually on the right when it should be on the left)</p>
<p>Is there a way to retroactively correct that Z axis? So that Slicer then turns my model around in the right way?</p>
<p>Thanks in advance,</p>
<p>Adrian</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c53db1402545ea7e6f09f8acdaaf115f679fa7f.jpeg" data-download-href="/uploads/short-url/k1ovnbavQLrIqp5n2mrqKCN1l1B.jpeg?dl=1" title="Z%20Axis" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c53db1402545ea7e6f09f8acdaaf115f679fa7f_2_690x388.jpeg" alt="Z%20Axis" data-base62-sha1="k1ovnbavQLrIqp5n2mrqKCN1l1B" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c53db1402545ea7e6f09f8acdaaf115f679fa7f_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c53db1402545ea7e6f09f8acdaaf115f679fa7f_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c53db1402545ea7e6f09f8acdaaf115f679fa7f_2_1380x776.jpeg 2x" data-dominant-color="8C8078"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Z%20Axis</span><span class="informations">2560×1440 1.37 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @cpinter (2018-08-23 19:44 UTC)

<p>What is the format of the dataset that you loaded? Is it DICOM, NRRD, etc?</p>
<p>As a tip, if you turn back on the “3D axis label” for the 3D view then you can immediately see which direction is where.</p>

---

## Post #3 by @lassoan (2018-08-24 13:40 UTC)

<p>You can change orientation of any node by creating a linear transform, apply the transform to selected nodes, and adjusting the transform using sliders (using Transforms module).</p>

---

## Post #4 by @Fernando (2018-08-24 23:54 UTC)

<p>The orientation marker on your 3D view indicates that the Superior axis points downwards. You just need to rotate the camera of the 3D view with your mouse.</p>

---

## Post #5 by @Trident (2018-08-25 20:19 UTC)

<p>So my original format is a 4GB Dicom File.<br>
The issue is not that I don’t know which direction it’s facing. The actual issue is that my coordinates are sort of wrong. I wan’t my image to stay the same but I want to change the coordinate system around it, but only partly so. The changes I want are:<br>
Up and Down to switch around. (S-Axis)<br>
Left and Right to stay the same. (R-Axis)<br>
Front and Back to stay the same. (A-Axis)<br>
The problem I with the linear transfroms is that it changes all my axis and I can’t simply change one of the 3.</p>
<p>Thank you already for your help.</p>

---

## Post #6 by @cpinter (2018-08-25 21:31 UTC)

<p>Thanks for the explanation!</p>
<p>Changing only one axis is a flipping, and it will change the coordinate system of your image from right-handed to left-handed. How was that DICOM acquired? Is there any tag in the DICOM file that describes the coordinate system? If you can do a dcmdump with DCMTK and paste the metadata tags here that would help.</p>

---
