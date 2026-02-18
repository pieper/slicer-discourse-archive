# Finding the Jacobian of a 3D image transform

**Topic ID**: 29018
**Date**: 2023-04-20
**URL**: https://discourse.slicer.org/t/finding-the-jacobian-of-a-3d-image-transform/29018

---

## Post #1 by @Akor (2023-04-20 03:46 UTC)

<p>Hi, so I have two 3D CT images that I’d like to register. The first being the fixed image and the second the moving image, using elastix in 3D slicer. Is there a way to have elastix output the Jacobian of the image transform? or else how do I know what transformation function is utilized so I can code for the Jacobian matrix separately.</p>

---

## Post #2 by @lassoan (2023-04-20 03:49 UTC)

<p>You can see the computed transformation matrix in Transforms module. However, Jacobian of a linear transform is not that exciting. What is your end goal?</p>
<p>If you want to compute strain for a warping transform then I would recommend to try <a href="https://github.com/KitwareMedical/ITKStrain">ITKStrain</a> on the displacement field vector image exported in Transforms module.</p>

---

## Post #3 by @pieper (2023-04-20 13:29 UTC)

<p>Maybe we should incorporate ITKStrain directly in Slicer?  It could be helpful as a visualization mode for nonlinear transforms.</p>

---

## Post #4 by @gcsharp (2023-04-20 16:41 UTC)

<p><a class="mention" href="/u/akor">@Akor</a> If you want the Jacobian determinant rather than the matrix, you can compute that using plastimatch and then import.  I’m not aware of any software that can export the Jacobian matrix.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks for the tip re: ITKStrain.  Looks interesting!</p>

---
