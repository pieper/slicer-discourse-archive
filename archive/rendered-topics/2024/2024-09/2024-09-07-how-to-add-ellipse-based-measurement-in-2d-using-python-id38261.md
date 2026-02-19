---
topic_id: 38261
title: "How To Add Ellipse Based Measurement In 2D Using Python"
date: 2024-09-07
url: https://discourse.slicer.org/t/38261
---

# How to add "ellipse" based measurement in 2D using Python?

**Topic ID**: 38261
**Date**: 2024-09-07
**URL**: https://discourse.slicer.org/t/how-to-add-ellipse-based-measurement-in-2d-using-python/38261

---

## Post #1 by @Saladi (2024-09-07 11:05 UTC)

<p>Hello Community,<br>
We are trying to make some measurements on Ultrasound data using ellipse. I have tried using various extensions but I was able to find ellipsoid only. I need an 2D ellipse <em>markup</em> preferably in Python, as our developed module is in Python. Any leads will be highly appreciated.<br>
Thanks!</p>

---

## Post #2 by @chir.set (2024-09-07 11:26 UTC)

<aside class="quote no-group" data-username="Saladi" data-post="1" data-topic="38261">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/saladi/48/77856_2.png" class="avatar"> Saladi:</div>
<blockquote>
<p>various extensions</p>
</blockquote>
</aside>
<p>You may consider the <a href="https://github.com/chir-set/SlicerExtraMarkups" rel="noopener nofollow ugc">ExtraMarkups</a> extension <em>if you have not considered it yet</em>.</p>
<p>It allows to draw many shapes including a Ellipsoid using 4 markups points. After reslicing a slice view along a chosen axis, 3 points get co-planar in this view, you may then resize at will. Since you work in 2D, only the measured radii will be relevant. If the ellipse area in the slice view is what you need, you’ll have to calculate it on your own.</p>
<p>Like anything in Slicer, the API is available in Python.</p>

---

## Post #3 by @Saladi (2024-09-07 11:30 UTC)

<p>Hi,<br>
I need to make multiple measurements and having ellipsoid for every measurement is overlapping with each other, and it is making the volume too Overcrowding.<br>
Also I only need the circumference of the ellipse</p>

---
