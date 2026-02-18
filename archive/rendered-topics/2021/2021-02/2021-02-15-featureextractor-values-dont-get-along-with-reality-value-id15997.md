# FeatureExtractor values don't get along with reality value

**Topic ID**: 15997
**Date**: 2021-02-15
**URL**: https://discourse.slicer.org/t/featureextractor-values-dont-get-along-with-reality-value/15997

---

## Post #1 by @11117 (2021-02-15 15:54 UTC)

<p>Hello everyone,</p>
<p>I’m trying to understand my results that I get from pyradiomics - FeatureExtractor and I have two questions:</p>
<ol>
<li>
<p>I want to understand what values the extractor gets me, so I calculate manually the energy, max, min in the ROI to compare the results with pyradomics results. I didn’t get the same values. I checked this on the example in radiomics (brain) (with one label)<br>
my method - I upload the mask and the image to an float array with nrrd.read() and did manually calculate…for exp.- max(image[mask == 1])<br>
anyone can explain me why I don’t get the same values?</p>
</li>
<li>
<p>what the different between seg Extract to voxel Extract?<br>
how can I analyse the voxel Extract?</p>
</li>
</ol>

---

## Post #2 by @JoostJM (2021-03-09 12:22 UTC)

<p>Dubplicate to <a href="https://discourse.slicer.org/t/help-in-deep-understanding-pyradiommics/16269" class="inline-onebox">Help in deep understanding pyRadiommics</a></p>

---

## Post #3 by @JoostJM (2021-03-09 12:22 UTC)



---
