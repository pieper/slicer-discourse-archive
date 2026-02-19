---
topic_id: 18960
title: "Grow From Seeds"
date: 2021-07-28
url: https://discourse.slicer.org/t/18960
---

# Grow from seeds

**Topic ID**: 18960
**Date**: 2021-07-28
**URL**: https://discourse.slicer.org/t/grow-from-seeds/18960

---

## Post #1 by @Ron (2021-07-28 21:26 UTC)

<p>Dear Andras</p>
<p>The fix for grow from seeds works very well as well as the additional segmentation script, thank you.<br>
The only issue is that the 3D rendering does not appear to automatically update.  Does so if manually forced to refresh.  I am using 4.13.0-2021-07-15 r30048 / 550f033.</p>
<p>Ron</p>

---

## Post #2 by @pieper (2021-07-28 21:28 UTC)

<p><a class="mention" href="/u/Ron">@Ron</a> I believe <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> just fixed this.  Can you try the latest nightly?</p>

---

## Post #3 by @Ron (2021-07-28 21:37 UTC)

<p>Steve</p>
<p>version 4.13.0 revision 30080 built 2021-07-28?</p>
<p>Quick Q. In our discussion, you mentioned that a second segmentation can be carried local to a specific label. Tried to do it in slicer by limiting threshold to a named mask #, but the change appears to be global. Is there an example how it is done. Ron</p>

---

## Post #4 by @pieper (2021-07-28 23:20 UTC)

<aside class="quote no-group" data-username="Ron" data-post="3" data-topic="18960">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ron/48/10835_2.png" class="avatar"> Ron:</div>
<blockquote>
<p>version 4.13.0 revision 30080 built 2021-07-28?</p>
</blockquote>
</aside>
<p>I think so but haven’t checked.  Maybe <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> can confirm.</p>
<p>Did you select the editable area like this?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d64c619cfd26f8cb376d41e6f675b26d418d8e2e.png" alt="image" data-base62-sha1="uzLP8LiHf84CWQHq78MkIUtarKu" width="595" height="103"></p>

---

## Post #5 by @Sunderlandkyl (2021-07-29 14:01 UTC)

<aside class="quote no-group quote-modified" data-username="pieper" data-post="4" data-topic="18960">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<aside class="quote no-group" data-username="Ron" data-post="3" data-topic="18960">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ron/48/10835_2.png" class="avatar"> Ron:</div>
<blockquote>
<p>version 4.13.0 revision 30080 built 2021-07-28?</p>
</blockquote>
</aside>
<p>I think so but haven’t checked. Maybe <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> can confirm.</p>
</blockquote>
</aside>
<p>Yes, it should be included in the 2021-07-28 installer.</p>

---

## Post #6 by @Ron (2021-07-29 15:54 UTC)

<p>Yes, it is working very nicely. Makes a considerable difference. Thank you <a href="https://mail.bidmc.org/u/sunderlandkyl" rel="noopener nofollow ugc">@Sunderlandkyl</a>.</p>

---
