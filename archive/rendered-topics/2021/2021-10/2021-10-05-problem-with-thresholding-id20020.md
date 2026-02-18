# Problem with Thresholding 

**Topic ID**: 20020
**Date**: 2021-10-05
**URL**: https://discourse.slicer.org/t/problem-with-thresholding/20020

---

## Post #1 by @Elie_Massaad (2021-10-05 12:16 UTC)

<p>I am having a problem with the thresholding option.<br>
I am trying to segment the CT spine - after loading the DICOM - The threshold option gives a range of -1024 to 1024 and it is impossible to change the range.<br>
I was working fine in the last couple of days. I think the problem started after updating my mac to latest BigSur update release.<br>
I am using the latest version of 3d slicer!<br>
Could</p>

---

## Post #2 by @lassoan (2021-10-05 16:06 UTC)

<p>Is this the threshold range shown in Volumes module or in Segment Editor module?<br>
Which Slicer version do you use?</p>

---

## Post #3 by @Elie_Massaad (2021-10-04 22:47 UTC)

<p>Operating system:MacOSBigsur<br>
Slicer version:4.13.0-2021-10-03 r30282 / 04d69cd<br>
Expected behavior: The range of values for thresholding needs to show up to be able too threshold bone from CT spine<br>
Actual behavior: I can’t change the thresholding bars. The values seen are from -1024 to -1024. It does not seem to read the range of values in the DICOMs. I have tried many files. Having the same problem.</p>

---

## Post #4 by @Elie_Massaad (2021-10-05 16:51 UTC)

<p>Hello Andras,<br>
It is showing in the Segment Editor module.<br>
I am using the latest version 4.13.0 of October 4, 2021.<br>
I noticed that this problem appeared after I updated my mac to the latest BigSur release. Before that, I did not have any problems. Also, I am having a problem re-analyzing the DICOMs I analyzed a few days ago. So the problem is new.<br>
I tried on Windows with the same imaging data, and everything works fine.<br>
I think what is happening on mac, is that the software is detecting the ranges in the black area outside the actual image - most probably only air as HU is -1024.</p>

---

## Post #5 by @Elie_Massaad (2021-10-05 17:53 UTC)

<p>Thank you, Andras, I think I solved the problem by creating a new segmentation and then loading the master volume.<br>
if any problem comes up in the future, I will let you know.<br>
Thanks<br>
Elie</p>

---

## Post #6 by @pieper (2021-10-05 18:32 UTC)

<p>That does not sound like a problem related to the operating system, but if you ever see issues that appear to be OS dependent let us know how to reproduce and we can test out on various machines.</p>

---
