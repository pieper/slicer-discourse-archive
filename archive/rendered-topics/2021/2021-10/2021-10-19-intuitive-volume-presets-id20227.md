---
topic_id: 20227
title: "Intuitive Volume Presets"
date: 2021-10-19
url: https://discourse.slicer.org/t/20227
---

# Intuitive volume presets

**Topic ID**: 20227
**Date**: 2021-10-19
**URL**: https://discourse.slicer.org/t/intuitive-volume-presets/20227

---

## Post #1 by @rbumm (2021-10-19 10:24 UTC)

<p>Following  <a href="https://github.com/Slicer/Slicer/issues/5951" class="inline-onebox">Make volume presets more accessible · Issue #5951 · Slicer/Slicer · GitHub</a></p>
<p>I implemented the following solution using the right click menu of the slice views:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa7feb4942727abed0ddcb0c912625993b5179ca.jpeg" alt="image" data-base62-sha1="okjeAHMABd8ulofZxN8rKcIx0r8" width="535" height="451"></p>
<p>Is this something you consider useful? If yes I would need to implement the logic and have some questions.</p>

---

## Post #2 by @pieper (2021-10-19 18:31 UTC)

<p>That does look very handy.  Perhaps it should be a pull-aside submenu to save space, which is pretty easy to do with a context menu.</p>

---

## Post #3 by @muratmaga (2021-10-19 19:20 UTC)

<p>I second that request. In fact would be an expansion of the Adjust Window/Level, perhaps?</p>

---

## Post #4 by @lassoan (2021-10-20 05:13 UTC)

<p>Very nice, thanks for working on this.</p>
<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="20227">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Perhaps it should be a pull-aside submenu to save space, which is pretty easy to do with a context menu.</p>
</blockquote>
</aside>
<p>Fully agree that would have been my first suggestion, too.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="20227" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I second that request. In fact would be an expansion of the Adjust Window/Level, perhaps?</p>
</blockquote>
</aside>
<p>It could make sense to add it there, but unfortunately Qt does not allow making checkable an action that has a submenu (that’s why we have “Interaction” checkable action and “Interaction options” submenu in two separate items).</p>
<p>One more thing that would be really cool would be to grab the current foreground/background image from the slice view, and create small icons with the window/level value applied. Rendering the images could take maybe a tenth of a second, so you could do it when the user clicked on the submenu (on <a href="https://doc.qt.io/qt-5/qmenu.html#aboutToShow">aboutToShow</a> signal). You could also make these icons bigger than the default menu icons (maybe 2x larger) so that details can be seen better.</p>

---

## Post #5 by @rbumm (2021-10-20 08:22 UTC)

<p>Thank you all for the feedback.<br>
I´ll try to implement a pull-aside submenu and maybe Icons (a really cool idea) later.<br>
What would be the best practice to involve the actual setPreset() action?<br>
There is a</p>
<pre><code class="lang-auto">void qSlicerScalarVolumeDisplayWidget::setPreset(const QString&amp; presetName)
</code></pre>
<p>in the Volumes module, should I use that and how could I call it from</p>
<pre><code class="lang-auto">qSlicerSubjectHierarchyViewContextMenuPlugin
</code></pre>
<p>?<br>
Thank you.</p>

---

## Post #6 by @rbumm (2021-10-21 10:53 UTC)

<p>This is the prototype for a pull-aside submenu:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b1ec2bd45c34b50e493150a509c99f933e32a69.png" alt="image" data-base62-sha1="69sr0VMFnVVq14RX1ZzvwjllLER" width="465" height="344"></p>

---

## Post #7 by @pieper (2021-10-21 12:13 UTC)

<p>Nice <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=10" title=":+1:" class="emoji" alt=":+1:"></p>
<p>Maybe the menu text could be “Window/level presets” to better match the wording above.</p>

---

## Post #8 by @rbumm (2021-10-21 13:40 UTC)

<p>Ok will do that, but would need a hint on how to actually set the levels from the SLOT function. Should this be done via the Volumes module? I found out how to get a pointer to the “Volumes” module in C++, but did not find suitable “Volumes” methods to invoke.</p>

---

## Post #9 by @pieper (2021-10-21 13:59 UTC)

<p>Unfortunately that feature is <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Volumes/Widgets/qSlicerScalarVolumeDisplayWidget.cxx#L406-L476">hard-coded</a> in the GUI currently.  Best would be to re-factor this feature so it can be re-used, ideally with the option for modules/extensions to register presets like we do for color tables and volume rendering.  Simplest would be to move the guts of the method linked above into <code>vtkSlicerVolumesLogic</code> but there could be other options too (e.g. put it into mrml volume display nodes).</p>

---

## Post #10 by @rbumm (2021-10-21 14:49 UTC)

<aside class="quote no-group" data-username="pieper" data-post="9" data-topic="20227">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>move the guts of the method linked above into <code>vtkSlicerVolumesLogic</code></p>
</blockquote>
</aside>
<p>Thanks Steve, will try that.</p>

---

## Post #11 by @lassoan (2021-10-21 20:12 UTC)

<aside class="quote no-group" data-username="pieper" data-post="9" data-topic="20227">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Best would be to re-factor this feature so it can be re-used, ideally with the option for modules/extensions to register presets like we do for color tables and volume rendering. Simplest would be to move the guts of the method linked above into <code>vtkSlicerVolumesLogic</code></p>
</blockquote>
</aside>
<p>Agreed. Maintaining the list in the Volumes module logic would be a great. For now, the presets can be hardcoded in the logic and we can add API to register new presets later.</p>

---

## Post #12 by @rbumm (2021-10-22 20:56 UTC)

<p>I am slowly getting there.<br>
My main problems are today: How to get a reference to the ScalarVolumeNode loaded in one of the slices and how to detect they are grayscale, because I would not want to offer the color presets in this case.</p>

---

## Post #13 by @pieper (2021-10-22 21:08 UTC)

<p>Since you know which sliceView the menu is on you can use the <code>sliceWidget</code>'s <code>sliceLogic()</code> method and then you can get the vtkMRMLSlicerCompositeNode <a href="https://apidocs.slicer.org/master/classvtkMRMLSliceLogic.html#ab4dfadf75a3b378c8e46c09ab68cfbbc">from the <code>sliceLogic</code></a> and that has the IDs of the nodes for the layers.  You can then use the IDs to get the nodes from the scene and use their <code>IsA</code> methods to check what class they are and only put up the menu items if they are in valid classes.</p>

---
