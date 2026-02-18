# ScreenCapture: how to capture "Rock 3D view" animation

**Topic ID**: 5610
**Date**: 2019-02-01
**URL**: https://discourse.slicer.org/t/screencapture-how-to-capture-rock-3d-view-animation/5610

---

## Post #1 by @mangotee (2019-02-01 18:18 UTC)

<p>I am trying to use ScreenCapture to record the 3D view. I have my 3D scene nicely laid out, and I get a very nice animation if I switch on “Rock the 3D view” from the drop-down menu. I would like to record that to disc, but frame by frame, since I have multi-volume renderings activated and that doesn’t run smoothly in real-time (otherwise I could use an external screen grabbing tool). Also, I would like the “rocking” animation recorded only once forth-and back (then I can loop it later e.g. in Powerpoint).</p>
<p>Unfortunately, “Rock 3D view” is not an option in ScreenCapture. I tried to replicate that myself, by recording just a 90 degree Yaw rotation in ScreenCapture, and then I could manually replicate those frames in the inverse order, concatenate both sweeps and thus create a “rocking” motion. However, in my current Slicer version (4.11.0-2019-01-21), ScreenCapture rotates my entire scene, kinda upside down, before the frame-by-frame rotation starts - instead, I wanna start exactly from the view that I get if I click the “R” perspective in the 3D view, so this “hack” is not an option.<br>
Another things I tried is following the code from the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Rotate_the_3D_View" rel="nofollow noopener">ScriptRepository</a>. The line “threeDView.yaw()” does what I need, but only in one direction (a rotation towards the right), and the step size is a bit too large. Could you please let me know how to achieve this using ScreenCapture code and the threeDview.yaw() method?</p>
<p>Come to think of it, this is the third or fourth time that I prefere the “Rock 3D view” animation more than a 360 degree rotation (or other). If it is not too hard for you to integrate this, I would very much welcome to have this as a feature in ScreenCapture. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"> I’m thus changing the category to “Feature request”. Thanks a lot!</p>

---

## Post #2 by @lassoan (2019-02-02 02:14 UTC)

<aside class="quote no-group" data-username="mangotee" data-post="1" data-topic="5610">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/c57346/48.png" class="avatar"> mangotee:</div>
<blockquote>
<p>Unfortunately, “Rock 3D view” is not an option in ScreenCapture</p>
</blockquote>
</aside>
<p>It is available already - see “Advanced” section “Forward-backward” checkbox.</p>

---

## Post #3 by @mangotee (2019-02-02 02:48 UTC)

<p>Awesome! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"> Didn’t notice this feature before. Thanks for the quick response!</p>

---

## Post #4 by @lassoan (2023-03-21 03:08 UTC)



---
