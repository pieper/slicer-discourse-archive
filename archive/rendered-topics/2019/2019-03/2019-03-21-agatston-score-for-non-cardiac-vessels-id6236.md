---
topic_id: 6236
title: "Agatston Score For Non Cardiac Vessels"
date: 2019-03-21
url: https://discourse.slicer.org/t/6236
---

# Agatston score for non-cardiac vessels

**Topic ID**: 6236
**Date**: 2019-03-21
**URL**: https://discourse.slicer.org/t/agatston-score-for-non-cardiac-vessels/6236

---

## Post #1 by @Akarken (2019-03-21 12:55 UTC)

<p>There ise a topic about agatston score already. But i could not manage to calculate.</p>
<p>I tried the method of segmenting and set the lower threshold value to 130.</p>
<p>But i could not go any futher than greens areas which may indicate calcification. I want to calculate the calcification score of some abdominal vessels.</p>
<p>Can you post a video about how to score calcification, or can you give more simple explanation about this topic( i am out of engineering profession, i could’nt apply the mentioned script).</p>
<p>Thank you again.</p>

---

## Post #2 by @lassoan (2019-03-21 20:20 UTC)

<p>(I’ve removed your duplicate post from <a href="https://discourse.slicer.org/t/cardiacagatstonscoring/1544/12" class="inline-onebox">"CardiacAgatstonScoring".</a>)</p>
<p>It is not clear what modules you tried to use and how. Could you please describe step by step (or record a video) of what you did and tell what you expected to happen and what happened instead?</p>

---

## Post #3 by @Akarken (2019-03-27 21:58 UTC)

<p>Thank you for the reply, and sorry for the delay.</p>
<p>I was trying to calculate agatston score of the renal arteria, and found that tutorial file “<a href="https://na-mic.org/w/images/4/4b/TutorialContest_CardiacAgatstonScoring_2014.pdf" rel="nofollow noopener">https://na-mic.org/w/images/4/4b/TutorialContest_CardiacAgatstonScoring_2014.pdf</a>” but as mentioned in the topic before, the scoring module did not work.</p>
<p>After that point i was lookin for some help, and found the topic that you were talking about agatson scoring.</p>
<p>As you indicated. I  loaded a test image, added a new segment, set the threshold value as &lt;130 HU. At that point, there were green areas, like the images on the tutorial pdf, which indicates areas with HU unit over 130 (calcification). That was the point i stuck.</p>
<p>I could not understand the concept of adding a new segment for each vessel and island effect part. So i kept reading the topic, and saw your post about metrics. “If you need to compute the metric slice by slice then you can use Mask volume effect (available in Segment Editor module after you install SegmentEditorExtraEffects extension)”</p>
<p>I loaded the extension you mentioned above, but could not initiate the script. Everything became more complicated after that point.</p>
<p>Sorry about the inconvenience, I hope, i have managed to tell what i tried, properly.</p>

---
