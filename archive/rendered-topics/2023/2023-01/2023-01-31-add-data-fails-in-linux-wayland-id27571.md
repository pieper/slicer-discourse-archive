# Add data fails in linux (wayland).

**Topic ID**: 27571
**Date**: 2023-01-31
**URL**: https://discourse.slicer.org/t/add-data-fails-in-linux-wayland/27571

---

## Post #1 by @umgpy (2023-01-31 19:23 UTC)

<p>The data loading module fails after the first time and results in a blank window. Only way to fix it is to restart Slicer.</p>
<p>My platform is Fedora 36 (linux) with wayland.<br>
Slicer version - Slicer-5.3.0-2023-01-28<br>
I’m attaching the terminal output along with the slicer log to help solve this issue.</p>
<pre><code class="lang-auto">[usr@usr ~]$ ~/Software/Slicer-5.3.0-2023-01-28-linux-amd64/Slicer 
Warning: Ignoring XDG_SESSION_TYPE=wayland on Gnome. Use QT_QPA_PLATFORM=wayland to run on Wayland anyway.
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/usr/Software/Slicer-5.3.0-2023-01-28-linux-amd64/lib/Python/lib/python3.9/imp.py", line 169, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 613, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
  File "/home/usr/Software/Slicer-5.3.0-2023-01-28-linux-amd64/NA-MIC/Extensions-31553/MONAILabel/lib/Slicer-5.3/qt-scripted-modules/MONAILabelReviewer.py", line 23, in &lt;module&gt;
    from MONAILabelReviewerLib.ImageData import ImageData
  File "/home/usr/Software/Slicer-5.3.0-2023-01-28-linux-amd64/NA-MIC/Extensions-31553/MONAILabel/lib/Slicer-5.3/qt-scripted-modules/MONAILabelReviewerLib/__init__.py", line 14, in &lt;module&gt;
    from .ImageDataController import ImageDataController
  File "/home/usr/Software/Slicer-5.3.0-2023-01-28-linux-amd64/NA-MIC/Extensions-31553/MONAILabel/lib/Slicer-5.3/qt-scripted-modules/MONAILabelReviewerLib/ImageDataController.py", line 19, in &lt;module&gt;
    from MONAILabelReviewerLib.ImageDataStatistics import ImageDataStatistics
ModuleNotFoundError: No module named 'MONAILabelReviewerLib.ImageDataStatistics'
loadSourceAsModule - Failed to load file "/home/usr/Software/Slicer-5.3.0-2023-01-28-linux-amd64/NA-MIC/Extensions-31553/MONAILabel/lib/Slicer-5.3/qt-scripted-modules/MONAILabelReviewer.py"  as module "MONAILabelReviewer" !
Fail to instantiate module  "MONAILabelReviewer"
The following modules failed to be instantiated:
   MONAILabelReviewer
Switch to module:  "Welcome"
QXcbConnection: XCB error: 8 (BadMatch), sequence: 2117, resource id: 20971620, major code: 130 (Unknown), minor code: 3
QXcbConnection: XCB error: 8 (BadMatch), sequence: 2120, resource id: 20971620, major code: 130 (Unknown), minor code: 3
QXcbConnection: XCB error: 8 (BadMatch), sequence: 2136, resource id: 20971620, major code: 130 (Unknown), minor code: 3
QXcbConnection: XCB error: 8 (BadMatch), sequence: 2137, resource id: 20971620, major code: 130 (Unknown), minor code: 3
QXcbConnection: XCB error: 8 (BadMatch), sequence: 2166, resource id: 20971620, major code: 130 (Unknown), minor code: 3
QXcbConnection: XCB error: 8 (BadMatch), sequence: 2174, resource id: 20971620, major code: 130 (Unknown), minor code: 3
</code></pre>
<p>Slicer log</p>
<pre><code class="lang-auto">[DEBUG][Qt] 31.01.2023 09:34:49 [] (unknown:0) - Session start time .......: 2023-01-31 09:34:49
[DEBUG][Qt] 31.01.2023 09:34:49 [] (unknown:0) - Slicer version ...........: 5.3.0-2023-01-28 (revision 31553 / 0f25e18) linux-amd64 - installed release
[DEBUG][Qt] 31.01.2023 09:34:49 [] (unknown:0) - Operating system .........: Linux / 5.17.13-300.fc36.x86_64 / #1 SMP PREEMPT Mon Jun 6 14:29:43 UTC 2022 / UTF-8 - 64-bit
[DEBUG][Qt] 31.01.2023 09:34:49 [] (unknown:0) - Memory ...................: 15365 MB physical, 8191 MB virtual
[DEBUG][Qt] 31.01.2023 09:34:49 [] (unknown:0) - CPU ......................: AuthenticAMD AMD Ryzen 7 4800HS with Radeon Graphics, 8 cores, 16 logical processors
[DEBUG][Qt] 31.01.2023 09:34:49 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, Sequential threading
[DEBUG][Qt] 31.01.2023 09:34:49 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (core profile)
[DEBUG][Qt] 31.01.2023 09:34:49 [] (unknown:0) - Internationalization .....: disabled, language=
[DEBUG][Qt] 31.01.2023 09:34:49 [] (unknown:0) - Developer mode ...........: disabled
[DEBUG][Qt] 31.01.2023 09:34:49 [] (unknown:0) - Application path .........: /home/uusr/Software/Slicer-5.3.0-2023-01-28-linux-amd64/bin
[DEBUG][Qt] 31.01.2023 09:34:49 [] (unknown:0) - Additional module paths ..: NA-MIC/Extensions-31553/MONAILabel/lib/Slicer-5.3/qt-scripted-modules
[CRITICAL][Stream] 31.01.2023 09:34:54 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 31.01.2023 09:34:54 [] (unknown:0) -   File "&lt;string&gt;", line 1, in &lt;module&gt;
[CRITICAL][Stream] 31.01.2023 09:34:54 [] (unknown:0) -   File "/home/uusr/Software/Slicer-5.3.0-2023-01-28-linux-amd64/lib/Python/lib/python3.9/imp.py", line 169, in load_source
[CRITICAL][Stream] 31.01.2023 09:34:54 [] (unknown:0) -     module = _exec(spec, sys.modules[name])
[CRITICAL][Stream] 31.01.2023 09:34:54 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap&gt;", line 613, in _exec
[CRITICAL][Stream] 31.01.2023 09:34:54 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
[CRITICAL][Stream] 31.01.2023 09:34:54 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
[CRITICAL][Stream] 31.01.2023 09:34:54 [] (unknown:0) -   File "/home/uusr/Software/Slicer-5.3.0-2023-01-28-linux-amd64/NA-MIC/Extensions-31553/MONAILabel/lib/Slicer-5.3/qt-scripted-modules/MONAILabelReviewer.py", line 23, in &lt;module&gt;
[CRITICAL][Stream] 31.01.2023 09:34:54 [] (unknown:0) -     from MONAILabelReviewerLib.ImageData import ImageData
[CRITICAL][Stream] 31.01.2023 09:34:54 [] (unknown:0) -   File "/home/uusr/Software/Slicer-5.3.0-2023-01-28-linux-amd64/NA-MIC/Extensions-31553/MONAILabel/lib/Slicer-5.3/qt-scripted-modules/MONAILabelReviewerLib/__init__.py", line 14, in &lt;module&gt;
[CRITICAL][Stream] 31.01.2023 09:34:54 [] (unknown:0) -     from .ImageDataController import ImageDataController
[CRITICAL][Stream] 31.01.2023 09:34:54 [] (unknown:0) -   File "/home/uusr/Software/Slicer-5.3.0-2023-01-28-linux-amd64/NA-MIC/Extensions-31553/MONAILabel/lib/Slicer-5.3/qt-scripted-modules/MONAILabelReviewerLib/ImageDataController.py", line 19, in &lt;module&gt;
[CRITICAL][Stream] 31.01.2023 09:34:54 [] (unknown:0) -     from MONAILabelReviewerLib.ImageDataStatistics import ImageDataStatistics
[CRITICAL][Stream] 31.01.2023 09:34:54 [] (unknown:0) - ModuleNotFoundError: No module named 'MONAILabelReviewerLib.ImageDataStatistics'
[CRITICAL][Qt] 31.01.2023 09:34:54 [] (unknown:0) - loadSourceAsModule - Failed to load file "/home/uusr/Software/Slicer-5.3.0-2023-01-28-linux-amd64/NA-MIC/Extensions-31553/MONAILabel/lib/Slicer-5.3/qt-scripted-modules/MONAILabelReviewer.py"  as module "MONAILabelReviewer" !
[CRITICAL][Qt] 31.01.2023 09:34:54 [] (unknown:0) - Fail to instantiate module  "MONAILabelReviewer"
[CRITICAL][Qt] 31.01.2023 09:34:54 [] (unknown:0) - The following modules failed to be instantiated:
[CRITICAL][Qt] 31.01.2023 09:34:54 [] (unknown:0) -    MONAILabelReviewer
[DEBUG][Python] 31.01.2023 09:34:57 [Python] (/home/uusr/Software/Slicer-5.3.0-2023-01-28-linux-amd64/lib/Slicer-5.3/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 31.01.2023 09:34:57 [Python] (/home/uusr/Software/Slicer-5.3.0-2023-01-28-linux-amd64/lib/Slicer-5.3/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 31.01.2023 09:34:57 [] (unknown:0) - Switch to module:  "Welcome"
[WARNING][Qt] 31.01.2023 09:35:07 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 2117, resource id: 20971620, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 31.01.2023 09:35:07 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 2120, resource id: 20971620, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 31.01.2023 09:35:07 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 2136, resource id: 20971620, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 31.01.2023 09:35:07 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 2137, resource id: 20971620, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 31.01.2023 09:35:07 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 2166, resource id: 20971620, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 31.01.2023 09:35:07 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 2174, resource id: 20971620, major code: 130 (Unknown), minor code: 3
</code></pre>
<p>Thanks in advance!</p>

---

## Post #2 by @jamesobutler (2023-01-31 20:18 UTC)

<p><a class="mention" href="/u/umgpy">@umgpy</a> Did the observed behavior change after building Slicer from source? I saw that you mentioned this over on the GitHub issue.</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6806">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6806" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6806" target="_blank" rel="noopener nofollow ugc">Add data menu fails in wayland linux </a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-01-31" data-time="10:06:18" data-timezone="UTC">10:06AM - 31 Jan 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/umgpy" target="_blank" rel="noopener nofollow ugc">
          <img alt="umgpy" src="https://avatars.githubusercontent.com/u/44013803?v=4" class="onebox-avatar-inline" width="20" height="20">
          umgpy
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

The add data menu fails after loading the first time. Upon opening<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> the menu the second time it results in a blank window.
Only way to fix this is to restart slicer. My system is using fedora with wayland.

## Steps to reproduce

Open slicer -&gt; open the add data menu -&gt; close the menu and reopen again.


## Expected behavior

Add data menu should not fail.



## Environment
- Slicer version:  5.3.0-2023-01-28 (revision 31553 / 0f25e18) linux-amd64
- Operating system: Linux / 5.17.13-300.fc36.x86_64 

I am attaching the terminal output and slicer log to help solve this is issue.

```
[usr@usr ~]$ ~/Software/Slicer-5.3.0-2023-01-28-linux-amd64/Slicer 
Warning: Ignoring XDG_SESSION_TYPE=wayland on Gnome. Use QT_QPA_PLATFORM=wayland to run on Wayland anyway.
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/usr/Software/Slicer-5.3.0-2023-01-28-linux-amd64/lib/Python/lib/python3.9/imp.py", line 169, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 613, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
  File "/home/usr/Software/Slicer-5.3.0-2023-01-28-linux-amd64/NA-MIC/Extensions-31553/MONAILabel/lib/Slicer-5.3/qt-scripted-modules/MONAILabelReviewer.py", line 23, in &lt;module&gt;
    from MONAILabelReviewerLib.ImageData import ImageData
  File "/home/usr/Software/Slicer-5.3.0-2023-01-28-linux-amd64/NA-MIC/Extensions-31553/MONAILabel/lib/Slicer-5.3/qt-scripted-modules/MONAILabelReviewerLib/__init__.py", line 14, in &lt;module&gt;
    from .ImageDataController import ImageDataController
  File "/home/usr/Software/Slicer-5.3.0-2023-01-28-linux-amd64/NA-MIC/Extensions-31553/MONAILabel/lib/Slicer-5.3/qt-scripted-modules/MONAILabelReviewerLib/ImageDataController.py", line 19, in &lt;module&gt;
    from MONAILabelReviewerLib.ImageDataStatistics import ImageDataStatistics
ModuleNotFoundError: No module named 'MONAILabelReviewerLib.ImageDataStatistics'
loadSourceAsModule - Failed to load file "/home/usr/Software/Slicer-5.3.0-2023-01-28-linux-amd64/NA-MIC/Extensions-31553/MONAILabel/lib/Slicer-5.3/qt-scripted-modules/MONAILabelReviewer.py"  as module "MONAILabelReviewer" !
Fail to instantiate module  "MONAILabelReviewer"
The following modules failed to be instantiated:
   MONAILabelReviewer
Switch to module:  "Welcome"
QXcbConnection: XCB error: 8 (BadMatch), sequence: 2117, resource id: 20971620, major code: 130 (Unknown), minor code: 3
QXcbConnection: XCB error: 8 (BadMatch), sequence: 2120, resource id: 20971620, major code: 130 (Unknown), minor code: 3
QXcbConnection: XCB error: 8 (BadMatch), sequence: 2136, resource id: 20971620, major code: 130 (Unknown), minor code: 3
QXcbConnection: XCB error: 8 (BadMatch), sequence: 2137, resource id: 20971620, major code: 130 (Unknown), minor code: 3
QXcbConnection: XCB error: 8 (BadMatch), sequence: 2166, resource id: 20971620, major code: 130 (Unknown), minor code: 3
QXcbConnection: XCB error: 8 (BadMatch), sequence: 2174, resource id: 20971620, major code: 130 (Unknown), minor code: 3
```

Slicer log

```
[DEBUG][Qt] 31.01.2023 09:34:49 [] (unknown:0) - Session start time .......: 2023-01-31 09:34:49
[DEBUG][Qt] 31.01.2023 09:34:49 [] (unknown:0) - Slicer version ...........: 5.3.0-2023-01-28 (revision 31553 / 0f25e18) linux-amd64 - installed release
[DEBUG][Qt] 31.01.2023 09:34:49 [] (unknown:0) - Operating system .........: Linux / 5.17.13-300.fc36.x86_64 / #1 SMP PREEMPT Mon Jun 6 14:29:43 UTC 2022 / UTF-8 - 64-bit
[DEBUG][Qt] 31.01.2023 09:34:49 [] (unknown:0) - Memory ...................: 15365 MB physical, 8191 MB virtual
[DEBUG][Qt] 31.01.2023 09:34:49 [] (unknown:0) - CPU ......................: AuthenticAMD AMD Ryzen 7 4800HS with Radeon Graphics, 8 cores, 16 logical processors
[DEBUG][Qt] 31.01.2023 09:34:49 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, Sequential threading
[DEBUG][Qt] 31.01.2023 09:34:49 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (core profile)
[DEBUG][Qt] 31.01.2023 09:34:49 [] (unknown:0) - Internationalization .....: disabled, language=
[DEBUG][Qt] 31.01.2023 09:34:49 [] (unknown:0) - Developer mode ...........: disabled
[DEBUG][Qt] 31.01.2023 09:34:49 [] (unknown:0) - Application path .........: /home/uusr/Software/Slicer-5.3.0-2023-01-28-linux-amd64/bin
[DEBUG][Qt] 31.01.2023 09:34:49 [] (unknown:0) - Additional module paths ..: NA-MIC/Extensions-31553/MONAILabel/lib/Slicer-5.3/qt-scripted-modules
[CRITICAL][Stream] 31.01.2023 09:34:54 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 31.01.2023 09:34:54 [] (unknown:0) -   File "&lt;string&gt;", line 1, in &lt;module&gt;
[CRITICAL][Stream] 31.01.2023 09:34:54 [] (unknown:0) -   File "/home/uusr/Software/Slicer-5.3.0-2023-01-28-linux-amd64/lib/Python/lib/python3.9/imp.py", line 169, in load_source
[CRITICAL][Stream] 31.01.2023 09:34:54 [] (unknown:0) -     module = _exec(spec, sys.modules[name])
[CRITICAL][Stream] 31.01.2023 09:34:54 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap&gt;", line 613, in _exec
[CRITICAL][Stream] 31.01.2023 09:34:54 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
[CRITICAL][Stream] 31.01.2023 09:34:54 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
[CRITICAL][Stream] 31.01.2023 09:34:54 [] (unknown:0) -   File "/home/uusr/Software/Slicer-5.3.0-2023-01-28-linux-amd64/NA-MIC/Extensions-31553/MONAILabel/lib/Slicer-5.3/qt-scripted-modules/MONAILabelReviewer.py", line 23, in &lt;module&gt;
[CRITICAL][Stream] 31.01.2023 09:34:54 [] (unknown:0) -     from MONAILabelReviewerLib.ImageData import ImageData
[CRITICAL][Stream] 31.01.2023 09:34:54 [] (unknown:0) -   File "/home/uusr/Software/Slicer-5.3.0-2023-01-28-linux-amd64/NA-MIC/Extensions-31553/MONAILabel/lib/Slicer-5.3/qt-scripted-modules/MONAILabelReviewerLib/__init__.py", line 14, in &lt;module&gt;
[CRITICAL][Stream] 31.01.2023 09:34:54 [] (unknown:0) -     from .ImageDataController import ImageDataController
[CRITICAL][Stream] 31.01.2023 09:34:54 [] (unknown:0) -   File "/home/uusr/Software/Slicer-5.3.0-2023-01-28-linux-amd64/NA-MIC/Extensions-31553/MONAILabel/lib/Slicer-5.3/qt-scripted-modules/MONAILabelReviewerLib/ImageDataController.py", line 19, in &lt;module&gt;
[CRITICAL][Stream] 31.01.2023 09:34:54 [] (unknown:0) -     from MONAILabelReviewerLib.ImageDataStatistics import ImageDataStatistics
[CRITICAL][Stream] 31.01.2023 09:34:54 [] (unknown:0) - ModuleNotFoundError: No module named 'MONAILabelReviewerLib.ImageDataStatistics'
[CRITICAL][Qt] 31.01.2023 09:34:54 [] (unknown:0) - loadSourceAsModule - Failed to load file "/home/uusr/Software/Slicer-5.3.0-2023-01-28-linux-amd64/NA-MIC/Extensions-31553/MONAILabel/lib/Slicer-5.3/qt-scripted-modules/MONAILabelReviewer.py"  as module "MONAILabelReviewer" !
[CRITICAL][Qt] 31.01.2023 09:34:54 [] (unknown:0) - Fail to instantiate module  "MONAILabelReviewer"
[CRITICAL][Qt] 31.01.2023 09:34:54 [] (unknown:0) - The following modules failed to be instantiated:
[CRITICAL][Qt] 31.01.2023 09:34:54 [] (unknown:0) -    MONAILabelReviewer
[DEBUG][Python] 31.01.2023 09:34:57 [Python] (/home/uusr/Software/Slicer-5.3.0-2023-01-28-linux-amd64/lib/Slicer-5.3/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 31.01.2023 09:34:57 [Python] (/home/uusr/Software/Slicer-5.3.0-2023-01-28-linux-amd64/lib/Slicer-5.3/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 31.01.2023 09:34:57 [] (unknown:0) - Switch to module:  "Welcome"
[WARNING][Qt] 31.01.2023 09:35:07 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 2117, resource id: 20971620, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 31.01.2023 09:35:07 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 2120, resource id: 20971620, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 31.01.2023 09:35:07 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 2136, resource id: 20971620, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 31.01.2023 09:35:07 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 2137, resource id: 20971620, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 31.01.2023 09:35:07 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 2166, resource id: 20971620, major code: 130 (Unknown), minor code: 3
[WARNING][Qt] 31.01.2023 09:35:07 [] (unknown:0) - QXcbConnection: XCB error: 8 (BadMatch), sequence: 2174, resource id: 20971620, major code: 130 (Unknown), minor code: 3
```</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @umgpy (2023-02-06 14:34 UTC)

<p>Hello <a class="mention" href="/u/jamesobutler">@jamesobutler</a> not yet, I’ll try to build it this week. Shall report back soon!</p>

---

## Post #4 by @Jens_Munk_Hansen (2023-11-10 18:56 UTC)

<p>I can build slicer on Debian 12 using wayland.</p>
<p>I use the following startup script</p>
<pre><code class="lang-auto">#!/bin/bash

__NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia QT_XCB_GL_INTEGRATION=xcb_egl QT_WAYLAND_SHELL_INTEGRATION=ivi-shell QT_WAYLAND_CLIENT_BUFFER_INTEGRATION=wayland-egl $@ -platform wayland
</code></pre>
<p>The first entries I use because I work on a laptop using hybrid graphics. Sometimes my entire computer freezes. I needed to install a different version for SSL to make it work.</p>

---

## Post #5 by @pieper (2023-11-10 19:29 UTC)

<p>Interesting - maybe that should go in slicer’s readthedocs somewhere.</p>

---
