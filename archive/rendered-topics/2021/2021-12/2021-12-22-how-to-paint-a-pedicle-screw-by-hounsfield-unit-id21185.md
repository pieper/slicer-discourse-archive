# How to "paint" a pedicle screw by hounsfield unit?

**Topic ID**: 21185
**Date**: 2021-12-22
**URL**: https://discourse.slicer.org/t/how-to-paint-a-pedicle-screw-by-hounsfield-unit/21185

---

## Post #1 by @jumbojing (2021-12-22 16:05 UTC)

<p>How to “paint” a pedicle screw by hounsfield unit ?<br>
<a class="mention" href="/u/lassoan">@lassoan</a>@Juicy@jamesobutler <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a><br>
I want to “paint” a pedicle screw(a Cylinder in pedicle) by hounsfield unit , e.g. if a point in soft tissue is red ,elif in bone is blue.</p>

---

## Post #2 by @jumbojing (2021-12-22 16:23 UTC)

<p>In the <a href="https://github.com/lassoan/PedicleScrewSimulator/blob/7bf04fc00695115ac64742e692849a15e430f9dc/PedicleScrewSimulator/PedicleScrewSimulatorWizard/GradeStep.py#L281-L331" rel="noopener nofollow ugc">PedicleScrewSimulator</a> , grade the pedicle screws with the <strong>probevolumewithmodel</strong>, I don’t know if it is based on the HU value.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
<a class="mention" href="/u/ungi">@ungi</a></p>

---

## Post #3 by @lassoan (2021-12-23 17:47 UTC)

<p>Yes, Pedicle Screw Simulator extension paints the screws with the CT voxel values (in HU).</p>

---
