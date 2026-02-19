---
topic_id: 10176
title: "Remove Small Islands Alternative Or Speedup"
date: 2020-02-09
url: https://discourse.slicer.org/t/10176
---

# Remove small islands alternative (or speedup?)

**Topic ID**: 10176
**Date**: 2020-02-09
**URL**: https://discourse.slicer.org/t/remove-small-islands-alternative-or-speedup/10176

---

## Post #1 by @hherhold (2020-02-09 23:40 UTC)

<p>Slicers -</p>
<p>In a few scans I’m working with, after thresholding and segmenting with brushes/scissors/etc, I wind up with many thousands of small islands in the integument of some insects. Basically, lots of tiny little buts that are the same intensity of the vessels I’m segmenting out, but separate from these features. The islands are typically less than 20 voxels, so removing them using remove small islands is pretty straightforward. The issue is that it is exceedingly slow - it can take hours, depending on how many (upwards of 100000) small specs show up.</p>
<p>I’ve dug into the python for the islands effect a bit, and by scattering print statements to do a very coarse profiling, it appears the slowest part is the modifySegmentByLabelmap() function (implemented in C++), so “refactoring” this is probably non-trivial.</p>
<p>What I’ve wound up doing is making a new segment and picking the larger islands one by one to add to it using Add selected island, but it’s still pretty tedious. I’ve also tried a few filtering and smoothing approaches, but they wind up removing detail on the things I want to keep.</p>
<p>Any ideas anybody has on this for either speeding up removing small islands, or a totally different approach would be most appreciated - Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @Sunderlandkyl (2020-02-10 01:06 UTC)

<p>The performance of the island effect is something that I plan to try to improve. I’ll take a look at it this week and let you know what happens.</p>

---

## Post #3 by @lassoan (2020-02-10 01:11 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="1" data-topic="10176">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>The islands are typically less than 20 voxels, so removing them using remove small islands is pretty straightforward. The issue is that it is exceedingly slow - it can take hours, depending on how many (upwards of 100000) small specs show up.</p>
</blockquote>
</aside>
<p>“Remove small islands” should be fast, as it does not create new segments. Maybe you mean “Split islands to segments” is too slow?</p>
<p>Can you take a screen capture video (or a few screenshots+ step-by-step description) that explains your workflow?</p>

---

## Post #4 by @hherhold (2020-02-10 12:18 UTC)

<p>It’s definitely remove small islands, not split islands. (Not sure I’ve ever used split islands…)</p>
<p>The same function in SegmentEditorIslandsEffect.py is used for splitting or removing, there’s just a bool to tell the function whether or not to split, so the logic is similar for both. As far as workflow, I basically use a combination of thresholding, thresholded brush, and scissors to pick out lots of air spaces, and in some specimens I get a lot of “noise” - very small islands scattered in the integument (20 voxels or less). Remove small islands does an <em>awesome</em> job removing these, but in some specimens with a LOT of noise, it can take hours.</p>
<p>I’m a little fuzzy on exactly what’s going on as I don’t speak VTK, but it looks like it uses vtkITKIslandMath to identify the islands larger than a particular size (this is the fast part), then makes a new segment and adds the large enough islands in one by one (this is the slow part).</p>
<p>The one call that appears to be taking the longest is towards the end of the function in the loop that adds each island back in. This one here:</p>
<pre><code>self.scriptedEffect.modifySegmentByLabelmap(segmentationNode, segmentID, modifierImage, modificationMode)
</code></pre>
<p>There is one other spot that’s a little slow but I’m forgetting what it is right now, and I took out my debug prints for “profiling”. Anyway, please let me know if there’s anything I can do to assist with fixes or testing. I know C++ (and python) but not VTK/ITK.</p>
<p>Thanks!!!</p>

---

## Post #5 by @lassoan (2020-02-11 16:08 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> has done some performance optimization on Islands effect. Please try Slicer Preview Release tomorrow (rev28765 or later) and let us know how it works.</p>

---

## Post #6 by @hherhold (2020-02-13 01:20 UTC)

<p>Definitely better. My test case took on the order of 40-50 minutes or so, which was:</p>
<p>1328 islands created (175699 ignored)</p>
<p>So this is absolutely much more useable. Previously I basically halted this particular scan after a couple of hours.</p>
<p>Thank you very much!!!</p>
<p>-Hollister</p>

---

## Post #7 by @lassoan (2020-02-13 01:28 UTC)

<p>Hundreds of thousands of speckles are most likely caused by random noise. Islands effect is not optimal for removing it, not just because of the long computation time but also because valid object boundaries will be still corrupted by noise.</p>
<p>Instead, you can suppress noise in the master image using image filtering - see modules: Filtering / Denoising; and Filtering / Simple filters.</p>
<p>You can also remove small speckles without significant loss of details by using Smoothing effect / Median method with a small kernel size.</p>

---

## Post #8 by @hherhold (2020-02-13 02:08 UTC)

<p>For this scan, in any one area, there’s not that much speckle, but the scan is 16 bit, 510 x 510 x 1800, so a bit of speckle here and there adds up.</p>
<p>I’ll try the de-noising filters, that’s a good idea. The smoothing/median effects actually do wind up removing detail I’m looking for (in the 1-5 voxel range) with very small tracheoles.</p>
<p>I have not spent nearly as much time as I should exploring the many filtering options.</p>
<p>Thanks much!!!</p>

---
