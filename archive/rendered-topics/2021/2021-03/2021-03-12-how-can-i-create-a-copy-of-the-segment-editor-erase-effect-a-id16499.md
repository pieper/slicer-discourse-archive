# How can I create a copy of the segment editor erase effect and rename it?

**Topic ID**: 16499
**Date**: 2021-03-12
**URL**: https://discourse.slicer.org/t/how-can-i-create-a-copy-of-the-segment-editor-erase-effect-and-rename-it/16499

---

## Post #1 by @akshay_pillai (2021-03-12 17:04 UTC)

<p>Operating system:windows 10<br>
Slicer version:4.11</p>
<p>I want to create a copy of the erase effect in segment editor. I want to rename it as eraser or something like that, but I want both erase and eraser(which is a copy of erase) to exist in the segment editor module.<br>
How can I do that?</p>

---

## Post #2 by @lassoan (2021-03-14 15:48 UTC)

<p>Since Erase effect is implemented in C++, you can only change its name by building Slicer and adding a C++ loadable module that registers a variant of the Erase effect.</p>
<p>Alternatively, you can create a new scripted effect, based on AbstractScriptedSegmentEditorPaintEffect.py, which reproduces the same behavior as the Erase effect - similarly to SegmentEditorSmoothingEffect (just simpler, because you don’t need to do any smoothing).</p>
<p>In the future, we’ll probably make displayed name of the Segment Editor effect translatable to different languages, which may make it easier to rename the effect on the GUI.</p>

---

## Post #3 by @akshay_pillai (2021-03-15 19:36 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>  I’m going to try the alternative method first as I haven’t built slicer. Where can I find AbstractScriptedSegmentEditorPaintEffect.py?</p>

---

## Post #4 by @akshay_pillai (2021-03-16 14:58 UTC)

<p>I found AbstractScriptedSegmentEditorPaintEffect.py. But I wanted to know what you meant by creating a new scripted effect?</p>

---

## Post #5 by @lassoan (2021-03-16 15:51 UTC)

<p>You could do something similar as SegmentEditorSmoothingEffect, which is based on AbstractScriptedSegmentEditorPaintEffect to allow users to paint in views.</p>

---

## Post #6 by @akshay_pillai (2021-03-26 15:37 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="16499">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>mething similar as SegmentEditorSmoothingEffect, which is based on AbstractScriptedSegmentEditorPaintEffect to</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> I created a copy of SegmentEditorSmoothingEffect and changed its name. But this does not create a copy of the effect in slicer. Where do I need to add the files to make it appear in Slicer? I have edited the init files to include the copy as well.</p>
<p>I am also getting an error like this: File “C:\Users\pilht4\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Slicer-4.11\qt-scripted-modules\SegmentEditorEffects_<em>init</em>_.py”, line 48, in registerEffects<br>
instance.self().register()<br>
AttributeError: ‘NoneType’ object has no attribute ‘register’</p>

---

## Post #7 by @lassoan (2021-03-29 13:41 UTC)

<p>You can use Extension Wizard module to create<br>
a new Segment Editor effect with a chosen name. It takes care of proper registration of the effect.</p>

---
