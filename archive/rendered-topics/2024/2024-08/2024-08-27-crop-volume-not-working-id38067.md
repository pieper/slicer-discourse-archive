---
topic_id: 38067
title: "Crop Volume Not Working"
date: 2024-08-27
url: https://discourse.slicer.org/t/38067
---

# Crop Volume Not Working

**Topic ID**: 38067
**Date**: 2024-08-27
**URL**: https://discourse.slicer.org/t/crop-volume-not-working/38067

---

## Post #1 by @Arash1 (2024-08-27 23:56 UTC)

<p>Hi<br>
I have an issue that I dont know the reason. No new modules was installed, dataset are the same, and pretty much everything but the Crop Volume module is not working.<br>
Here are the codes</p>
<p>Python 3.9.10 (main, Apr  5 2024, 01:02:26) [MSC v.1938 64 bit (AMD64)] on win32</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<p>Failed to load vtkSlicerCrossSectionAnalysisModuleLogicPython: No module named vtkSlicerShapeModuleMRMLPython<br>
Failed to load vtkSlicerStenosisMeasurement3DModuleLogicPython: No module named vtkSlicerShapeModuleMRMLPython<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Slicer 5.6.2\lib\Python\Lib\imp.py”, line 169, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 613, in _exec<br>
File “”, line 850, in exec_module<br>
File “”, line 228, in <em>call_with_frames_removed<br>
File “C:/Slicer 5.6.2/slicer.org/Extensions-32448/TCIABrowser/lib/Slicer-5.6/qt-scripted-modules/TCIABrowser.py”, line 23, in <br>
from TCIABrowserLib import TCIAClient<br>
File “C:\Slicer 5.6.2\slicer.org\Extensions-32448\TCIABrowser\lib\Slicer-5.6\qt-scripted-modules\TCIABrowserLib\TCIAClient.py”, line 7, in <br>
import tcia_utils.nbia<br>
File "C:\Slicer 5.6.2\lib\Python\Lib\site-packages\tcia_utils_<em>init</em></em>.py", line 1, in <br>
from . import nbia<br>
File “C:\Slicer 5.6.2\lib\Python\Lib\site-packages\tcia_utils\nbia.py”, line 111<br>
if ‘token_exp_time’ in globals() and datetime.now() &gt; token_exp_time:<br>
^<br>
IndentationError: unindent does not match any outer indentation level<br>
TODO: implement cloud fingerprint store<br>
[Qt] loadSourceAsModule - Failed to load file “C:/Slicer 5.6.2/slicer.org/Extensions-32448/TCIABrowser/lib/Slicer-5.6/qt-scripted-modules/TCIABrowser.py”  as module “TCIABrowser” !<br>
[Qt] Fail to instantiate module  “TCIABrowser”<br>
[Qt]   Error(s):<br>
[Qt]     CLI executable: C:/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerVMTK/lib/Slicer-5.6/qt-loadable-modules/vtkvmtk.py<br>
[Qt]     The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program.<br>
[Qt] Fail to instantiate module  “vtkvmtk”<br>
[Qt] The following modules failed to be instantiated:<br>
[Qt]    vtkvmtk<br>
[Qt]    TCIABrowser<br>
[Qt] When loading module  “ParticlesDisplay” , the dependency “TractographyDisplay” failed to be loaded.<br>
[VTK] There is more than one file, use the vtkITKArchetypeImageSeriesReader instead<br>
[ITK] WARNING: In D:\D\S\S-0-build\ITK\Modules\IO\ImageBase\include\itkImageSeriesReader.hxx, line 478<br>
[ITK] ImageSeriesReader (0000027FF1EEB030): Non uniform sampling or missing slices detected,  maximum nonuniformity:0.000249973<br>
[Qt] QLayout::addChildLayout: layout “” already has a parent<br>
[Qt] ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 1<br>
[Qt] ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 1<br>
[Qt] ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 1<br>
[Qt] ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 1<br>
[Qt] ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 1<br>
[Qt] ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 1<br>
[VTK] Resample Scalar/Vector/DWI Volume terminated with an unknown exception<br>
[VTK] Input port 0 of algorithm vtkImageMapToWindowLevelColors (0000027F8608A520) has 0 connections but is not optional.<br>
[VTK] Input port 0 of algorithm vtkImageThreshold (00000280357B55C0) has 0 connections but is not optional.<br>
[VTK] Input port 0 of algorithm vtkImageMapToWindowLevelColors (0000027F8608A520) has 0 connections but is not optional.<br>
[VTK] Input port 0 of algorithm vtkImageMapToWindowLevelColors (0000027F8608A520) has 0 connections but is not optional.<br>
[VTK] Input port 0 of algorithm vtkImageThreshold (00000280357B55C0) has 0 connections but is not optional.<br>
[VTK] Input port 0 of algorithm vtkImageMapToWindowLevelColors (0000027F8608A520) has 0 connections but is not optional.<br>
[Qt] ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 1</p>

---

## Post #2 by @cpinter (2024-08-28 08:22 UTC)

<p>It seems your log only includes errors, but it would be useful to see the whole thing to know at which point you switched to the Crop volumes module. Can you please provide the entire log file? Preferably of a run where you didn’t do much else (I see TCIA browser errors and Resample scalar volume runs etc as well).</p>
<p>Does the module work for you with sample data?</p>

---

## Post #3 by @Arash1 (2024-08-29 21:28 UTC)

<p>Hello<br>
Thank you very much for your response.<br>
The extra modules were errors caused by Slicer not being able to execute the extensions. I am no expert, but I believe the proxy settings might be the issue. However, I could be wrong.</p>
<p>The first thing I see on the console is: <strong>[Qt] When loading module  “ParticlesDisplay” , the dependency “TractographyDisplay” failed to be loaded.</strong> This is a new error that I am receving and I am not sure why. Dataset that I am using has not changed. Slicer version has also remained the same.</p>
<p>For the log:<br>
[DEBUG][Qt] 29.08.2024 14:59:26 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 20240829_145926<br>
[DEBUG][Qt] 29.08.2024 14:59:26 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 5.6.2 (revision 32448 / f10cd8c) win-amd64 - installed release<br>
[DEBUG][Qt] 29.08.2024 14:59:26 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows /  Professional / (Build 22631, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 29.08.2024 14:59:26 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 32501 MB physical, 37621 MB virtual<br>
[DEBUG][Qt] 29.08.2024 14:59:26 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel , 12 cores, 12 logical processors<br>
[DEBUG][Qt] 29.08.2024 14:59:26 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 29.08.2024 14:59:26 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 29.08.2024 14:59:26 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Internationalization …: disabled, language=<br>
[DEBUG][Qt] 29.08.2024 14:59:26 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode …: disabled<br>
[DEBUG][Qt] 29.08.2024 14:59:26 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: C:/Slicer 5.6.2/bin<br>
[DEBUG][Qt] 29.08.2024 14:59:26 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: <a href="http://slicer.org/Extensions-32448/Chest_Imaging_Platform/lib/Slicer-5.6/cli-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32448/Chest_Imaging_Platform/lib/Slicer-5.6/cli-modules</a>, <a href="http://slicer.org/Extensions-32448/Chest_Imaging_Platform/lib/Slicer-5.6/qt-loadable-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32448/Chest_Imaging_Platform/lib/Slicer-5.6/qt-loadable-modules</a>, <a href="http://slicer.org/Extensions-32448/Chest_Imaging_Platform/lib/Slicer-5.6/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32448/Chest_Imaging_Platform/lib/Slicer-5.6/qt-scripted-modules</a><br>
[WARNING][Qt] 29.08.2024 14:59:28 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - When loading module  “ParticlesDisplay” , the dependency “TractographyDisplay” failed to be loaded.<br>
[DEBUG][Python] 29.08.2024 14:59:28 [Python] (C:\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 29.08.2024 14:59:28 [Python] (C:\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 29.08.2024 14:59:29 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”</p>
<p>I tried the sample data, the crop functions works and a new volume is generated but even at 0.5, 0.2, or 0.1 spacing or using different interpolators, the new cropped remains intact. In other words, the resolution does not change.<br>
From what I know, lower spacing requires more calculations and more memory. The computer that I am working with doesnt have other softwares and applications and is only used for Slicer.</p>
<p>My goal to use this module is to increase the resolution. Is there any suggestions for this purpose?</p>
<p>Thanks,<br>
Arash</p>

---

## Post #4 by @cpinter (2024-08-30 10:25 UTC)

<p>Thanks for the complete log. You’re right, a module fails to load. Can you try to reinstall it in Extensions Manager? Are there any errors during/after installation?</p>
<aside class="quote no-group" data-username="Arash1" data-post="3" data-topic="38067">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/arash1/48/78865_2.png" class="avatar"> Arash1:</div>
<blockquote>
<p>but even at 0.5, 0.2, or 0.1 spacing or using different interpolators, the new cropped remains intact. In other words, the resolution does not change.</p>
</blockquote>
</aside>
<p>The CropVolumes module should not be impacted by this extension loading issue and should work. As far as I know the module never fails the way you describe (i.e. that the output is simply the same as the input). Do you have a log showing this? A video would help too.</p>

---
