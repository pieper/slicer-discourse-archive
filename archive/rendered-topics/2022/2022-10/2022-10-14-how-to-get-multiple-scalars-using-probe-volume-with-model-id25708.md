---
topic_id: 25708
title: "How To Get Multiple Scalars Using Probe Volume With Model"
date: 2022-10-14
url: https://discourse.slicer.org/t/25708
---

# How to get multiple scalars using Probe Volume With Model?

**Topic ID**: 25708
**Date**: 2022-10-14
**URL**: https://discourse.slicer.org/t/how-to-get-multiple-scalars-using-probe-volume-with-model/25708

---

## Post #1 by @mikebind (2022-10-14 16:52 UTC)

<p>I’ve started using Probe Volume With Model to view values from image volumes displayed on a surface model.  I know from seeing some other use cases for scalars associated with models that a single model can have multiple scalar overlays, and that you can choose between them using the “Active Scalar” dropdown in the Models module Display–&gt;Scalars section. So, I expected that I could probe different registered volumes with the same model and store each as separate scalars in the model, but this isn’t working as expected.  The Probe Volume With Model interface allows you to choose a name for the scalar array, and that name shows up as a selectable option to display one the probing is executed, but any prior existing scalar array seems to be removed.</p>
<p>Steps to reproduce:</p>
<ol>
<li>Probe volume1 with model1 as both the input and output model, and with scalar1 as the output array name. (After this, scalar1 is displayable on the model)</li>
<li>Probe volume2 with model1 as both the input and output model, and with scalar2 as the output array name.</li>
</ol>
<p>After step 2, scalar2 is displayable on the model, but scalar1 is gone and is no longer an option to display.  Is this the expected behavior?  Is there a different way to achieve this, where both scalar1 and scalar2 are options to be displayed?</p>
<p>I realize a workaround could be to duplicate model1 and just have one scalar on each model, but it seems like this shouldn’t be necessary because models can support multiple scalars.</p>

---

## Post #2 by @pieper (2022-10-14 20:38 UTC)

<p>Good point.  I think that’s just a limitation of the module.  <a href="https://github.com/Slicer/Slicer/blob/main/Modules/CLI/ProbeVolumeWithModel/ProbeVolumeWithModel.cxx">The code</a> is not super complex, and probably it’s just a matter of figuring out the options for <a href="https://vtk.org/doc/nightly/html/classvtkProbeFilter.html"><code>vtkProbeFilter</code></a>.</p>

---

## Post #3 by @mikebind (2022-10-18 04:30 UTC)

<p>OK, I’ll try to dig into the code a bit.  I was hoping there was just something I was missing…  Thanks for taking a look <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #4 by @lassoan (2022-10-19 05:46 UTC)

<p>Probably it is enough to call <code>Pass*ArraysOn()</code>. I don’t see any particular drawback of preserving the previous arrays, and I can see that it can be useful, so it should be fine to enable it.</p>

---
