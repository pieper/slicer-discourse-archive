---
topic_id: 3219
title: "How Do I Setup The Local Pacs Server On Slicer"
date: 2018-06-18
url: https://discourse.slicer.org/t/3219
---

# How do I setup the local PACS server on SLICER

**Topic ID**: 3219
**Date**: 2018-06-18
**URL**: https://discourse.slicer.org/t/how-do-i-setup-the-local-pacs-server-on-slicer/3219

---

## Post #1 by @JamesGalea (2018-06-18 19:09 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.9.0<br>
Expected behavior: Normal<br>
Actual behavior: Normal</p>
<p>I am a relative newbie when I come to PACS. I have managed to setup the correct file server to query. How do I setup the local PACS Dicom database on my PC so that the scans I query can retreived? The defaults are CTKSTORE  and STORAGE PORT 11112… Any ideas or online tutorials?</p>

---

## Post #2 by @pieper (2018-06-19 13:23 UTC)

<p>Hi -</p>
<p>A good place to start is to read up on <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM">DICOM</a> and use, for example, the command line tools in DCMTK to confirm all the settings (IP addresses, ports, AE titles…) for your network environment.  Once you know that, configuring them in Slicer should be pretty straightforward.  Here are <a href="https://discourse.slicer.org/t/dicom-pacs-does-retrieve-but-series-do-not-show-in-browser/2012">some</a> <a href="https://discourse.slicer.org/t/query-and-retrieve/378/4">posts</a> that should help.</p>

---

## Post #3 by @Robert_Leo (2019-12-05 12:18 UTC)

<p>Thanks for sharing this information!! It’s useful</p>

---
