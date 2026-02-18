# Customize keyboard shortcuts in Slicer?

**Topic ID**: 32891
**Date**: 2023-11-18
**URL**: https://discourse.slicer.org/t/customize-keyboard-shortcuts-in-slicer/32891

---

## Post #1 by @mvergnat (2023-11-18 11:40 UTC)

<p>Hello!<br>
dear all,</p>
<p>I would like to change few keyboard shortcuts:</p>
<p>I work on an echo loop and I am doing somme segmentation.<br>
to well identify structures, I often need to navigate quickly in the frames.</p>
<p>the normal schortcut to navigate through the frames is<br>
Ctrl+shift+arrow left/right<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55a7cf976f8e62100824c5fb790f4411753e944a.jpeg" data-download-href="/uploads/short-url/cdK7kkFqlCakXfnITkrDgTVWwuC.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55a7cf976f8e62100824c5fb790f4411753e944a_2_690x385.jpeg" alt="image" data-base62-sha1="cdK7kkFqlCakXfnITkrDgTVWwuC" width="690" height="385" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55a7cf976f8e62100824c5fb790f4411753e944a_2_690x385.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55a7cf976f8e62100824c5fb790f4411753e944a_2_1035x577.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55a7cf976f8e62100824c5fb790f4411753e944a_2_1380x770.jpeg 2x" data-dominant-color="7B7B7A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1392×777 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>may i change this shortcut to simply arrow left/right (to work with one hand and leave a hand for mouse).</p>
<p>I saw a 2020 post on this:</p><aside class="quote" data-post="1" data-topic="14814">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aitekk/48/7890_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-set-or-customize-keyboard-shortcuts-in-slicer/14814">How to set or customize keyboard shortcuts in Slicer?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I have some problems about using Slicer. First, how to set or customize keyboard shortcuts in Slicer? This will make slicer more in line with my habits. In addition, I found that when there are many segments in the scene, the display of all view windows is delayed, especially when using tools such as Paint or Draw effect. How to avoid it? I will be appreciate for the help, thanks!
  </blockquote>
</aside>
<p><strong>BUT:</strong><br>
the link quoted is not anymore functional…<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_keyboard_shortcuts" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_keyboard_shortcuts</a><br>
<strong>AND:</strong><br>
if we could find a solution <strong>without Pithon programmimg</strong> would be better…I am not a programmer…</p>
<p>Many thx for help!!<br>
mathieu</p>

---

## Post #2 by @lassoan (2023-11-20 17:04 UTC)

<p>The Slicer script repository has moved to readthedocs: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#keyboard-shortcuts-and-mouse-gestures" class="inline-onebox">Script repository — 3D Slicer documentation</a></p>
<p>Arrow keys are used for so many things that it may be rarely remain unassigned, so I would recommend to use other keys. For example, you can use the <kbd>q</kbd> and <kbd>w</kbd> keys to move to previous/next frame:</p>
<pre data-code-wrap="python"><code class="lang-python"># Load some sequence
# (this is just for testing, it is not needed if a sequence is already in the scene)
import SampleData
sequenceNode = SampleData.SampleDataLogic().downloadSample("CTPCardioSeq")


# Define functions to step to the next/previous item

def stepNext():
    sequenceBrowserNode = slicer.util.getModule('Sequences').toolBar().activeBrowserNode()
    sequenceBrowserNode.SelectNextItem(1)

def stepPrevious():
    sequenceBrowserNode = slicer.util.getModule('Sequences').toolBar().activeBrowserNode()
    sequenceBrowserNode.SelectNextItem(-1)

# Create keyboard shortcuts for the functions

shortcutNext = qt.QShortcut(slicer.util.mainWindow())
shortcutNext.setKey(qt.QKeySequence('w'))
shortcutNext.connect('activated()', stepNext)

shortcutPrevious = qt.QShortcut(slicer.util.mainWindow())
shortcutPrevious.setKey(qt.QKeySequence('q'))
shortcutPrevious.connect('activated()', stepPrevious)
</code></pre>

---

## Post #3 by @lalamax3d (2024-01-31 08:41 UTC)

<p>thanks for idea., i want to ask, is it possible to assign keyboard shortcut to default modules ( Data / Volumes / Models / Transforms … )<br>
keys like 1,2,3… (alpha) by any chance, in my case, this will really help speed up</p>

---
