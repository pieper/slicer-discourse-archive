# DSCMRI Analysis parameter question

**Topic ID**: 26519
**Date**: 2022-11-30
**URL**: https://discourse.slicer.org/t/dscmri-analysis-parameter-question/26519

---

## Post #1 by @mikebind (2022-11-30 19:35 UTC)

<p>We’re trying to use the DSCMRI Analysis module to calculate perfusion maps in Slicer, but are having trouble understanding some of the parameters and are getting unreasonable parameter map results.  Three questions:</p>
<ul>
<li>What is the parameter “CBV/CBV Time Interval Value”?  Perfusion processing parameter terminology   seems to vary a lot from paper to paper, and we can’t figure out what this one means.</li>
<li>Is there a sample perfusion imaging data set anyone is aware of where the parameter values are known that we can use to verify that we can get the right answers using this module and also play with to understand how the module parameters are affecting the results?</li>
<li>Is the K2 parameter output the same as the “Ktrans” parameter sometimes reported in the literature, or is it different?</li>
</ul>
<p>Thanks for any light you can shed on these questions!</p>

---

## Post #2 by @lassoan (2022-11-30 20:44 UTC)

<p>Have you checked in the source code if there is a description of thr algorithm or reference to a paper? Even if you find information on the algorithm it may still make sense to review the implementation to see exactly what is computed.</p>

---
