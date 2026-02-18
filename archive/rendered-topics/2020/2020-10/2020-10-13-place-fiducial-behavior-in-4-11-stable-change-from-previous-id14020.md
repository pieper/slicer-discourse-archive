# Place fiducial behavior in 4.11 stable - change from previous version

**Topic ID**: 14020
**Date**: 2020-10-13
**URL**: https://discourse.slicer.org/t/place-fiducial-behavior-in-4-11-stable-change-from-previous-version/14020

---

## Post #1 by @hherhold (2020-10-13 20:02 UTC)

<p>I did a quick search through past posts on fiducials (wow, there are a lot) but didn’t see this mentioned - apologies if I missed something.</p>
<p>In previous versions (as recent as 9-1 nightly, for example), after placing a fiducial, Slicer would automatically switch back to the “arrow” tool for rotating &amp; translating, etc. In the latest stable, however, the program remains in “placing fiducial” mode. Is this intentional? Is there a way to toggle this behavior?</p>
<p>Thanks!</p>

---

## Post #2 by @jamesobutler (2020-10-13 20:56 UTC)

<p>It sounds like you have “Persistent” enabled for markups. This is not a setting that persists across Slicer instances unless you had something in your slicerrc to do this.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c753da83ed907af60b408737e964b9c0fde77940.png" alt="image" data-base62-sha1="srkFFsDhSziRONML4CWoQDk0Wcg" width="163" height="226"></p>
<p>Do you by chance have SlicerMorph installed? <a class="mention" href="/u/muratmaga">@muratmaga</a> If someone types the letter “t” for changing a segmentation name or volume node name etc is this toggling persistent markups mode without a users knowledge?</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/blob/c0e367968d8a012f7fc3f16c5dceb98042d036ab/MorphPreferences/Resources/SlicerMorphRC.py#L119">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph/blob/c0e367968d8a012f7fc3f16c5dceb98042d036ab/MorphPreferences/Resources/SlicerMorphRC.py#L119" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/SlicerMorph/blob/c0e367968d8a012f7fc3f16c5dceb98042d036ab/MorphPreferences/Resources/SlicerMorphRC.py#L119" target="_blank" rel="noopener nofollow ugc">SlicerMorph/SlicerMorph/blob/c0e367968d8a012f7fc3f16c5dceb98042d036ab/MorphPreferences/Resources/SlicerMorphRC.py#L119</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="109" style="counter-reset: li-counter 108 ;">
          <li># setup shortcut keys</li>
          <li>
          </li>
<li>shortcuts = [</li>
          <li>    ('`', cycleEffectForward),</li>
          <li>    ('~', cycleEffectBackward),</li>
          <li>    ('b', setLayoutOneUpRedSliceView),</li>
          <li>    ('n', setLayoutOneUpYellowSliceView),</li>
          <li>    ('m', setLayoutOneUpGreenSliceView),</li>
          <li>    (',', setLayoutFourUpView),</li>
          <li>    ('p', enterPlaceFiducial),</li>
          <li class="selected">    ('t', togglePlaceModePersistence),</li>
          <li>    ('l', toggleMarkupLocks),</li>
          <li>    ]</li>
          <li>
          </li>
<li>for (shortcutKey, callback) in shortcuts:</li>
          <li>    shortcut = qt.QShortcut(slicer.util.mainWindow())</li>
          <li>    shortcut.setKey(qt.QKeySequence(shortcutKey))</li>
          <li>    if not shortcut.connect( 'activated()', callback):</li>
          <li>        print(f"Couldn't set up {shortcutKey}")</li>
          <li>logging.info(f"  {len(shortcuts)} keyboard shortcuts installed")</li>
          <li>
      </li>
</ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @hherhold (2020-10-13 20:58 UTC)

<p>I do have SlicerMorph installed! This now makes total sense. Thanks!!!</p>

---

## Post #4 by @muratmaga (2020-10-13 21:20 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="3" data-topic="14020" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>I do have SlicerMorph installed! This now makes total sense. Thanks!!!</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/hherhold">@hherhold</a>, if you go to Application Settings-&gt;SlicerMorph you can uncheck to use SlicerMorph defaults.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="14020">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>If someone types the letter “t” for changing a segmentation name or volume node name etc is this toggling persistent markups mode without a users knowledge?</p>
</blockquote>
</aside>
<p>I think we should document registered key shortcuts used in the core Slicer. I tried to look it up, but I couldn’t find a master document that has this. Are you aware of anything like that. That persistent toggle is a requested feature, but doesn’t have to be the ‘t’ key.</p>

---

## Post #5 by @lassoan (2020-10-13 22:04 UTC)

<p>Slicer core keyboard shortcuts are listed here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#mouse-keyboard-shortcuts">https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#mouse-keyboard-shortcuts</a></p>
<p>In addition to these, modules may specify additional shortcuts, which are described in each module documentation.</p>
<p>We could probably improve the documentation, but in the future we will be able to generate shortcut list dynamically, by querying displayable managers and module widgets.</p>

---
