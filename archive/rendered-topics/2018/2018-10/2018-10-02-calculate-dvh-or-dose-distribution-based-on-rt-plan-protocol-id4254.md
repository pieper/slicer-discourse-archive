# Calculate DVH or dose distribution based on RT plan protocol and structure set

**Topic ID**: 4254
**Date**: 2018-10-02
**URL**: https://discourse.slicer.org/t/calculate-dvh-or-dose-distribution-based-on-rt-plan-protocol-and-structure-set/4254

---

## Post #1 by @WardvanRooij (2018-10-02 11:31 UTC)

<p>Dear all,</p>
<p>For a new project I am looking for a Python integrated way to calculate the DVH or 3D dose distribution based on a radiotherapy treatment plan + structure set. Does anyone of you know if there is such a thing available? Any advice would be greatly appreciated.</p>
<p>Cheers,<br>
Ward</p>

---

## Post #2 by @cpinter (2018-10-02 12:29 UTC)

<p>Many RT evaluation tools exist in the SlicerRT extension, including DVH. If you want to calculate dose distribution based on a plan, then it is theoretically possible, but we don’t yet have a photon dose engine (we have a proton only, and plans to integrate others, but no funding for that).</p>
<p>That said all functions are accessible from python, and you can find examples in the automated tests, such as <a href="https://github.com/SlicerRt/SlicerRT/blob/master/Testing/Python/IGRTWorkflow_SelfTest.py">https://github.com/SlicerRt/SlicerRT/blob/master/Testing/Python/IGRTWorkflow_SelfTest.py</a></p>

---
