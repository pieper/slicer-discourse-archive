# Volume Rendering module UI redesign

**Topic ID**: 13956
**Date**: 2020-10-09
**URL**: https://discourse.slicer.org/t/volume-rendering-module-ui-redesign/13956

---

## Post #1 by @muratmaga (2020-10-09 15:24 UTC)

<p>Is there any plan to revamp the volume rendering module for upcoming stable or is it the too much to deal without specific funding?</p>
<p>At the minimum, without touching the core or adding any features, I would suggest reorganizing the UI with a multi-tab approach. First tab being the the parameters that broadly applies (GPU rendering settings, options) to everything. And the display and volume specific settings would be moved to another tab that has the (now familiar) data or markup node display, and all specific properties that can be set per volume basis.</p>

---

## Post #2 by @lassoan (2020-10-09 15:49 UTC)

<p>Can you draw a proposed design in some desktop GUI mockup tool (such as <a href="https://pencil.evolus.vn/">pencil</a>)?</p>

---

## Post #3 by @muratmaga (2020-10-09 16:36 UTC)

<p>ok. Will try to do one…</p>

---

## Post #4 by @muratmaga (2020-10-09 18:38 UTC)

<p>This is the first time I try something like this, apologies for lack of clarity. Here are some explanations.</p>
<p>The main volume rendering module would have two tabs: Technique and Volume Rendering.</p>
<p>Technique is fairly empty, and perhaps future rendering techniques (Osprey or Prism etc) can be added and listed here (as oppose to having their own modules). Basically this should contains that effects the volume rendering of everything, not just an individual volume.</p>
<p>Volume Rendering is mostly the same, except there is now hierarchy view and the properties can be modified by clicking on them. Advanced section is continuation of Volume Property with additional settings, and perhaps Lights module can be incorporated here (although as I understand that impact not just the VR module, but everything in the 3D viewer). This way the Scalar Opacity maps can be given somewhat higher area without making the module tab extremely long. I always find them too small to manipulate points precisely, and that little zoom scrollbar never worked for me.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/3039ffd25ce0758aef129f86bc3309bfc24efab4.png" data-download-href="/uploads/short-url/6SDbfKsEH44DSrwCUtI5ihD9Dp2.png?dl=1" title="VR_UI_small"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/3039ffd25ce0758aef129f86bc3309bfc24efab4_2_690x498.png" alt="VR_UI_small" data-base62-sha1="6SDbfKsEH44DSrwCUtI5ihD9Dp2" width="690" height="498" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/3039ffd25ce0758aef129f86bc3309bfc24efab4_2_690x498.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/3039ffd25ce0758aef129f86bc3309bfc24efab4_2_1035x747.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/3039ffd25ce0758aef129f86bc3309bfc24efab4.png 2x" data-dominant-color="898C8F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">VR_UI_small</span><span class="informations">1082×782 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2020-10-10 02:24 UTC)

<p>It makes sense to separate common settings from volume-specific settings a bit more clearly, and a separate tab would serve this purpose well. We already have top-level tab control in other modules (Data, Sequences, and Plots modules already), so it would not introduce a new GUI design element. It could also make sense to add lights settings nearby, but as you have noted, lights settings applies to all rendered objects (not just volume rendering) and lighting settings can be different for each view - so probably it is cleaner to adjust lights in a dedicated module.</p>
<p>Using a tree view would also make the module more convenient and consistent with other modules (Models, Markups).</p>
<p>I don’t see where ROI and Volume property node selector went.</p>
<p>You kept the tabs inside the Display section (Volume properties, Advanced), which I think makes things a bit more complicated (and not consistent with GUI of other modules). It could be better to move them into the usual collapsible sections, one above the other.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="13956">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I always find them too small to manipulate points precisely, and that little zoom scrollbar never worked for me.</p>
</blockquote>
</aside>
<p>They work reasonably well. What do you do, what do you expect to happen, and what happens instead?</p>

---

## Post #6 by @muratmaga (2020-10-10 03:48 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="13956">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I don’t see where ROI and Volume property node selector went.</p>
</blockquote>
</aside>
<p>I assumed they would be listed in the tree view and dragged in and out of the associated volume node to change (more than one VP can be nested under a volume, a little selection button can help choose ). So there wouldn’t be a need for a separate selector. But I can see this being an issue if you were to share a volume property or an ROI with two volumes. Perhaps cloning them in this case would help.  What I am not sure is how this would work with presets.</p>
<p>Adding all options into a single module panel is  of course is an option, but it will suffer from the same problem that Markups module has. When all of the collapsible tabs are expanded, the module is very long and scrolling up and down quite necessary.</p>
<p>Anyways, just a thought.</p>

---

## Post #7 by @lassoan (2020-10-10 04:02 UTC)

<p>Showing the ROI in the view is an interesting idea, but we don’t have to do it. Instead, the tree can be filtered to only show volume nodes.</p>

---

## Post #8 by @muratmaga (2020-10-10 04:08 UTC)

<p>If we go with the tree view, I think we should; not just the ROI but the VP too. Currently there is no mechanism to modify a VP without actually setting it to active under the properties. Assumption, here you can click on it, modify the settings without it being assigned to a specific volume.</p>
<p>I think this gives a cleaner view of what is set for a particular volume.</p>

---
