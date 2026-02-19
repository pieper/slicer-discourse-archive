---
topic_id: 29944
title: "Slicer 5 2 2 Not Starting On Windows Server 2016 Using Micro"
date: 2023-06-09
url: https://discourse.slicer.org/t/29944
---

# Slicer-5.2.2 not starting on Windows Server 2016 using Microsoft Application Virtualization (appv)

**Topic ID**: 29944
**Date**: 2023-06-09
**URL**: https://discourse.slicer.org/t/slicer-5-2-2-not-starting-on-windows-server-2016-using-microsoft-application-virtualization-appv/29944

---

## Post #1 by @Bernhard (2023-06-09 15:42 UTC)

<p>Operating system: win10, windows server 2016<br>
Slicer version: 5.2.2<br>
Expected behavior: starting<br>
Actual behavior: not starting</p>
<p>Hi all<br>
we are distributing software through Microsoft Application Virtualization (appv). Previous versions (latest was 4.10) were no problem, but version 5.2.2 does not start.</p>
<p>There are no error messages, no error dialogs, and no errors in the log files. The splash dialog appears, closes, appears again, and then the program just closes.</p>
<p>Interestingly, that happens also on a machine where 3dslicer 5.2.2 is installed locally, but started from within a so called virtual bubble.</p>
<p>Any idea what to look for?</p>
<p>the last line of the log file is:<br>
[DEBUG][Python] 09.06.2023 13:24:02 [Python] (C:\ProgramData\NA-MIC\Slicer 5.2.2\lib\Slicer-5.2\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentStatistics</p>
<p>thanks in advance for any suggestion!</p>

---

## Post #2 by @muratmaga (2023-06-09 16:49 UTC)

<aside class="quote no-group" data-username="Bernhard" data-post="1" data-topic="29944">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/c37758/48.png" class="avatar"> Bernhard:</div>
<blockquote>
<p>the last line of the log file is:</p>
</blockquote>
</aside>
<p>Please provide the full log.</p>

---

## Post #3 by @pieper (2023-06-09 19:45 UTC)

<p>I don’t know anything about appv so I searched for it and the first hit had this message, so maybe you can try the suggested replacement?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e934ca83effafb6a389050b19f02dacb6dbdac8.png" data-download-href="/uploads/short-url/bd6PtEqZOKtIr439GrzvX3mRZ0Y.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e934ca83effafb6a389050b19f02dacb6dbdac8.png" alt="image" data-base62-sha1="bd6PtEqZOKtIr439GrzvX3mRZ0Y" width="690" height="172" data-dominant-color="E8D3F3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">746×187 18.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Generally speaking there have been troubles with graphics drivers on remote desktops on windows so hopefully the newer versions won’t have these problems.</p>

---

## Post #4 by @Bernhard (2023-06-12 07:54 UTC)

<p>[DEBUG][Qt] 12.06.2023 09:48:50 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 2023-06-12 09:48:50<br>
[DEBUG][Qt] 12.06.2023 09:48:50 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 5.2.2 (revision 31382 / fb46bd1) win-amd64 - installed release<br>
[DEBUG][Qt] 12.06.2023 09:48:50 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows /  Professional / (Build 19044, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 12.06.2023 09:48:50 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 4095 MB physical, 5443 MB virtual<br>
[DEBUG][Qt] 12.06.2023 09:48:50 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel , 4 cores, 4 logical processors<br>
[DEBUG][Qt] 12.06.2023 09:48:50 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 12.06.2023 09:48:50 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 12.06.2023 09:48:50 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Internationalization …: disabled, language=<br>
[DEBUG][Qt] 12.06.2023 09:48:50 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode …: disabled<br>
[DEBUG][Qt] 12.06.2023 09:48:50 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: C:/Users/test/Desktop/Slicer/bin<br>
[DEBUG][Qt] 12.06.2023 09:48:50 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 12.06.2023 09:48:59 [Python] (C:\Users\test\Desktop\Slicer\lib\Slicer-5.2\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 12.06.2023 09:49:01 [Python] (C:\Users\test\Desktop\Slicer\lib\Slicer-5.2\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 12.06.2023 09:49:01 [Python] (C:\Users\test\Desktop\Slicer\lib\Slicer-5.2\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentStatistics</p>

---

## Post #5 by @Bernhard (2023-06-16 10:16 UTC)

<p>we could create a workaround.<br>
the reason Slicer.exe did not start correctly are all the environment variables that are set by the slicer.exe, but they are not valid inside an virtual appv package.<br>
The workaround is to set the variables correctly first, and then start the slicerapp-real.exe</p>

---

## Post #6 by @lassoan (2023-06-16 13:51 UTC)

<p><a href="https://social.technet.microsoft.com/Forums/en-US/3da89298-f44c-405a-94b9-c4b577585361/appv-5-package-ignores-environment-variable-included-in-virtual-registry">Many people struggle with this odd behavior of App-V</a> on this old Windows Server version and there does not seem to be a clear solution, only workarounds like you described. Probably the issue is fixed in more recent Windows Server versions.</p>

---

## Post #7 by @Bernhard (2023-06-17 11:09 UTC)

<p>Dear Andras,<br>
thanks for your reply. However: this behavious also occurs on windows 11 machines. It is clearly not a question of OS version. Rather, the paths inside the virtual bubble of an appv package are completely different than on a “real” installation.</p>
<p>cheers</p>

---

## Post #8 by @lassoan (2023-06-17 12:41 UTC)

<p>Thanks for the clarification. Did I understand correctly that you tried to start the application by running Slicer.exe and it failed because the environment variables that Slicer.exe set were not passed on to SlicerApp-real.exe (SlicerApp-real.exe did not inherit its environment from the process or launched it but got some default environment)?</p>

---

## Post #9 by @Bernhard (2023-06-17 12:57 UTC)

<p>Dear Andras,<br>
let’s say I did a “real” install on a win10 machine, installing as admin to c:\programdata\slicer5. If I start a cmd.exe after install, no new variables are set. But variables were created. you can see them by:<br>
start slicer<br>
click add data button<br>
click “choose file…”<br>
in the file name field, enter c:\windows\system32\cmd.*<br>
click Open button. Scroll down, rightclick cmd.exe and select Open in the context menu.<br>
in the cmd window, enter set to see these variables set:<br>
Path=C:/ProgramData/NA-MIC/Slicer5/bin/…/bin;C:/ProgramData/NA-MIC/Slicer5/bin/…/lib/Slicer-5.2/cli-modules;C:/ProgramData/NA-MIC/Slicer5/bin/…/lib/Slicer-5.2/qt-loadable-modules;C:/ProgramData/NA-MIC/Slicer5/bin/…/lib/Slicer-5.2;C:/ProgramData/NA-MIC/Slicer5/bin/…/…/lib/Slicer-5.2/qt-loadable-modules;C:/ProgramData/NA-MIC/Slicer5/bin/…/…/lib/Slicer-5.2/qt-loadable-modules/Release;C:/ProgramData/NA-MIC/Slicer5/bin/…/lib/Python/Lib/site-packages/numpy/core;C:/ProgramData/NA-MIC/Slicer5/bin/…/lib/Python/Lib/site-packages/numpy/lib;C:/ProgramData/NA-MIC/Slicer5/…/lib/Slicer-5.2/qt-loadable-modules;C:/ProgramData/NA-MIC/Slicer5/…/lib/Slicer-5.2/qt-loadable-modules/Release;<br>
PYTHONHOME=C:/ProgramData/NA-MIC/Slicer5/bin/…/lib/Python<br>
PYTHONNOUSERSITE=1<br>
PYTHONPATH=C:/ProgramData/NA-MIC/Slicer5/bin/…/lib/Slicer-5.2;C:/ProgramData/NA-MIC/Slicer5/bin/…/lib/Slicer-5.2/qt-scripted-modules;C:/ProgramData/NA-MIC/Slicer5/bin/…/lib/Slicer-5.2/qt-loadable-modules;C:/ProgramData/NA-MIC/Slicer5/bin/…/lib/vtkTeem;C:/ProgramData/NA-MIC/Slicer5/bin/…/bin/Python;C:/ProgramData/NA-MIC/Slicer5/bin/…/lib/Slicer-5.2/qt-loadable-modules/Python;C:/ProgramData/NA-MIC/Slicer5/bin/…/lib/Python/Lib;C:/ProgramData/NA-MIC/Slicer5/bin/…/lib/Python/Lib/lib-dynload;C:/ProgramData/NA-MIC/Slicer5/bin/…/lib/Python/Lib/site-packages;C:/ProgramData/NA-MIC/Slicer5/bin/…/bin/Lib/site-packages<br>
QT_PLUGIN_PATH=C:/ProgramData/NA-MIC/Slicer5/bin/…/lib/QtPlugins</p>
<p>I do not know how slicer.exe evaluates all these paths. the fact of having things like bin/…/lib is also quite interesting, but no problem…</p>
<p>Inside an appv package, all these paths will not exist, i.e. the paths are different</p>
<p>cheers<br>
bernhard</p>

---
