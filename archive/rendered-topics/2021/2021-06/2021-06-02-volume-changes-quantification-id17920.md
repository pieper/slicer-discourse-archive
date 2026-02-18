# Volume changes quantification

**Topic ID**: 17920
**Date**: 2021-06-02
**URL**: https://discourse.slicer.org/t/volume-changes-quantification/17920

---

## Post #1 by @CarmenG (2021-06-02 11:08 UTC)

<p>Hello! I have to superimpose two dental models in different timepoints and measure the changes that occur in a certain area. Someone knows if is there any way with this program to quantify those volume changes? It could be a percentage or any other measure.</p>
<p>Thank you all!</p>

---

## Post #2 by @lassoan (2021-06-05 00:33 UTC)

<p>You can segment the regions that you want to quantify using Segment Editor module and compute volumes using Segment Statistics module.</p>
<p>You can align images using by one of the registration methods. Probably a <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#semi-automatic-registration">semi-automatic (landmark-based) registration method</a> would be the most suitable.</p>

---
