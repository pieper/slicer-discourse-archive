# Fiducial registration wizard - rigid transform algorithm

**Topic ID**: 24976
**Date**: 2022-08-29
**URL**: https://discourse.slicer.org/t/fiducial-registration-wizard-rigid-transform-algorithm/24976

---

## Post #1 by @joanne40226 (2022-08-29 13:18 UTC)

<p>Hi community, i am now wondering about the rigid transform in IGT - Fiducial registration wizard.<br>
I want to know about the algorithm or the minimal objective function of the rigid transform for landmarks.<br>
However, it did not made the button of source code.<br>
Therefore, i am wondering what the minimal objective function of the landmarks is.<br>
Thank you for your time!</p>

---

## Post #2 by @lassoan (2022-08-31 03:49 UTC)

<p><a href="https://github.com/SlicerIGT/SlicerIGT/blob/d3fd2b26a4c10f6319aa8ae4173abc793c4113ce/FiducialRegistrationWizard/Logic/vtkSlicerFiducialRegistrationWizardLogic.cxx#L361-L363">Fiducial registration wizard module uses vtkLandmarkTransform</a> class for rigid registration.</p>
<p><a href="https://github.com/Kitware/VTK/blob/316670f66f2aa9f4732379790f280187f518e179/Common/Transforms/vtkLandmarkTransform.cxx#L79-L82">vtkLandmarkTransform uses the Horn method</a>.</p>

---

## Post #3 by @joanne40226 (2022-08-31 03:54 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Thank you so much!</p>

---
