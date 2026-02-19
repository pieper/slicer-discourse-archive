---
topic_id: 35303
title: "Segment Editor Shortcurts Does Not Work"
date: 2024-04-05
url: https://discourse.slicer.org/t/35303
---

# Segment Editor shortcurts does not work

**Topic ID**: 35303
**Date**: 2024-04-05
**URL**: https://discourse.slicer.org/t/segment-editor-shortcurts-does-not-work/35303

---

## Post #1 by @SANTIAGO_PENDON_MING (2024-04-05 07:35 UTC)

<p>Hi to everyone <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Today I’m looking for the command to activate and deactivate the segment Editor shortcuts using Python code. The shortcuts sometimes works correctly and then, in the same conditions if I open again the segmentation they doesn’t work anymore.</p>
<p>Can I anybody explain me how this works, and if it’s possible to activate and deactivate it?</p>
<p>Thanks a lot.</p>

---

## Post #2 by @lassoan (2024-04-06 15:17 UTC)

<p>Management of shortcuts in Qt is quite complex and fragile. Most often shortcuts break when you are trying to assign a shortcut multiple times. Make sure that after calling <code>installKeyboardShortcuts</code> you always call <code>uninstallKeyboardShortcuts</code>.</p>

---

## Post #3 by @Suhaim (2025-12-17 06:53 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="35303">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Make sure that after calling <code>installKeyboardShortcuts</code> you always call <code>uninstallKeyboardShortcuts</code>.</p>
</blockquote>
</aside>
<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>, could you please elaborate what you meant here?</p>
<p>Like <a class="mention" href="/u/santiago_pendon_ming">@SANTIAGO_PENDON_MING</a> tried, I was also disabling the shortcut “Ctrl+Z” with custom logic using -</p>
<pre><code class="lang-auto">def disableShortcut(sequence: str):
    shortcut = qt.QShortcut(slicer.util.mainWindow())
    shortcut.setKey(qt.QKeySequence(sequence))
    shortcut.connect("activated()", lambda: None)
</code></pre>
<p>After disabling the shortcut once, if I restart the application with the calls to this function removed( therefore no more “Ctrl+z” shortcut override), I am not able to use the shortcut for the segment editor. Like <a class="mention" href="/u/santiago_pendon_ming">@SANTIAGO_PENDON_MING</a> mentioned, the shortcut doesn’t work anymore. Would you happen to know why?</p>
<p>Found this in another post as well :-</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="26632">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/shortcuts-and-keys-already-assigned-somewhere-else/26632/4">Shortcuts and keys already assigned somewhere else?</a></div>
<blockquote>
<p>If you or someone else adds a shortcut with the same key sequence then effectively breaks all actions, as the shortcut will no longer emit <code>activated()</code> signal but <code>activatedAmbiguously()</code>.</p>
<p>Unfortunately, I don’t know an easy way to determine where each shortcut comes from where, other than search in the source code of all installed extensions for <code>shortcut</code>.</p>
<p>Extensions should not install any keyboard shortcut by default (without explicitly approved by the user). Also, if any shortcut is added then a meaningful <code>objectName</code> should be set, for example containing the name of the extension and module, to make it easier to detect and resolve conflicts by turning off irrelevant shortcuts.</p>
</blockquote>
</aside>
<p>So are you suggesting that I <strong>should not disable “Ctrl+z“ based on custom logic</strong>?</p>

---
