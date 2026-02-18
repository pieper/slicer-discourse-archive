# Sequence file type

**Topic ID**: 8417
**Date**: 2019-09-13
**URL**: https://discourse.slicer.org/t/sequence-file-type/8417

---

## Post #1 by @hnisar3 (2019-09-13 17:53 UTC)

<p>Can we save sequences (transform and/or image) as <strong>.mha</strong> file instead of .seq.nrrd or .seq.mha?</p>

---

## Post #2 by @lassoan (2019-09-13 18:09 UTC)

<p>.seq.mha file is a regular .mha file (with some additional custom fields). The .seq prefix is added to the file extension as a hint to indicate that the file contains additional metadata.</p>

---

## Post #3 by @hnisar3 (2019-09-13 20:30 UTC)

<p>I am having issues using PLUS to replay ‘Image.seq.nrrd’ and ‘Transform.seq.mha’ files.<br>
I want to replay them through PLUS to simulate hardware but I can’t. From what I could gather through forums, I supposed it was a file format issue.</p>
<p>(I played with ElbowUltrasoundSweep-Replay.xml before and could make it work)</p>

---

## Post #4 by @lassoan (2019-09-13 21:21 UTC)

<p>For hardware simulation, it is better to record in Plus (e.g., using “Plus remote” module).</p>

---
