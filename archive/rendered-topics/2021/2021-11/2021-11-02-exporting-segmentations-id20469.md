# Exporting Segmentations

**Topic ID**: 20469
**Date**: 2021-11-02
**URL**: https://discourse.slicer.org/t/exporting-segmentations/20469

---

## Post #1 by @NaghmehAnsari (2021-11-02 21:59 UTC)

<p>Hello ,</p>
<p>I am trying to create a segment model consisting of a Ventricle and head model, two target points, and trajectories to targets and extract them into a merged file.<br>
I am receiving “the application has run out of memory” error, Exception thrown in event: bad allocation.</p>
<p>What I am doing is that I create target and trajectory models and drag and drop them in the Ventricle segmentation node to be able to extract the model, but then slicer hangs for several minutes and then I get the mentioned error.</p>
<p>Can you help me to find out what I’m doing wrong? is the model too heavy for Slicer to render?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2021-11-03 04:26 UTC)

<p>The physical size of a head and all the other objects are quite large, so if you create a high-resolution segmentation then you can run out of memory (because the extent of the internal labelmap representation is expanded to include all objects).</p>
<p>The best would be if you could add more physical RAM to your computer but probably just increasing virtual memory size in your operating system settings would work, too.</p>
<p>You can also decrease the resolution (increase spacing) of the segmentation’s internal labelmap (using “Specify geometry” button) thereby reducing the memory need.</p>
<p>If you need surface meshes in the end then you can export all the meshes in the scene into into glTF, OBJ, or old x3d or vrml format. Probably <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-entire-scene-as-gltf">exporting glTF</a> is the best, as it is the most modern and powerful file format and it has nice web viewers.</p>

---
