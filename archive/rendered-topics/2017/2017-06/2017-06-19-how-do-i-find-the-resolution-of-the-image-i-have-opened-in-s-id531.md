# How do I find the resolution of the image I have opened in slicer?

**Topic ID**: 531
**Date**: 2017-06-19
**URL**: https://discourse.slicer.org/t/how-do-i-find-the-resolution-of-the-image-i-have-opened-in-slicer/531

---

## Post #1 by @Josiah_McAllister (2017-06-19 19:00 UTC)

<p>Operating system:Windows 7<br>
Slicer version:4.6.2<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @ihnorton (2017-06-19 19:25 UTC)

<p>Use the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Volumes">Volumes</a> module – see the first tab “Volume Information” for pixel and spacing information.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/327d7aa93f011535ae9d8ddcab45d1b6f2db1a47.png" alt="image" data-base62-sha1="7cEI6qNnoUyese44nQi8l0kaELl" width="308" height="30"></p>

---

## Post #3 by @Josiah_McAllister (2017-06-19 19:42 UTC)

<p>Is the image origin the pixels?</p>

---

## Post #4 by @lassoan (2017-06-19 19:51 UTC)

<p>Origin is in defined in the world (RAS) coordinate system, which is usually in mm. If you import from standard DICOM data sets then the unit it is always in mm.</p>

---
