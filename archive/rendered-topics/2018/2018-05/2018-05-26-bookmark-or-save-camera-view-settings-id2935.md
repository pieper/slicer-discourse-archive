# "Bookmark" or save camera view settings

**Topic ID**: 2935
**Date**: 2018-05-26
**URL**: https://discourse.slicer.org/t/bookmark-or-save-camera-view-settings/2935

---

## Post #1 by @hherhold (2018-05-26 10:46 UTC)

<p>Hey guys,</p>
<p>Is it possible to “bookmark” or save scene camera view settings from the 3D view? I have a specimen where I’d like to show people a few representative views. It would useful to be able to have a list of views to recall.</p>
<p>If this doesn’t exist, I’m happy to implement it (with some guidance) - I’m assuming it would be fetching the view parameters from the scene camera and saving them somewhere, and then setting them when requested.</p>
<p>At any rate, any assistance would be greatly appreciated.</p>
<p>Thanks!!</p>
<p>-Holister</p>

---

## Post #2 by @hherhold (2018-05-26 11:08 UTC)

<p>OK, I just found “Scene views”, which appears to do almost exactly what I want, except with two issues:</p>
<ol>
<li>
<p>Selecting the “Scene views” module from the Modules dropdown crashes slicer. The error I get is:</p>
<p>qSlicerSceneViewsModuleWidgetPrivate::setupUi - Capture link not implemented with Qt5<br>
qSlicerSceneViewsModuleWidgetPrivate::setupUi - Restore scroll bar position not implemented with Qt5<br>
Received signal 11 SEGV_MAPERR 000000000028<br>
[0x00010ce13f5c]<br>
[0x00010ce13e05]<br>
[0x7fffb0cdcb3a]<br>
[0x000000000000]<br>
[0x0001113ead63]<br>
Segmentation fault: 11</p>
</li>
<li>
<p>Restoring the saved scene view (using buttons on toolbar, which works) restores everything but the zoom setting. Simple workaround is to just re-zoom in, but it would be nice to save everything.</p>
</li>
</ol>
<p>Any ideas on the crash?</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #3 by @pieper (2018-05-26 13:29 UTC)

<ol>
<li>Yes, the SceneView module is broken due to changes related to Qt5 and QtWebEngine (<a href="https://www.slicer.org/wiki/Documentation/Labs/Qt5-and-VTK8#Slicer">see here</a>)</li>
</ol>
<p>Overall, there is <a href="https://discourse.slicer.org/t/what-scene-views-are-supposed-to-do/497/16">some debate</a> about what to do with SceneViews - the current design isn’t working but nobody has come up with something useful but simpler.</p>
<ol start="2">
<li>
<a class="mention" href="/u/hherhold">@hherhold</a> if you want to just save and restore camera views that would be a nicely defined project (some people use the term “lookmarks” for saved views).   The existing SceneViews tries to be more ambitious and save a lot of state and that sometimes causes problems in save/restore.</li>
</ol>

---

## Post #4 by @lassoan (2018-05-26 16:12 UTC)

<p>We should be able to restore working state of 4.8 by changing it to use Qt widgets instead of a web widget.</p>
<p>I agree that scene views wanted to do too much, but I think saving only camera positions would be too limited. Maybe we could take a stab of simplifying scene views at the upcoming project week?</p>

---

## Post #5 by @cpinter (2018-05-28 13:57 UTC)

<p>We have discussed this previously and came up witha limited scope for scene views, see <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer50#SceneViews">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer50#SceneViews</a></p>
<p>A discussion at the project week would be very useful. By agreeing on a concrete future design we could make a big step forward and then it would only be a matter of implementation.</p>

---

## Post #6 by @hherhold (2018-05-28 14:02 UTC)

<p>It sounds like there’s a desire for something more than “lookmarks” - I’ll hold off and look for what comes out of the project week. I’m willing to help out on the implementation side if you’re looking for a pair of hands - my knowledge of the internals of Slicer (for the moment) is such that I would not be much use on the design side.</p>

---

## Post #7 by @pieper (2018-05-28 18:21 UTC)

<p>As I recall the motivation for using the QtWebKit code in the SceneViews module had to do with some specific layout requirements of the image and title/subtitle of the SceneView info.  The layout was pretty trivial in HTML but had been a bottleneck in Qt (i think the original design used a list model/view).  We can take a fresh look at making a QWidget implementation of the SceneView module (the exact layout isn’t very important).  E.g. it could just be a list with optional popup for the image or whatever is straightforward to implement.</p>
<p><a class="mention" href="/u/hherhold">@hherhold</a> the code <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/SceneViews/GUI/qSlicerSceneViewsModuleWidget.cxx#L123-L249">is here</a> if you want to have a look.</p>
<p>Longer term, yes, getting a concrete design would be great.</p>

---
