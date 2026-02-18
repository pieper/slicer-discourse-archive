# CARDIAC module: echo Volume Render Bug

**Topic ID**: 31399
**Date**: 2023-08-28
**URL**: https://discourse.slicer.org/t/cardiac-module-echo-volume-render-bug/31399

---

## Post #1 by @mvergnat (2023-08-28 10:28 UTC)

<p>Operating system: windows<br>
Slicer version: 5.2.2</p>
<p>hello to everybody, hello Dr Lasso!</p>
<p>I am still Slicer beginner but I try to improve my self…</p>
<p>Now my current problem is that echo Volume Render does not function anymore<br>
<strong>It was well functioning last month but now does not anymore…</strong><br>
Here it is:<br>
I follow the classic upload pathway for 4D US, described on following video link:</p><div class="youtube-onebox lazy-video-container" data-video-id="bptkjcdvHD8" data-video-title="SlicerHeart: Echo Volume Rendering Module in 3D Slicer" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=bptkjcdvHD8" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/bptkjcdvHD8/maxresdefault.jpg" title="SlicerHeart: Echo Volume Rendering Module in 3D Slicer" width="" height="">
  </a>
</div>

<p>first philips 4d US dicom patcher<br>
input/output directory,<br>
then<br>
export to NRDD files<br>
the NRDD file is then draged into the 3D view.<br>
OK.<br>
then open the module echo Volume render,<br>
click apply to sequence, (smoothing factor ist 1)<br>
apply.</p>
<p>Then I dont see any 3D volume…</p>
<p>I tried several things, without success:<br>
-modify Rendering settings (smoothing, threshold…),<br>
-close other App in computer, restart the 3dslicer, restart computer,<br>
-redo the philips 4d US dicom patcher,<br>
-I also tried other NRDD files that were functioning last month.</p>
<p>the volume is there (I can make it appear with the module Volume rendering), BUT the <em>echo</em> volume Render Module does not function anymore.</p>
<p>noteworthy is:<br>
when I change, in the Volume Rendering Category, the echo Volume from 1 (for example from the selected volume) to another (to the selected volume*_filtered*), I see the volume VERY <strong>strong text</strong>quicly (0,01s) and then it disappear…<br>
(it was very difficult to catch it (0,01s) but I finally could screenshoot it:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6b70c7d06434ac187ff5bb4dcb1ddd3eea4d4e1.jpeg" data-download-href="/uploads/short-url/wUZZTTqv8nwoB23RMpl05hzTIiZ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6b70c7d06434ac187ff5bb4dcb1ddd3eea4d4e1_2_690x367.jpeg" alt="image" data-base62-sha1="wUZZTTqv8nwoB23RMpl05hzTIiZ" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6b70c7d06434ac187ff5bb4dcb1ddd3eea4d4e1_2_690x367.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6b70c7d06434ac187ff5bb4dcb1ddd3eea4d4e1_2_1035x550.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6b70c7d06434ac187ff5bb4dcb1ddd3eea4d4e1_2_1380x734.jpeg 2x" data-dominant-color="9D9EB1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1022 70.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
)<br>
So the volume is there, but does not want to show itself…</p>
<p>Can anything help to better understand the problem??<br>
Many thx for help!</p>
<p>mathieu</p>

---

## Post #2 by @mvergnat (2023-08-28 10:48 UTC)

<p>I also tried with installing the last version 5.4.0<br>
no effect.<br>
It is weird because Still, I can load some old scenes where I saved a 4D echo volume and it works…<br>
so:<br>
it is not a computer problem,<br>
it is not a software problem,<br>
it is apparently some settings somewhere that need to be refined.<br>
importantly:<br>
I (and nobody) did not touch the computer since a month, and before it was working fine.<br>
So, nothing changed in the settings and in the computer since a month.</p>

---

## Post #3 by @mvergnat (2023-08-28 11:43 UTC)

<p>sorry for hassling everyone, but some news happened:</p>
<p>I tested the data (nrrd file) in another computer…AND it WORKED!!</p>
<p>So problem is not the data.</p>
<p>We looked if the amount of memory on the computer was ok: it is OK:<br>
the CPU is also ok<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01df1cfb0cfda0e1c3d1a4573863ef4f50377be6.jpeg" data-download-href="/uploads/short-url/gyuHY29zSRUW90Zrhq2HXfnlB4.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01df1cfb0cfda0e1c3d1a4573863ef4f50377be6_2_690x482.jpeg" alt="image" data-base62-sha1="gyuHY29zSRUW90Zrhq2HXfnlB4" width="690" height="482" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01df1cfb0cfda0e1c3d1a4573863ef4f50377be6_2_690x482.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01df1cfb0cfda0e1c3d1a4573863ef4f50377be6_2_1035x723.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01df1cfb0cfda0e1c3d1a4573863ef4f50377be6_2_1380x964.jpeg 2x" data-dominant-color="E8F0F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1526×1067 204 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The graphic card is also OK, because it was ok last month, when the 3d was OK.</p>
<p>I discussed with my imaging specialist:<br>
he said, maybe I need to change something in the <strong>application settings</strong>???</p>

---

## Post #4 by @mvergnat (2023-08-28 12:09 UTC)

<p>application settings are the same on both computer…<br>
<strong>so something is with my computer wrong for 3dslicer</strong><br>
and this thing was not there a month ago (apparently not a hardware problem).</p>

---

## Post #5 by @mvergnat (2023-08-31 11:04 UTC)

<p>dear Slicer team,</p>
<p>thank you for your help,<br>
I am really big big fan of Slicer and it is big problem for me that this echo volume render module does not function anymore.</p>
<h2><a name="p-100024-summary-1" class="anchor" href="#p-100024-summary-1" aria-label="Heading link"></a>Summary</h2>
<p>4D echo loop from Qlab exported into 3dslicer as NRRD file. the ECHO VOLUME RENDER module (sub module of CARDIAC module extension) does not function: no 3d volume showed in the 3d panel.</p>
<h2><a name="p-100024-environment-2" class="anchor" href="#p-100024-environment-2" aria-label="Heading link"></a>Environment</h2>
<ul>
<li>Slicer version: 5.4.0 r31938 / <a href="https://github.com/Slicer/Slicer/commit/311cb26c5430f82c47e9ff186658b80e7b95e2a5" rel="noopener nofollow ugc">311cb26</a></li>
<li>Operating system: Windows 10</li>
</ul>
<h2><a name="p-100024-python-console-report-3" class="anchor" href="#p-100024-python-console-report-3" aria-label="Heading link"></a>Python Console Report</h2>
<p>I have no programming competence, but a colleague told me to enclose this report:</p>
<p>Python 3.9.10 (main, Feb 22 2023, 01:07:37) [MSC v.1930 64 bit (AMD64)] on win32</p>
<p>Traceback (most recent call last):<br>
File “C:/Users/50113999/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/SlicerHeart/lib/Slicer-5.2/qt-scripted-modules/EchoVolumeRender.py”, line 62, in<br>
self.ui.volumeRenderingVisibleCheckBox.stateChanged.connect(lambda state: self.logic.setVolumeRenderingVisible(state == qt.Qt.Checked))<br>
File “C:/Users/50113999/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/SlicerHeart/lib/Slicer-5.2/qt-scripted-modules/EchoVolumeRender.py”, line 469, in setVolumeRenderingVisible<br>
self.volumeRenderingDisplayNode.SetVisibility(visible)<br>
AttributeError: ‘NoneType’ object has no attribute ‘SetVisibility’<br>
<strong>[VTK] Warning: In D:\D\S\S-0\Modules\Loadable\VolumeRendering\Logic\vtkSlicerVolumeRenderingLogic.cxx, line 667</strong><br>
<strong>[VTK] vtkSlicerVolumeRenderingLogic (000001E5864B6D60): CopyDisplayToVolumeRenderingDisplayNode: Volume Rendering display node does not reference a volume node.</strong></p>
<h2><a name="p-100024-steps-to-reproduce-4" class="anchor" href="#p-100024-steps-to-reproduce-4" aria-label="Heading link"></a>Steps to reproduce</h2>
<p>echo loop from Qlab exported into 3dslicer as NRRD file. works fine</p>
<p>then opening of module Cardiac, subset ECHO VOLUME RENDER,<br>
then classic pathway:<br>
click apply to sequence, (smoothing factor is 1)<br>
apply.<br>
Then I dont see any 3D volume…<br>
<a href="https://user-images.githubusercontent.com/143593990/264282042-8ed75864-ef12-4a3f-a338-c8115ec4518b.png" rel="noopener nofollow ugc"><img src="https://user-images.githubusercontent.com/143593990/264282042-8ed75864-ef12-4a3f-a338-c8115ec4518b.png" alt="image" width="690" height="388"></a></p>
<h2><a name="p-100024-expected-behavior-5" class="anchor" href="#p-100024-expected-behavior-5" aria-label="Heading link"></a>Expected behavior</h2>
<p>expected is to see a volume in the 3d Panel, which is not the case.</p>
<p>I used the ECHO VOLUME RENDER module a month ago and it was working.<br>
now the module does not function anymore??<br>
since a month, I did not use my computer (nothing new nothing was installed, nobody used computer).</p>
<p>I tried multiple procedures:<br>
-modify Rendering settings (smoothing, threshold…) (of course the visible box is always checked),<br>
-close other App in computer, restart the 3dslicer, restart computer,<br>
-redo the philips 4d US dicom patcher,<br>
-I also tried other NRDD files that were functioning last month.<br>
-use older Slicer version (5.2),<br>
-look at computer memory (seems all normal, no problem of computer memory),<br>
-use another computer, use another windows User session.<br>
(in fact I tried several computer from my center, AND on only one computer, it was functionning, but on 3 other it did not function; unfortunately I dont undersatnd why, because there is no big difference between the 1 computer and the other…)</p>
<p>Seems to be a setting problem, because<br>
the ECHO VOLUME RENDER module does not function<br>
BUT<br>
the VOLUME RENDERING module DOES function:<br>
<a href="https://user-images.githubusercontent.com/143593990/264283075-8e368547-6da8-442b-8aff-5efbeaedf994.png" rel="noopener nofollow ugc"><img src="https://user-images.githubusercontent.com/143593990/264283075-8e368547-6da8-442b-8aff-5efbeaedf994.png" alt="image" width="690" height="388"></a></p>
<p>Any idea???<br>
many thanks for help!!!</p>
<p>mathieu<br>
big fan of 3dSlicer</p>

---

## Post #6 by @lassoan (2023-09-05 04:32 UTC)

<p>Thank you for reporting the issue. We have reproduced the issue in Slicer-5.4 and implemented a fix (it is available by updating the SlicerHeart extension later today).</p>

---

## Post #7 by @mvergnat (2023-09-06 09:17 UTC)

<p>Dear Dr Lasso!<br>
Many thanks for help and for your expert support!!<br>
Unfortunately I am still blocked. Apologizes.<br>
I went on extension manager:</p>
<ol>
<li>I tried “check for updates” and installed updates. Restart. Failed again.</li>
<li>I unsinstalled SlicerHeart extension und reinstalled it. Restart. Failed again.</li>
<li>Python module:<br>
<strong>Warning: In vtkSlicerVolumeRenderingLogic.cxx, line 692<br>
vtkSlicerVolumeRenderingLogic (000001AE2C301E50): CopyDisplayToVolumeRenderingDisplayNode: Volume Rendering display node does not reference a volume node.<br>
Same problem.</strong></li>
</ol>
<p>Did I do something wrong? Should I do differently??<br>
again, comment (maybe they help to understand):<br>
how is it possible that it was last month functioning and today not anymore???<br>
how is it possible that I found 2 computers where it works…,???</p>
<p>I apologize for hassling people.<br>
I love 3Dslicer, and I compliment everyday the 3dslicer progammer for their wonderful Programm, that ist SUPER helpful!!!<br>
(I also understand that all these things are made by volonteers! still very nice work!)<br>
again thank you!!<br>
mathieu, 3DSlicer big big fan</p>

---

## Post #8 by @mvergnat (2023-09-08 06:42 UTC)

<p>from lassoan:<br>
" Echo Volume Renderer requires GPU rendering mode.<br>
<strong>Change the default mode in application settings / Volume rendering to <code>VTK GPU Raycasting</code></strong> to fix this issue.<br>
I’ll make the module more robust to avoid this issue."</p>
<p>Awesome!!!<br>
endly, so easy process!<br>
Many thanks to Dr Lasso for expert help and support!</p>

---
