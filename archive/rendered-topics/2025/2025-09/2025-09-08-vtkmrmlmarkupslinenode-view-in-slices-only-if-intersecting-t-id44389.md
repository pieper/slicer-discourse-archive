---
topic_id: 44389
title: "Vtkmrmlmarkupslinenode View In Slices Only If Intersecting T"
date: 2025-09-08
url: https://discourse.slicer.org/t/44389
---

# vtkMRMLMarkupsLineNode view in slices only if intersecting the slice plans

**Topic ID**: 44389
**Date**: 2025-09-08
**URL**: https://discourse.slicer.org/t/vtkmrmlmarkupslinenode-view-in-slices-only-if-intersecting-the-slice-plans/44389

---

## Post #1 by @sarafv (2025-09-08 14:56 UTC)

<p>Hi!</p>
<p>There is a way to hide the control points of a vtkMRMLMarkupsLineNode in 2d views when the control points are not in the visible 2D Slices of Back/Foreground Volumes</p>
<p>thanks!</p>
<p>Sara</p>

---

## Post #2 by @sarafv (2025-09-09 09:49 UTC)

<p>I tried to hide by tuning 2D Displays parameters on Markups Module. I think that the “projection visibility check button is not working as expected in 5.8 version.</p>
<p>I’ve just tried on 5.9 and it is working <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=14" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #3 by @sarafv (2025-09-09 10:26 UTC)

<p>Same thing on scripting tests, on 5.9 displayNode.SetSliceProjection is working but not in 5.8 (on ubuntu22)</p>

---

## Post #4 by @cpinter (2025-09-09 11:22 UTC)

<p>Thank you for verifying that this works in the preview version! If there is any questions left about this let us know.</p>

---

## Post #5 by @sarafv (2025-09-09 11:29 UTC)

<p>Hi Csaba,</p>
<p>Sorry for the mess. The problem is not the version sorry, I just posted a new topic. The proble apperars in reformat mode only !!!</p>
<p>I aks Andras to erase this topic</p>

---

## Post #6 by @cpinter (2025-09-09 11:32 UTC)

<aside class="quote no-group" data-username="sarafv" data-post="5" data-topic="44389">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sarafv/48/1809_2.png" class="avatar"> sarafv:</div>
<blockquote>
<p>I aks Andras to erase this topic</p>
</blockquote>
</aside>
<p>I think this is fine here, we usually do not completely erase anything from the forums. Let me just reference the follow-up ticket:</p>
<aside class="quote" data-post="1" data-topic="44401">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sarafv/48/1809_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/markups-control-points-2d-views-projections-on-reformat-mode/44401">Markups control Points 2D Views projections on Reformat Mode</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #000000;" data-drop-close="true" class="badge-category --style-square " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
    </div>
  </div>
  <blockquote>
    Hello, 
Following and correcting previous topic about hiding projections of control points, I’v juste realize that the problem with displayNode.SetSliceProjection happens only when 2D  views are on Reformat Mode, the projection of all the control points are visibles and there is no way to hide them with displayNode.SetSliceProjection, whether  in the 5.9  or 5.8 version 
Sara
  </blockquote>
</aside>

<p>Yes in this case it does seem like a bug.</p>

---

## Post #7 by @sarafv (2025-09-09 11:39 UTC)

<p>Ok, because I’m upgrading some modules and this is a problem for me! <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=14" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"></p>

---
