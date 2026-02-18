# How can I access the source code for expanding margin method?

**Topic ID**: 31646
**Date**: 2023-09-11
**URL**: https://discourse.slicer.org/t/how-can-i-access-the-source-code-for-expanding-margin-method/31646

---

## Post #1 by @erhushenshou (2023-09-11 17:43 UTC)

<p>I am now trying to read source code to learn but I have no idea to find the exact file or location for the method I am interested in at this moment. Can anyone help?</p>

---

## Post #2 by @mikebind (2023-09-12 02:58 UTC)

<p>Here you go: <a href="https://github.com/Slicer/Slicer/blob/0e332ecdadff2034071260e8ffb5dd38e8f1ab42/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorMarginEffect.py#L13" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/blob/0e332ecdadff2034071260e8ffb5dd38e8f1ab42/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorMarginEffect.py#L13</a></p>
<p>I searched “margin” on the Slicer github repository and looked through the first few code results.  I knew I was looking for a Segment Editor Effect, which helped.</p>
<p>There is also this example in the script repository which uses a VTK filter directly (though note that the margin is specified as a kernel size is in voxels rather than millimeters in that case).<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#process-segment-using-a-vtk-filter" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a></p>

---
