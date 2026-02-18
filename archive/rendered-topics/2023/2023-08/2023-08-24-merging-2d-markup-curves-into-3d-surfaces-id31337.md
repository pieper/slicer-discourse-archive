# Merging 2D markup curves into 3D surfaces

**Topic ID**: 31337
**Date**: 2023-08-24
**URL**: https://discourse.slicer.org/t/merging-2d-markup-curves-into-3d-surfaces/31337

---

## Post #1 by @Emanuel_Tschopp (2023-08-24 15:00 UTC)

<p>I need to measure distances between growth lines in teeth.<br>
Because the CT-scan is not perfectly aligned to the longitudinal axis of the teeth, I wondered if it was possible to first use the Markup tool to mark individual growth lines in different views, and then use the MergeMarkups tool to merge the single 2D curves into 3D surfaces, and then finally measure the distances between the surfaces.<br>
Is that possible, or something that could be implemented?<br>
Or does somebody have another solution for my problem?<br>
Resampling to align the axes is not a very good solution because sometimes I have ultiple teeth in a single CT-scan, so I would have to realing every single tooth, and because the downsampling adds noise, which is already at critical levels to distinguish single growth lines.<br>
Thanks a lot in advance!<br>
Emanuel</p>

---

## Post #2 by @muratmaga (2023-08-24 16:12 UTC)

<p>What you describe <strong>might</strong> be possible with MarkupsToModel or SurfaceMarkup extension, but I am not sure. It also sounds too tedious.</p>
<p>Reorienting the data does not cause downsampling. It may cause some blurring due to interpolation, but should be fairly low if your original data is sufficiently high resolution and isotropic. You can crop individual tooth from the same scan, and turn them into separate volumes and then align them independently in whichever way you want.</p>

---
