---
topic_id: 7383
title: "Slicer 4 11 Slice View Widget Interactions Intersections Iss"
date: 2019-07-02
url: https://discourse.slicer.org/t/7383
---

# Slicer 4.11 Slice view widget interactions, intersections issue in slicelet

**Topic ID**: 7383
**Date**: 2019-07-02
**URL**: https://discourse.slicer.org/t/slicer-4-11-slice-view-widget-interactions-intersections-issue-in-slicelet/7383

---

## Post #1 by @RMR54 (2019-07-02 17:28 UTC)

<p>This has been observed with Slicer 4.11 nightly. When a slicelet is launched such that the mainWindow is hidden, (the .bat includes --no-main-window argument). I load in a 3D volume, and the red, yellow, and green slice views in the slicelet display this volume node. I can use the slider to go through each slice, but it if I try mouse events, as in moving the mouse wheel, clicking on volume to translate, or zoom in and out, I don’t see any response from the slice widget. Similarly when I try to view slice intersections (<code>SetSliceIntersectionVisiblity(1)</code> ), I don’t observe the slice intersections in any of the slice widgets. Interestingly, I observe the intersections, if I launch the script <em>with</em> the mainWindow displayed as well. Also, if I utilize <code>sliceViewInteractorStyle</code> to setActionEnabled(interactor_style.BrowseSlice, True), I’m able to observe the response to mouse wheel events. Again if I launch the slicelet with --no-main-window, then the same commands, to set BrowseSlice action enabled, don’t evoke a response on mouse wheel events.</p>
<p>I don’t observe this issue in stable release.</p>
<p>A simple way to recreate would be to set up a slicelet using the code <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets" rel="noopener nofollow ugc">provided here</a>, (with layout set as <code>slicer.vtkMRMLLayoutNode.SlicerLayoutFourUpView</code> instead). I ran the slicelet using a .bat with the following lines:<br>
<code>@echo off</code><br>
<code> "C:\Program Files\Slicer 4.11.0\Slicer.exe" --python-code "import MainWidget;" --no-splash --no-main-window --show-python-interactor</code><br>
<code>  pause</code><br>
Upon display of slicelet, I then load in volume using “Load Data” button click. I loaded in .MHA 3D volume, and then tried to evoke response using mouse events in red/yellow/green slice view, but couldn’t get any response. Also at one point, I think I saw these events working, but then as soon as I displayed the volume in red slice onto 3D view, I didn’t get see any response.</p>
<p>I noticed there was <a href="https://github.com/Slicer/Slicer/commit/9b8bc06cd53ab31753fcac456993595b70d73e56" rel="noopener nofollow ugc">a recent commit</a> regarding using widgets for showing slice intersections. Do any updates have to be made for slice widget/layouts in slicelets, in order to view slice intersections and maintain mouse event response?</p>
<hr>
<p>MainWidget.py contained the same code except for the following differences:</p>
<p>Top of file prior to <code>def onModuleSelected(modulename):</code> contains the following lines:</p>
<blockquote>
<p>import qt<br>
import <strong>main</strong><br>
from <strong>main</strong> import qt, slicer</p>
<p>mainWidget = qt.QWidget()<br>
mainWidget.objectName = “qSlicerAppMainWindow”<br>
vlayout = qt.QVBoxLayout()<br>
mainWidget.setLayout(vlayout)</p>
<p>def onModuleSelected(modulename):</p>
</blockquote>
<p>And this line was modified from <code>layoutManager.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutOneUp3DView)</code> to<br>
<code>layoutManager.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutFourUpView)</code></p>

---

## Post #2 by @lassoan (2019-07-03 13:49 UTC)

<p>Slicer has evolved a lot since the concepts of no-main-window-slicelets. Initialization of the main window has become more complicated (due to hi-DPI screens, OpenGL context initialization overrides, interaction widgets, etc.) and it is expected to get even more complex in the future (with multi-monitor support, multi-touch, pen, and Mac trackpad support, etc.). It should be still possible to mimic initialization steps of the Slicer main window in a generic widget in a Python script, but it would be significant effort to maintain consistency.</p>
<p>Instead, I would recommend to use Slicer’s main window but customize it (hide all those parts that you don’t need). This has the advantage that you can flip between “slicelet” and “full Slicer” experience very easily, which helps a lot in development and support.</p>
<p>I’ve added a number of <a href="https://github.com/Slicer/Slicer/commit/21dc780a216f077bdd080fdc64073ccf6b5356e0">helper functions to show/hide user interface elements</a> that you can use to show a single module and a view layout, with any additional user interface elements you need (these functions will be included in Preview releases you download tomorrow or later). You can add these functions in the module widget setup method and then launch Slicer using <code>Slicer.exe --python-code "slicer.util.selectModule('MyModuleName')"</code>. It would not be too difficult to generate application shortcut with an icon (at least on Windows), which would make it very easy for users to start Slicer with the simple GUI.</p>
<p>Here is an example module (not functional yet, but maybe we’ll make it work, if there is enough interest) that uses the newly added functions: <a href="https://github.com/lassoan/SlicerSimpleWorkflows/tree/master/QuickSegment" class="inline-onebox">SlicerSimpleWorkflows/QuickSegment at master · lassoan/SlicerSimpleWorkflows · GitHub</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/604780bb54a8f8f337d5d598985690dbd0cbd52e.jpeg" data-download-href="/uploads/short-url/dJJ1Wr0jn6TEOevtVdjEo5oXuvI.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/604780bb54a8f8f337d5d598985690dbd0cbd52e_2_690x496.jpeg" alt="image" data-base62-sha1="dJJ1Wr0jn6TEOevtVdjEo5oXuvI" width="690" height="496" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/604780bb54a8f8f337d5d598985690dbd0cbd52e_2_690x496.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/604780bb54a8f8f337d5d598985690dbd0cbd52e.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/604780bb54a8f8f337d5d598985690dbd0cbd52e.jpeg 2x" data-dominant-color="9F9F9F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">837×602 145 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>By hitting Ctrl+Shift+b you can switch to the full Slicer GUI:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b83011f0c3e754c21f700309456a18564a7cb0c.png" data-download-href="/uploads/short-url/6cVcP0L4blkoWZHzdYaBRPHbkkI.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b83011f0c3e754c21f700309456a18564a7cb0c_2_690x496.png" alt="image" data-base62-sha1="6cVcP0L4blkoWZHzdYaBRPHbkkI" width="690" height="496" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b83011f0c3e754c21f700309456a18564a7cb0c_2_690x496.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b83011f0c3e754c21f700309456a18564a7cb0c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b83011f0c3e754c21f700309456a18564a7cb0c.png 2x" data-dominant-color="A6A6A5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">837×602 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @pieper (2019-07-03 14:35 UTC)

<p>+1 for QuickSegment.  I think there’s a user base out there who use tools like Seg3D and ITKSnap because they don’t have all the complexity of Slicer, so having a more focused on-ramp could be very useful.</p>

---

## Post #4 by @lassoan (2019-07-03 16:02 UTC)

<p>I’ve updated <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets">Slicelets wiki page for latest Slicer version</a> to reflect the changes in infrastructure and the new way of approaching slicelets and custom applications.</p>
<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="7383" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>+1 for QuickSegment. I think there’s a user base out there who use tools like Seg3D and ITKSnap because they don’t have all the complexity of Slicer, so having a more focused on-ramp could be very useful.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> We can try to improve this QuickSegment module to implement simplified neuro segmentation workflow (at least start with this, then we may fork it if we start to add neuroanatomy specific segmentation features).</p>

---

## Post #5 by @jcfr (2019-07-03 21:55 UTC)

<aside class="quote no-group" data-username="RMR54" data-post="1" data-topic="7383">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/90ced4/48.png" class="avatar"> RMR54:</div>
<blockquote>
<p>Again if I launch the slicelet with --no-main-window, then the same commands, to set BrowseSlice action enabled, don’t evoke a response on mouse wheel events.</p>
</blockquote>
</aside>
<p>To follow up on this, the “problem” was that the layout manager is associated with the <code>qSlicerApplication</code> in <code>qSlicerMainWindowPrivate::setupUi</code> (see <a href="https://github.com/Slicer/Slicer/blob/21dc780a216f077bdd080fdc64073ccf6b5356e0/Base/QTApp/qSlicerMainWindow.cxx#L311">here</a>). By using <code>--no-main-window</code>, this call was skipped and logics were not associated with the <code>vtkMRMLSliceIntersectionWidget</code> object recently introduced.</p>
<p>To address this, replace:</p>
<pre><code class="lang-auto"># layout
layoutManager = slicer.qMRMLLayoutWidget()
layoutManager.setMRMLScene(slicer.mrmlScene)
layoutManager.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutFourUpView)
splitter.addWidget(layoutManager)
</code></pre>
<p>with</p>
<pre data-code-wrap="python"><code class="lang-python"># layout manager
layoutManager = slicer.qSlicerLayoutManager()
slicer.app.setLayoutManager(layoutManager)
layoutManager.setMRMLScene(slicer.mrmlScene)
layoutManager.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutFourUpView)

# layout widget
layoutWidget = slicer.qMRMLLayoutWidget()
splitter.addWidget(layoutWidget)
layoutWidget.setLayoutManager(layoutManager)
</code></pre>
<p>I also updated the older slicelet example <a href="https://www.slicer.org/w/index.php?title=Documentation%2F4.10%2FDevelopers%2FSlicelets&amp;type=revision&amp;diff=61282&amp;oldid=61278">found on the wiki</a>.</p>

---

## Post #6 by @lassoan (2019-07-03 22:53 UTC)

<p>I’ve tried to do something similar and slice view navigation did not work. Anyway, customizing the existing main window from factory-built Slicer is a more robust and flexible solution. The only shortcoming is that the full Slicer GUI flashes for a moment (but this can be solved by using a custom executable name and storing custom the screen layout and startup module in the ini file).</p>

---

## Post #7 by @RMR54 (2019-07-08 12:57 UTC)

<p>Thanks <a class="mention" href="/u/jcfr">@jcfr</a>, the updated code fixed the issues with slice intersections and interactions! <a class="mention" href="/u/lassoan">@lassoan</a>, Thanks for your insight regarding the new approach to slicelets. <a class="mention" href="/u/jcfr">@jcfr</a>’s solution is a good solution for our short-term needs, but implementing new approach would be next in backlog queue, to take advantage of recent updates for customization and support.</p>

---
