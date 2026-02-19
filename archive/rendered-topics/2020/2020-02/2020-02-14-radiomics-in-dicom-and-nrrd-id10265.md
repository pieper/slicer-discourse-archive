---
topic_id: 10265
title: "Radiomics In Dicom And Nrrd"
date: 2020-02-14
url: https://discourse.slicer.org/t/10265
---

# Radiomics in dicom and nrrd

**Topic ID**: 10265
**Date**: 2020-02-14
**URL**: https://discourse.slicer.org/t/radiomics-in-dicom-and-nrrd/10265

---

## Post #1 by @tenzin_kunkyab (2020-02-14 18:38 UTC)

<p>Hi,</p>
<p>I am doing a small radiomics study on clinical patients. The way I did it is imported dicom via “Load Data” in 3d Slicer and then saved the volume and segmentation as nrrd files. After that I did a batch processing. So I compared the feature values with Load dicom and then extracted features directly from Slicer 3D. Some of the features are quite different (even doubling the values), I tried then importing to nrrd again and using python script to extract features it is again different from one from 3D slicer. So the feature values depend on which format I used to extract from? which one is the correct way, is it because some infomration is lost in converting to nrrd format?</p>
<p>best<br>
Tenzin</p>

---

## Post #2 by @tenzin_kunkyab (2020-02-14 23:06 UTC)

<p>I mean majority sample cases are same but one or two comes of with different feature values (one or two patients).</p>

---

## Post #3 by @timeanddoctor (2020-02-15 03:40 UTC)

<p>If you went covert the DICOM. I thinke the best way is using the DICOM module to load the DICOM datas and then save as a NRRD files</p>

---

## Post #4 by @lassoan (2020-02-15 18:54 UTC)

<p>As you can see from <a href="https://discourse.slicer.org/tag/radiomics">radiomics questions posted on this forum</a>, there are radiomics features that tend to be very sensitive to how exactly they are computed. If you want to use these sensitive features then you need to get to know them very well, understand what parameters are needed to compute them, make a decision on how to determine those parameters, and ensure that you consistently follow your established rules.</p>
<p>If you give more specific information then (which features you have the problem with, what values do you get, on what images, etc.) then you may be able to get more specific help.</p>

---

## Post #5 by @JoostJM (2020-02-18 09:30 UTC)

<p>In addition to <a class="mention" href="/u/lassoan">@lassoan</a>’s great points, I’d like to point out that both PyRadiomics batch processing, as it’s implementation in Slicer includes a load of diagnostic features as part of the standard output. These include information both on the exact input used, as well as software versions and the configuration used in the extraction. It’s therefore is a great place to start to investigate any differences.</p>
<p>If you want more in-depth info on the extraction process itself, carefully read the (extensive) <a>documentation</a>, and extract using logging (potentially on DEBUG level).</p>

---
