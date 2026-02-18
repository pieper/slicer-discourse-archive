# Incomplete options in SlicerCIP (SlicerCIP4-10-2) on Windows (Windows 7 Enterprise, Service Pack 1) and Linux (Ubuntu 18.04.4 LTS)

**Topic ID**: 13067
**Date**: 2020-08-18
**URL**: https://discourse.slicer.org/t/incomplete-options-in-slicercip-slicercip4-10-2-on-windows-windows-7-enterprise-service-pack-1-and-linux-ubuntu-18-04-4-lts/13067

---

## Post #1 by @shahrokh (2020-08-18 09:58 UTC)

<p>Hello Dear Developers and Users</p>
<p>As mentioned on the sixth page of this file in <a href="https://chestimagingplatform.org/files/chestimagingplatform/files/interactivelobesegmentation_tutorial_pn.pdf" rel="nofollow noopener">Interactive Lobe segmentation</a>, when filtering is ”on” I expect to open a new frame opens for selecting filter type (NLM, Median and Gaussian), but it is not occurred for me.</p>
<p>I installed last version of SlicerCIP (SlicerCIP4-10-2) on Windows (Windows 7 Enterprise, Service Pack 1) and Linux (Ubuntu 18.04.4 LTS) and I do not this option (selecting filter). Why?</p>
<p>Please guide me.</p>
<p>Thanks a lot.</p>
<p>Shahrokh</p>

---

## Post #2 by @lassoan (2020-08-18 14:00 UTC)

<p>Do you see any error messages in application log (menu: Help / Report a bug)?</p>

---

## Post #3 by @shahrokh (2020-08-19 04:45 UTC)

<p>When I run it in Ubuntu:</p>
<p>sn@MP:~$ cd /home/sn/SlicerCIP4-10-2-linux/SlicerCIP4-10-2</p>
<p>sn@MP:~/SlicerCIP4-10-2-linux/SlicerCIP4-10-2$ ./SlicerCIP4-10-2</p>
<p>I get the following log message:</p>
<blockquote>
<p>[DEBUG][Qt] 19.08.2020 09:22:33 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 2020-08-19 09:22:33<br>
[DEBUG][Qt] 19.08.2020 09:22:33 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 4.10.2 (revision 28257) linux-amd64 - installed release<br>
[DEBUG][Qt] 19.08.2020 09:22:33 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Linux / 5.4.0-42-generic / #46~18.04.1-Ubuntu SMP Fri Jul 10 07:21:24 UTC 2020 - 64-bit<br>
[DEBUG][Qt] 19.08.2020 09:22:33 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 15864 MB physical, 2047 MB virtual<br>
[DEBUG][Qt] 19.08.2020 09:22:33 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel Intel(R) Core™ i7-9700K CPU @ 3.60GHz, 8 cores, 8 logical processors<br>
[DEBUG][Qt] 19.08.2020 09:22:33 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, Sequential threading<br>
[DEBUG][Qt] 19.08.2020 09:22:33 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 19.08.2020 09:22:33 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 19.08.2020 09:22:33 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: /home/sn/SlicerCIP4-10-2-linux/SlicerCIP4-10-2/bin/…/SlicerCIP4-10-2-Extensions/Chest_Imaging_Platform/lib/Slicer-4.10/cli-modules, /home/sn/SlicerCIP4-10-2-linux/SlicerCIP4-10-2/bin/…/SlicerCIP4-10-2-Extensions/Chest_Imaging_Platform/lib/Slicer-4.10/qt-loadable-modules, /home/sn/SlicerCIP4-10-2-linux/SlicerCIP4-10-2/bin/…/SlicerCIP4-10-2-Extensions/Chest_Imaging_Platform/lib/Slicer-4.10/qt-scripted-modules<br>
[CRITICAL][Qt] 19.08.2020 09:22:34 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Error(s):<br>
Cannot load library /home/sn/SlicerCIP4-10-2-linux/SlicerCIP4-10-2/SlicerCIP4-10-2-Extensions/Chest_Imaging_Platform/lib/Slicer-4.10/qt-loadable-modules/libqSlicerAirwayInspectorModule.so: (libvtkSlicerAirwayInspectorModuleLogic.so: cannot open shared object file: No such file or directory)<br>
[CRITICAL][Qt] 19.08.2020 09:22:34 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Error(s):<br>
Cannot load library /home/sn/SlicerCIP4-10-2-linux/SlicerCIP4-10-2/SlicerCIP4-10-2-Extensions/Chest_Imaging_Platform/lib/Slicer-4.10/qt-loadable-modules/libqSlicerParticlesDisplayModule.so: (libvtkSlicerParticlesDisplayModuleLogic.so: cannot open shared object file: No such file or directory)<br>
[CRITICAL][Qt] 19.08.2020 09:22:34 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Error(s):<br>
Cannot load library /home/sn/SlicerCIP4-10-2-linux/SlicerCIP4-10-2/SlicerCIP4-10-2-Extensions/Chest_Imaging_Platform/lib/Slicer-4.10/qt-loadable-modules/libqSlicerRegionTypeModule.so: (libvtkSlicerRegionTypeModuleLogic.so: cannot open shared object file: No such file or directory)<br>
[ERROR][Python] 19.08.2020 09:22:36 [Python] (/home/sn/SlicerCIP4-10-2-linux/SlicerCIP4-10-2/lib/Slicer-4.10/qt-scripted-modules/SubjectHierarchyPlugins/<strong>init</strong>.py:16) - Failed to import ._<strong>init</strong>: Traceback (most recent call last):<br>
File “/home/sn/SlicerCIP4-10-2-linux/SlicerCIP4-10-2/lib/Slicer-4.10/qt-scripted-modules/SubjectHierarchyPlugins/<strong>init</strong>.py”, line 14, in <br>
exec(importStr)<br>
File “”, line 1, in <br>
ImportError: No module named _<strong>init</strong><br>
[ERROR][Python] 19.08.2020 09:22:36 [Python] (/home/sn/SlicerCIP4-10-2-linux/SlicerCIP4-10-2/lib/Slicer-4.10/qt-scripted-modules/SubjectHierarchyPlugins/<strong>init</strong>.py:16) - Failed to import ._AbstractScriptedSubjectHierarchyPlugin: Traceback (most recent call last):<br>
File “/home/sn/SlicerCIP4-10-2-linux/SlicerCIP4-10-2/lib/Slicer-4.10/qt-scripted-modules/SubjectHierarchyPlugins/<strong>init</strong>.py”, line 14, in <br>
exec(importStr)<br>
File “”, line 1, in <br>
ImportError: No module named _AbstractScriptedSubjectHierarchyPlugin<br>
[ERROR][Python] 19.08.2020 09:22:36 [Python] (/home/sn/SlicerCIP4-10-2-linux/SlicerCIP4-10-2/lib/Slicer-4.10/qt-scripted-modules/SubjectHierarchyPlugins/<strong>init</strong>.py:16) - Failed to import ._AnnotationsSubjectHierarchyPlugin: Traceback (most recent call last):<br>
File “/home/sn/SlicerCIP4-10-2-linux/SlicerCIP4-10-2/lib/Slicer-4.10/qt-scripted-modules/SubjectHierarchyPlugins/<strong>init</strong>.py”, line 14, in <br>
exec(importStr)<br>
File “”, line 1, in <br>
ImportError: No module named _AnnotationsSubjectHierarchyPlugin<br>
[ERROR][Python] 19.08.2020 09:22:36 [Python] (/home/sn/SlicerCIP4-10-2-linux/SlicerCIP4-10-2/lib/Slicer-4.10/qt-scripted-modules/SubjectHierarchyPlugins/<strong>init</strong>.py:16) - Failed to import ._SegmentEditorSubjectHierarchyPlugin: Traceback (most recent call last):<br>
File “/home/sn/SlicerCIP4-10-2-linux/SlicerCIP4-10-2/lib/Slicer-4.10/qt-scripted-modules/SubjectHierarchyPlugins/<strong>init</strong>.py”, line 14, in <br>
exec(importStr)<br>
File “”, line 1, in <br>
ImportError: No module named _SegmentEditorSubjectHierarchyPlugin<br>
[ERROR][Python] 19.08.2020 09:22:36 [Python] (/home/sn/SlicerCIP4-10-2-linux/SlicerCIP4-10-2/lib/Slicer-4.10/qt-scripted-modules/SubjectHierarchyPlugins/<strong>init</strong>.py:16) - Failed to import ._SegmentStatisticsSubjectHierarchyPlugin: Traceback (most recent call last):<br>
File “/home/sn/SlicerCIP4-10-2-linux/SlicerCIP4-10-2/lib/Slicer-4.10/qt-scripted-modules/SubjectHierarchyPlugins/<strong>init</strong>.py”, line 14, in <br>
exec(importStr)<br>
File “”, line 1, in <br>
ImportError: No module named _SegmentStatisticsSubjectHierarchyPlugin<br>
[DEBUG][Python] 19.08.2020 09:22:36 [Python] (/home/sn/SlicerCIP4-10-2-linux/SlicerCIP4-10-2/lib/Slicer-4.10/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[CRITICAL][Stream] 19.08.2020 09:22:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Failed to import ._<strong>init</strong>: Traceback (most recent call last):<br>
[CRITICAL][Stream] 19.08.2020 09:22:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “/home/sn/SlicerCIP4-10-2-linux/SlicerCIP4-10-2/lib/Slicer-4.10/qt-scripted-modules/SubjectHierarchyPlugins/<strong>init</strong>.py”, line 14, in <br>
[CRITICAL][Stream] 19.08.2020 09:22:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     exec(importStr)<br>
[CRITICAL][Stream] 19.08.2020 09:22:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “”, line 1, in <br>
[CRITICAL][Stream] 19.08.2020 09:22:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - ImportError: No module named _<strong>init</strong><br>
[CRITICAL][Stream] 19.08.2020 09:22:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -<br>
[CRITICAL][Stream] 19.08.2020 09:22:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Failed to import ._AbstractScriptedSubjectHierarchyPlugin: Traceback (most recent call last):<br>
[CRITICAL][Stream] 19.08.2020 09:22:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “/home/sn/SlicerCIP4-10-2-linux/SlicerCIP4-10-2/lib/Slicer-4.10/qt-scripted-modules/SubjectHierarchyPlugins/<strong>init</strong>.py”, line 14, in <br>
[CRITICAL][Stream] 19.08.2020 09:22:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     exec(importStr)<br>
[CRITICAL][Stream] 19.08.2020 09:22:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “”, line 1, in <br>
[CRITICAL][Stream] 19.08.2020 09:22:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - ImportError: No module named _AbstractScriptedSubjectHierarchyPlugin<br>
[CRITICAL][Stream] 19.08.2020 09:22:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -<br>
[CRITICAL][Stream] 19.08.2020 09:22:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Failed to import ._AnnotationsSubjectHierarchyPlugin: Traceback (most recent call last):<br>
[CRITICAL][Stream] 19.08.2020 09:22:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “/home/sn/SlicerCIP4-10-2-linux/SlicerCIP4-10-2/lib/Slicer-4.10/qt-scripted-modules/SubjectHierarchyPlugins/<strong>init</strong>.py”, line 14, in <br>
[CRITICAL][Stream] 19.08.2020 09:22:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     exec(importStr)<br>
[CRITICAL][Stream] 19.08.2020 09:22:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “”, line 1, in <br>
[CRITICAL][Stream] 19.08.2020 09:22:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - ImportError: No module named _AnnotationsSubjectHierarchyPlugin<br>
[CRITICAL][Stream] 19.08.2020 09:22:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -<br>
[CRITICAL][Stream] 19.08.2020 09:22:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Failed to import ._SegmentEditorSubjectHierarchyPlugin: Traceback (most recent call last):<br>
[CRITICAL][Stream] 19.08.2020 09:22:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “/home/sn/SlicerCIP4-10-2-linux/SlicerCIP4-10-2/lib/Slicer-4.10/qt-scripted-modules/SubjectHierarchyPlugins/<strong>init</strong>.py”, line 14, in <br>
[CRITICAL][Stream] 19.08.2020 09:22:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     exec(importStr)<br>
[CRITICAL][Stream] 19.08.2020 09:22:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “”, line 1, in <br>
[CRITICAL][Stream] 19.08.2020 09:22:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - ImportError: No module named _SegmentEditorSubjectHierarchyPlugin<br>
[CRITICAL][Stream] 19.08.2020 09:22:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -<br>
[CRITICAL][Stream] 19.08.2020 09:22:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Failed to import ._SegmentStatisticsSubjectHierarchyPlugin: Traceback (most recent call last):<br>
[CRITICAL][Stream] 19.08.2020 09:22:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “/home/sn/SlicerCIP4-10-2-linux/SlicerCIP4-10-2/lib/Slicer-4.10/qt-scripted-modules/SubjectHierarchyPlugins/<strong>init</strong>.py”, line 14, in <br>
[CRITICAL][Stream] 19.08.2020 09:22:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     exec(importStr)<br>
[CRITICAL][Stream] 19.08.2020 09:22:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “”, line 1, in <br>
[CRITICAL][Stream] 19.08.2020 09:22:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - ImportError: No module named _SegmentStatisticsSubjectHierarchyPlugin<br>
[CRITICAL][Stream] 19.08.2020 09:22:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -<br>
[DEBUG][Python] 19.08.2020 09:22:36 [Python] (/home/sn/SlicerCIP4-10-2-linux/SlicerCIP4-10-2/lib/Slicer-4.10/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Qt] 19.08.2020 09:22:37 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”</p>
</blockquote>
<p>In Windows:</p>
<blockquote>
<p>[DEBUG][Qt] ??.??.??? ??:??:?? <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: ???-??-?? ??:??:??</p>
<p>[DEBUG][Qt] ??.??.??? ??:??:?? <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 4.11.0-2020-07-18 (revision 29221 / 26fbefd) win-amd64 - installed release</p>
<p>[DEBUG][Qt] ??.??.??? ??:??:?? <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows / 7 / (Build 7601, Code Page 1256) - 64-bit</p>
<p>[DEBUG][Qt] ??.??.??? ??:??:?? <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 8076 MB physical, 16150 MB virtual</p>
<p>[DEBUG][Qt] ??.??.??? ??:??:?? <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel , 8 cores, 8 logical processors</p>
<p>[DEBUG][Qt] ??.??.??? ??:??:?? <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading</p>
<p>[DEBUG][Qt] ??.??.??? ??:??:?? <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.0, with SSL, requested OpenGL 3.2 (compatibility profile)</p>
<p>[DEBUG][Qt] ??.??.??? ??:??:?? <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode enabled …: no</p>
<p>[DEBUG][Qt] ??.??.??? ??:??:?? <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Prefer executable CLI …: yes</p>
<p>[DEBUG][Qt] ??.??.??? ??:??:?? <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: C:/Users/naserish/AppData/Local/NA-MIC/Slicer 4.11.0-2020-07-18/bin</p>
<p>[DEBUG][Qt] ??.??.??? ??:??:?? <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: C:/Users/naserish/AppData/Roaming/NA-MIC/Extensions-29221/Chest_Imaging_Platform/lib/Slicer-4.11/cli-modules, C:/Users/naserish/AppData/Roaming/NA-MIC/Extensions-29221/Chest_Imaging_Platform/lib/Slicer-4.11/qt-loadable-modules, C:/Users/naserish/AppData/Roaming/NA-MIC/Extensions-29221/Chest_Imaging_Platform/lib/Slicer-4.11/qt-scripted-modules</p>
<p>[CRITICAL][Stream] ??.??.??? ??:??:?? <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Traceback (most recent call last):</p>
<p>[CRITICAL][Stream] ??.??.??? ??:??:?? <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - File “”, line 1, in </p>
<p>[CRITICAL][Stream] ??.??.??? ??:??:?? <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - File “C:\Users\naserish\AppData\Local\NA-MIC\Slicer 4.11.0-2020-07-18\lib\Python\Lib\imp.py”, line 170, in load_source</p>
<p>[CRITICAL][Stream] ??.??.??? ??:??:?? <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - module = _exec(spec, sys.modules[name])</p>
<p>[CRITICAL][Stream] ??.??.??? ??:??:?? <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - File “”, line 618, in _exec</p>
<p>[CRITICAL][Stream] ??.??.??? ??:??:?? <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - File “”, line 678, in exec_module</p>
<p>[CRITICAL][Stream] ??.??.??? ??:??:?? <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - File “”, line 219, in _call_with_frames_removed</p>
<p>[CRITICAL][Stream] ??.??.??? ??:??:?? <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - File “C:/Users/naserish/AppData/Roaming/NA-MIC/Extensions-29221/Chest_Imaging_Platform/lib/Slicer-4.11/qt-scripted-modules/CIP_BodyComposition.py”, line 18, in </p>
<p>[CRITICAL][Stream] ??.??.??? ??:??:?? <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - from .CIP_BodyComposition_logic import BodyCompositionParameters</p>
<p>[CRITICAL][Stream] ??.??.??? ??:??:?? <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - ImportError: attempted relative import with no known parent package</p>
<p>[CRITICAL][Qt] ??.??.??? ??:??:?? <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - loadSourceAsModule - Failed to load file “C:/Users/naserish/AppData/Roaming/NA-MIC/Extensions-29221/Chest_Imaging_Platform/lib/Slicer-4.11/qt-scripted-modules/CIP_BodyComposition.py” as module “CIP_BodyComposition” !</p>
<p>[CRITICAL][Qt] ??.??.??? ??:??:?? <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Fail to instantiate module “CIP_BodyComposition”</p>
<p>[CRITICAL][Qt] ??.??.??? ??:??:?? <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - The following modules failed to be instantiated:</p>
<p>[CRITICAL][Qt] ??.??.??? ??:??:?? <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CIP_BodyComposition</p>
<p>[DEBUG][Python] ??.??.??? ??:??:?? [Python] (C:\Users\naserish\AppData\Local\NA-MIC\Slicer 4.11.0-2020-07-18\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations</p>
<p>[WARNING][Qt] ??.??.??? ??:??:?? <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - When loading module “ParticlesDisplay” , the dependency “TractographyDisplay” failed to be loaded.</p>
<p>[DEBUG][Python] ??.??.??? ??:??:?? [Python] (C:\Users\naserish\AppData\Local\NA-MIC\Slicer 4.11.0-2020-07-18\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor</p>
<p>[DEBUG][Python] ??.??.??? ??:??:?? [Python] (C:\Users\naserish\AppData\Local\NA-MIC\Slicer 4.11.0-2020-07-18\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics</p>
<p>[DEBUG][Qt] ??.??.??? ??:??:?? <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module: “Welcome”</p>
</blockquote>
<p>Best regards.</p>

---

## Post #4 by @lassoan (2020-08-19 04:56 UTC)

<p>I’ve tried the latest Slicer Preview Release on Windows and it worked well.</p>

---

## Post #5 by @shahrokh (2020-08-19 05:10 UTC)

<p>Thanks a lot</p>
<p>Anyway, I still get these errors. I found a solution to this problem. I find filters available when filtering is ON (NLM, Median and Gaussian) in <strong>Processing</strong> category of <strong>Chest Imaging Platform</strong> which include: <strong>GenerateNLMFilteredImage</strong> and <strong>GenerateMedianFilteredImage</strong>.</p>

---
