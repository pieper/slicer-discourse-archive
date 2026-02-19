---
topic_id: 45772
title: "Ctkresedit Unable To Start"
date: 2026-01-13
url: https://discourse.slicer.org/t/45772
---

# CTKResEdit unable to start

**Topic ID**: 45772
**Date**: 2026-01-13
**URL**: https://discourse.slicer.org/t/ctkresedit-unable-to-start/45772

---

## Post #1 by @rphellan2210 (2026-01-13 16:39 UTC)

<p>Hello, I am trying to build Slicer and the process requires running CTKResEdit.exe to update some icons, but CTKResEdit fails and it leads to the error below.</p>
<p>C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(254,5): error MSB8066: Custom build for ‘C:\s\sR\Slicer-build\CMakeFiles\6ea644fa26f044f96bce4abbb021dfc4\[edited].rule’ exited with code -1073741502. [C:\s\sR\Slicer-build\Applications\[edited]\UpdateLauncherIcon.vcxproj</p>
<p>I downloaded CTKResEdit.exe from <a href="https://github.com/jcfr/ResEdit" class="inline-onebox" rel="noopener nofollow ugc">GitHub - jcfr/ResEdit: Convenient tool allow to update resource within an already compiled windows executable</a> and whenever I try to run it, it displays the error “The application was unable to start correctly (0xc0000142)“. My OS is Windows 11 home.</p>
<p>I also tried running CTKResEdit in another computer with Windows 11 and it run correctly.</p>
<p>Do you have any suggestion on how to solve this problem?</p>

---

## Post #2 by @rphellan2210 (2026-01-14 00:56 UTC)

<p>Just for future reference, I found the solution. This was a problem with the hard drive of my PC. I just run the chkdsk /f /r command to fix it and restarted the computer and now CTKResEdit works normally.</p>

---
