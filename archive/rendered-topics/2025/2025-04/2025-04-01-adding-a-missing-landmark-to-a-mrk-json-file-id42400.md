---
topic_id: 42400
title: "Adding A Missing Landmark To A Mrk Json File"
date: 2025-04-01
url: https://discourse.slicer.org/t/42400
---

# Adding a missing landmark to a mrk.json file 

**Topic ID**: 42400
**Date**: 2025-04-01
**URL**: https://discourse.slicer.org/t/adding-a-missing-landmark-to-a-mrk-json-file/42400

---

## Post #1 by @grega (2025-04-01 16:33 UTC)

<p>I have a point on a bone that i’m landmarking that isn’t present on all the samples in my data set. To be able to run GPA+PCA analysis I need to have a consistent number of points for each sample, so is there a way I can add a “missing landmark” so I can keep the number of landmarks the same, while not impacting the PCA slicer gives me?</p>

---

## Post #2 by @muratmaga (2025-04-03 04:15 UTC)

<p>You can. However that landmark needs to be in the same spot (e.g., if it is the 3rd landmark, it has to be in that position like every other dataset).</p>
<p>See this tutorial section on how to designate a control point (landmark) as missing: <a href="https://github.com/SlicerMorph/Tutorials/tree/main/Markups_1#the-control-points-menu" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/Markups_1 at main · SlicerMorph/Tutorials · GitHub</a></p>
<p>When you are setting your GPA analysis do not forget to enter the index (in my example 3) of that landmark into the <code>exclude landmarks</code> field. Otherwise your analysis won’t work.</p>
<p>(To clarify, you are technically designating the landmark as <strong>SKIPPED</strong> -as opposed to missing- in Slicer. THen you are telling GPA module to exclude it).</p>

---
