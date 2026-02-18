# Cannot obtain the center line.

**Topic ID**: 18112
**Date**: 2021-06-14
**URL**: https://discourse.slicer.org/t/cannot-obtain-the-center-line/18112

---

## Post #1 by @zhang-qiang-github (2021-06-14 13:27 UTC)

<p>I have two arteries, like:</p>
<p>                    <a href="https://user-images.githubusercontent.com/29271051/121808984-94924100-cc8d-11eb-8738-6c624480890d.png" target="_blank" rel="noopener nofollow ugc" class="onebox">
            <img src="https://user-images.githubusercontent.com/29271051/121808984-94924100-cc8d-11eb-8738-6c624480890d.png" width="278" height="500">
          </a>

</p>
<p>I can obtain the centerline for one artery, but fail for the other one. It failed to obtain the centerline between the two red point.</p>
<p>The running code is:</p>
<pre><code class="lang-auto">vmtksurfacereader -ifile E:\\DeepCenterLine\\vessel_smooth30.vtp --pipe vmtkcenterlines --pipe vmtkrenderer --pipe vmtksurfaceviewer -opacity 0.25 --pipe vmtksurfaceviewer -i @vmtkcenterlines.o -array MaximumInscribedSphereRadius
</code></pre>
<p>I have updated the <code>vessel_smooth30.vtp</code> to <a href="https://github.com/zhang-qiang-github/vmtkdata" rel="noopener nofollow ugc">github</a>.</p>
<p>Actually, I run it using python code, and a warning is reported:</p>
<pre><code class="lang-auto">vtkvmtkSteepestDescentLineTracer: can't find a steepest descent edget. Target not reached.
</code></pre>
<p>The source point is: [44, 398, 151], and the target point is: [47, 403, 558]</p>
<p>How to obtain the center line from [44, 398, 151] to [47, 403, 558].</p>

---

## Post #2 by @lassoan (2021-09-07 19:11 UTC)

<p>I would recommend to try the Extract Centerline script in 3D Slicer’s SlicerVMTK extension. If that does not work then let us know (I could not try, as the link was not valid anymore).</p>

---
