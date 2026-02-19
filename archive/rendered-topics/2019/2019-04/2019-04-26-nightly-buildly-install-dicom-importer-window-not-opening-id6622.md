---
topic_id: 6622
title: "Nightly Buildly Install Dicom Importer Window Not Opening"
date: 2019-04-26
url: https://discourse.slicer.org/t/6622
---

# Nightly Buildly Install- Dicom Importer Window not opening

**Topic ID**: 6622
**Date**: 2019-04-26
**URL**: https://discourse.slicer.org/t/nightly-buildly-install-dicom-importer-window-not-opening/6622

---

## Post #1 by @Kate_Serralde (2019-04-26 16:12 UTC)

<p>Problem report for Slicer 4.11.0-2019-04-17 macosx-amd64: [please describe expected and actual behavior]</p>
<p>dicom widget has no attribute</p>
<details>
<summary>
Application log</summary>
<pre><code>[DEBUG][Qt] 26.04.2019 10:15:05 [] (unknown:0) - Session start time .......: 2019-04-26 10:15:05
[DEBUG][Qt] 26.04.2019 10:15:05 [] (unknown:0) - Slicer version ...........: 4.11.0-2019-04-17 (revision 28152) macosx-amd64 - installed release
[DEBUG][Qt] 26.04.2019 10:15:05 [] (unknown:0) - Operating system .........: Mac OS X / 10.12.6 / 16G1918 - 64-bit
[DEBUG][Qt] 26.04.2019 10:15:05 [] (unknown:0) - Memory ...................: 65536 MB physical, 0 MB virtual
[DEBUG][Qt] 26.04.2019 10:15:05 [] (unknown:0) - CPU ......................: GenuineIntel Intel(R) Xeon(R) CPU E5-1650 v2 @ 3.50GHz, 6 cores, 12 logical processors
[DEBUG][Qt] 26.04.2019 10:15:05 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, Sequential threading
[DEBUG][Qt] 26.04.2019 10:15:05 [] (unknown:0) - Developer mode enabled ...: yes
[DEBUG][Qt] 26.04.2019 10:15:05 [] (unknown:0) - Prefer executable CLI ....: no
[DEBUG][Qt] 26.04.2019 10:15:05 [] (unknown:0) - Additional module paths ..: /Applications/Slicer.app/Contents/Extensions-28152/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-28152/MarkupsToModel/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer.app/Contents/Extensions-28152/OpenCAD/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-28152/IntensitySegmenter/lib/Slicer-4.11/cli-modules, /Applications/Slicer.app/Contents/Extensions-28152/SwissSkullStripper/lib/Slicer-4.11/cli-modules, /Applications/Slicer.app/Contents/Extensions-28152/SwissSkullStripper/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-28152/SegmentationWizard/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-28152/SegmentMesher/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-28152/Autoscroll/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-28152/DCMQI/lib/Slicer-4.11/cli-modules, /Applications/Slicer.app/Contents/Extensions-28152/ShapePopulationViewer/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer.app/Contents/Extensions-28152/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-28152/ModelToModelDistance/lib/Slicer-4.11/cli-modules, /Applications/Slicer.app/Contents/Extensions-28152/CMFreg/lib/Slicer-4.11/cli-modules, /Applications/Slicer.app/Contents/Extensions-28152/CMFreg/lib/Slicer-4.11/qt-scripted-modules
[DEBUG][Python] 26.04.2019 10:15:07 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 26.04.2019 10:15:11 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 26.04.2019 10:15:11 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 26.04.2019 10:15:13 [] (unknown:0) - Switch to module:  "Welcome"
[CRITICAL][Stream] 26.04.2019 10:15:13 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 26.04.2019 10:15:13 [] (unknown:0) -   File "/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/DICOM.py", line 72, in performPostModuleDiscoveryTasks
[CRITICAL][Stream] 26.04.2019 10:15:13 [] (unknown:0) -     self.startListener()
[CRITICAL][Stream] 26.04.2019 10:15:13 [] (unknown:0) -   File "/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/DICOM.py", line 94, in startListener
[CRITICAL][Stream] 26.04.2019 10:15:13 [] (unknown:0) -     slicer.dicomListener.start()
[CRITICAL][Stream] 26.04.2019 10:15:13 [] (unknown:0) -   File "/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/DICOMLib/DICOMProcesses.py", line 159, in start
[CRITICAL][Stream] 26.04.2019 10:15:13 [] (unknown:0) -     if self.killStoreSCPProcesses():
[CRITICAL][Stream] 26.04.2019 10:15:13 [] (unknown:0) -   File "/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/DICOMLib/DICOMProcesses.py", line 175, in killStoreSCPProcesses
[CRITICAL][Stream] 26.04.2019 10:15:13 [] (unknown:0) -     uniqueListener = self.killStoreSCPProcessesPosix(uniqueListener)
[CRITICAL][Stream] 26.04.2019 10:15:13 [] (unknown:0) -   File "/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/DICOMLib/DICOMProcesses.py", line 182, in killStoreSCPProcessesPosix
[CRITICAL][Stream] 26.04.2019 10:15:13 [] (unknown:0) -     if self.STORESCP_PROCESS_FILE_NAME in line:
[CRITICAL][Stream] 26.04.2019 10:15:13 [] (unknown:0) - TypeError: a bytes-like object is required, not 'str'
[DEBUG][Qt] 26.04.2019 10:15:56 [] (unknown:0) - Switch to module:  "DICOM"
[CRITICAL][Stream] 26.04.2019 10:15:56 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 26.04.2019 10:15:56 [] (unknown:0) -   File "/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/DICOM.py", line 357, in setup
[CRITICAL][Stream] 26.04.2019 10:15:56 [] (unknown:0) -     slicer.dicomListener.process.connect('stateChanged(QProcess::ProcessState)',self.onListenerStateChanged)
[CRITICAL][Stream] 26.04.2019 10:15:56 [] (unknown:0) - AttributeError: 'NoneType' object has no attribute 'connect'
[CRITICAL][Stream] 26.04.2019 10:15:56 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 26.04.2019 10:15:56 [] (unknown:0) -   File "/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/DICOM.py", line 315, in enter
[CRITICAL][Stream] 26.04.2019 10:15:56 [] (unknown:0) -     self.onOpenDetailsPopup()
[CRITICAL][Stream] 26.04.2019 10:15:56 [] (unknown:0) -   File "/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/DICOM.py", line 415, in onOpenDetailsPopup
[CRITICAL][Stream] 26.04.2019 10:15:56 [] (unknown:0) -     if not isinstance(self.detailsPopup, self.getSavedDICOMDetailsWidgetType()):
[CRITICAL][Stream] 26.04.2019 10:15:56 [] (unknown:0) - AttributeError: 'DICOMWidget' object has no attribute 'detailsPopup'
[CRITICAL][Stream] 26.04.2019 10:18:15 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 26.04.2019 10:18:15 [] (unknown:0) -   File "/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/DICOM.py", line 248, in dropEvent
[CRITICAL][Stream] 26.04.2019 10:18:15 [] (unknown:0) -     dicomWidget.detailsPopup.dicomBrowser.importDirectories(self.directoriesToAdd)
[CRITICAL][Stream] 26.04.2019 10:18:15 [] (unknown:0) - AttributeError: 'DICOMWidget' object has no attribute 'detailsPopup'
[DEBUG][Qt] 26.04.2019 10:18:18 [] (unknown:0) - Switch to module:  "Volumes"
[CRITICAL][Stream] 26.04.2019 10:18:18 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 26.04.2019 10:18:18 [] (unknown:0) -   File "/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/DICOM.py", line 318, in exit
[CRITICAL][Stream] 26.04.2019 10:18:18 [] (unknown:0) -     if not self.detailsPopup.browserPersistent:
[CRITICAL][Stream] 26.04.2019 10:18:18 [] (unknown:0) - AttributeError: 'DICOMWidget' object has no attribute 'detailsPopup'
[DEBUG][Qt] 26.04.2019 10:18:25 [] (unknown:0) - Switch to module:  "ViewControllers"
[DEBUG][Qt] 26.04.2019 10:34:02 [] (unknown:0) - Switch to module:  "DICOM"
[CRITICAL][Stream] 26.04.2019 10:34:02 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 26.04.2019 10:34:02 [] (unknown:0) -   File "/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/DICOM.py", line 315, in enter
[CRITICAL][Stream] 26.04.2019 10:34:02 [] (unknown:0) -     self.onOpenDetailsPopup()
[CRITICAL][Stream] 26.04.2019 10:34:02 [] (unknown:0) -   File "/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/DICOM.py", line 415, in onOpenDetailsPopup
[CRITICAL][Stream] 26.04.2019 10:34:02 [] (unknown:0) -     if not isinstance(self.detailsPopup, self.getSavedDICOMDetailsWidgetType()):
[CRITICAL][Stream] 26.04.2019 10:34:02 [] (unknown:0) - AttributeError: 'DICOMWidget' object has no attribute 'detailsPopup'
</code></pre>
</details>

---

## Post #2 by @lassoan (2019-04-26 16:23 UTC)

<p>It seems that the DICOM listener broke due to the recent switch to Python3.</p>
<p>For now, you need to disable the DICOM listener by copy-pasting this to the Python console:</p>
<pre><code>slicer.app.settings().setValue("DICOM/RunListenerAtStart", False)
</code></pre>
<p>After you restart Slicer, everything should work well.</p>
<p>We are doing large refactoring work in Slicer nightly builds, so unless you rely on a recent fix or improvement in the nightly builds, it may be better to use the latest stable version for a few more months.</p>

---

## Post #3 by @pieper (2019-04-26 17:51 UTC)

<p>Thanks for reporting <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>Should be <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28186">fixed in the next nightly</a>.</p>

---

## Post #4 by @muratmaga (2019-04-26 19:55 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="6622">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We are doing large refactoring work in Slicer nightly builds, so unless you rely on a recent fix or improvement in the nightly builds, it may be better to use the latest stable version for a few more months.</p>
</blockquote>
</aside>
<p>It might be useful to post a similar message to the download page as well…</p>

---

## Post #5 by @lassoan (2019-04-26 20:07 UTC)

<p>I fully agree. We are waiting on <a class="mention" href="/u/mhalle">@mhalle</a> to give us write access to the download page.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #6 by @pieper (2019-04-26 21:18 UTC)

<aside class="quote no-group quote-modified" data-username="muratmaga" data-post="4" data-topic="6622">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<blockquote>
<p>We are doing large refactoring work in Slicer nightly builds, so unless you rely on a recent fix or improvement in the nightly builds, it may be better to use the latest stable version for a few more months.</p>
</blockquote>
<p>It might be useful to post a similar message to the download page as well…</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="6622" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I fully agree. We are waiting on <a class="mention" href="/u/mhalle">@mhalle</a> to give us write access to the download page.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>
</blockquote>
</aside>
<p>Agreed - let me try again.</p>

---
