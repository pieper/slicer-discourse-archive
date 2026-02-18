# What is the proper way of including a GPL licensed code in an extension

**Topic ID**: 40946
**Date**: 2025-01-03
**URL**: https://discourse.slicer.org/t/what-is-the-proper-way-of-including-a-gpl-licensed-code-in-an-extension/40946

---

## Post #1 by @muratmaga (2025-01-03 19:11 UTC)

<p>We need to use code from this repository <a href="https://github.com/zsiki/Find-GCP" class="inline-onebox" rel="noopener nofollow ugc">GitHub - zsiki/Find-GCP: Find ArUco markers in digital photos</a> for the photogrammetry extension we are building. This code is licensed under GPL2.</p>
<p>My understanding is historical GPL licenses are not considered compatible with Slicer’s license and community’s modus operandi.</p>
<p>If we provide a button for the user to clone/download the repo (like ffmpeg) at the time of execution, is that considered acceptable?   If not, what would be the acceptable approach?</p>

---

## Post #2 by @pieper (2025-01-03 19:19 UTC)

<p>As long as we aren’t the ones distributing the code then there’s no problem with users installing GPL’d or similar code to use with Slicer.  So yes, a button like the one for ffmpeg is a good solution.</p>

---

## Post #3 by @shai-ikko (2025-01-06 08:18 UTC)

<p>AFAIK, It is not always that simple.</p>
<p>Code that depends on GPL’d code may potentially be considered a “derivative work” (which would trigger the license incompatibilities), regardless of if the GPL’d code is distributed with it. Details of how you use that code matter, and the existence alternatives (i.e. pieces of code that could replace the GPL’d module) may matter.</p>
<p>I am not a lawyer, and the only safe advice is to consult one.</p>

---
