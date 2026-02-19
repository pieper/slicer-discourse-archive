---
topic_id: 17582
title: "Subject Level Visibility Button Works Only Partially"
date: 2021-05-12
url: https://discourse.slicer.org/t/17582
---

# Subject Level visibility button works only partially

**Topic ID**: 17582
**Date**: 2021-05-12
**URL**: https://discourse.slicer.org/t/subject-level-visibility-button-works-only-partially/17582

---

## Post #1 by @muratmaga (2021-05-12 04:32 UTC)

<p>It appears that setting the visibility off in subject level does not hide volume in slice views. To replicate:</p>
<ol>
<li>Download and render MRHead.</li>
<li>Create a single fiducial on MRHead 3D view.</li>
<li>Center the slice views on fiducial</li>
<li>create a new subject and nest both MRHead and fiducial node beneath it.</li>
<li>Turn off the visibility for the subject level and observe that all 3D views are turned off, as well as visibilty of fiducial in 2D view, but the volume in slice views remains visible.</li>
</ol>
<p>Replicated in latest stable and a preview version from 4/22.</p>

---

## Post #2 by @cpinter (2021-05-12 10:26 UTC)

<p>Visibility of volumes and that of any other data type in Slicer works quite differently.</p>
<ol>
<li>Volumes can be visualized in the slices or as volume rendering, which are very different. Volume rendering works similarly to “normal” displayed objects, however it is only in 3D, and one of the two main ways of showing volumes in 3D (slice models is the other), moreover, volume rendering needs to be setup by the user most of the time because the default settings are typically not sufficient for proper display.</li>
<li>Volume visibility in slices is driven by so called composite nodes that specify background, foreground, and label volume, as opposed to the “display node for data node” approach mentioned above.</li>
<li>There are different kinds of layouts: some suggest showing the same volume in every view, others are for comparing two or more, etc.</li>
</ol>
<p>So there are many decisions to be made when one wants to “just turn on” visibility for a volume, and hence we have never reached a consensus about how to approach it, especially that different use cases need different behaviours and defaults. There have been several implementations for this, but none of them worked in each case.</p>
<p>This is a bit of a pandora’s box, but if you have time to think all the cases through and draft a plan then we welcome new ideas!</p>

---

## Post #3 by @jamesobutler (2021-05-12 12:18 UTC)

<p>There’s a Slicer Issue on this topic: <a href="https://github.com/Slicer/Slicer/issues/4961" class="inline-onebox" rel="noopener nofollow ugc">Controlling visibility of volume node children in subject hierarchy · Issue #4961 · Slicer/Slicer · GitHub</a>.</p>
<p>Could also review past discussion at</p><aside class="quote quote-modified" data-post="1" data-topic="11850">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/hiding-patient-in-hierarchy/11850">Hiding patient in hierarchy</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    When I click on the eyeball at the patient level the subject hierarchy, I would expect it to hide the entire patient (both CT and structure set), but it only hides the structure set.   Is this a bug or is this “works as designed”? 
[2020-06-03_12-46_1]
  </blockquote>
</aside>


---

## Post #4 by @muratmaga (2021-05-12 15:06 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="17582">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>This is a bit of a pandora’s box, but if you have time to think all the cases through and draft a plan then we welcome new ideas!</p>
</blockquote>
</aside>
<p>I am not sure what other use cases might be, but I would be surprised if mine is not a fairly common one: I have multiple subjects that I would like to review the landmarking procedure both in 2D and 3D. I collect the data nodes relevant to the subject in one level, and when I disable to visibility for that subject I expect everything under that level to be turned off.</p>
<p>Leaving the volume (particularly when there is a property called 2D visibility for subject level exists) out of this is kind of confusing and at times it is misleading.</p>
<p>I don’t want to break other use cases, but can this behavior also be supported? Perhaps a little lock button at subject level to show it is going to apply everything (what I expected to see) and unlock is the default behavior.</p>

---

## Post #5 by @cpinter (2021-05-12 15:15 UTC)

<p>Turning visibility off is straightforward. However, turning on is very complex due to the issues I mentioned above (2D/3D/both? Slices in 3D? Volume rendering settings? Background/Foreground? Which views in layout?).</p>
<p>Because we don’t have a good logic for turning visibility on, it would be assymetric if we added turning visibility off, however I’d be OK with that. <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a> ?</p>

---

## Post #6 by @jamesobutler (2021-05-12 15:20 UTC)

<p>If it was asymmetric behavior, then I really wouldn’t want the turning off to be done by the toggle visibility eye button.  A toggle should show/hide the target item. If asymmetric functionality, then there would need be a “Turn Off” button to make it clear the expected behavior. Otherwise we are still in a situation of why wouldn’t it turn on in the same way it turned off.</p>

---

## Post #7 by @muratmaga (2021-05-12 15:21 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="6" data-topic="17582">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>If it was asymmetric behavior, then I really wouldn’t want the turning off to be done by the toggle visibility eye button.</p>
</blockquote>
</aside>
<p>I agree, this would be as confusing as it is right now.</p>

---

## Post #8 by @lassoan (2021-05-12 15:22 UTC)

<p>The only proper solution I can think of would be to implement multi-layer (not just hardcoded 2 layers) volume display in slice views, the same way as we do it for all other node types. I think <a class="mention" href="/u/jcfr">@jcfr</a> has implemented this (at least partially) a few years ago. Although it would be a backward-incompatible change, it should be doable, it is just a matter of prioritization. The main driver (and funding source) of this change would probably be better multichannel image support (for example, for microscopy) and not small behavior inconsistencies.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="17582">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I am not sure what other use cases might be, but I would be surprised if mine is not a fairly common one: I have multiple subjects that I would like to review the landmarking procedure both in 2D and 3D. I collect the data nodes relevant to the subject in one level, and when I disable to visibility for that subject I expect everything under that level to be turned off.</p>
</blockquote>
</aside>
<p>A much more common use case is that you click to hide the current case and then click to show another case. The behavior is correct in this use case, the only minor inconsistency is that volumes of the previous case are hidden when you turn on visibility of the new case (and not immediately when you hide the previous case).</p>
<aside class="quote no-group" data-username="cpinter" data-post="9" data-topic="17582">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>We should still come up with a robust logic for layout and 3D decisions.</p>
</blockquote>
</aside>
<p>3D volume visibility already works well (folder node visibility controls volume rendering visibility as well). 3D slice visibility could work the same way as 3D model visibility (slice view is visible in 3D if folder display nodes visibility is enabled and scalar volume display node’s visibility and 3D visibility are enabled).</p>
<p>What do you mean by “logic for layout”? How to determine role and order of layers? We could use a “weight” property (heavy items sink to bottom) for ordering, and layer controls similar to image viewers (PhotoShop, Gimp, …).</p>

---

## Post #9 by @cpinter (2021-05-12 15:25 UTC)

<p>It would solve one issue of those I listed. We should still come up with a robust logic for layout and 3D decisions.</p>

---

## Post #10 by @cpinter (2021-05-12 15:44 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="17582">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>3D volume visibility already works well</p>
</blockquote>
</aside>
<p>Yes it is OK if you already have it shown and you want to turn it on/off easily. But if you click the visibility icon of a volume that is not currently visible how do you know if you want to only show it in 2D, or 3D, or both?</p>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="17582">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What do you mean by “logic for layout”?</p>
</blockquote>
</aside>
<p>By layout logic I mean show it in all 2D views, or if it’s a compare layout on the top row, bottom row, both? There is no way knowing where and how the user wants to show volumes unless there is some reference.<br>
A reference could be to remember where we just turned volume visibilities off, but it’s not a complete solution.<br>
In the past we did have some heuristics like show volumes only in 2D and in certain layers, but it didn’t work and that’s why we have the current behavior (don’t remember the actual reasoning but the consensus apparently was that not handling volume visibilities is better than doing them in a confusing or error-prone way).</p>

---

## Post #11 by @muratmaga (2021-05-12 15:55 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="10" data-topic="17582">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Yes it is OK if you already have it shown and you want to turn it on/off easily. But if you click the visibility icon of a volume that is not currently visible how do you know if you want to only show it in 2D, or 3D, or both?</p>
</blockquote>
</aside>
<p>I am not sure why this should be any different than what it is already:</p>
<ol>
<li>For new volume that is not actively selected for 3D rendering, visibility on controls the slice view.</li>
<li>If the volume has been rendered (either by dragging into the 3D viewer, or through volume rendering), the visibility button control both.</li>
</ol>
<p>Am I mistaken?</p>

---
