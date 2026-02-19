---
topic_id: 21635
title: "Add Center All Cameras To Control Point Right Click Menu"
date: 2022-01-26
url: https://discourse.slicer.org/t/21635
---

# Add "Center all cameras" to control point right-click menu?

**Topic ID**: 21635
**Date**: 2022-01-26
**URL**: https://discourse.slicer.org/t/add-center-all-cameras-to-control-point-right-click-menu/21635

---

## Post #1 by @hherhold (2022-01-26 15:35 UTC)

<p>Some of my scans have rather ungainly specimens with elongate structures and lots of intricate morphology (stick insects, mantises). The center of rotation for the entire scene is often not exactly where I would like it to be, and translating and rotating using left-middle-right mouse clicks and drags has become somewhat of an imperfect navigational art form. I’ve found the right-click “Center all cameras” option in the control point list to be <em>very</em> useful, however I often have well over 100 control points in a given control point list and it can be tedious to scroll through and find the one in question.</p>
<p>I was wondering if it would be generally useful to add a “Center all cameras” command in the right-click-on-a-control-point menu (the one with “rename control point”, etc). I’ve looked into this a little bit and it looks like it would just require changes to <code>qSlicerSubjectHierarchyMarkupsPlugin</code>. This does result in growing that menu a bit, however, and if it’s not generally useful, it would just add clutter.</p>
<p>Thoughts? Does anybody else re-center the camera on a given control point a lot?</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @jamesobutler (2022-01-26 15:51 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="1" data-topic="21635">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>I’ve found the right-click “Center all cameras” option in the control point list to be <em>very</em> useful</p>
</blockquote>
</aside>
<p>I was unable to find this option. Do you mean “Refocus all cameras”?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8bf8c95622c3f9bc39b5b4ca6414f3c2cf61a9a9.png" data-download-href="/uploads/short-url/jYfoeNHwp0ImM3eb5iNLeRYy22l.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bf8c95622c3f9bc39b5b4ca6414f3c2cf61a9a9_2_517x302.png" alt="image" data-base62-sha1="jYfoeNHwp0ImM3eb5iNLeRYy22l" width="517" height="302" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bf8c95622c3f9bc39b5b4ca6414f3c2cf61a9a9_2_517x302.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8bf8c95622c3f9bc39b5b4ca6414f3c2cf61a9a9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8bf8c95622c3f9bc39b5b4ca6414f3c2cf61a9a9.png 2x" data-dominant-color="E3E6E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">712×416 35.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="hherhold" data-post="1" data-topic="21635">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>however I often have well over 100 control points in a given control point list and it can be tedious to scroll through and find the one in question.</p>
</blockquote>
</aside>
<p>It has been discussed in another thread about adding a filter option to this table similar to how Segment Editor can have a filter option shown (right-click “Show Filter Bar”) to quickly find a segment in a large list of segments. This may be beneficial to this effort in finding the control point you want quicker.</p>
<p>Providing continuity between right-click context options in the control points table as with the right-click context option of the control point in the slice view may make sense too as you suggest.</p>

---

## Post #3 by @hherhold (2022-01-26 16:53 UTC)

<p>Yep, that’s the one - apologies for the mis-naming.</p>
<p>I can look into adding it to the control-point right-click, it does not look too intrusive but I may have a few questions on details. What do you think?</p>
<p>-Hollister</p>

---

## Post #4 by @hherhold (2022-01-26 21:38 UTC)

<p>I have this working, if there’s general interest I can submit a pull request.</p>
<p>-Hollister</p>

---
