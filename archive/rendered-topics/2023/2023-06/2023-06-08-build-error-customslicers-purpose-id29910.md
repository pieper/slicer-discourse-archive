# Build Error & CustomSlicer's Purpose

**Topic ID**: 29910
**Date**: 2023-06-08
**URL**: https://discourse.slicer.org/t/build-error-customslicers-purpose/29910

---

## Post #1 by @dsa934 (2023-06-08 06:34 UTC)

<p>Operating system: window 10<br>
Slicer version: 5.2.1</p>
<p>Hi all,</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63bf0ceac89a0a45826fb0c9e4aefbfad8537eb4.png" alt="image" data-base62-sha1="eeoAMC4qKQtXNQgJn7TNPMyiWkA" width="685" height="147"></p>
<p>Q1. When the Cmake → build process was performed for each of three slicer5.2.1, slicer5.2.2, and CustomSlicer, the same permission error for the vtk folder occurred. What to do in this case?</p>
<p>Q2. I’ve heard that CustomSlicer allows you to customize many things without changing the slicer’s core, but is the ‘many’ mentioned here only about the GUI?</p>

---

## Post #2 by @lassoan (2023-06-16 14:59 UTC)

<p>The build tree does not look similar to what you get by following the build instructions, so we cannot even guess what could cause the write permission issue.</p>
<p>You can customize complete behavior of Slicer in a custom application, not just the GUI.</p>

---
