---
topic_id: 48692
title: "Volume Sequence broken in 5.12?"
date: 2026-11-03
url: https://discourse.slicer.org/t/48692
last_bumped: 2026-11-04T18:19:57.127Z
---

# Volume Sequence broken in 5.12?

**Topic ID**: 48692
**Date**: 2026-11-03
**URL**: https://discourse.slicer.org/t/volume-sequence-broken-in-5-12/48692

---

## Post #1 by @coffee (2026-11-03 17:39 UTC)

<p>Hello,</p>
<p>I’m working with a 3D+time CT DICOM dataset (which unfortunately I cannot upload on account of it being patient data) in Windows, and in versions 5.12.0 and 5.12.4 I do not see the Volume Sequence show up as an option after running Examine. MultiVolume is the only option, and it doesn’t actually allow different phases to be examined. Jumping back down to 5.10.0 Volume Sequence shows up (in addition to MultiVolume) and everything is good. I can see that DICOMVolumeSequencePlugin is installed in 5.12.x, so wondered if this was a new bug.</p>
<p>Thank you.</p>

---

## Post #2 by @mhouse (2026-11-04 18:19 UTC)

<p>Yes there is an issue of the 5.12.4 version, both with Windows and Linux. You can use the preview version for this. For me it shows then Volume Sequence and MultiVolume in the DICOM Data column. The Reader is MultiVolume for both.</p>

---
