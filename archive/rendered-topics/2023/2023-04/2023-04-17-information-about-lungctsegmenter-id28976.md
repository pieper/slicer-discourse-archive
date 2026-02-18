# Information about LungCTSegmenter

**Topic ID**: 28976
**Date**: 2023-04-17
**URL**: https://discourse.slicer.org/t/information-about-lungctsegmenter/28976

---

## Post #1 by @paolo (2023-04-17 17:53 UTC)

<p>Hi everyone,</p>
<p>I’m a biomedical engineering student from Italy, this is the first time I’m using 3D Slicer.<br>
I’m writing to ask you some information about the Lung CT Analyzer and Lung CT Segmenter extensions in 3D Slicer.</p>
<p>I’d like to ask you some details about the image segmentation algorithms that are implemented in the extensions: which algorithms are used to segment the lungs (parenchyma)? Why are the markups needed?<br>
I read that airways are segmented by applying a local thrsholding algorithm; I’d like to ask<br>
which conditions are set in terms of number of pixels in the neighborhood and parameters used for the computation of the local thresholds.</p>
<p>Thank you for your support,</p>
<p>best regards,</p>
<p>Paolo</p>

---

## Post #2 by @rbumm (2023-04-17 18:28 UTC)

<p>Hello Paolo,</p>
<p>This is a two-step process in which Lung CT Segmenter produces lungs, lobe, and airway segmentation first, and in a second step the Lung Analyzer thresholds the parenchyma according to their respective Hounsfield unit ranges.<br>
The markups in Lung CT Segmenter must only be placed if you do not use one of the recently implemented AI tools. Airway segmentation uses the Segment Editor Local Threshold effect outgoing from on marker that is calculated in the center of the AI trachea segment (or, if you do not use AI, from the lastly placed manual marker).</p>
<p>The airway segmentation parameters <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/blob/2977886b1f3bd65869df50a0f8a2fa1cc2056e3e/LungCTSegmenter/LungCTSegmenter.py#L2528">are here</a>.  and use “Local threshold” and “GrowCut”. AIrway segmentation works best with thin sliced CT and tissue kernels.</p>

---

## Post #3 by @paolo (2023-04-17 18:42 UTC)

<p>Thank you!</p>
<p>So, roughly speaking, and excluding the recently implemented AI tools, lungs are segmented with a global threshold, according to their Hounsfield unit range.</p>
<p>As for the airways, they are segmented in a second step, via the 3D Slicer Segment Editor Local Threshold algorithm, and for this reason the markups are needed.</p>
<p>Is it generally correct?</p>

---

## Post #4 by @rbumm (2023-04-18 16:43 UTC)

<p>The conventional lung masks are actually generated with Slicer´s <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/blob/master/LungCTSegmenter/LungCTSegmenter.py#L1606:~:text=%23%20set%20effect-,self.segmentEditorWidget.setActiveEffectByName(%22Grow%20from%20seeds%22),-effect%20%3D%20self">Grow From Seeds</a> effect after you placed the markups in both lungs and one in the trachea.</p>

---

## Post #5 by @paolo (2023-04-18 20:24 UTC)

<p>Thanks for your reply,</p>
<p>Since I’m new in 3D Slicer but also in segmentation, I’m trying to figure out the relationships between the parameters requested in the extension and the actual segmentation algorithms that are implemented.<br>
So, hoping not to bother you, I’d like to ask the following question:<br>
if a grow from seeds algorithm is used for the lung segmentation, why do I have to set a Hounsfield Units range for the lungs? Is there any global thresholding?</p>

---

## Post #6 by @rbumm (2023-04-19 07:31 UTC)

<p>The overall goal was to segment abnormalities that are within the lungs. We wanted to create the lung masks first because everything we are interested in lies there (Lung CT Segmenter). In Lung CT Analyzer there is global thresholding within the lung regions to define emphysema, normal, infiltrated, and collapsed lung as volumetric segmentations. We included an airway analysis and the production of a vessel mask. The final goal is nodule and pattern recognition and full anatomic workup for surgical planning.</p>

---

## Post #7 by @paolo (2023-04-19 18:43 UTC)

<p>Thank you so much!</p>
<p>Paolo</p>

---
