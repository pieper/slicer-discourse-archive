---
topic_id: 9390
title: "Moving Freesurfer Support To An Extension"
date: 2019-12-04
url: https://discourse.slicer.org/t/9390
---

# Moving FreeSurfer support to an extension

**Topic ID**: 9390
**Date**: 2019-12-04
**URL**: https://discourse.slicer.org/t/moving-freesurfer-support-to-an-extension/9390

---

## Post #1 by @Sunderlandkyl (2019-12-04 21:04 UTC)

<p>Hi All,</p>
<p>Recently, we’ve been development on an extension to import FreeSurfer models in the correct coordinate system, as well as to import other files at the same time (segmentations, scalar overlay, etc.).</p>
<p>As part of this development, is there any support for moving all FreeSurfer related classes from Slicer core (colormap, data importers, etc.) to an extension?</p>
<p>Benefits:</p>
<ul>
<li>Smaller Slicer core</li>
<li>More frequent updates for FreeSurfer support</li>
</ul>
<p>Downsides:</p>
<ul>
<li>Users need to install another extension to read FreeSurfer files</li>
</ul>
<p>What are everyone’s thoughts?</p>

---

## Post #2 by @lassoan (2019-12-04 21:30 UTC)

<p>Additional benefit: when someone attempts to load a data set, the rarely useful “Scalar overlay” option would not be offered as the default option to everyone (only to those that install FreeSurfer extension because they want to load freesurfer files).</p>

---

## Post #3 by @lassoan (2019-12-05 02:02 UTC)

<p><a class="mention" href="/u/ljod">@ljod</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/rkikinis">@rkikinis</a></p>

---

## Post #4 by @pieper (2019-12-05 04:08 UTC)

<p>Moving all freesurfer related support to the extension makes sense to me <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #5 by @rkikinis (2019-12-05 04:24 UTC)

<p>In terms of doing it, I see no downside at this point. We might want to think about how to communicate to neuroscience users.</p>

---

## Post #6 by @lassoan (2019-12-05 04:42 UTC)

<p>Do you know if they read the Slicer forum? If not, it could be a good opportunity to invite them to participate in this and further discussions.</p>

---

## Post #7 by @jcfr (2019-12-05 22:05 UTC)

<p>That makes sense. <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> Thanks for working on this <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=9" title=":pray:" class="emoji" alt=":pray:"></p>

---
