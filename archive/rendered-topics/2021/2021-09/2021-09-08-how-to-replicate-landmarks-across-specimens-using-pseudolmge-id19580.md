# How to replicate landmarks across specimens using PseudoLMGenerator fiducials

**Topic ID**: 19580
**Date**: 2021-09-08
**URL**: https://discourse.slicer.org/t/how-to-replicate-landmarks-across-specimens-using-pseudolmgenerator-fiducials/19580

---

## Post #1 by @Siobhan_Summers (2021-09-08 18:34 UTC)

<p>Operating system: Windows 10 Home<br>
Slicer version: 4.13.0</p>
<p>I’m using PseudoLMGenerator to landmark an asymmetrical bone for a morphometric analysis. Can the landmark data collected be used to compare specimens in a morphometric study even though the pseudo-landmarks will not be in the exact same location on each specimen? If not, is there a way to use the same pseudo-landmarks across specimens?</p>

---

## Post #2 by @muratmaga (2021-09-08 20:48 UTC)

<p>PseudoLMGenerator is a tool to generate a “landmark template” that will be used across a study. If you change the reference specimen that you use with the PseudoLMGenerator, you will not get the same set of landmarks. So it is important to use a specimen that will be representative of population, or even generate a sample average (so that the template is not bias against/for any of the specimens). See the tutorial at <a href="https://github.com/SlicerMorph/Tutorials/tree/main/PseudoLMGenerator" rel="noopener nofollow ugc">https://github.com/SlicerMorph/Tutorials/tree/main/PseudoLMGenerator</a></p>
<p>You will need a tool like ALPACA or a set of fixed LMs to transfer this template to target samples.</p>
<p>So, in short you cannot generate pseudoLMs for every specimen, and run an analysis on them, since the number of landmarks and their placement will be different. You can try placeSemiLMPatches module for that. However, you should have a set of fixed LM to be able to use that tool.</p>

---

## Post #3 by @Siobhan_Summers (2021-09-13 15:52 UTC)

<p>Thank you for your response and for the additional resources!</p>

---
