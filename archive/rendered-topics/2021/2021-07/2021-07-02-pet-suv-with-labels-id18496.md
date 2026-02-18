# PET SUV with labels

**Topic ID**: 18496
**Date**: 2021-07-02
**URL**: https://discourse.slicer.org/t/pet-suv-with-labels/18496

---

## Post #1 by @Josef_Yu (2021-07-02 23:16 UTC)

<p>Hi people,</p>
<p>I was trying to figure out, how the easiest way, I can readout the SUV values (mean, max) of PET images.<br>
After segmentation, which are saved in the packaged file .mrb, I tried PET indic, but fail to choose the correct menus. I would really appreciate any help, directing me towards some manuals for this endeavour.</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2021-07-09 04:55 UTC)

<p>This message probably was not noticed because it was submitted to the “Radiomics” community. I’ve now moved to general support category.</p>
<p>Maybe <a class="mention" href="/u/pieper">@pieper</a> can help here.</p>

---

## Post #3 by @Josef_Yu (2021-07-09 06:19 UTC)

<p>I have managed to solve the issue for a while, as for my case, I draw the nodes in 3DSlicer and in the next step, before SUV quantification, I will need to click “export visible segments to binary labelmap”, after that I can use “Quantiative Indices” to manually read out raw SUV data.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72ad7a559a67890a9673815bdf5a634cb5d6a331.png" alt="export visible" data-base62-sha1="gmu6AqwB0ejfZOj7TONQtBXcI6t" width="330" height="202"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6cb472c5b33852fe351fc62f7a5a35bfb06e56f0.png" alt="quantindic" data-base62-sha1="fvEaSTpOmO1qDWhyNZGKY2P4JyM" width="385" height="336"></p>
<p>cheers</p>

---

## Post #4 by @pieper (2021-07-09 11:49 UTC)

<p>If you are still having trouble can you probably need to research the format of the PET data and any previous history of processing.  You mention they come from mrb, which would mean someone else processed the data before you in Slicer.  For the best results with you should import the dicom data with the pet plugins installed and you will generally get SUV directly (for most dicom variants).</p>

---
