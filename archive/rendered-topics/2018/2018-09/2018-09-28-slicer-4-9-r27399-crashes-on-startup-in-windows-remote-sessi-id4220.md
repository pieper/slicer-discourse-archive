# Slicer 4.9. (r27399) crashes on startup in Windows remote session

**Topic ID**: 4220
**Date**: 2018-09-28
**URL**: https://discourse.slicer.org/t/slicer-4-9-r27399-crashes-on-startup-in-windows-remote-session/4220

---

## Post #1 by @stephan (2018-09-28 14:55 UTC)

<p>Slicer 4.9. (r27399) but not Slicer 4.8.1. crashes when started in a remote desktop session.</p>
<p>Operating system (local as well as remote) Windows 7 Professional 64 bit.</p>
<p>Both Slicer versions start up and function as expected when used on the local desktop. However, every once in a while I remote into my work desktop using the Windows Remote Desktop utility. While Slicer 4.8.1 is starting up and working fine in this remote session, Slicer 4.9. does crash on startup after showing the splash screen (no error message, simply the Windows message “SlicerApp-real.exe has stopped working”). If Slicer 4.9. is already running (having been started in a local session) and I remote into this session, it keeps on running normally. But once closed, I can’t re-start it while in a remote session.</p>
<pre><code class="lang-auto">Log file of one of these failed start-up attempts:
[DEBUG][Qt] 28.09.2018 09:49:01 [] (unknown:0) - Session start time .......: 2018-09-28 09:49:01
[DEBUG][Qt] 28.09.2018 09:49:01 [] (unknown:0) - Slicer version ...........: 4.9.0-2018-09-10 (revision 27399) win-amd64 - installed release
[DEBUG][Qt] 28.09.2018 09:49:01 [] (unknown:0) - Operating system .........: Windows / 7 / Service Pack 1 (Build 7601) - 64-bit
[DEBUG][Qt] 28.09.2018 09:49:01 [] (unknown:0) - Memory ...................: 8072 MB physical, 16143 MB virtual
[DEBUG][Qt] 28.09.2018 09:49:01 [] (unknown:0) - CPU ......................: GenuineIntel , 4 cores, 4 logical processors
[DEBUG][Qt] 28.09.2018 09:49:01 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 28.09.2018 09:49:01 [] (unknown:0) - Developer mode enabled ...: no
[DEBUG][Qt] 28.09.2018 09:49:01 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 28.09.2018 09:49:01 [] (unknown:0) - Additional module paths ..: C:/Users/M171189/AppData/Roaming/NA-MIC/Extensions-27399/Sequences/lib/Slicer-4.9/qt-loadable-modules, C:/Users/M171189/AppData/Roaming/NA-MIC/Extensions-27399/Sequences/lib/Slicer-4.9/qt-scripted-modules, C:/Users/M171189/AppData/Roaming/NA-MIC/Extensions-27399/SlicerRT/lib/Slicer-4.9/cli-modules, C:/Users/M171189/AppData/Roaming/NA-MIC/Extensions-27399/SlicerRT/lib/Slicer-4.9/qt-loadable-modules, C:/Users/M171189/AppData/Roaming/NA-MIC/Extensions-27399/SlicerRT/lib/Slicer-4.9/qt-scripted-modules, C:/Users/M171189/AppData/Roaming/NA-MIC/Extensions-27399/CMFreg/lib/Slicer-4.9/cli-modules, C:/Users/M171189/AppData/Roaming/NA-MIC/Extensions-27399/CMFreg/lib/Slicer-4.9/qt-scripted-modules
[DEBUG][Python] 28.09.2018 09:49:08 [Python] (C:\Program Files\Slicer 4.9.0-2018-09-10\lib\Python\Lib\site-packages\git\cmd.py:719) - Popen(['git', 'version'], cwd=C:\Program Files\Slicer 4.9.0-2018-09-10, universal_newlines=False, shell=None)
[DEBUG][Python] 28.09.2018 09:49:09 [Python] (C:\Program Files\Slicer 4.9.0-2018-09-10\lib\Python\Lib\site-packages\git\cmd.py:719) - Popen(['git', 'version'], cwd=C:\Program Files\Slicer 4.9.0-2018-09-10, universal_newlines=False, shell=None)
[DEBUG][Python] 28.09.2018 09:49:11 [Python] (C:\Program Files\Slicer 4.9.0-2018-09-10\lib\Slicer-4.9\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 28.09.2018 09:49:15 [Python] (C:\Program Files\Slicer 4.9.0-2018-09-10\lib\Slicer-4.9\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 28.09.2018 09:49:15 [Python] (C:\Program Files\Slicer 4.9.0-2018-09-10\lib\Slicer-4.9\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics

</code></pre>
<p>Let me know if I can provide you any more details to reproduce this bug.</p>
<p>Thank you<br>
Stephan</p>

---

## Post #2 by @ihnorton (2018-09-28 15:20 UTC)

<p>Please see the following thread, and in particular two posts:</p>
<aside class="quote" data-post="3" data-topic="3148">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicer-remote-access/3148/3">Slicer Remote access</a> <a class="badge-category__wrapper " href="/c/support/feature-requests/9"><span data-category-id="9" style="--category-badge-color: #F1592A; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="11" data-drop-close="true" class="badge-category --has-parent" title="This category is for submitting ideas about what enhancements or new features should be added to 3D Slicer. Make your voice heard by voting on feature requests - by opening the topic and clicking the Vote button or by creating a new topics. Slicer developers will make it a priority to work on feature requests that have more votes."><span class="badge-category__name">Feature requests</span></span></a>
  </div>
  <blockquote>
    Slicer 4.9 minimum OpenGL requirements have been increased. Does this answer your questions? <a href="https://issues.slicer.org/view.php?id=4252">https://issues.slicer.org/view.php?id=4252</a> 
If not, then please write exact version of your Slicer, operating system, and remote desktop application.
  </blockquote>
</aside>

<aside class="quote" data-post="6" data-topic="3148">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicer-remote-access/3148/6">Slicer Remote access</a> <a class="badge-category__wrapper " href="/c/support/feature-requests/9"><span data-category-id="9" style="--category-badge-color: #F1592A; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="11" data-drop-close="true" class="badge-category --has-parent" title="This category is for submitting ideas about what enhancements or new features should be added to 3D Slicer. Make your voice heard by voting on feature requests - by opening the topic and clicking the Vote button or by creating a new topics. Slicer developers will make it a priority to work on feature requests that have more votes."><span class="badge-category__name">Feature requests</span></span></a>
  </div>
  <blockquote>
    The link from lassoan above describes the issue: Windows RDP client does not support newer OpenGL versions, and so Slicer crashes – unfortunately without a useful error message yet. The suggestion is to try VNC or NoMachine. I can confirm NoMachine works with recent Slicer builds from a Mac client to a Linux host. I haven’t tried it with a Windows client, but it should probably work fine.
  </blockquote>
</aside>

<p>Suggestions are: use TeamViewer, use VNC, or start Slicer <em>before</em> connecting with Remote Desktop.</p>
<p>Hope that helps!</p>

---

## Post #3 by @stephan (2018-09-28 15:41 UTC)

<p>Thank you for linking this. Sorry I didn’t see the other post.</p>

---
