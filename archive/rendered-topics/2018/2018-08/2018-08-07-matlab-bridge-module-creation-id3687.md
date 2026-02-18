# Matlab Bridge Module Creation

**Topic ID**: 3687
**Date**: 2018-08-07
**URL**: https://discourse.slicer.org/t/matlab-bridge-module-creation/3687

---

## Post #1 by @aginn (2018-08-07 20:06 UTC)

<p>Hi all,</p>
<p>I am relatively new to 3D Slicer and Matlab Bridge.</p>
<p>I have been using Matlab Bridge to create a custom module to cut down on my segmentation times. Is there a way to call and execute a pre-existing 3D Slicer Module (e.g. Grow Segmentation from Segment Editor or Generate/Export 3D model from Segmentations) within my .m file?</p>
<p>Any help would be appreciated - thanks in advance!</p>

---

## Post #2 by @cpinter (2018-08-07 20:29 UTC)

<p>I think the opposite approach would be easier and more appropriate. What I mean is writing a python script or module that drives the Segment Editor effects, and also calls your Matlab Bridge module to execute the algorithm. The intention with Matlab Bridge was to enable executing Matlab computations, and not to allow Matlab to drive a Slicer processing pipeline.</p>

---

## Post #3 by @lassoan (2018-08-07 20:57 UTC)

<p>You can find here examples of how to run segment editor effects from Python as shown in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">script repository</a>.</p>

---

## Post #4 by @aginn (2018-08-07 21:10 UTC)

<p>Thank you! I will do this instead.</p>

---

## Post #5 by @lassoan (2019-09-10 13:08 UTC)

<p>A post was split to a new topic: <a href="/t/how-to-call-matlab-module-from-python-scripted-module/8362">How to call Matlab module from Python scripted module</a></p>

---
