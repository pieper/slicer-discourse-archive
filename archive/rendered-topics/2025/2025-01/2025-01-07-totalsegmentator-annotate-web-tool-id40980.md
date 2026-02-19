---
topic_id: 40980
title: "Totalsegmentator Annotate Web Tool"
date: 2025-01-07
url: https://discourse.slicer.org/t/40980
---

# Totalsegmentator annotate web tool

**Topic ID**: 40980
**Date**: 2025-01-07
**URL**: https://discourse.slicer.org/t/totalsegmentator-annotate-web-tool/40980

---

## Post #1 by @Gokce_Guven (2025-01-07 11:09 UTC)

<p>Hi,</p>
<p>I am using the Total Segmentator Annotate web tool to segment vertebrae and have annotated approximately 218 segments so far. I’d like to continue contributing to the segmentation of vertebrae, but when I click the “Next Subject” button, previously annotated subjects reappear.</p>
<p>Will you be adding more subjects for segmentation? I am eager to help further and contribute to improving the accuracy of Total Segmentator. Could you guide me on how to proceed?</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2025-01-07 15:53 UTC)

<p>The <a href="https://annotate.totalsegmentator.com/">rudimentary web tool for submitting corrections to TotalSegmentator’s training data</a> is not related to Slicer, so I don’t know what is going on internally. <a class="mention" href="/u/wasserth">@wasserth</a> can give definitive answer, but my understanding is that:</p>
<ul>
<li>You always start from the current segmentation and make corrections.</li>
<li>It is unlikely that new subjects will be added to the current CT image set, as it is already considered a sufficiently large and diverse data set. If you have special data (e.g., spine with bone mets) then you could use the TotalSegmentator model as a starting point and fine-tune it for your application.</li>
</ul>

---

## Post #3 by @wasserth (2025-02-28 10:04 UTC)

<p><a class="mention" href="/u/gokce_guven">@Gokce_Guven</a> Thank you for your contribution to TotalSegmentator Annotate! This is greatly appreciated. You have probably corrected the vertebrae for all available subjects. Now you can switch to one of the other available masks and start correcting those. There is a lot of work left <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> . In your profile on <a href="http://annotate.totalsegmentator.com" rel="noopener nofollow ugc">annotate.totalsegmentator.com</a> you can also add your email address, then i can contact you directly with relevant information.</p>

---
