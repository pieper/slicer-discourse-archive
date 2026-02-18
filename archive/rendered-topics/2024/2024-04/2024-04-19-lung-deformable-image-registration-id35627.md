# Lung deformable image registration

**Topic ID**: 35627
**Date**: 2024-04-19
**URL**: https://discourse.slicer.org/t/lung-deformable-image-registration/35627

---

## Post #1 by @Wpy_K (2024-04-19 20:44 UTC)

<p>Hi everyone,</p>
<p>I’m a Medical physics student, I’m new for using 3DSlicer. I has problem that I want to deformable image (DIR) organ at risk nearby lung for check about breathing motion effected to other organ nearby lung, but I confused which extension I can used for. found Elastix extension in 3Dslicer.<br>
I’m writing to ask i can using Elastix for defromation or other suitable for ?<br>
I using CT image in 10 phase for using motion information.</p>
<p>Thank you for your support,</p>
<p>best regards,</p>

---

## Post #2 by @lassoan (2024-04-19 20:47 UTC)

<p>You can use Sequence Registration extension to compute the displacement field for the entire time sequence. You can use this transformation time sequence for motion compensation, dose accumulation, etc.</p>

---

## Post #3 by @Wpy_K (2024-04-22 06:11 UTC)

<p>Thank you for your suggestion.</p>

---
