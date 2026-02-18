# Calibrating Ruler for JPEG Measurements

**Topic ID**: 30818
**Date**: 2023-07-26
**URL**: https://discourse.slicer.org/t/calibrating-ruler-for-jpeg-measurements/30818

---

## Post #1 by @charlotte.jw (2023-07-26 21:57 UTC)

<p>Hi there,</p>
<p>I’m completely new to slicer and need a very simple distance measurement from the program but am unsure how to do so. I will be uploading JPEG images of cadaveric specimens with a ruler in the photo for scale. How do I calibrate the program to match the scale of the ruler in the photo so that I can use the line tool and have the measurements be accurate?</p>
<p>Thanks in advance.</p>

---

## Post #2 by @pieper (2023-07-28 14:50 UTC)

<p>By default, formats like jpg with no image geometry info will be assumed to be 1mm/pixel.  So you can measure a known feature of the image (ruler) with a Markup Line to get the size in pixels.  Then divide the known number size of the feature in mm by the number of pixels to get the mm/pixel.  This is called the Spacing, and it can be entered in the Volume Information section of the Volumes module.  Probably it’s the same in plane, and if you have multiple slices you may need to extend this analysis since they spacing in Z may not be equal.  Once you have done the calibration save in a format like nrrd that preserves the spacing in the header.</p>

---
