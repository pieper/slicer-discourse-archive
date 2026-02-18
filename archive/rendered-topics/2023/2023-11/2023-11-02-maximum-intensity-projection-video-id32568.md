# Maximum intensity projection video

**Topic ID**: 32568
**Date**: 2023-11-02
**URL**: https://discourse.slicer.org/t/maximum-intensity-projection-video/32568

---

## Post #1 by @muratmaga (2023-11-02 21:26 UTC)

<p>I don’t use the maximum intensity projection mode very much, but this animation has a really strange artifact. I can’t quite tell whether it is spinning clockwise or counterclockwise after a while (it was supposed to be 360 clockwise rotation). Is this a bug in GPURaycasting or normal with maximum intensity projections.<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68cf3be4d2334ec04046a5b35038ba653d5814cf.mp4">
  </div><p></p>

---

## Post #2 by @pieper (2023-11-02 21:29 UTC)

<p>That’s just the way MIPs work, whatever is brightest is shown so there’s no depth-based occlusion like other volume rendering methods.</p>

---

## Post #3 by @Fernando (2023-11-06 17:01 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a>, just for fun: I don’t think there would by a way to know whether it’s spinning clockwise or counterclockwise. See <a href="https://en.wikipedia.org/wiki/Spinning_dancer" rel="noopener nofollow ugc">Spinning dancer - Wikipedia</a>.</p>

---

## Post #4 by @muratmaga (2023-11-06 17:15 UTC)

<p>Fun, but it is one of those illusions that doesn’t work for me. For me it is a very clear clockwise spinning with no ambiguity. Yet, MIP above keeps going back and forth being CW and CCW very smoothly.</p>

---

## Post #5 by @mikebind (2023-11-06 21:13 UTC)

<p>The spinning dancer image series is indeterminate in rotation direction, just like a MIP spin. The basis of the illusion is that it is impossible to tell whether you are looking at the front of the dancer or the back when all you have is a silhouette and no depth information. When it appears to you that the toes are pointed towards you, it is equally consistent with the image data that they are pointed away and the back of the leg is towards you. Identically, for a maximum intensity projection, all you see is the maximum intensity value along a ray; it is impossible to know which side of the ray you are looking from.</p>
<p>For the dancer, I see the counterclockwise rotation most easily and have trouble seeing the reverse spin.  However, with the guided variants, visible in the “Left and right edge cue variant, with original” section on the Wikipedia page (you have to click the “show” link to see it), I can easily see either rotation by focusing on either the left image or the right, and whichever I am looking at, the middle image (the original illusion) seems to be spinning the same direction.</p>
<p>Once I’ve looked at both variants for a while, I can force a switch between them by focusing on just the lower foot and imagining that it is either a right foot or a left foot, and within a few spins the perceived direction of spin reverses.</p>
<p>If you most easily see a clockwise spin, here is the variant which guides you to the opposite view:<br>
<a href="https://en.wikipedia.org/wiki/Spinning_dancer#/media/File:Right_spinning_dancer.gif">counter-clockwise spinning dancer gif</a></p>
<p>Thanks for the fun link <a class="mention" href="/u/fernando">@Fernando</a>!</p>

---

## Post #6 by @Fernando (2023-11-08 11:20 UTC)

<p>That’s the answer I would’ve liked to have given. Thank you, <a class="mention" href="/u/mikebind">@mikebind</a>!</p>

---
