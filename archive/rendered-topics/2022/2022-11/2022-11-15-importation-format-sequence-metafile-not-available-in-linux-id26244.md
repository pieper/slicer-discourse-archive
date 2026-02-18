# Importation format sequence metafile not available in Linux

**Topic ID**: 26244
**Date**: 2022-11-15
**URL**: https://discourse.slicer.org/t/importation-format-sequence-metafile-not-available-in-linux/26244

---

## Post #1 by @Karl-Philippe (2022-11-15 11:24 UTC)

<p>Hi,</p>
<p>I am using 3D Slicer 5.0.3 and 5.1.0 on Ubuntu 22.04 and I am trying to import a sequence metafile (tracked ultrasound sequence, like the sample data ElbowUltrasoundSweep.mha). However, unlike the Windows version (where there are the importation format choices: Volume, sequence metafile and Transform) I do not have the choice to import the .mha file as a sequence metafile. Is the sequence metafile format available in 3D slicer for Ubuntu 22.04?</p>
<p>Is this a known problem and is there an alternative solution for importing a tracked ultrasound sequence in Linux?</p>
<p>Thank you,</p>

---

## Post #2 by @lassoan (2022-11-15 12:23 UTC)

<p>Sequence metafile reader is provided by SlicerIGSIO extension (see <a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html">here</a>). Install this extension to be able to read these files.</p>

---

## Post #3 by @Karl-Philippe (2022-11-15 14:00 UTC)

<p>Thank you for your answer <a class="mention" href="/u/lassoan">@lassoan</a>!</p>

---
