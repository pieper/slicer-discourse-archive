# Reload button bug in later nightlies

**Topic ID**: 8625
**Date**: 2019-09-30
**URL**: https://discourse.slicer.org/t/reload-button-bug-in-later-nightlies/8625

---

## Post #1 by @Alex_Vergara (2019-09-30 14:35 UTC)

<p>I have noticed that in the last nightly when I press the reload button it creates extra space between <code>Help &amp; Acknowledgment</code> and the <code>Reload &amp; Test </code> regions. This is valid for all plugins, so it is not plugin specific.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7fd011b0427ae8baba43e74cd6ed2bc724a97f5f.png" alt="image" data-base62-sha1="ieGqkEKJNsshyWS6b1i0ZdQJF5d" width="569" height="261"><br>
each time the <code>Reload</code> is pressed a new “line” is added.</p>
<p>My system is MacOS 10.14.6, latest homebrew slicer-nightly package. This behavior was not been seen in the august package.</p>

---

## Post #2 by @pieper (2019-09-30 15:56 UTC)

<p>I’ve noticed that too - it’s kind of annoying - would be great of someone could look into fixing it.</p>

---

## Post #3 by @lassoan (2019-09-30 16:16 UTC)

<p>I won’t be able to debug this, as the issue does not occur on Windows. <a class="mention" href="/u/pieper">@pieper</a>, could you have a look?</p>

---

## Post #4 by @pieper (2019-09-30 17:23 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="8625">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>could you have a look?</p>
</blockquote>
</aside>
<p>Yes, when I get annoyed enough <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"></p>

---

## Post #5 by @lassoan (2019-10-01 15:33 UTC)

<p>This has come up on my computer, too. I’ve fixed it in rev28526.</p>
<p>The issue was that some QLayoutItems got evaluated as (False) and the loop that supposed to remove all the items stopped at that point. Now all items are retrieved by index first, so we don’t need to evaluate them as Boolean.</p>

---
