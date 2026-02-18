# Brains registration error

**Topic ID**: 18228
**Date**: 2021-06-20
**URL**: https://discourse.slicer.org/t/brains-registration-error/18228

---

## Post #1 by @muratmaga (2021-06-20 00:13 UTC)

<p>I am trying to register one mouse head to another. These two are about 180 rotated with respect to each other. So I had defined 4 Lms on both of them and used Fiducial registration (rigid) to roughly align them. For better alignment, I am trying to use the Brains Registration. I have provided the output from the Fiducial registration as the initializing transform. However, I am still getting this error:</p>
<p><code>All samples map outside moving image buffer. The images do not sufficiently overlap. They need to be initialized to have more overlap before this metric will work. For instance, you can align the image centers by translation.</code></p>
<p>I can visually confirm that once the transformation from Fiducial registration is applied, these two volumes do indeed overlap.</p>
<p>Used sample A in fiducial registration as the fixed landmark set, and B as the moving one. And in the brains, I am putting as Sample A as the fixed image, and Sample B as the moving. So the image domains should be consistent too.</p>
<p>Am I misunderstanding what initializing transform supposed to do in Brains?</p>

---

## Post #2 by @lassoan (2021-06-20 03:07 UTC)

<p>Does it work well if you harden the transform on the moving image instead of using it as initialization transform?</p>

---
