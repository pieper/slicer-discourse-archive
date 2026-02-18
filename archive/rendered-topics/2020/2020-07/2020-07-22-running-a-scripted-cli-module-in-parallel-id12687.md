# Running a Scripted CLI Module in Parallel

**Topic ID**: 12687
**Date**: 2020-07-22
**URL**: https://discourse.slicer.org/t/running-a-scripted-cli-module-in-parallel/12687

---

## Post #1 by @vertebrae (2020-07-22 14:03 UTC)

<p>Hello,</p>
<p>I have a local threshold segmentation code in a scripted python module which iterates through fiducial points and runs the local threshold function. Iterating through points takes a while to do and to speed it up, I would like it to run in parallel with a scripted CLI python module. I have set a list of parameters, and I have this line of code:</p>
<p>slicer.cli.runSync(slicer.modules.climodulecode, None, param, True, True)</p>
<p>I am not sure what to do in terms of adding code to the scripted cli module and how to use the parameters from there. I have looked at some examples but I am still a little unclear.</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2020-07-23 01:33 UTC)

<p>2 posts were merged into an existing topic: <a href="/t/running-a-module-in-parallel/12641">Running a Module in Parallel</a></p>

---

## Post #4 by @lassoan (2020-07-23 01:33 UTC)



---
