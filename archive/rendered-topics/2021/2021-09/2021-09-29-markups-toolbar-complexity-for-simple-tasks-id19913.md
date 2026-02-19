---
topic_id: 19913
title: "Markups Toolbar Complexity For Simple Tasks"
date: 2021-09-29
url: https://discourse.slicer.org/t/19913
---

# Markups toolbar complexity for simple tasks

**Topic ID**: 19913
**Date**: 2021-09-29
**URL**: https://discourse.slicer.org/t/markups-toolbar-complexity-for-simple-tasks/19913

---

## Post #1 by @jamesobutler (2021-09-29 13:47 UTC)

<p>There have been recent changes to how users create and place markups using the toolbar. These changes have been written up in the following post.</p>
<aside class="quote quote-modified" data-post="1" data-topic="19871">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/changes-to-the-markups-module/19871">Changes to the Markups Module</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Several updates to the Markups module and the addition of a Markups toolbar were added in commit: <a href="https://github.com/Slicer/Slicer/commit/09d12ae6f7598fe8490b691d17a35dcca5bd344a" class="inline-onebox" rel="noopener nofollow ugc">ENH: Improve control point state management and add markups toolbar · Slicer/Slicer@09d12ae · GitHub</a> and are available in the latest preview version. 
The <a href="https://discourse.slicer.org/t/proposed-changes-to-markups-to-support-unplaced-points/12714">motivation for these changes</a> was to add support for unplaced or missing control points. These states make it possible to create landmark templates for efficient placing of pre-named points, which is a common feature in other landmarking software. …
  </blockquote>
</aside>

<p>It appears to be a great change to support easier functionality when using the markups Fiducial object for registration purposes, however it comes with a side effect of additional complexity for other markups such as “Line” which are primarily used for more simple measurement tasks. I hope with this thread we can brainstorm ideas to support the new functionality for the markups Fiducial object, but help make the other markups simpler to use again.</p>
<p>In previous versions of Slicer, to place a line (aka ruler) node, ROI node, angle node, etc you would go to the mouse mode toolbar and click in the menu to add a new node for the object and also enter placement mode. You would then place your 2 or 3 points, maybe use your mouse to adjust a point, view your measurement or accept your ROI for cropping and then be done. A fairly simple task with not a lot of interaction involved and when interaction is needed you can just use the mouse to move a position or right-click to delete or whatever. To place a second line I could simply click on the place button which now had a default action for the line node and create and place another object.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/9400ebda63bb26e519fb41e906aab8e3f33d1a00.jpeg" data-download-href="/uploads/short-url/l7iDEfWxtoN4rp7ZgAH59R75ttu.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/9400ebda63bb26e519fb41e906aab8e3f33d1a00.jpeg" alt="image" data-base62-sha1="l7iDEfWxtoN4rp7ZgAH59R75ttu" width="690" height="480" data-dominant-color="565555"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">719×501 65.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, now to follow the same pathway I must, toggle the markups toolbar from the mouse mode toolbar, go over to the markups toolbar, find my line node button in a large group of new widgets, then go to the slice view to place my line. First, a minor point in that the movement of the mouse across the screen is a bit annoying as default behavior to go from one toolbar to another.  Yes, the toolbars can be rearranged, but by default is not as simple as before.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb2fc6132dbbc36b545b564a14631e18a93c8371.png" data-download-href="/uploads/short-url/zQ6co8u6Uj9iX75hgxlRigKkTyp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb2fc6132dbbc36b545b564a14631e18a93c8371_2_690x324.png" alt="image" data-base62-sha1="zQ6co8u6Uj9iX75hgxlRigKkTyp" width="690" height="324" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb2fc6132dbbc36b545b564a14631e18a93c8371_2_690x324.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb2fc6132dbbc36b545b564a14631e18a93c8371_2_1035x486.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb2fc6132dbbc36b545b564a14631e18a93c8371.png 2x" data-dominant-color="8F8A8A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1200×564 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Second, the bigger issue is that there are all these new buttons in the new markups toolbar that are intimidating when going to just place a line node. It gives the impression as though I will need all these options for line node placement when really that is not the case. Node selection, color selector, place button, trash can to delete last placed control point or to unset control points, or other options for visibility and lock states. These are for the most part not needed at all for simple markups for measurement purposes. I do see the value for these for when dealing with Fiducial objects and manipulating/adding control points to various landmarking template lists across Fiducial objects, however they add additional complexity for simple tasks of placing a markup for quick measurement.</p>
<p>How can we make markups for measurement purposes simple without showing a lot of options that can be intimidating to users? There seems to be a split in the need of options between the “Fiducial” objects need for position status (unset, set, restore, skip), switching between nodes, setting colors to various groups, etc and the simple needs for less complex workflows of the other markups.</p>

---

## Post #2 by @muratmaga (2021-09-29 16:08 UTC)

<p>While I agree that there are things we need to streamline with the new markups toolbar, I am not sure if the behavior is all that different, or complicated for simple things like measuring lines, angles etc.</p>
<p>This is how it is in stable<br>
</p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b98e13624aa2ee29f7902e244f6088c52d781721.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b98e13624aa2ee29f7902e244f6088c52d781721.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b98e13624aa2ee29f7902e244f6088c52d781721.mp4</a>
    </source></video>
  </div><p></p>
<p>This is how it is now with new toolbar<br>
</p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2d59e572ab0183584832a8c110df608d67a2b77.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2d59e572ab0183584832a8c110df608d67a2b77.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2d59e572ab0183584832a8c110df608d67a2b77.mp4</a>
    </source></video>
  </div><p></p>
<p>To me that doesn’t seem like a change that should confuse a user who is used to the old way. And it won’t matter for new users, because that’s the interface that they will learn.</p>
<p>The change of place mode button as a toggle is an intentional change to make sure that long time users of Slicer are aware the things are different in terms of markup placement (that is there is now a specific toolbar to use).</p>

---

## Post #3 by @jamesobutler (2021-09-29 16:38 UTC)

<p>The main issue for line node creation using toolbars is that now I have to show a toolbar (“Markups toolbar”) that has all these new options which is intimidating when I just need to use one of them for line node (create line node button). It’s the fact that there are more widgets to navigate through for a simple task like measuring some with a line node. It’s the same type principle of why advanced sections exist in a collapsed state to avoid viewing things that are typically unnecessary. For the case of line nodes and other simple measurement markups, all the other options in the new markups toolbar are unnecessary.</p>

---

## Post #4 by @muratmaga (2021-09-29 17:14 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="3" data-topic="19913">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>The main issue for line node creation using toolbars is that now I have to show a toolbar (“Markups toolbar”) that has all these new options which is intimidating when I just need to use one of them for line node (create line node button).</p>
</blockquote>
</aside>
<p>I respectfully disagree with that. it is the same set of icons as before on the left hand of the toolbar. We simply rearranged in a horizontal view so all markups types are visible. We can change this back to dropbutton as it was before, I don’t have any issue with that. The right handside of the toolbar contains a mix of old and new icons (for the new clear, edit functionality). If a user never used any those before, I suspect that they will pay no heed to them.</p>
<p>The previous interface was simple, but if you are only going to do one type of markup node (perhaps lines, or angles). Once you start using curves and fiducials together, there is really no way to know what node you are editing/creating, what others are etc. That required users switching to Markups (or data) module and use half of those features there for simple things (like color change, rename a node etc), and we are back to users switching to different modules for simple tasks.</p>

---

## Post #5 by @jamesobutler (2021-09-29 17:22 UTC)

<p>Yes, user may not need any of those new widgets in the markups toolbar which is the problem. Compared to the old method, creating lines, angles, etc measurement markups is not as simple as before because you have to search through more things that you’re not going to use.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="19913">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>The previous interface was simple, but if you are only going to do one type of markup node (perhaps lines, or angles). Once you start using curves and fiducials together, there is really no way to know what node you are editing/creating, what others are etc</p>
</blockquote>
</aside>
<p>This brings back up the main topic I’m hoping to address which is how to keep simple measurement markups simple without other widgets as distractions, while also supporting the cases you have detailed where some markups do require more interaction for things like registration.</p>

---

## Post #6 by @lassoan (2021-09-29 17:43 UTC)

<p>Now that we have right-click menu for markups with many actions available there (and you can open the full Markups module menu from there), I agree that you could manage measurements by using the place mode button and Markups module (without showing the toolbar). But we had a lot of issues due to the dual meaning of the place button: create new markup / add point to existing markup.</p>
<p>OsiriX has a single place button for adding new markup and adding new points (same way as Slicer had it before), and as far as I can tell, it is simply not possible add points to existing curves (it does not have point lists).</p>
<p><strong>Using only the mouse mode toolbar, how would you distinguish between adding new points to an existing markup or create a new markup? How would you indicate that you have placed enough points (in the current curve or fiducial list) and you would like to start a new one?</strong></p>
<p>I agree Mouse move between the left side of the screen and the viewers is not good. We could make things easier by adding keyboard shortcuts and/or making the toolbar vertical-friendly (do something with the node selector) and snap it to the right side of the screen by default.</p>
<p>We will probably need to have a docking widget for fiducial placement that can be used while being in a module (so that the user can see point placement progress and choose the next point to place in any module, without the need to switch to the Markups module), similarly to what is done in Orthodontic Analysis extension:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22f8ba5ddfb5de99267eb70a92861857ad7f3042.jpeg" data-download-href="/uploads/short-url/4Zn88Aw6ul40qwqWHnO1wvKnE3w.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/22f8ba5ddfb5de99267eb70a92861857ad7f3042_2_690x421.jpeg" alt="image" data-base62-sha1="4Zn88Aw6ul40qwqWHnO1wvKnE3w" width="690" height="421" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/22f8ba5ddfb5de99267eb70a92861857ad7f3042_2_690x421.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/22f8ba5ddfb5de99267eb70a92861857ad7f3042_2_1035x631.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/22f8ba5ddfb5de99267eb70a92861857ad7f3042_2_1380x842.jpeg 2x" data-dominant-color="5C5C59"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1173 189 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>We should think about how to distribute features between the mouse mode toolbar, markups toolbar, measurements/landmarking docking widget, and markups module, which fulfills requirements of all use cases and respects “makes simple things simple and complex things possible”.</p>
<p><strong>To facilitate this discussion, would you mind briefly summarizing your use cases (what would be the ideal way the features would work)?</strong></p>
<p>Just to avoid having use cases spread across several posts, as an experiment, let’s try to use the Slicer GitHub wiki for this. Add your use case to <a href="https://github.com/Slicer/Slicer/wiki/Markups-rework">this page</a>. In the end we’ll see if we want to leave the use cases there or bring the result back here and remove that labs page.</p>

---

## Post #7 by @jamesobutler (2021-09-30 13:37 UTC)

<p>Yes, I will provide ideas and use case information to the above bolded items. I have currently been brainstorming and trying to organize thoughts on the topic in my notes so I can provide clear and detailed information. A very short summary of what I will be providing is that markups for measurement follow the “Create and place” action with little to no editing after the original interaction of placing. When there is interaction after the initial interaction has ended, points are moved by mouse left-click, more infrequently deleted by mouse right-click menu option and more infrequently selecting curves to ctrl+mouse left-click to insert additional points.</p>

---

## Post #8 by @mikebind (2021-10-01 00:02 UTC)

<p>I added a set of the use cases which jumped to mind for me on the wiki page.  For my purposes, the new toolbar is great and much easier and clearer to work with than the old version.  However, I only very rarely use the simple ruler or angle measurement tools.  I use the fiducials, open curves, planes, and ROI’s all the time, and the clarifications around when a new node will be used for a new point placement vs an additional point to a current node, as well as the improvements facilitating landmark templates, are very helpful.</p>

---

## Post #9 by @jamesobutler (2021-10-01 01:51 UTC)

<p>I’ve added use cases to the wiki labs page. Explains about “Quick measurements” where markups are created and points placed in one interaction (“Create-and-place”). Markup control points are usually not removed or added after the initial interaction. Since the markup is easy to redo, it makes sense to just recreate from scratch. Often deleted with right-click menu.</p>

---

## Post #10 by @jamesobutler (2021-10-03 18:36 UTC)

<p>Linking this thread below which began the discussion about how to improve knowledge of whether a new markups node was created or new control point added to a markups node.</p>
<aside class="quote quote-modified" data-post="1" data-topic="9016">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/markups-node-creation-icon-is-confusing-users/9016">Markups node creation icon is confusing users</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Currently same icon is used to create both a new fiducial in a list [1 below], and a new fiducial list [2] in the Markups module. This behavior is confusing to the users. I propose to modify the node creating one slightly to make it less similar. It might have visual clues to what it does (e.g., add three dots, have word Node/List on it etc). 
[1] [image] 
[2]  <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/5819b05df11d4505c4e17fb49d71c951d62cb511.png" data-download-href="/uploads/short-url/czn3s3qM9gNCXmlVzs1iP0jKDAZ.png?dl=1" title="image" rel="noopener nofollow ugc">[image]</a>
  </blockquote>
</aside>

<p><strong>Summary:</strong></p>
<ul>
<li>It was confusing if you “place a fiducial” if that means you are placing a node or placing a control point for a node because the vtkMRMLMarkupsFiducialNode is a list of control points.</li>
<li>Some issues brought up included the overall size of an updated markups related toolbar as the default state is what users will use first and will not bother to customize. Space concerns started the topic of how best to support more multi-module functionality availability at the same time. This includes how to have more Markups module functionality availability at the same time of using another module. Ribbon interface was mentioned.</li>
</ul>
<p>^ This topic is similar to what <a class="mention" href="/u/pieper">@pieper</a> mentioned in a weekly hangout about how best to support multi module use cases when space concerns are being brought up. The markups toolbar with a node selector uses more space. It is trying to add Markups module functionality to the toolbar as a solution to support that Markups functionality while actively in another module. Will this spark more modules to just add their functionality in a toolbar as a solution for multi-module workflows?</p>
<p>A lot of the vtkMRMLMarkupsFiducialNode use cases are paired with other modules for landmarking purposes. So a multi-module solution of functionality is needed. However vtkMRMLMarkupsLineNode is primarily a single module workflow as the distance measurement is provided by the markups module and can be manipulated in the slice views without a real need of viewing the module.</p>

---

## Post #11 by @lassoan (2021-10-03 19:25 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="10" data-topic="19913">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Will this spark more modules to just add their functionality in a toolbar as a solution for multi-module workflows?</p>
</blockquote>
</aside>
<p>Adding a toolbar does not make sense for all modules but only for those that provide features that are intended to be used while in another module. Current examples are Sequences, Scene Views, Virtual Reality, and Markups.</p>
<p>I would hesitate to make multiple module GUIs displayable at the same time, but allowing multiple toolbars seems like a good tradeoff.</p>

---

## Post #12 by @jamesobutler (2021-10-12 16:50 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Are we at a time now based on the use cases to brainstorm towards making markups actions simple for measurement purposes?</p>

---

## Post #13 by @lassoan (2021-10-13 04:34 UTC)

<p>Yes, we can assume that we won’t get anymore use case descriptions. Probably the best would be to discuss this during a call. Would all interested people be available to join the next Slicer weekly meeting (Tuesday at 10am)?</p>

---

## Post #14 by @jamesobutler (2021-10-13 13:28 UTC)

<p>Yes, unusually I can actually attend this next meeting if we want to discuss more about this topic then.</p>

---

## Post #15 by @smrolfe (2021-10-13 15:46 UTC)

<p>I will be available to attend next week also.</p>

---

## Post #16 by @ezgimercan (2021-10-19 19:45 UTC)

<p>Following up <a href="https://discourse.slicer.org/t/2021-10-19-weekly-meeting/20218/3">this</a>, on adding a measurement toolbar (or annotation toolbar): This is a functionality most DICOM viewers have. They even have text, arrow, ellipse, circle, pen options - but instead of markups, these are annotations (kinda like Zoom or video call annotations on the screen). With the exception of ruler and angles, they don’t return any measurements. I think a user with a medical background would expect to see this in Slicer. It is a very common thing for doctors to want to measure something to just see the number.  “Let’s see how wide the eyes are, hmm, 2.4 cm is wide for this age…” kind of situation.</p>
<p>See the web-based viewer our hospital uses:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e547c9011a9fc1fd21579f6d9c2f6b65e7499fe.png" data-download-href="/uploads/short-url/dstTq2qerMRPZXCUBkFexC5AMPQ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e547c9011a9fc1fd21579f6d9c2f6b65e7499fe_2_690x79.png" alt="image" data-base62-sha1="dstTq2qerMRPZXCUBkFexC5AMPQ" width="690" height="79" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e547c9011a9fc1fd21579f6d9c2f6b65e7499fe_2_690x79.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e547c9011a9fc1fd21579f6d9c2f6b65e7499fe.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e547c9011a9fc1fd21579f6d9c2f6b65e7499fe.png 2x" data-dominant-color="555654"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">857×99 17.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0db0051b406de37b6ccea939913a781f9c915770.png" data-download-href="/uploads/short-url/1X5klgyIb6nynuNacH4toAFUREs.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0db0051b406de37b6ccea939913a781f9c915770_2_283x499.png" alt="image" data-base62-sha1="1X5klgyIb6nynuNacH4toAFUREs" width="283" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0db0051b406de37b6ccea939913a781f9c915770_2_283x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0db0051b406de37b6ccea939913a781f9c915770_2_424x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0db0051b406de37b6ccea939913a781f9c915770.png 2x" data-dominant-color="4D5A54"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">450×794 64.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Previous mouse mode button with all markups nodes available under the expandable menu provided this functionality for users who didn’t care about the line markups node as much as being able to see the distance. With the current Markups toolbar, it is still possible, and as a heavy user of fiducials, it is still very straightforward and easy for me. But I understand the complexity this toolbar might present for a new user. If the idea is to simplify the use of Markups for some users, I like the option of adding a measurements toolbar - which uses the functionality of Markups and still creates lines, ROIs etc. in the scene but hides all the extra functions.</p>

---
