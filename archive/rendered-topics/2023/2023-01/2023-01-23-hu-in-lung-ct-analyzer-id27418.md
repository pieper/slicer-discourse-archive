---
topic_id: 27418
title: "Hu In Lung Ct Analyzer"
date: 2023-01-23
url: https://discourse.slicer.org/t/27418
---

# HU in Lung CT Analyzer

**Topic ID**: 27418
**Date**: 2023-01-23
**URL**: https://discourse.slicer.org/t/hu-in-lung-ct-analyzer/27418

---

## Post #1 by @Paula_R (2023-01-23 14:36 UTC)

<p>Hello,</p>
<p>I’m using the Lung CT Analyzer, and the thresholds range of HU for the lung parenchyma (bulla, vessels, etc) go from -1050 to 1000. Now, I’ve read in the literature that the whole range of HU goes from -1000 (for air) to +1000 (for compact bone) and that the range for lung is a part of that. In some literature the HU range for lung is supposed to be -400 to -600, or -600 to -950, and there’s no consensus. My point is, if -1000 to 1000 is the whole HU range and the lung HU range is a part of that, why bulla goes from -1050 to -950, inflated from -950 to -750, and so on? Why are you using these threshold ranges? I don’t find consensus in the literature on this issue.</p>
<p>Thank you.</p>

---

## Post #2 by @rbumm (2023-01-23 15:51 UTC)

<p>Hi,</p>
<p>This is an important question and there is no consensus on definite ranges, they slightly vary for CT scanners/conditions. The ranges in LCTA have a preset that works well under most, but not all circumstances. You can use the preview function to see whether the regions (bullae, inflated, infiltrated, collapsed, vessel) will be correctly segmented. The thresholds are persistent in the  ParameterNode of the scene when you save it after Lung CT Analysis.</p>
<p>It is a future goal for LCTA to normalize HU ranges when analyzing bigger databases. Maybe <a class="mention" href="/u/rkikinis">@rkikinis</a> can comment on the problem, too.</p>

---
