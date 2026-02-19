---
topic_id: 4510
title: "Documented Threshold Values For Various Body Parts"
date: 2018-10-23
url: https://discourse.slicer.org/t/4510
---

# Documented threshold values for various body parts

**Topic ID**: 4510
**Date**: 2018-10-23
**URL**: https://discourse.slicer.org/t/documented-threshold-values-for-various-body-parts/4510

---

## Post #1 by @EricWilson (2018-10-23 18:22 UTC)

<p>Hello,</p>
<p>Is there some kind of documentation about exactly what threshold values to use on various body parts to get the best segments?</p>
<p>if there is, how accurate is it, can it easily and cleanly separate things like skin, liver, heart and various organ tissues?</p>

---

## Post #2 by @pieper (2018-10-23 18:46 UTC)

<p>No sorry, it’s not exactly paint-by-numbers <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>If you are working with CT, <a href="https://en.wikipedia.org/wiki/Hounsfield_scale">this scale might help.</a>  If you are working with MR then mostly the images are not in physical units and only relative intensity values are meaningful.</p>

---

## Post #3 by @EricWilson (2018-10-23 19:32 UTC)

<p>I was afraid it would be an inexact science.</p>
<p>in that case, how would you do something like creating an accurate segment from a CT scan of a heart that has a hole in the side?</p>

---

## Post #4 by @pieper (2018-10-23 19:46 UTC)

<p>You could start with the tutorials - the second one on this list shows how to do a nice heart segmentation pretty quickly:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/Training#Slicer4_Image_Segmentation" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.10/Training#Slicer4_Image_Segmentation</a></p>

---
