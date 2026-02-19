---
topic_id: 17043
title: "How Do I Use Getlogbiasfieldasimage In C"
date: 2021-04-12
url: https://discourse.slicer.org/t/17043
---

# How do I use GetLogBiasFieldAsImage in c#?

**Topic ID**: 17043
**Date**: 2021-04-12
**URL**: https://discourse.slicer.org/t/how-do-i-use-getlogbiasfieldasimage-in-c/17043

---

## Post #1 by @Tami (2021-04-12 17:51 UTC)

<p>Operating system:window10<br>
Slicer version:4.10.2<br>
I have the N4BiasFieldCorrectionImageFilter implemented in c# (visual studio) and it is working correctly and improving images.<br>
However, I need to use a ShrinkFactor higher than 1, so I need to use the method: GetLogBiasFieldAsImage() in order to recover the full-resolution, filtered, image.<br>
But when I call this method I get the following compilation error:<br>
“‘N4BiasFieldCorrectionImageFilter’ does not contain a definition for ‘GetLogBiasFieldAsImage’ and no accessible extension method…”<br>
What can cause this method to be missing?<br>
Any hint would be helpful (I hope)…</p>

---

## Post #2 by @lassoan (2021-04-14 05:13 UTC)

<p>GetLogBiasFieldAsImage is not an ITK feature but it is added by SimpleITK in a very recent release. It is already available in latest Slicer Preview Release.</p>
<p>However, it may be simpler to use “N4ITK MRI bias correction” module, which takes care shrinking and applying the field to the full-resolution image. You can run it from Python as described <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_to_run_CLI_module_from_Python.3F">here</a>.</p>

---

## Post #3 by @Tami (2021-04-14 08:04 UTC)

<p>Thank you for your answer! I need to incorporate the GetLogBiasFieldAsImage into a c# code. So should I download that recent release of simpleITK that you mention? If you recommend, then what version is it and where should I download it from?</p>

---

## Post #4 by @lassoan (2021-04-14 14:04 UTC)

<p>Here we give help to SimpleITK users in Slicer’s Python environment. You need to ask SimpleITK developers about their C# wrappings.</p>

---

## Post #5 by @Tami (2021-04-15 08:23 UTC)

<p>I did that now and got an answer. Thank you for your advice!</p>

---

## Post #6 by @lassoan (2021-04-18 03:56 UTC)

<p>For reference, the question was answered <a href="https://discourse.itk.org/t/method-getlogbiasfieldasimage-missing-in-n4biasfieldcorrection-c-implementation/4033/4">here</a>.</p>

---
