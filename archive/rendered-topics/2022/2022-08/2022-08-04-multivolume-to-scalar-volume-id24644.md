---
topic_id: 24644
title: "Multivolume To Scalar Volume"
date: 2022-08-04
url: https://discourse.slicer.org/t/24644
---

# Multivolume to Scalar Volume

**Topic ID**: 24644
**Date**: 2022-08-04
**URL**: https://discourse.slicer.org/t/multivolume-to-scalar-volume/24644

---

## Post #1 by @PaoloZaffino (2022-08-04 14:55 UTC)

<p>Hi all,<br>
Slicer reads a CBCT as a multi-volume, even if it contains just a single scan.<br>
How can I convert it into a scalar volume?</p>
<p>Thanks a lot.<br>
Paolo</p>

---

## Post #2 by @cpinter (2022-08-04 15:02 UTC)

<p>Hi Paolo,</p>
<p>I think you could try to select a different importer. Check Advanced in the DICOM browser and see in the list which loadables are selected. If they are of the MultiVolume importer, uncheck them and choose the Scalar Volume one.</p>

---

## Post #3 by @PaoloZaffino (2022-08-04 15:12 UTC)

<p>Hi <a class="mention" href="/u/cpinter">@cpinter</a>,<br>
thanks for the quick reply.</p>
<p>I see just the multivolume reader…</p>

---

## Post #4 by @PaoloZaffino (2022-08-04 15:13 UTC)

<p>if it can help: plastimatch converts it without any problem.</p>

---

## Post #5 by @lassoan (2022-08-04 15:24 UTC)

<p>CBCTs still pretty often create non-standard, randomly broken DICOM images. Some common issues can be fixed by running them through the DICOM patcher. If we find that some cases are not covered by that then we can add a DICOM importer plugin that exposes some Plastimatch readers (or add the logic from Plastimatch to an existing DICOM reader plugin).</p>
<p>If you share the problematic image (upload to dropbox or OneDrive and post the link here) then I can have a look.</p>

---

## Post #6 by @PaoloZaffino (2022-08-05 12:17 UTC)

<p>That’s strange:<br>
the first scan is ok (scalar volume), the second scan is a series.<br>
This happens for whatever patient if I have more than a scan.</p>
<p>I’ll investigate better with the manufacturer, I think I can not share the data sorry (I don’t have the permission).</p>
<p>However, I think it is a scanner-side problem, not a slicer-related one.</p>
<p>Thanks a lot,<br>
Paolo.</p>

---
