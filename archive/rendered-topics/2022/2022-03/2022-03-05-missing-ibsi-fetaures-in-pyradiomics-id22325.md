# Missing IBSI fetaures in Pyradiomics.

**Topic ID**: 22325
**Date**: 2022-03-05
**URL**: https://discourse.slicer.org/t/missing-ibsi-fetaures-in-pyradiomics/22325

---

## Post #1 by @JonasB (2022-03-05 14:28 UTC)

<p>Dear Community.</p>
<p>I noticed some Issues with missing features from the IBSI recommendation in Pyradiomics.<br>
I went through the feature definitions and compared them (IBSI: <a href="https://pubs.rsna.org/doi/full/10.1148/radiol.2020191145" rel="noopener nofollow ugc">https://pubs.rsna.org/doi/full/10.1148/radiol.2020191145</a>, Pyradiomics: <a href="https://pyradiomics.readthedocs.io/" rel="noopener nofollow ugc">https://pyradiomics.readthedocs.io/</a>).<br>
Some features like Compactness 1 &amp; 2, Asphericity, Sum variance, Dissimilarity, etc. are equal or highly correlated to other features. I think it makes sense to exclude those.<br>
But I detected a bunch of missing features that are included in the IBSI feature definition but not in Pyradiomics.</p>
<p>I was wondering if there is any justification I am missing or if it is possible to include those into the feature set?:<br>
<strong>Intensity-based statistical features:</strong><br>
Intensity-based median absolute deviation<br>
Intensity-based coefficient of variation<br>
Intensity-based quartile coefficient of dispersion<br>
<strong>Morphological features</strong><br>
Centre of mass shift<br>
Volume density (axis-aligned bounding box)<br>
Volume density (oriented minimum bounding box)<br>
Area density (oriented minimum bounding box)<br>
Volume density (approximate enclosing ellipsoid)<br>
Area density (approximate enclosing ellipsoid)<br>
Volume density (minimum volume enclosing ellipsoid)<br>
Area density (minimum volume enclosing ellipsoid)<br>
Volume density (convex hull)<br>
Area density (convex hull)<br>
Integrated intensity<br>
Moran’s index<br>
Geary’s C measure<br>
<strong>Local intensity features</strong><br>
Local intensity peak<br>
Global intensity peak<br>
<strong>Intensity histogram features</strong><br>
Intensity histogram mode<br>
Intensity histogram mean absolute deviation<br>
Intensity histogram robust mean absolute deviation<br>
Intensity histogram median absolute deviation<br>
Intensity histogram coefficient of variation<br>
Intensity histogram quartile coefficient of dispersion<br>
Minimum histogram gradient<br>
Minimum histogram gradient intensity<br>
<strong>Intensity-volume histogram features</strong><br>
Volume at intensity fraction<br>
Intensity at volume fraction<br>
Volume fraction difference between intensity fractions<br>
Area under the IVH curve</p>
<p>Hope for help.<br>
Thank you in advance.</p>
<p>Best,<br>
Jonas</p>

---

## Post #2 by @pieper (2022-03-05 16:12 UTC)

<p>Funding and active development of pyradiomics finished a few years ago and the developers included what they felt to be the most important features with the resources available.  If someone is motivated to implement additional features (and documentation and tests) it should be possible to expand the list.</p>

---
