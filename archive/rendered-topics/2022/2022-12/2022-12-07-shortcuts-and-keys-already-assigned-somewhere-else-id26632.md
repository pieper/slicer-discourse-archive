# Shortcuts and keys already assigned somewhere else?

**Topic ID**: 26632
**Date**: 2022-12-07
**URL**: https://discourse.slicer.org/t/shortcuts-and-keys-already-assigned-somewhere-else/26632

---

## Post #1 by @hherhold (2022-12-07 17:11 UTC)

<p>Having odd issues with keyboard shortcuts (again). I have code set up like in the script repository:</p>
<pre><code>shortcuts = [
  ('p', lambda: hh_select_paint()),
  ('[', lambda: hh_select_erase()),
  (']', lambda: hh_select_scissors()),
  ('\\', lambda: hh_select_islands()),
  (';', lambda: hh_place_fiducial()),
  ('s', lambda: toggleSphereBrush()),
  ('`', lambda: cycleEffect(1)),
  ('~', lambda: cycleEffect(-1)),
  ('Ctrl+m', lambda: slicer.util.selectModule('Models')),
  ('S', lambda: slicer.util.selectModule('SegmentEditor')),
  ('U', lambda: slicer.util.selectModule('Markups')),
  ('D', lambda: slicer.util.selectModule('Data')),
]

for (shortcutKey, callback) in shortcuts:
    shortcut = qt.QShortcut(slicer.util.mainWindow())
    shortcut.setKey(qt.QKeySequence(shortcutKey))
    shortcut.connect( 'activated()', callback)
</code></pre>
<p>I’ve put debug prints in my various functions to do stuff (<code>toggleSphereBrush()</code>) and they don’t get executed, but interestingly, the backtick and tilde shortcuts <em>do</em> work.</p>
<p>If I reassign backtick or tilde to my functions, my functions get called.</p>
<p>Are those other keys getting caught somewhere else?</p>
<p>THANKS!!</p>

---

## Post #2 by @muratmaga (2022-12-07 17:29 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="1" data-topic="26632">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<pre><code class="lang-auto">'`', lambda: cycleEffect(1)),
  ('~', lambda: cycleEffect(-1)),
</code></pre>
</blockquote>
</aside>
<p>These are from SlicerMorphPrefs (Application Settings-&gt;Preferences-&gt;SlicerMorph). You may want to disable that first for your tests.</p>

---

## Post #3 by @hherhold (2022-12-07 17:41 UTC)

<p>Hey Murat! Hope you’re well.</p>
<p>Yep, that’s why I used them for testing - I know they work for SlicerMorph! Just wondering why the others don’t work.</p>
<p>Thanks!!</p>

---

## Post #4 by @lassoan (2022-12-07 22:57 UTC)

<p>Most of these shortcuts work for me (except the <code>S</code> and <code>s</code>, which you broke for yourself by redefining).</p>
<p>Try these:</p>
<pre><code class="lang-python">shortcuts = [
  ('p', lambda: print('pressed: p')),
  ('z', lambda: print('pressed: z')),
  ('q', lambda: print('pressed: q')),
  ('f', lambda: print('pressed: f')),
  ('[', lambda: print('pressed: [')),
  (']', lambda: print('pressed: ]')),
  ('\\', lambda: print('pressed: \\')),
  (';', lambda: print('pressed: ;')),
  ('`', lambda: print('pressed: `')),
  ('~', lambda: print('pressed: ~')),
  ('Ctrl+m', lambda: print('pressed: Ctrl-m')),
  ('S', lambda: print('pressed: S')),
  ('O', lambda: print('pressed: O')),
  ('U', lambda: print('pressed: U')),
  ('D', lambda: print('pressed: D')),
]

for (shortcutKey, callback) in shortcuts:
    shortcut = qt.QShortcut(slicer.util.mainWindow())
    shortcut.setKey(qt.QKeySequence(shortcutKey))
    shortcut.connect( 'activated()', callback)
</code></pre>
<p>If you or someone else adds a shortcut with the same key sequence then effectively breaks all actions, as the shortcut will no longer emit <code>activated()</code> signal but <code>activatedAmbiguously()</code>.</p>
<p>Unfortunately, I don’t know an easy way to determine where each shortcut comes from where, other than search in the source code of all installed extensions for <code>shortcut</code>.</p>
<p>Extensions should not install any keyboard shortcut by default (without explicitly approved by the user). Also, if any shortcut is added then a meaningful <code>objectName</code> should be set, for example containing the name of the extension and module, to make it easier to detect and resolve conflicts by turning off irrelevant shortcuts.</p>

---

## Post #5 by @hherhold (2022-12-08 00:54 UTC)

<p>Gaaaah, I should have realized ‘S’ and ‘s’ could be interpreted by Qt as the same keypress - I probably should have used <code>Qt::Shift</code> modifiers or whatever they are to be more explicit.</p>
<p>Thanks!</p>

---
