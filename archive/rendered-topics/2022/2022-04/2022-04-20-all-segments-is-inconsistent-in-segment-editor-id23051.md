---
topic_id: 23051
title: "All Segments Is Inconsistent In Segment Editor"
date: 2022-04-20
url: https://discourse.slicer.org/t/23051
---

# "All segments" is inconsistent in Segment Editor

**Topic ID**: 23051
**Date**: 2022-04-20
**URL**: https://discourse.slicer.org/t/all-segments-is-inconsistent-in-segment-editor/23051

---

## Post #1 by @hherhold (2022-04-20 14:11 UTC)

<p>I’ve been using scissors with “Apply to all segments” to erase or fill in multiple segments. This works on all <em>visible</em> segments, which is actually not what the check box says, but it <em>is</em> what I want it to do, so it works great and saves me a TON of time.</p>
<p>Erase, however, says “Erase all segments” in the check box, which <em>does</em> do what it says it does, erasing all segments - even not visible ones. This is actually NOT what I want - I’d like to be able to erase on ONLY visible segments, NOT ones that are not visible.</p>
<p>So I guess I have two related issues:</p>
<ul>
<li>Assuming this is what is intended, Scissors should say “Apply to all visible segments”</li>
<li>I would be really nice to have an option in Erase to only erase visible segments.</li>
</ul>
<p>Happy to work on fixing these as desired once a consensus is reached.</p>
<p>Thoughts?</p>
<p>Thanks!!</p>
<p>-Hollister</p>

---

## Post #2 by @hherhold (2022-04-20 14:24 UTC)

<p>I <em>did</em> just realize (need more coffee) I can do what I want with Erase by setting Editable area to Inside all visible segments, so I guess the only real issue is the text on the check box in Scissors.</p>

---

## Post #3 by @hherhold (2022-04-20 14:27 UTC)

<p>Actually, I take that back - even if a segment isn’t visible, and you set Editable area to Inside all visible segments, Erase still erases all segments (visible or not) if Erase all segments is checked.</p>
<p>Thoughts/ideas?</p>

---

## Post #4 by @rbumm (2022-04-20 15:24 UTC)

<p>Yes, combining “Erase”, “Erase all segments” and “Inside all visible segments” works well.</p>
<p>I could easily generate a PR with a change to the “Scissors” label text if this is the only issue.</p>

---

## Post #6 by @rbumm (2022-04-20 15:35 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="3" data-topic="23051">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>even if a segment isn’t visible, and you set Editable area to Inside all visible segments, Erase still erases all segments</p>
</blockquote>
</aside>
<p>Just tested this again with a spine segmentation in Slicer 4.13 and “Erase” with settings “Erase all segments” and “Inside visible segments” worked as expected: Visible segments got erased, invisible segments stayed untouched …</p>

---

## Post #7 by @hherhold (2022-04-20 15:49 UTC)

<p>OK, I’ll give it another try. Thanks!</p>

---

## Post #8 by @lassoan (2022-04-20 15:57 UTC)

<p>Segment Editor is primarily for visual editing, i.e., that you always modify visible segments. If you attempt to paint into a hidden segment then you’ll get a warning popup. So, by default when you edit, you edit what is visible.</p>
<p>We reduced the checkbox text to the minimum to save space (if we added “visible” word then it became much longer than other strings in that column) and keep things simple. The tooltip provides more details:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0a4b7945e6d6040bf901429af77c5f52e433268.png" alt="image" data-base62-sha1="ykPuR5T4NIDhTK13jea2xD484VG" width="577" height="484"></p>
<p>This shortening of the checkbox text and spelling out nuances in the tooltip is consistently used in Scissors, Smoothing, Hollow, and Margin effects.</p>
<p>If you find that this simplification goes too far and it is counterintuitive (despite all our efforts to convey the idea that Segment Editor is for modifying visible content) and misleading for users then please suggest alternative wording that is preferably not longer than the current text (or propose layout changes).</p>

---

## Post #9 by @hherhold (2022-04-20 16:06 UTC)

<p>Oops, I had tooltips turned off, my mistake. That wording looks good to me and the shortened checkbox text is clear enough, I think.</p>
<p><a class="mention" href="/u/rbumm">@rbumm</a> - I think I figured out my issue, I have multiple overlapping segments, some visible, some not and the distinction of “inside all visible segments” wasn’t capturing the subset of segments that I thought it was. Erase does work as advertised when Editable area is selected as you mentioned.</p>
<p>Thanks all!</p>

---
