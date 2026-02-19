---
topic_id: 34269
title: "Imported Nrrt Image Not Being Imported In The Correct Anatom"
date: 2024-02-12
url: https://discourse.slicer.org/t/34269
---

# Imported nrrt image not being imported in the correct anatomical orientation. 

**Topic ID**: 34269
**Date**: 2024-02-12
**URL**: https://discourse.slicer.org/t/imported-nrrt-image-not-being-imported-in-the-correct-anatomical-orientation/34269

---

## Post #1 by @cscanla (2024-02-12 21:48 UTC)

<p>I have a set of CT scans in a nrrd format. Half of them import correctly, in the orientation below:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7ba5e264945d370aee521bfffec79f5fc37ba2ae.png" alt="image" data-base62-sha1="hDQ8kMPgaOwWefNk5DGCmB9oQhg" width="477" height="315"></p>
<p>However, the other half of my images are being imported upside down. I have checked the way my images look in ImageJ to ensure that the original image is not upside down. When I first open 3D Slicer, the images look like this:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd7c2712ce5fad1ddd270c3e55305fc284eb158d.jpeg" alt="image" data-base62-sha1="tjNSo3EQHZJs7LPgRbvLVjiQhTn" width="477" height="375"></p>
<p>My goal is to use Total Segmentator to conduct a total segmentation. When I use the transform or the reformat modules, I am able to rotate the image, but Total Segmentator fails. The module segments according to the way the image was originally imported. The segmentations don’t align with the rotated image. How can I fix this issue?</p>
<p>I cannot share my own images so I provided ones that describe how my images are being imported.</p>

---

## Post #2 by @pieper (2024-02-13 01:44 UTC)

<p>The nrrd files must have incorrect headers - you could revisit how they were created and see how they ended up this way.</p>

---
