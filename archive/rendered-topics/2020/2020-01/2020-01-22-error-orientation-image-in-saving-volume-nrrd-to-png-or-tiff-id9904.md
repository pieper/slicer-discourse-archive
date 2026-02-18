# Error Orientation image in saving volume (nrrd) to png or tiff

**Topic ID**: 9904
**Date**: 2020-01-22
**URL**: https://discourse.slicer.org/t/error-orientation-image-in-saving-volume-nrrd-to-png-or-tiff/9904

---

## Post #1 by @carlos-luque (2020-01-22 10:02 UTC)

<p>Hello everyone,</p>
<p>I found a issue that is  when a volume saves in png or tiff, the orientation is different than the original volume orientation.<br>
I checked the IKJtoRAS matrix in module volume and it is identity matrix. I don´t know where I can fix this issue.</p>
<p>I am using the 3D slicer version 4.11 (2020-01-08) in windons 10 and I downloaded the a nrrd and a png in this link <a href="https://bit.ly/2RhJ0Hx" rel="nofollow noopener">https://bit.ly/2RhJ0Hx</a>. I think they can be useful.</p>
<p>Thanks in advance.</p>

---

## Post #2 by @pieper (2020-01-22 10:25 UTC)

<p>yes, that’s to be expected - the nrrd file stores the image orientation in the header, while the png and tiff files don’t have any established way to store that information.  The suggestion would be to use nrrd for cases where you need to preserve the orientation.</p>

---

## Post #3 by @carlos-luque (2020-01-22 10:47 UTC)

<p>I expect the png and tiff images have the same orientation as the orientation volume, when the png or tiff image is generated from the volume.<br>
I don´t know why the image orientation is different and  I cannot use the nrrd file for our objectives</p>

---

## Post #4 by @pieper (2020-01-23 17:50 UTC)

<p>After talking with Carlos we determined that the PLUS server needs to be configured to send the same orientation as given when loading a png file in Slicer from the Add Data dialog (negative one on the first two elements on the diagonal).</p>

---

## Post #5 by @lassoan (2020-01-24 10:01 UTC)

<p>Thanks for sharing the results. This behavior is due that .png file format cannot save IJK to LPS matrix in the file, therefore a .png file is always assumed to have IJKToLPS=identity, which is equivalent to IJKtoRAS=diag(-1,-1,1,1).</p>

---
