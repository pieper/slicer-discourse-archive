# Data save error: failed to save scene

**Topic ID**: 34409
**Date**: 2024-02-19
**URL**: https://discourse.slicer.org/t/data-save-error-failed-to-save-scene/34409

---

## Post #1 by @Gonzo009 (2024-02-19 20:32 UTC)

<p>hi, i am new to 3dslicer, but i have a very basic error all the time.<br>
after loading a .nrrd file, data are accepted and shown in all planes and 3d.<br>
Any saving of these data, with or without a scene, causes all the times “error saving failed”</p>
<p>see<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90182c1db52ab06c948b0236b04d3a014c9cdeb6.png" alt="grafik" data-base62-sha1="kyIxLTQ04vOgYGDuqr9TlzSYVkq" width="500" height="375"></p>

---

## Post #2 by @pieper (2024-02-19 21:24 UTC)

<p>A place to start would be to confirm that the save data directory exists and that you can write into it.</p>

---

## Post #3 by @Gonzo009 (2024-02-20 10:05 UTC)

<p>thanks for the basic reminder.<br>
All these directories exist.<br>
It does not matter, if i choose a different directory. same error.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2e26ccf67225e87298f101b1023a225b18b5a18.png" data-download-href="/uploads/short-url/rO1K2QOECM7VDJyna2HKOfP3uRi.png?dl=1" title="" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2e26ccf67225e87298f101b1023a225b18b5a18_2_690x321.png" data-base62-sha1="rO1K2QOECM7VDJyna2HKOfP3uRi" alt="" width="690" height="321" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2e26ccf67225e87298f101b1023a225b18b5a18_2_690x321.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2e26ccf67225e87298f101b1023a225b18b5a18.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2e26ccf67225e87298f101b1023a225b18b5a18.png 2x" data-dominant-color="CFCED1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename"></span><span class="informations">1014×472 78.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @pieper (2024-02-20 18:56 UTC)

<p>Hmm, does this happen if you try to save data loaded from the SampleData module or just with your data?</p>

---

## Post #5 by @lassoan (2024-02-20 19:41 UTC)

<p>The error in the screenshot (saving of the scene .mrml file failed) does not match the error in the log (saving of a markup ROI failed). Please post the log messages corresponding to the screenshot.</p>

---

## Post #6 by @Gonzo009 (2024-02-21 20:24 UTC)

<p>I tried to save a sample data set: same error meassge</p>
<p>see below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e31573e85419b3f578a7a664f0c8b5bf674e75eb.png" data-download-href="/uploads/short-url/woSlAcgIMgyW9sbF5GNmrJ4wqSf.png?dl=1" title="" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e31573e85419b3f578a7a664f0c8b5bf674e75eb_2_690x216.png" data-base62-sha1="woSlAcgIMgyW9sbF5GNmrJ4wqSf" alt="" width="690" height="216" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e31573e85419b3f578a7a664f0c8b5bf674e75eb_2_690x216.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e31573e85419b3f578a7a664f0c8b5bf674e75eb_2_1035x324.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e31573e85419b3f578a7a664f0c8b5bf674e75eb_2_1380x432.png 2x" data-dominant-color="CCCCD3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename"></span><span class="informations">1532×480 73.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<pre><code class="lang-auto">[DEBUG][Qt] 21.02.2024 21:19:05 [] (unknown:0) - Session start time .......: 2024-02-21 21:19:05
[DEBUG][Qt] 21.02.2024 21:19:05 [] (unknown:0) - Slicer version ...........: 5.6.0 (revision 32390 / 0a13b9c) win-amd64 - installed release
[DEBUG][Qt] 21.02.2024 21:19:05 [] (unknown:0) - Operating system .........: Windows / Professional / (Build 19045, Code Page 65001) - 64-bit
[DEBUG][Qt] 21.02.2024 21:19:05 [] (unknown:0) - Memory ...................: 4073 MB physical, 8964 MB virtual
[DEBUG][Qt] 21.02.2024 21:19:05 [] (unknown:0) - CPU ......................: GenuineIntel , 4 cores, 4 logical processors
[DEBUG][Qt] 21.02.2024 21:19:05 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 21.02.2024 21:19:05 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)
[DEBUG][Qt] 21.02.2024 21:19:05 [] (unknown:0) - Internationalization .....: disabled, language=
[DEBUG][Qt] 21.02.2024 21:19:05 [] (unknown:0) - Developer mode ...........: disabled
[DEBUG][Qt] 21.02.2024 21:19:05 [] (unknown:0) - Application path .........: C:/Users/gonzo11/AppData/Local/slicer.org/Slicer 5.6.0/bin
[DEBUG][Qt] 21.02.2024 21:19:05 [] (unknown:0) - Additional module paths ..: (none)
[DEBUG][Python] 21.02.2024 21:19:11 [Python] (C:\Users\gonzo11\AppData\Local\slicer.org\Slicer 5.6.0\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 21.02.2024 21:19:11 [Python] (C:\Users\gonzo11\AppData\Local\slicer.org\Slicer 5.6.0\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 21.02.2024 21:19:11 [] (unknown:0) - Switch to module: "Welcome"
[DEBUG][Qt] 21.02.2024 21:19:38 [] (unknown:0) - Switch to module: "SampleData"
[DEBUG][Python] 21.02.2024 21:19:40 [Python] (C:/Users/gonzo11/AppData/Local/slicer.org/Slicer 5.6.0/bin/../lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - Requesting download RegLib_C01_2.nrrd from [https://github.com/Slicer/SlicerTestingData/releases/download/SHA256/1a64f3f422eb3d1c9b093d1a18da354b13bcf307907c66317e2463ee530b7a97](https://github.com/Slicer/SlicerTestingData/releases/download/SHA256/1a64f3f422eb3d1c9b093d1a18da354b13bcf307907c66317e2463ee530b7a97) ...
[DEBUG][Python] 21.02.2024 21:19:41 [Python] (C:/Users/gonzo11/AppData/Local/slicer.org/Slicer 5.6.0/bin/../lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - Downloaded 600.0 KB (10% of 5.8 MB)...
[DEBUG][Python] 21.02.2024 21:19:41 [Python] (C:/Users/gonzo11/AppData/Local/slicer.org/Slicer 5.6.0/bin/../lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - Downloaded 1.2 MB (20% of 5.8 MB)...
[DEBUG][Python] 21.02.2024 21:19:41 [Python] (C:/Users/gonzo11/AppData/Local/slicer.org/Slicer 5.6.0/bin/../lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - Downloaded 1.8 MB (30% of 5.8 MB)...
[DEBUG][Python] 21.02.2024 21:19:41 [Python] (C:/Users/gonzo11/AppData/Local/slicer.org/Slicer 5.6.0/bin/../lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - Downloaded 2.3 MB (40% of 5.8 MB)...
[DEBUG][Python] 21.02.2024 21:19:41 [Python] (C:/Users/gonzo11/AppData/Local/slicer.org/Slicer 5.6.0/bin/../lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - Downloaded 2.9 MB (50% of 5.8 MB)...
[DEBUG][Python] 21.02.2024 21:19:41 [Python] (C:/Users/gonzo11/AppData/Local/slicer.org/Slicer 5.6.0/bin/../lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - Downloaded 3.5 MB (60% of 5.8 MB)...
[DEBUG][Python] 21.02.2024 21:19:41 [Python] (C:/Users/gonzo11/AppData/Local/slicer.org/Slicer 5.6.0/bin/../lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - Downloaded 4.1 MB (70% of 5.8 MB)...
[DEBUG][Python] 21.02.2024 21:19:41 [Python] (C:/Users/gonzo11/AppData/Local/slicer.org/Slicer 5.6.0/bin/../lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - Downloaded 4.7 MB (80% of 5.8 MB)...
[DEBUG][Python] 21.02.2024 21:19:41 [Python] (C:/Users/gonzo11/AppData/Local/slicer.org/Slicer 5.6.0/bin/../lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - Downloaded 5.3 MB (90% of 5.8 MB)...
[DEBUG][Python] 21.02.2024 21:19:41 [Python] (C:/Users/gonzo11/AppData/Local/slicer.org/Slicer 5.6.0/bin/../lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - Downloaded 5.8 MB (100% of 5.8 MB)...
[DEBUG][Python] 21.02.2024 21:19:41 [Python] (C:/Users/gonzo11/AppData/Local/slicer.org/Slicer 5.6.0/bin/../lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - Download finished
[DEBUG][Python] 21.02.2024 21:19:41 [Python] (C:/Users/gonzo11/AppData/Local/slicer.org/Slicer 5.6.0/bin/../lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - Verifying checksum
[DEBUG][Python] 21.02.2024 21:19:41 [Python] (C:/Users/gonzo11/AppData/Local/slicer.org/Slicer 5.6.0/bin/../lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - Checksum OK
[DEBUG][Python] 21.02.2024 21:19:41 [Python] (C:/Users/gonzo11/AppData/Local/slicer.org/Slicer 5.6.0/bin/../lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - Requesting load MRBrainTumor2 from C:/Users/gonzo11/AppData/Local/slicer.org/Slicer/cache/SlicerIO/RegLib_C01_2.nrrd ...
[DEBUG][Qt] 21.02.2024 21:19:41 [] (unknown:0) - "Volume" Reader has successfully read the file "C:/Users/gonzo11/AppData/Local/slicer.org/Slicer/cache/SlicerIO/RegLib_C01_2.nrrd" "[0.19s]"
[DEBUG][Python] 21.02.2024 21:19:42 [Python] (C:/Users/gonzo11/AppData/Local/slicer.org/Slicer 5.6.0/bin/../lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - Load finished
[ERROR][VTK] 21.02.2024 21:20:15 [vtkMRMLVolumeArchetypeStorageNode (0000019697EF14C0)] (vtkMRMLVolumeArchetypeStorageNode.cxx:821) - vtkMRMLVolumeArchetypeStorageNode::UpdateFileList: Failed to create directory C:/Users/gonzo11/Documents/3Ddata_dir/TempWriteMRBrainTumor2
[CRITICAL][Stream] 21.02.2024 21:20:15 [] (unknown:0) -
[CRITICAL][Stream] 21.02.2024 21:20:15 [] (unknown:0) - itk::ExceptionObject (00000003790F4478)
[CRITICAL][Stream] 21.02.2024 21:20:15 [] (unknown:0) - Location: "unknown"
[CRITICAL][Stream] 21.02.2024 21:20:15 [] (unknown:0) - File: D:\D\S\S-0-build\ITK\Modules\IO\NRRD\src\itkNrrdImageIO.cxx
[CRITICAL][Stream] 21.02.2024 21:20:15 [] (unknown:0) - Line: 1118
[CRITICAL][Stream] 21.02.2024 21:20:15 [] (unknown:0) - Description: ITK ERROR: NrrdImageIO(000001969BE8BAB0): Write: Error writing C:/Users/gonzo11/Documents/3Ddata_dir/MRBrainTumor2.nrrd:
[CRITICAL][Stream] 21.02.2024 21:20:15 [] (unknown:0) - [nrrd] nrrdSave: couldn't fopen("C:/Users/gonzo11/Documents/3Ddata_dir/MRBrainTumor2.nrrd","wb"): No such file or directory
[CRITICAL][Stream] 21.02.2024 21:20:15 [] (unknown:0) -
[CRITICAL][Stream] 21.02.2024 21:20:15 [] (unknown:0) -
[CRITICAL][Qt] 21.02.2024 21:20:15 [] (unknown:0) - bool __cdecl qSlicerCoreIOManager::saveNodes(class QString,const class QMap&lt;class QString,class QVariant&gt; &amp;,class vtkMRMLMessageCollection *,class vtkMRMLScene *) error: Saving failed with all writers found for file "C:/Users/gonzo11/Documents/3Ddata_dir/MRBrainTumor2.nrrd" of type "VolumeFile"
[CRITICAL][Qt] 21.02.2024 21:20:15 [] (unknown:0) - void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save error: "- Error: Failed to create directory C:/Users/gonzo11/Documents/3Ddata_dir/TempWriteMRBrainTumor2\n- Error: Cannot write data file: C:/Users/gonzo11/Documents/3Ddata_dir/MRBrainTumor2.nrrd.\n"
[ERROR][VTK] 21.02.2024 21:20:15 [vtkPNGWriter (00000196840FF520)] (vtkPNGWriter.cxx:258) - Unable to open file C:/Users/gonzo11/Documents/3Ddata_dir/2024-02-21-Scene.png
[ERROR][VTK] 21.02.2024 21:20:15 [vtkPNGWriter (00000196840FF520)] (vtkImageWriter.cxx:482) - Ran out of disk space; deleting file(s) already written
[ERROR][VTK] 21.02.2024 21:20:15 [vtkMRMLScene (000001968426D310)] (vtkMRMLScene.cxx:1079) - vtkMRMLScene::Commit: Scene writing failed: Could not open file C:/Users/gonzo11/Documents/3Ddata_dir/2024-02-21-Scene.mrml
[CRITICAL][Qt] 21.02.2024 21:20:15 [] (unknown:0) - bool __cdecl qSlicerCoreIOManager::saveNodes(class QString,const class QMap&lt;class QString,class QVariant&gt; &amp;,class vtkMRMLMessageCollection *,class vtkMRMLScene *) error: Saving failed with all writers found for file "C:/Users/gonzo11/Documents/3Ddata_dir/2024-02-21-Scene.mrml" of type "SceneFile"
[CRITICAL][Qt] 21.02.2024 21:20:15 [] (unknown:0) - void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save error: "- Error: Failed to save scene as C:/Users/gonzo11/Documents/3Ddata_dir/2024-02-21-Scene.mrml\n- Error: Saving failed with all writers found for file 'C:/Users/gonzo11/Documents/3Ddata_dir/2024-02-21-Scene.mrml' of type 'SceneFile'.\n"
</code></pre>

---

## Post #7 by @lassoan (2024-02-21 20:29 UTC)

<aside class="quote no-group" data-username="Gonzo009" data-post="6" data-topic="34409">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/6f9a4e/48.png" class="avatar"> Gonzo009:</div>
<blockquote>
<p><code>Ran out of disk space; deleting file(s) already written</code></p>
</blockquote>
</aside>
<p>You have ran out of disk space (or don’t have write access) in that location.</p>
<p>Also, it seems that you are not using the latest stable version of Slicer. Please upgrade to Slicer-5.6.1 as it may include fixes that you need.</p>

---

## Post #8 by @Gonzo009 (2024-02-22 08:34 UTC)

<p>i checked disk space, checked directories write access permission in windows10, all seems ok.<br>
I updated to v 5.6.1.</p>
<p>no success. Same error, trying to save sample data.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/216e29c703c7f718a335c7de17f2695ae7550bdf.png" data-download-href="/uploads/short-url/4LJMmCfmIznodT0o4FXMiCCshXh.png?dl=1" title="grafik" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/216e29c703c7f718a335c7de17f2695ae7550bdf.png" alt="grafik" data-base62-sha1="4LJMmCfmIznodT0o4FXMiCCshXh" width="690" height="462" data-dominant-color="DCE0EA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">grafik</span><span class="informations">940×630 50.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @pieper (2024-02-22 16:05 UTC)

<p>Have you tried a different computer?  There’s clearly something different about what you are trying to do from what works for other people on other machines.  Maybe it’s the computer, the directory, something about your installation, or something else entirely.  I’m not sure we can tell you but you should be able to try experiments and narrow down what’s different for this case.  Please report back what you find in case it can help others in the future.</p>

---
