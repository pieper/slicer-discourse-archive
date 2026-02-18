# Can you change the dimensions of an image?

**Topic ID**: 38292
**Date**: 2024-09-09
**URL**: https://discourse.slicer.org/t/can-you-change-the-dimensions-of-an-image/38292

---

## Post #1 by @Daniel_Murcia (2024-09-09 13:48 UTC)

<p>Good morning, dear 3D slicer community.</p>
<p>I want to know if the attached values ​​in the image can be changed, if they can I would like to know how to do it.</p>
<p>thank you very much for your help.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62508e887696843e642683e1961c1cf18a37f931.png" alt="Screenshot 2024-09-09 084535" data-base62-sha1="e1JnOOzJZvNkUBDC0eIFOr0hmMx" width="495" height="488"></p>

---

## Post #2 by @pieper (2024-09-09 14:30 UTC)

<p>Those numbers describe the size of your volume, so you can’t change them directly.  You can resample the volume, e.g. with the CropVolume module.</p>

---
