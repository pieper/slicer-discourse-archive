# Restoring scene view duplicates scene heirarchy

**Topic ID**: 22025
**Date**: 2022-02-17
**URL**: https://discourse.slicer.org/t/restoring-scene-view-duplicates-scene-heirarchy/22025

---

## Post #1 by @hherhold (2022-02-17 15:46 UTC)

<p>This harkens back to a number of discussions from months past on Scene Views, which I haven’t used in quite a while (and now I’m remembering some of the reasons why). One of the discussions linked below.</p>
<p>So right now, when I capture a scene view and later restore it, things <em>appear</em> to be okay. But when I check the Data module, restoring the scene view basically duplicates everything in the scene. Subsequent restores make yet another copy, and another.</p>
<p>As nobody’s really talked about scene views in quite some time, maybe it should be deprecated if it’s not going to be worked on?</p>
<p>Link to one of the old discussions:</p>
<aside class="quote quote-modified" data-post="1" data-topic="497">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/what-scene-views-are-supposed-to-do/497">What scene views are supposed to do?</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    We experienced many problems related to scene views, seen many workarounds in many places in the code, and there are many open issues caused by or related to scene views. 
The main problem seems to be that it is unclear what information scene views should store and restore. 
Should it be enough for scene views to store display information of nodes, view layout, view settings, and camera settings? 
If that’s true, we could simplify the scene view implementation a lot, because we would not need to…
  </blockquote>
</aside>


---

## Post #2 by @pieper (2022-02-17 17:29 UTC)

<p>I think that discussion from 5 years ago is basically still up to date.  Which is to say, yes, the feature is weird and unreliable.  I’d be happy to see it gone or replaced with something much simpler.</p>

---

## Post #3 by @muratmaga (2022-02-17 17:56 UTC)

<p>It is not very useful as is, so it can be axed. But a functionality to recover camera positions, light settings, etc is needed. Your suggestion to save the states as mrml files is not a very practical one, as in situations like <a class="mention" href="/u/hherhold">@hherhold</a> you might be making dozen figure plates and keeping them all separate mrml files will be too much a confusion.</p>
<p>So, maybe it is time to have that conversation about what can replace that?</p>

---

## Post #4 by @lassoan (2022-02-18 04:23 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="22025">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>It is not very useful as is, so it can be axed.</p>
</blockquote>
</aside>
<p>It is very useful feature and it can be fixed with today’s Slicer infrastructure much more easily than years ago. We could save display nodes (and camera and slice nodes, maybe the layout node) to sequence nodes, essentially automating the manual workflow that I showed <a href="https://discourse.slicer.org/t/new-feature-basic-support-for-physically-based-rendering-pbr/21725/17">here</a>.</p>

---
