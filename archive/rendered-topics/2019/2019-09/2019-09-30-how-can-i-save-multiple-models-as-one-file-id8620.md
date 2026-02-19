---
topic_id: 8620
title: "How Can I Save Multiple Models As One File"
date: 2019-09-30
url: https://discourse.slicer.org/t/8620
---

# How can i save multiple models as one file?

**Topic ID**: 8620
**Date**: 2019-09-30
**URL**: https://discourse.slicer.org/t/how-can-i-save-multiple-models-as-one-file/8620

---

## Post #1 by @Sukhe (2019-09-30 09:07 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/205ebce4c9234424a80cc40559dbcaec3ea5d040.png" alt="image" data-base62-sha1="4CmfKmoqTFZ6Q3Lfb0rvAFEQao8" width="336" height="305"><br>
I want to make a brain model with brain tissue, tumour, and ventricle. I have made these 3 models individually. But when I save them, they are saved as three separate files. How can I save (export) them as one stl or vtk etc file instead of three files?<br>
Thanks</p>

---

## Post #2 by @pieper (2019-09-30 12:30 UTC)

<p>If you want to add all the segments together into a single shape you can use the logic operators in the Segment Editor.  Otherwise I’m not sure what you mean by putting them all in the same file.</p>

---

## Post #3 by @Amine (2019-09-30 13:12 UTC)

<p>Hi, you have three options:</p>
<ol>
<li>If they are still segments, instead of using “Export/import models and labelmaps” use “Export to files” just beneath it, with merge into single file checked and select your export format</li>
<li>If you necessarly have models, you can’t do that natively in slicer (as far as i know), you need to export from slicer individually as .ob/stl import them in blender and export as .obj  with selection only unchecked in export options</li>
<li>to go further you could also import blender into slicer and do the last option automatically</li>
</ol>

---

## Post #4 by @lassoan (2019-09-30 16:31 UTC)

<aside class="quote no-group" data-username="Amine" data-post="3" data-topic="8620">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine/48/4844_2.png" class="avatar"> Amine:</div>
<blockquote>
<p>If you necessarly have models, you can’t do that natively in slicer (as far as i know), you need to export from slicer individually</p>
</blockquote>
</aside>
<p>In Data module, you can convert model nodes into segmentation nodes then drag-and-drop the segments into one segmentation. You can then export this segmentation as a single file as <a class="mention" href="/u/amine">@Amine</a> described above.</p>
<p>You can also merge meshes by a few lines of Python script.</p>
<p>Why do you need to merge the models? What software do you use for further processing (mesh viewing, mesh editing, 3D printing, …)?</p>

---

## Post #5 by @Sukhe (2019-10-02 00:59 UTC)

<p>Thanks Pieper, Segment editor does work for this. But I segmented it in Editor.</p>

---

## Post #6 by @Sukhe (2019-10-02 01:03 UTC)

<p>Thanks Lassoan, I did as what your recommended and it works. I am going mesh the domain in IA-FEMesh and i think this software works better for a single model file.</p>

---

## Post #7 by @Sukhe (2019-10-02 01:04 UTC)

<p>Thanks Amine, t works after i convert the model nodes to segmentation nodes and then follow your option 1.</p>

---

## Post #8 by @lassoan (2019-10-02 01:06 UTC)

<p>You can also use <a href="https://github.com/lassoan/SlicerSegmentMesher" rel="nofollow noopener">Segment mesher extension</a> to create finite-element meshes using Cleaver2 or TetGen directly from a segmentation node. You may also change the script in the extension to add an option to use IA-FEMesh.</p>

---

## Post #9 by @Sukhe (2019-10-02 01:13 UTC)

<p>Thank you so much for your help Lassoan, I will try it and let you know if I have questions.</p>

---
