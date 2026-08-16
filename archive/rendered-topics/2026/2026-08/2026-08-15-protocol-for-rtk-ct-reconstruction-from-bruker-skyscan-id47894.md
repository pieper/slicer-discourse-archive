---
topic_id: 47894
title: "Protocol for RTK CT Reconstruction from Bruker Skyscan?"
date: 2026-08-15
url: https://discourse.slicer.org/t/47894
last_bumped: 2026-08-15T23:51:55.624Z
---

# Protocol for RTK CT Reconstruction from Bruker Skyscan?

**Topic ID**: 47894
**Date**: 2026-08-15
**URL**: https://discourse.slicer.org/t/protocol-for-rtk-ct-reconstruction-from-bruker-skyscan/47894

---

## Post #1 by @raranda22 (2026-08-15 22:35 UTC)

<p>Hello, I’m wondering if anyone would be willing to share instructions on how to use RTK for CT reconstructions, assuming output from Bruker Skyscan (CT scanner)? I have access to Morphocloud, so I’m able to use GPU and/or CUDA for speed optimizations. Also, about half of my scans are oversize, so they’re composed of two subscans.</p>

---

## Post #2 by @muratmaga (2026-08-15 23:51 UTC)

<p>I don’t have any experience with RTK. I did ask claude if this is possible, and here is the respond. As it suggest, i think you need to decide why you are doing this since RTK will be subpar to Nrecon:</p>
<pre><code class="lang-auto">RTK doesn't have a Bruker importer, but Skyscan is a standard circular cone-beam geometry so you can build everything from the acquisition log (the .log written at scan time, not the NRecon recon log). The pieces you need from it: Object to Source (mm) → SID, Camera to Source (mm) → SDD, Rotation Step and number of projections → arc, and Camera Pixel Size / binning → detector spacing.

Install. pip install itk-rtk-cuda116 (the CUDA wheels; plain itk-rtk is CPU-only). On MorphoCloud instances the driver is new enough for the cu116 wheels.
Geometry. rtksimulatedgeometry -n &lt;nproj&gt; --sid &lt;ObjToSource&gt; --sdd &lt;CamToSource&gt; --arc &lt;nproj × rotation_step&gt; -o geometry.xml. If the scan is 180°+fan rather than 360°, set arc accordingly. Sign conventions are documented in Simon Rit's geometry PDF linked from the RTK docs.
Projections. The projection TIFFs are transmission images, so they need conversion to line integrals (−ln(I/I0)) with flat/dark correction before FDK. If your acquisition had flat-field correction ON, a constant I0 (near-saturation value from an air region) is usually adequate; otherwise apply your bright/dark references first. Easiest is a short Python preprocessing script that writes float32 attenuation projections into a single stack.
Alignment. NRecon's "post-alignment" value (rotation axis offset in pixels) maps to RTK's projOffsetX (in mm, offset × detector pixel size). Getting this wrong gives you the classic tuning-fork/double-edge artifact, so do a quick single-slice recon and sweep the offset if needed.
Reconstruct. rtkfdk -p . -r 'proj.*tif' -g geometry.xml -o vol.mha --hardware cuda --spacing &lt;voxel&gt; --size &lt;dims&gt;. Use --lowmem if the projection stack is large.
Oversized scans. Treat each subscan as an independent acquisition: reconstruct each one separately, then stitch the two volumes along z using the vertical stage offset recorded in the log (there's overlap between subscans; crop or feather in the overlap region). That's simpler and more robust than trying to encode both subscans into one RTK geometry.

One honest caveat: a bare RTK FDK won't include NRecon's beam-hardening, ring-artifact, and defect-pixel corrections, so expect somewhat different image quality unless you add those steps yourself (ring reduction can be done in projection space before FDK). If your goal is just GPU speed and batch processing rather than escaping NRecon specifically, it's worth saying what's driving the RTK requirement — there may be a shorter path.
</code></pre>

---
