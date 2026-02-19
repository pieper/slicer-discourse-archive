---
topic_id: 11906
title: "Customize Keyboard Shortcuts From Script Repository Not Work"
date: 2020-06-06
url: https://discourse.slicer.org/t/11906
---

# "Customize keyboard shortcuts" from script repository not working?

**Topic ID**: 11906
**Date**: 2020-06-06
**URL**: https://discourse.slicer.org/t/customize-keyboard-shortcuts-from-script-repository-not-working/11906

---

## Post #1 by @hherhold (2020-06-06 19:12 UTC)

<p>Okay, I’m <em>positive</em> I’m doing something wrong here, but I can’t figure out what it is. I’m trying to make a new keyboard shortcut based on the code from the script repository, but I can’t even get the example working. The code is loading and running fine from my .slicerrc.py but it is not working.</p>

---

## Post #2 by @hherhold (2020-06-06 19:13 UTC)

<p>Oops, hit post to quickly.</p>
<p>I get a “True” back when connecting the signal/slot, so everything appears happy, but the event never goes.</p>
<p>Any ideas? Thanks!!</p>
<p>-Hollister</p>

---

## Post #3 by @lassoan (2020-06-06 19:29 UTC)

<p>Can you post the code?</p>

---

## Post #4 by @hherhold (2020-06-06 19:32 UTC)

<p>Sure, it’s straight from the script repository.</p>
<pre><code>shortcuts = [
  ('Ctrl+b', lambda: slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutOneUpRedSliceView)),
  ('Ctrl+n', lambda: slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutOneUpYellowSliceView)),
  ('Ctrl+m', lambda: slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutOneUpGreenSliceView)),
  ('Ctrl+,', lambda: slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutFourUpView))
  ]

for (shortcutKey, callback) in shortcuts:
    shortcut = qt.QShortcut(slicer.util.mainWindow())
    shortcut.setKey(qt.QKeySequence(shortcutKey))
    shortcut.connect( 'activated()', callback)</code></pre>

---

## Post #5 by @lassoan (2020-06-06 19:37 UTC)

<p>This works well for me on recent Slicer-4.11 on Windows. Maybe there is something wrong with your .slicerrc.py file, so try to copy-paste it into the Python console.</p>

---

## Post #6 by @hherhold (2020-06-06 19:39 UTC)

<p>Hmm. Wonder if it’s a Mac thing. I did exactly that (copy paste into python console) and it doesn’t work.</p>
<p>I’ll try other key combos using actual Qt_Key:: values.</p>

---

## Post #7 by @lassoan (2020-06-06 19:43 UTC)

<p>On Mac, probably you need to write “Cmd” instead of “Ctrl”.</p>

---

## Post #8 by @hherhold (2020-06-06 19:49 UTC)

<p>Okay, this is odd.</p>
<p>You’re right on the mark with Cmd vs Ctrl.  Cmd plus those keys works. But if I change the key text to ‘Cmd+b’, for example, nothing works.</p>
<p>So basically Ctrl is Cmd on a Mac for this. Is this a PyQt thing? In my experience Qt is pretty good at this type of cross-platform thing, but I’ve only ever done Qt programming from C++.</p>
<p>Thanks!!</p>
<p>-Hollister</p>

---

## Post #9 by @lassoan (2020-06-06 20:00 UTC)

<p>It is a Macintosh keyboard thing that Ctrl is called Cmd. The best that Qt can do about this is to abstract it away:</p>
<blockquote>
<p>Note: On Mac OS X, references to “Ctrl”, Qt::CTRL, Qt::Control and Qt::ControlModifier correspond to the Command keys on the Macintosh keyboard, and references to “Meta”, Qt::META, Qt::Meta and Qt::MetaModifier correspond to the Control keys. Developers on Mac OS X can use the same shortcut descriptions across all platforms, and their applications will automatically work as expected on Mac OS X.</p>
</blockquote>

---

## Post #10 by @hherhold (2020-06-06 20:11 UTC)

<p>Ugh. Annoying. And Meta should be Meta, as in the old LISP machines and Sun keyboards. Oh well.</p>
<p>Thanks!!!</p>

---
