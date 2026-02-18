# Errors while loading Slicer nightly

**Topic ID**: 6540
**Date**: 2019-04-19
**URL**: https://discourse.slicer.org/t/errors-while-loading-slicer-nightly/6540

---

## Post #1 by @Alex_Vergara (2019-04-19 09:13 UTC)

<p>When I start nightly these errors appear in debug console:</p>
<pre><code class="lang-auto">[DEBUG][Qt] 17.04.2019 17:11:18 [] (unknown:0) - Session start time .......: 2019-04-17 17:11:18
[DEBUG][Qt] 17.04.2019 17:11:18 [] (unknown:0) - Slicer version ...........: 4.11.0-2019-04-12 (revision 28138) macosx-amd64 - installed release
[DEBUG][Qt] 17.04.2019 17:11:18 [] (unknown:0) - Operating system .........: Mac OS X / 10.14.4 / 18E226 - 64-bit
[DEBUG][Qt] 17.04.2019 17:11:18 [] (unknown:0) - Memory ...................: 8192 MB physical, 4096 MB virtual
[DEBUG][Qt] 17.04.2019 17:11:18 [] (unknown:0) - CPU ......................: GenuineIntel Intel(R) Core(TM) i7-4750HQ CPU @ 2.00GHz, 4 cores, 8 logical processors
[DEBUG][Qt] 17.04.2019 17:11:18 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, Sequential threading
[DEBUG][Qt] 17.04.2019 17:11:18 [] (unknown:0) - Developer mode enabled ...: yes
[DEBUG][Qt] 17.04.2019 17:11:18 [] (unknown:0) - Prefer executable CLI ....: no
[DEBUG][Qt] 17.04.2019 17:11:18 [] (unknown:0) - Additional module paths ..: /Users/alex/GIT/SlicerExtensions/Dosimetry/Dosimetry4D, /Users/alex/Applications/Slicer.app/Contents/Extensions-28138/SlicerJupyter/lib/Slicer-4.11/qt-loadable-modules, /Users/alex/Applications/Slicer.app/Contents/Extensions-28138/PETDICOMExtension/lib/Slicer-4.11/cli-modules, /Users/alex/Applications/Slicer.app/Contents/Extensions-28138/PETDICOMExtension/lib/Slicer-4.11/qt-scripted-modules, /Users/alex/Applications/Slicer.app/Contents/Extensions-28138/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules, /Users/alex/Applications/Slicer.app/Contents/Extensions-28138/MarkupsToModel/lib/Slicer-4.11/qt-loadable-modules, /Users/alex/Applications/Slicer.app/Contents/Extensions-28138/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules, /Users/alex/Applications/Slicer.app/Contents/Extensions-28138/SlicerRT/lib/Slicer-4.11/cli-modules, /Users/alex/Applications/Slicer.app/Contents/Extensions-28138/SlicerRT/lib/Slicer-4.11/qt-loadable-modules, /Users/alex/Applications/Slicer.app/Contents/Extensions-28138/SlicerRT/lib/Slicer-4.11/qt-scripted-modules
[DEBUG][Python] 17.04.2019 17:11:22 [Python] (/Users/alex/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pip/_internal/utils/misc.py:90) - lzma module is not available
[DEBUG][Python] 17.04.2019 17:11:23 [Python] (/Users/alex/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pip/_internal/vcs/__init__.py:144) - Registered VCS backend: git
[DEBUG][Python] 17.04.2019 17:11:23 [Python] (/Users/alex/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pip/_internal/vcs/__init__.py:144) - Registered VCS backend: hg
[DEBUG][Python] 17.04.2019 17:11:23 [Python] (/Users/alex/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pip/_internal/vcs/__init__.py:144) - Registered VCS backend: svn
[DEBUG][Python] 17.04.2019 17:11:23 [Python] (/Users/alex/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pip/_internal/vcs/__init__.py:144) - Registered VCS backend: bzr
[CRITICAL][Stream] 17.04.2019 17:11:21 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 17.04.2019 17:11:21 [] (unknown:0) -   File "&lt;string&gt;", line 1, in &lt;module&gt;
[CRITICAL][Stream] 17.04.2019 17:11:21 [] (unknown:0) -   File "/Users/alex/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/imp.py", line 170, in load_source
[CRITICAL][Stream] 17.04.2019 17:11:21 [] (unknown:0) -     module = _exec(spec, sys.modules[name])
[CRITICAL][Stream] 17.04.2019 17:11:21 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
[CRITICAL][Stream] 17.04.2019 17:11:21 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap_external&gt;", line 674, in exec_module
[CRITICAL][Stream] 17.04.2019 17:11:21 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap_external&gt;", line 781, in get_code
[CRITICAL][Stream] 17.04.2019 17:11:21 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap_external&gt;", line 741, in source_to_code
[CRITICAL][Stream] 17.04.2019 17:11:21 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
[CRITICAL][Stream] 17.04.2019 17:11:21 [] (unknown:0) -   File "/Users/alex/Applications/Slicer.app/Contents/Extensions-28138/SlicerRT/lib/Slicer-4.11/qt-scripted-modules/BatchStructureSetConversion.py", line 233
[CRITICAL][Stream] 17.04.2019 17:11:21 [] (unknown:0) -     except Exception, e:
[CRITICAL][Stream] 17.04.2019 17:11:21 [] (unknown:0) -                     ^
[CRITICAL][Stream] 17.04.2019 17:11:21 [] (unknown:0) - SyntaxError: invalid syntax
[CRITICAL][Qt] 17.04.2019 17:11:21 [] (unknown:0) - loadSourceAsModule - Failed to load file "/Users/alex/Applications/Slicer.app/Contents/Extensions-28138/SlicerRT/lib/Slicer-4.11/qt-scripted-modules/BatchStructureSetConversion.py"  as module "BatchStructureSetConversion" !
[CRITICAL][Qt] 17.04.2019 17:11:21 [] (unknown:0) - Fail to instantiate module  "BatchStructureSetConversion"
[CRITICAL][Stream] 17.04.2019 17:11:23 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 17.04.2019 17:11:23 [] (unknown:0) -   File "&lt;string&gt;", line 1, in &lt;module&gt;
[CRITICAL][Stream] 17.04.2019 17:11:23 [] (unknown:0) -   File "/Users/alex/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/imp.py", line 170, in load_source
[CRITICAL][Stream] 17.04.2019 17:11:23 [] (unknown:0) -     module = _exec(spec, sys.modules[name])
[CRITICAL][Stream] 17.04.2019 17:11:23 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
[CRITICAL][Stream] 17.04.2019 17:11:23 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap_external&gt;", line 674, in exec_module
[CRITICAL][Stream] 17.04.2019 17:11:23 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap_external&gt;", line 781, in get_code
[CRITICAL][Stream] 17.04.2019 17:11:23 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap_external&gt;", line 741, in source_to_code
[CRITICAL][Stream] 17.04.2019 17:11:23 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
[CRITICAL][Stream] 17.04.2019 17:11:23 [] (unknown:0) -   File "/Users/alex/Applications/Slicer.app/Contents/Extensions-28138/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules/Elastix.py", line 330
[CRITICAL][Stream] 17.04.2019 17:11:23 [] (unknown:0) -     print e
[CRITICAL][Stream] 17.04.2019 17:11:23 [] (unknown:0) -           ^
[CRITICAL][Stream] 17.04.2019 17:11:23 [] (unknown:0) - SyntaxError: Missing parentheses in call to 'print'. Did you mean print(e)?
[CRITICAL][Qt] 17.04.2019 17:11:23 [] (unknown:0) - loadSourceAsModule - Failed to load file "/Users/alex/Applications/Slicer.app/Contents/Extensions-28138/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules/Elastix.py"  as module "Elastix" !
[CRITICAL][Qt] 17.04.2019 17:11:23 [] (unknown:0) - Fail to instantiate module  "Elastix"
[CRITICAL][Stream] 17.04.2019 17:11:23 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 17.04.2019 17:11:23 [] (unknown:0) -   File "&lt;string&gt;", line 1, in &lt;module&gt;
[CRITICAL][Stream] 17.04.2019 17:11:23 [] (unknown:0) -   File "/Users/alex/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/imp.py", line 170, in load_source
[CRITICAL][Stream] 17.04.2019 17:11:23 [] (unknown:0) -     module = _exec(spec, sys.modules[name])
[CRITICAL][Stream] 17.04.2019 17:11:23 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
[CRITICAL][Stream] 17.04.2019 17:11:23 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap_external&gt;", line 674, in exec_module
[CRITICAL][Stream] 17.04.2019 17:11:23 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap_external&gt;", line 781, in get_code
[CRITICAL][Stream] 17.04.2019 17:11:23 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap_external&gt;", line 741, in source_to_code
[CRITICAL][Stream] 17.04.2019 17:11:23 [] (unknown:0) -   File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
[CRITICAL][Stream] 17.04.2019 17:11:23 [] (unknown:0) -   File "/Users/alex/Applications/Slicer.app/Contents/Extensions-28138/SlicerRT/lib/Slicer-4.11/qt-scripted-modules/IGRTWorkflow_SelfTest.py", line 78
[CRITICAL][Stream] 17.04.2019 17:11:23 [] (unknown:0) -     except Exception, e:
[CRITICAL][Stream] 17.04.2019 17:11:23 [] (unknown:0) -                     ^
[CRITICAL][Stream] 17.04.2019 17:11:23 [] (unknown:0) - SyntaxError: invalid syntax
[CRITICAL][Qt] 17.04.2019 17:11:23 [] (unknown:0) - loadSourceAsModule - Failed to load file "/Users/alex/Applications/Slicer.app/Contents/Extensions-28138/SlicerRT/lib/Slicer-4.11/qt-scripted-modules/IGRTWorkflow_SelfTest.py"  as module "IGRTWorkflow_SelfTest" !
[CRITICAL][Qt] 17.04.2019 17:11:23 [] (unknown:0) - Fail to instantiate module  "IGRTWorkflow_SelfTest"
[CRITICAL][Stream] 17.04.2019 17:11:24 [] (unknown:0) - TypeError: __init__() missing 1 required positional argument: 'y'
[CRITICAL][Qt] 17.04.2019 17:11:24 [] (unknown:0) - qSlicerPythonCppAPI::instantiateClass  - [ "slicer_fit" ] - Failed to instantiate scripted pythonqt class "slicer_fit" 0x7fc401c44758
[CRITICAL][Qt] 17.04.2019 17:11:24 [] (unknown:0) - Fail to instantiate module  "slicer_fit"
[DEBUG][Python] 17.04.2019 17:11:27 [Python] (/Users/alex/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[CRITICAL][Stream] 17.04.2019 17:11:28 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 17.04.2019 17:11:28 [] (unknown:0) -   File "&lt;string&gt;", line 1, in &lt;module&gt;
[CRITICAL][Stream] 17.04.2019 17:11:28 [] (unknown:0) -   File "/Users/alex/Applications/Slicer.app/Contents/Extensions-28138/SlicerRT/lib/Slicer-4.11/qt-scripted-modules/DoseEngines/__init__.py", line 1, in &lt;module&gt;
[CRITICAL][Stream] 17.04.2019 17:11:28 [] (unknown:0) -     from AbstractScriptedDoseEngine import *
[CRITICAL][Stream] 17.04.2019 17:11:28 [] (unknown:0) - ModuleNotFoundError: No module named 'AbstractScriptedDoseEngine'
[DEBUG][Python] 17.04.2019 17:11:29 [Python] (/Users/alex/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 17.04.2019 17:11:29 [Python] (/Users/alex/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 17.04.2019 17:11:29 [] (unknown:0) - Switch to module:  "Welcome"
</code></pre>

---

## Post #2 by @pieper (2019-04-19 11:28 UTC)

<p>Thanks for reporting.  SlicerRT needs to be ported for python3.  For now you should use the 4.10.1 release if you need RT.</p>

---

## Post #3 by @Alex_Vergara (2019-04-19 12:49 UTC)

<p>I have tried loading the last nightly and errors are gone</p>
<pre><code class="lang-auto">[DEBUG][Qt] 19.04.2019 14:47:03 [] (unknown:0) - Session start time .......: 2019-04-19 14:47:03
[DEBUG][Qt] 19.04.2019 14:47:03 [] (unknown:0) - Slicer version ...........: 4.11.0-2019-04-17 (revision 28152) macosx-amd64 - installed release
[DEBUG][Qt] 19.04.2019 14:47:03 [] (unknown:0) - Operating system .........: Mac OS X / 10.14.4 / 18E226 - 64-bit
[DEBUG][Qt] 19.04.2019 14:47:03 [] (unknown:0) - Memory ...................: 8192 MB physical, 5120 MB virtual
[DEBUG][Qt] 19.04.2019 14:47:03 [] (unknown:0) - CPU ......................: GenuineIntel Intel(R) Core(TM) i7-4750HQ CPU @ 2.00GHz, 4 cores, 8 logical processors
[DEBUG][Qt] 19.04.2019 14:47:03 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, Sequential threading
[DEBUG][Qt] 19.04.2019 14:47:03 [] (unknown:0) - Developer mode enabled ...: yes
[DEBUG][Qt] 19.04.2019 14:47:03 [] (unknown:0) - Prefer executable CLI ....: no
[DEBUG][Qt] 19.04.2019 14:47:03 [] (unknown:0) - Additional module paths ..: /Users/alex/GIT/SlicerExtensions/Dosimetry/Dosimetry4D
[DEBUG][Python] 19.04.2019 14:47:05 [Python] (/Users/alex/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pip/_internal/utils/misc.py:90) - lzma module is not available
[DEBUG][Python] 19.04.2019 14:47:06 [Python] (/Users/alex/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pip/_internal/vcs/__init__.py:144) - Registered VCS backend: git
[DEBUG][Python] 19.04.2019 14:47:06 [Python] (/Users/alex/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pip/_internal/vcs/__init__.py:144) - Registered VCS backend: hg
[DEBUG][Python] 19.04.2019 14:47:06 [Python] (/Users/alex/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pip/_internal/vcs/__init__.py:144) - Registered VCS backend: svn
[DEBUG][Python] 19.04.2019 14:47:06 [Python] (/Users/alex/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pip/_internal/vcs/__init__.py:144) - Registered VCS backend: bzr
[DEBUG][Python] 19.04.2019 14:47:06 [Python] (/Users/alex/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pip/_internal/configuration.py:274) - For variant 'global', will try loading '/Library/Application Support/pip/pip.conf'
[DEBUG][Python] 19.04.2019 14:47:06 [Python] (/Users/alex/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pip/_internal/configuration.py:274) - For variant 'user', will try loading '/Users/alex/.pip/pip.conf'
[DEBUG][Python] 19.04.2019 14:47:06 [Python] (/Users/alex/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pip/_internal/configuration.py:274) - For variant 'user', will try loading '/Users/alex/.config/pip/pip.conf'
[DEBUG][Python] 19.04.2019 14:47:06 [Python] (/Users/alex/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pip/_internal/configuration.py:274) - For variant 'global', will try loading '/Library/Application Support/pip/pip.conf'
[DEBUG][Python] 19.04.2019 14:47:06 [Python] (/Users/alex/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pip/_internal/configuration.py:274) - For variant 'user', will try loading '/Users/alex/.pip/pip.conf'
[DEBUG][Python] 19.04.2019 14:47:06 [Python] (/Users/alex/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pip/_internal/configuration.py:274) - For variant 'user', will try loading '/Users/alex/.config/pip/pip.conf'
[DEBUG][Qt] 19.04.2019 14:47:18 [] (unknown:0) - Switch to module:  "Welcome"
</code></pre>

---
