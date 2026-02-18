# OP-planing 25° hip rotation for DPO

**Topic ID**: 7028
**Date**: 2019-06-04
**URL**: https://discourse.slicer.org/t/op-planing-25-hip-rotation-for-dpo/7028

---

## Post #1 by @norus (2019-06-04 19:30 UTC)

<p>Operating system: win 7<br>
Slicer version: 4.10.2<br>
Expected behavior: the hip is segmented in two parts. One should be rotated about 25°. Exported one part in stl and imported it back. it landed at a very different place. Is there an option to do? or is CAD needed.<br>
Actual behavior: great software, and forum, thank´s a lot</p>

---

## Post #2 by @lassoan (2019-06-04 19:56 UTC)

<p>When you export a segment then you can choose LPS or RAS coordinate system. Slicer always assumes RAS when reading an STL, OBJ, or PLY file. If you exported in LPS coordinate system then you need to manually <a href="https://discourse.slicer.org/t/dicom-and-vtk-file-orientation-issue/717/7">apply a transform that flips the first two axes</a>.</p>
<p>We’ll soon <a href="https://issues.slicer.org/view.php?id=4445" rel="nofollow noopener">add automatic orientation adjustment based on file header</a> but it is still probably a few months away (planned for Slicer5).</p>

---

## Post #3 by @norus (2019-06-04 20:04 UTC)

<p>Thank you Professor, that helps.</p>

---
