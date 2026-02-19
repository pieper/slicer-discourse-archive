---
topic_id: 12714
title: "Proposed Changes To Markups To Support Unplaced Points"
date: 2020-07-23
url: https://discourse.slicer.org/t/12714
---

# Proposed changes to Markups to support unplaced points

**Topic ID**: 12714
**Date**: 2020-07-23
**URL**: https://discourse.slicer.org/t/proposed-changes-to-markups-to-support-unplaced-points/12714

---

## Post #1 by @smrolfe (2020-07-23 22:35 UTC)

<p>I’d like to help implement some updates to support the use of unplaced fiducials, as discussed in <a href="https://discourse.slicer.org/t/adding-control-points-with-undefined-position-from-python/12344/2">this thread</a>. From that discussion and our user needs, I made a detailed list of improvements and would appreciate feedback or advice. <a class="mention" href="/u/lassoan">@lassoan</a> your input would be especially helpful.</p>
<p><a class="mention" href="/u/ezgimercan">@ezgimercan</a> <a class="mention" href="/u/muratmaga">@muratmaga</a></p>
<p><strong>Views</strong></p>
<ul>
<li>Hide display of unplaced fiducials</li>
<li>Hide position of unplaced fiducial in Markups control point table</li>
</ul>
<p><strong>Markups Module</strong></p>
<ul>
<li>
<p>Add buttons for unplace all/unplace selected to the menu bar above the control points table, similar to delete all/delete selected (see screenshot)</p>
</li>
<li>
<p>Add column in the control points table for placement status. This could be modeled after the Segment editor status column, which shows an open circle for segments not started and a check mark for complete (see screenshot below). Toggling the icon to checkmark would initiate landmark placement mode to place this point. Toggling again to the open circle would set position to (0,0,0) and set “unplaced” flag.</p>
</li>
<li>
<p>Update “Add new markup at origin” button to add new unplaced markup. This button currently is not working for me with the intended function.</p>
</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e17888ea1f96820ef1f313d06e1d81cd012a2fa.png" data-download-href="/uploads/short-url/20F6uxFedwlsoNSQC2SvJOgdxi2.png?dl=1" title="Screen Shot 2020-07-23 at 2.56.04 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0e17888ea1f96820ef1f313d06e1d81cd012a2fa_2_414x499.png" alt="Screen Shot 2020-07-23 at 2.56.04 PM" data-base62-sha1="20F6uxFedwlsoNSQC2SvJOgdxi2" width="414" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0e17888ea1f96820ef1f313d06e1d81cd012a2fa_2_414x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0e17888ea1f96820ef1f313d06e1d81cd012a2fa_2_621x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0e17888ea1f96820ef1f313d06e1d81cd012a2fa_2_828x998.png 2x" data-dominant-color="393736"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-07-23 at 2.56.04 PM</span><span class="informations">1386×1670 180 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08872fc7c6d6edc558cfd7024656e206f883910c.png" data-download-href="/uploads/short-url/1drsg7VDGg6hSiIJbQHHVXBoT5a.png?dl=1" title="Screen Shot 2020-07-23 at 3.25.35 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08872fc7c6d6edc558cfd7024656e206f883910c_2_690x423.png" alt="Screen Shot 2020-07-23 at 3.25.35 PM" data-base62-sha1="1drsg7VDGg6hSiIJbQHHVXBoT5a" width="690" height="423" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08872fc7c6d6edc558cfd7024656e206f883910c_2_690x423.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08872fc7c6d6edc558cfd7024656e206f883910c_2_1035x634.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08872fc7c6d6edc558cfd7024656e206f883910c_2_1380x846.png 2x" data-dominant-color="3A3C41"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-07-23 at 3.25.35 PM</span><span class="informations">1394×856 80.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Save/Load</strong></p>
<ul>
<li>
<p>Update FCSV writer to save the position status flag</p>
</li>
<li>
<p>Update FCSV reader to read and set position status flag, set visibility</p>
</li>
</ul>

---

## Post #2 by @muratmaga (2020-07-24 04:15 UTC)

<p>Awesome <a class="mention" href="/u/smrolfe">@smrolfe</a>, thank you.</p>
<p>Would it be possible to address the confusion about selected vs highlighted fiducials as well? I am not entirely sure why we have two different modes of choosing LMs? (e.g., copy and paste seems to function only with highlight but not with select).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/5640c78886a7727b7094015fc4e185420690cbda.png" data-download-href="/uploads/short-url/cj1QO5GtfH7CmxUxTHQt2THXBSW.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/5640c78886a7727b7094015fc4e185420690cbda_2_690x360.png" alt="image" data-base62-sha1="cj1QO5GtfH7CmxUxTHQt2THXBSW" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/5640c78886a7727b7094015fc4e185420690cbda_2_690x360.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/5640c78886a7727b7094015fc4e185420690cbda_2_1035x540.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/5640c78886a7727b7094015fc4e185420690cbda_2_1380x720.png 2x" data-dominant-color="BBCCE1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1448×757 85.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2020-07-24 04:30 UTC)

<p>All sounds good.</p>
<aside class="quote no-group" data-username="smrolfe" data-post="1" data-topic="12714">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>Update “Add new markup at origin” button to add new unplaced markup. This button currently is not working for me with the intended function.</p>
</blockquote>
</aside>
<p>Yes, the button is currently broken (does not do anything) - it should be fixed.</p>
<p>In addition to what is described above:</p>
<ul>
<li>markup placement behavior should be changed so that if there are undefined control points then first they would be placed instead of adding new points.</li>
<li>markups table should be a reusable widget: you can either use qSlicerSimpleMarkupsWidget as a starting point or the segment list widget. Segment list widget already has status and filtering features (right-click to enable it) which will be <em>very</em> useful when you handle more than 10 control points.</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad54f2af949c7a3990e381d3c50be17f0dc48dfd.png" data-download-href="/uploads/short-url/oJmBmtjGlj3WgaplsAQcCk1Sh5z.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad54f2af949c7a3990e381d3c50be17f0dc48dfd_2_690x162.png" alt="image" data-base62-sha1="oJmBmtjGlj3WgaplsAQcCk1Sh5z" width="690" height="162" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad54f2af949c7a3990e381d3c50be17f0dc48dfd_2_690x162.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad54f2af949c7a3990e381d3c50be17f0dc48dfd_2_1035x243.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad54f2af949c7a3990e381d3c50be17f0dc48dfd.png 2x" data-dominant-color="D5DEE2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1050×247 15.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2020-07-24 04:44 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="12714">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Would it be possible to address the confusion about selected vs highlighted fiducials as well? I am not entirely sure why we have two different modes of choosing LMs?</p>
</blockquote>
</aside>
<p>“Selected” state of a control point is a property of the node (shared between all markups tables), which determines the color of the control point and is used by various modules (e.g., landmark registration only takes into account selected control points; vessel network extractor uses unselected points as source points, selected points as target points).</p>
<p>Highlight in the table is just temporary selection in one particular table so that you can operate on multiple points at once.</p>
<p>How would you change the GUI to make this more clear?</p>

---

## Post #5 by @muratmaga (2020-07-24 04:55 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="12714">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>How would you change the GUI to make this more clear?</p>
</blockquote>
</aside>
<p>I am not sure yet.</p>
<p>But right now, for SLicerMorph we need a mechanism that visually provides a clue of highlighted control points in the viewers (or vice versa, like picking a control point in the 3D viewer, should highlight in the table view). From our workshops we are seeing new users right also expecting that behavior.</p>
<p>From your description, ‘selected’ state seems like a fairly marginal use. In fact it sounds like both use cases can be covered by creating mutually exclusive fiducial nodes for selected and unselected subsets.</p>

---

## Post #6 by @lassoan (2020-07-24 05:51 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="5" data-topic="12714">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>From your description, ‘selected’ state seems like a fairly marginal use. In fact it sounds like both use cases can be covered by creating mutually exclusive fiducial nodes for selected and unselected subsets.</p>
</blockquote>
</aside>
<p>Easy toggling each control point is an important feature. You may need it at some point, too. Anyway, there is no conflict of interest here: Slicer core can be generic and you can use only the features that you need right now.</p>
<p>To make things very convenient, you probably want to add a custom landmark placement module to SlicerMorph. A very small, simple Python-scripted module would suffice, which would contain a few high-level widgets, which would be set up to work exactly as your users like it, hide things that you don’t need, and add convenience features, such as loading point set templates, maybe some quick import/export features, etc.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="5" data-topic="12714">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>But right now, for SLicerMorph we need a mechanism that visually provides a clue of highlighted control points in the viewers</p>
</blockquote>
</aside>
<p>This exists already: right-lick on the control point and choose “Toggle select point”.</p>
<p>If you need more temporary highlighting then “active” control point mechanism may be usable (this is in addition to selected/non-selected and defined/undefined state; it is just a display state). A control point (or curve) is highlighted when you hover over it or moving it. Highlighting is already propagated to all viewers and it could be quite easily displayed in the control point list, too. A limitation is that there is always only one active control point per context (i.e., one for the desktop mouse, and one for each virtual reality controller).</p>
<p>To have multiple selections and somewhat temporary selection state, the new control point table widget could offer a “direct select” mode. In this mode, the selection checkboxes could be hidden and row selection in the table widget could be synchronized with the control point’s selection state. You could enable this mode in your custom module (and maybe we could expose it in Markups module, too; similarly to how “Click to jump slices” mode can be enabled with a checkbox).</p>

---

## Post #7 by @chir.set (2020-07-24 15:14 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="12714">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>markup placement behavior should be changed</p>
</blockquote>
</aside>
<p>If you plan to make profound changes to Markups, I would suggest adding  more simple events like :</p>
<p>PointPrependEvent (added before the first, becoming first)<br>
PointAppendEvent (added after the last, becoming last)<br>
PointPositionChangedEvent (when changed in the list of control points)</p>
<p>Might be of interest.</p>
<p>Regards.</p>

---

## Post #8 by @smrolfe (2020-07-24 15:40 UTC)

<p>Thanks Andras. I have just one concern with the markup placement behavior:</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="12714">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>markup placement behavior should be changed so that if there are undefined control points then first they would be placed instead of adding new points.</p>
</blockquote>
</aside>
<p>Occasionally a user needs to skip a landmark (e.g. missing data, abnormality). If a landmark was skipped, it would not be possible to add new landmarks if the logic forced placement of all unplaced points first. I think you could make a case for keeping the current placement behavior and using the control point table to initiate placement.</p>
<p>One workaround might be to have a three toggle options in the status column (placed, not placed, skipped) that would let the placement logic skip over select unplaced points.</p>

---

## Post #9 by @smrolfe (2020-07-24 17:51 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="12714">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>How would you change the GUI to make this more clear?</p>
</blockquote>
</aside>
<p>I think having the selection toggle/checkboxes in the table along with cut/paste/delete tools that only work for highlighted points can be confusing. It would be nice to be able to select points with any method and use these tools. Unless I’m missing something, the only way to do this would be to highlight the selected points in the table individually.</p>
<p>Maybe a button to highlight all selected points could help?</p>

---

## Post #10 by @lassoan (2020-07-24 18:06 UTC)

<aside class="quote no-group" data-username="smrolfe" data-post="8" data-topic="12714">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>One workaround might be to have a three toggle options in the status column (placed, not placed, skipped) that would let the placement logic skip over select unplaced points.</p>
</blockquote>
</aside>
<p>This would not be a workaround but an elegant solution to add a state to indicate that a point should not be attempted to be placed. “Skipped” as state name is not bad, but maybe “missing” could be better, or maybe “unavailable” or “ignore”.</p>
<aside class="quote no-group" data-username="smrolfe" data-post="9" data-topic="12714">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>I think having the selection toggle/checkboxes in the table along with cut/paste/delete tools that only work for highlighted points can be confusing.</p>
</blockquote>
</aside>
<p>Yes, of course if a user does not need the additional flexibility and a simple transient selection state is sufficient then anything beyond that is “confusing”. The key is to find a way to “make simple things simple and complex things possible”. One option that I described above is to add a new operating mode to the control point table: “direct select mode”. In this mode, checkbox column would be hidden. Selecting/unselecting rows in the table would automatically select/unselect the control points.</p>
<aside class="quote no-group" data-username="smrolfe" data-post="9" data-topic="12714">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>Maybe a button to highlight all selected points could help?</p>
</blockquote>
</aside>
<p>I can see how a highlight selected/unselected points could be useful, especially when there are many points.</p>
<p>However, a more powerful and more sustainable solution would be to allow filtering based on selected state of the control point (in addition to search by text and filter by control point state undefined/unavailable/defined). Then you could easily create a custom list by search&amp;filtering and perform operations on all the points in the result set. For example, delete all could delete all control points that are displayed with the current search&amp;filter settings.</p>

---

## Post #11 by @smrolfe (2020-07-24 18:13 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="12714">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>However, a more powerful and more sustainable solution would be to allow filtering based on selected state of the control point (in addition to search by text and filter by control point state undefined/unavailable/defined). Then you could easily create a custom list by search&amp;filtering and perform operations on all the points in the result set. For example, delete all could delete all control points that are displayed with the current search&amp;filter settings.</p>
</blockquote>
</aside>
<p>That’s a great idea! And could easily be wrapped into the other updates to the table.</p>

---

## Post #12 by @ezgimercan (2020-07-24 18:57 UTC)

<p>First of all, so excited that Markups module is getting some much needed attention. Thanks, <a class="mention" href="/u/smrolfe">@smrolfe</a>!</p>
<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="12714" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This would not be a workaround but an elegant solution to add a state to indicate that a point should not be attempted to be placed. “Skipped” as state name is not bad, but maybe “missing” could be better, or maybe “unavailable” or “ignore”.</p>
</blockquote>
</aside>
<ol>
<li>
<p>Skipping one or more landmarks is a very common case when using template lists. Annotating landmarks in order is also very common and automatically moving to the next “unselected/unmarked” landmark on the list would be very helpful. But I also observed that sometimes it is easier to landmark points out of order. I think having an option to annotate a landmark point out of order would be good - without flagging points in between as “skipped/missing”. I’ve used other programs that does this by highlighting the point on the list: when the cursor is changed to “annotation” mode, if the user highlights another point on the list, that point is captured on the image. And then it can move to the next undefined point or go back to the first undefined point.</p>
</li>
<li>
<p>I might have missed this point in the discussion but from what I understand, before all points in a list are either placed or skipped, changing the cursor mode to landmark/annotate would not add a new point, right? So, there should be a  way to skip all points (for example by highlighting all and changing the flag).</p>
</li>
<li>
<p>Moving/reannotating or undefining (skipping) an already placed landmark. Undefining could be done by simply changing the flag. For moving or re-annotation (re-placing), it could be done by either changing the flag, or if there is a way to annotate a point by highlighting it (see 1 above), it could be done that way. And there is also the original way of moving landmarks on the views when not in fiducial placement mode.</p>
</li>
</ol>
<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="12714" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>However, a more powerful and more sustainable solution would be to allow filtering based on selected state of the control point (in addition to search by text and filter by control point state undefined/unavailable/defined). Then you could easily create a custom list by search&amp;filtering and perform operations on all the points in the result set. For example, delete all could delete all control points that are displayed with the current search&amp;filter settings.</p>
</blockquote>
</aside>
<p>I really like the idea of searching/filtering by name and state. Especially when working with large landmark templates, searching by name would be very useful. Not only delete but “lock”, “select”, “flag (finished/skipped/undefined)” actions can be applied to these filtered points.</p>

---

## Post #13 by @lassoan (2020-07-24 21:34 UTC)

<aside class="quote no-group" data-username="ezgimercan" data-post="12" data-topic="12714">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ezgimercan/48/4584_2.png" class="avatar"> ezgimercan:</div>
<blockquote>
<p>I also observed that sometimes it is easier to landmark points out of order. I think having an option to annotate a landmark point out of order would be good - without flagging points in between as “skipped/missing”. I’ve used other programs that does this by highlighting the point on the list: when the cursor is changed to “annotation” mode, if the user highlights another point on the list, that point is captured on the image. And then it can move to the next undefined point or go back to the first undefined point.</p>
</blockquote>
</aside>
<p>Yes, it would work like this in Slicer, too. You can click “place” button of in the table in any row to place that point. After that, if “persistent” mode is enabled then we would automatically offer placement of the next undefined point in the list.</p>
<p>We need to improve the toolbar as well, because currently it is not clear which point of which markups node would be placed when the user clicks the place button in the toolbar.</p>
<aside class="quote no-group" data-username="ezgimercan" data-post="12" data-topic="12714">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ezgimercan/48/4584_2.png" class="avatar"> ezgimercan:</div>
<blockquote>
<p>there should be a way to skip all points (for example by highlighting all and changing the flag)</p>
</blockquote>
</aside>
<p>We could do the same as in the segment list for segment status: you can select multiple rows and then change their state using right-click menu.</p>
<aside class="quote no-group" data-username="ezgimercan" data-post="12" data-topic="12714">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ezgimercan/48/4584_2.png" class="avatar"> ezgimercan:</div>
<blockquote>
<p>For moving or re-annotation (re-placing), it could be done by either changing the flag, or if there is a way to annotate a point by highlighting it (see 1 above), it could be done that way. And there is also the original way of moving landmarks on the views when not in fiducial placement mode.</p>
</blockquote>
</aside>
<p>Move: you can drag-and-drop any point.<br>
Re-place: you will be able to do it by clicking on the “Place” button in the corresponding row in the table.<br>
Undefine: you will be able to right-click in the table or in a view and setting state to undefined or delete.</p>
<aside class="quote no-group" data-username="ezgimercan" data-post="12" data-topic="12714">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ezgimercan/48/4584_2.png" class="avatar"> ezgimercan:</div>
<blockquote>
<p>I really like the idea of searching/filtering by name and state. Especially when working with large landmark templates, searching by name would be very useful. Not only delete but “lock”, “select”, “flag (finished/skipped/undefined)” actions can be applied to these filtered points.</p>
</blockquote>
</aside>
<p>Agreed. This has been proven to work very well for segment lists already: it is really easy to handle large atlases that contains hundreds of segments.</p>
<p><a class="mention" href="/u/smrolfe">@smrolfe</a> Since it seems that we will need most of the features of the segments table view, I would recommend to create a new qSlicerMarkupsControlPointsTableView class (and corresponding model and proxy model classes) based on qMRMLSegmentsTableView (and related classes).</p>

---

## Post #14 by @smrolfe (2020-07-27 21:44 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="13" data-topic="12714">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/smrolfe">@smrolfe</a> Since it seems that we will need most of the features of the segments table view, I would recommend to create a new qSlicerMarkupsControlPointsTableView class (and corresponding model and proxy model classes) based on qMRMLSegmentsTableView (and related classes).</p>
</blockquote>
</aside>
<p>Sounds great. I’m scheduling time next week to tackle this.</p>

---
