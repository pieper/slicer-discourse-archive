#  register and STL model into a dental Cbct scan ?

**Topic ID**: 27429
**Date**: 2023-01-24
**URL**: https://discourse.slicer.org/t/register-and-stl-model-into-a-dental-cbct-scan/27429

---

## Post #1 by @zvifudim (2023-01-24 01:48 UTC)

<p>Can anyone help me on how to register and STL model into a dental Cbct scan ?</p>

---

## Post #2 by @lassoan (2023-01-24 01:53 UTC)

<p>The documentation and previous answers to similar questions are good starting points:</p>
<ul>
<li><a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html">Registration page in the documentation</a></li>
<li><a href="https://discourse.slicer.org/t/surface-registration-stl-model-with-cbct-data/9726" class="inline-onebox">Surface Registration (STL model with cbct data)</a></li>
<li><a href="https://discourse.slicer.org/t/surface-registration-original-stl-with-cbct-converted-to-stl/15782" class="inline-onebox">Surface Registration (original STL with cbct converted to STL )</a></li>
</ul>
<p>Let us know if it works for you or if you have any specific questions.</p>

---

## Post #3 by @cpinter (2023-01-24 13:35 UTC)

<p>Automatic surface registration didn’t work for us for the same thing because the STL contained only the intraoral scan with the crowns, the gingiva, and part of the inner wall of the mouth (by the way <a class="mention" href="/u/zvifudim">@zvifudim</a> what you don’t need can be removed in the Dynamic Modeler module using Curve Cut), and the CBCT segmentation included all the teeth etc.</p>
<p>So we decided to use fiducial registration to register the two surfaces. It can be done using Fiducial Registration, Landmark Registration, or Fiducial Registration Wizard (this is in the SlicerIGT extension and I think this one is the best).</p>

---
