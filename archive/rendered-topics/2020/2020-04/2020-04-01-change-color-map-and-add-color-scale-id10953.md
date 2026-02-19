---
topic_id: 10953
title: "Change Color Map And Add Color Scale"
date: 2020-04-01
url: https://discourse.slicer.org/t/10953
---

# Change Color map and add color scale

**Topic ID**: 10953
**Date**: 2020-04-01
**URL**: https://discourse.slicer.org/t/change-color-map-and-add-color-scale/10953

---

## Post #1 by @Adam1122 (2020-04-01 11:26 UTC)

<p>Hello all,</p>
<p>I did the post-processing on brain images in 3D Slicer. I changed the color coding to display where MR signals values are higher or lower. I need to add the color bar onto the image in order to easily identify what “blue” or “red” color means. Please, in which program is it possible to change the color map and to add the color bar as well? I didn´t manage to do it in 3D Slicer.</p>
<p>Thanks a lot</p>
<p>Regards</p>
<p>Adam</p>

---

## Post #2 by @lassoan (2020-04-01 14:06 UTC)

<p>You can do this all in Slicer.</p>
<p>Edit color table: Go to colors module, choose a color node that you would like to modify, click “Copy” button to create an editable copy (the default color nodes are read-only). If you choose a “color table” type of node (this is the most common) then you get hundreds of predefined colors and you can modify each by double-clicking the color swatch in the color column, which can be tedious if you want to make large changes. It may be more convenient to modify “Continuous” color node, such as “RedGreenBlue” because you can specify a few colors at arbitrary levels and the colors are interpolated between them.</p>
<p>Show scalar bar:</p>
<ul>
<li>Slice views: go to DataProbe module, check “Enable slice view annotations”, check Scalar bar / Enable</li>
<li>3D views: go to Colors module, clone the color table that you use for the volume, set the same min/max range as you have set for your volume, and check Scalar bar / Display scalar bar</li>
</ul>

---

## Post #3 by @Adam1122 (2020-04-01 18:23 UTC)

<p>I´m working in the Slice view. In the colors module I set the color map and its range. In the colors module I check “Display Scalar bar” and the color range appears but in the 3D views. I would need to add the color scale to the slice views. How can I do it? Moreover, do I have to save separaetely the image and the color range or can one save the image and the color range at the same time?</p>
<p>Thanks a lot<br>
Regards<br>
Adam</p>

---

## Post #4 by @jamesobutler (2020-04-01 19:02 UTC)

<aside class="quote no-group" data-username="Adam1122" data-post="3" data-topic="10953">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/df788c/48.png" class="avatar"> Adam1122:</div>
<blockquote>
<p>I would need to add the color scale to the slice views. How can I do it?</p>
</blockquote>
</aside>
<p>The details from the above post provide the answer to this see below. You can also read → <a href="https://discourse.slicer.org/t/color-bar-in-slice-viewers/6291" class="inline-onebox">Color bar in slice viewers</a></p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="10953">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Show scalar bar:</p>
<ul>
<li>Slice views: go to DataProbe module, check “Enable slice view annotations”, check Scalar bar / Enable</li>
</ul>
</blockquote>
</aside>
<p>If you are wanting to create an image for a presentation or something you can use the “Screen Capture” module to generate an image that includes your image + scalar bar .</p>

---

## Post #5 by @Adam1122 (2020-04-02 19:15 UTC)

<p>thanks a lot. In the Colors module I modify the color table but how can I apply it on the image. I´ve just found it in the “Volumes” module. How can I apply my modified color table onto my image?</p>

---

## Post #6 by @lassoan (2020-04-04 20:46 UTC)

<p>You can create editable versions of built-in lookup tables or color maps in the Colors module. See details <a href="https://discourse.slicer.org/t/change-color-map-and-add-color-scale/10953/2">above</a>.</p>
<p>You can choose which color node is used for displaying a volume in Volumes module.</p>

---

## Post #7 by @Saima (2022-05-11 03:54 UTC)

<p>Hi Andras,<br>
Is it possibel to change the color scalar bar, colors table?</p>
<p>Also how to get the colour table from a model? and use it to change the colour scalar bar colour table?</p>
<p>Also how to set the foreground and background image using scripting for all the views (red, yellow green)?</p>
<p>thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #8 by @lassoan (2022-05-11 19:47 UTC)

<p>Color legends has been completely reworked recently in Slicer-4.13. Everything should be simpler and more intuitive and documented here:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/search.html?q=Legend" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/search.html?q=Legend</a></p>

---
