# General Registration won't recognize a series 

**Topic ID**: 7224
**Date**: 2019-06-18
**URL**: https://discourse.slicer.org/t/general-registration-wont-recognize-a-series/7224

---

## Post #1 by @jwatson (2019-06-18 20:52 UTC)

<p>Hello,</p>
<p>I am trying to co-register two different sequences from the same patient in Slicer, however, only one of the sequences is being recognized in the drop down menu for the fixed and moving images. I can select both sequences as volumes in other modules, but the registration does not display one of the sequences. Any hep is much appreciated.</p>

---

## Post #2 by @lassoan (2019-06-18 21:10 UTC)

<p>What is the volume type? You can find it in Volumes module. It can be Scalar, Vector, Tensor, etc.</p>
<p>If it is a vector volume then use Vector to Scalar volume module to convert to scalar volume.</p>

---

## Post #3 by @jwatson (2019-06-18 22:11 UTC)

<p>On the vector to scalar module it won’t let me click the ‘Input Vector Volume’ drop down. It lets me select an output scale volume but not an input.</p>

---

## Post #4 by @lassoan (2019-06-18 22:40 UTC)

<p>What is the volume type of the two volumes? You can find it in Volumes module. It can be Scalar, Vector, Tensor, etc.</p>

---

## Post #5 by @jwatson (2019-06-21 00:59 UTC)

<p>It says its an ‘MRMLMulti’ volume</p>

---

## Post #6 by @jwatson (2019-06-21 01:28 UTC)

<p>I tried to resample using the ‘Resample scalar/vector/DWI Volume’ module (input: the image, output: a newly created volume, reference volume: another scalar volume), but the output image is only a single slice and not an entire volume.</p>

---

## Post #7 by @lassoan (2019-06-21 01:42 UTC)

<aside class="quote no-group" data-username="jwatson" data-post="5" data-topic="7224" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/e47c2d/48.png" class="avatar"> jwatson:</div>
<blockquote>
<p>It says its an ‘MRMLMulti’ volume</p>
</blockquote>
</aside>
<p>This means that the image is a time series. Most likely a single slice, changing in time.</p>

---

## Post #8 by @jwatson (2019-06-21 01:45 UTC)

<p>Its a T2-weighted structural image – I’m not sure why it would read it as a time series … is there any way to convert it to a scalar volume?</p>

---

## Post #9 by @pieper (2019-06-21 11:01 UTC)

<p>Depending on your data it might work to turn off the multivolume plugin and select scalar volume explicitly using the advanced dicom import option.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/DICOM" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/Modules/DICOM</a></p>

---

## Post #10 by @jwatson (2019-06-21 17:48 UTC)

<p>That worked, thank you very much!</p>

---
