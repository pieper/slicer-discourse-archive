---
topic_id: 10232
title: "Nrrd Scale Factor"
date: 2020-02-13
url: https://discourse.slicer.org/t/10232
---

# NRRD scale factor

**Topic ID**: 10232
**Date**: 2020-02-13
**URL**: https://discourse.slicer.org/t/nrrd-scale-factor/10232

---

## Post #1 by @Hamburgerfinger (2020-02-13 01:51 UTC)

<p>I’ve used RawImageGuess module to guess the format of some images and I’d like to use the ‘Generate nrrd header’ function to create a header template and convert them all to *.nrrd with a script.</p>
<p>How can I include a scale factor in the nrrd header?</p>

---

## Post #2 by @muratmaga (2020-02-13 05:49 UTC)

<p>By scale factor, do you mean the voxel spacing?</p>
<p>If so, you should have specified that at the time of header creation (fields called X_Spacing, Y_Spacing, Z_Spacing). Alternatively you can edit the image spacing field of the imported NRRD file in Volumes module, and resave the data.</p>

---

## Post #3 by @Hamburgerfinger (2020-02-13 06:08 UTC)

<p>Ah sorry I mean a scalar which the raw image intensities (mine are integers) are multiplied by to give a real-world value (mine is activity concentration in Bq/mL) – in other words like the rescale slope in DICOM format.  Is there an equivalent in the NRRD format that Slicer recognizes?</p>

---

## Post #4 by @lassoan (2020-02-13 06:31 UTC)

<p>There is no intensity scaling information in NRRD format. You could add private fields that your software would recognize, but if you want to follow the standard and be compatible with more software then probably your best bet is to store the real-world values (as floating-point values).</p>

---
