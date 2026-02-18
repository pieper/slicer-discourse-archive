# Radiomics, image input volume

**Topic ID**: 13329
**Date**: 2020-09-03
**URL**: https://discourse.slicer.org/t/radiomics-image-input-volume/13329

---

## Post #1 by @KLH (2020-09-03 20:08 UTC)

<p>Operating system: Windows 10<br>
Slicer version:4.10.2<br>
Expected behavior: Able to choose a different image input volume<br>
Actual behavior:Can only select one image input volume (first one loaded maybe)</p>
<p>Im new to slicer and radiomics, so apologies if its a simple question. I’m not sure if this is a bug or I just don’t understand, but on the dropdown list of “image input volume” it seems like I should be able to select any volume that I have loaded into the project. (in my case I am using grayscale microscopy .jpeg) and I’d like to compare different image processes to one another. Should I be able to select a different volume in the image input list? There is only my original volume selection available in the dropdown.</p>
<p>My goal is if I make similar (or identical) thresholded segmentations for each version (HE, CLAHE, W/L, Original), I can compare using some radiomics features.  I know this is not how radiomics is normally used, but Im hoping to obtain quantitative comparison of histogram mapping methods.</p>
<p>I suppose I can make a whole new project for each process if I can’t select different image versions before running the tables.<br>
Any help much appreciated.<br>
KH</p>

---

## Post #2 by @lassoan (2020-09-03 21:46 UTC)

<p>Maybe you need to provide a scalar volume as input. You can convert vector (RGB) volume to scalar volume using “Vector to Scalar Volume” module.</p>

---

## Post #5 by @ZHENZC (2021-04-14 11:32 UTC)

<p>Thank to you suggeston, we just solved the obstacle on which we have worked for a month.<br>
Best wishes</p>

---
