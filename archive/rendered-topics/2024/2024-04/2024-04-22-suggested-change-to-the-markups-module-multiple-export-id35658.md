---
topic_id: 35658
title: "Suggested Change To The Markups Module Multiple Export"
date: 2024-04-22
url: https://discourse.slicer.org/t/35658
---

# Suggested change to the Markups module- multiple export

**Topic ID**: 35658
**Date**: 2024-04-22
**URL**: https://discourse.slicer.org/t/suggested-change-to-the-markups-module-multiple-export/35658

---

## Post #1 by @Logan_Moore (2024-04-22 19:21 UTC)

<p>Hi all,</p>
<p>In my cursory search, I did not find older posts suggesting this, so I thought it would be nice to bring it up. <a class="mention" href="/u/lassoan">@lassoan</a> would it be possible to add an additional export selection or option to the Markups module that would allow use to export all existing nodes into a singular file? For example, I am collecting standard fiducials as well as curve data in my current study, but I have to combine these files in post to run my analysis. At least, that is my current understanding as I haven’t found a way to do this from within Slicer.</p>
<p>My suggestion would be to either add an additional pop-up or a setting that would save all active nodes in the order in which they appear in the Markups section. So, I would imagine the data structure looking something like this.</p>
<p>F-1 (all fiducials in F-1)<br>
Curve 1<br>
Curve 2<br>
Closed Curve 1<br>
Angle 1</p>
<p>If it couldn’t be done in a json format, would it be possible to add the option if it was only fcsv?</p>
<p>Would love to hear your thoughts!<br>
-Logan</p>

---

## Post #2 by @muratmaga (2024-04-22 19:57 UTC)

<p>You can use MergeMarkups in Slicermorph to merge curves and pointlist.</p>
<p>Or you can copy/paste control points from one node to the other.</p>

---

## Post #3 by @Logan_Moore (2024-04-22 20:06 UTC)

<p>Oh, that would be great! I will call up some of my data today or tomorrow and take a look at this feature. Additionally, I wasn’t aware you could simply copy and paste the control points between nodes, so at a minimum I can do that.</p>
<p>Thank you for bringing this to my attention! It will really help bring down the number of files I was managing before!</p>
<p>-Logan</p>

---

## Post #4 by @lassoan (2024-04-23 03:04 UTC)

<p>For scene loading and saving, there is always a 1-to-1 correspondence between each markup node and markup file, but no such restrictions are needed for export and import of markup nodes.</p>
<p>You can already load many markup nodes from a single file.</p>
<p>However, such files currently have to be created manually (e.g., in a text editor). I envisioned a subject hierarchy folder plugin that displays a right-click menu action to export all markups in that folder into a single file - but it has not been implemented yet.</p>

---

## Post #5 by @Logan_Moore (2024-04-23 03:55 UTC)

<p>Andras, I’m sorry I didn’t come across as clear as I wanted. However, your suggested implementation is essentially what I was thinking. Having the ability to merge all markups and export them as a single file would be a great feature for those who use geometric morphometrics to do shape and other evolutionary analyses outside of Slicer, say in R for example. Murat highlighted that it can be done with Slicermorph, I just haven’t had the time to try it yet today.</p>
<p>I will have the time to test this tomorrow and mark his suggestion as a solution until it is potentially native to Slicer itself.</p>
<p>-Logan</p>

---

## Post #6 by @Logan_Moore (2024-04-29 18:34 UTC)

<p>Hi Murat,</p>
<p>Sorry for my delayed response, time got away from me last week. Looks like SlicerMorph does exactly what I want it to do.</p>
<p>Reading through the documentation it looks like it takes all of the curves and just adds them each to the end of the first curve in the list, correct? The visualization of the fused curves doesn’t matter; it just looks busy. Sorry I am working exclusively working with curved objects and just want to be doubly sure.</p>
<p>Outside of this, it fuses my 4 curves and my fixed landmark set nicely to give me a single json file that I can either do the entire analysis in Slicer or export and read into R.</p>
<p>Thanks for putting this together!<br>
-Logan</p>

---

## Post #7 by @muratmaga (2024-04-29 18:37 UTC)

<aside class="quote no-group" data-username="Logan_Moore" data-post="6" data-topic="35658">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/logan_moore/48/69222_2.png" class="avatar"> Logan_Moore:</div>
<blockquote>
<p>Reading through the documentation it looks like it takes all of the curves and just adds them each to the end of the first curve in the list, correct?</p>
</blockquote>
</aside>
<p>Yes, but there is a certain assumption. The last control point of the previous curve and the first point of the next one should be identical (otherwise merging them like this wouldn’t make sense).</p>

---

## Post #8 by @Logan_Moore (2024-04-29 18:44 UTC)

<p>Ah, I see. Given that I have 4 independent curves (measuring different portions of ribs), would you suggest taking my resampled curves and manually pasting them into the original point list so that they can be slid later? Or should I export all of them as jsons, convert the curves into fiducial nodes, and then fuse them? I have roughly 2300 ribs in my sample, so I am just trying to make this as easy as possible!</p>

---

## Post #9 by @muratmaga (2024-04-29 19:00 UTC)

<aside class="quote no-group" data-username="Logan_Moore" data-post="8" data-topic="35658">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/logan_moore/48/69222_2.png" class="avatar"> Logan_Moore:</div>
<blockquote>
<p>Given that I have 4 independent curves (measuring different portions of ribs), would you suggest taking my resampled curves and manually pasting them into the original point list so that they can be slid later?</p>
</blockquote>
</aside>
<p>MergeMarkups meant as a tool to merge separate but continuous curves into a single one. If your curves are independent, then it wouldn’t make much sense to use (you would be loosing the very first point in curves subsequent to the first one).</p>
<p>Is your goal to combine everything (all resampled curves from all samples) into a single json file? Or merge the 4 resampled curves and fixed landmarks from a specimen into a single json? Anyways both are doable via scripting.</p>

---

## Post #11 by @Logan_Moore (2024-04-29 19:11 UTC)

<p>My goal is your second point: to have a json file per specimen. This way, I can look at individual rib variation (just first ribs, just second ribs, etc), total rib variation, or any subset combination.</p>
<p>I don’t have much experience with scripting, but I can work on it on the side while continuing to collect my data.</p>

---
