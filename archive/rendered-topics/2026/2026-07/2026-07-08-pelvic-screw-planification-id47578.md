---
topic_id: 47578
title: "Pelvic screw planification "
date: 2026-07-08
url: https://discourse.slicer.org/t/47578
last_bumped: 2026-07-08T15:46:40.858Z
---

# Pelvic screw planification 

**Topic ID**: 47578
**Date**: 2026-07-08
**URL**: https://discourse.slicer.org/t/pelvic-screw-planification/47578

---

## Post #1 by @Emile_Vandromme (2026-07-08 11:08 UTC)

<p>Hi everyone,</p>
<p>I’m an orthopedic trauma surgeon and I’m currently trying to use 3D Slicer for preoperative planning of trans-sacral and sacroiliac screw fixation.</p>
<p>I’m looking for a way to simulate the screw trajectory directly on CT images. Ideally, I see two possible approaches:</p>
<ul>
<li><strong>A dedicated extension</strong> that allows virtual screw placement. I tried looking at the pedicle screw planning tools, but they don’t seem well suited for trans-sacral/sacroiliac screws.</li>
<li><strong>A simple 3D cylinder model</strong> representing the screw, which could be interactively positioned and rotated while remaining visible in all MPR views (axial, coronal, sagittal, and oblique). This would already be extremely useful for planning safe corridors and evaluating screw trajectories.</li>
</ul>
<p>Does anyone know of an existing extension, workflow, or module that could accomplish this? Any suggestions or examples would be greatly appreciated.</p>
<p>Thank you in advance for your help!</p>

---

## Post #2 by @chir.set (2026-07-08 11:57 UTC)

<aside class="quote no-group" data-username="Emile_Vandromme" data-post="1" data-topic="47578">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/emile_vandromme/48/77956_2.png" class="avatar"> Emile_Vandromme:</div>
<blockquote>
<ul>
<li><strong>A simple 3D cylinder model</strong> representing the screw</li>
</ul>
</blockquote>
</aside>
<p>You may check the <code>Create models</code> module of the <code>IGT</code> extension.</p>

---

## Post #3 by @PuxunTu (2026-07-08 15:46 UTC)

<p>Hi, we are currently developing an extension for AI-agent-driven pelvic fracture reduction and screw placement planning. You can find a demo video on <a href="https://github.com/puxuntu/Slicer_agent_for_surgical_planning" class="inline-onebox" rel="noopener nofollow ugc">GitHub - puxuntu/Slicer_agent_for_surgical_planning: Agentic System for 3D Slicer Software Manipulation · GitHub</a></p>
<p>this is still a work in progress and not all features have been released. We plan to make it available to the community once development is complete. In the meantime, you may find our previous project on pelvic fracture reduction planning useful: <a href="https://github.com/Bolun-Z/PelvicFracturePlanning" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Bolun-Z/PelvicFracturePlanning · GitHub</a> , along with the following related publications::</p>
<p>[1] Zeng, Bolun, et al. “Two-stage structure-focused contrastive learning for automatic identification and localization of complex pelvic fractures.” <em>IEEE Transactions on Medical Imaging</em> 42.9 (2023): 2751-2762.</p>
<p>[2] Liu, Jiaxuan, et al. “An end-to-end geometry-based pipeline for automatic preoperative surgical planning of pelvic fracture reduction and fixation.” <em>IEEE transactions on medical imaging</em> 44.1 (2024): 79-91.</p>
<p>[3] Zeng, Bolun, et al. “A bidirectional framework for fracture simulation and deformation-based restoration prediction in pelvic fracture surgical planning.” <em>Medical Image Analysis</em> 97 (2024): 103267.</p>

---
