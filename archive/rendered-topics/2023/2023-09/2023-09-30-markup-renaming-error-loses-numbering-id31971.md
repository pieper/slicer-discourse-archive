# Markup renaming error loses numbering

**Topic ID**: 31971
**Date**: 2023-09-30
**URL**: https://discourse.slicer.org/t/markup-renaming-error-loses-numbering/31971

---

## Post #1 by @slopezal (2023-09-30 04:20 UTC)

<p>Hi, I’m running into some sort of bug when renaming a point list. If I start off with a point list that is named using the scheme 7_1-%d and then I try to remove the underscore to make it 7-%d, the whole numbering scheme is lost and every point is renamed to 7-1.<br>
(This is repeatable and generalize-able, if I start with points named 7_3-%d, trying to remove the underscore changes every point to 7-3)<br>
I assume this is a problem with underscores confusing the renaming process, but I can’t figure out how to stop it from happening.</p>

---

## Post #2 by @lassoan (2023-09-30 04:25 UTC)

<p>I cannot reproduce this. Which Slicer version are you using? Could you record a screen capture video as you reproduce the unexpected behavior and share it here?</p>

---

## Post #3 by @slopezal (2023-09-30 13:37 UTC)

<p>Slicer version: 5.0.3 r30893 / 7ea0f43</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/add93d08e9d980c61779080a22493d338c788196.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/add93d08e9d980c61779080a22493d338c788196.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/add93d08e9d980c61779080a22493d338c788196.mp4</a>
    </video>
  </div><p></p>

---

## Post #4 by @muratmaga (2023-09-30 14:23 UTC)

<p>Please try with latest stake 5.4…0</p>

---

## Post #5 by @lassoan (2023-09-30 14:45 UTC)

<p>I see, this explains why you have trouble with the rename. When the name contains multiple numbers then the first number is assumed to be part of the name and the second number is assumed to be the point number. This heuristics works well for most cases, as Slicer generates unique node names from a prefix by adding <code>_{counter}</code> to it.</p>
<p>In your case, the second number was <code>1</code> for all the control points, therefore <code>%d</code> got replaced by <code>1</code> for all your points.</p>
<p>One solution could be to not use a number as node name (e.g., use <code>P7</code> instead of <code>7</code>). I would recommend this because this would make the points easier to identify anyway.</p>
<p>Another solution could be to set the node name before you start placing points</p>
<p>You could also write a 2-3-line code snippet that renames the points any way you need.</p>
<p>We could tune the renaming heuristics to match your current needs, but it may not be desirable for others. We could add more options to configure the behavior but the GUI of thr module is already way too complex, so it would be better to avoid adding more to it.</p>

---

## Post #6 by @muratmaga (2023-09-30 17:02 UTC)

<p>I wonder if it would be feasible to copy/paste the labels from somewhere. I know we can copy and paste whole control points, but this would be restricted to labels column only.</p>
<p><a class="mention" href="/u/slopezal">@slopezal</a> you would completely avoid the issue of renaming your landmarks, if you use a markups template with your proper landmark numbers/IDS. it only take a minute or two create blank template, and it will also provide you other safety checks such as not messing up the ordering of the landmarks, or accidentally skipping some.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="SUouhaIMWXw" data-video-title="Landmark Templates in 3D Slicer" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=SUouhaIMWXw" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/SUouhaIMWXw/maxresdefault.jpg" title="Landmark Templates in 3D Slicer" width="" height="">
  </a>
</div>


---

## Post #7 by @slopezal (2023-10-02 15:57 UTC)

<p>Ah thank you! I was using the first number as a name and the second number to index which replicate it was, but I am pretty sure I will be able to work around this now that I understand what is happening.</p>

---
