---
topic_id: 16387
title: "Segmentcomparison Hausdorff Metric"
date: 2021-03-05
url: https://discourse.slicer.org/t/16387
---

# SegmentComparison hausdorff metric

**Topic ID**: 16387
**Date**: 2021-03-05
**URL**: https://discourse.slicer.org/t/segmentcomparison-hausdorff-metric/16387

---

## Post #1 by @muratmaga (2021-03-05 07:14 UTC)

<p>Is the Hausdorff 95% means the value at 95th percentile?</p>

---

## Post #2 by @cpinter (2021-03-05 08:55 UTC)

<p>Yes.</p>
<p>Here’s the documentation from which there are links to the algorithm details but they are not accessible at the moment.<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/SegmentComparison" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/SegmentComparison</a><br>
<a class="mention" href="/u/gcsharp">@gcsharp</a> have you seen that the Plastimatch doxygen is down?</p>

---

## Post #3 by @gcsharp (2021-03-05 15:57 UTC)

<p>Yes, I know.  My web hosting provider exited the marketplace.  <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=9" title=":frowning:" class="emoji" alt=":frowning:">  Currently evaluating my options…</p>

---

## Post #4 by @lassoan (2021-03-05 17:18 UTC)

<p>I would recommend using github pages and/or readthedocs for hosting documentation. Readthedocs can be configured to generate and host doxygen documentation. It is very easy to integrate readthedocs with github so that the documentation is automatically updated whenever you commit a change.</p>

---

## Post #5 by @gcsharp (2021-03-05 23:15 UTC)

<p>I have a temporary site up now.  May take a day or so for DNS to update. Anyway, the below page should help to understand the formulas being used.</p>
<p><a href="https://plastimatch.gitlab.io/plastimatch/doxygen/classHausdorff__distance.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://plastimatch.gitlab.io/plastimatch/doxygen/classHausdorff__distance.html</a></p>

---
