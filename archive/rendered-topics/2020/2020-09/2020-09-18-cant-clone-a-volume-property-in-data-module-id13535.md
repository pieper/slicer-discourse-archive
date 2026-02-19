---
topic_id: 13535
title: "Cant Clone A Volume Property In Data Module"
date: 2020-09-18
url: https://discourse.slicer.org/t/13535
---

# Can't clone a volume property in Data module

**Topic ID**: 13535
**Date**: 2020-09-18
**URL**: https://discourse.slicer.org/t/cant-clone-a-volume-property-in-data-module/13535

---

## Post #1 by @muratmaga (2020-09-18 06:38 UTC)

<p>I want to have clone an existing VP and then modify that (for an animation). It seems right-clicking on the volume property to clone in Data module doesn’t seem to work (in all nodes tab). Is this expected?</p>
<p>I can save and reload it, but cloning is more convenient…</p>

---

## Post #2 by @lassoan (2020-09-18 15:22 UTC)

<p>Cloning a node is a high-level operation, implemented in subject hierarchy plugins. It involves cloning/copying node references and various node properties. For example, to clone a volume node, you need to deep-copy its image data, clone at least its display nodes and copy some of its node references.</p>
<p>There are no subject hierarchy plugins for low-level nodes that are mostly just implementation details. Volume rendering property (and display nodes in general) would fall into the low-level nodes category, which you would not want to pollute the data tree.</p>
<p>Maybe a “copy from” volume rendering property button somewhere in volume rendering module could be more appropriate solution if cloning turns out to be needed frequently.</p>

---

## Post #3 by @muratmaga (2020-09-18 15:36 UTC)

<p>Thanks Andras.</p>
<p>Yes with the animator module, we need typically need two (or more) volume properties for a volume (a start and an end one). For smooth transitions and color consistency, this is best done using by cloning/copying the first volume property and adjusting the cloned one as needed.</p>
<p>Another area I can see duplicating volume properties would be needed is the new multi-volume rendering. We experimenting with cloning an existing volume node and rendering both simultaneously with two different volume properties that seems to gives us a better control of rendering details.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> would it be possible to do the copy from button in volume rendering somehow?</p>

---

## Post #4 by @lassoan (2020-09-18 15:50 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="13535">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>with the animator module, we need typically need two (or more) volume properties for a volume</p>
</blockquote>
</aside>
<p>This might be handled more conveniently in animator module: it can create a new animation keyframe by copying, extrapolating,  or interpolating existing keyframes.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="13535">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Another area I can see duplicating volume properties would be needed is the new multi-volume rendering.</p>
</blockquote>
</aside>
<p>Here we need cloning of display nodes (not just volume property nodes), as we want the same volume to appear multiple times in a view. Slicer GUI only shows the first display node, but I agree that rendering the same volume multiple times with completely different transfer functions could allow nice new visualizations, so it could useful to make an exception here. In Volume rendering module, we could allow creating and editing multiple volume rendering display nodes for a selected volume. New volume rendering display node could be added by cloning or referencing the existing volume property node and clipping ROI.</p>

---

## Post #5 by @muratmaga (2020-09-18 16:16 UTC)

<p>Animator actually does what I want, I just brought it up as potential use case it to make it more generally available feature of duplicating volume property nodes.</p>
<p>I think multi-volume rendering will be a great tool for Slicer, but I also think we need to carefully review the volume rendering module UI.</p>

---
