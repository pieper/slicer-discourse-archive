---
topic_id: 47939
title: "TotalSegmentator Extension failed to install req. package"
date: 2026-08-20
url: https://discourse.slicer.org/t/47939
last_bumped: 2026-08-21T13:44:25.001Z
---

# TotalSegmentator Extension failed to install req. package

**Topic ID**: 47939
**Date**: 2026-08-20
**URL**: https://discourse.slicer.org/t/totalsegmentator-extension-failed-to-install-req-package/47939

---

## Post #1 by @dumichgh (2026-08-20 19:05 UTC)

<p>Problem report for Slicer 5.6.2 win-amd64:</p>
<p>When trying to run a TotalSeg got an “error” and process halted :</p>
<p>Failed to install required packages.</p>
<p>Command ‘[‘C:/Users/XXXX/AppData/Local/slicer.org/Slicer 5.6.2/bin/../bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘dicom2nifti’]’ returned non-zero exit status 1.</p>
<p>Suspect that the problem may be having  “back-slash” in the path for PythonSlicer.EXE on Windows machine.</p>
<p>Is there a workaround to run the TotalSegmentator?</p>

---

## Post #2 by @Thibault_Pelletier (2026-08-21 05:47 UTC)

<p>Hi <a class="mention" href="/u/dumichgh">@dumichgh</a>,</p>
<p>You are running a pretty old Slicer version (with outdated / unsupported Python version).<br>
I would suggest trying with the <a href="https://download.slicer.org/" rel="noopener nofollow ugc">latest stable  3D Slicer version (5.12.3)</a>.</p>
<p>Best,<br>
Thibault</p>

---

## Post #3 by @dumichgh (2026-08-21 13:44 UTC)

<p>Thank you, Thibault,</p>
<p>We tried 5.12.3 first, however, Extension Manager was not launching, so went down in version until found one that launched the Manager…  Will try fixing the 5.12.3 issue, --Dariya</p>

---
