---
topic_id: 48873
title: "Parent vessel reconstruction vmtk command line"
date: 2026-11-13
url: https://discourse.slicer.org/t/48873
last_bumped: 2026-11-13T13:38:45.147Z
---

# Parent vessel reconstruction vmtk command line

**Topic ID**: 48873
**Date**: 2026-11-13
**URL**: https://discourse.slicer.org/t/parent-vessel-reconstruction-vmtk-command-line/48873

---

## Post #1 by @amscosta (2026-11-13 13:38 UTC)

<p>Hello,</p>
<p>I am using the parent vessel reconstruction technique outlined in : <a href="http://vmtk.github.io/tutorials/ParentVesselReconstruction.html" class="inline-onebox" rel="noopener nofollow ugc">Parent vessel reconstruction | vmtk - the Vascular Modelling Toolkit</a></p>
<p>Unfortunatelly I am getting a “bumping” surface in the reconstructed parent (see the arrow in the attached figure). How can I “smooth” that bumping ? What settings in the command line should I play with?</p>
<p>Here it is the sequence of command lines I am using :</p>
<p>vmtk vmtkdelaunayvoronoi -ifile 203.vtp -removesubresolution 1 -voronoidiagramfile 203_voronoi.vtp<br>
vmtk vmtkcenterlines -ifile 203.vtp -endpoints 1 --pipe vmtkcenterlineresampling -length 0.1 -ofile 203_forwardcl.vtp<br>
python patchandinterpolatecenterlines.py . 0203 lateral<br>
python clipvoronoidiagram.py . 0203<br>
python paralleltransportvoronoidiagram.py . 0203 1</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a92b05ff0f97f90d6219c123b6f6ac1bd6990ae5.jpeg" data-download-href="/uploads/short-url/o8wRVnkDMDOkBou7wZZ1zNBrnox.jpeg?dl=1" title="parent_vessel_reconstruction" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a92b05ff0f97f90d6219c123b6f6ac1bd6990ae5_2_690x330.jpeg" alt="parent_vessel_reconstruction" data-base62-sha1="o8wRVnkDMDOkBou7wZZ1zNBrnox" width="690" height="330" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a92b05ff0f97f90d6219c123b6f6ac1bd6990ae5_2_690x330.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a92b05ff0f97f90d6219c123b6f6ac1bd6990ae5_2_1035x495.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a92b05ff0f97f90d6219c123b6f6ac1bd6990ae5_2_1380x660.jpeg 2x" data-dominant-color="8E7E81"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">parent_vessel_reconstruction</span><span class="informations">1501×718 92.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
