---
topic_id: 22862
title: "Slicer Silent Unattended Installation String For Windows"
date: 2022-04-07
url: https://discourse.slicer.org/t/22862
---

# Slicer Silent unattended installation string for Windows

**Topic ID**: 22862
**Date**: 2022-04-07
**URL**: https://discourse.slicer.org/t/slicer-silent-unattended-installation-string-for-windows/22862

---

## Post #1 by @Cyberdyne_Systems (2022-04-07 11:49 UTC)

<p>Hi, I need to integrate the new 3dSlicer Application into our Windows 10 20H2 Clients over SCCM Software distribution. Therefore I need to change the Installation path from %ProgramData% to %ProgramFiles% with a CMD installation string. %ProgramData% ‘re blocked by GPO and can’t be started b y customers.<br>
Unfortunately I don’t see any installation parameters with the command /?<br>
is there a command to do the installation under C:\ProgamFiles?<br>
thanx<br>
eCrofey</p>

---

## Post #2 by @lassoan (2022-04-07 12:25 UTC)

<p>Recent Slicer versions are fully portable, therefore it does not require installation. You can zip up the installation folder and instead of installation just unzip it anywhere. This works even after you install extensions (they are all in the portable Slicer application folder, too).</p>
<p>Note that in general if you want to allow your users to install extensions, Slicer must be installed into a writable folder. If that is not acceptable then it is possible to allow installation of some extensions (that don’t install additional Python packages) in the user’s profile folder; and if the user starts Slicer as admin then it is possible to install any extensions.</p>

---

## Post #3 by @jamesobutler (2022-04-07 14:19 UTC)

<p>It’s a NSIS installer so there are some command line parameters you can use to run silently and set the install path. See <a href="https://nsis.sourceforge.io/Docs/Chapter4.html#silent" rel="noopener nofollow ugc">https://nsis.sourceforge.io/Docs/Chapter4.html#silent</a>.</p>
<p>I actually have a NSIS installer that installs multiple things including Slicer so it does the following</p>
<pre><code class="lang-auto">Section "3D Slicer 4.13.0-2021-09-14 (64-bit)" SEC01
  SectionIn 2 3
  SetOverwrite ifnewer
  SetOutPath "$TEMP\CompanyName"
  File "Slicer-4.13.0-2021-09-14-win-amd64.exe"
  ExecWait '"$TEMP\CompanyName\Slicer-4.13.0-2021-09-14-win-amd64.exe" /S /D=C:\Program Files\Slicer 4.13.0-2021-09-14'
SectionEnd
</code></pre>

---

## Post #4 by @Cyberdyne_Systems (2022-04-08 08:03 UTC)

<p>awesome, thank you !</p>

---
