# Implicit representation of the segmentation

**Topic ID**: 14531
**Date**: 2020-11-10
**URL**: https://discourse.slicer.org/t/implicit-representation-of-the-segmentation/14531

---

## Post #1 by @Tekk_ya (2020-11-10 21:36 UTC)

<p>Hi everyone,</p>
<p>I was wondering if I can get an implicit representation of a segmented geometry in the 3DSlicer and do morphological or logical operations between two implicit functions such as union, growing, etc. I am already familiar with the 3DSlicer user interface and the logical operations and margin tool. However, I am mainly asking if it is possible to get implicit functions before creating the meshes through python. I would appreciate it if you can share how I can get those functions as I haven’t used 3DSlicer’s python interface before.</p>
<p>Best</p>

---

## Post #2 by @lassoan (2020-11-10 22:01 UTC)

<p>The options are quite limited for implicit representation of arbitrary 3D shapes. The only practically usable method that I am aware of is distance maps, which we already use (generate dynamically as needed, for example in Margin effect). Slicer also supports fractional labelmap representation. However, binary labelmap representation proved to work well enough and hard to beat in simplicity and performance.</p>
<p>You can find many examples of how to run segment editor effects from Python (without GUI) in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">script repository</a>.</p>

---
