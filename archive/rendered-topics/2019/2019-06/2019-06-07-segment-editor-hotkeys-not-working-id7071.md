---
topic_id: 7071
title: "Segment Editor Hotkeys Not Working"
date: 2019-06-07
url: https://discourse.slicer.org/t/7071
---

# Segment editor Hotkeys Not working

**Topic ID**: 7071
**Date**: 2019-06-07
**URL**: https://discourse.slicer.org/t/segment-editor-hotkeys-not-working/7071

---

## Post #1 by @Amine (2019-06-07 14:54 UTC)

<p>Hotkeys of segment editor for numbers 1,2,… ,9,0  work but the ones with shift +1,2,3…0 (to select effects 11 12… 20  as the documentation says) does not work, tried on slicer 4.10.1 4.10.2 and 4.11 and two different computers, is there something i’m doing wrong or was it disabled? thanks</p>

---

## Post #2 by @lassoan (2019-06-07 16:24 UTC)

<p>I’ve just tried Shift+number shortcuts and they works well for me on Windows. What operating system do you use?</p>
<p>Maybe Shift+number keys are not reliably detected as keyboard shortcuts on all platforms. You can define your custom key combinations by customizing then copying the code below to your <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_to_systematically_execute_custom_python_code_at_startup_.3F" rel="nofollow noopener">.slicerrc.py file</a>:</p>
<pre><code class="lang-auto">editor = slicer.modules.segmenteditor.widgetRepresentation().self().editor

shortcuts = [
    ('Ctrl+b', lambda: editor.setActiveEffectByName('Surface cut')),
    ('Ctrl+n', lambda: editor.setActiveEffectByName('Fast Marching')),
    ]

for (shortcutKey, callback) in shortcuts:
    shortcut = qt.QShortcut(slicer.util.mainWindow())
    shortcut.setKey(qt.QKeySequence(shortcutKey))
    shortcut.connect( 'activated()', callback)
</code></pre>

---

## Post #3 by @Amine (2019-06-07 17:22 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="2" data-topic="7071">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>editor = slicer.modules.segmenteditor.widgetRepresentation().self().editor shortcuts = [ (‘Ctrl+b’, lambda: editor.setActiveEffectByName(‘Surface cut’)), (‘Ctrl+n’, lambda: editor.setActiveEffectByName(‘Fast Marching’)), ] for (shortcutKey, callback) in shortcuts: shortcut = qt.QShortcut(slicer.util.mainWindow()) shortcut.setKey(qt.QKeySequence(shortcutKey)) shortcut.connect( ‘activated()’, callback)</p>
</blockquote>
</aside>
<p>This worked perfectly, only difference being it doesen’t switch back and forth between the effect and “none” when pressed twice like the predefined ones but does the trick, interestingly, shift+letter works fine and ctrl+number as well but shift+ number does not (maybe because it is already assigned to changing the effects)<br>
i tried on both windows 10 and windows 7.<br>
Thanks a lot, that will save me quite some time!!</p>

---

## Post #4 by @lassoan (2019-06-10 18:29 UTC)

<aside class="quote no-group" data-username="Amine" data-post="3" data-topic="7071">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine/48/4844_2.png" class="avatar"> Amine:</div>
<blockquote>
<p>only difference being it doesen’t switch back and forth between the effect and “none” when pressed twice like the predefined ones</p>
</blockquote>
</aside>
<p>You can call a custom function (instead of <code>setActiveEffectByName</code> directly) that checks which effect is active and if the selected effect is already active then it deactivates it.</p>

---
