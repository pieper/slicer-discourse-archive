---
topic_id: 11140
title: "Ultrasonix Linear Probe Calibration Matrix"
date: 2020-04-16
url: https://discourse.slicer.org/t/11140
---

# Ultrasonix linear probe calibration matrix

**Topic ID**: 11140
**Date**: 2020-04-16
**URL**: https://discourse.slicer.org/t/ultrasonix-linear-probe-calibration-matrix/11140

---

## Post #1 by @mta152 (2020-04-16 02:54 UTC)

<p>Hi,</p>
<p>I have a little confusion about the calibration matrix (referred to as C matrix) for the linear probe. As written in this website: <a href="http://www.ultrasonix.com/wikisonix/index.php/GPS_Data_Collection" class="inline-onebox" rel="noopener nofollow ugc">GPS Data Collection - WikiSonix</a>, C is a 3x3 matrix and based on this website <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceSonixVideo.html" class="inline-onebox" rel="noopener nofollow ugc">Plus applications user manual: Ultrasonix ultrasound systems</a>, C is reformed to be a 4x4 transformation matrix (referred to as T). I can do simple math to verify both are fine, but here is what I am confused:</p>
<ol>
<li>As written on both websites “% Ultrasonix uses [1yx] coordinates (first column is origin, second column is Y axis, third column is X axis)”, we can compute the missing Z axis by:<br>
Z axis vector = cross(X,Y). Now if [X, Y, Z] represents a rotation matrix, why norm(Y) != 1. Appreciate that norm(Y) is close to being 1, but why it is not 1.</li>
<li>Given the rotation matrix R = [X, Y, Z] and in order to avoid the confusion left-hand and right-hand rules may bring up, I used the combined transformation matrix (R_ref = Rz<em>Ry</em>Rx) as written in the bottom of this website as a reference: <a href="http://planning.cs.uiuc.edu/node102.html" class="inline-onebox" rel="noopener nofollow ugc">Yaw, pitch, and roll rotations</a><br>
My question is<br>
R = R_ref or R = transpose(R_ref) ?</li>
</ol>
<p>Any suggestion is appreciated. Thank you.</p>
<p>Best regards,<br>
Mike</p>

---
