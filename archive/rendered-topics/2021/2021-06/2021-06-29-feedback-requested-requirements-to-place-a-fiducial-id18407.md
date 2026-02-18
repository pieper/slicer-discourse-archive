# Feedback requested: Requirements to place a fiducial

**Topic ID**: 18407
**Date**: 2021-06-29
**URL**: https://discourse.slicer.org/t/feedback-requested-requirements-to-place-a-fiducial/18407

---

## Post #1 by @jamesobutler (2021-06-29 20:32 UTC)

<p>I’m looking to get feedback from users based on some recently changed behavior as it relates to placing fiducials. This post is originally motivated by a bug report I issued at <a href="https://github.com/Slicer/Slicer/issues/5713" class="inline-onebox" rel="noopener nofollow ugc">Unable to place markups points while moving mouse · Issue #5713 · Slicer/Slicer · GitHub</a>.</p>
<p>Starting with <a href="https://github.com/Slicer/Slicer/commit/6b8566e6384b34d86c353a3a2cd93c873673018a" class="inline-onebox" rel="noopener nofollow ugc">ENH: Allow view rotation&amp;zoom while placing markup · Slicer/Slicer@6b8566e · GitHub</a> which was first included in Slicer preview build <a href="http://slicer.kitware.com/midas3/api/rest?method=midas.bitstream.download&amp;name=Slicer-4.13.0-2021-06-25-win-amd64.exe&amp;checksum=461ec99a00bdc963b62e636efdfba3ed" rel="noopener nofollow ugc">Slicer-4.13.0-2021-06-25</a>, the mouse must not be moving at time of placing a fiducial. If you are slightly moving your mouse at time of click, the placement will get rejected.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> provided context of the change in markup placement behavior which can be read below:</p>
<blockquote>
<p>The change in behavior was introduced to remove the clash of right-click to finish placement / right-button-down to show context menu; and clash of left-click to jump to selected fiducial and left-button-down to place a fiducial. As a side effect, you can now zoom and rotate the view, etc. without exiting markups placement mode (and you assign the left-click-and-drag gesture during point placement in slice views to any custom actions).</p>
<p>The current implementation has several important advantages, but as side effect you indeed need to stop to place a point. Right now I feel that the advantages outweigh the single disadvantage, but it would be good to hear from others as well.</p>
</blockquote>
<p>I personally found this change in behavior annoying as well as some other users in my group because it slows down the workflow when trying to quick actions. These actions include placing a Line Node, placing points as part of a SurfaceCut segment editor effect and DrawTube effect. Often you can place the points quickly and then modify their position later if you weren’t as precise with your location click. However, now I end up missing a click and it throws off my workflow for a bit.</p>
<p>Below is a video of the fiducial placement behavior. It would be great to hear from other users about their thoughts of this recent change by using it. At first I place fiducials really quickly to demonstrate their placement being rejected. Then I try to place them slower, however even around the 6 second mark I accidentally have a fiducial position rejected even when I’m trying to be slow.<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/1883ef0adc9bf792129548b55cb30318a8ad6d84.mp4">
  </div><p></p>

---

## Post #2 by @lassoan (2021-06-29 21:16 UTC)

<p>Just to show why requiring “button click” (press and release) to place a markup instead of just “button press” - left click is used for placing a point, while left-click-and-drag rotates the view, right-click finishes point placement, while right-click-and-drag zooms in/out the view.</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/25c7b730c9e80bc1dae0943458a0752844f17a6f.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/25c7b730c9e80bc1dae0943458a0752844f17a6f.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/25c7b730c9e80bc1dae0943458a0752844f17a6f.mp4</a>
    </source></video>
  </div><p></p>
<p>You can now interact with your view normally, even during placing markups.<br>
<a class="mention" href="/u/muratmaga">@muratmaga</a> could you try the latest Slicer Preview Release?</p>
<p>Obviously any unrequested change is annoying, but the important question is if advantages of the new behavior justify the effort to adapt to the changes. We could also make it possible to turn this new feature off (as I often say, if you cannot turn off a feature then it is a bug). Unfortunately, making this operating mode switchable would not be easy, because it requires remapping of gestures in many widgets and it is complicated to separate click events (context menu, jump to slice) from mouse button events.</p>

---

## Post #3 by @jamesobutler (2021-06-29 21:18 UTC)

<p>Bringing over another comment from my GitHub issue post:</p>
<p>Placing fiducials in the 3D view in our 3D ultrasound workflow is not really of interest to us. We use the 3D view for visualization purposes only. I can ask some of the other users in my group about the usage in the 3D view, but I would assume they have similar opinions.</p>
<p>We also do some custom fiducial placement of M-Mode using DrawTube and this M-Mode volume doesn’t even need a 3D view being a 2D/2Dt volume. We detect this when we load and show volumes and set it to Red-slice only. These draw tube points are placed pretty quickly and having to stop to click is painful for the workflow.<br>
<img src="https://user-images.githubusercontent.com/15837524/123866864-9b5ebc00-d8fb-11eb-93c2-d38b692eecb6.png" alt="image" width="689" height="476"></p>

---

## Post #4 by @jamesobutler (2021-06-29 21:22 UTC)

<p>I’m ok with the change in the 3D View as it doesn’t impact me, however the decrease in performance when placing fiducials in the 2D slice views is not desired. Could the new behavior be limited to interaction of the 3D View?</p>

---

## Post #5 by @lassoan (2021-06-29 21:38 UTC)

<p>Your users may find it useful that they can zoom in/out without exiting and re-entering placement mode. The click-and-drag feature could be mapped to some other feature that is useful during curve drawing (for example, in inkscape click places a spline control point and click-and-drag adjusts the tangent). Maybe it would be better to do what many other spline drawing implementations do (PowerPoint, ITK-snap, etc.) if you click-and-drag during curve drawing: placing many points points automatically as you draw the line. It would by much faster and more convenient for the user than asking to quickly keep clicking while trying to follow the curve on the image.</p>

---

## Post #6 by @jamesobutler (2021-06-29 21:40 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="18407">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>if you click-and-drag during curve drawing: placing many points points automatically as you draw the line. It would by much faster and more convenient for the user than asking to quickly keep clicking while trying to follow the curve on the image.</p>
</blockquote>
</aside>
<p>Click and drag requires a lot more precision if lots of points were going to be placed. This would lead to a jagged curve. Here we actually want a smooth curve which is why placing points at the peaks has worked well for us.</p>
<p>Note that this still doesn’t resolve our 2D performance issues of using say SurfaceCut segmentations.</p>

---

## Post #7 by @muratmaga (2021-06-29 21:41 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="18407">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> could you try the latest Slicer Preview Release?</p>
</blockquote>
</aside>
<p>I did, and I like this behavior. It overcomes the major issue of not being able to rotate/zoom while placing fiducials. And we do most (not necessarily all) of landmarking in 3D views.</p>
<p>For me the slowdown in 2D slice is very little (required me to stop on a spot for a fraction of a second), but I only tested with MRHead. Perhaps it is slower for larger datasets. Anyhow, if it is going to help, I am ok having this new behavior reserved for 3D (where it really matters to be able to rotate and zoom, without going out of placement mode).</p>

---

## Post #8 by @lassoan (2021-06-29 22:06 UTC)

<p>Unfortunately, having different behavior in slice and 3D views would be about as hard to implement as making the mode selectable (and even worse, users may report this inconsistency as a bug). So, let’s keep brainstorming on alternative options.</p>
<p>What do you think about using the left-click-and-drag for something useful in slice views (e.g., continuous drawing with automatically placing control points along the way)? It could even be some kind of magnetic lasso tool (that would make the curve attracted to high gradient)? It could be all implemented in a new custom image curve markup (using the new pluggable markups infrastructure).</p>

---

## Post #9 by @muratmaga (2021-06-29 22:27 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="7" data-topic="18407">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I did, and I like this behavior. It overcomes the major issue of not being able to rotate/zoom while placing fiducials. And we do most (not necessarily all) of landmarking in 3D views.</p>
</blockquote>
</aside>
<p>Actually, I just tried with a 3D model of MRHead segmentation (previously I was using a volume rendering), and the interactions are indeed rather slow. For every mouse move, it takes about two seconds for the fiducial to catch up.</p>

---

## Post #10 by @jamesobutler (2021-06-29 22:29 UTC)

<p>Hmm I’m not sure how a continuous drawing with point placement will work in the slice views as it relates to Surface Cut. Surface cut benefits from a low number of points required that can then support modifying easily. If there is a bunch of points it is harder to know which ones are constraining the convex hull.</p>

---

## Post #11 by @smrolfe (2021-06-29 22:32 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="7" data-topic="18407">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I did, and I like this behavior. It overcomes the major issue of not being able to rotate/zoom while placing fiducials. And we do most (not necessarily all) of landmarking in 3D views.</p>
</blockquote>
</aside>
<p>Seconding <a class="mention" href="/u/muratmaga">@muratmaga</a>’s comments. This change makes the persistent placement mode much more useful. The placement mode shortcut in the <a href="https://github.com/Slicer/Slicer/pull/5325/commits" rel="noopener nofollow ugc">markups update</a> is now less important, although probably still nice to have.</p>

---

## Post #12 by @jamesobutler (2021-06-29 22:36 UTC)

<p>We had handled the rotation in placement mode issue by toggling with the space bar with the segment editor (surface cut fiducial placement) button visible. Then had used a forbidden arrow cursor and disabled the 3D view interactor as we don’t allow 3D view placement of fiducials for segmenting.</p>

---

## Post #13 by @jamesobutler (2021-06-30 11:49 UTC)

<p>For 2D Slice views, Ctrl+alt+left-click-and-drag is what does rotation of the slice intersections. If users are wanting to stay in placement mode during this action I think we have to keep it in context relative to this movement.</p>
<p>It’s the stacking of actions that use left mouse click that can get complicated. For instance Window/Level, left-click-and-drag can’t be used while in markups placement mode. Slicer requires changing the mouse mode to accomplish this. Will there be more mouse modes? What other left-click and left-click-and-drag actions will there be?</p>
<p>The new behavior change in the 3D view is essentially turning on 2 mouse modes at once (transform mode and placement mode).</p>

---

## Post #14 by @jamesobutler (2021-06-30 23:25 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Could this place fiducials and rotate type dual functionality be a new mouse mode?</p>

---

## Post #15 by @tomekcz (2021-07-01 13:58 UTC)

<p>I’m from the same group as <a class="mention" href="/u/jamesobutler">@jamesobutler</a> and have to agree with him that it is annoying that I have to deliberately stop moving my cursor to be able to place fiducials in the 2D views (for segmenting and other operations). I use Slicer not only for analysis, but also for acquiring new image data with robotic imaging hardware. It is common for me to quickly place fiducials in a 2D view that guide the robot where to go. These locations do not have to be precise which is why my cursor might frequently be moving at the time that I click. When I’m imaging there is usually a lot of things going on at once and I want to be as fast as possible and not get thrown off by a fiducial placement getting rejected.</p>
<p>Another observation, the fact that my cursor type is the fiducial placement icon with a fiducial visible at the end of it even while my cursor is moving and then it not doing anything when I click in a 2D view feels like a bug. It’s indicating to me that it can place something, but then silently rejects it which is confusing.</p>
<p>I took a look at other 3D modeling programs (e.g. Solidworks) to get some inspiration on how to deal with simultaneous point placement and view manipulation. It looks like their approach is to not perform any view manipulation with the Left click and keep that action reserved for Tool actions. For example, the 3D Rotation action is performed by the Middle-click, while Pan and 2D-Rotate are accomplished by Ctrl-Middle and Alt-Middle respectively. Slicer currently accomplishes these things with Left-click, Middle-click, and Ctrl-Left.</p>
<p>If it is too drastic of a change to migrate away from Left-click, what about using an Alt-Left when in Point Placement mode? The Alt button appears to be underutilized for these sorts of view manipulations.</p>

---

## Post #16 by @seanchoi0519 (2021-07-01 17:34 UTC)

<p>I agree with you guys - we would much rather have superior performance in placing markup points over view because well, that’s what we want to focus on when using the markups module.</p>
<p>As in, I think it’s not a big deal if we place the markup point in a slightly incorrect spot occasionally due to view issue because it can be easily corrected once it’s been placed - however having to deal with the slightly delayed mouse click every time we place a point is quite annoying I must say.</p>
<p>It would be great if you could take our feedback into consideration <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=9" title=":smiley:" class="emoji" alt=":smiley:"></p>

---

## Post #17 by @muratmaga (2021-07-01 17:47 UTC)

<aside class="quote no-group" data-username="seanchoi0519" data-post="16" data-topic="18407">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/seanchoi0519/48/10354_2.png" class="avatar"> seanchoi0519:</div>
<blockquote>
<p>As in, I think it’s not a big deal if we place the markup point in a slightly incorrect spot occasionally due to view issue because it can be easily corrected once it’s been placed - however having to deal with the slightly delayed mouse click every time we place a point is quite annoying I must say.</p>
</blockquote>
</aside>
<p>I think this depends on the workflow what level of precision you are looking for. It is completely the other way around for us. I would rather place the point precisely in the first place and move on to the next without having the review the placement later. This new behavior facilitates that.</p>
<p>The challenge is finding a behavior that will support both use cases effectively.</p>

---

## Post #18 by @muratmaga (2021-07-01 17:50 UTC)

<aside class="quote no-group" data-username="tomekcz" data-post="15" data-topic="18407">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tomekcz/48/11462_2.png" class="avatar"> tomekcz:</div>
<blockquote>
<p>If it is too drastic of a change to migrate away from Left-click, what about using an Alt-Left when in Point Placement mode? The Alt button appears to be underutilized for these sorts of view manipulations.</p>
</blockquote>
</aside>
<p>I tried to simulate this behavior when I am doing LM. It is might be solution. However, I suspect you will find this equally disruptive and causing slow down, if your goal is to place lots of landmarks approximately in a very quick fashion. (Or perhaps not if you keep the ALT pressed down and manage to go click-click-click).</p>

---

## Post #19 by @smrolfe (2021-07-01 17:53 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="18" data-topic="18407">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I tried to simulate this behavior when I am doing LM. It is might be solution. However, I suspect you will find this equally disruptive and causing slow down, if your goal is to place lots of landmarks approximately in a very quick fashion. (Or perhaps not if you keep the ALT pressed down and manage to go click-click-click).</p>
</blockquote>
</aside>
<p>In this case, it might be preferable to use the ALT key to enable rotation, and update the mouse icon to to translate.</p>
<p>This would be more consistent with the place mode selection, which the user could then temporarily suspend with a keyboard shortcut.</p>

---

## Post #20 by @tomekcz (2021-07-01 17:56 UTC)

<p>Oh I see, my original post may not have been clear. What I meant is the Left-click action will place fiducial points as in previous versions of Slicer, while holding Alt-Left would allow you to perform a 3D rotation of the view.</p>
<p>In other words, roll back to the old version of the fiduicial placement, which is fast and snappy, but achieve the 3D rotation functionality your group desires by introducing a new Alt-Left action.</p>
<p>This type of manipulation is already somewhat enabled using Ctrl-Left. If you enter the Open Curve Draw Mode, Left click lets you place fiducials, while Ctrl-Left lets you do a 2D rotation of the 3D view even though you’re still technically in “point placement mode”.</p>
<p>Does this make sense?</p>

---

## Post #21 by @muratmaga (2021-07-02 04:13 UTC)

<aside class="quote no-group" data-username="tomekcz" data-post="20" data-topic="18407">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tomekcz/48/11462_2.png" class="avatar"> tomekcz:</div>
<blockquote>
<p>In other words, roll back to the old version of the fiduicial placement, which is fast and snappy, but achieve the 3D rotation functionality your group desires by introducing a new Alt-Left action.</p>
</blockquote>
</aside>
<p>This may work for us, <a class="mention" href="/u/lassoan">@lassoan</a> what do you think?</p>

---

## Post #22 by @seanchoi0519 (2021-07-02 07:52 UTC)

<p>This would be great for me.</p>

---

## Post #23 by @lassoan (2021-07-03 18:26 UTC)

<p>I loved the new mouse behavior and it made the code much cleaner. But I agree that this is not how curve drawing works in most other software and if we don’t have a dedicated continuous line drawing widget then it forces users to pause at each point. Since I don’t have time to make the behavior configurable or create a new continuous drawing mode, I will find some other way to add right-click menu to viewers while preserving the old way of placing points.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="10" data-topic="18407">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Surface cut benefits from a low number of points required that can then support modifying easily</p>
</blockquote>
</aside>
<p>We could fit a spline to the drawn curve, or drop points at predefined distances, or automatically place a point at each sharp turn. All doable, and would allow faster and more convenient curve drawing on images, but someone would need to invest at least a few days into implementing this. It would be also a good opportunity to introduce a “magnetic” mode, which would snap the drawn curve to the nearest “boundary” (voxel with high image gradient magnitude).</p>
<aside class="quote no-group" data-username="muratmaga" data-post="9" data-topic="18407">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Actually, I just tried with a 3D model of MRHead segmentation (previously I was using a volume rendering), and the interactions are indeed rather slow. For every mouse move, it takes about two seconds for the fiducial to catch up.</p>
</blockquote>
</aside>
<p>This is indeed inconvenient, but it is not related to this discussion. The behavior was the same before. We could store locators for large models in the model displayable manager and use that in the point picker. This would probably make curve placement over large and complex models 10-100x faster, and so drawing curves over complex models would not be delayed. You can start a new topic or feature request on github if you want to explore this further.</p>

---
