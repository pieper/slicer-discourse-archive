---
topic_id: 40714
title: "Segment Statistics Module On 3D Slicer 5 6 2"
date: 2024-12-16
url: https://discourse.slicer.org/t/40714
---

# Segment Statistics Module on 3D Slicer 5.6.2

**Topic ID**: 40714
**Date**: 2024-12-16
**URL**: https://discourse.slicer.org/t/segment-statistics-module-on-3d-slicer-5-6-2/40714

---

## Post #1 by @imbeatriz (2024-12-16 14:00 UTC)

<p>Hi everyone!</p>
<p>I wanted to use the Segment Statistics module to validate the VOIs I segmented using Scalar Volume Statistic, but it doesn’t seem to be working in my 3D Slicer version 5.6.2.</p>
<p>Does anyone what this could be done to? What alternative could I use?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c1bd1f90292235560d7fc1c5c0ef6355e7ff21d.png" data-download-href="/uploads/short-url/fqnaCzs9LzgNPYwC8guOPhbdTm5.png?dl=1" title="tttt" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c1bd1f90292235560d7fc1c5c0ef6355e7ff21d_2_690x481.png" alt="tttt" data-base62-sha1="fqnaCzs9LzgNPYwC8guOPhbdTm5" width="690" height="481" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c1bd1f90292235560d7fc1c5c0ef6355e7ff21d_2_690x481.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c1bd1f90292235560d7fc1c5c0ef6355e7ff21d_2_1035x721.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c1bd1f90292235560d7fc1c5c0ef6355e7ff21d.png 2x" data-dominant-color="ADA5A4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">tttt</span><span class="informations">1130×789 275 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you!</p>
<p>Greetings,<br>
Beatriz</p>

---

## Post #2 by @cpinter (2024-12-16 14:58 UTC)

<p>What operating system do you use? Is there any error in the Python console or Error log after start-up?</p>

---

## Post #3 by @imbeatriz (2024-12-16 15:05 UTC)

<p>I have Ubuntu 24.04 LTS system. On the python console it shows the following:</p>
<p>Python 3.9.10 (main, Apr  5 2024, 04:28:47)<br>
[GCC 7.3.1 20180303 (Red Hat 7.3.1-5)] on linux2</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<p>[Qt]   Error(s):<br>
[Qt]     Cannot load library /home/administrator/Software/Slicer-5.6.2-linux-amd64/slicer.org/Extensions-32448/SlicerRT/lib/Slicer-5.6/qt-loadable-modules/libqSlicerBeamsModule.so: (libvtkIECTransformLogic.so: cannot open shared object file: No such file or directory)<br>
[Qt]   Error(s):<br>
[Qt]     Cannot load library /home/administrator/Software/Slicer-5.6.2-linux-amd64/slicer.org/Extensions-32448/SlicerRT/lib/Slicer-5.6/qt-loadable-modules/libqSlicerDicomRtImportExportModule.so: (libvtkIECTransformLogic.so: cannot open shared object file: No such file or directory)<br>
[Qt]   Error(s):<br>
[Qt]     Cannot load library /home/administrator/Software/Slicer-5.6.2-linux-amd64/slicer.org/Extensions-32448/SlicerRT/lib/Slicer-5.6/qt-loadable-modules/libqSlicerDicomSroImportExportModule.so: (libvtkIECTransformLogic.so: cannot open shared object file: No such file or directory)<br>
[Qt]   Error(s):<br>
[Qt]     Cannot load library /home/administrator/Software/Slicer-5.6.2-linux-amd64/slicer.org/Extensions-32448/SlicerRT/lib/Slicer-5.6/qt-loadable-modules/libqSlicerDrrImageComputationModule.so: (libvtkIECTransformLogic.so: cannot open shared object file: No such file or directory)<br>
[Qt]   Error(s):<br>
[Qt]     Cannot load library /home/administrator/Software/Slicer-5.6.2-linux-amd64/slicer.org/Extensions-32448/SlicerRT/lib/Slicer-5.6/qt-loadable-modules/libqSlicerExternalBeamPlanningModule.so: (libvtkIECTransformLogic.so: cannot open shared object file: No such file or directory)<br>
[Qt]   Error(s):<br>
[Qt]     Cannot load library /home/administrator/Software/Slicer-5.6.2-linux-amd64/slicer.org/Extensions-32448/SlicerRT/lib/Slicer-5.6/qt-loadable-modules/libqSlicerPlmProtonDoseEngineModule.so: (libvtkIECTransformLogic.so: cannot open shared object file: No such file or directory)<br>
[Qt]   Error(s):<br>
[Qt]     Cannot load library /home/administrator/Software/Slicer-5.6.2-linux-amd64/slicer.org/Extensions-32448/SlicerRT/lib/Slicer-5.6/qt-loadable-modules/libqSlicerRoomsEyeViewModule.so: (libvtkIECTransformLogic.so: cannot open shared object file: No such file or directory)<br>
libvtkIECTransformLogic.so: cannot open shared object file: No such file or directory<br>
libvtkIECTransformLogic.so: cannot open shared object file: No such file or directory<br>
libvtkIECTransformLogic.so: cannot open shared object file: No such file or directory<br>
libvtkIECTransformLogic.so: cannot open shared object file: No such file or directory<br>
libvtkIECTransformLogic.so: cannot open shared object file: No such file or directory<br>
libvtkIECTransformLogic.so: cannot open shared object file: No such file or directory<br>
libvtkIECTransformLogic.so: cannot open shared object file: No such file or directory<br>
libvtkIECTransformLogic.so: cannot open shared object file: No such file or directory<br>
libvtkIECTransformLogic.so: cannot open shared object file: No such file or directory<br>
libvtkIECTransformLogic.so: cannot open shared object file: No such file or directory<br>
[Qt] When loading module  “BatchStructureSetConversion” , the dependency “DicomRtImportExport” failed to be loaded.<br>
[Qt] When loading module  “IGRTWorkflow_SelfTest” , the dependency “DicomRtImportExport” failed to be loaded.<br>
Traceback (most recent call last):<br>
File “/home/administrator/Software/Slicer-5.6.2-linux-amd64/lib/Slicer-5.6/qt-scripted-modules/SegmentStatistics.py”, line 58, in setup<br>
self.logic = SegmentStatisticsLogic()<br>
File “/home/administrator/Software/Slicer-5.6.2-linux-amd64/lib/Slicer-5.6/qt-scripted-modules/SegmentStatistics.py”, line 394, in <strong>init</strong><br>
self.reset()<br>
File “/home/administrator/Software/Slicer-5.6.2-linux-amd64/lib/Slicer-5.6/qt-scripted-modules/SegmentStatistics.py”, line 430, in reset<br>
params = self.getParameterNode()<br>
File “/home/administrator/Software/Slicer-5.6.2-linux-amd64/lib/Slicer-5.6/qt-scripted-modules/SegmentStatistics.py”, line 399, in getParameterNode<br>
self.setParameterNode(ScriptedLoadableModuleLogic.getParameterNode(self))<br>
File “/home/administrator/Software/Slicer-5.6.2-linux-amd64/lib/Slicer-5.6/qt-scripted-modules/SegmentStatistics.py”, line 409, in setParameterNode<br>
plugin.setParameterNode(parameterNode)<br>
File “/home/administrator/Software/Slicer-5.6.2-linux-amd64/lib/Slicer-5.6/qt-scripted-modules/SegmentStatisticsPlugins/SegmentStatisticsPluginBase.py”, line 124, in setParameterNode<br>
self.createDefaultOptionsWidget()<br>
File “/home/administrator/Software/Slicer-5.6.2-linux-amd64/lib/Slicer-5.6/qt-scripted-modules/SegmentStatisticsPlugins/SegmentStatisticsPluginBase.py”, line 164, in createDefaultOptionsWidget<br>
info = self.getMeasurementInfo(key)<br>
File “/home/administrator/Software/Slicer-5.6.2-linux-amd64/slicer.org/Extensions-32448/PET-IndiC/lib/Slicer-5.6/qt-scripted-modules/PETVolumeSegmentStatisticsPlugin/PETVolumeSegmentStatisticsPlugin.py”, line 106, in getMeasurementInfo<br>
self.createMeasurementInfo(name=“Mean”, description=“Mean uptake value”,<br>
TypeError: createMeasurementInfo() missing 1 required positional argument: ‘title’<br>
Traceback (most recent call last):<br>
File “/home/administrator/Software/Slicer-5.6.2-linux-amd64/lib/Slicer-5.6/qt-scripted-modules/SegmentStatistics.py”, line 170, in enter<br>
if self.parameterNodeSelector.currentNode() is None:<br>
AttributeError: ‘SegmentStatisticsWidget’ object has no attribute ‘parameterNodeSelector’<br>
Requirement already satisfied: pillow&lt;10.1 in ./lib/Python/lib/python3.9/site-packages (10.0.1)<br>
[Qt] libpng warning: iCCP: known incorrect sRGB profile<br>
Traceback (most recent call last):<br>
File “/home/administrator/Software/Slicer-5.6.2-linux-amd64/lib/Slicer-5.6/qt-scripted-modules/SegmentStatistics.py”, line 170, in enter<br>
if self.parameterNodeSelector.currentNode() is None:<br>
AttributeError: ‘SegmentStatisticsWidget’ object has no attribute 'parameterNodeSelector</p>

---

## Post #4 by @cpinter (2024-12-16 15:13 UTC)

<p>Thanks, this is very helpful!</p>
<p>First of all this means that the SlicerRT installation failed. I’ll look into this.</p>
<p>Second, the issue you posted about is probably due to the PET-IndiC extension, it seems that there was a change in the API that was not handled correctly. If you do not absolutely need the PET-IndiC extension, try uninstalling it and then probably the SegmentStatistics module will work.<br>
But in any case the owner of the extension should look into this.</p>
<p>Actually, Slicer 5.8 is around the corner. Can you try the latest Slicer preview version?</p>

---

## Post #5 by @imbeatriz (2024-12-16 15:24 UTC)

<p>Thank you! I would really appreciate it if you could look into the SlicerRT installation issue cause I will need it.</p>
<p>I uninstalled PET-IndiC extension and the SegmentStatistics module works now.</p>
<p>Yeah I can try Slicer preview. Where can I find it tho?</p>

---

## Post #6 by @cpinter (2024-12-16 15:26 UTC)

<aside class="onebox allowlistedgeneric" data-onebox-src="https://download.slicer.org/">
  <header class="source">
      <img src="https://slicer.org/assets/favicons/favicon-32x32.png?v=Gv63MLlwnz" class="site-icon" width="32" height="32">

      <a href="https://download.slicer.org/" target="_blank" rel="noopener">3D Slicer</a>
  </header>

  <article class="onebox-body">
    <img width="128" height="128" src="https://slicer.org/assets/img/3d-slicer-128x128.png" class="thumbnail onebox-avatar">

<h3><a href="https://download.slicer.org/" target="_blank" rel="noopener">Download 3D Slicer</a></h3>

  <p>3D Slicer is a free, open source software for visualization, processing, segmentation, registration, and analysis of medical, biomedical, and other 3D images and meshes; and planning and navigating image-guided procedures.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb47df4ad9367828a974d5e8bb33d7ea46de6c1c.png" data-download-href="/uploads/short-url/xzobQD1gVF55p8QS2Iv6L7PuNly.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb47df4ad9367828a974d5e8bb33d7ea46de6c1c.png" alt="image" data-base62-sha1="xzobQD1gVF55p8QS2Iv6L7PuNly" width="690" height="279" data-dominant-color="F2F0F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">873×353 13.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @imbeatriz (2024-12-16 15:35 UTC)

<p>It seems like the preview it’s not opening in my system <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=12" title=":confused:" class="emoji" alt=":confused:" loading="lazy" width="20" height="20"></p>

---

## Post #8 by @cpinter (2024-12-16 15:40 UTC)

<aside class="quote no-group" data-username="imbeatriz" data-post="5" data-topic="40714">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/e8c25b/48.png" class="avatar"> imbeatriz:</div>
<blockquote>
<p>I would really appreciate it if you could look into the SlicerRT installation</p>
</blockquote>
</aside>
<p>One of the binaries is deployed in the incorrect folder. Please consider this folder:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/995138d2dea7635caaa90dfd85a9191318d07fcb.png" data-download-href="/uploads/short-url/lSj4m0zVnhOsYDdSf9JxdsfUvAD.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/995138d2dea7635caaa90dfd85a9191318d07fcb.png" alt="image" data-base62-sha1="lSj4m0zVnhOsYDdSf9JxdsfUvAD" width="597" height="204"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">597×204 23.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>There is an <code>.so</code> file in <code>vtkIECTransformLogic</code> that needs to be moved to <code>Slicer-5.7/qt-loadable-modules</code>. This is for the preview, for 5.6.2 it is obviously <code>Slicer-5.6</code>. I did that and then SlicerRT worked correctly. We’ll look into the code to fix deployment in upcoming packages.</p>

---

## Post #9 by @imbeatriz (2024-12-16 15:47 UTC)

<p>Thank you so much! I did the same for Slicer 5.6.2 and it fixed the errors I was getting on the python console.</p>

---

## Post #10 by @cpinter (2024-12-16 15:53 UTC)

<p>No problem!</p>
<p>For reference, here’s the ticket to follow the resolution of the SlicerRT problem: <a href="https://github.com/SlicerRt/SlicerRT/issues/262" class="inline-onebox">SlicerRT deployment fails on Linux · Issue #262 · SlicerRt/SlicerRT · GitHub</a></p>
<p>I added a new ticket in PET-IndiC as well (but not sure who will do it and when they will notice): <a href="https://github.com/QIICR/PET-IndiC/issues/8" class="inline-onebox">The extension breaks SegmentStatistics · Issue #8 · QIICR/PET-IndiC · GitHub</a></p>

---
