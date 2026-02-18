# Calculate angular displacement of rotated DICOM data

**Topic ID**: 7794
**Date**: 2019-07-29
**URL**: https://discourse.slicer.org/t/calculate-angular-displacement-of-rotated-dicom-data/7794

---

## Post #1 by @Manuel (2019-07-29 04:53 UTC)

<p>Hey there,</p>
<p>I would need to know the procedure (mathematical calculations) how to calculate the angular displacement (axis x, y and z) of rotated DICOM data. I already know that it is possible to access the image axis directions in RAS coordinate system from the volume, but I would need the direct calculation only out of the DICOM attributes. I also already know that the attribute (0020, 0037) “ImageOrientationPatient” includes the x and y vectors of the image and z can be calculated with the cross product of x and y. Is there also another attribute necessary to calculate the angles?</p>
<p>Thank you in advanced for any help.<br>
Manuel</p>

---

## Post #2 by @lassoan (2019-07-29 18:34 UTC)

<p>ImageOrientationPatient tag everything you need to compute image axis angles relative to patient axes. There are several parametrizations available for computing angles between coordinate systems. <a href="https://en.wikipedia.org/wiki/Euler_angles" rel="nofollow noopener">Euler angles wikipedia page</a> gives a nice summary and also formulae that you can use to compute rotation angles from axis vectors.</p>

---

## Post #3 by @Manuel (2019-07-29 18:57 UTC)

<p>Perfect. It’s good to know that only the attribute is needed to calculate the angles. Then I’m not too far off with my approach.<br>
Thank you very much for your help.</p>

---
