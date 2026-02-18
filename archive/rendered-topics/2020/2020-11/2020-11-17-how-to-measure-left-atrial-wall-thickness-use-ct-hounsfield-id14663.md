# How to measure left atrial wall thickness use CT Hounsfield Units

**Topic ID**: 14663
**Date**: 2020-11-17
**URL**: https://discourse.slicer.org/t/how-to-measure-left-atrial-wall-thickness-use-ct-hounsfield-units/14663

---

## Post #1 by @caiwei (2020-11-17 15:06 UTC)

<p>I would like to know whether it is possible to use 3D Slicer to accurately measure the left atrial wall(myocardial) thickness which excludes the fat tissue use CT Hounsfield Units. The concrete method is showed in the below picture from MJ Mulder’s paper("*m<a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7334811/" rel="noopener nofollow ugc">pact of local left atrial wall thickness on the incidence of acute pulmonary vein reconnection after Ablation Index-guided atrial fibrillation ablation")。</a><br>
Are there any existing extensions to do so? OR is there a need to use the programming language to achieve this?<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f6e02e0bc4b626e434e55dfd5ed8216d63861b3.jpeg" alt="tileshop" data-base62-sha1="dCd3zLmYln6ByHCtxX8Qr2Iia3x" width="256" height="256"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2e63fd26e6b9359a3a23b070c67ff1d02b17176.jpeg" alt="tilesh (1)" data-base62-sha1="yEMQZv2VxL0PxrNsqoUCclJdj5I" width="283" height="415"></p>

---

## Post #2 by @lassoan (2020-11-19 03:21 UTC)

<p>You can get a line profile using “Line profile” module (provided by “Sandbox” extension). It is a Python scripted module, so you can quite easily extend it to compute the thickness fully automatically from the line profile.</p>
<p>I also believe that you can do much better than what they did in the paper: instead of doing a few manual measurements, you can measure min/max/average thickness in whole regions, but segmenting the blood pool and the myocardium (using Segment Editor module) and measure the distance between these surfaces (using Model to Model distance module).</p>

---
