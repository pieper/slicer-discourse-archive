---
topic_id: 46986
title: "How To Convert A 4X4 Matrix To Inter Bone Kinematic Paramete"
date: 2026-05-11
url: https://discourse.slicer.org/t/46986
---

# How to convert a 4x4 matrix to inter-bone kinematic parameters

**Topic ID**: 46986
**Date**: 2026-05-11
**URL**: https://discourse.slicer.org/t/how-to-convert-a-4x4-matrix-to-inter-bone-kinematic-parameters/46986

---

## Post #1 by @HHH (2026-05-11 12:38 UTC)

<p>Hello everyone, I am working on a knee joint registration project. According to the experience of predecessors, I have obtained a 4x4 matrix, but I am unable to calculate the kinematics of the knee joint. I am seeking help here.</p>
<p>How can two 4x4 homogeneous transformation matrices (representing the coordinate systems of bone A and bone B, respectively) be converted into the kinematic parameters of bone B relative to bone A? The calculations needed are:</p>
<ol>
<li>Relative translation (in the coordinate system of bone A)</li>
<li>Relative rotation angles (Euler angles: Yaw/Pitch/Roll)</li>
</ol>
<p>Do I need to first establish coordinate systems (including the origin) for the two bones, and how would I represent the coordinate systems in the volume?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c12a22b1968d7977b51305ef55073dd0531a2b0.png" data-download-href="/uploads/short-url/mgGpg6ztUNfmSnMpRJvxPVlZxHW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c12a22b1968d7977b51305ef55073dd0531a2b0.png" alt="image" data-base62-sha1="mgGpg6ztUNfmSnMpRJvxPVlZxHW" width="690" height="39" data-dominant-color="424242"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1915×110 9.49 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>This is a 4x4 matrix of values</p>

---
