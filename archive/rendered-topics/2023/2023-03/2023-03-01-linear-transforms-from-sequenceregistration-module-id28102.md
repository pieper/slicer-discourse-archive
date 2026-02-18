# Linear transforms from SequenceRegistration module?

**Topic ID**: 28102
**Date**: 2023-03-01
**URL**: https://discourse.slicer.org/t/linear-transforms-from-sequenceregistration-module/28102

---

## Post #1 by @mikebind (2023-03-01 00:08 UTC)

<p>Is there a way to have the Sequence Registration module output linear transforms rather than grid transforms?  I want to rigidly register a dynamic CT image sequence (to compensate for head turning motion) and SequenceRegistration does a good job using the “rigid (all)” preset.  However, the created transforms are stored as grid transforms which are gigantic.  The saved transform sequence is &gt;21 GB (because the transforms are on a 512x512x96 grid and there are 38 frames).  This is ridiculous overkill for storing 38 4x4 linear matrices. I see that the Elastix module, but not the Sequence Registration version, has a checkbox for forcing the result to a grid transform.  I think, if I supply a linear transform node as the output transform to the Elastix module, do a rigid transformation, and keep the “force grid transform” unchecked, that I get a linear transform out of the basic Elastix model (or at least I think I was able to do this at some point in the past), but I don’t see any way to do the same trick in the Sequence Registration module. Is there something I’m missing?  Is there a way to convert a grid transform to a linear transform matrix if I know the transformation is rigid? Any other suggestions?</p>

---
