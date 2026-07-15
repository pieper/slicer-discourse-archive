---
topic_id: 46206
title: "Abdominal Muscle Segmentation any better ways to approach this?"
date: 2026-02-18
url: https://discourse.slicer.org/t/46206
last_bumped: 2026-07-14T16:00:34.093Z
---

# Abdominal Muscle Segmentation any better ways to approach this?

**Topic ID**: 46206
**Date**: 2026-02-18
**URL**: https://discourse.slicer.org/t/abdominal-muscle-segmentation-any-better-ways-to-approach-this/46206

---

## Post #1 by @CS1 (2026-02-18 05:18 UTC)

<p>Hello there,</p>
<p>I’ve been using total segmentator, 3D slicer for the past few months trying to get the volumetric data for body composition of the lumbar region. I have to say that it is a great resource and gives you a decent segmentation result, however, I’ve also noticed multiple issues such as some muscle groups are poorly segmented requiring lots of manual correction or there is segmentation error when it comes to intermuscular fat which requires thresholding with HU.</p>
<p>I intended to train my own model however I have zero background in coding, python and I had no dataset for me to train my own AI. On top of that I don’t even know if it’s gonna perform better than total segmentator which was trained using triple the number of segmented CTs than what I’ve got…</p>
<p>I’m now very stuck, each CT takes me 30-40 mins to segment including the time requires for manual correction, took me 4 months to go through 130 patients with 2 CT scans each…</p>
<p>Any suggestions on how I can improve my workflow and methods.. any other tools that I could potentially use? I’d love to include more patients but I don’t think this is a sustainable approach..</p>
<p>I’m very grateful for this supportive community, I don’t think I could make it this far without this forum and all the help I’ve received. thank you thank you.</p>

---

## Post #2 by @rkikinis (2026-02-18 06:43 UTC)

<p>Hi<br>
there are several options in terms of trained networks. Have you checked them out?<br>
<a href="https://arxiv.org/pdf/2512.15921" class="onebox" target="_blank" rel="noopener nofollow ugc">https://arxiv.org/pdf/2512.15921</a><br>
Best<br>
Ron</p>

---

## Post #3 by @drnoorfatima (2026-02-19 02:36 UTC)

<p>Hi,</p>
<p>I completely understand this frustration….30-40 minutes per scan for manual correction is exactly the kind of workflow bottleneck that makes scaling impossible, and you’ve already proven that with 4 months invested on 260 scans.</p>
<p>The good news: this problem is solvable without you needing to learn Python or train your own model from scratch.</p>
<p>The bad news: TotalSegmentator’s limitations for lumbar body composition (especially intermuscular fat and specific muscle groups) aren’t something you can easily fix with settings adjustments alone.</p>
<p>There are approaches that would dramatically reduce your per-scan time and let you scale to more patients, but they require either:</p>
<ol>
<li>A custom segmentation pipeline optimized for your specific imaging protocol and the muscle groups TotalSegmentator struggles with</li>
<li></li>
<li>Semi-automated workflows with smart preprocessing that reduce manual correction to 5-10 mins per scan instead of 30-40</li>
</ol>
<p>Given the scale you’re working at and want to reach, this is worth solving properly.</p>
<p>I work as a freelancer on medical imaging segmentation projects like this ….body composition workflows are something I’ve optimized before. If you’d like to discuss how to fix your workflow so you can actually scale your study, DM me. Happy to look at your data and give you specific recommendations.</p>
<p>You’ve already invested 4 months…getting this right now will save you that much time on the next 100+ patients.</p>

---

## Post #4 by @kennethaweberii (2026-07-14 16:00 UTC)

<p>The free and open-source MuscleMap extension can provide muscle segmentation: <a href="https://discourse.slicer.org/t/new-extension-musclemap-automated-whole-body-muscle-segmentation/47364" class="inline-onebox">New extension: MuscleMap --  Automated Whole-Body Muscle Segmentation</a></p>
<p>We are working towards automated whole-body contrast-agnostic muscle segmentation for MRI and CT. The current model does not include the abdominal muscles, but we can work with you to develop a solution. Please feel free to reply to the MuscleMap extension in the new topic via the above link.</p>
<p>Also, feel free to suggest any new features that may be helpful for your needs. We are here to help!</p>

---
