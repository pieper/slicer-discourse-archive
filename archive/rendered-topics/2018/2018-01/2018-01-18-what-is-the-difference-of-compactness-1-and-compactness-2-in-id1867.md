---
topic_id: 1867
title: "What Is The Difference Of Compactness 1 And Compactness 2 In"
date: 2018-01-18
url: https://discourse.slicer.org/t/1867
---

# What is the difference of Compactness 1 and compactness 2 in heterogeneity CAD package? 

**Topic ID**: 1867
**Date**: 2018-01-18
**URL**: https://discourse.slicer.org/t/what-is-the-difference-of-compactness-1-and-compactness-2-in-heterogeneity-cad-package/1867

---

## Post #1 by @Teresa (2018-01-18 13:48 UTC)

<p>Operating system: Windows<br>
Slicer version: Newest version<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello.<br>
I have a question about the compactness 1 and compactness 2 parameters in the Heterogeneity CAD package for tumor segmentation.<br>
On the website it is explained;<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/HeterogeneityCAD" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/HeterogeneityCAD</a></p>
<p>•  Compactness 1: A dimensionless measure, independent of scale and orientation. Compactness 1 is defined as the ratio of volume to the (surface area)^(1.5). This is a measure of the compactness of the shape of the image ROI<br>
•  Compactness 2: a dimensionless measure, independent of scale and orientation. This is a measure of the compactness of the shape of the image ROI.</p>
<p>So what does compactness 2 really mean?</p>
<p>I’m asking this question because in a study I’m participating, In group A and group B the compactness 1 and compactness 2 showed reverse characters.<br>
(The compactness 1 was larger in group B and compactness 2 was larger in group A, which was weird for me)</p>
<p>Thanks a lot <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #2 by @JoostJM (2018-01-19 10:14 UTC)

<p>Hi Teresa,</p>
<p>What exactly do you mean by “reverse characters”?</p>
<p>I’m not entirely sure about the precise implementation in HeterogeneityCAD, but I expect it to follow the ommon definition. In that case, Compactness1 and Compactness2 are different formulas expressing the same property (they are also mathematically related. The formulas can be found here for <a href="http://pyradiomics.readthedocs.io/en/latest/features.html#radiomics.shape.RadiomicsShape.getCompactness1FeatureValue" rel="nofollow noopener">compactness1</a> and <a href="http://pyradiomics.readthedocs.io/en/latest/features.html#radiomics.shape.RadiomicsShape.getCompactness2FeatureValue" rel="nofollow noopener">compactness2</a>. These are the definitions of the features as they are implemented in PyRadiomics, which is also available in Slicer through the SlicerRadiomics extension.</p>
<p>N.B. If you want to use this extension, you’d need customization with the parameter file, as Compactness1 and 2 are disabled by default (due to the mathematical correlation to sphericity). If you need any help, please let me know.</p>
<p>Cheers,</p>
<p>Joost</p>

---

## Post #3 by @crossmanith (2018-01-19 12:09 UTC)

<p>Hi,</p>
<p>documentation and implementation seem to be inconsistent (exponent 3/2 vs. 2/3). The documentation for Compactness 1 states “(surface area)^(1.5)” but the <a href="https://github.com/vnarayan13/Slicer-OpenCAD/blob/master/HeterogeneityCAD/FeatureExtractionLib/MorphologyStatistics.py" rel="nofollow noopener">source code</a> around l. 64 shows the following calculations for compactness[1|2]:</p>
<p>def compactness1 (self, surfaceArea, volumeMM3):<br>
return ( (volumeMM3) / ((surfaceArea)**(2/3.0) * math.sqrt(math.pi)) )</p>
<p>def compactness2 (self, surfaceArea, volumeMM3):<br>
return ((36 * math.pi) * ((volumeMM3)**2)/((surfaceArea)**3))</p>
<p>Christina</p>

---

## Post #4 by @JoostJM (2018-01-19 15:18 UTC)

<p><a class="mention" href="/u/crossmanith">@crossmanith</a>, Yes, that is due to the fact that the documentation is PyRadiomics’ documentation, not heterogeneityCAD (in PyRadiomics, the <a href="https://github.com/Radiomics/pyradiomics/blob/master/radiomics/shape.py#L263" rel="nofollow noopener">Compactness1</a> function uses the exponent as defined in the documentation).</p>
<p>The reason the implementation is different in PyRadiomics is due to the fact that the reversal of the exponent in Compactness1 is a common (and rather persistent) error. If you use the function as it is defined in HeterogeneityCAD, it will NOT be dimensionless (i.e. the value will be dependent on the volume, not just the relationship between volume and surface area).</p>
<p>See also the <a href="https://arxiv.org/pdf/1612.07003.pdf" rel="nofollow noopener">IBSI feature definition document</a>, page 22.</p>
<p>Joost</p>

---

## Post #5 by @JoostJM (2018-01-19 15:31 UTC)

<p>The sphericity and compactness formulas are based on comparisons to a perfect sphere, where the surface area (A) = 4 * pi * r^2 (with r being the radius) and the volume (V) = (4/3) * pi * r^3.</p>
<p>This could be rewritten as r = (A / 4 * pi)^(1/2) and r = (V * pi * (3/4))^(1/3)</p>
<p>So, in case of a perfect sphere, you can write the correlation between A and V as<br>
A = 4 * pi * ( (V * pi * (3/4))^(1/3)) ^2 = (36 * pi * V^2) ^ (1/3)</p>
<p>This correlation (which is independent from the radius (the dimension)!) is reflected in the sphericity and compactness formulas. If you look at the formula for <a href="http://pyradiomics.readthedocs.io/en/latest/features.html#radiomics.shape.RadiomicsShape.getSphericityFeatureValue" rel="nofollow noopener">sphericity</a>, this is directly visible, and Compactness 1 and 2 can be mathematically derived from this.<br>
Therefore, they are independent of the radius of the perfect sphere, making them dimensionless…</p>
<p>Joost</p>

---

## Post #6 by @crossmanith (2018-01-19 16:02 UTC)

<p>I just wanted to make clear that Teresa is calculating something different than what she might guess from the HeterogeneityCAD documentation, which is what she quoted. The author of OpenCAD has been informed.</p>

---
