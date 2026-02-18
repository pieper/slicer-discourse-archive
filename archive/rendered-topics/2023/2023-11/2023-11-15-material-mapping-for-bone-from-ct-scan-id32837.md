# Material mapping for bone from CT scan

**Topic ID**: 32837
**Date**: 2023-11-15
**URL**: https://discourse.slicer.org/t/material-mapping-for-bone-from-ct-scan/32837

---

## Post #1 by @ElaniaDiBart (2023-11-15 12:27 UTC)

<p>Hi all,</p>
<p>I’m attempting material mapping for mechanical properties in bones. I’ve previously achieved this in MITK-Gen by correlating Hounsfield Units (HS units) with bone density, followed by computing the elastic modulus. Now, I’d like to replicate a similar process in 3D Slicer.</p>
<p>I segmented a femur from a CT scan, meshed it using the Segment Mesher extension, utilized probe volume with a model for mapping, and employed segment statistics to compute the minimum, maximum, and mean values of HS units.</p>
<p>How can I proceed to obtain material mapping or bone density and apply the same equation or a similar method as in the MITK-Gen process? Does anyone have any ideas?</p>

---

## Post #2 by @pieper (2023-11-15 12:56 UTC)

<p>There’s a lot of literature on this, but I don’t think there’s a Slicer extension that puts everything together like MITK-Gem does.  From what I’ve seen, usually there’s a pretty simple formula used to map Houndfield units to material properties, and it sounds like you have all the pieces needed to perform the mapping.  Since CT doesn’t tell you everything you need to know about mechanics, you’ll need to feed in external variables that depend on the exact physical system you are trying to model.  Best would be to correlate your simulations with some kind of physical experiments to calibrate.</p>

---

## Post #3 by @ElaniaDiBart (2023-11-16 05:43 UTC)

<p>Thank you for replying.<br>
Since I know all the equations that I need to go from HU to obtain the elastic modulus, my question is how can I export/visualize/obtain more useful information from the model created by “probe volume with model”.<br>
I think <a class="mention" href="/u/lassoan">@lassoan</a> mention this function in order to not use BoneMat for material mapping… if you can please give more details about it.</p>
<p>Thank you!</p>

---

## Post #4 by @pieper (2023-11-16 14:59 UTC)

<p>When you use the Probe Volume with Model feature you will get a scalar field on the vertices with the HU value sampled from the volume.  You can visualize it using options in the Models module.  You can get this data as a numpy array with <code>slicer.util.arrayFromModelPointData()</code>.  How you make use of it depends on how you export the mesh to your analysis package.</p>

---
