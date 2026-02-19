---
topic_id: 27632
title: "Combination Segmentation Effect"
date: 2023-02-04
url: https://discourse.slicer.org/t/27632
---

# Combination segmentation effect

**Topic ID**: 27632
**Date**: 2023-02-04
**URL**: https://discourse.slicer.org/t/combination-segmentation-effect/27632

---

## Post #1 by @mohammed_alshakhas (2023-02-04 16:38 UTC)

<p>i wish that we could have a combination of effect tools<br>
the following is what I would love to use</p>
<p>1 combined erase/ median smooth<br>
2 combined paint / median smooth.<br>
those would be great time savers instead of applying both consecutively. especially useful for the local edition which I use for most of my work</p>
<p>3 combined paint/erase: I know this sounds ridiculous but when you need to refine segmentation to a fine degree where the part you are segmenting has multiple thresholds in different anatomical areas (some being very low and some high ) ) like in orbit or TMJ.</p>
<p>this would simply work by defining what your threshold to paint and anything outside will be erased.</p>
<p>thanks</p>

---

## Post #2 by @lassoan (2023-02-08 20:45 UTC)

<p>1-2: I’m not sure what you mean by combining erase or paint with median smoothing. In general, smoothing should be applied after you have completed many paint/erase operations.</p>
<p>3: Combined paint/erase is already available if you enable “Color smudge” option in Paint effect. If you start painting from inside a segment then you paint; if you start painting from outside (where there is no segment) then you erase. This option even switches the current segment automatically (selects the segment that is at the position where you press the mouse button).</p>

---

## Post #3 by @mohammed_alshakhas (2023-02-09 09:57 UTC)

<p>I meant a tool or ability to stack tools  that automatically apply  median smoothening to area after being painted or erased .<br>
I specifically think those would be highly useful for local effects .</p>
<p>In this example I’m not able to do global operation for segment therefore I’ll have to do paint or erase then smooth one area then again for different area of same segment.</p>
<p>This usually happens because of threshold differences and different details level I need in each area of my segment .</p>
<p>I have never used smudge paint , I’ll give it a try .</p>

---

## Post #4 by @mohammed_alshakhas (2023-02-10 08:38 UTC)

<p>i have just tried the smudge color and I love it .</p>
<p>i really think that filling holes in smoothing and color smudge should be separate effects not with under other  effects.  I suggest a "  refining effect " which can include both or make them standalone effects . I use fill holes a lot and I wish it is seperate  since I use it with different  parameters than median smoothing.</p>

---

## Post #5 by @lassoan (2023-03-14 04:32 UTC)

<p>Adding a combined “Refine” effect for color smudge + hole filling smoothing is an interesting idea. My main concern is that if you often run hole filling many times then each time it may slightly modify the segmentation. We should also try to keep number of segment editor effects</p>
<p>You can add a keyboard shortcut to switch to Smoothing effect with hole filling mode with a certain kernel size and another shortcut to switch to Smoothing effect with Median smoothing mode with a different kernel size.</p>

---

## Post #6 by @mohammed_alshakhas (2023-03-18 10:54 UTC)

<p>I’m not sure that color smudge + filling hole is   very helpful to me,  but it would not be a bad idea</p>
<p>I originally referred to combined  (  paint +  median smoothening ) and /or    (  erase  +  median smoothening )<br>
this effect is useful in my opinion and how I do segmentation at the end where I need to finalize or refine my segmentation. This combination will be definitely  a time saver</p>
<p>the other suggestion was to remove color smudge and fill hole from the current location.<br>
the reason is that fill holes and color smudge are practically very close to each other.</p>
<p>the number of editing effects should be customizable, I almost never use fill-between-slices or level tracing. Therefore being able to remove the basic effect directly from the menu ( right click and remove ) is better than trying to keep the effects number smaller</p>

---

## Post #7 by @lassoan (2023-03-18 17:52 UTC)

<p>You can customize which effects are displayed in what order in as shown <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-list-of-displayed-segment-editor-effects">here</a>.</p>
<p>It is not clear for me how paint and smoothing can be combined, because painting adds a solid disk or sphere. If you use masking with intensity range then there may be gaps, but those are best to fill at the end, not after each paint stroke. Nevertheless, if you want to do this then you can add a single-key shortcut for disabling intensity masking, smoothing, and re-enabling masking - so that you can very easily apply this operation anytime.</p>

---

## Post #8 by @mohammed_alshakhas (2023-03-18 18:15 UTC)

<p>Customization would be great if can be done without coding <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"> , like from the menu with right click or drag and drop .</p>

---

## Post #9 by @lassoan (2023-03-18 18:28 UTC)

<p>No coding is needed. All you need is copy-paste the few lines of text from the link above into your <code>.slicerrc.py</code> file.</p>

---
