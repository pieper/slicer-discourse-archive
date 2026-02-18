# Ability to grab/selects fiducials depedent on zoom level

**Topic ID**: 6989
**Date**: 2019-06-01
**URL**: https://discourse.slicer.org/t/ability-to-grab-selects-fiducials-depedent-on-zoom-level/6989

---

## Post #1 by @muratmaga (2019-06-01 18:33 UTC)

<p>As I was testing the new ruler and orthographic projection bug fixes in the nightly,  I noticed that I can’t seem to grab fiducials after they are placed, unless I really zoom in.</p>
<p>I have mixed feelings about this. In one hand, it is good that user don’t accidentally manipulate the fiducial placement when trying to rotate the volume. On the other hand, required level of zoom in constrains how much you can move the fiducial in one go.</p>

---

## Post #2 by @pieper (2019-06-01 19:02 UTC)

<p>Yes, I see what you mean - that seems like a problem with the picker in orthographic mode.  <a class="mention" href="/u/lassoan">@lassoan</a> or <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> might have ideas what’s wrong or if not I could have a look.</p>

---

## Post #3 by @lassoan (2019-06-01 19:50 UTC)

<p>Does picking work well in perspective projection?I haven’t tested it much with ortho projection, so maybe the picking tolerance computation needs some tuning for that mode. <a class="mention" href="/u/pieper">@pieper</a> it would be great if you could have a look.</p>

---

## Post #4 by @lassoan (2019-06-01 23:26 UTC)

<p>I’ve tried this now and it is actually a regression. It was still working well in version 2019-05-29 (28272) and was broken in 2019-05-30 (28277).</p>
<p>I’ve now fixed the regression and made another improvement that makes picking more robust (that removes interference of labels with occlusion detection, that might have been the root cause of the picking issue in ortho mode). The preview (formerly called “nightly”) version that you download tomorrow or later will include the fix.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="6989">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>In one hand, it is good that user don’t accidentally manipulate the fiducial placement when trying to rotate the volume. On the other hand, required level of zoom in constrains how much you can move the fiducial in one go.</p>
</blockquote>
</aside>
<p>Zooming should not affect how easily a markup point can be picked. You can pick anywhere on the displayed markup point or in its “neighborhood”. The size of this neighborhood is defined by a tolerance value in display coordinates, so it does not depend on zoom factor.</p>
<p>If you find that it is too easy to hit a markup point while manipulating the view, then you can lock markups to prevent accidental modifications. We may also decide to add a “markup manipulate” mouse mode and allow markup moving only in that mode (similarly how window/level is only adjustable now in a dedicated mode).</p>
<p>If you find that it is too hard to hit a markup point (so it is hard to move them) then we may make the picking tolerance user-adjustable. It could make sense, since tolerance may depend on the eyesight and hand-motion-precision of the user and the size and resolution of the screen. If we make the value adjustable then we need to decide where to store it (in the application settings; or in the scene, maybe as a default view parameter) and if we want to make it adjustable per view or even adjustable per markup. These are all doable, just need to find a good balance between flexibility and simplicity.</p>

---

## Post #5 by @muratmaga (2019-06-02 20:42 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> thanks for the fix. I will try with the ‘preview’. These are also all excellent suggestions. I will definitely follow up on them…</p>

---
