---
topic_id: 45914
title: "Nninteractive Module No Longer Segments Properly"
date: 2026-01-26
url: https://discourse.slicer.org/t/45914
---

# nnInteractive module no longer segments properly

**Topic ID**: 45914
**Date**: 2026-01-26
**URL**: https://discourse.slicer.org/t/nninteractive-module-no-longer-segments-properly/45914

---

## Post #1 by @lukejprose (2026-01-26 10:34 UTC)

<p>I have been using the nnInteractive module through MorphoCloud to segment CT scans of fish skulls, with a good bit of success. Now, however, the nnInteractive module no longer functions properly. The Configuration tab says that the server is reachable, but when placing the first positive point on one of the slices, it generates a cube that does not render in 3D space. Placing any additional points results in nothing happening. I have tried closing and reopening 3D Slicer, restarting the server in the terminal, changing the server port, deleting and reinstalling the nnInteractive server, logging in and out of MorphoCloud, shelving and unshelving the MorphoCloud Instance, and redoing my mrb file. Nothing fixes the issue. Even after updating the nnInteractive extension to the latest version, it still has the same issue.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e1ba617533b94a742f707812740b2a6c1417b4b.jpeg" data-download-href="/uploads/short-url/dqw7pjy7OMGPirsQs97cG2CH5Rp.jpeg?dl=1" title="Terminal - nnInteractive Server Startup" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e1ba617533b94a742f707812740b2a6c1417b4b.jpeg" alt="Terminal - nnInteractive Server Startup" data-base62-sha1="dqw7pjy7OMGPirsQs97cG2CH5Rp" width="690" height="359" data-dominant-color="47263D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Terminal - nnInteractive Server Startup</span><span class="informations">738×384 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b1bbbbe2bd07b20a9d688edd1629c5b413acd87.jpeg" data-download-href="/uploads/short-url/8qTAwZJ43zi4PMN412uisCreVcX.jpeg?dl=1" title="Terminal - nnInteractive Server Point Processing" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b1bbbbe2bd07b20a9d688edd1629c5b413acd87_2_623x500.jpeg" alt="Terminal - nnInteractive Server Point Processing" data-base62-sha1="8qTAwZJ43zi4PMN412uisCreVcX" width="623" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b1bbbbe2bd07b20a9d688edd1629c5b413acd87_2_623x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b1bbbbe2bd07b20a9d688edd1629c5b413acd87.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b1bbbbe2bd07b20a9d688edd1629c5b413acd87.jpeg 2x" data-dominant-color="411E36"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Terminal - nnInteractive Server Point Processing</span><span class="informations">710×569 188 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22bd27e5432fb576d40bf2a2b62f4442d6a478bb.jpeg" data-download-href="/uploads/short-url/4XjuUiJtLlPyqwRZyr9Ad5kwzdF.jpeg?dl=1" title="Slicer - nnInteractive Segmenting Error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22bd27e5432fb576d40bf2a2b62f4442d6a478bb_2_509x500.jpeg" alt="Slicer - nnInteractive Segmenting Error" data-base62-sha1="4XjuUiJtLlPyqwRZyr9Ad5kwzdF" width="509" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22bd27e5432fb576d40bf2a2b62f4442d6a478bb_2_509x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22bd27e5432fb576d40bf2a2b62f4442d6a478bb.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22bd27e5432fb576d40bf2a2b62f4442d6a478bb.jpeg 2x" data-dominant-color="25251F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer - nnInteractive Segmenting Error</span><span class="informations">726×712 88.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>3D Slicer - Log File:</p>
<p>[DEBUG][Qt] 25.01.2026 21:32:37 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Session start time …: 20260125_213237<br>
[DEBUG][Qt] 25.01.2026 21:32:37 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Slicer version …: 5.10.0 (revision 34045 / a2b6d08) linux-amd64 - installed release<br>
[DEBUG][Qt] 25.01.2026 21:32:37 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Operating system …: Linux / 6.8.0-90-generic / #91~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Thu Nov 20 15:20:45 UTC 2 / UTF-8 - 64-bit<br>
[DEBUG][Qt] 25.01.2026 21:32:37 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Memory …: 60263 MB physical, 0 MB virtual<br>
[DEBUG][Qt] 25.01.2026 21:32:37 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - CPU …: AuthenticAMD AMD EPYC-Milan Processor, 16 cores, 16 logical processors<br>
[DEBUG][Qt] 25.01.2026 21:32:37 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 25.01.2026 21:32:37 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (core profile)<br>
[DEBUG][Qt] 25.01.2026 21:32:37 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - DCMTK configuration …: version 3.6.8, no SSL<br>
[DEBUG][Qt] 25.01.2026 21:32:37 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Internationalization …: disabled, language=<br>
[DEBUG][Qt] 25.01.2026 21:32:37 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Developer mode …: disabled<br>
[DEBUG][Qt] 25.01.2026 21:32:37 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Application path …: /media/volume/MyData/Slicer/bin<br>
[DEBUG][Qt] 25.01.2026 21:32:37 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Additional module paths ..: <a href="http://slicer.org/Extensions-34045/SegmentEditorExtraEffects/lib/Slicer-5.10/qt-loadable-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/SegmentEditorExtraEffects/lib/Slicer-5.10/qt-loadable-modules</a>, <a href="http://slicer.org/Extensions-34045/SegmentEditorExtraEffects/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/SegmentEditorExtraEffects/lib/Slicer-5.10/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34045/SurfaceMarkup/lib/Slicer-5.10/qt-loadable-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/SurfaceMarkup/lib/Slicer-5.10/qt-loadable-modules</a>, <a href="http://slicer.org/Extensions-34045/SlicerMorph/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/SlicerMorph/lib/Slicer-5.10/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34045/MarkupsToModel/lib/Slicer-5.10/qt-loadable-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/MarkupsToModel/lib/Slicer-5.10/qt-loadable-modules</a>, <a href="http://slicer.org/Extensions-34045/SurfaceWrapSolidify/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/SurfaceWrapSolidify/lib/Slicer-5.10/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34045/PyTorch/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/PyTorch/lib/Slicer-5.10/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34045/Photogrammetry/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/Photogrammetry/lib/Slicer-5.10/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34045/MorphoDepot/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/MorphoDepot/lib/Slicer-5.10/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34045/DenseCorrespondenceAnalysis/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/DenseCorrespondenceAnalysis/lib/Slicer-5.10/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34045/Sandbox/lib/Slicer-5.10/qt-loadable-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/Sandbox/lib/Slicer-5.10/qt-loadable-modules</a>, <a href="http://slicer.org/Extensions-34045/Sandbox/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/Sandbox/lib/Slicer-5.10/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34045/SlicerBiomech/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/SlicerBiomech/lib/Slicer-5.10/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34045/ScriptEditor/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/ScriptEditor/lib/Slicer-5.10/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34045/ModelToModelDistance/lib/Slicer-5.10/cli-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/ModelToModelDistance/lib/Slicer-5.10/cli-modules</a>, <a href="http://slicer.org/Extensions-34045/NNInteractive/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/NNInteractive/lib/Slicer-5.10/qt-scripted-modules</a><br>
[INFO][Stream] 25.01.2026 21:32:37 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -<br>
[WARNING][Qt] 25.01.2026 21:32:45 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - libpng warning: iCCP: profile ‘ICC Profile’: ‘CMYK’: invalid ICC profile color space<br>
[DEBUG][Python] 25.01.2026 21:32:46 [Python] (/media/volume/MyData/Slicer/lib/Python/lib/python3.12/site-packages/git/cmd.py:1253) - Popen([‘git’, ‘version’], cwd=/home/exouser, stdin=None, shell=False, universal_newlines=False)<br>
[DEBUG][Python] 25.01.2026 21:32:46 [Python] (/media/volume/MyData/Slicer/lib/Python/lib/python3.12/site-packages/git/cmd.py:1253) - Popen([‘git’, ‘version’], cwd=/home/exouser, stdin=None, shell=False, universal_newlines=False)<br>
[WARNING][Qt] 25.01.2026 21:32:46 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile<br>
[DEBUG][Python] 25.01.2026 21:32:47 [Python] (/media/volume/MyData/Slicer/lib/Slicer-5.10/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 25.01.2026 21:32:47 [Python] (/media/volume/MyData/Slicer/lib/Slicer-5.10/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 25.01.2026 21:32:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Python] 25.01.2026 21:32:48 [Python] (/media/volume/MyData/Slicer/lib/Slicer-5.10/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: FormatMarkups<br>
[INFO][Python] 25.01.2026 21:32:48 [Python] (:3) - Adding SlicerMorph Volume Rendering Presets<br>
[DEBUG][Python] 25.01.2026 21:32:48 [Python] (/media/volume/MyData/Slicer/lib/Slicer-5.10/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SavePyFile<br>
[DEBUG][Qt] 25.01.2026 21:32:48 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - bool qSlicerSubjectHierarchyPluginHandler::registerPlugin(qSlicerSubjectHierarchyAbstractPlugin*) : SubjectHierarchy plugin  “SavePyFile”  is already registered<br>
[DEBUG][Qt] 25.01.2026 21:35:39 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Switch to module:  “SlicerNNInteractive”<br>
[WARNING][Qt] 25.01.2026 21:35:40 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - QLayout::addChildLayout: layout “” already has a parent<br>
[WARNING][Qt] 25.01.2026 21:35:40 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - QLayout::addChildLayout: layout “” already has a parent<br>
[DEBUG][Python] 25.01.2026 21:35:43 [Python] (/media/volume/MyData/Slicer/lib/Python/lib/python3.12/site-packages/urllib3/connectionpool.py:241) - Starting new HTTP connection (1): 0.0.0.0:1527<br>
[DEBUG][Python] 25.01.2026 21:35:43 [Python] (/media/volume/MyData/Slicer/lib/Python/lib/python3.12/site-packages/urllib3/connectionpool.py:544) - <a href="http://0.0.0.0:1527" rel="noopener nofollow ugc">http://0.0.0.0:1527</a> “GET / HTTP/1.1” 404 22<br>
[DEBUG][Python] 25.01.2026 21:35:45 [Python] (/media/volume/MyData/Slicer/lib/Python/lib/python3.12/site-packages/urllib3/connectionpool.py:241) - Starting new HTTP connection (1): 0.0.0.0:1527<br>
[DEBUG][Python] 25.01.2026 21:35:45 [Python] (/media/volume/MyData/Slicer/lib/Python/lib/python3.12/site-packages/urllib3/connectionpool.py:544) - <a href="http://0.0.0.0:1527" rel="noopener nofollow ugc">http://0.0.0.0:1527</a> “GET / HTTP/1.1” 404 22<br>
[ERROR][VTK] 25.01.2026 21:36:16 [vtkMRMLSliceNode (0x1998ce10)] (vtkMRMLSliceNode.cxx:357) - GetSliceOrientationPreset: invalid orientation preset name: Reformat<br>
[ERROR][VTK] 25.01.2026 21:36:16 [vtkMRMLSliceNode (0x19842b90)] (vtkMRMLSliceNode.cxx:357) - GetSliceOrientationPreset: invalid orientation preset name: Reformat<br>
[ERROR][VTK] 25.01.2026 21:36:16 [vtkMRMLSliceNode (0x1984df30)] (vtkMRMLSliceNode.cxx:357) - GetSliceOrientationPreset: invalid orientation preset name: Reformat<br>
[DEBUG][Qt] 25.01.2026 21:36:18 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - “MRB Slicer Data Bundle” Reader has successfully read the file “/media/volume/MyData/Betta 3D Data/Betta-tomi_01_cas-su_69819/2026-01-22-Scene.mrb” “[11.10s]”<br>
[WARNING][Qt] 25.01.2026 21:36:32 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 1 1<br>
[DEBUG][Python] 25.01.2026 21:37:11 [Python] (/media/volume/MyData/Slicer/lib/Python/lib/python3.12/site-packages/urllib3/connectionpool.py:241) - Starting new HTTP connection (1): 0.0.0.0:1527<br>
[DEBUG][Python] 25.01.2026 21:37:18 [Python] (/media/volume/MyData/Slicer/lib/Python/lib/python3.12/site-packages/urllib3/connectionpool.py:544) - <a href="http://0.0.0.0:1527" rel="noopener nofollow ugc">http://0.0.0.0:1527</a> “POST /upload_image HTTP/1.1” 200 15<br>
[DEBUG][Python] 25.01.2026 21:37:28 [Python] (/media/volume/MyData/Slicer/lib/Python/lib/python3.12/site-packages/urllib3/connectionpool.py:241) - Starting new HTTP connection (1): 0.0.0.0:1527<br>
[DEBUG][Python] 25.01.2026 21:37:39 [Python] (/media/volume/MyData/Slicer/lib/Python/lib/python3.12/site-packages/urllib3/connectionpool.py:544) - <a href="http://0.0.0.0:1527" rel="noopener nofollow ugc">http://0.0.0.0:1527</a> “POST /upload_segment HTTP/1.1” 200 15<br>
[DEBUG][Python] 25.01.2026 21:37:39 [Python] (/media/volume/MyData/Slicer/lib/Python/lib/python3.12/site-packages/urllib3/connectionpool.py:241) - Starting new HTTP connection (1): 0.0.0.0:1527<br>
[DEBUG][Python] 25.01.2026 21:37:53 [Python] (/media/volume/MyData/Slicer/lib/Python/lib/python3.12/site-packages/urllib3/connectionpool.py:544) - <a href="http://0.0.0.0:1527" rel="noopener nofollow ugc">http://0.0.0.0:1527</a> “POST /add_point_interaction HTTP/1.1” 200 124096<br>
[DEBUG][Python] 25.01.2026 21:38:24 [Python] (/media/volume/MyData/Slicer/lib/Python/lib/python3.12/site-packages/urllib3/connectionpool.py:241) - Starting new HTTP connection (1): 0.0.0.0:1527<br>
[DEBUG][Python] 25.01.2026 21:38:29 [Python] (/media/volume/MyData/Slicer/lib/Python/lib/python3.12/site-packages/urllib3/connectionpool.py:544) - <a href="http://0.0.0.0:1527" rel="noopener nofollow ugc">http://0.0.0.0:1527</a> “POST /upload_segment HTTP/1.1” 200 15<br>
[DEBUG][Python] 25.01.2026 21:38:29 [Python] (/media/volume/MyData/Slicer/lib/Python/lib/python3.12/site-packages/urllib3/connectionpool.py:241) - Starting new HTTP connection (1): 0.0.0.0:1527<br>
[DEBUG][Python] 25.01.2026 21:38:31 [Python] (/media/volume/MyData/Slicer/lib/Python/lib/python3.12/site-packages/urllib3/connectionpool.py:544) - <a href="http://0.0.0.0:1527" rel="noopener nofollow ugc">http://0.0.0.0:1527</a> “POST /add_point_interaction HTTP/1.1” 200 155758<br>
[DEBUG][Qt] 25.01.2026 22:12:07 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Switch to module:  “Reformat”<br>
[INFO][Stream] 25.01.2026 22:12:10 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - onSliceVisibilityChanged<br>
[INFO][Stream] 25.01.2026 22:12:14 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - onSliceVisibilityChanged<br>
[DEBUG][Qt] 25.01.2026 22:12:16 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Switch to module:  “SlicerNNInteractive”</p>

---

## Post #2 by @muratmaga (2026-01-26 18:28 UTC)

<aside class="quote no-group" data-username="lukejprose" data-post="1" data-topic="45914">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lukejprose/48/81826_2.png" class="avatar"> lukejprose:</div>
<blockquote>
<p>Now, however, the nnInteractive module no longer functions properly. The Configuration tab says that the server is reachable, but when placing the first positive point on one of the slices, it generates a cube that does not render in 3D space.</p>
</blockquote>
</aside>
<p>Looks like NNinteractive got some updates in the last month ( <a href="https://github.com/coendevente/SlicerNNInteractive/commits/main/" class="inline-onebox" rel="noopener nofollow ugc">Commits · coendevente/SlicerNNInteractive · GitHub</a> ) It appears there is a version update, but not clear if any of the code has changed.</p>
<p>To decouple this issue from a potential difference in the dataset, you might want to retry running your older datasets, and see if it still works like it did before, or you are seeing the the cube effect. If you see, probably best to open an issue on their github page documenting the difference.</p>

---

## Post #3 by @lukejprose (2026-01-26 21:00 UTC)

<p>Reopening my previously segmented skulls and adding additional segments results in the nnInteractive module functioning like it did previously.</p>

---

## Post #4 by @lukejprose (2026-01-26 21:38 UTC)

<p>Enabling developer mode and running “Reload and Test” on nnInteractive does not result in any errors, but the cube effect still appears when loading in my latest mrb and placing a positive point.</p>

---

## Post #5 by @muratmaga (2026-01-26 22:27 UTC)

<aside class="quote no-group" data-username="lukejprose" data-post="3" data-topic="45914">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lukejprose/48/81826_2.png" class="avatar"> lukejprose:</div>
<blockquote>
<p>Reopening my previously segmented skulls and adding additional segments results in the nnInteractive module functioning like it did previously.</p>
</blockquote>
</aside>
<p>If you are getting good segmentations with your older dataset, this tells me this is more of a data/workflow issue then a change in NNInteractive (either on the server or the client side).</p>
<p>Is there anything different about this dataset compared to the others (e.g., perhaps the others were 8 bit and this is 16bit?). Is possible for you to share this?</p>
<p>if you put the prompt on other places, do you still see the block? What other prompts types did you use (scribble, ROI, point)?</p>

---

## Post #6 by @lukejprose (2026-01-26 23:28 UTC)

<p>There should be no difference in my mrb files other than the spacing (mm) when first entering the CT data via ImageStacks. The mrb files were created through 3D Slicer on my PC, then ported into the “MyData” folder on MorphoCloud.</p>
<p>The cube effect only seems to occur on my “Maxilla” segment, regardless of where I place the point (the slice and view don’t seem to matter), and seemingly only when it’s the first point placed. Placing more points on this segment can actually render something reasonable in 3D space, although the slices still only show the cube. Trying to place points on other segments produces mixed results. Sometimes it works properly and makes a fully segmented bone, other times it produces nothing. Going from segment to segment hides other bones from the 3D space and from the slices. It seems to behave differently each time I reopen the scene.</p>
<p>I have only been using the point prompts because the others (bounding box, scribble, lasso) either never produce anything, don’t function as well as the points, or the server/slicer would crash.</p>
<p>Additionally, sometimes, when closing and reopening the scene in slicer and restarting the nnInteractive server, selecting “point” generates a markup point rather than a point used for the nnInteractive segmenting. This was happening beforehand, but it can be fixed by reloading.</p>

---

## Post #7 by @lukejprose (2026-01-26 23:39 UTC)

<p>I am curious if creating a new MorphoCloud instance, reestablishing the nnInteractive server, and importing my mrb files again would resolve the issue.</p>

---

## Post #8 by @muratmaga (2026-01-27 00:36 UTC)

<p>Do you have the both failing and successfully running datasets on your MorphoCloud instance? I can hop into and look.</p>

---

## Post #9 by @lukejprose (2026-01-27 00:43 UTC)

<p>I currently have five mrb files in my “MyData” folder. The ones for <em>Betta fusca</em>, <em>Betta</em> <em>picta</em>, and <em>Betta waseri</em> all function properly with nnInteractive. The ones for <em>Betta tomi</em> and <em>Betta pi</em> do not. If you want to open my MorphoCloud instance and check them out, you can. The three skulls I have already finished are saved on my PC.</p>

---

## Post #10 by @muratmaga (2026-01-27 01:03 UTC)

<p>Can’t replicate your issue. The tool is segmenting as it is expected. Though I noticed a few things that might be causing problem and slowing you down.</p>
<ol>
<li>You are using MRBs, which itself is not a problem (beyond slowing you down quite a bit when saving or loading data). But NNInteractive creates these transient markups for following prompts that are saved in the scene. I am not familiar with internal workings of NNInteractive, but probably it doesn’t make much sense to keep this part of the MRB and it might be confusing the prompt. They should probably be deleted each time you load the data into Slicer and then before switching to NNinteractive (try that and see that helps).</li>
<li>I noticed your dataset is 16 bit. But you have only bones and no contrast. 16bit is probably an overkill for that situation. I also noticed that you downsampled data in Z plane (possibly to make the data smaller?). Instead, I would suggest using 8 bit data (which will give you 50% reduction in file size), but keeping the Z resolution intact (as opposed to skipping a slice). The resultant file size will be the same, but you will have more spatial resolution. I wouldn’t make the changes for the ones you already segmented, but consider that option for your new data</li>
<li>Not sure if there are benefits to creating all these empty segments with names. We do support the terminology use case (so you can simply select from a dropdown menu), but it is of course your call.</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f66c11296c8517c1c61bcf40698a312b333e9ef.png" data-download-href="/uploads/short-url/dBXvAD4wNuTU49WYGViEHkoPztR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f66c11296c8517c1c61bcf40698a312b333e9ef.png" alt="image" data-base62-sha1="dBXvAD4wNuTU49WYGViEHkoPztR" width="629" height="252"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">629×252 43.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19c640e2fc8264271d587f96ae99b121b9965886.jpeg" data-download-href="/uploads/short-url/3G0GXj3n9FJ2VkQkYN7uwWNiQPs.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19c640e2fc8264271d587f96ae99b121b9965886_2_369x500.jpeg" alt="image" data-base62-sha1="3G0GXj3n9FJ2VkQkYN7uwWNiQPs" width="369" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19c640e2fc8264271d587f96ae99b121b9965886_2_369x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19c640e2fc8264271d587f96ae99b121b9965886.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19c640e2fc8264271d587f96ae99b121b9965886.jpeg 2x" data-dominant-color="262520"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">506×685 54.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @lukejprose (2026-01-27 02:34 UTC)

<p>I tried deleting the transient markups from nnInteractive in the Data module before switching to the nnInteractive module, then starting the server in the terminal. I made sure to start on my first listed segment, and after placing the first point prompt it now seems to be functioning. Jumping to other segments also does not appear to cause any issue.</p>
<p>Restarting the scene and server then beginning on the “Maxilla” segment no longer results in the cube effect. Instead, nothing happens. It would appear beginning on the first segment is necessary, for whatever reason.</p>
<p>Perhaps the transient markups were confusing the prompt. I do not recall having to delete these for my three mrb files that worked previously, so maybe this was a result of the update for the module.</p>
<p>What I have done previously is create the list of empty segments with names first, as those are the bones I need to segment for my project. When I create my next mrb file, I will instead save it with no segments. I will make the segments once the file is uploaded into MorphoCloud. I will try and go one segment at a time with nnInteractive to see if that is more reliable. I can also try and make it 8 bit instead of 16 bit to see if that also helps. As I recall, I normally save them as 16 bit because the volume rendering does not appear properly when I try 8 bit.</p>

---

## Post #12 by @muratmaga (2026-01-27 03:33 UTC)

<aside class="quote no-group" data-username="lukejprose" data-post="11" data-topic="45914">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lukejprose/48/81826_2.png" class="avatar"> lukejprose:</div>
<blockquote>
<p>As I recall, I normally save them as 16 bit because the volume rendering does not appear properly when I try 8 bit.</p>
</blockquote>
</aside>
<p>These are not calibrated scans, so none of the Slicer presets will work as intended. However you can try 8bit mCT preset that should give you an ok starting point, from which you can use the shift sliders to control it.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f20664dec948a1aef98adc2a673b9fb48f41c88.png" alt="image" data-base62-sha1="fR4pJDQfQDDu7gRPkQjjSrlnvV6" width="92" height="93"></p>

---
