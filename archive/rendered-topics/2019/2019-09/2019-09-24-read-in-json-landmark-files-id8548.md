---
topic_id: 8548
title: "Read In Json Landmark Files"
date: 2019-09-24
url: https://discourse.slicer.org/t/8548
---

# Read In JSON Landmark files

**Topic ID**: 8548
**Date**: 2019-09-24
**URL**: https://discourse.slicer.org/t/read-in-json-landmark-files/8548

---

## Post #1 by @stevenagl12 (2019-09-24 15:39 UTC)

<p>Hi, I was wondering fi there was a way to read in landmark json files into 3D Slicer. I have Json files such as the following: [{“id”:“A”,“coordinates”:[-24.27351391435728,28.911588222173073,-123.59017318765929],“uncertainty”:{“stddevs”:[1.0314645489033252,1.0102904254707992,0.9816888397547289],“pcvectors”:[[-0.5679702259804069,-0.8192947708623337,-0.07852325029825062],[0.8142129897713141,-0.5732519865382224,0.09186602863757418],[-0.12027896610556417,-0.011757481346694274,0.9926705052256556]]}} created from another program and would like to be able to display them in 3D Slicer.</p>

---

## Post #2 by @lassoan (2019-09-24 15:59 UTC)

<p>In short term, you can probably implement this in 10-15 lines of python code (read in the json file, iterate through its items and add each point to a markups node).</p>
<p>We are planning to implement markups import/export in json format. Is the file that you received follows some commonly used standard or it is just invented for a particular project?</p>

---

## Post #3 by @stevenagl12 (2019-09-25 20:46 UTC)

<p>It’s a common standard. I’ve found it in several statistical shape modelling programs.</p>

---

## Post #4 by @pieper (2019-09-25 20:58 UTC)

<p>Can you provide some references? It would be nice to know if there’s community agreement on such a standard.  Does the standard have a name?</p>

---

## Post #5 by @stevenagl12 (2019-09-26 01:24 UTC)

<p>So not sure if you’re talking about references for the standard itself or the software, but the software I have found that uses it is RvtkStatismo, Statismo, and Scalismo all for statistical shape modelling.</p>

---

## Post #6 by @muratmaga (2019-09-26 01:50 UTC)

<p>JSON itself is not a standard for anything specific, it is a format to exchange data of many different kinds. What we are interested in learning if there was a common convention to describe landmark coordinates agreed upon communities. From what I am seeing in the few lines of the sample in the original email, it doesn’t appear that way to me but I might be mistaken.</p>

---

## Post #7 by @pieper (2019-09-26 11:28 UTC)

<aside class="quote no-group" data-username="stevenagl12" data-post="5" data-topic="8548">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>talking about references for the standard itself</p>
</blockquote>
</aside>
<p>Hi <a class="mention" href="/u/stevenagl12">@stevenagl12</a> - Yes, that is the question.  Your original email implied that this particular json encoding is a kind of agreed upon standard for interchange of these landmark files, so my question is whether this kind of file has a particular name (json is of course generic).  Even better, perhaps there is a json schema and/or a human readable description of the file format?</p>
<p>If there’s something well defined we could consider supporting it - as <a class="mention" href="/u/lassoan">@lassoan</a> says, it doesn’t look like it would be much work to implement.</p>

---

## Post #8 by @stevenagl12 (2019-10-01 16:25 UTC)

<p>I’m not exactly sure, all I know is that using those softwares previously mentioend produces the same type of JSON formatted files with coordinates, uncertainty, and pcvectors from any mesh being landmarked.</p>

---

## Post #9 by @lassoan (2019-10-02 03:44 UTC)

<p>Can you post a link to a json file that contains named landmarks? Statismo file format is probably only used by that software, so Slicer would not adopt it as is, but we could still learn from it.</p>

---

## Post #10 by @Emmanuel_Salinas_Mir (2020-07-18 12:29 UTC)

<p>Hi</p>
<p>EPAD also works with JSON landmarks using AIM protocol<a href="https://wiki.nci.nih.gov/display/AIM/Annotation+and+Image+Markup+-+AIM" rel="nofollow noopener">Annotation and Image Markup - AIM</a>.</p>

---

## Post #11 by @lassoan (2020-07-18 14:48 UTC)

<p>We checked out AIM but in many aspects it was too complex, yet it would have been too limiting to be used as an internal storage format. We decided that if there is interest then exporter/importer can be added for this format (similarly to DICOM).</p>

---
