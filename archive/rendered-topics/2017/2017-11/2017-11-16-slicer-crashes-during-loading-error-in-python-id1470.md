# Slicer crashes during loading, error in Python?

**Topic ID**: 1470
**Date**: 2017-11-16
**URL**: https://discourse.slicer.org/t/slicer-crashes-during-loading-error-in-python/1470

---

## Post #1 by @terajnol (2017-11-16 17:09 UTC)

<p>Hi everyone,<br>
I am a brand new user of Slicer 3D and I first want to tell you I am amazed by this soft! A lots of people did a great job !</p>
<p>I am actually editing a scripted module with Python, and after a minor change, I cannot start 3D Slicer anymore. It is the second time it happens to me and I had to reinstall Slicer last time.<br>
Since Slicer is loading the module I am editing and my previous change in the code did not affect the soft before that, I guess my problem is due to a code mistake (simple error in a loop or something like that). When I execute Slicer, I still see the first small image but then the Slicer windows never appears and nothing loads. Deleting the associated .pyc before to execute Slicer didn’t chnage anything.</p>
<p>I am running Slicer 4.9.0 on Windows 10</p>
<p>Any idea how to fix that ?</p>
<p>Thank you a lot,<br>
Thomas</p>

---

## Post #2 by @cpinter (2017-11-16 17:22 UTC)

<p>Can you please provide a log file? If you can start Slicer you can get it in Help / Report a bug, otherwise it’s in c:\Users[USER]\AppData\Local\Temp\ or …\Temp\Slicer.</p>

---

## Post #3 by @lassoan (2017-11-16 17:26 UTC)

<p>To get a clean slate, you need to remove <code>c:\Users\(YourUserName)\AppData\Roaming\NA-MIC\Slicer.ini</code> file.</p>

---

## Post #4 by @terajnol (2017-11-20 13:09 UTC)

<p>Thank you for your fast answers.</p>
<p>This problem happened to me again this morning. I joined the last log file I could find.<br>
Maybe you can get some info from this screenshot but this log is about the previous session of Slicer. I had some bug in my code so I closed it, made some change on the module and then it was impossible to open Slicer again, like last time.<br>
Slicer cannot get to even create the log file.<br>
Removing the Slicer.ini file in AppDatra/Roaming… didn’t change anything.</p>
<p>Maybe it the way I am working on the module, closing slicer, making some change in the code and the opening Slicer and this for many times ?</p>
<p>Thanks for your help<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4c1b14cc7879a312ae5d1f9010e480698982b57.png" data-download-href="/uploads/short-url/s4AzfRkx4qEPPd4fvS2V52kOO1x.png?dl=1" title="Slicer_26631_20171120_121038" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4c1b14cc7879a312ae5d1f9010e480698982b57_2_690x356.png" alt="Slicer_26631_20171120_121038" data-base62-sha1="s4AzfRkx4qEPPd4fvS2V52kOO1x" width="690" height="356" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4c1b14cc7879a312ae5d1f9010e480698982b57_2_690x356.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4c1b14cc7879a312ae5d1f9010e480698982b57_2_1035x534.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4c1b14cc7879a312ae5d1f9010e480698982b57_2_1380x712.png 2x" data-dominant-color="EFEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_26631_20171120_121038</span><span class="informations">1917×991 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2017-11-20 13:48 UTC)

<p>Could you please copy-paste the text here instead of attaching a screenshot? If the log is too long to be included in the post in full, then upload to dropbox/onedrive/gdrive/pastebin/github-gist and post the link.</p>

---

## Post #6 by @terajnol (2017-11-20 14:02 UTC)

<p>Ok sorry.<br>
Here the begining of the log. But again this is the log from the session before the one that crashed, everything seems to be good on it. I haven’t included the end of the log file, which is about info stream of the module and should not concern my problem since I printed many variables and matrices.</p>
<hr>
<p>[DEBUG][Qt] 20.11.2017 12:10:38 [] (unknown:0) - Session start time …: 2017-11-20 12:10:38<br>
[DEBUG][Qt] 20.11.2017 12:10:38 [] (unknown:0) - Slicer version …: 4.9.0-2017-11-14 (revision 26631) win-amd64 - installed<br>
[DEBUG][Qt] 20.11.2017 12:10:38 [] (unknown:0) - Operating system …: Windows /  Professional /  (Build 9200) - 64-bit<br>
[DEBUG][Qt] 20.11.2017 12:10:38 [] (unknown:0) - Memory …: 16282 MB physical, 18714 MB virtual<br>
[DEBUG][Qt] 20.11.2017 12:10:38 [] (unknown:0) - CPU …: GenuineIntel , 4 cores, 16 logical processors<br>
[DEBUG][Qt] 20.11.2017 12:10:38 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 20.11.2017 12:10:38 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 20.11.2017 12:10:38 [] (unknown:0) - Additional module paths …: C:\Users\Lonjaret_PYTHEAS\Documents\DevInfo\Slicer3D\PedicleScrewSimulator-master\PedicleScrewSimulator<br>
[DEBUG][Python] 20.11.2017 12:10:41 [Python] (C:\Program Files\Slicer 4.9.0-2017-11-14\lib\Python\Lib\site-packages\git\<a href="http://cmd.py:719" rel="nofollow noopener">cmd.py:719</a>) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)<br>
[DEBUG][Python] 20.11.2017 12:10:41 [Python] (C:\Program Files\Slicer 4.9.0-2017-11-14\lib\Python\Lib\site-packages\git\<a href="http://cmd.py:719" rel="nofollow noopener">cmd.py:719</a>) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)<br>
[DEBUG][Python] 20.11.2017 12:10:43 [Python] (C:\Program Files\Slicer 4.9.0-2017-11-14\lib\Slicer-4.9\qt-scripted-modules\SubjectHierarchyPlugins\<a href="http://AbstractScriptedSubjectHierarchyPlugin.py:36" rel="nofollow noopener">AbstractScriptedSubjectHierarchyPlugin.py:36</a>) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 20.11.2017 12:10:44 [Python] (C:\Program Files\Slicer 4.9.0-2017-11-14\lib\Slicer-4.9\qt-scripted-modules\SubjectHierarchyPlugins\<a href="http://AbstractScriptedSubjectHierarchyPlugin.py:36" rel="nofollow noopener">AbstractScriptedSubjectHierarchyPlugin.py:36</a>) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 20.11.2017 12:10:44 [Python] (C:\Program Files\Slicer 4.9.0-2017-11-14\lib\Slicer-4.9\qt-scripted-modules\SubjectHierarchyPlugins\<a href="http://AbstractScriptedSubjectHierarchyPlugin.py:36" rel="nofollow noopener">AbstractScriptedSubjectHierarchyPlugin.py:36</a>) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 20.11.2017 12:10:40 [] (unknown:0) - Number of registered modules: 136<br>
[DEBUG][Qt] 20.11.2017 12:10:41 [] (unknown:0) - Number of instantiated modules: 136<br>
[DEBUG][Qt] 20.11.2017 12:10:44 [] (unknown:0) - Number of loaded modules: 136<br>
[DEBUG][Qt] 20.11.2017 12:10:44 [] (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 20.11.2017 12:10:48 [] (unknown:0) - Switch to module:  “PedicleScrewSimulator”<br>
[WARNING][Qt] 20.11.2017 12:10:48 [] (unknown:0) - addTransition - Cannot create a transition that matches a previously created transition<br>
[WARNING][Qt] 20.11.2017 12:10:48 [] (unknown:0) - addTransition - Cannot create a transition that matches a previously created transition<br>
[WARNING][Qt] 20.11.2017 12:10:48 [] (unknown:0) - addTransition - Cannot create a transition that matches a previously created transition<br>
[INFO][Stream] 20.11.2017 12:10:48 [] (unknown:0) - currentStep in parameter node is empty!<br>
[INFO][Stream] 20.11.2017 12:10:48 [] (unknown:0) - -&gt; onEntry - current [LoadData] - comingFrom [None]<br>
[INFO][Stream] 20.11.2017 12:10:51 [] (unknown:0) - <b>File already exists in cache - reusing it.</b><br>
[INFO][Stream] 20.11.2017 12:10:51 [] (unknown:0) - <b>Requesting load</b> <i>CTChest</i> from C:/Users/LONJAR~1/AppData/Local/Temp/Slicer/RemoteIO/CT-chest.nrrd…<br>
[INFO][Stream] 20.11.2017 12:10:51 [] (unknown:0) -<br>
[INFO][VTK] 20.11.2017 12:10:51 [vtkMRMLVolumeArchetypeStorageNode (0000022C6878F070)] (D:\D\N\Slicer-1\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: C:/Users/LONJAR~1/AppData/Local/Temp/Slicer/RemoteIO/CT-chest.nrrd. Dimensions: 512x512x139. Number of components: 1. Pixel type: int.<br>
[DEBUG][Qt] 20.11.2017 12:10:51 [] (unknown:0) - “Volume” Reader has successfully read the file “C:/Users/LONJAR~1/AppData/Local/Temp/Slicer/RemoteIO/CT-chest.nrrd” “[0.87s]”<br>
[INFO][Stream] 20.11.2017 12:10:51 [] (unknown:0) - <b>Load finished</b><br>
[INFO][Stream] 20.11.2017 12:10:51 [] (unknown:0) -<br>
[INFO][Stream] 20.11.2017 12:10:52 [] (unknown:0) - [-389.6192625761033, 0.38085949420928966, -389.6192625761033, 0.38085949420928966, -1.25, 346.25]<br>
[INFO][Stream] 20.11.2017 12:10:52 [] (unknown:0) - Done<br>
[INFO][Stream] 20.11.2017 12:10:52 [] (unknown:0) - -&gt; onExit - current [LoadData] - goingTo [DefineROI]<br>
[INFO][Stream] 20.11.2017 12:10:52 [] (unknown:0) - -&gt; onEntry - current [DefineROI] - comingFrom [LoadData]<br>
[WARNING][VTK] 20.11.2017 12:10:53 [vtkMRMLLinearTransformNode (0000022C66F676E0)] (D:\D\N\Slicer-1\Libs\MRML\Core\vtkMRMLTransformNode.cxx:1515) - vtkMRMLTransformNode::SetAndObserveMatrixTransformToParent method is deprecated. Use vtkMRMLTransformNode::SetMatrixTransformToParent instead<br>
[INFO][Stream] 20.11.2017 12:10:53 [] (unknown:0) - PedicleScrewSimulator VR: will observe ID vtkMRMLScalarVolumeNode1<br>
[WARNING][VTK] 20.11.2017 12:10:53 [vtkObserverManager (0000022C6C7AA4F0)] (D:\D\N\Slicer-1\Libs\MRML\Core\vtkObserverManager.cxx:131) - The same object is already observed with the same priority. The observation is kept as is.<br>
[WARNING][VTK] 20.11.2017 12:10:53 [vtkObserverManager (0000022C6C7AA4F0)] (D:\D\N\Slicer-1\Libs\MRML\Core\vtkObserverManager.cxx:131) - The same object is already observed with the same priority. The observation is kept as is.<br>
[INFO][Stream] 20.11.2017 12:10:53 [] (unknown:0) - [0, 0, 0]<br>
[WARNING][VTK] 20.11.2017 12:10:53 [vtkObserverManager (0000022C6C7AA4F0)] (D:\D\N\Slicer-1\Libs\MRML\Core\vtkObserverManager.cxx:131) - The same object is already observed with the same priority. The observation is kept as is.<br>
[DEBUG][Qt] 20.11.2017 12:10:59 [] (unknown:0) - Found CommandLine Module, target is  C:/Program Files/Slicer 4.9.0-2017-11-14/lib/Slicer-4.9/cli-modules/ResampleScalarVectorDWIVolume.exe<br>
[DEBUG][Qt] 20.11.2017 12:10:59 [] (unknown:0) - ModuleType: CommandLineModule<br>
[DEBUG][Qt] 20.11.2017 12:11:00 [] (unknown:0) - Resample Scalar/Vector/DWI Volume command line:</p>
<p>C:/Program Files/Slicer 4.9.0-2017-11-14/lib/Slicer-4.9/cli-modules/ResampleScalarVectorDWIVolume.exe --hfieldtype h-Field --interpolation linear --transform_order output-to-input --image_center input --spacing 0.38085949420929,0.38085949420929,0.38085949420929 --size 52,52,52 --origin 9.71192,9.71192,-9.71192 --direction_matrix -1,0,0,0,-1,0,0,0,1 --number_of_thread 0 --default_pixel_value 0 --window_function c --spline_order 3 --transform_matrix 1,0,0,0,1,0,0,0,1,0,0,0 --transform a C:/Users/LONJAR~1/AppData/Local/Temp/Slicer/FFFG_vtkMRMLScalarVolumeNodeB.nrrd C:/Users/LONJAR~1/AppData/Local/Temp/Slicer/FFFG_vtkMRMLScalarVolumeNodeC.nrrd<br>
[DEBUG][Qt] 20.11.2017 12:11:01 [] (unknown:0) - Resample Scalar/Vector/DWI Volume completed without errors<br>
[WARNING][VTK] 20.11.2017 12:11:01 [vtkSlicerCLIModuleLogic (0000022C67048380)] (D:\D\N\Slicer-1\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:2556) - Unable to delete temporary file C:/Users/LONJAR~1/AppData/Local/Temp/Slicer/FFFG_vtkMRMLScalarVolumeNodeB.nrrd<br>
[INFO][VTK] 20.11.2017 12:11:01 [vtkMRMLVolumeArchetypeStorageNode (0000022C6C68A7F0)] (D:\D\N\Slicer-1\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: C:/Users/LONJAR~1/AppData/Local/Temp/Slicer/FFFG_vtkMRMLScalarVolumeNodeC.nrrd. Dimensions: 52x52x52. Number of components: 1. Pixel type: int.<br>
[INFO][Stream] 20.11.2017 12:11:01 [] (unknown:0) - -&gt; onExit - current [DefineROI] - goingTo [Landmarks]</p>

---

## Post #7 by @lassoan (2017-11-20 15:04 UTC)

<aside class="quote no-group" data-username="terajnol" data-post="6" data-topic="1470">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/eb8c5e/48.png" class="avatar"> terajnol:</div>
<blockquote>
<p>But again this is the log from the session before the one that crashed,</p>
</blockquote>
</aside>
<p>Log should be available for all sessions, even when there is a crash. Can you find that log? Does Slicer always fail to start up or just sometimes, randomly?</p>

---

## Post #8 by @terajnol (2017-11-20 15:17 UTC)

<p>No way to find this log, at least in the folder c:\Users[USER]\AppData\Local\Temp\Slicer.<br>
I understand that logs should be available for all sessions but apparently, in my case, Slicer crashed just before to create the log file. In total, since last week, Slicer Failed to start up 3 times but it is difficult to say if it was random or not. I was intensively closing and opening it for my development, that’s it.<br>
Each time, it worked perfectly after reinstallation. Just to know, these reinstallation were just made from the windows configuration Panel, so a lot of files (like the logs…) were still in my hard drive.<br>
If there is a logic in these failures, Slicer should not be able to start at some point tomorrow. If it is the case I will again double-check the logs and let you know if I find anything.<br>
I really don’t understand this problem since I was doing nothing unusual before each failure…</p>

---

## Post #9 by @terajnol (2017-11-20 16:01 UTC)

<p>Ok so again Slicer failed to start up 5 min ago.<br>
If it is not random, it is faster and faster to fail. But maybe it is random.</p>
<p>Again, there is no log file for this session… And the previous log file doe not show any weird behaviour.<br>
When I closes Slicer during the previous session, no error was indicated. I don’t think my modification on a module are affecting this, since the modules are loaded at the end, then after the time when my Slicer fail. And when all is working, code errors are well indicated in the python console, as expected.</p>
<p>Any clue on what could be the problem ? Do I do something wrong with my development (opening and closing the soft multiple times?)</p>

---

## Post #10 by @lassoan (2017-11-20 16:07 UTC)

<p>Please follow these instructions for troubleshooting application startup problems:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Troubleshooting#Debugging_Slicer_application_startup_issues" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Troubleshooting#Debugging_Slicer_application_startup_issues</a></p>

---

## Post #11 by @terajnol (2017-12-04 10:54 UTC)

<p>Thank you for your answers Andreas.<br>
I followed the first steps of troubleshooting instructions without success but then I figured out that my bug does not appear anymore with the newest release of the Nighty build.</p>
<p>I just have sometimes a slow starting time when I launch Slicer, but nothing problematic.<br>
Of course, I shall follow the previous instructions if I ever found another problem.</p>
<p>Thank you anyway,</p>

---

## Post #12 by @Ramya_C (2019-12-28 22:18 UTC)

<p>anyone facing the issues that the Slicer crashes when trying to load or undo any operations ?<br>
I am using slicer 4.8.1 and windows 10 OS for the segmentation .</p>
<p>Is there any issues with the graphics card ? Not sure if this is related</p>

---

## Post #13 by @lassoan (2019-12-29 01:51 UTC)

<p>The only known reason Slicer would crash is when it runs out of memory (like all other applications). You can reduce the image size by cropping and/or resampling using Crop volume module. You may also upgrade to a recent Slicer Preview release, which contains several memory usage optimizations.</p>

---

## Post #15 by @Ramya_C (2019-12-29 04:29 UTC)

<p>May I know how to resample sing crop volume module ?</p>
<p>Thanks</p>

---

## Post #16 by @lassoan (2019-12-29 15:24 UTC)

<p>See documentation here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Crop_Volume">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Crop_Volume</a></p>

---

## Post #17 by @thenineteen (2020-07-03 22:13 UTC)

<p>Reproducible:</p>
<ol>
<li>start 3D slicer without external monitor. works</li>
<li>connect external monitor and move the 3D slicer app to the external monitor (extended screens)</li>
<li>close 3D slicer app.</li>
<li>Now, when restarting 3D slicer app, it will attempt to open it in the external monitor. It will fail 100%</li>
</ol>
<p>Windows 10<br>
3D Slicer 4.11.0-2020-05-12 r29055 / 829bbe1</p>
<p>“Not Responding”</p>

---

## Post #18 by @thenineteen (2020-07-03 22:16 UTC)

<p>[DEBUG][Qt] 03.07.2020 23:04:21 [] (unknown:0) - Session start time …: 2020-07-03 23:04:21<br>
[DEBUG][Qt] 03.07.2020 23:04:21 [] (unknown:0) - Slicer version …: 4.11.0-2020-05-12 (revision 29055 / 829bbe1) win-amd64 - installed release<br>
[DEBUG][Qt] 03.07.2020 23:04:21 [] (unknown:0) - Operating system …: Windows /  Personal / (Build 18362, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 03.07.2020 23:04:21 [] (unknown:0) - Memory …: 32611 MB physical, 37475 MB virtual<br>
[DEBUG][Qt] 03.07.2020 23:04:21 [] (unknown:0) - CPU …: GenuineIntel , 12 cores, 12 logical processors<br>
[DEBUG][Qt] 03.07.2020 23:04:21 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 03.07.2020 23:04:21 [] (unknown:0) - Qt configuration …: version 5.10.1, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 03.07.2020 23:04:21 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 03.07.2020 23:04:21 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 03.07.2020 23:04:21 [] (unknown:0) - Application path …: C:/Users/ali_m/AppData/Local/NA-MIC/Slicer 4.11.0-2020-05-12/bin<br>
[DEBUG][Qt] 03.07.2020 23:04:21 [] (unknown:0) - Additional module paths …: C:/Users/ali_m/AnacondaProjects/PhD/Semiology-Visualisation-Tool/slicer<br>
[DEBUG][Python] 03.07.2020 23:04:22 [Python] (C:\Users\ali_m\AppData\Local\NA-MIC\Slicer 4.11.0-2020-05-12\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 03.07.2020 23:04:23 [Python] (C:\Users\ali_m\AppData\Local\NA-MIC\Slicer 4.11.0-2020-05-12\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 03.07.2020 23:04:23 [Python] (C:\Users\ali_m\AppData\Local\NA-MIC\Slicer 4.11.0-2020-05-12\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 03.07.2020 23:04:23 [] (unknown:0) - Switch to module:  “Welcome”</p>

---

## Post #19 by @lassoan (2020-07-04 03:30 UTC)

<p>Thanks for reporting this. Could you upload your <code>Slicer.ini</code> and <code>Slicer-(revisionnumber).ini</code> files and post the link here so that we can reproduce the issue?</p>

---
