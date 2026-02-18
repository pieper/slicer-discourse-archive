# cannot load DICOM browser

**Topic ID**: 1522
**Date**: 2017-11-27
**URL**: https://discourse.slicer.org/t/cannot-load-dicom-browser/1522

---

## Post #1 by @researchtomliu (2017-11-27 02:15 UTC)

<p>Operating system:win 7 64bit<br>
Slicer version:4.8<br>
Expected behavior:open DICOM browser<br>
Actual behavior: when I press the “DICOM” button to want to load dicom data, the DICOM browser window cannot pop-up as usual.  Then I pressed the button of “Start Listener” beneath the “servers”, a pop-up window show me the problem as follows " Could not start listener: Database directory not set: cannot start DICOM listener". I have restarted my PC and the problem still exists.</p>

---

## Post #2 by @lassoan (2017-11-27 02:43 UTC)

<p>Could you please send the application log? Start Slicer, switch to DICOM module, then go to menu: Help/Report a bug, click <code>Copy log messages to clipboard</code> button, and paste the log messages here.</p>

---

## Post #3 by @lassoan (2017-11-27 02:52 UTC)

<p>Maybe the DICOM browser window is just out of view (Slicer remembers the last position and the DICOM popup window and maybe if you change number and resolution of displays then you may end up not seeing the window). Please reset your application settings by removing <a href="https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/ApplicationSettings#Settings_file_location">Slicer.ini</a> file and let us know if it fixed the issue.</p>

---

## Post #4 by @researchtomliu (2017-11-27 16:45 UTC)

<p>Thanks a lot for your advice, but it is no use.</p>

---

## Post #5 by @Jenny_Lee (2017-11-27 19:07 UTC)

<p>I have the same problem.  I am using version 4.9.0-2017-11-23.</p>

---

## Post #6 by @Jenny_Lee (2017-11-27 19:13 UTC)

<p>Below is my log message.  As you can see, the Dicom Module and several other modules can not be load.  I don’t know if this helps, but I have python installed on my PC.</p>
<pre><code class="lang-auto">[DEBUG][Qt] 27.11.2017 13:41:39 [] (unknown:0) - Session start time .......: 2017-11-27 13:41:39
[DEBUG][Qt] 27.11.2017 13:41:39 [] (unknown:0) - Session start time .......: 2017-11-27 13:41:39
[DEBUG][Qt] 27.11.2017 13:41:39 [] (unknown:0) - Slicer version ...........: 4.9.0-2017-11-23 (revision 26654) win-amd64 - installed
[DEBUG][Qt] 27.11.2017 13:41:39 [] (unknown:0) - Slicer version ...........: 4.9.0-2017-11-23 (revision 26654) win-amd64 - installed
[DEBUG][Qt] 27.11.2017 13:41:39 [] (unknown:0) - Operating system .........: Windows / 7 / Service Pack 1 (Build 7601) - 64-bit
[DEBUG][Qt] 27.11.2017 13:41:39 [] (unknown:0) - Operating system .........: Windows / 7 / Service Pack 1 (Build 7601) - 64-bit
[DEBUG][Qt] 27.11.2017 13:41:39 [] (unknown:0) - Memory ...................: 24573 MB physical, 49145 MB virtual
[DEBUG][Qt] 27.11.2017 13:41:39 [] (unknown:0) - Memory ...................: 24573 MB physical, 49145 MB virtual
[DEBUG][Qt] 27.11.2017 13:41:39 [] (unknown:0) - CPU ......................: GenuineIntel , 6 cores, 32 logical processors
[DEBUG][Qt] 27.11.2017 13:41:39 [] (unknown:0) - CPU ......................: GenuineIntel , 6 cores, 32 logical processors
[DEBUG][Qt] 27.11.2017 13:41:39 [] (unknown:0) - Developer mode enabled ...: no
[DEBUG][Qt] 27.11.2017 13:41:39 [] (unknown:0) - Developer mode enabled ...: no
[DEBUG][Qt] 27.11.2017 13:41:39 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 27.11.2017 13:41:39 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 27.11.2017 13:41:39 [] (unknown:0) - Additional module paths ..: (none)
[DEBUG][Qt] 27.11.2017 13:41:39 [] (unknown:0) - Additional module paths ..: (none)
[DEBUG][Python] 27.11.2017 13:41:43 [Python] (C:\Users\leeje\Slicer 4.9.0-2017-11-23\lib\Python\Lib\site-packages\git\cmd .py:719) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)
[DEBUG][Python] 27.11.2017 13:41:43 [Python] (C:\Users\leeje\Slicer 4.9.0-2017-11-23\lib\Python\Lib\site-packages\git\cmd .py:719) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)
[DEBUG][Python] 27.11.2017 13:41:43 [Python] (C:\Users\leeje\Slicer 4.9.0-2017-11-23\lib\Python\Lib\site-packages\git\cmd .py: 719) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)
[DEBUG][Python] 27.11.2017 13:41:43 [Python] (C:\Users\leeje\Slicer 4.9.0-2017-11-23\lib\Python\Lib\site-packages\git\cmd .py:719) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)
[WARNING][Python] 27.11.2017 13:41:46 [Python] (C:\Users\leeje\Slicer 4.9.0-2017-11-23\lib\Slicer-4.9\qt-scripted-modules\DataProbeLib\SliceViewAnnotations .py:26) - SliceAnnotations: Disable features relying on vtkPVScalarBarActor
[WARNING][Python] 27.11.2017 13:41:46 [Python] (C:\Users\leeje\Slicer 4.9.0-2017-11-23\lib\Slicer-4.9\qt-scripted-modules\DataProbeLib\SliceViewAnnotations .py:26) - SliceAnnotations: Disable features relying on vtkPVScalarBarActor
[DEBUG][Qt] 27.11.2017 13:41:39 [] (unknown:0) - Number of registered modules: 58
[DEBUG][Qt] 27.11.2017 13:41:45 [] (unknown:0) - Number of instantiated modules: 58
[WARNING][Qt] 27.11.2017 13:41:46 [] (unknown:0) - When loading module  "DICOM" , the dependency "SubjectHierarchy" failed to be loaded.
[WARNING][Qt] 27.11.2017 13:41:46 [] (unknown:0) - When loading module  "DICOM" , the dependency "SubjectHierarchy" failed to be loaded.
[WARNING][Qt] 27.11.2017 13:41:46 [] (unknown:0) - When loading module  "DICOMPatcher" , the dependency "DICOM" failed to be loaded.
[WARNING][Qt] 27.11.2017 13:41:46 [] (unknown:0) - When loading module  "MarkupsWidgetsSelfTest" , the dependency "Markups" failed to be loaded.
[WARNING][Qt] 27.11.2017 13:41:46 [] (unknown:0) - When loading module  "MultiVolumeImporter" , the dependency "MultiVolumeExplorer" failed to be loaded.
[WARNING][Qt] 27.11.2017 13:41:46 [] (unknown:0) - When loading module  "SegmentEditor" , the dependency "Segmentations" failed to be loaded.
[WARNING][Qt] 27.11.2017 13:41:46 [] (unknown:0) - When loading module  "SegmentStatistics" , the dependency "SubjectHierarchy" failed to be loaded.
[WARNING][Qt] 27.11.2017 13:41:46 [] (unknown:0) - When loading module  "SubjectHierarchyCorePluginsSelfTest" , the dependency "SubjectHierarchy" failed to be loaded.
[WARNING][Qt] 27.11.2017 13:41:46 [] (unknown:0) - When loading module  "SubjectHierarchyGenericSelfTest" , the dependency "SubjectHierarchy" failed to be loaded.
[WARNING][Qt] 27.11.2017 13:41:46 [] (unknown:0) - When loading module  "TablesSelfTest" , the dependency "Tables" failed to be loaded.
[DEBUG][Qt] 27.11.2017 13:41:46 [] (unknown:0) - Number of loaded modules: 49
[CRITICAL][Stream] 27.11.2017 13:41:46 [] (unknown:0) - SliceAnnotations: Disable features relying on vtkPVScalarBarActor
[DEBUG][Qt] 27.11.2017 13:41:39 [] (unknown:0) - Number of registered modules: 58
[DEBUG][Qt] 27.11.2017 13:41:45 [] (unknown:0) - Number of instantiated modules: 58
[WARNING][Qt] 27.11.2017 13:41:46 [] (unknown:0) - When loading module  "DICOM" , the dependency "SubjectHierarchy" failed to be loaded.
[WARNING][Qt] 27.11.2017 13:41:46 [] (unknown:0) - When loading module  "DICOM" , the dependency "SubjectHierarchy" failed to be loaded.
[WARNING][Qt] 27.11.2017 13:41:46 [] (unknown:0) - When loading module  "DICOMPatcher" , the dependency "DICOM" failed to be loaded.
[WARNING][Qt] 27.11.2017 13:41:46 [] (unknown:0) - When loading module  "MarkupsWidgetsSelfTest" , the dependency "Markups" failed to be loaded.
[WARNING][Qt] 27.11.2017 13:41:46 [] (unknown:0) - When loading module  "MultiVolumeImporter" , the dependency "MultiVolumeExplorer" failed to be loaded.
[WARNING][Qt] 27.11.2017 13:41:46 [] (unknown:0) - When loading module  "SegmentEditor" , the dependency "Segmentations" failed to be loaded.
[WARNING][Qt] 27.11.2017 13:41:46 [] (unknown:0) - When loading module  "SegmentStatistics" , the dependency "SubjectHierarchy" failed to be loaded.
[WARNING][Qt] 27.11.2017 13:41:46 [] (unknown:0) - When loading module  "SubjectHierarchyCorePluginsSelfTest" , the dependency "SubjectHierarchy" failed to be loaded.
[WARNING][Qt] 27.11.2017 13:41:46 [] (unknown:0) - When loading module  "SubjectHierarchyGenericSelfTest" , the dependency "SubjectHierarchy" failed to be loaded.
[WARNING][Qt] 27.11.2017 13:41:46 [] (unknown:0) - When loading module  "TablesSelfTest" , the dependency "Tables" failed to be loaded.
[DEBUG][Qt] 27.11.2017 13:41:46 [] (unknown:0) - Number of loaded modules: 49
[CRITICAL][Stream] 27.11.2017 13:41:46 [] (unknown:0) - SliceAnnotations: Disable features relying on vtkPVScalarBarActor
[WARNING][Qt] 27.11.2017 13:42:24 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
</code></pre>

---

## Post #7 by @cpinter (2017-11-27 19:24 UTC)

<p>These are two different issues it seems.</p>
<p><a class="mention" href="/u/researchtomliu">@researchtomliu</a> started a <a href="https://discourse.slicer.org/t/dicom-browser-could-not-pop-up/1528">new thread</a> where pasted the error log, which suggests it’s a special character related issue.</p>
<p><a class="mention" href="/u/jenny_lee">@Jenny_Lee</a> has problem with all the python modules, which is unrelated and is similar to <a href="https://discourse.slicer.org/t/why-the-editor-module-is-missing/1464/2">this</a></p>

---

## Post #8 by @cpinter (2017-11-27 22:12 UTC)

<p>After a second look at the log by <a class="mention" href="/u/jenny_lee">@Jenny_Lee</a> it seems that the SubjectHierarchy module was not loaded, which suggests an even different kind of problem which I haven’t seen before. The log says only 58 modules have been registered which is less than half of what it should be. I downloaded and installed the same version, and it works fine with me. Not sure if it’s related to Windows 7. Can you please try to uninstall that Slicer and install <a href="http://slicer.kitware.com/midas3/api/rest?method=midas.bitstream.download&amp;name=Slicer-4.9.0-2017-11-23-win-amd64.exe&amp;checksum=1029c8b87a4f1d22cffd3567c44cbd93">this release</a>?</p>

---
