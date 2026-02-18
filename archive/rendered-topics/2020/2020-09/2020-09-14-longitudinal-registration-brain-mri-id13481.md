# Longitudinal registration brain MRI

**Topic ID**: 13481
**Date**: 2020-09-14
**URL**: https://discourse.slicer.org/t/longitudinal-registration-brain-mri/13481

---

## Post #1 by @Marianne (2020-09-14 12:28 UTC)

<p>What is the best way to compare segments from MRIs with different geometry (individual scans of the same subject)? Do I have to register all the MRIs in order to compare the segments to each other? What is the easiest way to do this? I have not had luck with affine or landmark registration, there is no change “sticking” to the output volume when I change module…</p>
<p>Context: I have a set of MRI-images with corresponding manual and machine-learning-derived tumor segments, shoving longitudinal tumor developments. I want to register all the MRIs to the first MRI, so the geometry of the segments can be compared in respekt of visualization of growth, as well as dice-coefficient between manual and machine-derived, longitudinally.</p>

---
