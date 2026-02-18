# Critical Qt error on start-up of just-downloaded preview 4.13.0-2021-05-29

**Topic ID**: 17913
**Date**: 2021-06-02
**URL**: https://discourse.slicer.org/t/critical-qt-error-on-start-up-of-just-downloaded-preview-4-13-0-2021-05-29/17913

---

## Post #1 by @mikebind (2021-06-02 00:58 UTC)

<p>On start-up of a freshly downloaded preview release (no extensions, no extra modules added, no actions taken within Slicer after opening), I get a number of errors saying “setViewLabel should be called before setViewNode”.  Here is the full log file:</p>
<blockquote>
<p>[DEBUG][Qt] 01.06.2021 17:49:20 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 2021-06-01 17:49:20<br>
[DEBUG][Qt] 01.06.2021 17:49:20 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 4.13.0-2021-05-29 (revision 29934 / 7cce89a) win-amd64 - installed release<br>
[DEBUG][Qt] 01.06.2021 17:49:20 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows /  Professional / (Build 19041, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 01.06.2021 17:49:20 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 32499 MB physical, 55027 MB virtual<br>
[DEBUG][Qt] 01.06.2021 17:49:20 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel , 12 cores, 12 logical processors<br>
[DEBUG][Qt] 01.06.2021 17:49:20 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 01.06.2021 17:49:20 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.1, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 01.06.2021 17:49:20 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode enabled …: yes<br>
[DEBUG][Qt] 01.06.2021 17:49:20 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 01.06.2021 17:49:20 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: C:/Users/mikeb/AppData/Local/NA-MIC/Slicer 4.13.0-2021-05-29/bin<br>
[DEBUG][Qt] 01.06.2021 17:49:20 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: (none)<br>
[CRITICAL][Qt] 01.06.2021 17:49:24 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - setViewLabel should be called before setViewNode !<br>
[CRITICAL][Qt] 01.06.2021 17:49:24 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - setViewLabel should be called before setViewNode !<br>
[DEBUG][Python] 01.06.2021 17:49:25 [Python] (C:\Users\mikeb\AppData\Local\NA-MIC\Slicer 4.13.0-2021-05-29\lib\Slicer-4.13\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[CRITICAL][Qt] 01.06.2021 17:49:25 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - setViewLabel should be called before setViewNode !<br>
[CRITICAL][Qt] 01.06.2021 17:49:25 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - setViewLabel should be called before setViewNode !<br>
[CRITICAL][Qt] 01.06.2021 17:49:25 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - setViewLabel should be called before setViewNode !<br>
[CRITICAL][Qt] 01.06.2021 17:49:25 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - setViewLabel should be called before setViewNode !<br>
[CRITICAL][Qt] 01.06.2021 17:49:25 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - setViewLabel should be called before setViewNode !<br>
[CRITICAL][Qt] 01.06.2021 17:49:25 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - setViewLabel should be called before setViewNode !<br>
[CRITICAL][Qt] 01.06.2021 17:49:25 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - setViewLabel should be called before setViewNode !<br>
[CRITICAL][Qt] 01.06.2021 17:49:25 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - setViewLabel should be called before setViewNode !<br>
[CRITICAL][Qt] 01.06.2021 17:49:25 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - setViewLabel should be called before setViewNode !<br>
[DEBUG][Python] 01.06.2021 17:49:26 [Python] (C:\Users\mikeb\AppData\Local\NA-MIC\Slicer 4.13.0-2021-05-29\lib\Slicer-4.13\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 01.06.2021 17:49:26 [Python] (C:\Users\mikeb\AppData\Local\NA-MIC\Slicer 4.13.0-2021-05-29\lib\Slicer-4.13\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[CRITICAL][Qt] 01.06.2021 17:49:26 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - setViewLabel should be called before setViewNode !<br>
[CRITICAL][Qt] 01.06.2021 17:49:26 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - setViewLabel should be called before setViewNode !<br>
[CRITICAL][Qt] 01.06.2021 17:49:26 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - setViewLabel should be called before setViewNode !<br>
[DEBUG][Qt] 01.06.2021 17:49:26 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[CRITICAL][Qt] 01.06.2021 17:49:27 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - setViewLabel should be called before setViewNode !<br>
[CRITICAL][Qt] 01.06.2021 17:49:27 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - setViewLabel should be called before setViewNode !</p>
</blockquote>
<p>I get these errors on the stable release, but had assumed they had probably been fixed in the preview.  I just updated to the preview and still see them.  They don’t seem to have any effect in the stable I have been using for months, but they also seem like they should be easy to fix, for someone who knows where to look.</p>

---

## Post #2 by @jamesobutler (2021-06-02 01:01 UTC)

<p>The problem commit is probably the same one I posted about in <a href="https://github.com/Slicer/Slicer/issues/5550" class="inline-onebox" rel="noopener nofollow ugc">Slice intersections appear white in 3D view when no volume displayed · Issue #5550 · Slicer/Slicer · GitHub</a></p>

---
