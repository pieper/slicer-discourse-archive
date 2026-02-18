# Fractured zygoma and virtual fracture reduction

**Topic ID**: 41034
**Date**: 2025-01-11
**URL**: https://discourse.slicer.org/t/fractured-zygoma-and-virtual-fracture-reduction/41034

---

## Post #1 by @Ck1312 (2025-01-11 00:06 UTC)

<p>Hello</p>
<p>I am a new slicer user. Using CT data, I am looking for some guidance on how to effectively segment a complex zygomaticomaxillary complex fracture.</p>
<p>I then wish to virtually manipulate the respective fragments into a desired post-op position and export all fragments as one file. This file will then be 3D printed.</p>
<p>While I have seen videos on YouTube and a handful of discussions in this forum, but they haven’t really documented the process in a way that I can understand.</p>
<p>Can someone point me/guide me through the process?</p>
<p>Many thanks</p>

---

## Post #2 by @muratmaga (2025-01-11 00:34 UTC)

<p>I am not sure if this is what you are looking for but here are pointers:</p>
<ol>
<li>Assuming this is clinical data, you can use the DICOM module to import the CT scan into Slicer as a volume.</li>
<li>You can then use the Segment Editor to segment the individual bones from this volume</li>
<li>You can then use the Segmentations module to export these segments into individual 3D models.</li>
<li>You can put every segmented model under its own transform so that you can manipulate their spatial relationship independently and realign them.</li>
<li>Once you have reconfigured the fractured bones, you can “harden” transforms so transformations are fixed.</li>
<li>I am not very knowledgeable in 3D printing, but my understanding it will require a single model. If that’s really the case you can tend use MergeModels modules to stitch these individual models into a single model.</li>
<li>Export the stitched model as an STL file for printing.</li>
</ol>
<p>This the rough steps. The rest is learning to use the software. You can look at the Slicer’s official documentation at <a href="https://slicer.readthedocs.io" rel="noopener nofollow ugc">https://slicer.readthedocs.io</a></p>

---
