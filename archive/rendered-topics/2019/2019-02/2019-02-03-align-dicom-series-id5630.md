# Align dicom series

**Topic ID**: 5630
**Date**: 2019-02-03
**URL**: https://discourse.slicer.org/t/align-dicom-series/5630

---

## Post #1 by @Stweie (2019-02-03 17:52 UTC)

<p>Hello Everyone,<br>
I am fairly new to CT image. I am struggling with coordinate transformation. I have data of the same patient with following details:</p>
<p>Series 1<br>
‘ImagePositionPatient’,<br>
[’-205.0966796875’, ‘-384.0966796875’, ‘-1496.5’]<br>
‘Pixelspacing’,[‘0.806640625’, ‘0.806640625’]<br>
slice Thickness’ 2mm<br>
Image Orientation (Patient)[‘1’, ‘0’, ‘0’, ‘0’, ‘1’, ‘0’]</p>
<p>Series 2<br>
‘ImagePositionPatient’,<br>
[’-171.650390625’, ‘-356.650390625’, ‘-1099.7’]<br>
‘Pixelspacing’, [‘0.69921875’, ‘0.69921875’]<br>
‘slice Thickness’, 2mm<br>
Image Orientation (Patient)[‘1’, ‘0’, ‘0’, ‘0’, ‘1’, ‘0’]<br>
In both series slices are of  512*512 in size</p>
<p>What I want to do is translate coordinates of series 1 to coordinates of series 2 and vice versa. I know this can be done by interpolation. But I want to know what would be the affine transformation matrix to do that job ? I tried to formulate but failed.<br>
Any code example in python or the formula would be great help.<br>
Thanks a lot in advance.</p>

---

## Post #2 by @lassoan (2019-02-03 19:41 UTC)

<p>This page may help in getting started: <a href="https://www.slicer.org/wiki/Coordinate_systems" rel="nofollow noopener">https://www.slicer.org/wiki/Coordinate_systems</a></p>

---

## Post #3 by @Stweie (2019-02-03 19:45 UTC)

<p>I have already read. Converted nifti to dicom coordinate. But now trying to align one dicom to another dicom series. To do that how can I construct the transformation matrix  ?</p>

---

## Post #4 by @lassoan (2019-02-04 12:11 UTC)

<p>You can compute transformation between physical coordinate system of images by using any of the registration modules, such as:</p>
<ul>
<li>intensity-based registration (e.g., General registration (BRAINS) module)</li>
<li>landmark-based registration (e.g., Fiducial Registration Wizard module in SlicerIGT extension)</li>
<li>segmentation based registration (Segment Registration module in SegmentRegistration extension)</li>
</ul>

---
