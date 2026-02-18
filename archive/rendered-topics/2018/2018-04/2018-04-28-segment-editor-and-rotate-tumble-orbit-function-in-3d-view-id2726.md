# Segment Editor and rotate/tumble/orbit function in 3D view

**Topic ID**: 2726
**Date**: 2018-04-28
**URL**: https://discourse.slicer.org/t/segment-editor-and-rotate-tumble-orbit-function-in-3d-view/2726

---

## Post #1 by @nslizer (2018-04-28 15:10 UTC)

<p>I’ve just returned to using Slicer for 3D modelling. The new segment concept and its editor are amazing!</p>
<p>But how to rotate/tumble/orbit the 3D view in editing mode? The left-button is taken over by the paint function. I couldn’t find any modifiers, say CTRL, that’ll give it back.</p>
<p>Would my Connexion 3D mouse solve the problem if I could connect it?</p>
<p>The “None” effect does not work well in practice either because it messes up the “spacebar” mode switch between “paint” and “erase”. (And my fingers can’t find keys “0”, “1”, … easily with tablet use.)</p>

---

## Post #2 by @lassoan (2018-04-28 15:39 UTC)

<p>You can use space bar to toggle between paint/none effect but if you use space bar already for toggle between paint/erase then you can use arrow keys to rotate the view. I don’t know how we could use Shift/Ctrl modifiers, since they already mapped to other actions. You can get a wireless numeric keypad to switch between effects. What devices do you use?</p>

---

## Post #3 by @hherhold (2018-04-28 15:43 UTC)

<p>I have a 6 button mouse that I set up to do numbers for often used functions. I also use a Wacom tablet and set up the stylus buttons for paint and erase. I use a left hand mouse and stylus in my right hand, so I do segmentations without taking my hands off the mouse or stylus. Goes very quickly.</p>

---

## Post #4 by @nslizer (2018-04-28 19:51 UTC)

<p><a class="mention" href="/u/hherhold">@hherhold</a> Thanks for extra mouse tip, so you rotate 3D view by switching to the “None” mode, move pen, and then switch back to previous mode?</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks, the arrow keys would help in 3D and Numeric keypad might be an idea.</p>
<p>Still I’d like to use mouse for rotate – without mode switching.  So if you I don’t mind back to 3D view question  in the segment editor: here Ctrl-Left-button in 3D is bound to “Paint” (if in Paint mode) as far as I can tell, but you say it’s bound to an other action?</p>
<p>Also, the Alt-modifier seems to be entirely unused in all of 3D Slicer? If Alt-Left-button did “Rotate”, then that’ll help too although I’d vote for Ctrl!</p>
<p>My second mode of working has an issue that boils down to the very same problem. I’d like to use my Wacom tablet with standard modifier keys to effortlessly switch between Paint, Erase, Pan, Scroll, Zoom and Rotate.</p>
<p>The following already works out-of-the-box: Paint (pen in Paint mode), Scroll (touch ring),  Zoom (pen side button).  An easy tablet setting (middle-click assigned to Wacom “Pan” button) makes Pan work! And, so does Switching between Paint and Erase (Spacebar assigned to Wacom button).</p>
<p>All done for one thing: there’s no 3D Slicer equivalent to map to for Rotate! Here again, I’d love it to be just Ctrl-left button.</p>
<p>So in other words, Ctrl-left button bound to Rotate would solve both mouse and tablet issues – neither should involve mode switching for rotating I think.</p>
<p>As for your question about devices: I have</p>
<ul>
<li>keyboard,</li>
<li>3-button mouse,</li>
<li>Wacom tablet (with 7 buttons and dial), and</li>
<li>3D Spacenavigator (3dconnexion).</li>
</ul>
<p>I haven’t configured the Spacenavigator although I gather it’s possible though your PLUS software?</p>

---

## Post #5 by @lassoan (2018-04-29 03:15 UTC)

<p>Ctrl + Left-Click-and-drag rotates the 3D view around the view plane normal. It would be complicated to temporarily re-map that to regular regulation.</p>
<p>Would it help if you had the option to only paint/erase in slice views? Then you could rotate 3D views as usual.</p>

---

## Post #6 by @pieper (2018-04-29 13:14 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="2726">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Would it help if you had the option to only paint/erase in slice views? Then you could rotate 3D views as usual.</p>
</blockquote>
</aside>
<p>This is what I was going to suggest.  Painting in the 3D view is cool, but often is not needed, while 3D viewing is always needed.</p>

---

## Post #7 by @hherhold (2018-04-29 20:51 UTC)

<p><a class="mention" href="/u/nslizer">@nslizer</a> - Yes, that’s pretty much what I do. I don’t have a terribly fast graphics card so I usually don’t have a 3D view active while segmenting, but when I do, I make sure I switch to “None” before rotating.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> - Andras, that’s an excellent idea - I almost never use paint in 3D, so having an option to disable it would be extremely useful.</p>

---

## Post #8 by @lassoan (2018-04-29 21:38 UTC)

<p>OK, I’ll make 3D paint optional.</p>
<p>Note that since recent performance improvements (implemented in Slicer core a few weeks ago), if you turn off surface smoothing then update of 3D representation should be almost instantaneous, regardless of how good GPU you have.</p>

---

## Post #9 by @lassoan (2018-04-30 12:45 UTC)

<p>I’ve made painting/erasing in 3D view optional. It should be available in nightly builds that you download tomorrow or later. I’ve also added “smudge” option to Paint effect: auto-select segment at click position, which should help in minimizing switching between segments when adjusting boundaries between them. I’ve also added option to erase all segments (not just the selected segment) using Erase effect.</p>

---

## Post #10 by @nslizer (2018-04-30 16:28 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> Optional is good, the best would be without sub-modes via more UI states (each UI state=“bad”, but that’s hard to live by) . BTW, as far as I can tell, the “rotate in view plane” functionality in 3D viewer is not documented: <a href="https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/MouseandKeyboardShortcuts" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/MouseandKeyboardShortcuts</a><br>
Also, it seems that Left-Ctrl, Right-Ctrl, and Right-Alt (on Windows) all map to this function in 3D mode. Perhaps use Alt only or introduce a orbit-mode  toggle (as is most common in 3D apps as AFAIK)? Then you’d free up Ctrl for “active manipulation” such a painting where another UI sub-state is painful.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a>  That’s amazing you were able to change this so quick, thanks!</p>
<p>Another somewhat related issue is that Ctrl-left-button doesn’t actually view-plane-rotate the 3D view if the cursor happens to trace back to something paintable (in Paint mode) – instead paint is applied and that doesn’t seem right.  (That’s why I didn’t understand your initial comment, btw, the cursor has to be moved to empty space, which then, enables normal rotate, too.)</p>
<p>The recent upgrades to the 3D rendering completely transforms the usability of the tool in my (limited) experience. With a graphics card, smoothing runs extremely quickly. 3D Paint is really useful here actually.</p>

---

## Post #11 by @lassoan (2018-04-30 18:11 UTC)

<aside class="quote no-group" data-username="nslizer" data-post="10" data-topic="2726">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/ba9def/48.png" class="avatar"> nslizer:</div>
<blockquote>
<p>Also, it seems that Left-Ctrl, Right-Ctrl, and Right-Alt (on Windows) all map to this function in 3D mode.</p>
</blockquote>
</aside>
<p>Currently, Paint/Erase responds to Left-click with no Shift modified. Ctrl modifier is ignored. We could map some variant of the Paint effect to Ctrl+Left-click, or keep default 3D view behavior of Ctrl+Left-click.</p>
<p>Unfortunately, it is very hard to make small changes to keyboard shortcuts, as they would lead to a cascade of changes, ending up re-mapping a lot of shortcuts. It may be possible, but then we should come up with a complete re-map of all shortcuts that is accepted by most users.</p>

---

## Post #12 by @nslizer (2018-04-30 21:30 UTC)

<blockquote>
<p>Currently, Paint/Erase responds to Left-click with no Shift modified. Ctrl modifier is ignored. We could map some variant of the Paint effect to Ctrl+Left-click, or keep default 3D view behavior of Ctrl+Left-click.</p>
</blockquote>
<p>Yes, my 2 cents is that Paint effect (Erase and Scissors, too) should go with Ctrl-Left-click as simplest fix overriding rotate-in-view-plane in order to paint. I see where you’re coming from: I know that there are voxel editors where click-and-drag has two meanings depending on whether your cursor maps to the object you’re constructing, but that strategy works best for little things with no need for close-up inspection.</p>
<p>Personally, I love Meshmixer’s default mode: it works well with zoom, panning, and rotate, and select/deselect-painting and allows to investigate triangles in insanely complicated models (say from 3D slicer!) – with no UI sub-states (and only one modifier with three-button mouse: Ctrl for deselect-painting with left-key).</p>
<blockquote>
<p>Unfortunately, it is very hard to make small changes to keyboard shortcuts, as they would lead to a cascade of changes, ending up re-mapping a lot of shortcuts. It may be possible, but then we should come up with a complete re-map of all shortcuts that is accepted by most users.</p>
</blockquote>
<p>That’s big <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> But I see the general problem that your modifiers have been mostly consumed by one-button mice and radiology convenience. Using left-click for any thing other than selecting and applying the current tool tends to lead to trouble. And you’re building a voxel editor on top, that’s quite a tangle!</p>

---

## Post #13 by @pieper (2018-04-30 23:15 UTC)

<p>Let’s not forget we also have the mac laptop issue to deal with, where we need to use the modifiers to handle pan and zoom so we need to carefully test any extra use of modifiers.</p>

---

## Post #14 by @nslizer (2018-05-02 19:06 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/lassoan">@lassoan</a> Impressive development pipeline and process you’ve in place: I just downloaded the latest version, 4.9, in May 1 build, and voila, it’s frustration-free to inspect the segmentations in 3D view while painting/erasing! Thx a thousand.</p>

---

## Post #15 by @lassoan (2018-05-02 22:20 UTC)

<p>It’s great to hear this. We plan to review/update keyboard shortcuts and mouse gestures and will take your recommendations into account.</p>

---
