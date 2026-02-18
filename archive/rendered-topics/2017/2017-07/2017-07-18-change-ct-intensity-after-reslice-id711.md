# Change CT intensity after Reslice

**Topic ID**: 711
**Date**: 2017-07-18
**URL**: https://discourse.slicer.org/t/change-ct-intensity-after-reslice/711

---

## Post #1 by @Francesco_Sammartino (2017-07-18 21:09 UTC)

<p>Operating system:Linux 64bit<br>
Slicer version:4.7.0-2017-03-21<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2017-07-19 02:59 UTC)

<p>Could you be a bit more specific?</p>
<p>The window width/level (brightness/contrast) is computed for each new volume (even if it was generated from an existing volume). You may have to click-and-drag in the slice viewer to adjust brightness/contrast or go to Volumes module and copy the window width/level from the input volume to make the processed volume look the same as the input.</p>

---

## Post #3 by @Francesco_Sammartino (2017-07-19 13:30 UTC)

<p>Hi Andras thank you so much for replying and apologies for not providing enough details.<br>
Briefly I am using Slicer to realign CT images . After creating a new transform I use the Reslice Scalar/DWI Volume module to apply the transform to the original volume and create a new volume ready to be exported.<br>
Now, the main goal of my analysis is to calculate the average density of the skull bone : so when I calculate the density on the volume after reslicing the intensities are different(they are higher) and this changes the outcome of the density of the bone computation. Is there a way to maintain the intensities or any workaround?</p>
<p>thanks</p>

---

## Post #4 by @Fernando (2017-07-19 22:31 UTC)

<p>Can’t you calculate the density before reslicing?</p>

---

## Post #5 by @pieper (2017-07-19 23:41 UTC)

<p>Are you able to reproduce the issue using data you can share (or using the existing sample data)?  I don’t think the reslicing should change the pixel values, but maybe the way the are displayed as Andras noted.  You can try using the DataProbe to look at the actual values before and after reslicing.</p>

---

## Post #6 by @Francesco_Sammartin1 (2017-07-20 20:40 UTC)

<p>Hi Steve<br>
thank you a lot for your email. I repeated the procedure with the stable<br>
version for Linux and this issue disappeared. At this point I think the<br>
issue was due to an old nightly build version of Slicer.</p>
<p><em>Francesco Sammartino MD</em></p>

---
