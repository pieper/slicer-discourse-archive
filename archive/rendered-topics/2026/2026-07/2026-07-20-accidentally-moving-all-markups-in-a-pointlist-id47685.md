---
topic_id: 47685
title: "Accidentally moving all markups in a pointList"
date: 2026-07-20
url: https://discourse.slicer.org/t/47685
last_bumped: 2026-07-20T15:05:57.108Z
---

# Accidentally moving all markups in a pointList

**Topic ID**: 47685
**Date**: 2026-07-20
**URL**: https://discourse.slicer.org/t/accidentally-moving-all-markups-in-a-pointlist/47685

---

## Post #1 by @muratmaga (2026-07-20 04:14 UTC)

<p>This was happening before but I though it was fixed. I can replicate this on MacOS 5.12.1 middle click and drag, moves the entire pointList. interaction is not enabled, so I would consider this a bug.</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efe06270a2712e34356dd0db25135db47a308ebb.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e773466ef2f2d74c7e7c4651e580e68808a059f.jpeg" data-video-base62-sha1="ye2R8BJkUf1TYT4rYMGO5LLUasX.mp4">
  </div><p></p>

---

## Post #2 by @chir.set (2026-07-20 09:49 UTC)

<p>I always considered that as an interesting feature. Undo/Redo cancels the displacement nicely.</p>

---

## Post #3 by @jamesobutler (2026-07-20 14:30 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="47685">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>interaction is not enabled</p>
</blockquote>
</aside>
<p>How do you determine this? Through context-menu or from Markups module? It appears the context menu interaction checkable item refers to interaction handle visibility and is different from the Interaction locked state of the Control Points.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/6394c733aef2edf3d6a3c60111944d387b3f7fcf.png" data-download-href="/uploads/short-url/ecW1z4uBYb6n9fe7VKXDhLpneVh.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/6394c733aef2edf3d6a3c60111944d387b3f7fcf.png" alt="image" data-base62-sha1="ecW1z4uBYb6n9fe7VKXDhLpneVh" width="639" height="122"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">639×122 3.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4cc22b90cfc666234dd182ad5323bc0633fff560.png" data-download-href="/uploads/short-url/aX2ijGheVUjpXOKpUfBw13R8lO0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4cc22b90cfc666234dd182ad5323bc0633fff560.png" alt="image" data-base62-sha1="aX2ijGheVUjpXOKpUfBw13R8lO0" width="448" height="499" data-dominant-color="EEEEF1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">506×564 21.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @muratmaga (2026-07-20 14:51 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="2" data-topic="47685">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Undo/Redo cancels the displacement nicely.</p>
</blockquote>
</aside>
<p>Where is the undo? I am not aware of it. Is it finally done?</p>

---

## Post #5 by @muratmaga (2026-07-20 14:52 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="3" data-topic="47685">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>It appears the context menu interaction checkable item refers to interaction handle visibility</p>
</blockquote>
</aside>
<p>No that interaction lock is not set. I do need to be able to interact with the individual points. I refer to the interaction widget which is specifically for this kind of rotation/translation movement.</p>

---

## Post #6 by @jamesobutler (2026-07-20 14:55 UTC)

<p>Moving an entire Markups node by mouse wheel click has been a feature for a while. The way to prevent translation block of the control points would be with the control point locked state being set.</p>

---

## Post #7 by @muratmaga (2026-07-20 14:59 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="6" data-topic="47685">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Moving an entire Markups node by mouse wheel click has been a feature for a while.</p>
</blockquote>
</aside>
<p>But it is a dangerous operation without a reliable undo operation. We can’t translate model or volume like that. Why is that enabled for markups?</p>
<p>It is particularly concerning and confusing, since middle button and drag has indeed a specific function to drag the camera. But if this hits a markup this moves it without anyway to undo.</p>

---

## Post #8 by @chir.set (2026-07-20 15:04 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="47685">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Where is the undo? I am not aware of it. Is it finally done?</p>
</blockquote>
</aside>
<p>It’s not in Slicer core, I am using an external <a href="https://gitlab.com/chir-set/Tools7/-/tree/master/ManyThingsToolBar#4-markups-undoredo-functions" rel="noopener nofollow ugc">module</a> for that. It has been working seamlessly the few times I needed that.</p>

---

## Post #9 by @muratmaga (2026-07-20 15:05 UTC)

<p>Yes, that’s the one also available in SlicerMorph. But it is not in the core and has to be enabled manually.</p>
<p>This is not a plea for myself. A lot of people use pointLists to do manual anatomical landmarks on 3D data whether clinical or biological. It is extremely frustrating to accidentally mess up your data you spend 10 minutes creating by a simple mistake without the option of undo. We are modifying user data without consent, and in a destructive way, which none of the modules I am aware of does it in this way.</p>
<p>This is the kind of thing that makes Slicer frustrating.</p>
<p>I can’t think of one, but if there is a need for this use case, then this should be an option that can be easily turned off and on (without using interaction lock, which disables every kind of interaction, which is non-starter).</p>

---
