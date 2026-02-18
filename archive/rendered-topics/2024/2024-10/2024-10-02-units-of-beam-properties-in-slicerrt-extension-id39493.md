# Units of Beam Properties in SlicerRT extension

**Topic ID**: 39493
**Date**: 2024-10-02
**URL**: https://discourse.slicer.org/t/units-of-beam-properties-in-slicerrt-extension/39493

---

## Post #1 by @SCJohnson (2024-10-02 12:35 UTC)

<p>Good day. I would like to ask what is the unit of the Beams weight in RT slicer for proton therapy? I extracted data from the plan but the units for weight was not specified.<br>
Thank you.</p>

---

## Post #2 by @cpinter (2024-10-03 08:56 UTC)

<p>It’s a relative weight of the beams within the plan. It is taken into account when accumulating per-beam doses. A dose with a weight of 1.0 is added to the accumulated final dose as is, but with a weight of 0.5 the calculated cGy values will be halved during the summation.</p>

---
