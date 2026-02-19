---
topic_id: 41748
title: "Do You Know How To Convert Real World Coordination To Image"
date: 2025-02-17
url: https://discourse.slicer.org/t/41748
---

# Do you know how to convert real world coordination to image coordination?

**Topic ID**: 41748
**Date**: 2025-02-17
**URL**: https://discourse.slicer.org/t/do-you-know-how-to-convert-real-world-coordination-to-image-coordination/41748

---

## Post #1 by @chris_Prince (2025-02-17 20:25 UTC)

<p>In data probe. we can see the image coordination, do you know or having script to know how it convert the real world coordination to image coordination?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1fd79943581c8ac01ddf67de07b58351c9787b0.jpeg" data-download-href="/uploads/short-url/ywK8y1PiZ4xUcKwgFVBR4vuYSdi.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1fd79943581c8ac01ddf67de07b58351c9787b0_2_690x348.jpeg" alt="image" data-base62-sha1="ywK8y1PiZ4xUcKwgFVBR4vuYSdi" width="690" height="348" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1fd79943581c8ac01ddf67de07b58351c9787b0_2_690x348.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1fd79943581c8ac01ddf67de07b58351c9787b0_2_1035x522.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1fd79943581c8ac01ddf67de07b58351c9787b0_2_1380x696.jpeg 2x" data-dominant-color="8D8D8D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1776×898 180 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
My task is to get the boundingbox in 2D slicer from 3D segmentation.  so e.g I get a segmentation bounding box coordination like: “box”: [<br>
[<br>
68.03462219238281,<br>
105.50535583496094,<br>
-159.68885803222656,<br>
21.68463134765625,<br>
21.6978759765625,<br>
17.426727294921875<br>
],         but I don’t know how to map them back to the image coordination.<br>
I find a guild in 3D visulization: <a href="https://github.com/Project-MONAI/tutorials/tree/main/detection/luna16_visualization" class="inline-onebox" rel="noopener nofollow ugc">tutorials/detection/luna16_visualization at main · Project-MONAI/tutorials · GitHub</a>       so then I convert a .obj file like: for one boundingbox, the 8 corner coordination(cube) like :v 78.87693786621094 116.35429382324219 -168.4022216796875<br>
v 78.87693786621094 94.65641784667969 -168.4022216796875<br>
v 57.19230651855469 94.65641784667969 -168.4022216796875<br>
v 57.19230651855469 116.35429382324219 -168.4022216796875<br>
v 78.87693786621094 116.35429382324219 -150.97549438476562<br>
v 78.87693786621094 94.65641784667969 -150.97549438476562<br>
v 57.19230651855469 94.65641784667969 -150.97549438476562<br>
v 57.19230651855469 116.35429382324219 -150.97549438476562       and the nii.gz original file attrubute like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11e150f821979954e5aeb68a82678e765fa7fd03.png" data-download-href="/uploads/short-url/2yaR0i2Eqn796U0FjNN5IqCcoXp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11e150f821979954e5aeb68a82678e765fa7fd03.png" alt="image" data-base62-sha1="2yaR0i2Eqn796U0FjNN5IqCcoXp" width="690" height="335" data-dominant-color="E5E5E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1122×546 28.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
However, I use<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e58e75ab7c4b91973a63df3aafa8fb2b6a9d3146.png" data-download-href="/uploads/short-url/wKKyFg9gHbXXi4z7hmsfSoxEtVQ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e58e75ab7c4b91973a63df3aafa8fb2b6a9d3146_2_690x325.png" alt="image" data-base62-sha1="wKKyFg9gHbXXi4z7hmsfSoxEtVQ" width="690" height="325" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e58e75ab7c4b91973a63df3aafa8fb2b6a9d3146_2_690x325.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e58e75ab7c4b91973a63df3aafa8fb2b6a9d3146_2_1035x487.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e58e75ab7c4b91973a63df3aafa8fb2b6a9d3146_2_1380x650.png 2x" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1558×736 46 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I calculated , in Z -ray. it works,  the bounding box contain 14 slicer  which same to :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f09b5ed9d0dd8b00013e0869a651c0cbd7085916.png" data-download-href="/uploads/short-url/ykvtj1SAhG1Z80XW9WtxrpGpunk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f09b5ed9d0dd8b00013e0869a651c0cbd7085916_2_514x500.png" alt="image" data-base62-sha1="ykvtj1SAhG1Z80XW9WtxrpGpunk" width="514" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f09b5ed9d0dd8b00013e0869a651c0cbd7085916_2_514x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f09b5ed9d0dd8b00013e0869a651c0cbd7085916_2_771x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f09b5ed9d0dd8b00013e0869a651c0cbd7085916.png 2x" data-dominant-color="F1F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">880×856 45.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
but, X,Y are wrong.  however I find that in monai 3D slicer data probe.  the conversion is correct.  so I wnat to know how it convert?</p>

---

## Post #2 by @pieper (2025-02-17 21:35 UTC)

<p>You don’t need to do these calculations yourself.  There are lots of example in the script repository for going between screen coordinates, world coordinates, and image index coordinates.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-volume-voxel-coordinates-from-markup-control-point-ras-coordinates">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-volume-voxel-coordinates-from-markup-control-point-ras-coordinates</a></p>

---
