---
topic_id: 18904
title: "Decomposing The Transformation Matrix And The Order Of Opera"
date: 2021-07-24
url: https://discourse.slicer.org/t/18904
---

# Decomposing the Transformation matrix and the order of operation?

**Topic ID**: 18904
**Date**: 2021-07-24
**URL**: https://discourse.slicer.org/t/decomposing-the-transformation-matrix-and-the-order-of-operation/18904

---

## Post #1 by @Amit_1993 (2021-07-24 09:29 UTC)

<p>Hi all!</p>
<p>In 3D slicer Image Registration Operation :</p>
<p>I want to decompose the individual Transformation operation as a product of Translation Matrix, Scaling Matrix, and Rotation Matrix(if used). So, I need to know the order of multiplication and elements of these matrices. Finally, I wanted to take a general equation out of these matrices which tell the order of operation and element relationship (if any, between the elements of each matrix)</p>
<p>Can anyone give some solution related to this? Thanks!</p>

---

## Post #2 by @lassoan (2021-07-24 12:27 UTC)

<p>Scaling matrix is a diagonal matrix that contains the column norms of the transformation matrix.<br>
Rotation matrix is the transformation matrix with translation removed (the 4th column set to <code>[0,0,0,1]</code>) and the columns normalized.<br>
Translation matrix is the transformation matrix with the top-left 3x3 submatrix set to identity matrix.</p>
<p>Order of rotation and scaling does not matter (rotate then scale = scale then rotate). You need to translate after you rotated&amp;scaled.</p>

---
