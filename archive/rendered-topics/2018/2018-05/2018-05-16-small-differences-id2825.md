---
topic_id: 2825
title: "Small Differences"
date: 2018-05-16
url: https://discourse.slicer.org/t/2825
---

# Small differences

**Topic ID**: 2825
**Date**: 2018-05-16
**URL**: https://discourse.slicer.org/t/small-differences/2825

---

## Post #1 by @Olof (2018-05-16 08:49 UTC)

<p>Hi Martin and Beau,<br>
I am running a shape analysis  in which there are very small differences between groups - and at some points one group is larger than the other - in other places it is the opposite  …<br>
Using the old shape analysis mancova wizard … I find it difficult to interpret the results … what one really would like is some option (like in correlation) in which I can ask for one sided test … like is group 1 larger than group 0 and the opposite.</p>
<p>Is there any way of getting such results?</p>
<p>best<br>
Olof</p>

---

## Post #5 by @styner (2018-05-24 19:39 UTC)

<p>Hi Olof<br>
Sorry for the delayed answer.</p>
<ol>
<li>If I understand correctly the order of the groups is not consistent across the surface (as some regions have group A &gt; group B and other regions otherwise). It would not make sense to use a one-sided test in such as setting. One sided tests should only be used if there is independent reasoning why group A &gt; group B (or vice versa), e.g. if by design one group should be larger than the other.</li>
<li>the shape analysis results (if you look at the mean difference) should tell whether and where group A &gt; B or vice versa.<br>
Best<br>
Martin</li>
</ol>

---
