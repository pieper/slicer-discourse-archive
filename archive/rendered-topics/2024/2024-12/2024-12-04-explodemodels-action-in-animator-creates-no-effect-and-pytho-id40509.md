---
topic_id: 40509
title: "Explodemodels Action In Animator Creates No Effect And Pytho"
date: 2024-12-04
url: https://discourse.slicer.org/t/40509
---

# ExplodeModels Action in Animator Creates no effect, and Python code does not run an error message

**Topic ID**: 40509
**Date**: 2024-12-04
**URL**: https://discourse.slicer.org/t/explodemodels-action-in-animator-creates-no-effect-and-python-code-does-not-run-an-error-message/40509

---

## Post #1 by @ibehar (2024-12-04 14:59 UTC)

<p>I am learning how to use the Animator module in SlicerMorph for a class assignment and none of the inputted segments seem to respond to the ExplodeModels action. Other actions (like rotation) seem to function fine, but I can’t seem to pinpoint what is going wrong with this one.</p>
<p>What baffles me is that there is no error message in response to my animation setup, or any Python code running at all. I’m not quite sure where to start looking to troubleshoot this problem and would appreciate any insight to help lead me in the right direction.</p>
<p>So far I have tried the following, to no avail:</p>
<ul>
<li>Experimented with the calibrations for all of the animation parameters and the bar beneath ExplodeModels</li>
<li>Uninstalled and reinstalled Slicer Morph</li>
<li>Uninstalled and redownloaded Slicer</li>
<li>Double-checked my volume &amp; segmentation inputs</li>
</ul>
<p>Operating system: MacOS Sequoia 15.1<br>
Slicer version: 5.6.2</p>

---

## Post #2 by @muratmaga (2024-12-04 15:20 UTC)

<p>You need to export the segmentations to models first. Right click on the segmentation object, and then choose export visible segments to models.</p>
<p>Then use that for exploding models.</p>

---
