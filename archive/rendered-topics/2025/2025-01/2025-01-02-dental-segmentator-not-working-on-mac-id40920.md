# Dental Segmentator not working on Mac

**Topic ID**: 40920
**Date**: 2025-01-02
**URL**: https://discourse.slicer.org/t/dental-segmentator-not-working-on-mac/40920

---

## Post #1 by @nguyetun (2025-01-02 00:07 UTC)

<p>Dental Segmentator was working on Slicer 5.7 May or June 2024 build but on the latest 12.31.2024 build, it stalls.  Any help would be appreciated.</p>
<p>Could some one also direct me to where I can download the old versions of the nightly build as a backup?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/135b2c9e4f5084fd5e3d3b3215701662f37dde84.jpeg" data-download-href="/uploads/short-url/2LepxytC7Uo8vpvWWwPlifaEROk.jpeg?dl=1" title="Screenshot 2025-01-01 at 10.48.24 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/135b2c9e4f5084fd5e3d3b3215701662f37dde84_2_690x470.jpeg" alt="Screenshot 2025-01-01 at 10.48.24 AM" data-base62-sha1="2LepxytC7Uo8vpvWWwPlifaEROk" width="690" height="470" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/135b2c9e4f5084fd5e3d3b3215701662f37dde84_2_690x470.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/135b2c9e4f5084fd5e3d3b3215701662f37dde84_2_1035x705.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/135b2c9e4f5084fd5e3d3b3215701662f37dde84_2_1380x940.jpeg 2x" data-dominant-color="C7C7C4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-01-01 at 10.48.24 AM</span><span class="informations">1920×1310 201 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2025-01-02 00:10 UTC)

<p>Please copy the complete log here (menu: Help / Report a bug). I can see in the screnshot that there were some error messages, but the log entry you selected was just some informational message.</p>

---

## Post #3 by @nguyetun (2025-01-04 20:06 UTC)

<p>Since I’m new, it won’t let me post with more than 3 links and the error log has multiple links</p>

---

## Post #4 by @nguyetun (2025-01-04 20:10 UTC)

<p>I took out the links.  Hope this works.</p>
<p>Here’s the log:</p>
<p>[DEBUG][Qt] 02.01.2025 12:29:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 20250102_122913<br>
[DEBUG][Qt] 02.01.2025 12:29:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 5.7.0-2024-12-31 (revision 33176 / e18fac6) macosx-amd64 - installed release<br>
[DEBUG][Qt] 02.01.2025 12:29:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: macOS / 15.1.1 / 24B91 / UTF-8 - 64-bit<br>
[DEBUG][Qt] 02.01.2025 12:29:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 32768 MB physical, 0 MB virtual<br>
[DEBUG][Qt] 02.01.2025 12:29:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …:  Apple M1 Max, 10 cores, 10 logical processors<br>
[DEBUG][Qt] 02.01.2025 12:29:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 02.01.2025 12:29:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.8, with SSL, requested OpenGL 3.2 (core profile)<br>
[DEBUG][Qt] 02.01.2025 12:29:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - DCMTK configuration …: version 3.6.8, no SSL<br>
[DEBUG][Qt] 02.01.2025 12:29:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Internationalization …: disabled, language=<br>
[DEBUG][Qt] 02.01.2025 12:29:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode …: disabled<br>
[DEBUG][Qt] 02.01.2025 12:29:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: /Applications/Slicer.app/Contents/MacOS<br>
[DEBUG][Qt] 02.01.2025 12:29:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: Extensions-33176/AnglePlanesExtension/lib/Slicer-5.7/qt-scripted-modules, Extensions-33176/CMFreg/lib/Slicer-5.7/cli-modules, Extensions-33176/CMFreg/lib/Slicer-5.7/qt-scripted-modules, Extensions-33176/DatabaseInteractor/lib/Slicer-5.7/qt-scripted-modules, Extensions-33176/EasyClip/lib/Slicer-5.7/qt-scripted-modules, Extensions-33176/MeshStatisticsExtension/lib/Slicer-5.7/qt-scripted-modules, Extensions-33176/BoneTextureExtension/lib/Slicer-5.7/cli-modules, Extensions-33176/BoneTextureExtension/lib/Slicer-5.7/qt-scripted-modules, Extensions-33176/MeshToLabelMap/lib/Slicer-5.7/cli-modules, Extensions-33176/MeshToLabelMap/lib/Slicer-5.7/qt-scripted-modules, Extensions-33176/ModelToModelDistance/lib/Slicer-5.7/cli-modules, Extensions-33176/PickAndPaintExtension/lib/Slicer-5.7/qt-scripted-modules, Extensions-33176/Q3DC/lib/Slicer-5.7/qt-scripted-modules, Extensions-33176/ShapePopulationViewer/lib/Slicer-5.7/qt-loadable-modules, Extensions-33176/SlicerMarkupConstraints/lib/Slicer-5.7/qt-scripted-modules, Extensions-33176/SlicerCMF/lib/Slicer-5.7/qt-scripted-modules, Extensions-33176/ShapeVariationAnalyzer/lib/Slicer-5.7/cli-modules, Extensions-33176/ShapeVariationAnalyzer/lib/Slicer-5.7/qt-scripted-modules, Extensions-33176/NNUNet/lib/Slicer-5.7/qt-scripted-modules, Extensions-33176/PyTorch/lib/Slicer-5.7/qt-scripted-modules, Extensions-33176/DentalSegmentator/lib/Slicer-5.7/qt-scripted-modules, Extensions-33176/SlicerPythonTestRunner/lib/Slicer-5.7/qt-scripted-modules<br>
[CRITICAL][FD] 02.01.2025 12:29:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - 2025-01-02 12:29:13.907 Slicer[44098:1058598] +[IMKClient subclass]: chose IMKClient_Modern<br>
[CRITICAL][FD] 02.01.2025 12:29:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - 2025-01-02 12:29:13.907 Slicer[44098:1058598] +[IMKInputSession subclass]: chose IMKInputSession_Modern<br>
[WARNING][Qt] 02.01.2025 12:29:17 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile<br>
[DEBUG][Python] 02.01.2025 12:29:17 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.7/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 02.01.2025 12:29:17 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.7/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 02.01.2025 12:29:17 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[WARNING][Qt] 02.01.2025 12:29:18 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Populating font family aliases took 139 ms. Replace uses of missing font family “.AppleSystemUIFont” with one that exists to avoid this cost.<br>
[DEBUG][Qt] 02.01.2025 12:30:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “Volume” Reader has successfully read the file “/Volumes/TTN/_Herbst Project/_Herbst/1 Chapman/Segmentations/V1 Chapman FH.nii.gz” “[0.51s]”<br>
[DEBUG][Qt] 02.01.2025 12:30:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “DentalSegmentator”<br>
[CRITICAL][Qt] 02.01.2025 12:30:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - void qMRMLSegmentEditorWidget::setSourceVolumeNode(vtkMRMLNode *)  failed: need to set segment editor and segmentation nodes first<br>
[INFO][Python] 02.01.2025 12:30:17 [Python] (/Applications/Slicer.app/Contents/Extensions-33176/NNUNet/lib/Slicer-5.7/qt-scripted-modules/SlicerNNUNetLib/InstallLogic.py:56) - nnUNet is already installed (2.5.1) and compatible with requested version (nnunetv2).<br>
[DEBUG][Python] 02.01.2025 12:30:17 [Python] (/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/urllib3/connectionpool.py:1055) - Starting new HTTPS connection (1):<br>
[DEBUG][Python] 02.01.2025 12:30:17 [Python] (/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/urllib3/connectionpool.py:549) –<br>
“GET / HTTP/1.1” 200 None<br>
[DEBUG][Python] 02.01.2025 12:30:17 [Python] (/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/urllib3/connectionpool.py:1055) - Starting new HTTPS connection (1): <a href="http://api.github.com:443" rel="noopener nofollow ugc">api.github.com:443</a><br>
[DEBUG][Python] 02.01.2025 12:30:17 [Python] (/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/urllib3/connectionpool.py:549)<br>
“GET /repos/gaudot/SlicerDentalSegmentator HTTP/1.1” 200 1466<br>
[DEBUG][Python] 02.01.2025 12:30:18 [Python] (/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/urllib3/connectionpool.py:549)<br>
“GET /repos/gaudot/SlicerDentalSegmentator/releases HTTP/1.1” 200 810<br>
[DEBUG][Python] 02.01.2025 12:30:18 [Python] (/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/urllib3/connectionpool.py:549)<br>
“GET /repos/gaudot/SlicerDentalSegmentator/releases/147040025/assets HTTP/1.1” 200 598<br>
[CRITICAL][Stream] 02.01.2025 12:30:18 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 02.01.2025 12:30:18 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “/Applications/Slicer.app/Contents/Extensions-33176/DentalSegmentator/lib/Slicer-5.7/qt-scripted-modules/DentalSegmentatorLib/SegmentationWidget.py”, line 238, in onApplyClicked<br>
[CRITICAL][Stream] 02.01.2025 12:30:18 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     self._runSegmentation()<br>
[CRITICAL][Stream] 02.01.2025 12:30:18 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “/Applications/Slicer.app/Contents/Extensions-33176/DentalSegmentator/lib/Slicer-5.7/qt-scripted-modules/DentalSegmentatorLib/SegmentationWidget.py”, line 257, in _runSegmentation<br>
[CRITICAL][Stream] 02.01.2025 12:30:18 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     if not parameter.isSelectedDeviceAvailable():<br>
[CRITICAL][Stream] 02.01.2025 12:30:18 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “/Applications/Slicer.app/Contents/Extensions-33176/NNUNet/lib/Slicer-5.7/qt-scripted-modules/SlicerNNUNetLib/Parameter.py”, line 66, in isSelectedDeviceAvailable<br>
[CRITICAL][Stream] 02.01.2025 12:30:18 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     import torch<br>
[CRITICAL][Stream] 02.01.2025 12:30:18 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - ModuleNotFoundError: No module named ‘torch’</p>

---

## Post #5 by @jamesobutler (2025-01-04 21:02 UTC)

<p><a class="mention" href="/u/nguyetun">@nguyetun</a> I fixed some things with the SlicerNNUNet extension used by DentalSegmentator. This would only be available in the latest Slicer preview from the past day or so. Can you install the latest macOS Slicer preview and try your installation again?</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://download.slicer.org/">
  <header class="source">
      <img src="https://slicer.org/assets/favicons/favicon-32x32.png?v=Gv63MLlwnz" class="site-icon" width="32" height="32">

      <a href="https://download.slicer.org/" target="_blank" rel="noopener nofollow ugc">3D Slicer</a>
  </header>

  <article class="onebox-body">
    <img width="128" height="128" src="https://slicer.org/assets/img/3d-slicer-128x128.png" class="thumbnail onebox-avatar">

<h3><a href="https://download.slicer.org/" target="_blank" rel="noopener nofollow ugc">Download 3D Slicer</a></h3>

  <p>3D Slicer is a free, open source software for visualization, processing, segmentation, registration, and analysis of medical, biomedical, and other 3D images and meshes; and planning and navigating image-guided procedures.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I do know see that DentalSegmenatot has a selection for CUDA which you won’t have being on Apple Silicon but it should pull the CPU only version of torch for macOS.</p>

---

## Post #6 by @nguyetun (2025-01-05 01:40 UTC)

<p>Thanks, the latest version 1.3.25 of Slicer works with Dental Segmentator.</p>
<p>Tung</p>

---
