---
topic_id: 23054
title: "New User Loading Non Dicom Data"
date: 2022-04-20
url: https://discourse.slicer.org/t/23054
---

# New user: Loading non-dicom data

**Topic ID**: 23054
**Date**: 2022-04-20
**URL**: https://discourse.slicer.org/t/new-user-loading-non-dicom-data/23054

---

## Post #1 by @CamRiddle22 (2022-04-20 16:18 UTC)

<p>Hi Slicer community. I am an undergraduate student assisting in research and I am brand new to 3D modeling. Our research involves scans of fish and we have 10 or so folders with the scan data. The only downside that I have seen is that none of the files are in .dcm format. Instead, they are in .tif or .png files. When I try to load this non-dicom data, the application ends up crashing and I have only been able to load around 500 png’s at a time. Does anyone have any advice on possibly how to convert png to another file type or useful extensions?<br>
Thanks!</p>
<ul>
<li>Cam</li>
</ul>

---

## Post #2 by @hherhold (2022-04-20 16:19 UTC)

<p>TIFF and PNG files should work fine. How much memory, what kind of CPU, etc?</p>

---

## Post #3 by @CamRiddle22 (2022-04-20 16:33 UTC)

<p>3.92 GB of PNG’s</p>
<p>Processor Intel(R) Xeon(R) Gold 6240R CPU @ 2.40GHz   2.39 GHz<br>
32 GB ram</p>

---

## Post #4 by @hherhold (2022-04-20 16:34 UTC)

<p>OK, that should work. How many PNG files, and what are their dimensions? (i.e., what are the dimensions of your stack)?</p>

---

## Post #5 by @CamRiddle22 (2022-04-20 16:36 UTC)

<p>There are 2,973 png’s</p>
<p>If by dimensions you mean pixels it is 2436 x 2088.</p>

---

## Post #6 by @pieper (2022-04-20 17:24 UTC)

<p>You can try the ImageStacks module in SlicerMorph: <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks" class="inline-onebox">SlicerMorph/Docs/ImageStacks at master · SlicerMorph/SlicerMorph · GitHub</a>.  It was designed for this purpose and allows you to subset or resample the data while loading to save memory.</p>

---

## Post #7 by @hherhold (2022-04-20 17:26 UTC)

<p>I’d highly recommend Steve <a class="mention" href="/u/pieper">@pieper</a>’s suggestion. ImageStacks works great.</p>

---

## Post #8 by @CamRiddle22 (2022-04-20 19:03 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/hherhold">@hherhold</a></p>
<p>I will give SlicerMorph a try and let you know how it goes. I appreciate your fast and knowledgeable replies!</p>

---
