---
topic_id: 18445
title: "Packaging Error"
date: 2021-07-01
url: https://discourse.slicer.org/t/18445
---

# Packaging error

**Topic ID**: 18445
**Date**: 2021-07-01
**URL**: https://discourse.slicer.org/t/packaging-error/18445

---

## Post #1 by @qiqi5210 (2021-07-01 00:55 UTC)

<p>Hello everyone, I made some minor changes to the successful 3D slicer. When I packaged the software, there was an error</p>
<p><strong>seriousness code explain project file that 's ok Disable display status</strong><br>
<strong>error MSB6006 “ “CMD. Exe” exited with code - 1073741819. kneeUpdateLauncherWIcon C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\Common7\IDE\VC\VCTargets\Microsoft.CppCommon.targets two hundred and nine</strong></p>
<p><strong>seriousness code explain project file that 's ok Disable display status</strong><br>
<strong>error MSB6006 “ “CMD. Exe” exited with code - 1073741819. kneeUpdateLauncherIcon C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\Common7\IDE\VC\VCTargets\Microsoft.CppCommon.targets two hundred and nine</strong></p>
<p>Hope to get your reply, thank you！</p>

---

## Post #2 by @lassoan (2021-07-02 04:16 UTC)

<p>This happens when the application icon of <code>Slicer.exe</code> cannot updated because the file is read-only. This typically happens when <code>Slicer.exe</code> is running.</p>
<p>To avoid this, start Visual Studio by double-clicking on the <code>Slicer.sln</code>. You only need to launch Visual Studio using <code>Slicer.exe --VisualStudio</code> shortcut if you want to launch Slicer, but it is not needed for packaging.</p>

---
