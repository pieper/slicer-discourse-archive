# Can't export segmentation to binary labelmap in 4.11 Ubuntu 25.05.2020 version

**Topic ID**: 14197
**Date**: 2020-10-22
**URL**: https://discourse.slicer.org/t/cant-export-segmentation-to-binary-labelmap-in-4-11-ubuntu-25-05-2020-version/14197

---

## Post #1 by @l.znaniecki (2020-10-22 04:35 UTC)

<p>Hi,</p>
<p>As in the title, I can’t <strong>export</strong> my segmentation to <strong>binary labelmap</strong> in 4.11 Ubuntu. It works perfectly in Windows &amp; Mac, not in Ubuntu.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44066ed64a7bd090a13de4d870046b4a64baf392.png" data-download-href="/uploads/short-url/9HMfx4e77ARf8sZpovZVMAWBVxU.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44066ed64a7bd090a13de4d870046b4a64baf392_2_690x175.png" alt="2" data-base62-sha1="9HMfx4e77ARf8sZpovZVMAWBVxU" width="690" height="175" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44066ed64a7bd090a13de4d870046b4a64baf392_2_690x175.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44066ed64a7bd090a13de4d870046b4a64baf392_2_1035x262.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44066ed64a7bd090a13de4d870046b4a64baf392.png 2x" data-dominant-color="ADAFAF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1224×312 87.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Please help.<br>
Thanks in advance.</p>
<p>Lukasz</p>

---

## Post #2 by @l.znaniecki (2020-10-22 04:42 UTC)

<p>[DEBUG][Qt] 22.10.2020 06:21:35 [] (unknown:0) - Session start time …: 2020-10-22 06:21:35<br>
[DEBUG][Qt] 22.10.2020 06:21:35 [] (unknown:0) - Slicer version …: 4.11.0-2020-05-25 (revision 29077 / fb87a55) linux-amd64 - installed release<br>
[DEBUG][Qt] 22.10.2020 06:21:35 [] (unknown:0) - Operating system …: Linux / 5.4.0-52-generic / <span class="hashtag">#57-Ubuntu</span> SMP Thu Oct 15 10:57:00 UTC 2020 - 64-bit<br>
[DEBUG][Qt] 22.10.2020 06:21:35 [] (unknown:0) - Memory …: 32121 MB physical, 2047 MB virtual<br>
[DEBUG][Qt] 22.10.2020 06:21:35 [] (unknown:0) - CPU …: AuthenticAMD AMD Ryzen 9 3900X 12-Core Processor, 12 cores, 24 logical processors<br>
[DEBUG][Qt] 22.10.2020 06:21:35 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, Sequential threading<br>
[DEBUG][Qt] 22.10.2020 06:21:35 [] (unknown:0) - Qt configuration …: version 5.11.2, with SSL, requested OpenGL 3.2 (core profile)<br>
[DEBUG][Qt] 22.10.2020 06:21:35 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 22.10.2020 06:21:35 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 22.10.2020 06:21:35 [] (unknown:0) - Application path …: /home/dugi/Dokumenty/Slicer-4.11.0-2020-05-25-linux-amd64/bin<br>
[DEBUG][Qt] 22.10.2020 06:21:35 [] (unknown:0) - Additional module paths …: /home/dugi/.config/NA-MIC/Extensions-29077/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules, /home/dugi/.config/NA-MIC/Extensions-29077/MarkupsToModel/lib/Slicer-4.11/qt-loadable-modules, /home/dugi/.config/NA-MIC/Extensions-29077/VolumeClip/lib/Slicer-4.11/qt-scripted-modules, /home/dugi/.config/NA-MIC/Extensions-29077/SlicerHeart/lib/Slicer-4.11/cli-modules, /home/dugi/.config/NA-MIC/Extensions-29077/SlicerHeart/lib/Slicer-4.11/qt-loadable-modules, /home/dugi/.config/NA-MIC/Extensions-29077/SlicerHeart/lib/Slicer-4.11/qt-scripted-modules, /home/dugi/.config/NA-MIC/Extensions-29077/SlicerIGT/lib/Slicer-4.11/qt-loadable-modules, /home/dugi/.config/NA-MIC/Extensions-29077/SlicerIGT/lib/Slicer-4.11/qt-scripted-modules, /home/dugi/.config/NA-MIC/Extensions-29077/SlicerRT/lib/Slicer-4.11/cli-modules, /home/dugi/.config/NA-MIC/Extensions-29077/SlicerRT/lib/Slicer-4.11/qt-loadable-modules, /home/dugi/.config/NA-MIC/Extensions-29077/SlicerRT/lib/Slicer-4.11/qt-scripted-modules, /home/dugi/.config/NA-MIC/Extensions-29077/SlicerVMTK/lib/Slicer-4.11/qt-loadable-modules, /home/dugi/.config/NA-MIC/Extensions-29077/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules<br>
[CRITICAL][Qt] 22.10.2020 06:21:37 [] (unknown:0) -   Error(s):<br>
CLI executable: /home/dugi/.config/NA-MIC/Extensions-29077/SlicerVMTK/lib/Slicer-4.11/qt-loadable-modules/vtkvmtk.py<br>
The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program.<br>
[CRITICAL][Qt] 22.10.2020 06:21:37 [] (unknown:0) - Fail to instantiate module  “vtkvmtk”<br>
[CRITICAL][Qt] 22.10.2020 06:21:37 [] (unknown:0) - The following modules failed to be instantiated:<br>
[CRITICAL][Qt] 22.10.2020 06:21:37 [] (unknown:0) -    vtkvmtk<br>
[DEBUG][Python] 22.10.2020 06:21:40 [Python] (/home/dugi/Dokumenty/Slicer-4.11.0-2020-05-25-linux-amd64/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 22.10.2020 06:21:42 [Python] (/home/dugi/Dokumenty/Slicer-4.11.0-2020-05-25-linux-amd64/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 22.10.2020 06:21:42 [Python] (/home/dugi/Dokumenty/Slicer-4.11.0-2020-05-25-linux-amd64/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 22.10.2020 06:21:42 [] (unknown:0) - Switch to module:  “Welcome”<br>
[INFO][VTK] 22.10.2020 06:21:43 [vtkMRMLVolumeArchetypeStorageNode (0x6ace820)] (/work/Preview/Slicer-0/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:471) - Loaded volume from file: /home/dugi/.config/NA-MIC/Extensions-29077/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules/Resources/Vesselness.png. Dimensions: 65x50x1. Number of components: 3. Pixel type: unsigned char.<br>
[DEBUG][Qt] 22.10.2020 06:21:46 [] (unknown:0) - Switch to module:  “DICOM”<br>
[ERROR][Python] 22.10.2020 06:21:51 [Python] (/home/dugi/.config/NA-MIC/Extensions-29077/SlicerHeart/lib/Slicer-4.11/qt-scripted-modules/DicomUltrasoundPlugin.py:134) - sopClassUID 1.2.840.10008.5.1.4.1.1.2 != supportedSOPClassUID 1.2.840.10008.5.1.4.1.1.3.1<br>
[CRITICAL][Stream] 22.10.2020 06:21:51 [] (unknown:0) - sopClassUID 1.2.840.10008.5.1.4.1.1.2 != supportedSOPClassUID 1.2.840.10008.5.1.4.1.1.3.1<br>
[DEBUG][Python] 22.10.2020 06:21:51 [Python] (/home/dugi/Dokumenty/Slicer-4.11.0-2020-05-25-linux-amd64/bin/…/lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py:456) - MultiVolumeImportPlugin::examine<br>
[DEBUG][Python] 22.10.2020 06:21:52 [Python] (/home/dugi/Dokumenty/Slicer-4.11.0-2020-05-25-linux-amd64/bin/…/lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py:496) - DICOMMultiVolumePlugin found 1 multivolumes!<br>
[DEBUG][Python] 22.10.2020 06:21:52 [Python] (/home/dugi/Dokumenty/Slicer-4.11.0-2020-05-25-linux-amd64/bin/…/lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py:168) - MultiVolumeImportPlugin:examineMultiseries<br>
[DEBUG][Python] 22.10.2020 06:21:52 [Python] (/home/dugi/Dokumenty/Slicer-4.11.0-2020-05-25-linux-amd64/bin/…/lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py:173) - DICOMMultiVolumePlugin found 0 multivolumes!<br>
[INFO][Python] 22.10.2020 06:21:52 [Python] (/home/dugi/Dokumenty/Slicer-4.11.0-2020-05-25-linux-amd64/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:336) - Loading with imageIOName: GDCM<br>
[INFO][Python] 22.10.2020 06:21:54 [Python] (/home/dugi/Dokumenty/Slicer-4.11.0-2020-05-25-linux-amd64/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:408) - Window/level found in DICOM tags (center=100.0, width=600.0) has been applied to volume 2: Std<br>
[DEBUG][Python] 22.10.2020 06:21:54 [Python] (/home/dugi/Dokumenty/Slicer-4.11.0-2020-05-25-linux-amd64/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:741) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 2.96484e-06 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 22.10.2020 06:21:52 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 22.10.2020 06:21:54 [] (unknown:0) - Window/level found in DICOM tags (center=100.0, width=600.0) has been applied to volume 2: Std<br>
[DEBUG][Qt] 22.10.2020 06:22:00 [] (unknown:0) - Switch to module:  “SegmentEditor”<br>
[WARNING][Qt] 22.10.2020 06:22:00 [] (unknown:0) - QLayout::addChildLayout: layout “” already has a parent<br>
[WARNING][Qt] 22.10.2020 06:22:00 [] (unknown:0) - ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 1<br>
[DEBUG][Qt] 22.10.2020 06:22:10 [] (unknown:0) - Switch to module:  “Data”<br>
[ERROR][VTK] 22.10.2020 06:22:13 [vtkMRMLSegmentationNode (0x9641dc0)] (/work/Preview/Slicer-0/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.cxx:1016) - ExportSegmentsToLabelmapNode: Failed to generate shared labelmap<br>
[CRITICAL][Qt] 22.10.2020 06:22:13 [] (unknown:0) - void qSlicerSubjectHierarchySegmentationsPlugin::exportToBinaryLabelmap() :  “Failed to export segments from segmentation Segmentation to labelmap node!\n\nMost probably the segment cannot be converted into binary labelmap representation”<br>
[DEBUG][Qt] 22.10.2020 06:28:01 [] (unknown:0) - Switch to module:  “SegmentEditor”<br>
[DEBUG][Qt] 22.10.2020 06:28:01 [] (unknown:0) - Switch to module:  “Segmentations”<br>
[ERROR][VTK] 22.10.2020 06:28:27 [vtkMRMLSegmentationNode (0x9641dc0)] (/work/Preview/Slicer-0/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.cxx:1016) - ExportSegmentsToLabelmapNode: Failed to generate shared labelmap<br>
[CRITICAL][Qt] 22.10.2020 06:28:27 [] (unknown:0) - bool qSlicerSegmentationsModuleWidget::exportFromCurrentSegmentation() :  “Failed to export segments from segmentation Segmentation to labelmap node Segmentation-Segment_1-label_1!\n\nMost probably the segment cannot be converted into binary labelmap representation.”</p>

---

## Post #3 by @l.znaniecki (2020-10-22 04:44 UTC)

<aside class="quote no-group quote-modified" data-username="l.znaniecki" data-post="2" data-topic="14197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/2bfe46/48.png" class="avatar"> l.znaniecki:</div>
<blockquote>
<p>[ERROR][Python] 22.10.2020 06:21:51 [Python] (/home/dugi/.config/NA-MIC/Extensions-29077/SlicerHeart/lib/Slicer-4.11/qt-scripted-modules/DicomUltrasoundPlugin.py:134) - sopClassUID 1.2.840.10008.5.1.4.1.1.2 != supportedSOPClassUID 1.2.840.10008.5.1.4.1.1.3.1<br>
[CRITICAL][Stream] 22.10.2020 06:21:51 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - sopClassUID 1.2.840.10008.5.1.4.1.1.2 != supportedSOPClassUID 1.2.840.10008.5.1.4.1.1.3.1</p>
</blockquote>
</aside>
<p>I get a lot of lines of this:<br>
[ERROR][Python] 22.10.2020 06:21:51 [Python] (/home/dugi/.config/NA-MIC/Extensions-29077/SlicerHeart/lib/Slicer-4.11/qt-scripted-modules/DicomUltrasoundPlugin.py:134) - sopClassUID 1.2.840.10008.5.1.4.1.1.2 != supportedSOPClassUID 1.2.840.10008.5.1.4.1.1.3.1</p>
<p>and this:<br>
[CRITICAL][Stream] 22.10.2020 06:21:51 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - sopClassUID 1.2.840.10008.5.1.4.1.1.2 != supportedSOPClassUID 1.2.840.10008.5.1.4.1.1.3.1</p>
<p>Just erased them, so I could fit the log in here.</p>
<p>Regards,<br>
Lukasz</p>

---

## Post #4 by @lassoan (2020-10-22 04:46 UTC)

<p>Please try with latest Slicer Stable Release and let us know if you run into any problems.</p>

---

## Post #5 by @l.znaniecki (2020-10-22 07:32 UTC)

<p>4.11 from 25.05 is the latest stable that works under Ubuntu. 4.11 from 5.10.2020 and 4.13 just don’t start.</p>

---

## Post #6 by @lassoan (2020-10-22 13:18 UTC)

<p>Many people uses latest version of Slicer (4.11.20200930) on Ubuntu without any problems. What CPU, Graphics, and Ubuntu version do you have?</p>

---

## Post #7 by @l.znaniecki (2020-10-22 13:28 UTC)

<p>Ryzen 3900x, amd r5 230 gpu, ubuntu 20.4</p>

---

## Post #8 by @lassoan (2020-10-22 13:43 UTC)

<p>Radeon R5 230 was launched in April 2014. Do you have this one? We try to balance between compatibility and performance/simplicity of our code base. As a result, we aim for keeping compatibility with hardware that is released in the past 5 years. Can you try with a newer card or at least latest drivers?</p>
<p>Does latest <a href="https://www.paraview.org/">ParaView</a> version work on your computer?</p>

---

## Post #9 by @l.znaniecki (2020-10-22 16:09 UTC)

<p>Paraview runs OK, I just installed it, the program opens and windows respond.</p>
<p>I have this R5 230 that you mention. Will update drivers and let you know.</p>
<p>Regards,<br>
Lukasz</p>

---

## Post #10 by @l.znaniecki (2020-10-22 20:31 UTC)

<p>Updated AMD drivers to the latest version, didn’t help. Still can’t export segmentation to binary labelmap. Your help would be very much appreciated.</p>
<p>Regards,<br>
Łukasz</p>

---

## Post #11 by @lassoan (2020-10-22 21:09 UTC)

<p>ParaView uses similar Qt and VTK versions as Slicer, so it it probably just some trivial configuration option that causes you problems.</p>
<p>What do you see when you start Slicer? Are any windows displayed? Do you see any error messages? Can you get a stack trace?</p>
<p>Does Slicer start if you remove <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#settings-file-location">Slicer.ini</a> (or the entire Slicer settings folder)?</p>

---

## Post #12 by @l.znaniecki (2020-10-22 21:18 UTC)

<p>When I start 25.05 4.11 version - all is OK, until I try to <strong>export to binary</strong> - then it is not possible.<br>
Version 4.11 form 30.09 - just does not start, for a millisecond a initial logo appers and instantly disappears.</p>

---

## Post #13 by @l.znaniecki (2020-10-22 21:30 UTC)

<p>Shame on me, but I can’t locate Slicer.ini. I have extracted Slicer folders into documents folder, can’t find .ini file.</p>

---

## Post #14 by @l.znaniecki (2020-10-22 21:34 UTC)

<p>OK, just found Slicer.ini. Will experiment.</p>

---

## Post #15 by @lassoan (2020-10-22 21:48 UTC)

<p>I just remember now that there is a problem with recent Qt versions on linux - this may solve your problem:</p>
<aside class="quote quote-modified" data-post="2" data-topic="14029">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/cant-start-latest-stable-on-ubuntu-20-04/14029/2">Can't start latest stable on ubuntu 20.04</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    OK. As per <a href="https://askubuntu.com/questions/308128/failed-to-load-platform-plugin-xcb-while-launching-qt5-app-on-linux-without" rel="noopener nofollow ugc">this thread,</a> setting: 
export QT_DEBUG_PLUGINS=1 
revealed missing library  libxcb-xinerama0. Installing it fixed the problem. 
maga@magalab-ubuntu:~/Downloads/Slicer-4.11.20200930-linux-amd64$ export QT_DEBUG_PLUGINS=1
maga@magalab-ubuntu:~/Downloads/Slicer-4.11.20200930-linux-amd64$ ./Slicer 
QFactoryLoader::QFactoryLoader() ignoring "com.nokia.qt.QGuiPlatformPluginInterface" since plugins are disabled in static builds 
QFactoryLoader::QFactoryLoader() ignoring "com.trolltech.Qt.QSt…
  </blockquote>
</aside>


---

## Post #16 by @l.znaniecki (2020-10-23 04:00 UTC)

<p>Super. The problem was solved by reinstalling xinerama:</p>
<pre><code class="lang-auto">sudo apt-get install --reinstall libxcb-xinerama0
</code></pre>
<p>Now latest 4.11 works, and export to binary works as well.</p>
<p>Thank you!<br>
Best regards,</p>
<p>Lukasz</p>

---

## Post #17 by @lassoan (2020-10-23 04:20 UTC)

<p>Awesome. I’ll add this to the linux install instructions.</p>

---
