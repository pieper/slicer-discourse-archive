---
topic_id: 25894
title: "Registration Discussion"
date: 2022-10-25
url: https://discourse.slicer.org/t/25894
---

# Registration discussion

**Topic ID**: 25894
**Date**: 2022-10-25
**URL**: https://discourse.slicer.org/t/registration-discussion/25894

---

## Post #1 by @jay1987 (2022-10-25 12:53 UTC)

<p>I’ve watched the demonstration of the BrainLab Elements and Medtronic Stealth software. Their registration methods are so amazing that can finish the registration in about 5~8 seconds and the registration result is very good. Has anyone known about articles or materials involved in the registration?</p>

---

## Post #2 by @pieper (2022-10-25 15:42 UTC)

<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/registration.html</a></p>

---

## Post #3 by @jay1987 (2022-10-26 08:09 UTC)

<p>thank you pieper<br>
slicerants seems don’t support Slicer4.11version now</p>

---

## Post #4 by @pieper (2022-10-26 11:20 UTC)

<p>There are many registration tools for Slicer.  Did they not work for your use case?  Try the latest release 5.0.3.</p>

---

## Post #5 by @jay1987 (2022-10-26 12:18 UTC)

<p>i tryed brainsfit and elastix,it works very well,registration result is very good . the only disadvantage is the registation time is too long,when i set brainsfit sample rate to 0.1 , it takes 50s more .</p>

---

## Post #6 by @pieper (2022-10-26 16:13 UTC)

<p>Ah, okay, thanks for the context.  Probably posting to the ITK forum or the specific tool issue pages could give you suggestions.  Slicer’s tools tend to be general purpose where Brainlab probably optimizes a lot.  Maybe there are ways to speed up the ITK-based tools if you use the right parameters.</p>

---

## Post #7 by @jay1987 (2022-10-27 02:32 UTC)

<p>thank you very much pieper.</p>

---

## Post #8 by @lassoan (2022-10-27 03:10 UTC)

<p>Rigid registration on CPU typically takes 10-20 seconds. You may need to tighten up some registration settings to achieve this - tune the number of samples, maximum iterations, various stopping conditions, skip generation of a resampled output image, etc.</p>
<p>In most workflows, this computation time is short enough that decreasing it any further would not make a practical difference, and it is very convenient that users don’t need to have any special hardware. However, if you have a strong GPU and you need faster registration then you can build Elastix with GPU acceleration enabled (maybe you need to build ITK with GPU support, too) and then registration may complete within a few seconds.</p>

---

## Post #9 by @jay1987 (2022-10-27 03:23 UTC)

<p>thank you very much lassoan<br>
sometimes I am wondering if where exist a registration method that can use GPU to perform Rigid registration work to speed up the process.<br>
try elastix GPU version is a good solution<br>
tighten up some registration settings will make the registration result not good enough to do Surgical planning, Therefore, it is necessary to balance the registration time and accuracy</p>

---
