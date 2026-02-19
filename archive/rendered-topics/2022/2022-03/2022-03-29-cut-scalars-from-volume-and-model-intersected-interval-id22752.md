---
topic_id: 22752
title: "Cut Scalars From Volume And Model Intersected Interval"
date: 2022-03-29
url: https://discourse.slicer.org/t/22752
---

# Cut scalars from volume and model intersected interval

**Topic ID**: 22752
**Date**: 2022-03-29
**URL**: https://discourse.slicer.org/t/cut-scalars-from-volume-and-model-intersected-interval/22752

---

## Post #1 by @keri (2022-03-29 17:29 UTC)

<p>Hi,</p>
<p>I have a volume and surface that intersets that volume. Is it possible to slice/calculate amplitudes (scalars) from volume along that instersected interval?</p>
<p>To clarify a little:<br>
There is a <code>vtkMRMLScalarVolume</code> node with scalars and <code>vtkMRMLModelNode</code>. They have intersected interval. The are two possible tasks:</p>
<ol>
<li>get the nearest/interpolated scalars from volume and set them as scalars for model;</li>
<li>set a window and at each model point and calculate some <strong>mean</strong> (median, standard deviation) value in that window. As a result I the calculated values should be displayed as model’s scalars</li>
</ol>

---

## Post #2 by @pieper (2022-03-29 21:05 UTC)

<p>Have a look at the Probe Volume With Model module.  It does your option 1, not sure about option 2.</p>

---

## Post #3 by @keri (2022-03-29 21:20 UTC)

<p>Great! that works, thank you</p>
<p>I think the second option is reacheable through <code>Simple Filters</code> module:<br>
I should be able to calculate filtered volume and after that cut amplitudes from that filtered volume.</p>
<p>The only thing is that <code>Simple Filters</code> doesn’t work yet with Scalar Volume derived nodes but I hope the <a href="https://github.com/SimpleITK/SlicerSimpleFilters/pull/24" rel="noopener nofollow ugc">PR</a> will be accepted in the future and this will greatly expand my opportunities.</p>

---
