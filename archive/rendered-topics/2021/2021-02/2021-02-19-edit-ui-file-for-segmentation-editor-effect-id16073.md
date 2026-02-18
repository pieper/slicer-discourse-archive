# Edit UI file for segmentation editor effect

**Topic ID**: 16073
**Date**: 2021-02-19
**URL**: https://discourse.slicer.org/t/edit-ui-file-for-segmentation-editor-effect/16073

---

## Post #1 by @diazandr3s (2021-02-19 02:46 UTC)

<p>Hi,</p>
<p>I started using 3D Slicer a couple of days ago and I’m really excited for the things it can do.<br>
I created a scripted segment editor effect and I was wondering whether I can edit the ui using the same developer options explained in slide 36 in <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx" class="inline-onebox" rel="noopener nofollow ugc">PerkLabBootcamp/day3_2_SlicerProgramming.pptx at master · PerkLab/PerkLabBootcamp · GitHub</a></p>
<p>I’m still struggling a bit with the association of the ui file with the logic. After checking the plugin made for the AIAA server in NVIDIA, it seems a big chunk of that effect was created by the Wizard, right?</p>
<p>I’ll really appreciate your reply,</p>
<p>Best,</p>
<p>Andres</p>

---

## Post #2 by @lassoan (2021-02-19 03:32 UTC)

<p>Most segment editor effects create the user interface by Python scripting, but if you need more than just a few widgets then it is worth using a .ui file. I think the only two examples for this are these:</p>
<ul>
<li><a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify/tree/master/SegmentEditorWrapSolidify/SegmentEditorWrapSolidifyLib" class="inline-onebox">Slicer-SurfaceWrapSolidify/SegmentEditorWrapSolidify/SegmentEditorWrapSolidifyLib at master · sebastianandress/Slicer-SurfaceWrapSolidify · GitHub</a></li>
<li><a href="https://github.com/NVIDIA/ai-assisted-annotation-client/tree/master/slicer-plugin/NvidiaAIAA/SegmentEditorNvidiaAIAALib" class="inline-onebox">ai-assisted-annotation-client/slicer-plugin/NvidiaAIAA/SegmentEditorNvidiaAIAALib at master · NVIDIA/ai-assisted-annotation-client · GitHub</a></li>
</ul>
<p>You can either create new segment editor effect using the Extension wizard and update it to use a .ui file (based on the two above modules as examples), or clone one of the two modules above and rename and modify the files to fit your needs.</p>

---

## Post #3 by @diazandr3s (2021-02-19 09:22 UTC)

<p>Many thanks for your quick reply, I appreciate it.</p>

---
