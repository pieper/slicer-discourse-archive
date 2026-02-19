---
topic_id: 34169
title: "Probe Position And Ijk Ras Coordinates"
date: 2024-02-06
url: https://discourse.slicer.org/t/34169
---

# Probe position and IJK_RAS coordinates

**Topic ID**: 34169
**Date**: 2024-02-06
**URL**: https://discourse.slicer.org/t/probe-position-and-ijk-ras-coordinates/34169

---

## Post #1 by @alessandro_um (2024-02-06 15:06 UTC)

<p>Hello,<br>
I am learning the ropes with orienting dicoms, so I am using some well known softwares as a ground of truth, among them I’m using Slicer.<br>
Through math formulas I obtained the same data found under Volume Information (origin and rotation matrix).<br>
What I am struggling to catch are the points coordinates shown in Data Probe that show up when moving the cursor [CT.xxxxxx (coord1, coord2, coord3) ], this are the coordinates in unscaled dicom coordinates with RAS orientation?<br>
Given a point P_ijk (should be in not oriented raw data coordinates right?), and having the IJK_TO_RAS_matrix, to obtain the probe position I should do: IJK_TO_RAS_direction_matrix * P_ijk?</p>
<p>As an example, I have a CT dicom of a patient in a prone position, the header data are:<br>
image_patient_position = [134.716796875, 313.716796875, -78.5]<br>
image_orientation_patient = [-1,0,0,0,-1,0]<br>
rows = columns = 512<br>
spacing = [0.566, 0.566]<br>
calculated_spacing_between_slices = 0.7<br>
n_slices = 177<br>
Extent = [0, 512, 0, 512, 0, 177]</p>
<p>In Slicer upon loading the dicom i have:<br>
the origin in [-134.716796875, -313.716796875, -78.5] and<br>
the IJKtoRAS_direction_matrix =<br>
[1.0, 0.0, 0.0]<br>
[0.0, 1.0, 0.0]<br>
[0.0, 0.0, 1.0].<br>
I have the same numbers using my formulas, so to obtain the ijk position of the upper_left_corner Pnt[0.0, 0.0, 0.0] in IJK i did [IJKtoRAS_direction_matrix * Pnt] and obviously I get the same point as the rotation matrix is an Identity, but in probes coordinates it’s [512, 512, 0] and not [0, 0, 0].<br>
What am I missing?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41a5ec71d6ffb0080f5419ca1fbdb495fef85ee8.png" data-download-href="/uploads/short-url/9mKwzazVWxbjOxJfNLiGV7xMJWU.png?dl=1" title="probe_position" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41a5ec71d6ffb0080f5419ca1fbdb495fef85ee8_2_690x301.png" alt="probe_position" data-base62-sha1="9mKwzazVWxbjOxJfNLiGV7xMJWU" width="690" height="301" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41a5ec71d6ffb0080f5419ca1fbdb495fef85ee8_2_690x301.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41a5ec71d6ffb0080f5419ca1fbdb495fef85ee8_2_1035x451.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41a5ec71d6ffb0080f5419ca1fbdb495fef85ee8_2_1380x602.png 2x" data-dominant-color="353437"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">probe_position</span><span class="informations">1915×837 238 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @alessandro_um (2024-02-06 16:21 UTC)

<p>Maybe the rotation around the corner (origin in IJK) can be misleading as the rotation is done around the origin, in my tests I evaluate the rotation of the points forming the bounding box having the same extent as the volume.</p>

---
