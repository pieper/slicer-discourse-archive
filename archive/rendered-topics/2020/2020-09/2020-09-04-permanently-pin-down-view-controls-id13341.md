---
topic_id: 13341
title: "Permanently Pin Down View Controls"
date: 2020-09-04
url: https://discourse.slicer.org/t/13341
---

# Permanently pin down view controls

**Topic ID**: 13341
**Date**: 2020-09-04
**URL**: https://discourse.slicer.org/t/permanently-pin-down-view-controls/13341

---

## Post #1 by @EvanMcNabb (2020-09-04 16:08 UTC)

<p>I was wondering if there is a way to have the “pin button” above the view (where you can select Axial/Sagittal/Coronal and the volume) permanently set.</p>
<p>I find myself using this panel quite often and wish that panel would stay in view without having to hover the mouse over pin button first. I don’t need the rest of the controls though (the double arrow button).</p>
<p>I want to add a listener function to my .slicerrc file that checks whether the views changed, and if so, set some python command to “press” the pin button. Or is there some easier method?</p>
<p>Thank you.</p>

---

## Post #2 by @pieper (2020-09-04 16:36 UTC)

<p>Yes, probably a python script would be the best workaround for that.</p>
<p>But you might also look at the View Controllers module.  You could make a hotkey to bring that up as an alternative to using the pins.</p>

---

## Post #3 by @lassoan (2020-09-04 17:38 UTC)

<aside class="quote no-group" data-username="EvanMcNabb" data-post="1" data-topic="13341">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/evanmcnabb/48/66159_2.png" class="avatar"> EvanMcNabb:</div>
<blockquote>
<p>I find myself using this panel quite often and wish that panel would stay in view without having to hover the mouse over pin button first</p>
</blockquote>
</aside>
<p>Which part do you find that you use often?</p>
<p>We have been adding most commonly needed features to Data module’s Subject hierarchy tab.</p>
<p>For selecting what image is displayed in which view, I’m thinking about enabling drag-and-drop, as it has become a quite common trend in medical image viewers. As a test, I’ve already implemented it for images and labelmap (and it would be easy to enable this for all node types):</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe2082945c3c56be4ba7b9f03a120ac5d0ad796d.gif" alt="2020-09-04-13-31-57" data-base62-sha1="Ag6VEXJnoCszEB9StvJwnk2XNh3" width="640" height="390"></p>

---

## Post #4 by @EvanMcNabb (2020-09-04 19:13 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="13341">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Which part do you find that you use often?</p>
</blockquote>
</aside>
<p>Hi thank you both for replying.</p>
<p>I click the pin so that orientation/volume panel stays open. It sounds simple, but you have to hover over the pin which is quite small in screen area in order to bring the panel down. And if you move the mouse too far it’ll disappear quickly. It just interrupts my workflow so I wanted to add a listener to ensure no matter which layout is open, all the views have the pin button permanently pressed.</p>
<p>I could have the View Controller modules open, but I’m usually using other modules to segment/mask/register, etc.</p>
<p>I know how to add listener/observer functions, but I don’t know the object tree well enough to do this.</p>
<p>I’m wondering if the python console can interact with the view control buttons? My thinking would be to loop over all the views in the layout, check if the pin button is pressed, and if not, “click” it.</p>
<p>Thanks so much.</p>

---

## Post #5 by @pieper (2020-09-04 19:56 UTC)

<aside class="quote no-group" data-username="EvanMcNabb" data-post="4" data-topic="13341">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/evanmcnabb/48/66159_2.png" class="avatar"> EvanMcNabb:</div>
<blockquote>
<p>I’m wondering if the python console can interact with the view control buttons? My thinking would be to loop over all the views in the layout, check if the pin button is pressed, and if not, “click” it.</p>
</blockquote>
</aside>
<p>Sure, that’s very possible.  You just need to search around in the code to find the widgets and look at what method activate the thing you need.</p>
<p>I agree the little pin button with the hover behavior can be annoying.  If your goal is to easily move between layouts you might try the script below or some variant in .slicerrc.py.</p>
<pre><code class="lang-auto">if qt.QSysInfo().productType() == 'osx':
    controlKey = "Meta"
else:
    controlKey = "Ctrl"

shortcuts = [
    (controlKey+'+b', lambda: slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutOneUpRedSliceView)),
    (controlKey+'+n', lambda: slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutOneUpYellowSliceView)),
    (controlKey+'+m', lambda: slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutOneUpGreenSliceView)),
    (controlKey+'+,', lambda: slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutFourUpView)),
    ]

for (shortcutKey, callback) in shortcuts:
    shortcut = qt.QShortcut(slicer.util.mainWindow())
    shortcut.setKey(qt.QKeySequence(shortcutKey))
    if not shortcut.connect( 'activated()', callback):
        print(f"Couldn't set up {shortcutKey}")
</code></pre>

---

## Post #6 by @lassoan (2020-09-04 20:21 UTC)

<aside class="quote no-group" data-username="EvanMcNabb" data-post="4" data-topic="13341">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/evanmcnabb/48/66159_2.png" class="avatar"> EvanMcNabb:</div>
<blockquote>
<p>I click the pin so that orientation/volume panel stays open. It sounds simple, but you have to hover over the pin which is quite small in screen area in order to bring the panel down. And if you move the mouse too far it’ll disappear quickly. It just interrupts my workflow</p>
</blockquote>
</aside>
<p>Can you tell about your workflow? Why do you need to keep adjusting view orientations?</p>
<p>We have modules designed for specific tasks, such as comparing volumes or register volumes. Maybe a more convenient solution would be to use these modules and improve them as needed.</p>
<p>You can also use “View controllers” module - it gives you access to all the view controls at one place, without taking away space from the viewers:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8fe9a7f0469b7a67deb8cac352e857222b5eeb1.png" data-download-href="/uploads/short-url/qoxl58IjjkaDjvZoj3xg4Tpn8eR.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8fe9a7f0469b7a67deb8cac352e857222b5eeb1_2_492x500.png" alt="image" data-base62-sha1="qoxl58IjjkaDjvZoj3xg4Tpn8eR" width="492" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8fe9a7f0469b7a67deb8cac352e857222b5eeb1_2_492x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8fe9a7f0469b7a67deb8cac352e857222b5eeb1_2_738x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8fe9a7f0469b7a67deb8cac352e857222b5eeb1_2_984x1000.png 2x" data-dominant-color="484742"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1081×1098 55.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Note that <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_widgets_in_view_controller_bars">you can also add more buttons to slice view controls</a>, so for example you could add an Ax, Sag, Cor button right next to the slice offset slider and so you could switch between slice orientations without having to sacrifice any space in the viewers.</p>
<p>We could also add some slice view property adjustments (such as orientation) to right-click menu.</p>

---

## Post #7 by @muratmaga (2020-09-05 04:07 UTC)

<p>This interesting. Does it mean that slice viewers would stay empty until a node is dragged into them? Are you planning the same for the 3D viewer as well (otherwise I think it will be a bit weird).</p>

---

## Post #8 by @lassoan (2020-09-05 04:12 UTC)

<p>Drag-and-drop to viewers could be just an additional way of making display nodes in selected views (or view groups). This is how most clinical image viewers allow specifying what is shown where.</p>
<p>This could be enabled for all views (slice, 3d, table, plot) and all node types.</p>

---
