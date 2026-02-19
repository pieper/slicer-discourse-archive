---
topic_id: 32082
title: "Installing Slicerjupyter Causes Slicer To Crash"
date: 2023-10-06
url: https://discourse.slicer.org/t/32082
---

# Installing SlicerJupyter causes Slicer to crash

**Topic ID**: 32082
**Date**: 2023-10-06
**URL**: https://discourse.slicer.org/t/installing-slicerjupyter-causes-slicer-to-crash/32082

---

## Post #1 by @smrolfe (2023-10-06 21:35 UTC)

<p>When I install SlicerJupyter on my MacBook (OS Monterey, 12.5.1) and restart, the application repeatedly crashes during launch. I can fix this by deleting the extension files from the application.</p>
<p>I have tried this for the nightly preview and a fresh install of the stable version of Slicer. I’m not able to replicate this on an older Mac in our lab, so it is likely specific to my setup.</p>

---

## Post #2 by @pieper (2023-10-06 21:43 UTC)

<p>It’s probably this issue again <a href="https://discourse.slicer.org/t/the-dependency-dicomrtimportexport-failed-to-be-loaded-slicerrt-issue/32073/2" class="inline-onebox">The dependency "DicomRtImportExport" failed to be loaded - SlicerRT Issue - #2 by pieper</a></p>
<p>It may take a few days to fix the mac extensions for the current release.</p>

---

## Post #3 by @Viktor (2023-11-28 10:56 UTC)

<p>Are there any news on this topic?<br>
I have the same issue on my macbook (Apple M2, Sonoma 14.1.1) since Slicer 5.4.0.</p>
<p>I also tried to install the SlicerRT extension, without success. Although slicer does not crash, a lot of error messages appear and the extension does not load.</p>

---

## Post #4 by @maximeb (2024-04-16 15:58 UTC)

<p>Hi! I have recently (april 2024) downloaded 3DSlicer. When I tried to install the jupyslicer extension, the app Slicer crashed each time (if the folder of the extension was deleted, the app worked again). As recommended above and in or other forum, I downloaded an older version (5.2.2) and now jupyslicer works. Probably there is a bug in the new stable release that has not been fixed?</p>

---
