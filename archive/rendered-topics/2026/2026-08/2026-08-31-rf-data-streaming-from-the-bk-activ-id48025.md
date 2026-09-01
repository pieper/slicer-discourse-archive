---
topic_id: 48025
title: "RF data streaming from the BK Activ"
date: 2026-08-31
url: https://discourse.slicer.org/t/48025
last_bumped: 2026-08-31T19:26:01.994Z
---

# RF data streaming from the BK Activ

**Topic ID**: 48025
**Date**: 2026-08-31
**URL**: https://discourse.slicer.org/t/rf-data-streaming-from-the-bk-activ/48025

---

## Post #1 by @J.vd.Zee (2026-08-31 08:54 UTC)

<p>We would like to perform research on the raw RF data acquired with a BK Activ ultrasound scanner, with the aim of developing and evaluating methods for improving ultrasound image quality. Could anyone advise us on:</p>
<ul>
<li>which hardware and/or software interfaces are required to access and stream the RF data from a BK Activ scanner;</li>
<li>whether RF data can be streamed directly from the scanner, rather than only the reconstructed B-mode images;</li>
<li>Existing BK Activ → PLUS → 3D Slicer data-streaming workflow  still supported is and up to date?</li>
</ul>
<p>We have found previous examples/documentation describing BK ultrasound integration with PLUS, but we are unsure whether these approaches are still applicable to the current BK Activ systems. Any advice, documentation, examples, or experience with accessing RF data from BK Activ would be greatly appreciated.</p>

---

## Post #2 by @pieper (2026-08-31 14:37 UTC)

<p>In the past we found that special research agreements were needed in order to access the BK RF data.  It would be great if this has changed (I haven’t been involved of over a decade).  If you can get the data in a format you can process, you might find <a href="https://github.com/KitwareMedical/ITKUltrasound" class="inline-onebox">GitHub - KitwareMedical/ITKUltrasound: ITK module with classes particularly useful for ultrasound. · GitHub</a> helpful.</p>

---

## Post #3 by @lassoan (2026-08-31 19:26 UTC)

<p>In earlier BK systems that we worked with:</p>
<ul>
<li>you can connect without research agreement to the OEM interface to grab frames one by one; it is quite slow (few frames per second)</li>
<li>with an extra license, you can activate continuous streaming via the OEM interface, which allows full-speed data acquisition (tens of frames per second)</li>
<li>BK interface for RF data acquisition requires special hardware (CameraLink capture card), research agreement, and most likely it only works on older models (ProFocus)</li>
</ul>
<p>See more details here: <a href="https://pluslib.readthedocs.io/en/latest/devices/DeviceBkProFocus.html" class="inline-onebox">BK ultrasound systems — PlusLib 2.9 documentation</a></p>
<p>There is a good chance that the OEM interface still works with newer models and hopefully a streaming option is available, but you need to confirm this with your BK representative.</p>

---
