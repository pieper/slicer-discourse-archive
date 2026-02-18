# Only show base color

**Topic ID**: 22509
**Date**: 2022-03-15
**URL**: https://discourse.slicer.org/t/only-show-base-color/22509

---

## Post #1 by @qiqi5210 (2022-03-15 03:19 UTC)

<p>Hello,everyone.When I click on the red area<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c06c5bd7fea8e57607fdcc731b5c610ae435c419.png" alt="click" data-base62-sha1="rsfPzR765zIp0NnAoMdnQXWwqwN" width="347" height="131"><br>
I want to hide the window below<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/4257f537829c8b2d31728b120f4f0e8bd149acbe.png" alt="slicer" data-base62-sha1="9sTXDFYuIVm8HakQUv4tcYGDqRo" width="314" height="383"><br>
Keep the select color widget<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4ceec74bed9061807aa896d4ec8d6cee9e759ab.png" alt="select color" data-base62-sha1="nvXDuN98HRTJ31RyhMyQVIPcxrd" width="582" height="417"><br>
I have read this article<br>
[<a href="https://discourse.slicer.org/t/segment-editor-reduce-the-number-of-mouse-clicks-to-set-basic-colour-for-segment/20236/3" class="inline-onebox">Segment Editor: reduce the number of mouse clicks to set basic colour for segment - #3 by lassoan</a>]<br>
I change  in Application settings → Application startup script → add ctk.ctkColorDialog().setDefaultTab(0)` to the end of the displayed startup script file.<br>
But it didn’t work.I hope you can help me. Thank you！</p>

---

## Post #2 by @lassoan (2022-03-15 03:35 UTC)

<aside class="quote no-group" data-username="qiqi5210" data-post="1" data-topic="22509">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/qiqi5210/48/15920_2.png" class="avatar"> qiqi5210:</div>
<blockquote>
<p>I change in Application settings → Application startup script → add ctk.ctkColorDialog().setDefaultTab(0)` to the end of the displayed startup script file.<br>
But it didn’t work.I hope you can help me. Thank you！</p>
</blockquote>
</aside>
<p>This feature is only available in recent Slicer Preview Releases.</p>

---
