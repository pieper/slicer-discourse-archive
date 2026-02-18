# How to generate RAS bounding box possible to adjust by users 

**Topic ID**: 42947
**Date**: 2025-05-15
**URL**: https://discourse.slicer.org/t/how-to-generate-ras-bounding-box-possible-to-adjust-by-users/42947

---

## Post #1 by @xwan (2025-05-15 15:05 UTC)

<p>I’m working on an extension to generate a bounding box based on 6 or more points placed on the extreme boundaries of a region of interest (e.g., a tumor).</p>
<p><strong>Setup:</strong></p>
<ol>
<li>The user loads multiple MR sequences from a single scan session, and selects one sequence to define the points. Images may be of different sizes and FOV, but are registered in the world coordinate.</li>
<li>These points (minimum of 6) are placed on or near the extreme boundaries of the tumor. A bounding box is generated based on these points.</li>
<li>The user then inspects other sequences to verify that the bounding box fully covers the ROI. If not, the user can manually adjust the box.</li>
<li>The final bounding box is saved as a segmentation (NIfTI) for each MR image.</li>
</ol>
<p>The problem I’m facing is that the selected points and the generated bounding box are in <strong>world coordinates</strong> , while I’d like the bounding box to align with <strong>RAS coordinates</strong> . Now I register the bounding box to every image and save them.</p>
<p>To achieve this, I register the bounding box to each image, then generate a <code>vtkMRMLLabelMapVolumeNode</code> , and finally update a <code>vtkMRMLSegmentationNode</code> to save it as a segmentation in NIfTI format.</p>
<p>However, this workflow is tedious, and there’s a disconnect: the box the user adjusts is not the one that is ultimately saved. As shown in the figure, the box with bright-green edge is what the user manipulates, while the colored box (in RAS) is the final saved segmentation.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aaf2288d58c8811de8ad1fc3ab7bab2302a1b7f1.png" data-download-href="/uploads/short-url/oofZv8fimW7R2yARHnl4OqKtqX7.png?dl=1" title="Screenshot 2025-05-15 at 12.49.02" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aaf2288d58c8811de8ad1fc3ab7bab2302a1b7f1.png" alt="Screenshot 2025-05-15 at 12.49.02" data-base62-sha1="oofZv8fimW7R2yARHnl4OqKtqX7" width="349" height="337"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-05-15 at 12.49.02</span><span class="informations">349×337 51 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>My Question:</strong></p>
<p>Is there a way in 3D Slicer to allow the user to <strong>directly adjust the bounding box in RAS coordinates</strong> for my case, so that the edited version is the same as the final output—without needing to separately register from world to RAS?</p>

---
