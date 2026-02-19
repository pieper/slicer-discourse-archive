---
topic_id: 19255
title: "Error Command Elastix Returned Non Zero Exit Status 32212257"
date: 2021-08-18
url: https://discourse.slicer.org/t/19255
---

# Error: Command 'elastix' returned non-zero exit status 3221225785.

**Topic ID**: 19255
**Date**: 2021-08-18
**URL**: https://discourse.slicer.org/t/error-command-elastix-returned-non-zero-exit-status-3221225785/19255

---

## Post #1 by @srathee (2021-08-18 14:58 UTC)

<p>HI: I am completely new to 3D slicer, downloaded 2 days. I wanted to use Elastix and tried it using the MR tumor sample images, but I get the message: Error: Command ‘elastix’ returned non-zero exit status 3221225785.<br>
I have tried the latest version 4.13… instead of 4.11 both give the same error.<br>
Tried to :uninstall and install Elastix extension, same thing.<br>
The log file is copied below.</p>
<pre><code class="lang-nohighlight">[DEBUG][Qt] 18.08.2021 06:44:27 [] (unknown:0) - Session start time .......: 2021-08-18 06:44:27
[DEBUG][Qt] 18.08.2021 06:44:27 [] (unknown:0) - Slicer version ...........: 4.11.20210226 (revision 29738 / 7a593c8) win-amd64 - installed release
[DEBUG][Qt] 18.08.2021 06:44:27 [] (unknown:0) - Operating system .........: Windows /  Professional / (Build 18363, Code Page 65001) - 64-bit
[DEBUG][Qt] 18.08.2021 06:44:27 [] (unknown:0) - Memory ...................: 16031 MB physical, 18463 MB virtual
[DEBUG][Qt] 18.08.2021 06:44:27 [] (unknown:0) - CPU ......................: GenuineIntel , 20 cores, 20 logical processors
[DEBUG][Qt] 18.08.2021 06:44:27 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 18.08.2021 06:44:27 [] (unknown:0) - Qt configuration .........: version 5.15.1, with SSL, requested OpenGL 3.2 (compatibility profile)
[DEBUG][Qt] 18.08.2021 06:44:27 [] (unknown:0) - Developer mode enabled ...: no
[DEBUG][Qt] 18.08.2021 06:44:27 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 18.08.2021 06:44:27 [] (unknown:0) - Application path .........: C:/Users/satyapal/AppData/Local/NA-MIC/Slicer 4.11.20210226/bin
[DEBUG][Qt] 18.08.2021 06:44:27 [] (unknown:0) - Additional module paths ..: NA-MIC/Extensions-29738/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules
[DEBUG][Python] 18.08.2021 06:44:30 [Python] (C:\Users\satyapal\AppData\Local\NA-MIC\Slicer 4.11.20210226\lib\Python\Lib\site-packages\pydicom\datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword...
[DEBUG][Python] 18.08.2021 06:44:32 [Python] (C:\Users\satyapal\AppData\Local\NA-MIC\Slicer 4.11.20210226\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 18.08.2021 06:44:32 [Python] (C:\Users\satyapal\AppData\Local\NA-MIC\Slicer 4.11.20210226\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 18.08.2021 06:44:32 [Python] (C:\Users\satyapal\AppData\Local\NA-MIC\Slicer 4.11.20210226\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 18.08.2021 06:44:33 [] (unknown:0) - Switch to module:  "Welcome"
[DEBUG][Python] 18.08.2021 06:44:38 [Python] (C:/Users/satyapal/AppData/Local/NA-MIC/Slicer 4.11.20210226/bin/../lib/Slicer-4.11/qt-scripted-modules/SampleData.py:373) - &lt;p&gt;Status: &lt;i&gt;Idle&lt;/i&gt;&lt;/p&gt;
[DEBUG][Qt] 18.08.2021 06:44:38 [] (unknown:0) - Switch to module:  "SampleData"
[DEBUG][Python] 18.08.2021 06:44:40 [Python] (C:/Users/satyapal/AppData/Local/NA-MIC/Slicer 4.11.20210226/bin/../lib/Slicer-4.11/qt-scripted-modules/SampleData.py:373) - &lt;b&gt;Verifying checksum&lt;/b&gt;
[DEBUG][Python] 18.08.2021 06:44:40 [Python] (C:/Users/satyapal/AppData/Local/NA-MIC/Slicer 4.11.20210226/bin/../lib/Slicer-4.11/qt-scripted-modules/SampleData.py:373) - &lt;b&gt;File already exists and checksum is OK - reusing it.&lt;/b&gt;
[DEBUG][Python] 18.08.2021 06:44:40 [Python] (C:/Users/satyapal/AppData/Local/NA-MIC/Slicer 4.11.20210226/bin/../lib/Slicer-4.11/qt-scripted-modules/SampleData.py:373) - &lt;b&gt;Requesting load&lt;/b&gt; &lt;i&gt;MRBrainTumor1&lt;/i&gt; from C:/Users/satyapal/AppData/Local/NA-MIC/Slicer/cache/SlicerIO/RegLib_C01_1.nrrd ...
[DEBUG][Python] 18.08.2021 06:44:40 [Python] (C:/Users/satyapal/AppData/Local/NA-MIC/Slicer 4.11.20210226/bin/../lib/Slicer-4.11/qt-scripted-modules/SampleData.py:373) - &lt;b&gt;Load finished&lt;/b&gt;
[INFO][VTK] 18.08.2021 06:44:40 [vtkMRMLVolumeArchetypeStorageNode (00000176CEAF2920)] (D:\D\S\Slicer-1\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:509) - Loaded volume from file: C:/Users/satyapal/AppData/Local/NA-MIC/Slicer/cache/SlicerIO/RegLib_C01_1.nrrd. Dimensions: 256x256x112. Number of components: 1. Pixel type: short.
[DEBUG][Qt] 18.08.2021 06:44:40 [] (unknown:0) - "Volume" Reader has successfully read the file "C:/Users/satyapal/AppData/Local/NA-MIC/Slicer/cache/SlicerIO/RegLib_C01_1.nrrd" "[0.18s]"
[DEBUG][Python] 18.08.2021 06:44:42 [Python] (C:/Users/satyapal/AppData/Local/NA-MIC/Slicer 4.11.20210226/bin/../lib/Slicer-4.11/qt-scripted-modules/SampleData.py:373) - &lt;b&gt;Verifying checksum&lt;/b&gt;
[DEBUG][Python] 18.08.2021 06:44:42 [Python] (C:/Users/satyapal/AppData/Local/NA-MIC/Slicer 4.11.20210226/bin/../lib/Slicer-4.11/qt-scripted-modules/SampleData.py:373) - &lt;b&gt;File already exists and checksum is OK - reusing it.&lt;/b&gt;
[DEBUG][Python] 18.08.2021 06:44:42 [Python] (C:/Users/satyapal/AppData/Local/NA-MIC/Slicer 4.11.20210226/bin/../lib/Slicer-4.11/qt-scripted-modules/SampleData.py:373) - &lt;b&gt;Requesting load&lt;/b&gt; &lt;i&gt;MRBrainTumor2&lt;/i&gt; from C:/Users/satyapal/AppData/Local/NA-MIC/Slicer/cache/SlicerIO/RegLib_C01_2.nrrd ...
[DEBUG][Python] 18.08.2021 06:44:42 [Python] (C:/Users/satyapal/AppData/Local/NA-MIC/Slicer 4.11.20210226/bin/../lib/Slicer-4.11/qt-scripted-modules/SampleData.py:373) - &lt;b&gt;Load finished&lt;/b&gt;
[INFO][VTK] 18.08.2021 06:44:42 [vtkMRMLVolumeArchetypeStorageNode (00000176CEAF19A0)] (D:\D\S\Slicer-1\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:509) - Loaded volume from file: C:/Users/satyapal/AppData/Local/NA-MIC/Slicer/cache/SlicerIO/RegLib_C01_2.nrrd. Dimensions: 256x256x130. Number of components: 1. Pixel type: short.
[DEBUG][Qt] 18.08.2021 06:44:42 [] (unknown:0) - "Volume" Reader has successfully read the file "C:/Users/satyapal/AppData/Local/NA-MIC/Slicer/cache/SlicerIO/RegLib_C01_2.nrrd" "[0.16s]"
[WARNING][Python] 18.08.2021 06:44:52 [Python] (C:\Users\satyapal\AppData\Local\NA-MIC\Slicer 4.11.20210226\bin\Python\slicer\util.py:2160) - toVTKString is deprecated! Conversion is no longer necessary.
[DEBUG][Qt] 18.08.2021 06:44:52 [] (unknown:0) - Switch to module:  "Elastix"
[CRITICAL][Stream] 18.08.2021 06:44:52 [] (unknown:0) - toVTKString is deprecated! Conversion is no longer necessary.
[INFO][Python] 18.08.2021 06:45:49 [Python] (C:/Users/satyapal/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules/Elastix.py:392) - Volume registration is started in working directory: C:/Users/satyapal/AppData/Local/Temp/Slicer/Elastix/20210818_064549_257
[INFO][Stream] 18.08.2021 06:45:49 [] (unknown:0) - Volume registration is started in working directory: C:/Users/satyapal/AppData/Local/Temp/Slicer/Elastix/20210818_064549_257
[INFO][Python] 18.08.2021 06:45:49 [Python] (C:/Users/satyapal/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules/Elastix.py:392) - Register volumes...
[WARNING][VTK] 18.08.2021 06:45:49 [] (unknown:0) - Generic Warning: In D:\D\S\Slicer-1\Libs\MRML\Core\vtkDataFileFormatHelper.cxx, line 237
vtkDataFileFormatHelper::GetFileExtensionFromFormatString: please update deprecated extension-only format specifier to 'File format name (.ext)' format! Current format string: .mha
[WARNING][VTK] 18.08.2021 06:45:49 [] (unknown:0) - Generic Warning: In D:\D\S\Slicer-1\Libs\MRML\Core\vtkDataFileFormatHelper.cxx, line 237
vtkDataFileFormatHelper::GetFileExtensionFromFormatString: please update deprecated extension-only format specifier to 'File format name (.ext)' format! Current format string: .mha
[INFO][Stream] 18.08.2021 06:45:49 [] (unknown:0) - Register volumes...
[WARNING][Python] 18.08.2021 06:45:49 [Python] (C:\Users\satyapal\AppData\Local\NA-MIC\Slicer 4.11.20210226\bin\Python\slicer\util.py:2160) - toVTKString is deprecated! Conversion is no longer necessary.
[INFO][Python] 18.08.2021 06:45:49 [Python] (C:/Users/satyapal/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules/Elastix.py:493) - Register volumes using: C:\Users\satyapal\AppData\Local\NA-MIC\Slicer 4.11.20210226\NA-MIC\Extensions-29738\SlicerElastix\lib\Slicer-4.11\elastix.exe: ['-f', 'C:/Users/satyapal/AppData/Local/Temp/Slicer/Elastix/20210818_064549_257\\input\\fixed.mha', '-m', 'C:/Users/satyapal/AppData/Local/Temp/Slicer/Elastix/20210818_064549_257\\input\\moving.mha', '-out', 'C:/Users/satyapal/AppData/Local/Temp/Slicer/Elastix/20210818_064549_257\\result-transform', '-p', 'C:\\Users\\satyapal\\AppData\\Local\\NA-MIC\\Slicer 4.11.20210226\\NA-MIC\\Extensions-29738\\SlicerElastix\\lib\\Slicer-4.11\\qt-scripted-modules\\Resources\\RegistrationParameters\\Parameters_Rigid.txt', '-p', 'C:\\Users\\satyapal\\AppData\\Local\\NA-MIC\\Slicer 4.11.20210226\\NA-MIC\\Extensions-29738\\SlicerElastix\\lib\\Slicer-4.11\\qt-scripted-modules\\Resources\\RegistrationParameters\\Parameters_BSpline.txt']
[CRITICAL][Stream] 18.08.2021 06:45:49 [] (unknown:0) - toVTKString is deprecated! Conversion is no longer necessary.
[INFO][Stream] 18.08.2021 06:45:49 [] (unknown:0) - Register volumes using: C:\Users\satyapal\AppData\Local\NA-MIC\Slicer 4.11.20210226\NA-MIC\Extensions-29738\SlicerElastix\lib\Slicer-4.11\elastix.exe: ['-f', 'C:/Users/satyapal/AppData/Local/Temp/Slicer/Elastix/20210818_064549_257\\input\\fixed.mha', '-m', 'C:/Users/satyapal/AppData/Local/Temp/Slicer/Elastix/20210818_064549_257\\input\\moving.mha', '-out', 'C:/Users/satyapal/AppData/Local/Temp/Slicer/Elastix/20210818_064549_257\\result-transform', '-p', 'C:\\Users\\satyapal\\AppData\\Local\\NA-MIC\\Slicer 4.11.20210226\\NA-MIC\\Extensions-29738\\SlicerElastix\\lib\\Slicer-4.11\\qt-scripted-modules\\Resources\\RegistrationParameters\\Parameters_Rigid.txt', '-p', 'C:\\Users\\satyapal\\AppData\\Local\\NA-MIC\\Slicer 4.11.20210226\\NA-MIC\\Extensions-29738\\SlicerElastix\\lib\\Slicer-4.11\\qt-scripted-modules\\Resources\\RegistrationParameters\\Parameters_BSpline.txt']
[INFO][Stream] 18.08.2021 06:45:49 [] (unknown:0) - Command 'elastix' returned non-zero exit status 3221225785.
[CRITICAL][Stream] 18.08.2021 06:45:49 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 18.08.2021 06:45:49 [] (unknown:0) -   File "C:/Users/satyapal/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules/Elastix.py", line 335, in onApplyButton
[CRITICAL][Stream] 18.08.2021 06:45:49 [] (unknown:0) -     forceDisplacementFieldOutputTransform = self.forceDisplacementFieldOutputChecbox.checked)
[CRITICAL][Stream] 18.08.2021 06:45:49 [] (unknown:0) -   File "C:/Users/satyapal/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules/Elastix.py", line 807, in registerVolumes
[CRITICAL][Stream] 18.08.2021 06:45:49 [] (unknown:0) -     self.logProcessOutput(ep)
[CRITICAL][Stream] 18.08.2021 06:45:49 [] (unknown:0) -   File "C:/Users/satyapal/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules/Elastix.py", line 728, in logProcessOutput
[CRITICAL][Stream] 18.08.2021 06:45:49 [] (unknown:0) -     raise subprocess.CalledProcessError(return_code, "elastix")
[CRITICAL][Stream] 18.08.2021 06:45:49 [] (unknown:0) - subprocess.CalledProcessError: Command 'elastix' returned non-zero exit status 3221225785.
[DEBUG][Qt] 18.08.2021 07:07:15 [] (unknown:0) - Switch to module:  ""
</code></pre>
<p>Please help.</p>

---

## Post #2 by @lassoan (2021-09-07 19:24 UTC)

<p>I’ve checked this exact same registration - same input data, same registration settings, same operating system - and it works well.</p>
<p>The error code 3221225785 (more commonly used in hexadecimal form 0xc0000135) means that there is a dll conflict. You probably have an ITK-based application in your system path, which conflicts with Slicer. If you clean up your system paths (at least in the environment where you launch Slicer) then the problem should go away.</p>

---

## Post #3 by @srathee (2021-09-16 21:03 UTC)

<p>I know this is probably a question for my own it, would not uninstall followed by install would clear the system path of the conflicting dll?<br>
Thanks</p>

---

## Post #4 by @lassoan (2021-09-16 22:43 UTC)

<p>Uninstalling/installing Slicer or extensions will probably not help. You would need to temporarily rename or delete the conflicting Elastix DLLs on your system.</p>

---
