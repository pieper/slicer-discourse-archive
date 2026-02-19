---
topic_id: 6240
title: "Silent Unattended Install"
date: 2019-03-21
url: https://discourse.slicer.org/t/6240
---

# Silent / Unattended Install

**Topic ID**: 6240
**Date**: 2019-03-21
**URL**: https://discourse.slicer.org/t/silent-unattended-install/6240

---

## Post #1 by @cmguog (2019-03-21 16:22 UTC)

<p>Hi there,</p>
<p>Could anyone tell me if there is a way to run a silent / unattended installation of Slicer on Windows 10 please?</p>
<p>Many thanks</p>

---

## Post #2 by @jamesobutler (2019-03-21 17:08 UTC)

<p>It is a NSIS installer so you can use the /S flag to run it silently. There is also a /D flag if you want to specify a different install location from the default.</p>
<pre><code class="lang-auto">./Slicer-4.11.0-2019-03-20-win-amd64.exe /S
</code></pre>

---

## Post #3 by @pieper (2019-03-21 20:59 UTC)

<p>Also, if you don’t need the windows menu shortcut and other installer side-effects you can just copy the Slicer directory around or unpack a zip file.  Everything should be locally self-contained (except settings and extensions).</p>

---
