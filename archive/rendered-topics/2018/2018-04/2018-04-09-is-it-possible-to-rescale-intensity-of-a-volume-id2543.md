---
topic_id: 2543
title: "Is It Possible To Rescale Intensity Of A Volume"
date: 2018-04-09
url: https://discourse.slicer.org/t/2543
---

# Is it possible to rescale intensity of a volume?

**Topic ID**: 2543
**Date**: 2018-04-09
**URL**: https://discourse.slicer.org/t/is-it-possible-to-rescale-intensity-of-a-volume/2543

---

## Post #1 by @Alex_Vergara (2018-04-09 16:01 UTC)

<p>I want to rescale a Volume created reading a wrongly calibrated dicom file. Is this possible?</p>
<p>Usually this is automatically done with the RescaleIntercept and RescaleSlope from the dicom header but when those values are wrong or missing then I need to do this manually.</p>

---

## Post #2 by @pieper (2018-04-09 17:09 UTC)

<p>You can modify the pixel values directly:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Accessing_Volume_data_as_numpy_array" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Accessing_Volume_data_as_numpy_array</a></p>

---

## Post #3 by @gcsharp (2018-04-09 17:52 UTC)

<p>Hi Alex,</p>
<p>I have one idea how to do this.  Download the “ImageMaker” module.  Create two images: one with the desired offset, and one with the desired scale.  Then use the “Add Volume” and “Multiply Volume” modules in the “Filter” menu to adjust your image.</p>
<p>Of course, any better idea is welcome J</p>
<p>Greg</p>

---

## Post #4 by @Hamburgerfinger (2018-04-09 18:10 UTC)

<p>The easiest way to do this IMO is use the “ShiftScaleImageFilter” from the Simple Filters module.  Just enter your correction factor as the scale factor.</p>

---

## Post #5 by @sfglio (2020-07-11 16:26 UTC)

<p>Does this also apply for the calibration of CBCT to MDCT?</p>
<p>I have a CBCT and MDCT of the same specimen and I want to “convert” the grey values in CBCT accordingly the ones in MDCT and consequently be able to measure “HU” values in the CBCT volume?</p>
<p>How can I calculate the correction factor?</p>

---
