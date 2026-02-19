---
topic_id: 2752
title: "How To Open Analyze Format Files In Slicer"
date: 2018-05-03
url: https://discourse.slicer.org/t/2752
---

# How to open Analyze format files in Slicer

**Topic ID**: 2752
**Date**: 2018-05-03
**URL**: https://discourse.slicer.org/t/how-to-open-analyze-format-files-in-slicer/2752

---

## Post #1 by @drusmanbashir (2018-05-03 10:33 UTC)

<p>Hi,<br>
I have a series of files saved as separate .img and .hdr files (analyze). When i load them using add data dialog, i get an error:</p>
<p>‘Could not read scalar volme using DCMTK / GDCM appraoch Error is fileformat’</p>
<p>Any tips?</p>

---

## Post #2 by @pieper (2018-05-03 12:36 UTC)

<p>You only need to select the .hdr file and it should find the corresponding .img file automatically.  If that doesn’t work let us know.</p>

---

## Post #3 by @drusmanbashir (2018-05-04 08:45 UTC)

<p>Unfortunately, still nothing happens. I am wondering if the analyze files are to blame or something in the API</p>

---

## Post #4 by @drusmanbashir (2018-05-04 08:48 UTC)

<p>It may well be the images because ITK-snap is also unable to open them.</p>

---
