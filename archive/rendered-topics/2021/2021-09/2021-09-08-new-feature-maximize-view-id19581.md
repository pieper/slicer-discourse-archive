# New feature: maximize view

**Topic ID**: 19581
**Date**: 2021-09-08
**URL**: https://discourse.slicer.org/t/new-feature-maximize-view/19581

---

## Post #1 by @lassoan (2021-09-08 18:42 UTC)

<p>We added a new feature that allows quickly maximize a view (use the space of the entire view layout) without switching between layouts.</p>
<p>The feature can be activated using 3 methods:</p>
<ul>
<li>double-click on a view to maximize/restore</li>
<li>click the maximize/restore button in the view control bar (at the top of each view)</li>
<li>right-click on the view and choose maximize/restore</li>
</ul>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc915dbe1eebb7d4e81ce90e23fe94aeac16680c.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc915dbe1eebb7d4e81ce90e23fe94aeac16680c.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc915dbe1eebb7d4e81ce90e23fe94aeac16680c.mp4</a>
    </source></video>
  </div><p></p>
<p>When the view is restored then the original view layout is restored. The feature is available in latest Slicer Preview Release.</p>
<p>Any feedback and suggestions are welcome.</p>

---

## Post #2 by @chir.set (2021-09-08 20:53 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="1" data-topic="19581">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>feedback</p>
</blockquote>
</aside>
<p>Awesome, real time saver. And helper, as with this ergonomic switch, I for one, is already switching to maximized view more often. Formerly, multiple clicks for such display was bad for lazy guys like me.</p>
<p>+10.</p>
<aside class="quote no-group" data-username="lassoan" data-post="1" data-topic="19581">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>suggestions</p>
</blockquote>
</aside>
<p>It can’t be better.</p>

---

## Post #3 by @jamesobutler (2021-09-29 13:06 UTC)

<p>I have run into an annoying issue regarding this feature’s activation by “double left-click on a view to maximize/restore”.</p>
<p>I have a mouse that is a bit broken that will occasionally trigger double left clicks. When I’m placing control points for a markup in “Place multiple control points” mode, that can cause it to place the point and also maximize/restore the view which is jarring. I could also see a user using double left-click to apply/confirm a control point’s position.</p>
<p>Would it be possible to only support maximize/minimize while in the regular cursor (ViewTransform) mouse mode? It appears that double left-click to maximize/restore does not happen while in the AdjustWindowLevel mouse mode.</p>

---

## Post #4 by @lassoan (2021-09-29 13:39 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="3" data-topic="19581">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>It appears that double left-click to maximize/restore does not happen while in the AdjustWindowLevel mouse mode.</p>
</blockquote>
</aside>
<p>Double-left-click has a different action in AdjustWindowLevel mode (reset window/level).</p>
<p>I agree that it makes sense to have left-click and left-double-click do related actions, as a double-click event always means that a single-click event happened too. I’ve now tried mapping double-click event to end placement and it works very well: double-click places a point and that position and stops placement, which is a very convenient feature even if it was not needed due to interference with maximize event. This solution still allows maximizing the view (which can be a very useful feature during placement), the user just need to add a different shortcut.</p>

---

## Post #5 by @jamesobutler (2021-09-29 13:51 UTC)

<p>It’s the double clicking while in placement mode that is maximize/restoring the view that is the annoying part for me. I don’t necessarily need the placement to be applied on double click, but when I’m in placement mode I’m expecting that left clicking is only going to be placing and not doing any other action at the same time such as maximize/restore. That’s the unexpected and confusing behavior.</p>

---

## Post #6 by @lassoan (2021-09-29 14:00 UTC)

<p>Double-click to finish placement is a useful feature anyway and this is how point editing is finished in most other software. It also solves the inconsistency between default mapping of click and double-click actions.</p>
<p>If you want to eliminate double-click in the application because of a broken mouse then it seems to make sense to replace that mouse; but you can also remove the double-click mapping or re-map to something else (such as Ctrl + Left-double-click).</p>
<p>Mouse and keyboard gestures preferences are personal, probably the result of what people got used to do in various software that they used in the past. So, we will not be able to make everyone happy with a single default mapping. We have made good progress towards customizing all the event translations, but some more work would be needed to expose the feature conveniently to users.</p>

---

## Post #7 by @hherhold (2021-09-29 14:09 UTC)

<p>I happened upon the double click to maximize view by accident and I have to say it has changed how I work. I flip between conventional and 3D only <em>a lot</em> and the double click is a huge time saver for me. As <a class="mention" href="/u/lassoan">@lassoan</a> mentioned, the number of different workflows and applications using 3D Slicer, keeping everyone happy is going to be a challenge (at best), but for me, at least, the double click change view is awesome.</p>

---

## Post #8 by @lassoan (2021-09-29 14:31 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="7" data-topic="19581">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>it has changed how I work. I flip between conventional and 3D only <em>a lot</em> and the double click is a huge time saver for me</p>
</blockquote>
</aside>
<p>Great, thanks for the feedback!</p>
<aside class="quote no-group" data-username="hherhold" data-post="7" data-topic="19581">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>I happened upon the double click to maximize view by accident</p>
</blockquote>
</aside>
<p>Do you have a suggestion for how to make aware users about new features? Do you know that all new features that are announced on the forum are tagged with the “feature” tag and so they are listed <a href="https://discourse.slicer.org/tag/feature">here</a> (and you can also sign up for notifications about new features by clicking on the <img src="https://emoji.discourse-cdn.com/twitter/bell.png?v=12" title=":bell:" class="emoji" alt=":bell:" loading="lazy" width="20" height="20"> icon in the top-right corner on that page)?</p>

---

## Post #9 by @jamesobutler (2021-09-29 14:52 UTC)

<p>Let me clarify, placing markup position with single left-click or with double left-click is fine with me.  What is confusing is when two actions happen on the same mouse action. So if mouse double-click places the position then we have the following issue:</p>
<p>Left Double-Click</p>
<ul>
<li>Places control point</li>
<li>Also maximizes/restores the view</li>
</ul>
<p>^ 2 different actions in the same click should not happen and is confusing. Only one thing should be processed. What would be clear for me is that single left-click places the control point or double left-click places the control point, however no maximize/restore view layout would happen on double left-click while in multiple control point placement mode.</p>

---

## Post #10 by @lassoan (2021-09-29 15:06 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="9" data-topic="19581">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>2 different actions in the same click should not happen and is confusing.</p>
</blockquote>
</aside>
<p>Actually, this is how most software works: when the user double-clicks then it initiates a click event followed by a double-click event. This is like this both at operating system level and in Qt level. You don’t even notice this, because applications choose the double-click action so that the included single-click action before it feels natural.</p>
<p>It is feasible to ignore the single-click event in case of a double click, but only if you delay the processing of the single-click event (to see if a second click is coming), which slows down the software, not clear, and it is very rarely done.</p>
<p>With the double-click-to-complete, curve drawing will work the same way in Slicer as in most other software (PowerPoint, Inkscape, Gimp, etc.).</p>

---

## Post #11 by @jamesobutler (2021-09-29 15:19 UTC)

<p>When a left double-click is processed, I’m fine with it process actions for the single click and for the double click event. However different action makes it very confusing when placing a line node which is in the “Place multiple control points” mode.</p>
<p>It would be helpful for usability if double left-click processed the maximize/restore action only while in the ViewTransform mouse mode. When I double left-click while in the AdjustWindowLevel mode, it resets the window level for the volume, but it does not also maximize/restore the view layout. This same type behavior would be helpful while in Place mode.</p>
<p>Here’s me double left-clicking on purpose placing points. Here I’m trying to place control points in a square and I’m having difficulties because the maximize/restore view layout keeps happening on double left click when I don’t want it to.</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14418d0d2d5da2a4ea43a6ae2e423a586899fe6a.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14418d0d2d5da2a4ea43a6ae2e423a586899fe6a.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14418d0d2d5da2a4ea43a6ae2e423a586899fe6a.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #12 by @lassoan (2021-09-29 15:51 UTC)

<p>I see, I did not explicitly describe this, but if markups consumes the double-click event (for ending the placement) then of course the view will not be maximized/minimized anymore by that same event.</p>
<p>New behavior (implemented in <a href="https://github.com/Slicer/Slicer/pull/5910" class="inline-onebox">ENH: Add mouse gesture to finish markup point placement by double-click by lassoan · Pull Request #5910 · Slicer/Slicer · GitHub</a>):</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4150f25db7f72774741dd5ed2bc6cbccaa785cc.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4150f25db7f72774741dd5ed2bc6cbccaa785cc.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4150f25db7f72774741dd5ed2bc6cbccaa785cc.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #13 by @jamesobutler (2021-09-29 15:54 UTC)

<p>Yes, this is better. Thanks! Double left-click to place the control point and get out of placement mode is good with me especially if this is common behavior in other applications.</p>

---

## Post #14 by @thangngoc89 (2023-12-03 08:15 UTC)

<p>Sorry for replying to an old topics but after upgrading to Slicer 5.6.0 on macOS 13.4 (Ventura), this feature is gone. Double click doesn’t have any effect.</p>

---

## Post #15 by @pieper (2023-12-03 14:23 UTC)

<p>Yes, that’s a known issue that will hopefully be fixed in a patch release.  For now you can use the icon on the view control bar next to the slice slider.</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/7429">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/7429" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/7429" target="_blank" rel="noopener">Doubleclick to maximize sliceViews and threeDViews stopped working</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-11-26" data-time="17:26:25" data-timezone="UTC">05:26PM - 26 Nov 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/pieper" target="_blank" rel="noopener">
          <img alt="pieper" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

See this discussion:

https://discourse.slicer.org/t/maximize-vi<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ews-on-double-click-stopped-working/33025/4

## Steps to reproduce

Use latest and try doubleclicking.

## Environment
- Slicer version: Local build linux from git main as of 2023-11-15
- Operating system: linux</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #16 by @jcfr (2023-12-03 22:39 UTC)

<p>This should be fixed in <a href="https://github.com/Slicer/Slicer/pull/7442">PR-7442</a></p>
<p>Once this is integrated, we will backport the fix to the <code>5.6</code> branch.</p>

---
