---
topic_id: 34326
title: "Error Given When Trying To Screen Capture A Binary Label Map"
date: 2024-02-14
url: https://discourse.slicer.org/t/34326
---

# Error given when trying to screen capture a binary label map

**Topic ID**: 34326
**Date**: 2024-02-14
**URL**: https://discourse.slicer.org/t/error-given-when-trying-to-screen-capture-a-binary-label-map/34326

---

## Post #1 by @M_finlayson (2024-02-14 14:35 UTC)

<p>I am trying to create an image stack of a binary label map, I have created the map but when I try to make the image stack by using the screen capture module I receive and error stating “not all arguments converted during string formatting” I am not sure why this is happening as I have done this before without issue but now I am getting this error</p>

---

## Post #2 by @lassoan (2024-02-14 14:42 UTC)

<p>It sounds like an error related to recent internationalization efforts of Slicer (we had to change some string formattings to make Slcier translatable to different languages).</p>
<p>What Slicer version do you use? What is the full error message (including filename and line number)?<br>
Do you use the LanguagePacks extension and non-English application language?</p>

---
