---
topic_id: 3360
title: "Editor Function And Ukf Tractography"
date: 2018-07-03
url: https://discourse.slicer.org/t/3360
---

# Editor Function and UKF tractography 

**Topic ID**: 3360
**Date**: 2018-07-03
**URL**: https://discourse.slicer.org/t/editor-function-and-ukf-tractography/3360

---

## Post #1 by @eclataurora (2018-07-03 00:29 UTC)

<p>Hi everyone,</p>
<p>I am currently trying to visualize and compare tracts going through the right and left corticospinal tract. I used the Per-Structure Volume tab and added the two structures, going by the code that they came with (085 for right corticospinal tract, and 086 for left corticospinal tract). After I made the region of interests, I wanted to process them under UKF tractography. However, I get the following error:<br>
UKF Tractography standard error:</p>
<p><strong>UKFTractography: ITK ExceptionObject caught!</strong></p>
<p><strong>itk::ExceptionObject (0x107219520)</strong><br>
**Location: “unknown” **<br>
<strong>File: /Users/kitware/Dashboards/Stable/S-481-E-b/UKFTractography/ukf/tractography.cc</strong><br>
<strong>Line: 223</strong><br>
<strong>Description: itk::ERROR: No matching label ROI seeds found! Please verify label selection.</strong></p>
<p>What was it that I did wrong? How can I remedy this? Thanks.</p>

---

## Post #2 by @ljod (2018-07-03 19:25 UTC)

<p>It looks like the label number that was entered into the module does not match any label in the ROI image. Usually labelmaps do not use labels like 085, so perhaps that label is interpreted as 85. You can check by hovering your mouse cursor over it and seeing what label value shows to the left in the data probe. If it shows as 85, then you know that is the value to use. (Or just try entering 85 and see if it works in UKF.) Another possibility is that if you are using the Segment Editor, you need to convert your segmentation to a labelmap.</p>

---

## Post #3 by @eclataurora (2018-07-06 18:36 UTC)

<p>Great! Thank you so much for your help!</p>

---

## Post #4 by @ljod (2018-07-06 20:28 UTC)

<p>You’re welcome. Please let us know if it worked for you and what you did. This way we and future users can have useful information.</p>

---

## Post #5 by @eclataurora (2018-07-09 19:57 UTC)

<p>So I used the Fiber Bundle Selection and Scalar Measurement tutorial as a guide. I did a whole brain tractography with UKF first and then made regions of interest using the different colors for the structures whole taking not of the numbers that I used. Afterwards, in order to get my tracts, I used THOSE NUMBERS in my Tractography ROI selections.</p>

---
