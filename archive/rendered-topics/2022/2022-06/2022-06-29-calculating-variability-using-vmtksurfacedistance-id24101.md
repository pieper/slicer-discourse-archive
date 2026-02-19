---
topic_id: 24101
title: "Calculating Variability Using Vmtksurfacedistance"
date: 2022-06-29
url: https://discourse.slicer.org/t/24101
---

# Calculating variability using vmtksurfacedistance

**Topic ID**: 24101
**Date**: 2022-06-29
**URL**: https://discourse.slicer.org/t/calculating-variability-using-vmtksurfacedistance/24101

---

## Post #1 by @fsneden (2022-06-29 12:52 UTC)

<p>I am trying to calculate intra-observer variability in a dataset. I am creating surface data from images, and using the vmtksurfacedistance script to calculate difference from an input image (my 2nd surface) and a reference image (my 1st surface). This should give a distancearray value that will describe difference between the two.</p>
<p>Assuming this is the correct procedure, I am then trying to translate this to numpy in order to get the distancearray value. However, this doesn’t seem to work. My code (minus the specific paths and in 2 parts) is the following:</p>
<pre><code class="lang-auto">## format image for analysis
vmtkimageviewer -ifile "raw_image.ima" --pipe vmtkimagewriter -ofile "formatted_image.vti"

## segment formatted image
vmtklevelsetsegmentation -ifile "formatted_image.vti" -ofile "segmented_image.vti"

## create surface of segmented image
vmtkmarchingcubes -ifile "segmented_image.vti" -ofile "new_surface.vtp"

## calculate distance from new surface and old surface
vmtksurfacedistance -ifile "new_surface.vtp" -rfile "old_surface.vtp" -ofile "surface_distance.vtp"

</code></pre>
<p>Extraction of numerical values is performed in Jupyter notebook (see below).</p>
<pre><code class="lang-auto">## import packages
from vmtk import vmtkscripts 
import numpy as np

## read surface
surfaceReader = vmtkscripts.vmtkSurfaceReader()
surfaceReader.InputFileName = 'surface_distance.vtp'
surfaceReader.Execute()

## translate surface to numpy
surfaceNumpyAdaptor = vmtkscripts.vmtkSurfaceToNumpy()
surfaceNumpyAdaptor.Surface = surfaceReader.Surface
surfaceNumpyAdaptor.Execute()

## get dictionary output
numpySurface = surfaceNumpyAdaptor.ArrayDict
numpySurface
</code></pre>

---
