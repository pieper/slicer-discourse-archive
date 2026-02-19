---
topic_id: 26990
title: "Collaborative Distributed Segmentation Of Many Images"
date: 2022-12-30
url: https://discourse.slicer.org/t/26990
---

# Collaborative/distributed segmentation of many images

**Topic ID**: 26990
**Date**: 2022-12-30
**URL**: https://discourse.slicer.org/t/collaborative-distributed-segmentation-of-many-images/26990

---

## Post #1 by @Gourav25911 (2022-12-30 16:41 UTC)

<p>Hello 3D slicer community,</p>
<p>I am wondering if there is a extension/feature available in 3D slicer that allows users to collaboratively annotate / work on images. People can work in teams perform their operations /collaboratively annotate, segment, and get seamless access to datasets</p>

---

## Post #2 by @muratmaga (2022-12-30 18:19 UTC)

<aside class="quote no-group" data-username="Gourav25911" data-post="1" data-topic="26990">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gourav25911/48/17870_2.png" class="avatar"> Gourav25911:</div>
<blockquote>
<p>I am wondering if there is a extension/feature available in 3D slicer that allows users to collaboratively annotate / work on images. People can work in teams perform their operations /collaboratively annotate, segment, and get seamless access to datasets</p>
</blockquote>
</aside>
<p>If you mean realtime collaboration (as if editing a google doc), that is not available. Otherwise data exchange is fairly easy. You can create a scene with all the data loaded, package it is a MRB file and send it to your collaborators for them to work on them.</p>

---

## Post #3 by @pieper (2022-12-30 18:59 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="26990">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Otherwise data exchange is fairly easy.</p>
</blockquote>
</aside>
<p>Agreed.  What we routinely do these days is share a dropbox or google drive filled with source data and segmentations.  The downside is you need to use directory names and spreadsheets to track things, but it’s workable.</p>
<p>The <a href="https://github.com/Project-MONAI/MONAILabel/tree/main/plugins/slicer/MONAILabelReviewer">MONAI Label Reviewer</a> module may be of interest but I haven’t tried it myself.</p>

---

## Post #4 by @Gourav25911 (2023-01-02 12:44 UTC)

<p>Thanks for the suggestion. We will try it</p>

---
