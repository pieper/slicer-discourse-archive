---
topic_id: 14368
title: "Using Slicer Via Web Service Api"
date: 2020-11-01
url: https://discourse.slicer.org/t/14368
---

# Using Slicer via web service API

**Topic ID**: 14368
**Date**: 2020-11-01
**URL**: https://discourse.slicer.org/t/using-slicer-via-web-service-api/14368

---

## Post #1 by @puia (2020-11-01 13:43 UTC)

<p>hello<br>
i am new to this software and my research is under going and i and the end i found what i need here .<br>
a stack of 2d images out of a 3d stl image .<br>
i am implementing an web app in order to work with 3d stl file , in order to provide a machine learning model with a series of 2d images .</p>
<p>this is what i need to know :<br>
is there any way to use the 3Dslicer as an API service ?<br>
in order to use it should i install the decstop software ?</p>
<p>tnx</p>

---

## Post #2 by @puia (2020-11-01 15:41 UTC)

<p>Hello</p>
<p>I am researching to find a way to have a collection of 2d images from a single 3d .stl object in order to use that collection of 2d images for training a machine learning model.</p>
<ul>
<li>first : can i use the 3Dslicer as an API service , which means my app sends the stl image to the service and in return get the result as a collection of 2d images ? ( slices of the 3d object )</li>
<li>even 2d images from different angles would be solution  . ( 20 images from different angles )</li>
</ul>
<p>tnx</p>

---

## Post #3 by @lassoan (2020-11-01 19:27 UTC)

<p>Since you can use any Python packages in Slicer, it is relatively easy to expose any features via web services. See an example here: <a href="https://github.com/pieper/SlicerWeb">https://github.com/pieper/SlicerWeb</a>.</p>

---
