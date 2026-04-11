---
topic_id: 46707
title: "Slicerseqseg Extension"
date: 2026-04-10
url: https://discourse.slicer.org/t/46707
---

# SlicerSeqSeg Extension

**Topic ID**: 46707
**Date**: 2026-04-10
**URL**: https://discourse.slicer.org/t/slicerseqseg-extension/46707

---

## Post #1 by @numisveinsson (2026-04-10 17:29 UTC)

<p>Hi everyone,</p>
<p>I’m sharing <strong>SeqSeg</strong>, a new <strong>3D Slicer extension</strong> for <strong>seed-based segmentation of tubular/vascular structures</strong> from CT or MR. You place <strong>two fiducial seeds</strong> and a <strong>radius estimate</strong>; the module runs the <strong>SeqSeg</strong> pipeline (with <strong>nnUNet</strong>) and loads the segmentation (and optional surface mesh) back into Slicer. Pretrained weights can be pulled from Zenodo via a button in the module UI.</p>
<ul>
<li>
<p><strong>Source / documentation:</strong> <a href="https://github.com/numisveinsson/SlicerSeqSeg" rel="noopener nofollow ugc">https://github.com/numisveinsson/SlicerSeqSeg</a></p>
</li>
<li>
<p><strong>Underlying method (Python package):</strong> <a href="https://github.com/numisveinsson/SeqSeg" rel="noopener nofollow ugc">https://github.com/numisveinsson/SeqSeg</a></p>
</li>
</ul>
<p><strong>Publication</strong></p>
<p>Sveinsson Cepero, N., Shadden, S.C. <em>SeqSeg: Learning Local Segments for Automatic Vascular Model Construction.</em> Ann Biomed Eng <strong>53</strong>, 158–179 (2025). <a href="https://doi.org/10.1007/s10439-024-03611-z" rel="noopener nofollow ugc">https://doi.org/10.1007/s10439-024-03611-z</a></p>
<p>I’m planning to submit the extension to the <strong>Slicer Extensions Index</strong> so it can be installed from the Extension Manager; until then it can be used by adding the module path or building from source as usual.</p>
<p>Feedback, bug reports, and collaboration ideas are welcome—either here or on GitHub issues.</p>
<p>Thanks,<br>
Numi</p>

---
