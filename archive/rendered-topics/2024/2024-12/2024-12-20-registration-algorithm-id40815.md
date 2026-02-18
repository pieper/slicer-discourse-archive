# Registration Algorithm

**Topic ID**: 40815
**Date**: 2024-12-20
**URL**: https://discourse.slicer.org/t/registration-algorithm/40815

---

## Post #1 by @benedettabottelli (2024-12-20 09:40 UTC)

<p>I need to segment different structures from images acquired using various imaging techniques that, however, do not share the same reference system. Therefore, I would require a registration algorithm to align the STL solids resulting from the various segmentations. Does 3D Slicer have an extension that allows me to do this? Additionally, does the extension support rigid registration for volumes</p>

---

## Post #2 by @pieper (2024-12-20 09:59 UTC)

<p>Yes, there are plenty of registration algorithms available.  If you can be more specific people might be able to help you.</p>

---

## Post #3 by @benedettabottelli (2024-12-20 10:03 UTC)

<p>I have CT and MRI images of the shoulder from the same patient, and I need to segment as many structures as possible (bones, muscles, ligaments) based on the available resolution. I plan to segment the bones from the CT images, as the process is much faster, and the other structures from the MRI images. However, since the structures are segmented from different datasets, they are not aligned. I want to understand how I can align the various STL files of bones and muscles to create a complete model.</p>

---

## Post #4 by @pieper (2024-12-20 10:26 UTC)

<p>Okay, thanks, that helps.  Generally registration of MR and CT is trivial in places like the brain/skull where there are few moving parts.  But the shoulder is highly mobile and there’s really no way to get a pixel-wise alignment of all the structures.  Bone-by-bone is probably all you can expect.  Maybe you can use the MR as your base coordinate system for the soft tissue details and then bring in the CT based bones one by one.</p>
<p>Search the archives here.  I believe similar questions have come up before.</p>

---

## Post #5 by @benedettabottelli (2025-01-14 10:40 UTC)

<p>is it possible to use SegmentRegistration for this scope?</p>

---
