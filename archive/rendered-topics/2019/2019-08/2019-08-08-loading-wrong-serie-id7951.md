---
topic_id: 7951
title: "Loading Wrong Serie"
date: 2019-08-08
url: https://discourse.slicer.org/t/7951
---

# Loading wrong serie

**Topic ID**: 7951
**Date**: 2019-08-08
**URL**: https://discourse.slicer.org/t/loading-wrong-serie/7951

---

## Post #1 by @Harlock1978 (2019-08-08 21:43 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.2<br>
Expected behavior:<br>
When I open Dicom Browser and I search a patient writing the Patient ID the right patient is shown and I expect that when clicking load this patient is loaded.<br>
Actual behavior:<br>
Actually when I click load not always the Patient showed is loaded, if you don’t click on. If you have already open other Patients one of the previous loaded Patients is reloaded, not always the last opened.</p>

---

## Post #2 by @pieper (2019-08-09 00:15 UTC)

<p>Hi -</p>
<p>Thanks for the report - I haven’t seen this behavior myself.  Can you replicate this using data you can share or existing public data?</p>

---

## Post #3 by @Harlock1978 (2019-09-04 11:14 UTC)

<p>Sorry for the late answer, I asked but I cannot load my images somewhere.<br>
Here is how I proceed.<br>
I created a directory on a network drive and in these directory I exported a single serie with more or less 1000 images of 47 exams. There 83094 files for 40.9 Gbyte, then I let 3dSlicer create his database.</p>
<p>When I finish my exams I will try to create another directory with so many files on a fressh installation of 3D-Slicer.</p>

---

## Post #4 by @pieper (2019-09-04 12:44 UTC)

<p>Hmm, not sure how to investigate this if we can’t reproduce.  Let us know how your further experiments go, especially if you have any hints about potentially erroneous behavior.</p>

---
