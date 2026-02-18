# Create cylinder from central coordinates

**Topic ID**: 11206
**Date**: 2020-04-20
**URL**: https://discourse.slicer.org/t/create-cylinder-from-central-coordinates/11206

---

## Post #1 by @Matt_B (2020-04-20 14:39 UTC)

<p>Hi,</p>
<p>I was wondering if it was possible to (programatically) create a curved cylinder segment from a list of coordinates which run along its centre?<br>
This generated segement/mesh would then be subtracted from another to create a new one with these cylindrical tracks removed (with the ultimate aim of converting this back to a DICOM Structure file as well as for 3D printing).</p>
<p>Thanks,</p>

---

## Post #2 by @lassoan (2020-04-20 15:15 UTC)

<p>This is implemented in “Draw Tube” effect in Segment Editor (provided by SegmentEditorExtraEffects extension.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f94b4d04eed8371ab04a3cfdc05935acb6dd39ac.jpeg" data-download-href="/uploads/short-url/zzmdJnz8XbVur7Dpijujccge5gE.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f94b4d04eed8371ab04a3cfdc05935acb6dd39ac_2_690x419.jpeg" alt="image" data-base62-sha1="zzmdJnz8XbVur7Dpijujccge5gE" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f94b4d04eed8371ab04a3cfdc05935acb6dd39ac_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f94b4d04eed8371ab04a3cfdc05935acb6dd39ac_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f94b4d04eed8371ab04a3cfdc05935acb6dd39ac_2_1380x838.jpeg 2x" data-dominant-color="B5B8B8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1370 572 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If you want to use this for HDR brachytherapy catheter segmentation there are a couple of extensions you might find relevant: <a href="https://github.com/SlicerIGT/SlicerPathReconstruction">PathReconstruction extension</a> can create catheter paths from electromagnetically tracked position sensor; <a href="http://www.slicerigt.org/">SlicerIGT extension</a> can reconstruct volumes from tracked ultrasound (so that you can draw catheters in ultrasound).</p>
<p>You can find examples of how to use Segment Editor using Python scripting instead of GUI in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">script repository</a>, which may be useful if you want to import curve point positions from an external source.</p>

---
