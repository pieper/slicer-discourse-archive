# No intensity change at 4.11

**Topic ID**: 16722
**Date**: 2021-03-23
**URL**: https://discourse.slicer.org/t/no-intensity-change-at-4-11/16722

---

## Post #1 by @siaeleni (2021-03-23 14:46 UTC)

<p>Hello,</p>
<p>I have realized that when I load dicom files on Slicer 4.11+ I cannot change the intensity on the 2D Views, while on 4.10 this can change, is it a normal behavior?</p>
<p>Thanks</p>

---

## Post #2 by @cpinter (2021-03-23 15:20 UTC)

<p>If by intensity you mean window/level (or brightness/contrast), then these topics help:</p>
<aside class="quote quote-modified" data-post="1" data-topic="6817">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/joostjm/48/1091_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/adjust-window-level-is-not-working-nightly-release-4-11-0/6817">Adjust Window Level is not working (nightly release 4.11.0)</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    In the latest nigthly release (13-05-2019, windows), adjusting window/level by left-click + dragging is not working anymore. It is still possible to adjust window/level through the Volumes module however. 
Furthermore, when checking the interactorstyle, it shows that AdjustWindowLevelForeground and AdjustWindowLevelBackground are enabled. 
&gt;&gt;&gt; interactorStyle = slicer.app.layoutManager().sliceWidget('Red').sliceView().sliceViewInteractorStyle()
&gt;&gt;&gt; interactorStyle.GetActionEnabled(interactorStyl…
  </blockquote>
</aside>
<aside class="quote" data-post="1" data-topic="6923">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ecgt/48/17012_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/i-cannot-change-the-window-center-level-with-left-click/6923">I cannot change the window/center level with left click</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Problem report for Slicer 4.11.0-2019-05-01 win-amd64: Change window level does not work
  </blockquote>
</aside>

<p>As you see many questions already have an answer on tis forum, so trying with search a little bit will probably get you the answer.</p>

---

## Post #3 by @siaeleni (2021-03-23 15:26 UTC)

<p>Thank you and I am sorry that I asked again, but I was using different words for this.</p>

---
