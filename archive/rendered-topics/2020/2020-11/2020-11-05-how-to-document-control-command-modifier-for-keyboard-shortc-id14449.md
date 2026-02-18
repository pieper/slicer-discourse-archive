# How to document Control/Command modifier for keyboard shortcuts?

**Topic ID**: 14449
**Date**: 2020-11-05
**URL**: https://discourse.slicer.org/t/how-to-document-control-command-modifier-for-keyboard-shortcuts/14449

---

## Post #1 by @lassoan (2020-11-05 16:21 UTC)

<p>Users seem to have a problem with interpreting our keyboard shortcuts (see for example <a href="https://discourse.slicer.org/t/new-segment-editor-effect-local-threshold/9233/22">here</a>) because Windows and Linux’s “Control” key is mapped to “Command” key on Mac. Qt automatically generates shortcut name based on operating system (Ctrl or ⌘) and we could replace hardcoded “Ctrl” string with platform-specific string in all of our modules (added an <a href="https://github.com/Slicer/Slicer/issues/5295">issue</a> to track this), but what to do with the documentation?</p>
<ul>
<li>Option A: Use “Ctrl” and describe somewhere that on Mac you need to hit ⌘ if you read “Ctrl” in the documentation. Are Mac of multiplatform software got used to this? For example, I see that this is done in the <a href="https://docs.blender.org/manual/en/latest/interface/keymap/introduction.html">Blender manual</a>.</li>
<li>Option B: Replace shortcuts such as <kbd>Ctrl+A</kbd> by <kbd>Ctrl/⌘+A</kbd>. Would this be clear enough for Mac users? Would it be acceptable (wouldn’t it cause confusion) for Windows users?</li>
</ul>

---

## Post #2 by @pieper (2020-11-05 16:49 UTC)

<p>Modern mac keyboards include the text “command” on the modifier key, so I would avoid the “⌘” character. The “⌘” looks very 80s to me and feels like mac pretentiousness (said as a regular mac user for decades).</p>
<p>As long as we are consistent that <code>command</code> on mac always means the same as <code>control</code> on non-mac then I would be comfortable just saying <code>Ctrl-</code> in the documentation and mac users can easily learn it.</p>
<p>My concern would be that at the vtk event level we actually need to use the key marked <code>control</code>.  Are we sure it’s always mapped to <code>command</code> in all uses?</p>

---

## Post #3 by @lassoan (2020-11-05 17:11 UTC)

<p>OK, having to display only Ctrl would simplify things.</p>
<p>In source code it is already just called Ctrl, in both Qt and VTK. There is not even a “Cmd” modifier in VTK (see <a href="https://github.com/Kitware/VTK/blob/5a225156e34b9b1c21d367dee3afe0560677d98c/Interaction/Widgets/vtkEvent.h#L53-L57">here</a>). <a href="https://doc.qt.io/qt-5/qt.html#KeyboardModifier-enum">Qt documentation</a> states that on macOS <code>ControlModifier</code> refers to the “Command” key.</p>

---

## Post #4 by @jamesobutler (2020-11-05 17:48 UTC)

<p>If you only display it in the documentation as “Ctrl”, you’re still going to have the same issue of Apple Mac users reading “Ctrl+A” and actually pressing the “Control” key instead of the “Command” key on their keyboard.</p>

---

## Post #5 by @jamesobutler (2020-11-05 17:57 UTC)

<p><code>⌘+A</code> actually seems appropriate since macOS shows it as such in the menubar area even though the actual key no longer has the “⌘” symbol.</p>

---

## Post #6 by @pieper (2020-11-05 18:09 UTC)

<p>There’s no perfect solution, and mac users need to live with the legacy of single-button mice.  So the ‘control’ key on the mac keyboard together with a left mouse click is equal to the right mouse click on other platforms.  (And shift-left mouse is the middle mouse button.)</p>
<p>So yes, as long as both Qt and VTK both uniformly map <code>control</code> to the <code>command</code> key we just need to find a clean way to communicate that.</p>
<p>The cleanest I have seen is to just have multiple shortcut tables as needed for the platforms you support (e.g. <a href="https://support.google.com/chrome/answer/157179?hl=en&amp;co=GENIE.Platform=Desktop">here’s what Chrome does</a>).  That way you avoid the extra visual distraction of trying to put multiple shortcut options into a single string, particularly when there are multiple modifiers involved. So you get “⌘ + Shift + b” in the mac table and ‘Ctrl + Shift + b’ in the windows/linux table rather than the probably confusing “Ctrl + Shift/Ctrl + Shift b” in a unified table.  So I’d vote for either separate tables or separate columns.</p>

---

## Post #7 by @jamesobutler (2020-11-05 18:13 UTC)

<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="14449">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>So you get “⌘ + Shift + b” in the mac table and ‘Ctrl + Shift + b’ in the windows/linux table rather than the probably confusing “Ctrl + Shift/Ctrl + Shift b” in a unified table. So I’d vote for either separate tables or separate columns.</p>
</blockquote>
</aside>
<p>I second that vote.  That will make it obviously clear to Apple Mac users.</p>

---
