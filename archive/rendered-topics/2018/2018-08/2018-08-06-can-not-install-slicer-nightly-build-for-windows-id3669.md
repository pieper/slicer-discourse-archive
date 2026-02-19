---
topic_id: 3669
title: "Can Not Install Slicer Nightly Build For Windows"
date: 2018-08-06
url: https://discourse.slicer.org/t/3669
---

# Can not install slicer nightly build for windows

**Topic ID**: 3669
**Date**: 2018-08-06
**URL**: https://discourse.slicer.org/t/can-not-install-slicer-nightly-build-for-windows/3669

---

## Post #1 by @daniJb (2018-08-06 12:30 UTC)

<p>Hi, I am trying to get the latest slicer nightly build running on my machine in order to test the VR component. The exe file throws an error and won’t start with the installation. Apprecaite any help in this.</p>
<p>Operating system: Windows 10 Pro<br>
Slicer version: Slicer-4.9.0-2018-08-04-win-amd64<br>
Expected behavior: install and launch!<br>
Actual behavior: issues an NSIS error “Installer integrity check has failed. Common causes include incomplete download and damaged media. Contact the installer’s author to obtain a new copy”</p>

---

## Post #2 by @lassoan (2018-08-06 12:43 UTC)

<p>I’ve tested the latest (2018-08-04) Windows package and it worked without any issues.</p>
<p>Most likely the file download was incomplete (you tried to download over slow or unreliable network connection, etc.). If you try again, maybe via a better connection, then the download should be successful.</p>

---

## Post #3 by @daniJb (2018-08-06 15:32 UTC)

<p>yup…it was a faulty download. my bad. I followed the instructions here <a href="https://www.instructables.com/id/How-to-Solve-NSIS-error/" rel="nofollow noopener">https://www.instructables.com/id/How-to-Solve-NSIS-error/</a><br>
now the installer is working.<br>
Thanks</p>

---
