# Unable to Load DICOM data

**Topic ID**: 13714
**Date**: 2020-09-26
**URL**: https://discourse.slicer.org/t/unable-to-load-dicom-data/13714

---

## Post #1 by @jax200 (2020-09-26 22:27 UTC)

<p>I’m a new user and trying to follow the tutorial with a 3D Slicer dataset.   I am unable to load the DICOM data in that the lower “Load” button remains grayed-out when I select “patient1”.   What is more, I have previously loaded data without issue, so this is new.  I’ve tried re-installing 3D Slicer 4.10.2 but no luck.</p>

---

## Post #2 by @lassoan (2020-09-26 22:29 UTC)

<p>DICOM loading should work well in latest Slicer Preview Release. If you still experience issues then follow instructions here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM</a></p>

---

## Post #3 by @jax200 (2020-09-26 23:49 UTC)

<p>Thank you.  Only after I selected “Examine” did it properly load.   What does that mean?</p>

---

## Post #4 by @lassoan (2020-09-27 00:07 UTC)

<p>If you enable “Advanced” mode then clicking “Examine” will provide a list of loading options (as DICOM files can be interpreted different ways and you might not want to use the default one) and then you click “Load” to load all the selected ones into the scene.</p>
<p>If you  disable “Advanced” option then the default interpretation is used, so you can directly click “Load” button.</p>
<p>In recent Slicer Preview Releases, you can also just double-click on any patient/study/series in the table to examine/load it, saving a button click.</p>

---

## Post #5 by @jax200 (2020-09-27 14:12 UTC)

<p>Got it.  Thanks for the help.</p>

---
