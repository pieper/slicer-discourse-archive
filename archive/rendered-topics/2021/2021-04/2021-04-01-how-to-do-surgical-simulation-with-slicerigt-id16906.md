---
topic_id: 16906
title: "How To Do Surgical Simulation With Slicerigt"
date: 2021-04-01
url: https://discourse.slicer.org/t/16906
---

# how to do surgical simulation with slicerIGT

**Topic ID**: 16906
**Date**: 2021-04-01
**URL**: https://discourse.slicer.org/t/how-to-do-surgical-simulation-with-slicerigt/16906

---

## Post #1 by @Sophie_Legendri (2021-04-01 13:09 UTC)

<p>Operating system: OLEA<br>
Slicer version: 4.11.202009<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello,<br>
I’m an OBGYN resident, and i’m a beginner with slicer (it’s been a few month since i’m using this great software), i’m working on a medical project of surgical planning, and i would like to know how can i add a stylus in my surgical scene for simulation (to see the entry point). Is it a way to do it directly or with Python code? I load the IGT slicer extension but i don’t really understand how to use it?<br>
I would need some help to do it.<br>
Regards,<br>
Sophie</p>

---

## Post #2 by @pieper (2021-04-01 18:04 UTC)

<p>That’s sounds like a great idea.  Did you read through the tutorials on SlicerIGT’s web page?</p>
<p><a href="http://www.slicerigt.org/wp/" class="onebox" target="_blank" rel="noopener">http://www.slicerigt.org/wp/</a></p>

---

## Post #3 by @Sophie_Legendri (2021-04-08 14:21 UTC)

<p>Hello Steeve,<br>
Thank you for your answer. Actually, i’m trying to do surgical planning but not in real time, i would like to had a device in my 3D reconstruction scene and see differents path for the “endoscope”. Is it possible to had a stylus or other device responding to my mouse movements permitting to see hypothetics paths?</p>
<p>Best regards,<br>
Sophie</p>

---

## Post #4 by @pieper (2021-04-09 18:28 UTC)

<p>Hi Sophie -</p>
<p>From the Slicer point of view, at some level we treat motions that come from trackers the same as motions that come from a mouse.  Both are used to control Transforms, that can be used to manipulate objects in the scene.  These objects might be simulated instruments or scopes.  So I think SlicerIGT is a good place to get a sense of what’s possible, but you can ignore the details of connecting a physical tracker.</p>
<p>HTH,<br>
Steve</p>

---

## Post #5 by @lassoan (2021-04-10 04:40 UTC)

<p>You can import an STL model or generate models using “Create Models” module in SlicerIGT extension, then <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#apply-transform-to-a-node">move it around using a transform</a>. You can use “Volume Reslice Driver” module to reslice the image along the tool axes to verify that the trajectory is feasible and safe. You may also use PathExplorer module to simulate a tool trajectory.</p>
<p>You may also find <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/PortPlacement">PortPlacement extension</a> and <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/PercutaneousApproachAnalysis">PercutaneousApproachAnalysis</a> extensions relevant. PortPlacement extension had a build error that I’ve pushed a fix for, we’ll see tomorrow if the fix worked. PercutaneousApproachAnalysis needs some updates for Python3.</p>

---
