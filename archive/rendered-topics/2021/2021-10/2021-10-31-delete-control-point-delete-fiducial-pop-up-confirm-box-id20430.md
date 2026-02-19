---
topic_id: 20430
title: "Delete Control Point Delete Fiducial Pop Up Confirm Box"
date: 2021-10-31
url: https://discourse.slicer.org/t/20430
---

# Delete control point / delete fiducial pop-up - confirm box?

**Topic ID**: 20430
**Date**: 2021-10-31
**URL**: https://discourse.slicer.org/t/delete-control-point-delete-fiducial-pop-up-confirm-box/20430

---

## Post #1 by @hherhold (2021-10-31 15:10 UTC)

<p>This kinda harkens back to some discussions here and there with <a class="mention" href="/u/muratmaga">@muratmaga</a> and others here regarding placing control points and the right-click pop-up menu. I rename and delete control points placed in the 3D view a lot, and on several occasions I’ve accidentally hit “Delete Fiducial” instead of “Delete control point”, and wind up blowing away a bunch of points. I fully realize it’s my own lack of dexterity that leads to this, but would it make sense to have a confirmation dialog for “Delete Fiducial”? Or possibly moving it so it’s not right next to “Delete control point”? If I’m the only one with this issue, it’s no big deal and I can live with it, just wondering if others have run into this and if it’s worth thinking about changing.</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @jamesobutler (2021-10-31 15:54 UTC)

<p>I don’t believe an additional confirmation box is the right solution to this issue. Right-click context menu with selection and clicking is a fairly deliberate action, so it would be a bit annoying to deliberately choose to “Delete Fiducial” and then have to click another pop-up to confirm the deliberate action to delete.</p>
<p>Moving the location of this action to the top of the list however, could be a nice solution to move the two options away from being directly next to each other. It would also make consistent the ordering of the control point actions versus the fiducial object actions where the “Delete” action is at the top followed by various editing of that object below it. Having it at the top is probably also consistent with it seemingly being the more commonly used action as well. See the image below of this change.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Current</th>
<th>New Option</th>
</tr>
</thead>
<tbody>
<tr>
<td><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/7774f072aecc8ac3f501c1cebfacb7239baf2196.png" alt="image" data-base62-sha1="h2LmkuOmSBGSduR4lpJovvMcsf4" width="428" height="397"></td>
<td></td>
</tr>
</tbody>
</table>
</div>

---

## Post #3 by @muratmaga (2021-10-31 16:11 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="20430">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>I don’t believe an additional confirmation box is the right solution to this issue. Right-click context menu with selection and clicking is a fairly deliberate action, so it would be a bit annoying to deliberately choose to “Delete Fiducial” and then have to click another pop-up to confirm the deliberate action to delete.</p>
</blockquote>
</aside>
<p>It is true, but we don’t have an undo. So a mistake of accidentally deleting a whole markup node vs a control point is very costly (that you might loose dozens or hundreds of points). While I don’t see a need for confirmation for deleting an individual point, I think the cost of error overweighs the minor annoyance, for confirming to delete a whole node.</p>

---

## Post #4 by @jamesobutler (2021-10-31 16:16 UTC)

<p>If a confirmation dialog is added, then it should be added consistently across the application for all delete object actions. This would including right-clicking and pressing “Delete” when selecting an object to delete in a node table such as the Data module or Markups module. This just doesn’t strike me as the correct solution. It is going to be annoying to users who know what they are doing and are saying to delete and then get asked are you sure you want to delete. All this to avoid the more infrequent case of accidentally deleting.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75403a54eef98759825cefb63f2084ef7111fed7.png" alt="image" data-base62-sha1="gJfteOdItjEcmRJeHxBpEWJFdEH" width="468" height="158"></p>

---

## Post #5 by @muratmaga (2021-10-31 16:25 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="4" data-topic="20430">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>If a confirmation dialog is added, then it should be added consistently across the application for all delete object actions.</p>
</blockquote>
</aside>
<p>Why? It is not like we  have lots of consistency across actions in all modules?</p>
<p>THe screenshot you share is not reflective of the issue in hand. In markups, in the menu there are two delete operations and that the difference between control points and fiducials has been murky for users (perhaps with the exception of people who has been using Slicer since version 2) at best. In your scenario above, there is no accidental deleting (i.e., mistaking an action).</p>
<p>I would also second that confirmation should be added to any costly unrecoverable operations, with the option to disable the confirmation (e.g., like we do closing the slicer scene without asking to save the files, if it is a deliberate action)</p>

---

## Post #6 by @jamesobutler (2021-10-31 16:31 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="5" data-topic="20430">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>It is not like we have lots of consistency across actions in all modules?</p>
</blockquote>
</aside>
<p>This should be something attempted. Blatantly going against consistency is bad design.</p>
<p>If your users have some confusion between fiducials and control points have you considered creating a Slicer custom application so that you can customize the right-click context menu as you please for your users?</p>

---

## Post #7 by @muratmaga (2021-10-31 16:40 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="6" data-topic="20430">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>This should be something attempted. Blatantly going against consistency is bad design.</p>
</blockquote>
</aside>
<p>I would argue risking to loose data is even worse design.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="6" data-topic="20430">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>If your users have some confusion between fiducials and control points have you considered creating a Slicer custom application so that you can customize the right-click context menu as you please for your users?</p>
</blockquote>
</aside>
<p>We do not have a set of ‘fixed users’. A lot of ‘our users’ are biologists, who are likely to use the base SLicer application, not a customized version of slicer. Nor we have the bandwidth or resources to maintain such application. We are biologists, not software developers. Plus, this mistake is likely to affect any new Slicer user, just ‘our users’.</p>

---

## Post #8 by @jamesobutler (2021-10-31 16:49 UTC)

<p><a class="mention" href="/u/hherhold">@hherhold</a> Would the proposed design of moving the delete control point action to the top of the list be helpful for you? If so, I would be happy to submit that change as a new PR.</p>

---

## Post #9 by @muratmaga (2021-10-31 17:00 UTC)

<p>I would suggest having these actions close together and with at a more description, perhaps something like this:</p>
<ul>
<li>Delete Control Point</li>
<li>Delete FiducialNode (deletes all control points).</li>
</ul>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/hherhold">@hherhold</a> <a class="mention" href="/u/smrolfe">@smrolfe</a> what do you think?</p>

---

## Post #10 by @hherhold (2021-10-31 18:09 UTC)

<p>I think <a class="mention" href="/u/jamesobutler">@jamesobutler</a> 's suggestion of moving Delete Fiducial Node away from Delete Control Point is the “low hanging fruit” for this. Regarding the last suggestion from <a class="mention" href="/u/muratmaga">@muratmaga</a> - It’s not that I don’t know what each one does, it’s just in the heat of the moment (putting down markups is pretty exciting) I will inadvertently click the wrong one and delete a bunch of work.</p>
<p>I would leave Rename as the first option as it’s probably done more than any other, and delete control point right under it.</p>
<p>Opinions?</p>

---

## Post #11 by @muratmaga (2021-10-31 18:29 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="10" data-topic="20430">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>It’s not that I don’t know what each one does, it’s just in the heat of the moment (putting down markups is pretty exciting) I</p>
</blockquote>
</aside>
<p>That’s exactly my point. You as an experienced user can potentially confuse this. İ thought keeping them right next to each other oppose to far from, likely to reduce this error. Because you are more likely to see both at the same time and give it a thought before you click the whichever one you saw first.</p>

---

## Post #12 by @hherhold (2021-10-31 18:30 UTC)

<p>Oh, I see. Yeah, that’s a valid point, and having the extra verbiage is probably enough to make sure I don’t click the wrong one. And organizationally it does make sense to have them in the same general area. Sure, I’ll vote for that option.</p>

---

## Post #13 by @lassoan (2021-10-31 20:51 UTC)

<p>Actions that apply to the entire node actions are kept away from actions that only apply to the current control point. I wouldn’t break this grouping. There are reasons to have “Delete…” at the top of the action group and bottom of the action group, too.</p>
<p>The proper solution would be to <a href="https://discourse.slicer.org/t/new-markups-functionality-retains-unset-control-point-positions/20140/11">enable scene undo</a> (at least for markups), but we can also add a confirmation popup (with a “Don’t show again” checkbox) - it is easy to implement, and we already have such popups at a number of places.</p>

---

## Post #14 by @jamesobutler (2021-10-31 21:57 UTC)

<p>If we can not show the confirmation Dialog by default, but support customization to show it, that would be great. It would help reduce customization of code and maintenance burden on our group’s end to maintain current behavior. Adding code to maintain current behavior is not desired.</p>

---

## Post #15 by @muratmaga (2021-10-31 23:58 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="13" data-topic="20430">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The proper solution would be to <a href="https://discourse.slicer.org/t/new-markups-functionality-retains-unset-control-point-positions/20140/11">enable scene undo</a> (at least for markups)</p>
</blockquote>
</aside>
<p>That will indeed be the best solution. +1</p>

---

## Post #16 by @jamesobutler (2021-11-01 01:04 UTC)

<p>Renaming “Fiducial” to “Fiducial List” would resolve issues of terminology confusion between “Fiducial” vs “Control Point”. Use of the “node” terminology is too technical for regular users, so would have to be something like “Fiducial List” rather than “Fiducial Node”. It is unexpected that “Fiducial” is a group of points. I understand some of the mistakes from the past about this terminology, but surely some improvement is possible even if it may be annoying to fix on the backend code side.</p>

---

## Post #17 by @hherhold (2021-11-01 01:36 UTC)

<p>That’s a valid point too, as to casual users “Fiducial” sounds singular, as in a single point. Renaming it to “Delete Fiducial List” seems like a good compromise?</p>

---

## Post #18 by @lassoan (2021-11-01 04:41 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="16" data-topic="20430">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Renaming “Fiducial” to “Fiducial List” would resolve issues of terminology confusion between “Fiducial” vs “Control Point”</p>
</blockquote>
</aside>
<p>We’ll do this. This need to separate the <em>machine readable</em> markup type (<code>Fiducial</code>, <code>ClosedCurve</code>, etc.) from what is displayed on the GUI (with better formatting, more clear meaning, translatable to different languages; such as <code>fiducial list</code>, <code>closed curve</code>) has come up in another discussion already. I’ve added a ticket to track this:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5976">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5976" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5976" target="_blank" rel="noopener">Make displayed markup node type names more user-friendly</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-11-01" data-time="04:40:42" data-timezone="UTC">04:40AM - 01 Nov 21 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2021-11-09" data-time="15:27:24" data-timezone="UTC">03:27PM - 09 Nov 21 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Enhancement
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">It is not clear for users that "Fiducial node" means a "fiducial list". It is no<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">t nice that a closed curve is referred to as "ClosedCurve node" on the GUI.

## Describe the solution you'd like

Use a different string for markup type in code and files (simple machine-readable string, such as `Fiducial`, `ClosedCurve`) and on the GUI (human-readable, translatable string, such as `fiducial list`, `closed curve`).

## Describe alternatives you've considered

Automatic conversion from CamelCase to space separators could work, but would not be translatable to different languages.

## Additional context

https://discourse.slicer.org/t/delete-control-point-delete-fiducial-pop-up-confirm-box/20430/14</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #19 by @pieper (2021-11-01 14:49 UTC)

<p>Going further, the term “Fiducial” is pretty odd (it comes from Slicer’s neurosurgery roots where it refers to a marker stuck to the skin before a scan, and those are even used any more).  If we are changing things why not drop that term completely and use a term like “Point Set” or “Point List” or “Landmarks”?</p>
<p>As an aside, for proper names of data types I think Title Case is correct, so Closed Curve and Point Set make sense, even if they are used in a UI element where the text is in Sentence case (that is the menu item would read “Delete highlighted Point Set” or “Delete highlighted Closed Curve”).</p>

---

## Post #20 by @muratmaga (2021-11-01 14:50 UTC)

<aside class="quote no-group" data-username="pieper" data-post="19" data-topic="20430">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Going further, the term “Fiducial” is pretty odd (it comes from Slicer’s neurosurgery roots where it refers to a marker stuck to the skin before a scan, and those are even used any more). If we are changing things why not drop that term completely and use a term like “Point Set” or “Point List” or “Landmarks”?</p>
</blockquote>
</aside>
<p>I agree. Point List or Landmark List would be great to refer to fiducials.</p>

---

## Post #21 by @hherhold (2021-11-01 14:57 UTC)

<p>Totally agreed. I’ve had to explain “Fiducial” on several occasions - always gets a quizzical look. Either Point List or Landmark List (following <a class="mention" href="/u/pieper">@pieper</a>’s Title Case) would be much clearer.</p>

---

## Post #22 by @lassoan (2021-11-01 15:20 UTC)

<p>I like “Point List” because it is similar to other markup types - line, curve, plane, etc. and does not assume any particular use. A geometric primitive has multiple uses (point can represent a fiducial marker or an anatomical landmark; a line can represent a distance measurement ruler or caliper, or an axis of rotation, etc.) so it makes sense to not name them based on one specific use.</p>
<p>I would prefer “Point List”, as indicates that order of points matter; in contrast to “point set”, which often means that the items are unordered.</p>
<p>Changing class names and code strings would be disruptive but changing the display name from “Fiducial” to “Point List” should have minimal impact.</p>

---

## Post #23 by @jamesobutler (2021-11-01 15:21 UTC)

<p>I support “Point List” as yes we use this node type for placing locations to move our motion stage to, so it isn’t always for Landmarking purposes.</p>

---

## Post #24 by @cpinter (2021-11-02 09:22 UTC)

<p>Just to chime in, I like Point List too. It is good timing for such a change before releasing Slicer 5.</p>
<p>I tend to agree with <a class="mention" href="/u/jamesobutler">@jamesobutler</a> that “node” may be too technical, but still I think the users know what they are (it can be seen in many places in the UI), so adding “node” to the end of the delete action text would make things more explicit.</p>

---

## Post #25 by @jamesobutler (2021-11-02 10:05 UTC)

<p>As it relates to “node” being too technical I say that because multiple of our users had previously asked “what is a node?” when we had some mention of it. I had to explain that it essentially just meant “object”. So we changed from saying “creating a line node” to simply “creating a line”.</p>
<p>If there are places in Slicer that say “node” in the GUI those should be removed. I know in the Segment Editor module the main combobox objects at the top are “Segmentation” and “Master Volume” which don’t have “node” mentions even though technically it is a node selector.</p>

---

## Post #26 by @lassoan (2021-11-05 18:19 UTC)

<p>We should try to avoid using “node” in the GUI as much as possible, but I don’t think it is reasonable to ban it. For example, It would be not easy to remove “node” term from everywhere in Data module and anywhere where we collectively refer to different types of nodes or we don’t know the exact node type.</p>
<p>I agree that “object” would sound less technical, but it would be confusing when it is used for constructs that are not physical objects, such as a parameter node, display node, storage node, unit node, selection node, interaction node. “Object” is also a heavily used term in programming, so it would be hard to talk about how to use methods if the inputs/outputs were just objects. If we used “object” on the GUI and “node” in the API then it would complicate things.</p>

---

## Post #27 by @jamesobutler (2021-11-08 17:39 UTC)

<p>To follow up, there was a PR created that includes changing “Fiducial” to “Point List”.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/5986">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/5986" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/5986" target="_blank" rel="noopener nofollow ugc">Improvements to displayed markup type including "Point List" terminology</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>jamesobutler:displayed-markup-type</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-11-03" data-time="21:09:42" data-timezone="UTC">09:09PM - 03 Nov 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>

      <div class="lines" title="2 commits changed 12 files with 41 additions and 14 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/5986/files" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+41</span>
          <span class="removed">-14</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This closes #5976 and is based on @pieper's original suggestion of a new method <span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/5986" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">that returned a string for markup type that was appropriate to be used in the GUI unlike `GetMarkupType()` which is used for internal logic for registering markups.

This makes the GUI easier to read and understand such as "Delete ClosedCurve" -&gt; "Delete Closed Curve". Also the change from the term "Fiducial" -&gt; "Point List" to represent a group of control points. Note that this improves usability for users, but does not yet make things simpler for developers. Developers will still use `slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode")` to create what is shown as a "Point List" which is a bit confusing.

## Markups module and toolbar updates

| Current | This PR |
|----------|---------|
|![image](https://user-images.githubusercontent.com/15837524/140191701-fe14a341-244f-4157-8e26-953f11b61437.png)|![image](https://user-images.githubusercontent.com/15837524/140192965-1b93d3da-ed2c-49b5-9be0-86206d819c66.png)|

- Other considerations could be to update the default short node name from "F" to "PL" or something to match the updated markup type displayed to users. Thoughts on a better short node name?

## Right-click context menu updates

| Current | This PR |
|----------|---------|
|![image](https://user-images.githubusercontent.com/15837524/140192287-668f9bf6-2c7a-4ba6-a765-08b27d019864.png)|![image](https://user-images.githubusercontent.com/15837524/140192311-b5b43f02-13d7-4fdb-a532-3312e7341fab.png)|
|![image](https://user-images.githubusercontent.com/15837524/140192346-dda261b0-11a1-4cb5-9c40-5af6f745bea4.png)|![image](https://user-images.githubusercontent.com/15837524/140192376-486f8223-44d0-4a0a-8d40-53860c8405ef.png)|</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
