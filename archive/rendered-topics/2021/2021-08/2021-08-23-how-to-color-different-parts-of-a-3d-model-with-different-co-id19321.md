---
topic_id: 19321
title: "How To Color Different Parts Of A 3D Model With Different Co"
date: 2021-08-23
url: https://discourse.slicer.org/t/19321
---

# How to color different parts of a 3d model with different colors according to the pixel value from the ct scans?

**Topic ID**: 19321
**Date**: 2021-08-23
**URL**: https://discourse.slicer.org/t/how-to-color-different-parts-of-a-3d-model-with-different-colors-according-to-the-pixel-value-from-the-ct-scans/19321

---

## Post #1 by @akshay_pillai (2021-08-23 16:09 UTC)

<p>I have created a 3d model of a head from ct scans of the head. I would like to know how I can color different parts of the head in different colors using the pixel value in the ct scans. Is there a way to do this?<br>
I know I can individually segment the body parts in the head with the segment editor but is there a way to do this with just pixel values so I have different colors on the 3d model of the head. For example, the tongue is one color, tonsils are a different color, and so on. Any help is appreciated. Thanks.</p>

---

## Post #2 by @lassoan (2021-08-23 16:19 UTC)

<p>Do you want to “color” (it will be all just different shade of gray) the models using the CT values? You can do that with <a href="https://discourse.slicer.org/t/mapping-intensity-values-to-model-surface-as-texture/6972">Probe Volume with Model module</a>.</p>
<p>Usually it does not result in very interesting or nice-looking images (especially if you segment soft tissues in CT). See some discussion in these topics:</p>
<ul>
<li><a href="https://discourse.slicer.org/t/mapping-intensity-values-to-model-surface-as-texture/6972" class="inline-onebox">Mapping intensity values to Model Surface as texture?</a></li>
<li><a href="https://discourse.slicer.org/t/retain-image-color-in-volume-rendering/12294" class="inline-onebox">Retain Image Color in Volume Rendering</a></li>
</ul>

---

## Post #3 by @akshay_pillai (2021-08-23 20:15 UTC)

<p>Yes, I tried probe volume with model module and the 3d model still looks pretty much the same as from segment editor. Is there a way I can choose a custom color map or a pre defined color map? My objective is to render a 3d model close to natural anatomical colors.</p>

---

## Post #4 by @lassoan (2021-08-23 20:41 UTC)

<p>CT density has nothing to do with natural colors that you would see when you take photos of skin or exposed tissues. Even colors probed from frozen cross-section images do not resemble those colors or textures - as discussed in the <a href="https://discourse.slicer.org/t/retain-image-color-in-volume-rendering/12294/19" class="inline-onebox">Retain Image Color in Volume Rendering - #19 by lassoan</a> link that I posted above.</p>
<p>All the colors and textures that you see in anatomical atlases are mostly just artistic creative work. The artist might get some inspiration of colors from real pictures, but colors must be changed to clearly differentiate structures that may look exactly the same in real life for a human eye in with regular lighting, textures may need to be changed/emphasized to help with understanding 3D geometry, the picture has to look aesthetically pleasing, etc. so the final result does look like real life photos at all. So, you will not be able to automatically create artistic illustrations from CT images either.</p>
<p>If you want to create nice illustrations from CTs then you can segment the image to get shapes (meshes) and then use computer graphics software (Blender, etc.) to apply textures, set up nice lighting, transparencies, maybe do rigging and skinning, etc. See for example <a href="https://discourse.slicer.org/t/open-source-human-anatomy-atlas/17734/6">this topic</a> to get some inspiration.</p>

---
