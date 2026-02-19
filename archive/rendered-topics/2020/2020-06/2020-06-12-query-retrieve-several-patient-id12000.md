---
topic_id: 12000
title: "Query Retrieve Several Patient"
date: 2020-06-12
url: https://discourse.slicer.org/t/12000
---

# query retrieve several patient

**Topic ID**: 12000
**Date**: 2020-06-12
**URL**: https://discourse.slicer.org/t/query-retrieve-several-patient/12000

---

## Post #1 by @cyrina (2020-06-12 15:22 UTC)

<p>Hello</p>
<p>I try to retrieve several Patient at once but it seems impossible or am I doing something wrong ?<br>
I select with ctrl several patient in the “form” window and click on retrieve but only one is retrieve and my logs seems to say there is only one that is asked<br>
So I wonder if it really the case or if I am doing something wrong…</p>
<p>I would like to be able to load several patient at once</p>
<p>Have a great day !<br>
Cyrina</p>

---

## Post #2 by @lassoan (2020-06-12 15:44 UTC)

<p>There is no retrieve queue implemented in DICOM module’s Query/Retrieve. It would not be that hard to implement, but there has not been much interest in this feature. For transferring DICOM data sets in bulk, using DICOM files is by far the most common method, so most efforts have been focused on optimizing that.</p>
<p>Network transfer is used sometimes, but even then it is more common to use DICOM push (C-STORE) from the clinical workstation and use Slicer’s DICOM listener to receive it, rather than query it from Slicer.</p>

---
