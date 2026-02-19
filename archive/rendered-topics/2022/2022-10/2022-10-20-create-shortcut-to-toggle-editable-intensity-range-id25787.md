---
topic_id: 25787
title: "Create Shortcut To Toggle Editable Intensity Range"
date: 2022-10-20
url: https://discourse.slicer.org/t/25787
---

# Create shortcut to toggle editable intensity range

**Topic ID**: 25787
**Date**: 2022-10-20
**URL**: https://discourse.slicer.org/t/create-shortcut-to-toggle-editable-intensity-range/25787

---

## Post #1 by @Alex_Shen (2022-10-20 00:56 UTC)

<p>Hi,<br>
I’m currently working on customising a few things to make segmentation in slicer faster.<br>
I want to customize a shortcut to toggle paint with an editable intensity range. e.g. when I press ALT while I paint, it will enable the intensity rage, and release to disable it.<br>
I find a helpful script about how to customize the shortcuts as follows:<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-keyboard-shortcut-for-toggling-sphere-brush-for-paint-and-erase-effects" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-keyboard-shortcut-for-toggling-sphere-brush-for-paint-and-erase-effects</a></p>
<p>The question is how may I find the parameter name for Editable intensity range tick box?  Will be appreciated if someone can point it out. Also will be more interested to know how you will find it out from either codebase or documents.</p>
<p>Thanks ahead.</p>

---

## Post #2 by @hherhold (2022-10-20 01:11 UTC)

<p>Not exactly what you were asking as far as how to find the parameter to set, but ‘i’ toggles intensity range on and off.</p>
<p>The holding of a key down to enable/disable is an interesting idea. I’m not sure if there are other tools that use that kind of modifier yet, but I think it should be doable?</p>

---

## Post #3 by @hherhold (2022-10-20 01:18 UTC)

<p>This is actually implemented in the C++ code, qMRMLSegmentEditorWidget.cxx, starting on line 3187.</p>
<p>(Sooner or later I gotta learn how to put pointers to the code in here…)</p>

---

## Post #4 by @Alex_Shen (2022-10-20 01:19 UTC)

<p>Thanks for pointing that out, it fits 90% of what I want to do.<br>
Didn’t find it in the shortcuts document here:<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html</a><br>
Think there are similar features like hold shift while dragging will pan the view etc.</p>

---

## Post #5 by @hherhold (2022-10-20 01:22 UTC)

<p>Shift will also center all slices to the pointed to location, useful if you’re pointing at something in 3D.</p>
<p>I <em>highly</em> recommend getting a true 3-button mouse; middle button while dragging pans the view.</p>
<p>Also, if you’re about to do a lot of manual segmentation, a tablet may be a good investment. I have a Wacom intuos pro size medium with many miles on it. You can program the buttons on the pen and tablet to do various commands (paint, erase, islands, etc) and it can speed tasks up considerably.</p>

---

## Post #6 by @Alex_Shen (2022-10-20 01:40 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="3" data-topic="25787">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>This is actually implemented in the C++ code, qMRMLSegmentEditorWidget.cxx, starting on line 3187.</p>
</blockquote>
</aside>
<p>Thanks for pointing that out. Is there a way to define it using python API (purely because I know python only)? The script offers a way to set a shortcut via qt.Qshortcut, and gave an example of pointing and changing the parameter “BrushSphere”. Wondering how may I find the feature parameter name, e.g. editable intensity range, to replace “BrushSphere” here?</p>

---

## Post #7 by @hherhold (2022-10-20 10:47 UTC)

<p>I’m not sure - I seem to remember that at the time (this was a little while ago…) this parameter was not exposed to python, but this might have changed. <a class="mention" href="/u/lassoan">@lassoan</a>, is this still the case or can you reach this now in python?</p>

---
