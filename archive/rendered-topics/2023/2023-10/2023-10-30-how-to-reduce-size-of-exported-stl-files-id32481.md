# How to reduce size of exported STL files?

**Topic ID**: 32481
**Date**: 2023-10-30
**URL**: https://discourse.slicer.org/t/how-to-reduce-size-of-exported-stl-files/32481

---

## Post #1 by @lhefeng662 (2023-10-30 11:49 UTC)

<p>How does slicer perform image compression similar to the Simplification: Quadric Edge Collapse Decision function of Meshlab to reduce the size of exported stl files?</p>

---

## Post #2 by @lassoan (2023-10-30 15:52 UTC)

<p>Yes, we have several methods in Slicer that can provide equivalent or better quality mesh simplification and size reduction.</p>
<p>If you have only a few meshes to process then I would recommend to use <code>Surface toolbox</code> module’s <code>Uniform remesh</code> option (it creates very nice mesh with uniform triangle sizes) or <code>Decimate</code> option (it performs quadric decimation - probaby exactly the same as Meshlab - if you enable boundary deletion; or the slightly different DecimatePro algorithm if you disable boundary deletion).</p>
<p>If you need to process many segments (anatomical atlases, TotalSegmentator segmentation results, etc.) then I would recommend to use <code>SlicerOpenAnatomy</code> extension, which can apply quadric decimation to many segments or models at once.</p>

---
