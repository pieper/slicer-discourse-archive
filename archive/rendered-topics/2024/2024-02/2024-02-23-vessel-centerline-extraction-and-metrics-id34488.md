---
topic_id: 34488
title: "Vessel Centerline Extraction And Metrics"
date: 2024-02-23
url: https://discourse.slicer.org/t/34488
---

# Vessel centerline extraction and metrics

**Topic ID**: 34488
**Date**: 2024-02-23
**URL**: https://discourse.slicer.org/t/vessel-centerline-extraction-and-metrics/34488

---

## Post #1 by @sampadsengupta (2024-02-23 02:51 UTC)

<p>Hi,</p>
<p>I have CFD results for vascular flow which I am processing and want to correlate geometric factors with haemodynamic metrics.</p>
<p>Is it possible to:<br>
a) automate the computation of a centerline through a vessel for a large number of cases at once?<br>
b) Non-dimenionalise the centerline and then calculate the cross-sectional area along the centerline at regular intervals?</p>
<p>Many thanks in advance for all of your help!</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2024-02-23 02:54 UTC)

<p>Yes, you can compute centerline and get cross-sectional area using modules in VMTK extension.</p>
<p>All features of all modules are available in Python, so you can automate any processing using Puthon scripting.</p>

---

## Post #3 by @sampadsengupta (2024-02-23 12:26 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thank you for your response!</p>
<p>Could you possibly guide me in the direction of the code which would allow for calculating the cross-sectional area along the centerline?  I have been using vmtk on PypePad but I want to transition to using it via scripting, especially since I need to work on it for a large dataset.  Also, the vmtkcenterlinesections command continues to result in errors on PypePad, so ineed to try something else.</p>
<p>Thanks in advance!</p>

---
