# Slicer Crashes During ALPACA/FastModelAlign

**Topic ID**: 32912
**Date**: 2023-11-20
**URL**: https://discourse.slicer.org/t/slicer-crashes-during-alpaca-fastmodelalign/32912

---

## Post #1 by @AaronHardgrave (2023-11-20 17:06 UTC)

<p>Hello,</p>
<p>I am using ALPACA to landmark vertebrae and there are certain models that will cause Slicer to crash. I have gotten most of my dataset landmarked but these select few are causing me trouble. I am trying to figure out where exactly the error occurs but nothing comes up from the error log files. This same issue occurs when I am using the “FastModelAlign” utility. I have tried decimating/regularizing the model further in the Surface Toolbox module and then trying alignment and that caused Slicer to crash as well. I tried this with Slicer 5.4 and the newest preview version. Does anyone have ideas as to what I should try next?</p>
<p>I can share the models as well if there is a way to do that on this forum. The log file from my crashed session is copy and pasted below.</p>
<pre><code class="lang-auto">[DEBUG][Qt] 20.11.2023 11:41:31 [] (unknown:0) - Session start time .......: 2023-11-20 11:41:31
[DEBUG][Qt] 20.11.2023 11:41:31 [] (unknown:0) - Slicer version ...........: 5.4.0 (revision 31938 / 311cb26) win-amd64 - installed release
[DEBUG][Qt] 20.11.2023 11:41:31 [] (unknown:0) - Operating system .........: Windows /  Professional / (Build 19042, Code Page 65001) - 64-bit
[DEBUG][Qt] 20.11.2023 11:41:31 [] (unknown:0) - Memory ...................: 65158 MB physical, 77066 MB virtual
[DEBUG][Qt] 20.11.2023 11:41:31 [] (unknown:0) - CPU ......................: GenuineIntel , 24 cores, 24 logical processors
[DEBUG][Qt] 20.11.2023 11:41:31 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 20.11.2023 11:41:31 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)
[DEBUG][Qt] 20.11.2023 11:41:31 [] (unknown:0) - Internationalization .....: disabled, language=
[DEBUG][Qt] 20.11.2023 11:41:31 [] (unknown:0) - Developer mode ...........: disabled
[DEBUG][Qt] 20.11.2023 11:41:31 [] (unknown:0) - Application path .........: C:/Users/HARDGRAVE/AppData/Local/slicer.org/Slicer 5.4.0/bin
[DEBUG][Qt] 20.11.2023 11:41:31 [] (unknown:0) - Additional module paths ..: slicer.org/Extensions-31938/SlicerMorph/lib/Slicer-5.4/qt-scripted-modules, slicer.org/Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/qt-loadable-modules, slicer.org/Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/qt-scripted-modules, slicer.org/Extensions-31938/MarkupsToModel/lib/Slicer-5.4/qt-loadable-modules, slicer.org/Extensions-31938/SurfaceWrapSolidify/lib/Slicer-5.4/qt-scripted-modules
[WARNING][Qt] 20.11.2023 11:41:38 [] (unknown:0) - libpng warning: iCCP: profile 'ICC Profile': 'CMYK': invalid ICC profile color space
[WARNING][Qt] 20.11.2023 11:41:38 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[DEBUG][Python] 20.11.2023 11:41:40 [Python] (C:\Users\HARDGRAVE\AppData\Local\slicer.org\Slicer 5.4.0\lib\Slicer-5.4\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 20.11.2023 11:41:40 [Python] (C:\Users\HARDGRAVE\AppData\Local\slicer.org\Slicer 5.4.0\lib\Slicer-5.4\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 20.11.2023 11:41:40 [] (unknown:0) - Switch to module:  "Welcome"
[DEBUG][Python] 20.11.2023 11:41:41 [Python] (C:\Users\HARDGRAVE\AppData\Local\slicer.org\Slicer 5.4.0\lib\Slicer-5.4\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: FormatMarkups
[INFO][Python] 20.11.2023 11:41:41 [Python] (&lt;string&gt;:3) - Adding SlicerMorph Volume Rendering Presets
[DEBUG][Qt] 20.11.2023 11:42:00 [] (unknown:0) - Switch to module:  "FastModelAlign"
[INFO][VTK] 20.11.2023 11:42:30 [vtkMRMLModelStorageNode (000001FB8FF722C0)] (D:\D\S\S-0\Libs\MRML\Core\vtkMRMLModelStorageNode.cxx:414) - ReadDataInternal ((unknown)): File //nas-45-49-84/Aaron/Eastern Newt/Vertebrae Project/Data/Meshes/Sacral Meshes/Sacral_001.ply does not contain coordinate system information. Assuming LPS.
[DEBUG][Qt] 20.11.2023 11:42:30 [] (unknown:0) - "Model" Reader has successfully read the file "//nas-45-49-84/Aaron/Eastern Newt/Vertebrae Project/Data/Meshes/Sacral Meshes/Sacral_001.ply" "[0.36s]"
[INFO][VTK] 20.11.2023 11:42:31 [vtkMRMLModelStorageNode (000001FB90093C30)] (D:\D\S\S-0\Libs\MRML\Core\vtkMRMLModelStorageNode.cxx:414) - ReadDataInternal ((unknown)): File //nas-45-49-84/Aaron/Eastern Newt/Vertebrae Project/Data/Meshes/Sacral Meshes/New folder/Sacral_003.ply does not contain coordinate system information. Assuming LPS.
[DEBUG][Qt] 20.11.2023 11:42:31 [] (unknown:0) - "Model" Reader has successfully read the file "//nas-45-49-84/Aaron/Eastern Newt/Vertebrae Project/Data/Meshes/Sacral Meshes/New folder/Sacral_003.ply" "[0.29s]"
[INFO][Stream] 20.11.2023 11:42:38 [] (unknown:0) - parameters are  {'pointDensity': 1.0, 'normalSearchRadius': 2.0, 'FPFHNeighbors': 100, 'FPFHSearchRadius': 5.0, 'distanceThreshold': 3.0, 'maxRANSAC': 1000000, 'ICPDistanceThreshold': 1.5}
[INFO][Stream] 20.11.2023 11:42:38 [] (unknown:0) - :: Loading point clouds and downsampling
[INFO][Stream] 20.11.2023 11:42:38 [] (unknown:0) - Scale length are   0.005009546085026773 0.00534802755207394
[INFO][Stream] 20.11.2023 11:42:38 [] (unknown:0) - Voxel Size is  9.108265609139587e-05
[INFO][Stream] 20.11.2023 11:42:38 [] (unknown:0) - ------------------------------------------------------------
[INFO][Stream] 20.11.2023 11:42:38 [] (unknown:0) - movingMeshPoints.shape  (5374, 3)
[INFO][Stream] 20.11.2023 11:42:38 [] (unknown:0) - movingMeshPointNormals.shape  (5374, 3)
[INFO][Stream] 20.11.2023 11:42:38 [] (unknown:0) - fixedMeshPoints.shape  (5195, 3)
[INFO][Stream] 20.11.2023 11:42:38 [] (unknown:0) - fixedMeshPointNormals.shape  (5195, 3)
[INFO][Stream] 20.11.2023 11:42:38 [] (unknown:0) - ------------------------------------------------------------
</code></pre>

---

## Post #2 by @muratmaga (2023-11-20 17:14 UTC)

<aside class="quote no-group" data-username="AaronHardgrave" data-post="1" data-topic="32912">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aaronhardgrave/48/67100_2.png" class="avatar"> AaronHardgrave:</div>
<blockquote>
<p>I can share the models as well if there is a way to do that on this forum.</p>
</blockquote>
</aside>
<p>If you can share couple models (one works and one crashes) it will be great. Looking at the log file, I suspect the failing ones are extremely small in size. Reported voxel size is miniscule.</p>

---

## Post #3 by @AaronHardgrave (2023-11-20 17:29 UTC)

<p>Hey Murat,</p>
<p>Here is a link to a <a href="https://etsu365-my.sharepoint.com/:f:/g/personal/hardgrave_etsu_edu/EjhvCPxEgkxPmib3eExomtwBGIkdOJ0eljO6rhF059ljCA?e=q13RNv" rel="noopener nofollow ugc">OneDrive Folder</a> with the different models.</p>
<p>If there is a different way you would like me to share them, please let me know. I use  Sacral_001 as the Source Model. Sacral_007 is the one that works and Sacral_003 causes my Slicer to crash.</p>
<p>Thank you,</p>
<p>Aaron</p>

---

## Post #4 by @muratmaga (2023-11-20 17:55 UTC)

<p>I didn’t test with ALPACA, but with FastModelAlign I can get the crash, but for me it crashes with the any model. And as I suspect that’s due to the size of the models, which are tiny. I don’t think that’s an accurate size. It is reporting the AP length of vertebrate to be 2.5 microns.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a28583528b36d765b4a3c875c3a645ad98db271.jpeg" data-download-href="/uploads/short-url/1rRdaXosOJsodY2hCAsbTSNUHVD.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a28583528b36d765b4a3c875c3a645ad98db271_2_461x500.jpeg" alt="image" data-base62-sha1="1rRdaXosOJsodY2hCAsbTSNUHVD" width="461" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a28583528b36d765b4a3c875c3a645ad98db271_2_461x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a28583528b36d765b4a3c875c3a645ad98db271_2_691x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a28583528b36d765b4a3c875c3a645ad98db271.jpeg 2x" data-dominant-color="A2A26F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">845×916 204 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>We will try to fix this in future, but meanwhile you can create linear transform whose first three diagonal elements are 1000, then put the models under this transform and then harden them. That will linearly scale each model by 1000.<br>
Then running the FastmodelAlign things seems to work. Since the actual size doesn’t seem to be critical to you, give that a try…</p>

---

## Post #5 by @AaronHardgrave (2023-11-20 18:30 UTC)

<p>I definitely agree that the 2.5 microns are too small. I have done my segmenting in Dragonfly and have been exporting .ply models into Slicer for landmarking. The units/values are correct in Dragonfly so I guess something went wrong between exporting/importing between programs.</p>
<p>Thank you for your help!</p>
<p>-Aaron</p>

---

## Post #6 by @muratmaga (2023-11-20 19:52 UTC)

<p>Most 3D model formats do not have explicit units associated with them. Slicer is displaying whatever value is in the coordinates. Perhaps default unit value in Dragonfly is in meters (it is in millimeters in Slicer). if that’s the case, 1000 folds scaling should work.</p>
<p>Is there a reason you prefer to do your segmentation in Dragonfly as opposed to Slicer?</p>

---

## Post #7 by @AaronHardgrave (2023-11-21 14:05 UTC)

<p>Okay great! I will definitely fix the scaling on those that were giving me issues.</p>
<p>There is no real preference for Dragonfly other than I was initially trained using it by others in the lab. Dragonfly feels more “beginner-friendly” but that may just be because I was able to bounce questions off people around me. Although, it would be nice to have the entire workflow in the same software so I will likely switch to Slicer for segmenting in the future.</p>

---
