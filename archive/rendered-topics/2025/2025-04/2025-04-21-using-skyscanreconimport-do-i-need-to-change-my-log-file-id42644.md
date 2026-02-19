---
topic_id: 42644
title: "Using Skyscanreconimport Do I Need To Change My Log File"
date: 2025-04-21
url: https://discourse.slicer.org/t/42644
---

# Using SkyScanReconImport - do I need to change my .log file?

**Topic ID**: 42644
**Date**: 2025-04-21
**URL**: https://discourse.slicer.org/t/using-skyscanreconimport-do-i-need-to-change-my-log-file/42644

---

## Post #1 by @atay5510 (2025-04-21 11:34 UTC)

<p>I have scanned some specimens on a Bruker SkyScan 2214 MicroCT. I have transferred these scans into a separate computer from the machine I used to acquire the images.</p>
<p>As such, in the .log file, the Home Directory and Data Directory all correspond to a different computer.</p>
<p>If I want to use SkyScanReconImport to upload these images, do I need to edit these .log files to reflect the machine I am running 3D slicer on?</p>
<p>If so, what should go in Home Directory vs. Data Directomy.</p>
<p>Thanks in Advance</p>

---

## Post #2 by @muratmaga (2025-04-21 14:50 UTC)

<p>As long as the _rec.log file and reconstructions are in the same folder, path shouldn’t matter. Let me know if it doesn’t work.</p>

---

## Post #3 by @atay5510 (2025-04-22 08:28 UTC)

<p>That worked perfectly.</p>
<p>Thank you Murat.</p>

---
