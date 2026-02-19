---
topic_id: 11994
title: "Cannot Rename Markupsfiducial In Load Data Window"
date: 2020-06-11
url: https://discourse.slicer.org/t/11994
---

# Cannot rename MarkupsFiducial in load data window

**Topic ID**: 11994
**Date**: 2020-06-11
**URL**: https://discourse.slicer.org/t/cannot-rename-markupsfiducial-in-load-data-window/11994

---

## Post #1 by @DiamondKMG (2020-06-11 20:56 UTC)

<p>Problem report for Slicer 4.11.0-2020-03-11 linux-amd64: [please describe expected and actual behavior]</p>
<p>I have  a set of .fcsv files that have very similar and long names and I would like to rename each file to a shorter name when I load more than one file into Slicer, similar to how you can rename volume files in the load data window by checking the Show Options box.</p>

---

## Post #2 by @lassoan (2020-06-11 20:59 UTC)

<p>Can you rename them after you added them to the scene, for example in Data module?</p>

---

## Post #3 by @muratmaga (2020-06-11 21:19 UTC)

<p>More to the point, if the input file has a ‘.’ in its prefix, Slicer truncates the file name and discards the part of prefix after the ‘.’. So we can’t distinguish which one is which once it is loaded into the scene.</p>
<p>So F.ab.fcsv, and F.aa.fcsv would be both shown as F in the data module after load.</p>

---

## Post #4 by @lassoan (2020-06-11 23:47 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="11994">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Slicer truncates the file name and discards the part of prefix after the ‘.’. So we can’t distinguish which one is which once it is loaded into the scene.</p>
</blockquote>
</aside>
<p>Thanks for reporting, <a href="https://github.com/Slicer/Slicer/commit/6e346bfb6764793d4a6db13bd268e14eb897551f">fixed</a> now.</p>

---

## Post #5 by @DiamondKMG (2020-07-02 17:40 UTC)

<p>I’m having the same problem again with the current preview of Slicer 4.11.0-2020-06-30 linux-amd64 truncating file names after “.” when importing segmentations and labelmaps.</p>

---

## Post #6 by @lassoan (2020-07-02 20:52 UTC)

<p>Just to clarify, there is no regression (loading of markups fiducials from .fcsv files still works correctly), but you have found that everything is considered to be part of the extension after the first dot for other file extensions. Probably we just used the overly simplistic file extension detection mechanism at a few more places. It should be no problem to fix those, too. As general advice, do not routinely use “.” character inside filenames because that character is reserved for separating file name from extension and may cause problems or inconveniences at various places (not just in Slicer).</p>
<p>Which file extensions do you have problem with and what did you choose in “Description” column when you loaded them?</p>

---

## Post #7 by @DiamondKMG (2020-07-02 21:11 UTC)

<p>The file extensions are .seg.nrrd or .nrrd and the error occurs when the Description is ‘Segmentation’ or ‘volume’</p>
<p>I did not name the original files, but in the future I’ll rename files that include ‘.’ at the start of all projects!<br>
Thank you for your help!</p>

---

## Post #8 by @muratmaga (2020-07-02 23:08 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="11994">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>As general advice, do not routinely use “.” character inside filenames because that character is reserved for separating file name from extension and may cause problems or inconveniences at various places (not just in Slicer).</p>
</blockquote>
</aside>
<p>It is really uphill battle. People seem to want to convey all the information in their experiment as part of the filename, and then we are stuck. How is this for a filename?</p>
<p><code> B6;129P2-Il2tm1Hor/J</code> (a knock out mice experiment).</p>

---

## Post #9 by @lassoan (2020-07-02 23:28 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="8" data-topic="11994">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>How is this for a filename?</p>
<p><code> B6;129P2-Il2tm1Hor/J</code> (a knock out mice experiment).</p>
</blockquote>
</aside>
<p>Nice! Fortunately, this one is not even a valid filename, so there is no temptation to use it. Eventually people learn the more subtle rules and best practices, too. We just have to make sure Slicer is as good in accepting complicated filenames as most other software, so that users they don’t think that something is wrong with Slicer.</p>

---

## Post #10 by @lassoan (2020-07-03 14:08 UTC)

<p>A <a href="https://github.com/Slicer/Slicer/pull/5026">fix</a> has been submitted for correctly loading all remaining nodes types (segmentations, models, markups, color tables, sequences, and volume rendering presets) when there are multiple “.” characters in the filename.</p>

---
