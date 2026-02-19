---
topic_id: 45790
title: "Autoscoper Crashes When Trying To Load"
date: 2026-01-15
url: https://discourse.slicer.org/t/45790
---

# Autoscoper crashes when trying to load

**Topic ID**: 45790
**Date**: 2026-01-15
**URL**: https://discourse.slicer.org/t/autoscoper-crashes-when-trying-to-load/45790

---

## Post #1 by @Janae (2026-01-15 20:46 UTC)

<p>Hello,</p>
<p>I have not been able to successfully open Autoscoper and have been receiving the error message included below. I have Slicer 5.10.0 and Autoscoper last update “Mon Nov 10 2025  (Revision: 85cd82f)”. A coworker with Slicer 5.6.2 and Autoscoper “06acebe last update Nov 22 2024” is also seeing the same error. All help is greatly appreciated! Thank you!</p>
<p>Error: File “C:\Users\User\AppData\Local\slicer.org\3D Slicer 5.10.0\lib\Python\Lib\site-packages\PyAutoscoper\connect.py”, line 142, in _openConnection</p>
<p>s.connect((self.address, 30007))</p>
<p>ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it</p>

---

## Post #2 by @John_Holtgrewe (2026-01-16 15:26 UTC)

<p>Hi Janae,</p>
<p>Thanks for reaching out! Were you able to open previous versions of Autoscoper on previous versions of 3D Slicer, or has this always been an issue? Also could you provided some details about the system you are working on: the operating system and GPU?</p>

---

## Post #3 by @Janae (2026-01-16 15:47 UTC)

<p>Thank you for the quick reply!</p>
<p>I have only had Slicer 5.10.0 on this device and have always had the problem. Operating system Windows 11, Intel(R) Graphics, processor Intel(R) Core™ Ultra 5 135U</p>
<p>My coworker had Autoscoper working on Slicer 5.6.2, and it just recently caused the same problem. Operating system Windows 11, Intel(R) Iris(R) XE Graphics, processor 12th Gen Intel(R) Core™ i5-1245U</p>
<p>Let me know if there any other information that might help! Thanks again</p>

---

## Post #4 by @John_Holtgrewe (2026-01-16 18:21 UTC)

<p>Are you launching Autoscoper using CUDA or OpenCL?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bfd56ec2d27acd24c9d959af09122af043184b3f.png" data-download-href="/uploads/short-url/rn2toUeYoSzYQFxTCKZKoTyN2iz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bfd56ec2d27acd24c9d959af09122af043184b3f.png" alt="image" data-base62-sha1="rn2toUeYoSzYQFxTCKZKoTyN2iz" width="627" height="228"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">627×228 6.41 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @Janae (2026-01-16 18:23 UTC)

<p>I have tried both and get the same error.</p>

---

## Post #6 by @John_Holtgrewe (2026-01-16 18:32 UTC)

<p>This sounds similar to an issue another user was having that we haven’t quite been able to figure out yet (<a href="https://discourse.slicer.org/t/trouble-opening-the-load-data/44330/8" class="inline-onebox">Trouble Opening the Load Data - #8 by Megan_Weaver</a>).  Could you share a screenshot of the error you are getting? I will bring this up to our team and see if we can prioritize fixing this issue.</p>

---

## Post #7 by @Janae (2026-01-16 20:14 UTC)

<p>Thank you! This is the entire error I get when launching with OpenCL</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc12021c0a19accbe64ccb40e6ab66127f5b8b79.png" data-download-href="/uploads/short-url/zXUU6W1PEAxlYWsY124hQ16mDfH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc12021c0a19accbe64ccb40e6ab66127f5b8b79_2_690x479.png" alt="image" data-base62-sha1="zXUU6W1PEAxlYWsY124hQ16mDfH" width="690" height="479" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc12021c0a19accbe64ccb40e6ab66127f5b8b79_2_690x479.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc12021c0a19accbe64ccb40e6ab66127f5b8b79.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc12021c0a19accbe64ccb40e6ab66127f5b8b79.png 2x" data-dominant-color="FEF4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">847×588 184 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @allemangd (2026-01-28 17:15 UTC)

<p>The issue seems to be unique to Intel graphics. I pushed <a href="https://github.com/BrownBiomechanics/SlicerAutoscoperM/pull/193" rel="noopener nofollow ugc">a fix</a> yesterday that ought to resolve it. Please update the AutoscoperM extension and test again. If you encounter further issues, please provide logs (accessible via “Help” &gt; “Report a Bug” in the toolbar).</p>

---

## Post #9 by @Janae (2026-01-30 19:43 UTC)

<p>Hello,</p>
<p>I was able to update the Autoscoper extension, but do not have the option to launch it. Below is the log. Thanks!</p>
<p>[DEBUG][Qt] 30.01.2026 12:37:43 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Session start time …: 20260130_123743<br>
[DEBUG][Qt] 30.01.2026 12:37:43 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Slicer version …: 5.10.0 (revision 34045 / a2b6d08) win-amd64 - installed release<br>
[DEBUG][Qt] 30.01.2026 12:37:43 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Operating system …: Windows /  Professional / (Build 26100, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 30.01.2026 12:37:43 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Memory …: 15817 MB physical, 30665 MB virtual<br>
[DEBUG][Qt] 30.01.2026 12:37:43 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - CPU …: GenuineIntel , 14 cores, 14 logical processors<br>
[DEBUG][Qt] 30.01.2026 12:37:43 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 30.01.2026 12:37:43 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (core profile)<br>
[DEBUG][Qt] 30.01.2026 12:37:43 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - DCMTK configuration …: version 3.6.8, no SSL<br>
[DEBUG][Qt] 30.01.2026 12:37:43 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Internationalization …: disabled, language=<br>
[DEBUG][Qt] 30.01.2026 12:37:43 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Developer mode …: disabled<br>
[DEBUG][Qt] 30.01.2026 12:37:43 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Application path …: C:/Users/janae.ruzicki1/AppData/Local/slicer.org/3D Slicer 5.10.0/bin<br>
[DEBUG][Qt] 30.01.2026 12:37:43 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Additional module paths ..: <a href="http://slicer.org/Extensions-34045/SurfaceWrapSolidify/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/SurfaceWrapSolidify/lib/Slicer-5.10/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34045/Sandbox/lib/Slicer-5.10/qt-loadable-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/Sandbox/lib/Slicer-5.10/qt-loadable-modules</a>, <a href="http://slicer.org/Extensions-34045/Sandbox/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/Sandbox/lib/Slicer-5.10/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34045/SegmentEditorExtraEffects/lib/Slicer-5.10/qt-loadable-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/SegmentEditorExtraEffects/lib/Slicer-5.10/qt-loadable-modules</a>, <a href="http://slicer.org/Extensions-34045/SegmentEditorExtraEffects/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/SegmentEditorExtraEffects/lib/Slicer-5.10/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34045/MarkupsToModel/lib/Slicer-5.10/qt-loadable-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/MarkupsToModel/lib/Slicer-5.10/qt-loadable-modules</a>, <a href="http://slicer.org/Extensions-34045/SlicerAutoscoperM/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/SlicerAutoscoperM/lib/Slicer-5.10/qt-scripted-modules</a><br>
[INFO][Stream] 30.01.2026 12:37:49 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -<br>
[CRITICAL][Stream] 30.01.2026 12:37:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 30.01.2026 12:37:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -   File “”, line 1, in<br>
[CRITICAL][Stream] 30.01.2026 12:37:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -   File “”, line 999, in exec_module<br>
[CRITICAL][Stream] 30.01.2026 12:37:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -   File “”, line 488, in _call_with_frames_removed<br>
[CRITICAL][Stream] 30.01.2026 12:37:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -   File “C:/Users/janae.ruzicki1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/SlicerAutoscoperM/lib/Slicer-5.10/qt-scripted-modules/AutoscoperM.py”, line 23, in<br>
[CRITICAL][Stream] 30.01.2026 12:37:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -     from AutoscoperMLib import IO, SubVolumeExtraction, Validation<br>
[CRITICAL][Stream] 30.01.2026 12:37:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - ModuleNotFoundError: No module named ‘AutoscoperMLib’<br>
[CRITICAL][Qt] 30.01.2026 12:37:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - loadSourceAsModule - Failed to load file “C:/Users/janae.ruzicki1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/SlicerAutoscoperM/lib/Slicer-5.10/qt-scripted-modules/AutoscoperM.py”  as module “AutoscoperM” !<br>
[CRITICAL][Qt] 30.01.2026 12:37:57 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Fail to instantiate module  “AutoscoperM”<br>
[CRITICAL][Stream] 30.01.2026 12:38:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 30.01.2026 12:38:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -   File “”, line 1, in<br>
[CRITICAL][Stream] 30.01.2026 12:38:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -   File “”, line 999, in exec_module<br>
[CRITICAL][Stream] 30.01.2026 12:38:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -   File “”, line 488, in _call_with_frames_removed<br>
[CRITICAL][Stream] 30.01.2026 12:38:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -   File “C:/Users/janae.ruzicki1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/SlicerAutoscoperM/lib/Slicer-5.10/qt-scripted-modules/Hierarchical3DRegistration.py”, line 17, in<br>
[CRITICAL][Stream] 30.01.2026 12:38:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -     from AutoscoperM import AutoscoperMLogic<br>
[CRITICAL][Stream] 30.01.2026 12:38:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - ImportError: cannot import name ‘AutoscoperMLogic’ from ‘AutoscoperM’ (C:/Users/janae.ruzicki1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/SlicerAutoscoperM/lib/Slicer-5.10/qt-scripted-modules/AutoscoperM.py)<br>
[CRITICAL][Qt] 30.01.2026 12:38:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - loadSourceAsModule - Failed to load file “C:/Users/janae.ruzicki1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/SlicerAutoscoperM/lib/Slicer-5.10/qt-scripted-modules/Hierarchical3DRegistration.py”  as module “Hierarchical3DRegistration” !<br>
[CRITICAL][Qt] 30.01.2026 12:38:00 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Fail to instantiate module  “Hierarchical3DRegistration”<br>
[CRITICAL][Qt] 30.01.2026 12:38:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - The following modules failed to be instantiated:<br>
[CRITICAL][Qt] 30.01.2026 12:38:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -    AutoscoperM<br>
[CRITICAL][Qt] 30.01.2026 12:38:02 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -    Hierarchical3DRegistration<br>
[DEBUG][Python] 30.01.2026 12:38:04 [Python] (C:\Users\janae.ruzicki1\AppData\Local\slicer.org\3D Slicer 5.10.0\lib\Slicer-5.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 30.01.2026 12:38:04 [Python] (C:\Users\janae.ruzicki1\AppData\Local\slicer.org\3D Slicer 5.10.0\lib\Slicer-5.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 30.01.2026 12:38:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[WARNING][Qt] 30.01.2026 12:39:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - An OpenGL Core Profile was requested, but it is not supported on the current platform. Falling back to a non-Core profile. Note that this might cause rendering issues.<br>
[WARNING][Qt] 30.01.2026 12:39:05 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Property ‘verbose’’ of object ‘qSlicerWebPythonProxy’ has no notify signal and is not constant, value updates in HTML will be broken!<br>
[WARNING][Qt] 30.01.2026 12:39:06 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Property ‘verbose’’ of object ‘qSlicerWebPythonProxy’ has no notify signal and is not constant, value updates in HTML will be broken!<br>
[WARNING][Qt] 30.01.2026 12:39:08 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Mixed Content: The page at ‘ <a href="https://extensions.slicer.org/catalog/All/34045/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a> ’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://wiki.slicer.org/slicerWiki/images/f/f6/IntensitySegmenterIcon.png%E2%80%99" rel="noopener nofollow ugc">http://wiki.slicer.org/slicerWiki/images/f/f6/IntensitySegmenterIcon.png’</a>. This content should also be served over HTTPS.<br>
[DEBUG][Qt] 30.01.2026 12:39:13 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Switch to module:  “TrackingEvaluation”<br>
[WARNING][Qt] 30.01.2026 12:39:15 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - A cookie associated with a cross-site resource at <a href="http://www.nitrc.org/" rel="noopener nofollow ugc">http://www.nitrc.org/</a> was set without the <code>SameSite</code> attribute. A future release of Chrome will only deliver cookies with cross-site requests if they are set with <code>SameSite=None</code> and <code>Secure</code>. You can review cookies in developer tools under Application&gt;Storage&gt;Cookies and see more details at <a href="https://www.chromestatus.com/feature/5088147346030592" class="inline-onebox" rel="noopener nofollow ugc">Chrome Platform Status</a> and <a href="https://www.chromestatus.com/feature/5633521622188032" class="inline-onebox" rel="noopener nofollow ugc">Chrome Platform Status</a>.</p>

---

## Post #10 by @allemangd (2026-01-30 19:58 UTC)

<p>Thanks for including the logs! It is very helpful.</p>
<p>That looks to me like something has failed during the extension update. Try opening the extension manager and <em>uninstall</em> SlicerAutoscoperM, then restart Slicer, then <em>install</em> SlicerAutoscoperM, then restart Slicer again.</p>
<p>To help confirm the extension installed correctly, you could navigate to <code>C:/Users/janae.ruzicki1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/SlicerAutoscoperM/lib/Slicer-5.10/qt-scripted-modules/</code> in Windows File Explorer; there should be a directory there called <code>AutoscoperMLib</code> that contains several <code>.py</code> files. If that directory is missing or empty, it indicates the extension has failed to install correctly.</p>

---

## Post #12 by @Janae (2026-01-30 20:39 UTC)

<p>Thanks so much David! Upon reinstalling the Autoscoper extension, I am now able to open and run Autoscoper.</p>

---
