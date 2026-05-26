---
topic_id: 46213
title: "issues with Elastix tool"
date: 2026-02-18
url: https://discourse.slicer.org/t/46213
last_bumped: 2026-02-20T09:48:55.155Z
---

# issues with Elastix tool

**Topic ID**: 46213
**Date**: 2026-02-18
**URL**: https://discourse.slicer.org/t/issues-with-elastix-tool/46213

---

## Post #1 by @Martina_Ma (2026-02-18 17:25 UTC)

<p>Operating system: Windows 11 PRO<br>
Slicer version: 5.10.0<br>
Hi everyone,</p>
<p>I’m trying to use Elastix tool to register a CT scan with a CBCT one but the tool doesn’t work anymore and gives error. I already resampled the volume size of both the scans.</p>
<p>Has anyone had a similar problem?</p>

---

## Post #2 by @drnoorfatima (2026-02-19 02:28 UTC)

<p>Hi,</p>
<p>Elastix errors on CT-CBCT registration are usually related to one of a few things: memory issues with large volumes, parameter file incompatibility with Slicer 5.10, or field of view mismatches between the two acquisitions.</p>
<p>What’s the specific error message you’re getting? That would help narrow down what’s happening.</p>
<p>Also, CT and CBCT registration can be tricky even when Elastix runs without errors, the intensity ranges and image characteristics are quite different, so the registration quality depends a lot on the right parameter settings for your specific use case.</p>

---

## Post #3 by @lassoan (2026-02-20 00:31 UTC)

<p><a class="mention" href="/u/martina_ma">@Martina_Ma</a> Does it work if you use the <code>MRBrainTumor1</code> and <code>MRBrainTumor2</code> data sets as fixed and moving volume, you choose a new volume as output volume, and you use the default registration settings?</p>

---

## Post #4 by @Martina_Ma (2026-02-20 09:48 UTC)

<p>Hi <a class="mention-group" href="/groups/internationalization">@Internationalization</a> and <a class="mention" href="/u/drnoorfatima">@drnoorfatima</a>,</p>
<p>thank you both for the answers. I think I solved the issue.</p>
<p>Thanks a million.</p>

---
