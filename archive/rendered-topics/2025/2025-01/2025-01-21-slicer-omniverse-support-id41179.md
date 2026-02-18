# Slicer Omniverse Support

**Topic ID**: 41179
**Date**: 2025-01-21
**URL**: https://discourse.slicer.org/t/slicer-omniverse-support/41179

---

## Post #1 by @Islam_Ibrahim (2025-01-21 01:19 UTC)

<p>Hi<br>
I’m going to build extention to export slicer model to Nvidia omniverse</p>

---

## Post #2 by @jcfr (2025-01-21 05:55 UTC)



---

## Post #3 by @jcfr (2025-01-21 06:01 UTC)

<p>It may be worth looking into re-using the VTK module <code>vtkOmniverseConnector</code> developed in the context of <a href="https://github.com/NVIDIA-Omniverse/ParaViewConnector/">NVIDIA-Omniverse/ParaViewConnector/</a> project.</p>
<p>Related to USD support, the recent work from <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> published in Slicer pull request <a href="https://github.com/Slicer/Slicer/pull/8141">#8141</a> is likely relevant.</p>
<p>cc: <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a></p>
<hr>
<p><em>This post follows up on a question of <a class="mention" href="/u/islam_ibrahim">@Islam_Ibrahim</a> originally posted on <a href="https://discourse.slicer.org/t/slicer-hackathon-hosted-by-kitware-january-24th-2025/41096/3" class="inline-onebox">Slicer Hackathon hosted by Kitware: January 24th, 2025 - #2 by jcfr</a> and moved into a dedicated topic.</em></p>

---

## Post #4 by @Islam_Ibrahim (2025-01-21 06:06 UTC)

<p>is that allowed in the Hackathon</p>

---

## Post #5 by @Davide_Punzo (2025-01-21 08:17 UTC)

<p>there is also this importer <a href="https://github.com/f3d-app/f3d/tree/master/plugins/usd/module" class="inline-onebox" rel="noopener nofollow ugc">f3d/plugins/usd/module at master · f3d-app/f3d · GitHub</a>.</p>
<p>regarding <a href="https://github.com/Slicer/Slicer/pull/8141" class="inline-onebox" rel="noopener nofollow ugc">ENH: Add JSON format for writing/reading scene and nodes by Punzo · Pull Request #8141 · Slicer/Slicer · GitHub</a> is a preliminary PR for JSON support, but yes on the long term ideally we would like to support OpenUSD in Slicer core.</p>

---
