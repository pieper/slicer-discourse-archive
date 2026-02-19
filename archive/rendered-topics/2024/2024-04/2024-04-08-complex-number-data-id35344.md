---
topic_id: 35344
title: "Complex Number Data"
date: 2024-04-08
url: https://discourse.slicer.org/t/35344
---

# Complex-number data

**Topic ID**: 35344
**Date**: 2024-04-08
**URL**: https://discourse.slicer.org/t/complex-number-data/35344

---

## Post #1 by @gabuzi (2024-04-08 02:44 UTC)

<p>Hi,</p>
<p>I’m looking into building a python extension for slicer to visualize our MRI data. I realized that there doesn’t seem to be a straightforward way of getting time series of complex data (real&amp;imaginary or magnitude&amp;phase) in a slicer sequence.</p>
<p>I can manage fine to manually load my custom data format into a slicer sequence, but only get the real part.</p>
<p>Are complex numbers at all supported? It seems like VTK has no problem creating 2-component images, but Slicer seems to reserve images with &gt; 1 components for VectorVolumes, and then requires them to have 3 components (I assume to interpret them as xyz spatial vector components). At least that’s my guess from seeing a lot of errors like " [VTK] Input has too few components" and “[VTK] Execute: Component 2 is not in input.” errors when creating a sequence of 2-component VectorVolumeNodes.</p>
<p>What are the recommendations for working with complex data? I’d like to avoid splitting into separate volumes/sequences, because complex data must remain synchronized.</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2024-04-08 21:12 UTC)

<p>There’s no built-in complex data type for volumes currently.  If you’re just doing a few cases, the most straightforward thing I’d suggest just loading the real and imaginary parts as two volumes, and then implementing any calculations using numpy.  You can group the volume using folders or sequences.</p>
<p>On the other hand if you wanted to dig deeper, then implementing a specific class like a <code>vtkMRMLComplexVolumeNode</code> and associated classes wouldn’t be that hard, and would make it clear where to put the save/load, visualization, GUI, and other code specific to that data and be consistent with the overall Slicer architecture.</p>
<p>What’s your clinical application?</p>

---

## Post #3 by @gabuzi (2024-04-09 17:19 UTC)

<p>I see, thanks for confirming!</p>
<p>My use case is quantitative MRI sequence development and data modelling from raw data (very far away from clinical routine). Generally, we have series of 3D complex images and I had hoped to utilize slicer for data inspection. Most home-cooked tools rely on sluggish matlab or matplotlib code, which I hope to avoid.</p>
<p>For now, I built a small extension where I just store the complex raw data series as numpy arrays and on-demand create volumes for viewing. It works quite alright, but requires me to handle the GUI bits for the appropriate complex → real transformation as part of the extension, rather than a built-in function.</p>
<p>I guess this is akin to the sequence browser where a proxy-node is updated on-demand (but I don’t actually know how the sequence browser is implemented).</p>

---
