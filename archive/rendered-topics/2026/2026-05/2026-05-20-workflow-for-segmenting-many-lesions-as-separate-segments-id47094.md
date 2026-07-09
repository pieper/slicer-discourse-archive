---
topic_id: 47094
title: "Workflow for segmenting many lesions as separate segments?"
date: 2026-05-20
url: https://discourse.slicer.org/t/47094
last_bumped: 2026-07-08T08:56:49.097Z
---

# Workflow for segmenting many lesions as separate segments?

**Topic ID**: 47094
**Date**: 2026-05-20
**URL**: https://discourse.slicer.org/t/workflow-for-segmenting-many-lesions-as-separate-segments/47094

---

## Post #1 by @zhousy5310 (2026-05-20 10:07 UTC)

<p>Hi all,</p>
<p>I’m currently working on NF1 cases using Slicer, and trying to find a better workflow.</p>
<p>The main difficulty is not segmenting one lesion, but handling many separate lesions efficiently while keeping them as different segments/labels.</p>
<p>For this kind of task, what would people normally use in Slicer?</p>
<p>I tried nnInteractive, but I’m not sure if it is the right workflow for this. It seems better for one object at a time, while for many separate lesions I’m having trouble keeping the workflow efficient and stable.</p>
<p>I’m currently looking into Islands / Split islands, Grow from seeds, and Logical operators, but the workflow still feels quite tedious. I’m mainly looking for a practical workflow, not necessarily a fully automatic model..</p>
<p>I’m mainly looking for a practical workflow, not necessarily a fully automatic model.</p>
<p>Many Thanks!</p>

---

## Post #2 by @pieper (2026-05-21 11:17 UTC)

<p>I’m not familiar with NF1 lesions, and I’m not sure what you mean by “practical” - how many cases do you need to segment?  How much time are you able to commit?  How accurate do they need to be?  What modality of imaging?  Maybe you can include screenshots of the data and what your segmentations look like now.</p>

---

## Post #3 by @zhousy5310 (2026-05-25 11:38 UTC)

<p>Hi Steve, thanks for your quick reply. About screenshots, I’m afraid that i can’t share them due to patient confidentiality, but I can describe my situation here:<span lang="EN-US"></span></p>
<ol>
<li>Modality: 3T MRI, T2-weighted fat-sat and post-contrast T1. NF1-related neurofibromas (plexiform and cutaneous). <span lang="EN-US"></span></li>
<li>Lesion: Typically 30–80 small ovoid lesions per case, 3–20 mm diameter, scattered in subcutaneous fat and along nerve sheaths (torso and extremities). Many are hyperintense on T2, clearly visible against fat.<span lang="EN-US"></span></li>
<li>Current method: I manually draw ROIs slice-by-slice. That’s the tedious part. <span lang="EN-US"></span></li>
<li>Case load: ~20 cases. Need accuracy good enough for volume change over time (not for surgical planning). I’m willing to invest time in a good workflow but not in training a deep learning model from scratch.</li>
</ol>
<p>Sorry my english is not that good. So i use AI to rephrase, hope you dont mind. <img src="https://emoji.discourse-cdn.com/twitter/folded_hands.png?v=15" title=":folded_hands:" class="emoji" alt=":folded_hands:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @pieper (2026-07-02 20:03 UTC)

<p>Sorry for the slow response - the message got buried in my inbox.  I would suggest nnInteractive if you haven’t already found it.  It would probably work well for that scenario.</p>

---

## Post #5 by @zhousy5310 (2026-07-07 11:09 UTC)

<p>Hi Steve,</p>
<p>No worries at all, and thanks for getting back to me. Since my previous post, I have also been looking at some AAA cases, so the task has changed a bit.</p>
<p>I did try nnInteractive since. It is a really impressive tool, and I can see how it would probably work well for NF1-type lesions. However, for current goal: AAA/aorta segmentation, I am still not sure if I am using it in the best way.</p>
<p>Firstly, the aorta is a long structure, when I add prompts in the lower part of the vessel, sometimes the upper part changes or disappears. Also, after several prompts, it becomes hard for me to understand which region has been updated, expanded, or reduced.</p>
<p>At the moment, my practical workflow is to use nnInteractive once to get an initial segmentation, and then continue with manual editing. But I feel I may be missing a better way to use it.</p>
<p>May I ask whether this behavior is expected for long structures like the aorta? Have you seen similar issues before, and is there a recommended workflow to avoid overwriting or losing previously segmented regions?</p>
<p>Thanks again for your help.</p>

---

## Post #6 by @pieper (2026-07-08 08:56 UTC)

<p>You can report the specifics of the segmentation behavior to the <a href="https://github.com/MIC-DKFZ/nnInteractive">nnInteractive</a> team, ideally with exact steps to replicate on public data.</p>
<p>In general, segmentation is a difficult task, so you need to experiment with what works well for your data.  If you have contrast enhanced CT, you might find that Grow from seeds works well for you task.</p>

---
