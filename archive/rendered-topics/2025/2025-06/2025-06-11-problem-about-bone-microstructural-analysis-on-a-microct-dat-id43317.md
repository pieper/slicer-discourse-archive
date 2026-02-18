# Problem About Bone Microstructural Analysis on a  MicroCt Data

**Topic ID**: 43317
**Date**: 2025-06-11
**URL**: https://discourse.slicer.org/t/problem-about-bone-microstructural-analysis-on-a-microct-data/43317

---

## Post #1 by @TAHA_KOSE (2025-06-11 15:59 UTC)

<p>I am trying to perform trabecular separation, trabecular thickness, trabecular number and bone volume/tissue volume analyses on an irregularly shaped segmented area on the microct dataset. While I am getting normal values ​​on the CBCT data, the program does not give any results on the microct data. Do you think there is a problem with my dataset or am I doing something wrong? Can anyone help? Thank you</p>

---

## Post #2 by @muratmaga (2025-06-12 04:54 UTC)

<p>You need to give more information. What extension are you using to calculate those values? And what do you mean by “program does not give any results on the microct data”? What program?</p>

---

## Post #3 by @TAHA_KOSE (2025-06-12 06:58 UTC)

<p>I am using 3D Slicer V. 5.8.1 with BoneTexture extension. First of all, I create a segment, then go to segment editor and select the area of bone between the roots of rats 1st molar. I create a threshold to select the mineralized area of bone. Then go to segmentations section and exporting a new label map. After that go to BoneTexture extension and select input volume and input labelmap. Then choice the GLCM, GLRLM and BM features. Clicking populate parameters based on inputs and last of it click the compute texture feature set.The results coming for the GLCM features and , GLRLM features but even after a long wait no values for the BM features (Bone Volume Dentisty, Trabecular Thickness, Trabecular Seperation, Trabecular Number) which i want to calculate. The percentage of the load area stuck at %66.<br>
Sorry I am new to this type of bone analysis on micro ct, what I am doing wrong or what I am missing? Is there any other steps?</p>
<p>Murat Maga via 3D Slicer Community &lt;<a href="mailto:notifications@slicer.discoursemail.com">notifications@slicer.discoursemail.com</a>&gt;, 12 Haz 2025 Per, 07:54 tarihinde şunu yazdı:</p>

---

## Post #4 by @muratmaga (2025-06-12 15:42 UTC)

<p>So steps you describe workflow works for a CBCT, but not a microCT? Is that correct?</p>
<p>MicroCT datasets are often much higher resolution than CBCT. Maybe you are hitting memory limitation. Perhaps downsample your original volume (using Crop Volume) and start fresh.</p>
<p>Also if you hit CTRL+0 (CMD in mac) you can get the log file, and see if there are any errors reported.</p>

---

## Post #5 by @TAHA_KOSE (2025-06-23 12:32 UTC)

<p>Thank you for the support. I couldn’t make it with 3D slicer after also cropping the volume. I made the assessment at ImageJ with BoneJ extension.</p>

---
