---
topic_id: 12902
title: "Slicerdcm2Nii Error"
date: 2020-08-08
url: https://discourse.slicer.org/t/12902
---

# SlicerDcm2nii error

**Topic ID**: 12902
**Date**: 2020-08-08
**URL**: https://discourse.slicer.org/t/slicerdcm2nii-error/12902

---

## Post #1 by @KIM_TY (2020-08-08 00:04 UTC)

<p>Hi</p>
<p>Thank you for the SlicerDMR Quick Feedback.</p>
<p>I felt that the usefulness of the forum was great.</p>
<p>This is another error report.</p>
<p>Error for SlicerDcm2nii among Diffusion-related extension apps.</p>
<p>If 60% is reached while loading the Dicom, the program will run SlicerDcm2nii and exit.</p>
<p>If uninstall and reload the SlicerDcm2nii, it will run without a problem.</p>
<p>I pay our respects to all 3D slicer developers.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/aef21968d7bf034c71de46ab65780127b8c962fe.jpeg" alt="20200808_081554" data-base62-sha1="oXDM3zgEmzDx0VDRoIym5MsscvI" width="570" height="320"></p>

---

## Post #2 by @pieper (2020-08-10 16:28 UTC)

<p>Hi - thanks for the kind words about Slicer and the forum!</p>
<p>Are you able to get a log from a time when you get the hang/crash?  The logs from previous runs will be in the Help -&gt; Report a bug menu item’s dialog.</p>
<p>Also is it reproducible using public data?</p>

---

## Post #3 by @KIM_TY (2020-08-10 21:51 UTC)

<p>Thank you for replying.</p>
<p>Public data can be loaded without any problems.</p>
<p>It’s Report a bug.</p>
<p>[DEBUG][Qt] 11.08.2020 06:37:14 [] (unknown:0) - “Python Metric Script” Reader has successfully read the file “C:/Users/KIMTY/AppData/Roaming/NA-MIC/Extensions-29256/PerkTutor/lib/Slicer-4.11/qt-scripted-modules\PythonMetrics\TissueTime.py” “[0.01s]”<br>
[DEBUG][Python] 11.08.2020 06:37:14 [Python] (C:\Users\KIMTY\AppData\Local\NA-MIC\Slicer 4.11.0-2020-08-07\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 11.08.2020 06:37:14 [Python] (C:\Users\KIMTY\AppData\Local\NA-MIC\Slicer 4.11.0-2020-08-07\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[INFO][Python] 11.08.2020 06:37:16 [Python] (C:/Users/KIMTY/AppData/Roaming/NA-MIC/Extensions-29256/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAA.py:32) - This plugin dir: C:/Users/KIMTY/AppData/Roaming/NA-MIC/Extensions-29256/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules<br>
[DEBUG][Qt] 11.08.2020 06:37:15 [] (unknown:0) - Switch to module:  “Welcome”<br>
[INFO][Stream] 11.08.2020 06:37:16 [] (unknown:0) - OnMRMLSceneNodeAdded()<br>
[INFO][Stream] 11.08.2020 06:37:16 [] (unknown:0) - setEditorParamNode()<br>
[INFO][Stream] 11.08.2020 06:37:16 [] (unknown:0) - 0000024C912FE940::1<br>
[INFO][Stream] 11.08.2020 06:37:16 [] (unknown:0) - setEditorParamNode()END<br>
[INFO][Stream] 11.08.2020 06:37:16 [] (unknown:0) - This plugin dir: C:/Users/KIMTY/AppData/Roaming/NA-MIC/Extensions-29256/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules<br>
[INFO][Stream] 11.08.2020 06:37:16 [] (unknown:0) - OnMRMLSceneNodeAdded()<br>
[INFO][Stream] 11.08.2020 06:37:16 [] (unknown:0) - setEditorParamNode()<br>
[INFO][Stream] 11.08.2020 06:37:16 [] (unknown:0) - 0000024C912FE940::2<br>
[INFO][Stream] 11.08.2020 06:37:16 [] (unknown:0) - setEditorParamNode()END<br>
[INFO][VTK] 11.08.2020 06:37:16 [vtkMRMLVolumeArchetypeStorageNode (0000024CE20D1340)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:470) - Loaded volume from file: C:/Users/KIMTY/AppData/Roaming/NA-MIC/Extensions-29256/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules/Resources/Vesselness.png. Dimensions: 65x50x1. Number of components: 3. Pixel type: unsigned char.<br>
[WARNING][Qt] 11.08.2020 06:37:21 [] (unknown:0) - An OpenGL Core Profile was requested, but it is not supported on the current platform. Falling back to a non-Core profile. Note that this might cause rendering issues.<br>
[WARNING][Qt] 11.08.2020 06:37:21 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:21 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:21 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:21 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:21 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:21 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:21 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:21 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:21 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:21 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:21 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:21 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:21 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:21 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:21 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:21 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:21 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:21 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:21 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:21 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:21 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:21 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile<br>
[WARNING][Qt] 11.08.2020 06:37:21 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:21 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:21 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:21 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:21 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:21 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:21 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:22 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:22 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:22 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:22 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:22 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:22 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:22 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:22 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:22 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:22 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:22 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:22 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:22 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:22 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:22 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:22 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:22 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:22 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:22 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:22 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:22 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:22 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:22 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:22 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:22 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:22 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 11.08.2020 06:37:22 [] (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[DEBUG][Qt] 11.08.2020 06:37:30 [] (unknown:0) - “Retrieving extension metadata [ extensionId: 391026]”<br>
[DEBUG][Qt] 11.08.2020 06:37:30 [] (unknown:0) - “Downloading extension [ itemId: 533431]”<br>
[DEBUG][Qt] 11.08.2020 06:37:33 [] (unknown:0) - “Installed extension SlicerDcm2nii (391026) revision 4f09c62”<br>
[DEBUG][Qt] 11.08.2020 06:37:38 [] (unknown:0) - Switch to module:  “”<br>
[WARNING][Qt] 11.08.2020 06:37:38 [] (unknown:0) - Warning sound object is invalid</p>

---

## Post #4 by @pieper (2020-08-10 22:08 UTC)

<aside class="quote no-group quote-modified" data-username="KIM_TY" data-post="3" data-topic="12902">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kim_ty/48/7283_2.png" class="avatar"> KIM_TY:</div>
<blockquote>
<p>[DEBUG][Qt] 11.08.2020 06:37:30 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “Downloading extension [ itemId: 533431]”<br>
[DEBUG][Qt] 11.08.2020 06:37:33 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “Installed extension SlicerDcm2nii (391026) revision 4f09c62”</p>
</blockquote>
</aside>
<p>This indicates that this is the log for the installation of SlicerDcm2nii.  Can you find a log for one of the times it hangs?</p>
<p>What kind of data are you trying to load?  Does it work if you run dcm2nii on the command line directly?</p>

---

## Post #5 by @lassoan (2020-08-11 13:38 UTC)

<p>You have also seem to have installed many extensions. Maybe some of them interferes with the loading. It would be useful to try uninstalling all the extensions and install only that you need right now (later you can install more and see which one causes problem and we can fix that then).</p>
<p>This error is also very odd: “An OpenGL Core Profile was requested, but it is not supported on the current platform”. What graphics card and CPU you have in this computer?</p>

---

## Post #6 by @KIM_TY (2020-08-11 17:21 UTC)

<p>Thank you for your answer.</p>
<p>To simplify the contents of the bug, Slicer 4.11.0-2020-08-10 was newly installed and the extended plug-in was only installed with SlicerDcm2nii.</p>
<p>Report a bug when loading the Dicom file again.</p>
<p>[DEBUG][Qt] 12.08.2020 02:13:58 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 2020-08-12 02:13:58<br>
[DEBUG][Qt] 12.08.2020 02:13:58 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 4.11.0-2020-08-10 (revision 29263 / 6afabbc) win-amd64 - installed release<br>
[DEBUG][Qt] 12.08.2020 02:13:58 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows /  Professional / (Build 18363, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 12.08.2020 02:13:58 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 15791 MB physical, 18223 MB virtual<br>
[DEBUG][Qt] 12.08.2020 02:13:58 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: AuthenticAMD AMD Ryzen 5 4600H with Radeon Graphics         , 12 cores, 12 logical processors<br>
[DEBUG][Qt] 12.08.2020 02:13:58 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 12.08.2020 02:13:58 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.0, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 12.08.2020 02:13:58 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 12.08.2020 02:13:58 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 12.08.2020 02:13:58 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin<br>
[DEBUG][Qt] 12.08.2020 02:13:58 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: C:/Users/KIMTY/AppData/Roaming/NA-MIC/Extensions-29263/SlicerDcm2nii/lib/Slicer-4.11/qt-scripted-modules<br>
[DEBUG][Python] 12.08.2020 02:13:59 [Python] (C:\Users\KIMTY\AppData\Local\NA-MIC\Slicer 4.11.0-2020-08-10\lib\Python\Lib\site-packages\pydicom\datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…<br>
[DEBUG][Python] 12.08.2020 02:14:00 [Python] (C:\Users\KIMTY\AppData\Local\NA-MIC\Slicer 4.11.0-2020-08-10\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 12.08.2020 02:14:00 [Python] (C:\Users\KIMTY\AppData\Local\NA-MIC\Slicer 4.11.0-2020-08-10\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 12.08.2020 02:14:00 [Python] (C:\Users\KIMTY\AppData\Local\NA-MIC\Slicer 4.11.0-2020-08-10\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 12.08.2020 02:14:00 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”</p>
<p>Log message content after executing 3d slicer again.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc75528b918be3fd8616f5a10773c22510276b2e.jpeg" data-download-href="/uploads/short-url/qTb7QIu0IuWV4u4mYNBtDenKaXY.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc75528b918be3fd8616f5a10773c22510276b2e_2_690x420.jpeg" alt="1" data-base62-sha1="qTb7QIu0IuWV4u4mYNBtDenKaXY" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc75528b918be3fd8616f5a10773c22510276b2e_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc75528b918be3fd8616f5a10773c22510276b2e.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc75528b918be3fd8616f5a10773c22510276b2e.jpeg 2x" data-dominant-color="E1E6ED"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">756×461 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I’m about to load a CT or MRI Dicom file acquired by the hospital. DCM files other than DTI will also be closed during the loading of dcm2nii.</p>
<p>In Slicer 4.10.2 version, I can load it without any problem even if install dcm2nii.</p>

---

## Post #7 by @KIM_TY (2020-08-11 17:22 UTC)

<p><em>Thank you for your answer.</em></p>
<p><em>If I install only SlicerDcm2nii without installing another extension, the error is the same.</em></p>
<p><em>This is ASUS’ gaming laptop released in 2020.(Renoir)</em></p>
<p><em>ASUS TUF GAMING A15 FA506II-HN162</em><br>
<em>-------------------------------------------------------------------------</em><br>
<em>Socket 1	CPU</em></p>
<ul>
<li>Manufacturer		AuthenticAMD*</li>
<li>Name			AMD Ryzen 5 Mobile*</li>
<li>Codename		Renoir*</li>
<li>Specification		AMD Ryzen 5 4600H with Radeon Graphics         *</li>
<li>Package 		Socket FP5*</li>
<li>CPUID			F.0.1*</li>
<li>Extended CPUID		17.60*</li>
<li>Core Stepping		*</li>
<li>Technology		7 nm*</li>
<li>Core Speed		1397.2 MHz*<br>
<em>-------------------------------------------------------------------------</em><br>
<em>Display adapter 1</em>
</li>
<li>Name			NVIDIA GeForce GTX 1650 Ti*</li>
<li>Board Manufacturer	ASUSTeK Computer Inc.*</li>
<li>Revision		A1*</li>
<li>Core family		0x167 (0x167)*</li>
<li>Memory size		4 GB*</li>
<li>Memory type		GDDR6*<br>
<em>-------------------------------------------------------------------------</em><br>
<em>Memory Type			DDR4</em><br>
<em>Memory Size			16 GBytes</em><br>
<em>Channels			Dual</em><br>
<em>Memory Frequency		1596.8 MHz (1:16)</em><br>
<em>-------------------------------------------------------------------------</em><br>
*Monitor 0	*</li>
<li>Model			 ()*</li>
<li>ID			NCP004D*</li>
<li>Serial			*</li>
<li>Manufacturing Date	Week 51, Year 2019*</li>
<li>Size			15.3 inches*</li>
<li>Max Resolution		1920 x 1080 @ 144 Hz*</li>
</ul>

---

## Post #8 by @lassoan (2020-08-11 18:15 UTC)

<p>Thanks for the additional information. Interestingly, in this log there is no “An OpenGL Core Profile was requested, but it is not supported on the current platform” warning message.</p>
<p>In the log, the last message is “Switch to module: Welcome”, which means that it is not the log of the session where you tried DICOM import. You need to go to menu: Help / Report a bug, and in the listbox select a previous session (by default, logs of the current session is displayed).</p>

---

## Post #9 by @KIM_TY (2020-08-11 18:58 UTC)

<p>Thank you for your additional reply.</p>
<p>What’s interesting is that I thought it was a hardware problem, but the Slicer 4.10.2 version doesn’t have this error.</p>
<p>The latest release of the 3D slider version creates the same trouble on my other desktop PC and MSI Gamming laptop.</p>
<p>There was no problem with the version installed in May, but since June, there has been a loading trouble for SlicerDcm2nii.</p>
<p>This is a message after loading Dicom in Slider 4.10.2 version.SlicerDcm2nii is installed.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be4fefa2ad6c29318f039e34d3c2baaf943931d8.jpeg" data-download-href="/uploads/short-url/r9zYRpTDSa32YbgGvuy5u101t2g.jpeg?dl=1" title="1-vert" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/be4fefa2ad6c29318f039e34d3c2baaf943931d8_2_690x426.jpeg" alt="1-vert" data-base62-sha1="r9zYRpTDSa32YbgGvuy5u101t2g" width="690" height="426" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/be4fefa2ad6c29318f039e34d3c2baaf943931d8_2_690x426.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/be4fefa2ad6c29318f039e34d3c2baaf943931d8_2_1035x639.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be4fefa2ad6c29318f039e34d3c2baaf943931d8.jpeg 2x" data-dominant-color="E6E9EF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1-vert</span><span class="informations">1156×715 182 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @lassoan (2020-08-11 19:03 UTC)

<p>Could you provide the actual log (menu: Help / Report a bug) instead of a screenshot? The screenshot only contains a small fraction of the log messages.</p>

---

## Post #11 by @KIM_TY (2020-08-11 19:06 UTC)

<p>O.K</p>
<p>To simplify the contents of the bug, Slicer 4.11.0-2020-08-10 was newly installed and the extended plug-in was only installed with SlicerDcm2nii.</p>
<p>Report a bug when loading the Dicom file again.</p>
<p>[DEBUG][Qt] 12.08.2020 04:05:05 [] (unknown:0) - Session start time …: 2020-08-12 04:05:05<br>
[DEBUG][Qt] 12.08.2020 04:05:05 [] (unknown:0) - Slicer version …: 4.11.0-2020-08-10 (revision 29263 / 6afabbc) win-amd64 - installed release<br>
[DEBUG][Qt] 12.08.2020 04:05:05 [] (unknown:0) - Operating system …: Windows /  Professional / (Build 18363, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 12.08.2020 04:05:05 [] (unknown:0) - Memory …: 15791 MB physical, 18223 MB virtual<br>
[DEBUG][Qt] 12.08.2020 04:05:05 [] (unknown:0) - CPU …: AuthenticAMD AMD Ryzen 5 4600H with Radeon Graphics         , 12 cores, 12 logical processors<br>
[DEBUG][Qt] 12.08.2020 04:05:05 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 12.08.2020 04:05:05 [] (unknown:0) - Qt configuration …: version 5.15.0, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 12.08.2020 04:05:05 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 12.08.2020 04:05:05 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 12.08.2020 04:05:05 [] (unknown:0) - Application path …: C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin<br>
[DEBUG][Qt] 12.08.2020 04:05:05 [] (unknown:0) - Additional module paths …: C:/Users/KIMTY/AppData/Roaming/NA-MIC/Extensions-29263/SlicerDcm2nii/lib/Slicer-4.11/qt-scripted-modules<br>
[DEBUG][Python] 12.08.2020 04:05:06 [Python] (C:\Users\KIMTY\AppData\Local\NA-MIC\Slicer 4.11.0-2020-08-10\lib\Python\Lib\site-packages\pydicom\datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…<br>
[DEBUG][Python] 12.08.2020 04:05:07 [Python] (C:\Users\KIMTY\AppData\Local\NA-MIC\Slicer 4.11.0-2020-08-10\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 12.08.2020 04:05:07 [Python] (C:\Users\KIMTY\AppData\Local\NA-MIC\Slicer 4.11.0-2020-08-10\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 12.08.2020 04:05:07 [Python] (C:\Users\KIMTY\AppData\Local\NA-MIC\Slicer 4.11.0-2020-08-10\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 12.08.2020 04:05:07 [] (unknown:0) - Switch to module:  “Welcome”</p>

---

## Post #12 by @lassoan (2020-08-11 19:07 UTC)

<p>Good, now try to load data using dcm2nii and send the log of that.</p>

---

## Post #13 by @KIM_TY (2020-08-11 19:12 UTC)

<p>The contents of the above article are Report a bug that already installed dcm2nii and loaded Dicom.</p>

---

## Post #14 by @KIM_TY (2020-08-11 19:16 UTC)

<p>Report a bug when dcm2nii is uninstalled and Dicom is loaded.</p>
<p>[DEBUG][Qt] 12.08.2020 04:14:09 [] (unknown:0) - Session start time …: 2020-08-12 04:14:09<br>
[DEBUG][Qt] 12.08.2020 04:14:09 [] (unknown:0) - Slicer version …: 4.11.0-2020-08-10 (revision 29263 / 6afabbc) win-amd64 - installed release<br>
[DEBUG][Qt] 12.08.2020 04:14:09 [] (unknown:0) - Operating system …: Windows /  Professional / (Build 18363, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 12.08.2020 04:14:09 [] (unknown:0) - Memory …: 15791 MB physical, 18223 MB virtual<br>
[DEBUG][Qt] 12.08.2020 04:14:09 [] (unknown:0) - CPU …: AuthenticAMD AMD Ryzen 5 4600H with Radeon Graphics         , 12 cores, 12 logical processors<br>
[DEBUG][Qt] 12.08.2020 04:14:09 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 12.08.2020 04:14:09 [] (unknown:0) - Qt configuration …: version 5.15.0, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 12.08.2020 04:14:09 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 12.08.2020 04:14:09 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 12.08.2020 04:14:09 [] (unknown:0) - Application path …: C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin<br>
[DEBUG][Qt] 12.08.2020 04:14:09 [] (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 12.08.2020 04:14:10 [Python] (C:\Users\KIMTY\AppData\Local\NA-MIC\Slicer 4.11.0-2020-08-10\lib\Python\Lib\site-packages\pydicom\datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…<br>
[DEBUG][Python] 12.08.2020 04:14:11 [Python] (C:\Users\KIMTY\AppData\Local\NA-MIC\Slicer 4.11.0-2020-08-10\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 12.08.2020 04:14:11 [Python] (C:\Users\KIMTY\AppData\Local\NA-MIC\Slicer 4.11.0-2020-08-10\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 12.08.2020 04:14:11 [Python] (C:\Users\KIMTY\AppData\Local\NA-MIC\Slicer 4.11.0-2020-08-10\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 12.08.2020 04:14:11 [] (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 12.08.2020 04:14:18 [] (unknown:0) - Switch to module:  “DICOM”<br>
[WARNING][Python] 12.08.2020 04:14:24 [Python] (C:\Users\KIMTY\AppData\Local\NA-MIC\Slicer 4.11.0-2020-08-10\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMUtils.py:629) - Geometric issues were found with 1 of the series. Please use caution.<br>
[CRITICAL][Stream] 12.08.2020 04:14:24 [] (unknown:0) - Geometric issues were found with 1 of the series. Please use caution.<br>
[CRITICAL][Stream] 12.08.2020 04:14:24 [] (unknown:0) -<br>
[DEBUG][Python] 12.08.2020 04:14:24 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py:456) - MultiVolumeImportPlugin::examine<br>
[DEBUG][Python] 12.08.2020 04:14:28 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py:496) - DICOMMultiVolumePlugin found 1 multivolumes!<br>
[DEBUG][Python] 12.08.2020 04:14:35 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py:168) - MultiVolumeImportPlugin:examineMultiseries<br>
[DEBUG][Python] 12.08.2020 04:14:36 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py:173) - DICOMMultiVolumePlugin found 1 multivolumes!<br>
[INFO][Python] 12.08.2020 04:14:45 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:377) - Loading with imageIOName: GDCM<br>
[INFO][Python] 12.08.2020 04:14:45 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:449) - Window/level found in DICOM tags (center=368.0, width=767.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)<br>
[DEBUG][Python] 12.08.2020 04:14:45 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:782) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.29569e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 12.08.2020 04:14:45 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 12.08.2020 04:14:45 [] (unknown:0) - Window/level found in DICOM tags (center=368.0, width=767.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)<br>
[CRITICAL][Qt] 12.08.2020 04:14:45 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( “1onDisplayNodeModified(vtkObject*, vtkObject*)” ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 12.08.2020 04:14:45 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 12.08.2020 04:14:45 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:377) - Loading with imageIOName: GDCM<br>
[INFO][Python] 12.08.2020 04:14:46 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:449) - Window/level found in DICOM tags (center=66.0, width=195.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_1<br>
[DEBUG][Python] 12.08.2020 04:14:46 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:782) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.29569e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 12.08.2020 04:14:45 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 12.08.2020 04:14:46 [] (unknown:0) - Window/level found in DICOM tags (center=66.0, width=195.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_1<br>
[CRITICAL][Qt] 12.08.2020 04:14:46 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 12.08.2020 04:14:46 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 12.08.2020 04:14:46 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:377) - Loading with imageIOName: GDCM<br>
[INFO][Python] 12.08.2020 04:14:46 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:449) - Window/level found in DICOM tags (center=67.0, width=197.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_2<br>
[DEBUG][Python] 12.08.2020 04:14:46 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:782) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.29569e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 12.08.2020 04:14:46 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 12.08.2020 04:14:46 [] (unknown:0) - Window/level found in DICOM tags (center=67.0, width=197.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_2<br>
[CRITICAL][Qt] 12.08.2020 04:14:46 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 12.08.2020 04:14:46 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 12.08.2020 04:14:46 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:377) - Loading with imageIOName: GDCM<br>
[INFO][Python] 12.08.2020 04:14:46 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:449) - Window/level found in DICOM tags (center=60.0, width=174.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_3<br>
[DEBUG][Python] 12.08.2020 04:14:46 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:782) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.29569e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 12.08.2020 04:14:46 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 12.08.2020 04:14:46 [] (unknown:0) - Window/level found in DICOM tags (center=60.0, width=174.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_3<br>
[CRITICAL][Qt] 12.08.2020 04:14:46 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 12.08.2020 04:14:46 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 12.08.2020 04:14:46 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:377) - Loading with imageIOName: GDCM<br>
[INFO][Python] 12.08.2020 04:14:46 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:449) - Window/level found in DICOM tags (center=64.0, width=189.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_4<br>
[DEBUG][Python] 12.08.2020 04:14:46 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:782) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.29569e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 12.08.2020 04:14:46 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 12.08.2020 04:14:46 [] (unknown:0) - Window/level found in DICOM tags (center=64.0, width=189.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_4<br>
[CRITICAL][Qt] 12.08.2020 04:14:47 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 12.08.2020 04:14:47 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 12.08.2020 04:14:47 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:377) - Loading with imageIOName: GDCM<br>
[INFO][Python] 12.08.2020 04:14:47 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:449) - Window/level found in DICOM tags (center=59.0, width=174.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_5<br>
[DEBUG][Python] 12.08.2020 04:14:47 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:782) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.29569e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 12.08.2020 04:14:47 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 12.08.2020 04:14:47 [] (unknown:0) - Window/level found in DICOM tags (center=59.0, width=174.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_5<br>
[CRITICAL][Qt] 12.08.2020 04:14:47 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 12.08.2020 04:14:47 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 12.08.2020 04:14:47 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:377) - Loading with imageIOName: GDCM<br>
[INFO][Python] 12.08.2020 04:14:47 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:449) - Window/level found in DICOM tags (center=61.0, width=180.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_6<br>
[DEBUG][Python] 12.08.2020 04:14:47 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:782) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.29569e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 12.08.2020 04:14:47 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 12.08.2020 04:14:47 [] (unknown:0) - Window/level found in DICOM tags (center=61.0, width=180.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_6<br>
[CRITICAL][Qt] 12.08.2020 04:14:47 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 12.08.2020 04:14:47 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 12.08.2020 04:14:47 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:377) - Loading with imageIOName: GDCM<br>
[INFO][Python] 12.08.2020 04:14:47 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:449) - Window/level found in DICOM tags (center=63.0, width=183.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_7<br>
[DEBUG][Python] 12.08.2020 04:14:47 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:782) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.29569e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 12.08.2020 04:14:47 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 12.08.2020 04:14:47 [] (unknown:0) - Window/level found in DICOM tags (center=63.0, width=183.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_7<br>
[CRITICAL][Qt] 12.08.2020 04:14:47 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 12.08.2020 04:14:47 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 12.08.2020 04:14:48 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:377) - Loading with imageIOName: GDCM<br>
[INFO][Python] 12.08.2020 04:14:48 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:449) - Window/level found in DICOM tags (center=62.0, width=181.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_8<br>
[DEBUG][Python] 12.08.2020 04:14:48 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:782) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.29569e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 12.08.2020 04:14:48 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 12.08.2020 04:14:48 [] (unknown:0) - Window/level found in DICOM tags (center=62.0, width=181.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_8<br>
[CRITICAL][Qt] 12.08.2020 04:14:48 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 12.08.2020 04:14:48 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 12.08.2020 04:14:48 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:377) - Loading with imageIOName: GDCM<br>
[INFO][Python] 12.08.2020 04:14:48 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:449) - Window/level found in DICOM tags (center=53.0, width=157.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_9<br>
[DEBUG][Python] 12.08.2020 04:14:48 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:782) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.29569e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 12.08.2020 04:14:48 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 12.08.2020 04:14:48 [] (unknown:0) - Window/level found in DICOM tags (center=53.0, width=157.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_9<br>
[CRITICAL][Qt] 12.08.2020 04:14:48 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 12.08.2020 04:14:48 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 12.08.2020 04:14:48 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:377) - Loading with imageIOName: GDCM<br>
[INFO][Python] 12.08.2020 04:14:48 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:449) - Window/level found in DICOM tags (center=59.0, width=174.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_10<br>
[DEBUG][Python] 12.08.2020 04:14:48 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:782) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.29569e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 12.08.2020 04:14:48 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 12.08.2020 04:14:48 [] (unknown:0) - Window/level found in DICOM tags (center=59.0, width=174.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_10<br>
[CRITICAL][Qt] 12.08.2020 04:14:48 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 12.08.2020 04:14:48 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 12.08.2020 04:14:48 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:377) - Loading with imageIOName: GDCM<br>
[INFO][Python] 12.08.2020 04:14:49 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:449) - Window/level found in DICOM tags (center=57.0, width=167.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_11<br>
[DEBUG][Python] 12.08.2020 04:14:49 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:782) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.29569e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 12.08.2020 04:14:48 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 12.08.2020 04:14:49 [] (unknown:0) - Window/level found in DICOM tags (center=57.0, width=167.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_11<br>
[CRITICAL][Qt] 12.08.2020 04:14:49 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 12.08.2020 04:14:49 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 12.08.2020 04:14:49 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:377) - Loading with imageIOName: GDCM<br>
[INFO][Python] 12.08.2020 04:14:49 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:449) - Window/level found in DICOM tags (center=57.0, width=166.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_12<br>
[DEBUG][Python] 12.08.2020 04:14:49 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:782) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.29569e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 12.08.2020 04:14:49 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 12.08.2020 04:14:49 [] (unknown:0) - Window/level found in DICOM tags (center=57.0, width=166.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_12<br>
[CRITICAL][Qt] 12.08.2020 04:14:49 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 12.08.2020 04:14:49 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 12.08.2020 04:14:49 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:377) - Loading with imageIOName: GDCM<br>
[INFO][Python] 12.08.2020 04:14:49 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:449) - Window/level found in DICOM tags (center=55.0, width=161.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_13<br>
[DEBUG][Python] 12.08.2020 04:14:49 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:782) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.29569e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 12.08.2020 04:14:49 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 12.08.2020 04:14:49 [] (unknown:0) - Window/level found in DICOM tags (center=55.0, width=161.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_13<br>
[CRITICAL][Qt] 12.08.2020 04:14:49 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 12.08.2020 04:14:49 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 12.08.2020 04:14:49 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:377) - Loading with imageIOName: GDCM<br>
[INFO][Python] 12.08.2020 04:14:50 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:449) - Window/level found in DICOM tags (center=63.0, width=188.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_14<br>
[DEBUG][Python] 12.08.2020 04:14:50 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:782) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.29569e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 12.08.2020 04:14:49 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 12.08.2020 04:14:50 [] (unknown:0) - Window/level found in DICOM tags (center=63.0, width=188.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_14<br>
[CRITICAL][Qt] 12.08.2020 04:14:50 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 12.08.2020 04:14:50 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 12.08.2020 04:14:50 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:377) - Loading with imageIOName: GDCM<br>
[INFO][Python] 12.08.2020 04:14:50 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:449) - Window/level found in DICOM tags (center=61.0, width=179.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_15<br>
[DEBUG][Python] 12.08.2020 04:14:50 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:782) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.29569e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 12.08.2020 04:14:50 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 12.08.2020 04:14:50 [] (unknown:0) - Window/level found in DICOM tags (center=61.0, width=179.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_15<br>
[CRITICAL][Qt] 12.08.2020 04:14:50 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 12.08.2020 04:14:50 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 12.08.2020 04:14:50 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:377) - Loading with imageIOName: GDCM<br>
[INFO][Python] 12.08.2020 04:14:50 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:449) - Window/level found in DICOM tags (center=56.0, width=164.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_16<br>
[DEBUG][Python] 12.08.2020 04:14:50 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:782) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.29569e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 12.08.2020 04:14:50 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 12.08.2020 04:14:50 [] (unknown:0) - Window/level found in DICOM tags (center=56.0, width=164.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_16<br>
[CRITICAL][Qt] 12.08.2020 04:14:50 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 12.08.2020 04:14:50 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 12.08.2020 04:14:50 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:377) - Loading with imageIOName: GDCM<br>
[INFO][Python] 12.08.2020 04:14:50 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:449) - Window/level found in DICOM tags (center=56.0, width=164.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_17<br>
[DEBUG][Python] 12.08.2020 04:14:50 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:782) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.29569e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 12.08.2020 04:14:50 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 12.08.2020 04:14:50 [] (unknown:0) - Window/level found in DICOM tags (center=56.0, width=164.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_17<br>
[CRITICAL][Qt] 12.08.2020 04:14:50 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 12.08.2020 04:14:50 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 12.08.2020 04:14:51 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:377) - Loading with imageIOName: GDCM<br>
[INFO][Python] 12.08.2020 04:14:51 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:449) - Window/level found in DICOM tags (center=57.0, width=169.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_18<br>
[DEBUG][Python] 12.08.2020 04:14:51 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:782) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.29569e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 12.08.2020 04:14:51 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 12.08.2020 04:14:51 [] (unknown:0) - Window/level found in DICOM tags (center=57.0, width=169.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_18<br>
[CRITICAL][Qt] 12.08.2020 04:14:51 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 12.08.2020 04:14:51 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 12.08.2020 04:14:51 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:377) - Loading with imageIOName: GDCM<br>
[INFO][Python] 12.08.2020 04:14:51 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:449) - Window/level found in DICOM tags (center=58.0, width=171.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_19<br>
[DEBUG][Python] 12.08.2020 04:14:51 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:782) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.29569e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 12.08.2020 04:14:51 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 12.08.2020 04:14:51 [] (unknown:0) - Window/level found in DICOM tags (center=58.0, width=171.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_19<br>
[CRITICAL][Qt] 12.08.2020 04:14:51 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 12.08.2020 04:14:51 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 12.08.2020 04:14:51 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:377) - Loading with imageIOName: GDCM<br>
[INFO][Python] 12.08.2020 04:14:51 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:449) - Window/level found in DICOM tags (center=56.0, width=163.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_20<br>
[DEBUG][Python] 12.08.2020 04:14:51 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:782) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.29569e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 12.08.2020 04:14:51 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 12.08.2020 04:14:51 [] (unknown:0) - Window/level found in DICOM tags (center=56.0, width=163.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_20<br>
[CRITICAL][Qt] 12.08.2020 04:14:51 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 12.08.2020 04:14:51 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 12.08.2020 04:14:51 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:377) - Loading with imageIOName: GDCM<br>
[INFO][Python] 12.08.2020 04:14:52 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:449) - Window/level found in DICOM tags (center=58.0, width=171.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_21<br>
[DEBUG][Python] 12.08.2020 04:14:52 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:782) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.29569e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 12.08.2020 04:14:51 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 12.08.2020 04:14:52 [] (unknown:0) - Window/level found in DICOM tags (center=58.0, width=171.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_21<br>
[CRITICAL][Qt] 12.08.2020 04:14:52 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 12.08.2020 04:14:52 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 12.08.2020 04:14:52 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:377) - Loading with imageIOName: GDCM<br>
[INFO][Python] 12.08.2020 04:14:52 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:449) - Window/level found in DICOM tags (center=63.0, width=186.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_22<br>
[DEBUG][Python] 12.08.2020 04:14:52 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:782) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.29569e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 12.08.2020 04:14:52 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 12.08.2020 04:14:52 [] (unknown:0) - Window/level found in DICOM tags (center=63.0, width=186.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_22<br>
[CRITICAL][Qt] 12.08.2020 04:14:52 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 12.08.2020 04:14:52 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 12.08.2020 04:14:52 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:377) - Loading with imageIOName: GDCM<br>
[INFO][Python] 12.08.2020 04:14:52 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:449) - Window/level found in DICOM tags (center=64.0, width=185.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_23<br>
[DEBUG][Python] 12.08.2020 04:14:52 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:782) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.29569e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 12.08.2020 04:14:52 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 12.08.2020 04:14:52 [] (unknown:0) - Window/level found in DICOM tags (center=64.0, width=185.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_23<br>
[CRITICAL][Qt] 12.08.2020 04:14:52 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 12.08.2020 04:14:52 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 12.08.2020 04:14:52 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:377) - Loading with imageIOName: GDCM<br>
[INFO][Python] 12.08.2020 04:14:52 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:449) - Window/level found in DICOM tags (center=61.0, width=180.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_24<br>
[DEBUG][Python] 12.08.2020 04:14:53 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:782) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.29569e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 12.08.2020 04:14:52 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 12.08.2020 04:14:53 [] (unknown:0) - Window/level found in DICOM tags (center=61.0, width=180.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_24<br>
[CRITICAL][Qt] 12.08.2020 04:14:53 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 12.08.2020 04:14:53 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 12.08.2020 04:14:53 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:377) - Loading with imageIOName: GDCM<br>
[INFO][Python] 12.08.2020 04:14:53 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:449) - Window/level found in DICOM tags (center=66.0, width=196.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_25<br>
[DEBUG][Python] 12.08.2020 04:14:53 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:782) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.29569e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 12.08.2020 04:14:53 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 12.08.2020 04:14:53 [] (unknown:0) - Window/level found in DICOM tags (center=66.0, width=196.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_25<br>
[CRITICAL][Qt] 12.08.2020 04:14:53 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 12.08.2020 04:14:53 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 12.08.2020 04:14:53 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:377) - Loading with imageIOName: GDCM<br>
[INFO][Python] 12.08.2020 04:14:53 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:449) - Window/level found in DICOM tags (center=65.0, width=190.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_26<br>
[DEBUG][Python] 12.08.2020 04:14:53 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:782) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.29569e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 12.08.2020 04:14:53 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 12.08.2020 04:14:53 [] (unknown:0) - Window/level found in DICOM tags (center=65.0, width=190.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_26<br>
[CRITICAL][Qt] 12.08.2020 04:14:53 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 12.08.2020 04:14:53 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 12.08.2020 04:14:53 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:377) - Loading with imageIOName: GDCM<br>
[INFO][Python] 12.08.2020 04:14:53 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:449) - Window/level found in DICOM tags (center=67.0, width=196.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_27<br>
[DEBUG][Python] 12.08.2020 04:14:53 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:782) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.29569e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 12.08.2020 04:14:53 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 12.08.2020 04:14:53 [] (unknown:0) - Window/level found in DICOM tags (center=67.0, width=196.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_27<br>
[CRITICAL][Qt] 12.08.2020 04:14:53 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 12.08.2020 04:14:53 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 12.08.2020 04:14:54 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:377) - Loading with imageIOName: GDCM<br>
[INFO][Python] 12.08.2020 04:14:54 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:449) - Window/level found in DICOM tags (center=63.0, width=183.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_28<br>
[DEBUG][Python] 12.08.2020 04:14:54 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:782) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.29569e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 12.08.2020 04:14:54 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 12.08.2020 04:14:54 [] (unknown:0) - Window/level found in DICOM tags (center=63.0, width=183.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_28<br>
[CRITICAL][Qt] 12.08.2020 04:14:54 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 12.08.2020 04:14:54 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 12.08.2020 04:14:54 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:377) - Loading with imageIOName: GDCM<br>
[INFO][Python] 12.08.2020 04:14:54 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:449) - Window/level found in DICOM tags (center=60.0, width=177.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_29<br>
[DEBUG][Python] 12.08.2020 04:14:54 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:782) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.29569e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 12.08.2020 04:14:54 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 12.08.2020 04:14:54 [] (unknown:0) - Window/level found in DICOM tags (center=60.0, width=177.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_29<br>
[CRITICAL][Qt] 12.08.2020 04:14:54 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 12.08.2020 04:14:54 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 12.08.2020 04:14:54 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:377) - Loading with imageIOName: GDCM<br>
[INFO][Python] 12.08.2020 04:14:54 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:449) - Window/level found in DICOM tags (center=65.0, width=189.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_30<br>
[DEBUG][Python] 12.08.2020 04:14:54 [Python] (C:/Users/KIMTY/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:782) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 7.29569e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 12.08.2020 04:14:54 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 12.08.2020 04:14:54 [] (unknown:0) - Window/level found in DICOM tags (center=65.0, width=189.0) has been applied to volume 3: ep2d_diff_DTI (3mm interp)_30<br>
[CRITICAL][Qt] 12.08.2020 04:14:54 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 12.08.2020 04:14:54 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject *,class vtkObject *) : Invalid object type calling display node modified event</p>

---

## Post #15 by @lassoan (2020-08-11 19:34 UTC)

<p>Thank you for the logs.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> The crash seems to be due to the error that <a class="mention" href="/u/pieper">@pieper</a> fixed <a href="https://github.com/commontk/AppLauncher/pull/117">here</a>. Has a new launcher been built and updated in Slicer?</p>

---

## Post #16 by @KIM_TY (2020-08-11 19:54 UTC)

<p>Thank you for interpreting my log and answering.</p>
<p>When installing dcm2ni in the current state, Slicer 4.10.2 version is stable.</p>
<p>I hope the next version of dcm2nii without colliding with Dicom.</p>

---

## Post #17 by @lassoan (2020-08-11 23:19 UTC)

<p>You can still use latest Slicer Preview Release and SlicerDcm2niix, and just disable its DICOM plugin in the DICOM module:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41c4c6cb4a909fce02b54d4e38ab72359b9db62f.png" data-download-href="/uploads/short-url/9nOCTBZGeVslw9AOYDg4nk4AW3J.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/41c4c6cb4a909fce02b54d4e38ab72359b9db62f_2_690x430.png" alt="image" data-base62-sha1="9nOCTBZGeVslw9AOYDg4nk4AW3J" width="690" height="430" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/41c4c6cb4a909fce02b54d4e38ab72359b9db62f_2_690x430.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/41c4c6cb4a909fce02b54d4e38ab72359b9db62f_2_1035x645.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/41c4c6cb4a909fce02b54d4e38ab72359b9db62f_2_1380x860.png 2x" data-dominant-color="F9F8F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2312×1444 224 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #18 by @KIM_TY (2020-08-13 10:35 UTC)

<p>I solved it.<br>
That’s a good way.<br>
Thank you again master lassoan.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6be119d8b46a93ac1044914dad639c248848ea7.jpeg" data-download-href="/uploads/short-url/nN4tNAvKUJfTTCHJxmCEmu7CJoz.jpeg?dl=1" title="34234" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6be119d8b46a93ac1044914dad639c248848ea7_2_690x448.jpeg" alt="34234" data-base62-sha1="nN4tNAvKUJfTTCHJxmCEmu7CJoz" width="690" height="448" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6be119d8b46a93ac1044914dad639c248848ea7_2_690x448.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6be119d8b46a93ac1044914dad639c248848ea7_2_1035x672.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6be119d8b46a93ac1044914dad639c248848ea7_2_1380x896.jpeg 2x" data-dominant-color="37363B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">34234</span><span class="informations">1417×922 269 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
