# Play back Stl models

**Topic ID**: 8518
**Date**: 2019-09-21
**URL**: https://discourse.slicer.org/t/play-back-stl-models/8518

---

## Post #1 by @Jainey (2019-09-21 14:37 UTC)

<p>Hi all</p>
<p>I m trying to add few stl files (models) and get them to playback as in a small video clip.<br>
I tried the creating sequence and sequence browser modules.</p>
<p>I can create sequence of volumes- and get it to play back.<br>
But it doesn’t play back similarly with models.</p>
<p>Could you kindly explain what I should do,<br>
Thanks<br>
(tried creating new sequence browser for models, it doesn’t add models as expected and  no play back)</p>

---

## Post #2 by @lassoan (2019-09-21 14:58 UTC)

<p>You need to put the models Ina sequence using Sequences module and then create a sequence browser node to show them as an animation in Sequence Browser module.</p>

---

## Post #3 by @Jainey (2019-09-21 15:09 UTC)

<p>Thanks Prof <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>I did do the sequence<br>
But creating a browser was the issue.<br>
I select the first model as my proxy node, then I can add one model only. Even then it does not play back.</p>
<p>Do I have to select the new sequence in the 3 D window. ( Slice vies allows doing that but I dont know about the 3 D window)</p>
<p>Thanks</p>

---

## Post #4 by @Jainey (2019-09-21 15:15 UTC)

<p>It shows as playing back in the browser, but nothing happens in the 3 D window</p>

---

## Post #5 by @lassoan (2019-09-21 15:15 UTC)

<p>No need to select a proxy node, it is created for you automatically when you add your sequence node to the browser node.</p>

---

## Post #6 by @Jainey (2019-09-21 15:16 UTC)

<aside class="quote no-group" data-username="Jainey" data-post="4" data-topic="8518" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a88e57/48.png" class="avatar"> Jainey:</div>
<blockquote>
<p>It shows as playing back in the browser, but nothing happens in the 3 D window</p>
</blockquote>
</aside>
<p>It shows as playing back in the browser, but nothing happens in the 3 D window</p>

---

## Post #7 by @lassoan (2019-09-21 15:16 UTC)

<aside class="quote no-group" data-username="Jainey" data-post="4" data-topic="8518" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a88e57/48.png" class="avatar"> Jainey:</div>
<blockquote>
<p>It shows as playing back in the browser, but nothing happens in the 3 D window</p>
</blockquote>
</aside>
<p>Can you share a screen recording of what you did?</p>

---

## Post #8 by @Jainey (2019-09-21 15:16 UTC)

<p>Yes Prof , 2 mins, Thanks</p>

---

## Post #9 by @Jainey (2019-09-21 15:18 UTC)

<p>Ohh I had to hide the models in the data module, and keep only the sequence open.<br>
Works fine; with all the models open, it does not show the play back<br>
Thanks ever so much for help</p>

---

## Post #10 by @lassoan (2019-09-21 15:24 UTC)

<p>Yes, sure you need to hide or delete the original models (once you copied one in the sequence you don’t need it anymore) side they would occlude the animated model.</p>

---

## Post #11 by @Jainey (2019-09-21 15:30 UTC)

<p>Thank you, One more quick question Prof.  <a class="mention" href="/u/lassoan">@lassoan</a><br>
How do I get two models to play back synchronously<br>
Thanks</p>
<p>(Two bones that are not overlapping)</p>

---

## Post #12 by @lassoan (2019-09-21 15:34 UTC)

<p>You can achieve synchronized playback by adding multiple sequence nodes to the same browser node. That is why we went into the trouble of separating sequence nodes from sequence browser nodes.</p>

---

## Post #13 by @Jainey (2019-09-21 15:58 UTC)

<p>Thanks heaps Prof <a class="mention" href="/u/lassoan">@lassoan</a></p>

---
