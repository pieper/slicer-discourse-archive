---
topic_id: 24135
title: "Vmtk Vesselness Filtering Select Seedpoint In Python"
date: 2022-07-01
url: https://discourse.slicer.org/t/24135
---

# Vmtk Vesselness Filtering: select seedpoint in Python

**Topic ID**: 24135
**Date**: 2022-07-01
**URL**: https://discourse.slicer.org/t/vmtk-vesselness-filtering-select-seedpoint-in-python/24135

---

## Post #1 by @KateDelb (2022-07-01 09:31 UTC)

<p>Hey!</p>
<p>I’m using the VMTK VesselnessFilter to find my vessels in a T1ce image. I did this manually in 3DSlicer with no issues.<br>
However, I’m seeing that I get better results when I select a seedpoint to determine the min/max vessel diameter.</p>
<p>Now I’d like to implement the same process in python/JupyterNotebooks.<br>
I have a working piece of code that finds the vesselness, but can’t seem to figure out how to manually add a seedpoint.<br>
Here is the code:</p>
<blockquote>
<p><strong><span class="hashtag-raw">#Push</span> input volume to node</strong><br>
InputVolumeNode = su.PushVolumeToSlicer(t1ce_brain)</p>
<p>dim_in = t1ce_brain.GetSize()<br>
spacing_in = t1ce_brain.GetSpacing()</p>
<p><strong><span class="hashtag-raw">#Create</span> output volume with same dim and spacing of InputVolume</strong><br>
OutputNode = createEmptyVolume(dim_in, spacing_in, ‘VesselnessFiltered’)  # invoke function</p>
<p><strong><span class="hashtag-raw">#create</span> vesselness filtering logic</strong><br>
vfl = VesselnessFiltering.VesselnessFilteringLogic()<br>
<strong><span class="hashtag-raw">#Select</span> seed to determine min/max vessel diameter</strong><br>
<span class="hashtag-raw">#TODO</span><br>
<strong><span class="hashtag-raw">#compute</span> VesselnessFiltering</strong><br>
vfl.computeVesselnessVolume(InputVolumeNode, OutputNode, minimumDiameterMm=1, maximumDiameterMm=6, alpha=0.3, beta=0.3, contrastMeasure=130)</p>
</blockquote>
<p>I can see that I can set the minimum/maximumDiameter inside the computeVesselnessVolume function, but I’m not sure how to find these automatically by setting a seedpoint (Fiducials.</p>
<p>I was looking through <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/VesselnessFiltering/VesselnessFiltering.py" class="inline-onebox" rel="noopener nofollow ugc">SlicerExtension-VMTK/VesselnessFiltering/VesselnessFiltering.py at master · vmtk/SlicerExtension-VMTK · GitHub</a> for hints, but this seems to be the code to select this point within the GUI node.<br>
using</p>
<blockquote>
<p><strong><span class="hashtag-raw">#Select</span> seed to determine min/max vessel diameter</strong><br>
vfl.seedFiducialsNodeSelector((x,y,z))</p>
</blockquote>
<p>gives the error</p>
<blockquote>
<p>AttributeError: ‘VesselnessFilteringLogic’ object has no attribute ‘seedFiducialsNodeSelector’</p>
</blockquote>
<p>so I’m clearly not on the right path. How can I select this seedpoint in python?</p>
<p>Thanks for any help!</p>

---

## Post #2 by @lassoan (2022-07-03 01:51 UTC)

<p>You can probably use the same minimum and maximum diameters and contrast difference and other filtering parameters for similar images. So, you can determine the optimal parameters by using the module GUI and then use them in your Python scripts.</p>

---
