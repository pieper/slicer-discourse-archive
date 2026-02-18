# Is there any way I can change how the scissor tool works in segment editor?

**Topic ID**: 16472
**Date**: 2021-03-10
**URL**: https://discourse.slicer.org/t/is-there-any-way-i-can-change-how-the-scissor-tool-works-in-segment-editor/16472

---

## Post #1 by @akshay_pillai (2021-03-10 15:12 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11<br>
Expected behavior:<br>
Actual behavior:</p>
<p>I want to use the scissor tools to make dents or cuts on a 3d model. But the scissor tool completely removes everything inside the area drawn or selected. Instead, I want to control the depth of the cut. Is this possible, is there any way I can change that. Or are there any other tools for it?</p>

---

## Post #2 by @muratmaga (2021-03-10 15:31 UTC)

<p>I think the surface cut is meant to do exactly that. You can get that via SegmentEditorExtraEffects extension.</p>

---

## Post #3 by @lassoan (2021-03-10 15:41 UTC)

<p>Yes, using Surface cut effect is a good idea.</p>
<p>If you use Scissors effect then you can control the depth of the cut in slice views. In 3D views, you can use masking to restrict cutting to a specific region; or use two cuts as demonstrated in the <a href="https://lassoan.github.io/SlicerSegmentationRecipes/Craniotomy/">craniotomy segmentation recipe</a>.</p>
<p>You can also change the Scissors effect to make it work exactly as you need. The source code is available <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/qSlicerSegmentEditorScissorsEffect.cxx">here</a>, build instructions are <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/index.html">here</a>. If you make any improvements or customizations that you think could be useful for others then please send a pull request with the proposed changes.</p>

---

## Post #4 by @akshay_pillai (2021-03-10 15:51 UTC)

<p>Thanks, I’ll try that out. Are there any tutorial videos for that?</p>

---

## Post #5 by @lassoan (2021-03-10 15:53 UTC)

<p>There are lots of tutorials, you can start from here <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html#segment-editor-module-overview" class="inline-onebox">Image Segmentation — 3D Slicer documentation</a>, but you can also just search on google and youtube. If you have any specific question then you can ask here.</p>

---
