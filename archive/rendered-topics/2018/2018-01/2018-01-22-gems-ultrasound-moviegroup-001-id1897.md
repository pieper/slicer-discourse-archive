---
topic_id: 1897
title: "Gems Ultrasound Moviegroup 001"
date: 2018-01-22
url: https://discourse.slicer.org/t/1897
---

# GEMS_Ultrasound_MovieGroup_001

**Topic ID**: 1897
**Date**: 2018-01-22
**URL**: https://discourse.slicer.org/t/gems-ultrasound-moviegroup-001/1897

---

## Post #1 by @Manzoor_Patel (2018-01-22 14:15 UTC)

<p>Operating system: macOS Sierra<br>
Slicer version: 4.8.1</p>
<p>Hello Guys,</p>
<p>I have a US modality DICOM image which appears to contain the 3D/4D data stored in Spherical or Cylindrical co-ordinates in a private tag (raw-data). The binary string of this data has series of “GEMS_Ultrasound_MovieGroup_001” segments.</p>
<p>I am trying to use Slicer to convert this data sets to cartesian system, don’t seem to be heading in the right direction. Any thoughts would be helpful.</p>
<p>Thanks for any help.</p>
<p>-MP</p>

---

## Post #2 by @pieper (2018-01-22 14:37 UTC)

<p>I don’t know of any solutions for that particular case.  It’s possible that the company has made it difficult to convert on purpose.  If anyone were to try writing a converter it would really help if you have shareable data (for example a phantom) with both the original non-cartesian data along with some screenshots of what the images should look like.</p>

---

## Post #3 by @lassoan (2018-01-24 05:18 UTC)

<p>It may be a KretzFile ultrasound sequence. Can you find the word <code>Kretz</code> in any of the files? If yes, then <a href="https://github.com/SlicerHeart/SlicerHeart/tree/master/KretzFileReader">SlicerHeart extension’s GE Kretz ultrasound reader</a> may be able to read it or the reader can be tuned so that it can read it.</p>

---

## Post #4 by @Manzoor_Patel (2018-01-24 15:23 UTC)

<p>Nope, I don’t see word “Kretz” anywhere in the file.</p>
<p>-Manzoor Patel</p>

---

## Post #5 by @lassoan (2018-01-24 15:35 UTC)

<p>Unfortunately, we only have solution for reading GE 3D/4D ultrasound files that are stored in Kretz format. Newer systems use proprietary compressed image data that only GE knows how to interpret. You may contact GE for converter software that can export this data to formats that can be read by third-party software.</p>
<p>Some time ago we discussed with GE about accessing their 3D/4D image data from our software, but open solution was not an option, so we did not go for it (they would have required signing us a non-disclosure agreement, so we could not make the reader publicly available).</p>
<p>Philips systems have an exporter software (QLab) that can save 3D/4D images to DICOM files that other tools, such as 3D Slicer can import. So, we use Philips systems for all 3D/4D ultrasound image acquisition.</p>

---

## Post #6 by @ButuiHu (2018-10-27 09:39 UTC)

<p>Hey, keyword “GEMS_Ultrasound_MovieGroup_001” lead me here. Any new suggestion? I got a DVD from hospital. DICOM image contains multiple 2D frames ultrasound image (2D + t). I wonder if there are some free converter to export those data to real DICOM file? It seems that <a href="http://tomovision.com/products/dicomatic.html" rel="nofollow noopener">DICOMatic</a> could export to DICOM format, but with expensive cost.</p>

---

## Post #7 by @ButuiHu (2018-10-28 07:19 UTC)

<p>Hey, I found that maybe <a href="http://gdcm.sourceforge.net" rel="nofollow noopener">gdcm</a> could help. There is a example might help, <a href="https://github.com/malaterre/GDCM/blob/master/Examples/Cxx/GetSubSequenceData.cxx" rel="nofollow noopener">GetSubSequenceData</a>.<br>
However, in my case, this example doesn’t work at all. The image size is wrong. The real size is 434x636, while it give me 207x496.</p>

---

## Post #8 by @lassoan (2018-10-28 14:08 UTC)

<p>Slicer can load ultrasound image sequence from GE “moviegroup” DICOM files if you install SlicerHeart extension. See <a href="https://github.com/SlicerHeart/SlicerHeart">SlicerHeart extension documentation</a> for details.</p>

---
