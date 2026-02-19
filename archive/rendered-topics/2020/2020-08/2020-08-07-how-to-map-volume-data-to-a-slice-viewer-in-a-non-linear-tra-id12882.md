---
topic_id: 12882
title: "How To Map Volume Data To A Slice Viewer In A Non Linear Tra"
date: 2020-08-07
url: https://discourse.slicer.org/t/12882
---

# How to map volume data to a slice viewer in a non-linear transformation using custom code?

**Topic ID**: 12882
**Date**: 2020-08-07
**URL**: https://discourse.slicer.org/t/how-to-map-volume-data-to-a-slice-viewer-in-a-non-linear-transformation-using-custom-code/12882

---

## Post #1 by @Tesla2687 (2020-08-07 01:17 UTC)

<p>Operating system:Windows 10<br>
Slicer version: 4.11.0<br>
Expected behavior:  How to map volume data to a slice display viewer in a non-linear transformation using custom code?<br>
Actual behavior:</p>
<p>I would like to display a curved slice in Red slice view. This should use a non-linear transformation to do that. Is there any suggestion to do this?<br>
Goal:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39bb32dd4ad59be137055565bfb2be1b7bfe05f2.png" alt="image" data-base62-sha1="8eIhNPE0cDm8K5dYMgqOa2bk8XU" width="515" height="165"></p>
<p>Display the volume upon in a curved style like the volume below by non-linear transform.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24b53c819cab92a20f0028c33a28457a8bc53b1e.jpeg" alt="image" data-base62-sha1="5eJu8iOkShIGU4tjjLLArkyyvKK" width="527" height="187"></p>

---

## Post #2 by @lassoan (2020-08-07 02:57 UTC)

<p>Ultrasound scan conversion can be indeed very efficiently implemented using a grid transform. See for example how it is done in <a href="https://github.com/SlicerHeart/SlicerHeart/tree/master/KretzFileReader">GE Kretz 3D ultrasound reader in SlicerHeart extension</a>.</p>
<p>Note that SlicerHeart extension can import 3D/4D ultrasound data from a wide range of systems. For 2D (and 2D+t) ultrasound scan conversion, you can use <a href="https://www.slicerigt.org">SlicerIGT extension</a> and <a href="https://plustoolkit.github.io/">Plus toolkit</a>.</p>
<p>We can give more information about features that could be useful for you if you write a bit about your project. What is your end goal?</p>

---

## Post #3 by @Tesla2687 (2020-08-09 00:52 UTC)

<p>Thank you very much lassoan.</p>

---
