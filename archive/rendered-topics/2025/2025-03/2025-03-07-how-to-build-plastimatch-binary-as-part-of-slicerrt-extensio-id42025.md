# How to build plastimatch binary as part of SlicerRT extension?

**Topic ID**: 42025
**Date**: 2025-03-07
**URL**: https://discourse.slicer.org/t/how-to-build-plastimatch-binary-as-part-of-slicerrt-extension/42025

---

## Post #1 by @fedorov (2025-03-07 22:25 UTC)

<p>I understand Plastimatch library is a dependency of SlicerRT, and I would like to build the command-line plastimatch binary as part of the superbuild. Is this possible? I can’t figure out how to enable it via cmake… I thought this was possible in the earlier versions of this extension.</p>

---

## Post #2 by @lassoan (2025-03-08 00:53 UTC)

<p>Several command-line tools of Plastimatch are build as part of SlicerRT (PlmBspline, PlmDrr, PlmLandwarp, PlmMismatchError, PlmProtonDoseEngine, PlmRegister, PlmSynth, PlmThreshbox, PlmVectorFieldAnalysis). Is there a specific binary that you would like to use and not included already?</p>

---

## Post #3 by @fedorov (2025-03-08 00:58 UTC)

<p>I was looking for <code>plastimatch convert</code>, as documented here: <a href="https://plastimatch.org/plastimatch.html#plastimatch-convert" class="inline-onebox">plastimatch — Plastimatch 1.10.0 documentation</a>.</p>

---

## Post #4 by @cpinter (2025-03-10 10:56 UTC)

<p>Plastimatch is <a href="https://github.com/SlicerRt/SlicerRT/issues/39">statically built into SlicerRT</a>, so executables and DLLs are not generated, only as part of the SlicerRT DLLs. I think you’ll need to build Plastimatch separately to get those.</p>

---

## Post #5 by @fedorov (2025-03-10 14:17 UTC)

<p>Thanks for the quick reply!</p>
<p>I was looking for a command line tool to convert RTSTRUCT into raster volume, and Plastimatch convert was my first choice. Unfortunately, it is no longer installable with Linux package manager, there is no linux or mac binary provided, and I could not find the “official” docker image. I next tried to compile it myself from source, but ran into C++17 standard errors. Since I am able to compile SlicerRT, and I know it is used there, that was my next choice.</p>
<p>I ended up using Platipy and specifically this function: <a href="https://github.com/pyplati/platipy/blob/master/platipy/dicom/io/rtstruct_to_nifti.py#L220" class="inline-onebox">platipy/platipy/dicom/io/rtstruct_to_nifti.py at master · pyplati/platipy · GitHub</a>.  I don’t know how robust it is, but it seems to work for the contours I needed to process.</p>

---
