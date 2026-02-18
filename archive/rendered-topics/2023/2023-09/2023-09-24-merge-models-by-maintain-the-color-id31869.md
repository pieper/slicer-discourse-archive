# Merge models by maintain the color

**Topic ID**: 31869
**Date**: 2023-09-24
**URL**: https://discourse.slicer.org/t/merge-models-by-maintain-the-color/31869

---

## Post #1 by @linda_varghese (2023-09-24 12:27 UTC)

<p>I wanted to merge different nodes(models) together and also maintain the color of each structure and export it in .obj<br>
I tried to merge the models by ‘merge models’ and even by ‘logical operators’ but the color of all structures become same.</p>
<p>Can anyone suggest me a solution.<br>
My end aim is to convert it into .glb format may be in any other software.</p>
<p>Thanks for your help.</p>

---

## Post #2 by @cpinter (2023-09-25 14:03 UTC)

<p>The reason the color became the same is that the models you merged became the same “poly data” data structure. One way to maintain the “colors” is to merge the models in a way that there is a scalar array in the data structure that labels each vertex. I don’t know about an easy way to do the merging together this way, without scripting. However, it seems to me that this extension could solve your problem: <a href="https://github.com/PerkLab/SlicerOpenAnatomy" class="inline-onebox">GitHub - PerkLab/SlicerOpenAnatomy: 3D Slicer extension for exporting Slicer scenes to use in the OpenAnatomy.org browser</a> (install it and try the OpenAnatomyExport module)</p>

---
