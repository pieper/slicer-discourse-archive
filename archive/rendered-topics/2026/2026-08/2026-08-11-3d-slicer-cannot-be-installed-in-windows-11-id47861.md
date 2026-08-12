---
topic_id: 47861
title: "3D Slicer cannot be installed in Windows 11"
date: 2026-08-11
url: https://discourse.slicer.org/t/47861
last_bumped: 2026-08-12T03:17:56.042Z
---

# 3D Slicer cannot be installed in Windows 11

**Topic ID**: 47861
**Date**: 2026-08-11
**URL**: https://discourse.slicer.org/t/3d-slicer-cannot-be-installed-in-windows-11/47861

---

## Post #1 by @Abdoelabassi (2026-08-11 14:03 UTC)

<p>I downloaded the installer, but the integrity check of Win11 has failed. Common causes include an incomplete download (which is unlikely, because the download was healthy and complete) and damaged media.</p>

---

## Post #2 by @muratmaga (2026-08-12 03:17 UTC)

<p>I just installed the current 5.12.3 on two different Windows 11 machines today. it is also the version of slicer that’s most heavily used, and so far no one else reported this. This points out a problem on your network.</p>
<p>Do you have an antivirus or overzealous security environment? Most likely something between the your computer and <a href="http://download.slicer.org" rel="noopener nofollow ugc">download.slicer.org</a> is tampering with the package and corrupting it. If you have the option either temporarily disable them, or download the installer some other computer and copy to yours.</p>

---
