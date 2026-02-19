---
topic_id: 1228
title: "Failed Build On Windows"
date: 2017-10-14
url: https://discourse.slicer.org/t/1228
---

# Failed build on Windows

**Topic ID**: 1228
**Date**: 2017-10-14
**URL**: https://discourse.slicer.org/t/failed-build-on-windows/1228

---

## Post #1 by @peterkshultz (2017-10-14 22:56 UTC)

<p><strong>Operating system:</strong> Windows 10<br>
<strong>Slicer version:</strong> 4.7.0-2010-10-10<br>
<strong>Expected behavior:</strong> Install and open build; open DICOM file.<br>
<strong>Actual behavior:</strong> Install and open build with some errors; cannot open DICOM file.</p>
<p>Full console output is here:</p>
<details>
<summary>
Console Log</summary>
<pre><code>    Number of registered modules: 140
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "C:/Users/peter/Desktop/debug/Slicer-build/lib/Slicer-4.7/qt-scripted-modules/DICOM.py", line 11, in &lt;module&gt;
    import DICOMLib
  File "C:\Users\peter\Desktop\debug\Slicer-build\lib\Slicer-4.7\qt-scripted-modules\DICOMLib\__init__.py", line 4, in &lt;module&gt;
    from DICOMWidgets import *
  File "C:\Users\peter\Desktop\debug\Slicer-build\lib\Slicer-4.7\qt-scripted-modules\DICOMLib\DICOMWidgets.py", line 8, in &lt;module&gt;
    from ctk import ctkDICOMObjectListWidget, ctkDICOMDatabase, ctkDICOMIndexer, ctkDICOMBrowser, ctkPopupWidget, ctkExpandButton
ImportError: cannot import name ctkPopupWidget
loadSourceAsModule - Failed to load file "C:/Users/peter/Desktop/debug/Slicer-build/lib/Slicer-4.7/qt-scripted-modules/DICOM.py"  as module "DICOM" !
Fail to instantiate module  "DICOM"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "C:/Users/peter/Desktop/debug/Slicer-build/lib/Slicer-4.7/qt-scripted-modules/DICOMScalarVolumePlugin.py", line 4, in &lt;module&gt;
    from DICOMLib import DICOMPlugin
  File "C:\Users\peter\Desktop\debug\Slicer-build\lib\Slicer-4.7\qt-scripted-modules\DICOMLib\__init__.py", line 4, in &lt;module&gt;
    from DICOMWidgets import *
  File "C:\Users\peter\Desktop\debug\Slicer-build\lib\Slicer-4.7\qt-scripted-modules\DICOMLib\DICOMWidgets.py", line 8, in &lt;module&gt;
    from ctk import ctkDICOMObjectListWidget, ctkDICOMDatabase, ctkDICOMIndexer, ctkDICOMBrowser, ctkPopupWidget, ctkExpandButton
ImportError: cannot import name ctkPopupWidget
loadSourceAsModule - Failed to load file "C:/Users/peter/Desktop/debug/Slicer-build/lib/Slicer-4.7/qt-scripted-modules/DICOMScalarVolumePlugin.py"  as module "DICOMScalarVolumePlugin" !
Fail to instantiate module  "DICOMScalarVolumePlugin"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "C:/Users/peter/Desktop/debug/Slicer-build/lib/Slicer-4.7/qt-scripted-modules/DICOMSlicerDataBundlePlugin.py", line 3, in &lt;module&gt;
    from DICOMLib import DICOMPlugin
  File "C:\Users\peter\Desktop\debug\Slicer-build\lib\Slicer-4.7\qt-scripted-modules\DICOMLib\__init__.py", line 4, in &lt;module&gt;
    from DICOMWidgets import *
  File "C:\Users\peter\Desktop\debug\Slicer-build\lib\Slicer-4.7\qt-scripted-modules\DICOMLib\DICOMWidgets.py", line 8, in &lt;module&gt;
    from ctk import ctkDICOMObjectListWidget, ctkDICOMDatabase, ctkDICOMIndexer, ctkDICOMBrowser, ctkPopupWidget, ctkExpandButton
ImportError: cannot import name ctkPopupWidget
loadSourceAsModule - Failed to load file "C:/Users/peter/Desktop/debug/Slicer-build/lib/Slicer-4.7/qt-scripted-modules/DICOMSlicerDataBundlePlugin.py"  as module "DICOMSlicerDataBundlePlugin" !
Fail to instantiate module  "DICOMSlicerDataBundlePlugin"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "C:/Users/peter/Desktop/debug/Slicer-build/lib/Slicer-4.7/qt-scripted-modules/ExtensionWizard.py", line 12, in &lt;module&gt;
    from ExtensionWizardLib import *
  File "C:\Users\peter\Desktop\debug\Slicer-build\lib\Slicer-4.7\qt-scripted-modules\ExtensionWizardLib\__init__.py", line 9, in &lt;module&gt;
    from SettingsPanel import SettingsPanel
  File "C:\Users\peter\Desktop\debug\Slicer-build\lib\Slicer-4.7\qt-scripted-modules\ExtensionWizardLib\SettingsPanel.py", line 49, in &lt;module&gt;
    class SettingsPanel(ctk.ctkSettingsPanel):
AttributeError: 'module' object has no attribute 'ctkSettingsPanel'
loadSourceAsModule - Failed to load file "C:/Users/peter/Desktop/debug/Slicer-build/lib/Slicer-4.7/qt-scripted-modules/ExtensionWizard.py"  as module "ExtensionWizard" !
Fail to instantiate module  "ExtensionWizard"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "C:/Users/peter/Desktop/debug/Slicer-build/lib/Slicer-4.7/qt-scripted-modules/JRC2013Vis.py", line 4, in &lt;module&gt;
    from DICOMLib import DICOMUtils
  File "C:\Users\peter\Desktop\debug\Slicer-build\lib\Slicer-4.7\qt-scripted-modules\DICOMLib\__init__.py", line 4, in &lt;module&gt;
    from DICOMWidgets import *
  File "C:\Users\peter\Desktop\debug\Slicer-build\lib\Slicer-4.7\qt-scripted-modules\DICOMLib\DICOMWidgets.py", line 8, in &lt;module&gt;
    from ctk import ctkDICOMObjectListWidget, ctkDICOMDatabase, ctkDICOMIndexer, ctkDICOMBrowser, ctkPopupWidget, ctkExpandButton
ImportError: cannot import name ctkPopupWidget
loadSourceAsModule - Failed to load file "C:/Users/peter/Desktop/debug/Slicer-build/lib/Slicer-4.7/qt-scripted-modules/JRC2013Vis.py"  as module "JRC2013Vis" !
Fail to instantiate module  "JRC2013Vis"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "C:/Users/peter/Desktop/debug/Slicer-build/lib/Slicer-4.7/qt-scripted-modules/MultiVolumeImporterPlugin.py", line 5, in &lt;module&gt;
    import DICOMLib
  File "C:\Users\peter\Desktop\debug\Slicer-build\lib\Slicer-4.7\qt-scripted-modules\DICOMLib\__init__.py", line 4, in &lt;module&gt;
    from DICOMWidgets import *
  File "C:\Users\peter\Desktop\debug\Slicer-build\lib\Slicer-4.7\qt-scripted-modules\DICOMLib\DICOMWidgets.py", line 8, in &lt;module&gt;
    from ctk import ctkDICOMObjectListWidget, ctkDICOMDatabase, ctkDICOMIndexer, ctkDICOMBrowser, ctkPopupWidget, ctkExpandButton
ImportError: cannot import name ctkPopupWidget
loadSourceAsModule - Failed to load file "C:/Users/peter/Desktop/debug/Slicer-build/lib/Slicer-4.7/qt-scripted-modules/MultiVolumeImporterPlugin.py"  as module "MultiVolumeImporterPlugin" !
Fail to instantiate module  "MultiVolumeImporterPlugin"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "C:/Users/peter/Desktop/debug/Slicer-build/lib/Slicer-4.7/qt-scripted-modules/RSNAVisTutorial.py", line 4, in &lt;module&gt;
    from DICOMLib import DICOMUtils
  File "C:\Users\peter\Desktop\debug\Slicer-build\lib\Slicer-4.7\qt-scripted-modules\DICOMLib\__init__.py", line 4, in &lt;module&gt;
    from DICOMWidgets import *
  File "C:\Users\peter\Desktop\debug\Slicer-build\lib\Slicer-4.7\qt-scripted-modules\DICOMLib\DICOMWidgets.py", line 8, in &lt;module&gt;
    from ctk import ctkDICOMObjectListWidget, ctkDICOMDatabase, ctkDICOMIndexer, ctkDICOMBrowser, ctkPopupWidget, ctkExpandButton
ImportError: cannot import name ctkPopupWidget
loadSourceAsModule - Failed to load file "C:/Users/peter/Desktop/debug/Slicer-build/lib/Slicer-4.7/qt-scripted-modules/RSNAVisTutorial.py"  as module "RSNAVisTutorial" !
Fail to instantiate module  "RSNAVisTutorial"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "C:/Users/peter/Desktop/debug/Slicer-build/lib/Slicer-4.7/qt-scripted-modules/SubjectHierarchyGenericSelfTest.py", line 5, in &lt;module&gt;
    from DICOMLib import DICOMUtils
  File "C:\Users\peter\Desktop\debug\Slicer-build\lib\Slicer-4.7\qt-scripted-modules\DICOMLib\__init__.py", line 4, in &lt;module&gt;
    from DICOMWidgets import *
  File "C:\Users\peter\Desktop\debug\Slicer-build\lib\Slicer-4.7\qt-scripted-modules\DICOMLib\DICOMWidgets.py", line 8, in &lt;module&gt;
    from ctk import ctkDICOMObjectListWidget, ctkDICOMDatabase, ctkDICOMIndexer, ctkDICOMBrowser, ctkPopupWidget, ctkExpandButton
ImportError: cannot import name ctkPopupWidget
loadSourceAsModule - Failed to load file "C:/Users/peter/Desktop/debug/Slicer-build/lib/Slicer-4.7/qt-scripted-modules/SubjectHierarchyGenericSelfTest.py"  as module "SubjectHierarchyGenericSelfTest" !
Fail to instantiate module  "SubjectHierarchyGenericSelfTest"
Number of instantiated modules: 132
Traceback (most recent call last):
  File "C:/Users/peter/Desktop/debug/Slicer-build/bin/Python/slicer/slicerqt.py", line 54, in emit
    self.pythonToCtkLevelConverter[record.levelno], self.origin, context, record.msg)
AttributeError: 'SlicerApplicationLogHandler' object has no attribute 'pythonToCtkLevelConverter'
Logged from file AbstractScriptedSubjectHierarchyPlugin.py, line 36
When loading module  "DICOMPatcher" , the dependency "DICOM" failed to be loaded.
Traceback (most recent call last):
  File "C:/Users/peter/Desktop/debug/Slicer-build/bin/Python/slicer/slicerqt.py", line 54, in emit
    self.pythonToCtkLevelConverter[record.levelno], self.origin, context, record.msg)
AttributeError: 'SlicerApplicationLogHandler' object has no attribute 'pythonToCtkLevelConverter'
Logged from file AbstractScriptedSubjectHierarchyPlugin.py, line 36
Traceback (most recent call last):
  File "C:/Users/peter/Desktop/debug/Slicer-build/bin/Python/slicer/slicerqt.py", line 54, in emit
    self.pythonToCtkLevelConverter[record.levelno], self.origin, context, record.msg)
AttributeError: 'SlicerApplicationLogHandler' object has no attribute 'pythonToCtkLevelConverter'
Logged from file AbstractScriptedSubjectHierarchyPlugin.py, line 36
Number of loaded modules: 131
</code></pre>
</details>
<p>Build errors from Visual Studio are here:</p>
<details>
<summary>
Build errors</summary>
<pre><code>                    Description      File    Line    Column    Project   
Error	1	error MSB6006: "cmd.exe" exited with code 1. [C:\Users\peter\Desktop\debug\CTK-build\CTK-build\Libs\Widgets\CTKWidgetsPythonQt.vcxproj] [C:\Users\peter\Desktop\debug\CTK-build\CTK.vcxproj]	C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets	170	5	CTK

Error	2	error MSB6006: "cmd.exe" exited with code 1. [C:\Users\peter\Desktop\debug\CTK-build\CTK-build\Libs\Widgets\CTKWidgetsPythonQt.vcxproj] [C:\Users\peter\Desktop\debug\CTK-build\CTK.vcxproj]	C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets	170	5	CTK

Error	3	error MSB6006: "cmd.exe" exited with code 1. [C:\Users\peter\Desktop\debug\CTK-build\CTK-build\Libs\Widgets\CTKWidgetsPythonQt.vcxproj] [C:\Users\peter\Desktop\debug\CTK-build\CTK.vcxproj]	C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets	170	5	CTK

Error	4	error MSB6006: "cmd.exe" exited with code 1. [C:\Users\peter\Desktop\debug\CTK-build\CTK-build\Libs\Widgets\CTKWidgetsPythonQt.vcxproj] [C:\Users\peter\Desktop\debug\CTK-build\CTK.vcxproj]	C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets	170	5	CTK
</code></pre>
</details>
<p>Any suggestions?</p>

---

## Post #2 by @lassoan (2017-10-14 23:10 UTC)

<p>What Visual Studio and Qt version do you use?<br>
Have you built Qt as described in the build instructions?<br>
Please post build errors that you get when building …\CTK-build\CTK-build\CTK.sln project.</p>

---

## Post #3 by @peterkshultz (2017-10-14 23:53 UTC)

<p>Thanks for the reply, Andras.</p>
<p><strong>Visual Studio:</strong> 2013, Update 5<br>
<strong>Qt:</strong> qt-4.8.7-64-vs2013-deb</p>
<p>I built Qt by using <a href="https://github.com/jcfr/qt-easy-build/tree/4.8.7#windows" rel="nofollow noopener">this</a>, which I believe was included in the build instructions.</p>
<p>Build log for CTK.sln after doing <code>BUILD_ALL</code>:</p>
<details>
<summary>
Build log</summary>
<pre><code>1&gt;------ Build started: Project: CTKCore, Configuration: Debug x64 ------
2&gt;------ Build started: Project: CopyCTKScriptingPythonCorePythonScriptFiles, Configuration: Debug x64 ------
1&gt;  CTKCore.vcxproj -&gt; C:\Users\peter\Desktop\debug\CTK-build\CTK-build\bin\Debug\CTKCore.dll
3&gt;------ Build started: Project: CompileCTKScriptingPythonCorePythonFiles, Configuration: Debug x64 ------
4&gt;------ Build started: Project: CTKVisualizationVTKCore, Configuration: Debug x64 ------
5&gt;------ Build started: Project: CTKWidgets, Configuration: Debug x64 ------
4&gt;  CTKVisualizationVTKCore.vcxproj -&gt; C:\Users\peter\Desktop\debug\CTK-build\CTK-build\bin\Debug\CTKVisualizationVTKCore.dll
6&gt;------ Build started: Project: CTKDICOMCore, Configuration: Debug x64 ------
5&gt;  CTKWidgets.vcxproj -&gt; C:\Users\peter\Desktop\debug\CTK-build\CTK-build\bin\Debug\CTKWidgets.dll
6&gt;  CTKDICOMCore.vcxproj -&gt; C:\Users\peter\Desktop\debug\CTK-build\CTK-build\bin\Debug\CTKDICOMCore.dll
7&gt;------ Build started: Project: CTKScriptingPythonCore, Configuration: Debug x64 ------
7&gt;  CTKScriptingPythonCore.vcxproj -&gt; C:\Users\peter\Desktop\debug\CTK-build\CTK-build\bin\Debug\CTKScriptingPythonCore.dll
8&gt;------ Build started: Project: CTKVisualizationVTKWidgets, Configuration: Debug x64 ------
9&gt;------ Build started: Project: CTKDICOMWidgets, Configuration: Debug x64 ------
8&gt;  CTKVisualizationVTKWidgets.vcxproj -&gt; C:\Users\peter\Desktop\debug\CTK-build\CTK-build\bin\Debug\CTKVisualizationVTKWidgets.dll
10&gt;------ Build started: Project: CTKImageProcessingITKCore, Configuration: Debug x64 ------
9&gt;  CTKDICOMWidgets.vcxproj -&gt; C:\Users\peter\Desktop\debug\CTK-build\CTK-build\bin\Debug\CTKDICOMWidgets.dll
11&gt;------ Build started: Project: CTKQtTesting, Configuration: Debug x64 ------
11&gt;  CTKQtTesting.vcxproj -&gt; C:\Users\peter\Desktop\debug\CTK-build\CTK-build\bin\Debug\CTKQtTesting.dll
12&gt;------ Build started: Project: CTKScriptingPythonWidgets, Configuration: Debug x64 ------
13&gt;------ Build started: Project: CTKCorePythonQt, Configuration: Debug x64 ------
13&gt;  CTKCorePythonQt.vcxproj -&gt; C:\Users\peter\Desktop\debug\CTK-build\CTK-build\bin\Debug\CTKCorePythonQt.pyd
12&gt;  CTKScriptingPythonWidgets.vcxproj -&gt; C:\Users\peter\Desktop\debug\CTK-build\CTK-build\bin\Debug\CTKScriptingPythonWidgets.dll
14&gt;------ Build started: Project: CTKDICOMCorePythonQt, Configuration: Debug x64 ------
14&gt;  CTKDICOMCorePythonQt.vcxproj -&gt; C:\Users\peter\Desktop\debug\CTK-build\CTK-build\bin\Debug\CTKDICOMCorePythonQt.pyd
15&gt;------ Build started: Project: CTKDICOMWidgetsPlugins, Configuration: Debug x64 ------
15&gt;  CTKDICOMWidgetsPlugins.vcxproj -&gt; C:\Users\peter\Desktop\debug\CTK-build\CTK-build\bin\designer\Debug\CTKDICOMWidgetsPlugins.dll
16&gt;------ Build started: Project: CTKDICOMWidgetsPythonQt, Configuration: Debug x64 ------
16&gt;  CTKDICOMWidgetsPythonQt.vcxproj -&gt; C:\Users\peter\Desktop\debug\CTK-build\CTK-build\bin\Debug\CTKDICOMWidgetsPythonQt.pyd
17&gt;------ Build started: Project: CTKImageProcessingITKCorePythonQt, Configuration: Debug x64 ------
17&gt;  CTKImageProcessingITKCorePythonQt.vcxproj -&gt; C:\Users\peter\Desktop\debug\CTK-build\CTK-build\bin\Debug\CTKImageProcessingITKCorePythonQt.pyd
18&gt;------ Build started: Project: CTKQtTestingPythonQt, Configuration: Debug x64 ------
19&gt;------ Build started: Project: CTKScriptingPythonWidgetsPlugins, Configuration: Debug x64 ------
18&gt;  CTKQtTestingPythonQt.vcxproj -&gt; C:\Users\peter\Desktop\debug\CTK-build\CTK-build\bin\Debug\CTKQtTestingPythonQt.pyd
20&gt;------ Build started: Project: CTKScriptingPythonWidgetsPythonQt, Configuration: Debug x64 ------
19&gt;  CTKScriptingPythonWidgetsPlugins.vcxproj -&gt; C:\Users\peter\Desktop\debug\CTK-build\CTK-build\bin\designer\Debug\CTKScriptingPythonWidgetsPlugins.dll
20&gt;  CTKScriptingPythonWidgetsPythonQt.vcxproj -&gt; C:\Users\peter\Desktop\debug\CTK-build\CTK-build\bin\Debug\CTKScriptingPythonWidgetsPythonQt.pyd
21&gt;------ Build started: Project: CTKVisualizationVTKCorePythonQt, Configuration: Debug x64 ------
21&gt;  CTKVisualizationVTKCorePythonQt.vcxproj -&gt; C:\Users\peter\Desktop\debug\CTK-build\CTK-build\bin\Debug\CTKVisualizationVTKCorePythonQt.pyd
22&gt;------ Build started: Project: CTKVisualizationVTKWidgetsPlugins, Configuration: Debug x64 ------
23&gt;------ Build started: Project: CTKVisualizationVTKWidgetsPythonQt, Configuration: Debug x64 ------
23&gt;  CTKVisualizationVTKWidgetsPythonQt.vcxproj -&gt; C:\Users\peter\Desktop\debug\CTK-build\CTK-build\bin\Debug\CTKVisualizationVTKWidgetsPythonQt.pyd
24&gt;------ Build started: Project: CTKWidgetsPlugins, Configuration: Debug x64 ------
25&gt;------ Build started: Project: CTKWidgetsPythonQt, Configuration: Debug x64 ------
24&gt;  CTKWidgetsPlugins.vcxproj -&gt; C:\Users\peter\Desktop\debug\CTK-build\CTK-build\bin\designer\Debug\CTKWidgetsPlugins.dll
26&gt;------ Build started: Project: ctkDICOM, Configuration: Debug x64 ------
25&gt;  Building Custom Rule C:/Users/peter/Desktop/debug/CTK/Libs/Widgets/CMakeLists.txt
25&gt;  CMake does not need to re-run because C:\Users\peter\Desktop\debug\CTK-build\CTK-build\Libs\Widgets\CMakeFiles\generate.stamp is up-to-date.
25&gt;  PythonQt Wrapping - Generating generated_cpp/org_commontk_CTKWidgets/org_commontk_CTKWidgets_init.cpp
25&gt;  Traceback (most recent call last):
25&gt;    File "C:/Users/peter/Desktop/debug/CTK/CMake/ctkWrapPythonQt.py", line 237, in &lt;module&gt;
25&gt;      ctk_wrap_pythonqt(options.target, options.namespace, options.output_dir, args, options.extra_verbose)
25&gt;    File "C:/Users/peter/Desktop/debug/CTK/CMake/ctkWrapPythonQt.py", line 77, in ctk_wrap_pythonqt
25&gt;      with open(input_file) as f:
25&gt;  IOError: [Errno 2] No such file or directory: 'C:/Users/peter/Desktop/debug/CTK/Libs/Widgets/ctkRangeSliderEvenTranslator.h'
25&gt;C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(170,5): error MSB6006: "cmd.exe" exited with code 1.
26&gt;  ctkDICOM.vcxproj -&gt; C:\Users\peter\Desktop\debug\CTK-build\CTK-build\bin\Debug\ctkDICOM.exe
27&gt;------ Build started: Project: ALL_BUILD, Configuration: Debug x64 ------
27&gt;  Building Custom Rule C:/Users/peter/Desktop/debug/CTK/CMakeLists.txt
27&gt;  CMake does not need to re-run because C:\Users\peter\Desktop\debug\CTK-build\CTK-build\CMakeFiles\generate.stamp is up-to-date.
========== Build: 26 succeeded, 1 failed, 1 up-to-date, 0 skipped ==========
</code></pre>
</details>
<p>Build errors:</p>
<details>
<summary>
Build errors</summary>
<p><code>Error	1	error MSB6006: "cmd.exe" exited with code 1.	C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets	170	5	CTKWidgetsPythonQt</code></p>
</details>
<p>Let me know if you need anything else.</p>

---

## Post #4 by @cpinter (2017-10-15 00:27 UTC)

<p>This seems like the right way to build Slicer. Do you have another python installed on your computer?</p>

---

## Post #5 by @lassoan (2017-10-15 00:45 UTC)

<p>Yes, make sure Python executable’s folder is not added to PATH environment variable at user or system level.</p>

---

## Post #6 by @msmolens (2017-10-16 14:44 UTC)

<blockquote>
<p><code>IOError: [Errno 2] No such file or directory: 'C:/Users/peter/Desktop/debug/CTK/Libs/Widgets/ctkRangeSliderEvenTranslator.h'</code></p>
</blockquote>
<p>The path of your build directory is likely too long. That typically results in errors like above, where a letter is missing from the filename (the “<code>t</code>” in <code>Event</code>").</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Windows_2" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Developers/Build Instructions - Slicer Wiki</a> suggests using a short path like <code>C:\S4D</code>.</p>

---
