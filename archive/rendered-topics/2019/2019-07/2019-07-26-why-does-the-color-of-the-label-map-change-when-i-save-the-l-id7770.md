# Why does the color of the label map change when I save the label map?

**Topic ID**: 7770
**Date**: 2019-07-26
**URL**: https://discourse.slicer.org/t/why-does-the-color-of-the-label-map-change-when-i-save-the-label-map/7770

---

## Post #1 by @kscript (2019-07-26 09:00 UTC)

<p>Hi.<br>
I am currently working on outputting Dicom as a 3D Slicer and annotating it.<br>
Annotation completed file is saved as nrrd file. If I load the saved file again, the color was changed. Why is the color changing?</p>
<p>Original Annotation Data<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e09620e34865acf3a66f002e7db0fcf9bddc0e3a.png" data-download-href="/uploads/short-url/w2MBkCOE9EONaUiP0ITxtGeuu5s.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e09620e34865acf3a66f002e7db0fcf9bddc0e3a_2_690x375.png" alt="image" data-base62-sha1="w2MBkCOE9EONaUiP0ITxtGeuu5s" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e09620e34865acf3a66f002e7db0fcf9bddc0e3a_2_690x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e09620e34865acf3a66f002e7db0fcf9bddc0e3a_2_1035x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e09620e34865acf3a66f002e7db0fcf9bddc0e3a_2_1380x750.png 2x" data-dominant-color="393A42"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1997×1087 67.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Load Data<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e8540f3359cc0cd3ef8887684cdac55864843e9.png" data-download-href="/uploads/short-url/6Dxsq5xPTBLvTBoWucG1240fpqN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e8540f3359cc0cd3ef8887684cdac55864843e9_2_690x362.png" alt="image" data-base62-sha1="6Dxsq5xPTBLvTBoWucG1240fpqN" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e8540f3359cc0cd3ef8887684cdac55864843e9_2_690x362.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e8540f3359cc0cd3ef8887684cdac55864843e9_2_1035x543.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e8540f3359cc0cd3ef8887684cdac55864843e9_2_1380x724.png 2x" data-dominant-color="32303C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2072×1088 63.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2019-07-26 12:20 UTC)

<p>If you save the segmentation as a segmentation node (4D .seq.nrrd file) then colors are preserved.</p>
<p>If you export to merged labelmap then voxels are saved to a 3D .nrrd file and segment names and colors are saved to a separate color table (.ctbl file). If you save and load the entire scene, association between labelmap and color table is preserved. If you load the labelmap volume separately, you also need to load the color table and set the labelmap volume to use it for display.</p>
<p>I would recommend to keep using segmentation node format until final export. Use latest Slicer stable release and Segment Editor module for editing.</p>

---

## Post #3 by @kscript (2019-07-28 23:58 UTC)

<p>Hi lassoan.<br>
Thanks for your relply.<br>
And I have another question.<br>
I created a program that can open nrrd files and i trying to open Segmentation.seg.nrrd. but i cannot open.<br>
Segmentation.seg.nrrd file is cannot open alone but i need to open nrrd file alone.<br>
if i open nrrd file, i must open origin file.<br>
how to open Segmentation.seg.nrrd file alone.</p>

---

## Post #4 by @lassoan (2019-07-29 03:06 UTC)

<p>Segmentation is stored in a 4D nrrd file with a couple of custom fields to store additional metadata - see detailed description <a href="https://apidocs.slicer.org/master/classvtkMRMLSegmentationStorageNode.html" rel="nofollow noopener">here</a>.</p>
<p>You can use any nrrd reader that is capable to read 4D files. If your software cannot read such files then you can export to 3D labelmap (nrrd file) + color table (text file) and read those.</p>

---

## Post #5 by @Reza (2023-11-27 17:29 UTC)

<p>Hi,<br>
I have the same problem. When I use the Segment Editor Module, and save my segmentation, when I reopen the segmented file, I see that the labels have been changed. I would be thankful if you could help me with this issue.</p>

---

## Post #6 by @mikebind (2023-11-28 20:41 UTC)

<p>Did you read this response above?</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="7770" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you save the segmentation as a segmentation node (4D .seq.nrrd file) then colors are preserved.</p>
<p>If you export to merged labelmap then voxels are saved to a 3D .nrrd file and segment names and colors are saved to a separate color table (.ctbl file). If you save and load the entire scene, association between labelmap and color table is preserved. If you load the labelmap volume separately, you also need to load the color table and set the labelmap volume to use it for display.</p>
<p>I would recommend to keep using segmentation node format until final export. Use latest Slicer stable release and Segment Editor module for editing.</p>
</blockquote>
</aside>
<p>If you have tried this approach, what is not working?</p>

---
