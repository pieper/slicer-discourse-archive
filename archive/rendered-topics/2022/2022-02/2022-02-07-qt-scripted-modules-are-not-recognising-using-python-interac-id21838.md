---
topic_id: 21838
title: "Qt Scripted Modules Are Not Recognising Using Python Interac"
date: 2022-02-07
url: https://discourse.slicer.org/t/21838
---

# Qt-scripted-modules are not recognising using python interacter in slicer

**Topic ID**: 21838
**Date**: 2022-02-07
**URL**: https://discourse.slicer.org/t/qt-scripted-modules-are-not-recognising-using-python-interacter-in-slicer/21838

---

## Post #1 by @Mahesh_Timmanagoudar (2022-02-07 13:49 UTC)

<p>I have two python files.<br>
1)plan.py<br>
2)manager.py</p>
<p>plan.py - is like below.</p>
<p>import manager<br>
def plan(baseDir=None):<br>
m = manager.managerLogic(baseDir)<br>
m.load(‘plan’)<br>
plan()</p>
<p>Whenever I tried like below commands Its working using python interacter in slicer.</p>
<p>import plan<br>
plan.plan()</p>
<p>But when i try like below. Its not working.</p>
<p>import plan</p>
<p>I have added above file inside scripting file also. (compile_Slicer_python_scripts.py). building is also fine.</p>
<p>ctk_compile_file(‘D:/W2/S-r/S-bld/Slicer-build/lib/Slicer-4.13/qt-scripted-modules/plan.py’, force=1)</p>
<p>May I know what is the issue here?</p>
<p>Why python module is not initiating by default?</p>
<p>I got some error message after launching the application. The log looks like below.</p>
<p>[CRITICAL][Stream] 07.02.2022 10:24:19 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 07.02.2022 10:24:19 [] (unknown:0) -   File “”, line 1, in <br>
[CRITICAL][Stream] 07.02.2022 10:24:19 [] (unknown:0) -   File “D:\W2\S-r\S-bld\python-install\Lib\imp.py”, line 170, in load_source<br>
[CRITICAL][Stream] 07.02.2022 10:24:19 [] (unknown:0) -     module = _exec(spec, sys.modules[name])<br>
[CRITICAL][Stream] 07.02.2022 10:24:19 [] (unknown:0) -   File “”, line 618, in _exec<br>
[CRITICAL][Stream] 07.02.2022 10:24:19 [] (unknown:0) -   File “”, line 678, in exec_module<br>
[CRITICAL][Stream] 07.02.2022 10:24:19 [] (unknown:0) -   File “”, line 219, in _call_with_frames_removed<br>
[CRITICAL][Stream] 07.02.2022 10:24:19 [] (unknown:0) -   File “D:/W2/S-r/S-bld/Slicer-build/lib/Slicer-4.13/qt-scripted-modules/plan.py”, line 11, in <br>
[CRITICAL][Stream] 07.02.2022 10:24:19 [] (unknown:0) -     plan()<br>
[CRITICAL][Stream] 07.02.2022 10:24:19 [] (unknown:0) -   File “D:/W2/S-r/S-bld/Slicer-build/lib/Slicer-4.13/qt-scripted-modules/plan.py”, line 9, in plan<br>
[CRITICAL][Stream] 07.02.2022 10:24:19 [] (unknown:0) -     m.load(‘plan’)<br>
[CRITICAL][Stream] 07.02.2022 10:24:19 [] (unknown:0) -   File “D:/W2/S-r/S-bld/Slicer-build/lib/Slicer-4.13/qt-scripted-modules/manager.py”, line 524, in load<br>
[CRITICAL][Stream] 07.02.2022 10:24:19 [] (unknown:0) -     lm.setLayout(3)<br>
[CRITICAL][Stream] 07.02.2022 10:24:19 [] (unknown:0) - AttributeError: ‘NoneType’ object has no attribute ‘setLayout’<br>
[CRITICAL][Qt] 07.02.2022 10:24:19 [] (unknown:0) - loadSourceAsModule - Failed to load file “D:/W2/S-r/S-bld/Slicer-build/lib/Slicer-4.13/qt-scripted-modules/plan.py”  as module “plan” !<br>
[CRITICAL][Qt] 07.02.2022 10:24:19 [] (unknown:0) - Fail to instantiate module  “plan”</p>

---
