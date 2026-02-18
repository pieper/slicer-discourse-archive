# SlicerDMRI Tractography Display, Fiber bundle selection with custom function

**Topic ID**: 17566
**Date**: 2021-05-11
**URL**: https://discourse.slicer.org/t/slicerdmri-tractography-display-fiber-bundle-selection-with-custom-function/17566

---

## Post #1 by @simonoxen (2021-05-11 08:16 UTC)

<p>Hi, would it be possible to set up different ways of fiber bundle selection other than ROI?</p>
<p>I would be interested in using a sphere for example, simulating a simple volume of tissue activated and displaying overlapping fibers.</p>
<p>I did this locally by exposing <code>vtkExtractPolyDataGeometry* ExtractFromROI;</code> in <code>vtkMRMLFiberBundleNode.h</code> and then calling <code>fiberBundleNode.GetExtractFromROI().SetImplicitFunction()</code> with a vtkSphere.</p>
<p>Any comments, thoughts? Can give it a try making a PR if you found this feasible.</p>

---

## Post #2 by @pieper (2021-05-19 16:10 UTC)

<p>Hi <a class="mention" href="/u/simonoxen">@simonoxen</a> - yes, it makes good sense to me to generalize this.  A PR would be welcome.  Let us know if you want to discuss or make this part of a Project Week activity.</p>

---

## Post #3 by @simonoxen (2021-05-19 16:27 UTC)

<p>Great! I guess I’ll start looking into it. Project Week also works for me!</p>

---
