# SUV quantification modules and segment statistics--negative SUV values?

**Topic ID**: 11457
**Date**: 2020-05-07
**URL**: https://discourse.slicer.org/t/suv-quantification-modules-and-segment-statistics-negative-suv-values/11457

---

## Post #1 by @eap (2020-05-07 23:12 UTC)

<p>I’m trying to calculate SUVmean and SUVmax for segments I’ve created as labelmaps on my PET-CT. I’ve been running these through quantitative indices module with my PET or the SUVbw image that was automatically created through the SUVplugin (the SUVbw map and the original PET scan give the same results). I can get a SUVmean and SUVmax, but sometimes I get negative SUV values. Can someone explain to me why this is happening? How can I check the SUV calculation slicer computes?</p>
<p>I tried to manually calculate the SUVmean and SUVmax for my segments as well, using the SUVbw conversion factor calculated through the SUV factor calculator module. I figured I could use this against the segment’s pixel/voxel value in segment statistics with the PET scan as the scalar volume. What’s the difference between the Labelmap Statistics, Scalar Volume, Closed Surfaces, and PET volume statistics–they all give voxel counts, which voxel count should be used? What’s the units for “minimum uptake values” and “maximum uptake values” given? How would I have a negative value for my minimum?</p>
<p>I appreciate all patience and help–I’m new to this software and quantification.</p>

---
