# How to change the scale bar and units in the 2D view area

**Topic ID**: 21718
**Date**: 2022-01-31
**URL**: https://discourse.slicer.org/t/how-to-change-the-scale-bar-and-units-in-the-2d-view-area/21718

---

## Post #1 by @steve01 (2022-01-31 19:16 UTC)

<p>I just finished working in the Segment Editor and I added a scale bar to the red, 2D image.  I noticed that the scale bar is very big.  The red circle in the image is approximately 300µm in diameter. How do I change the size of the scale bar and the units associated with it?  The images were originally from a DICOM which I dropped into image J, concatenated 3 different files, and then exported it as one tiff stack.  I can not program so I will not  be able to work directly with python.  Any help would be greatly appreciated.  Thank you,</p>
<p>Steve</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4c912a1ceffb04d556b4bb8ca6a60d17a1476e3.jpeg" data-download-href="/uploads/short-url/umo1fA7d1JrrcgvW3SxvqD8ZDzl.jpeg?dl=1" title="Screen Shot 2022-01-31 at 11.09.14 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d4c912a1ceffb04d556b4bb8ca6a60d17a1476e3_2_484x500.jpeg" alt="Screen Shot 2022-01-31 at 11.09.14 AM" data-base62-sha1="umo1fA7d1JrrcgvW3SxvqD8ZDzl" width="484" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d4c912a1ceffb04d556b4bb8ca6a60d17a1476e3_2_484x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d4c912a1ceffb04d556b4bb8ca6a60d17a1476e3_2_726x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d4c912a1ceffb04d556b4bb8ca6a60d17a1476e3_2_968x1000.jpeg 2x" data-dominant-color="43525C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-01-31 at 11.09.14 AM</span><span class="informations">1290×1330 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<a href="/uploads/short-url/7HDhIsbvThdxiH6at9MYc4AluQ6.jpeg">Screen Shot 2022-01-31 at 10.59.20 AM|589x500</a></p>

---

## Post #2 by @steve01 (2022-01-31 19:19 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35fde696d429dc6105938e34788fb61b6dbec62e.jpeg" data-download-href="/uploads/short-url/7HDhIsbvThdxiH6at9MYc4AluQ6.jpeg?dl=1" title="Screen Shot 2022-01-31 at 10.59.20 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/35fde696d429dc6105938e34788fb61b6dbec62e_2_589x500.jpeg" alt="Screen Shot 2022-01-31 at 10.59.20 AM" data-base62-sha1="7HDhIsbvThdxiH6at9MYc4AluQ6" width="589" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/35fde696d429dc6105938e34788fb61b6dbec62e_2_589x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/35fde696d429dc6105938e34788fb61b6dbec62e_2_883x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/35fde696d429dc6105938e34788fb61b6dbec62e_2_1178x1000.jpeg 2x" data-dominant-color="A0A2A8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-01-31 at 10.59.20 AM</span><span class="informations">1920×1628 188 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
It seems this screen shot didn’t make it into my first message.</p>

---

## Post #3 by @lassoan (2022-02-01 02:44 UTC)

<p>It seems that you need to set the correct spacing in the image because ImageJ has lost it either during DICOM import or when it saved the data into TIFF format.</p>
<p>You can go to Volumes module and set the correct spacing values in Volume Information section. Spacing of segmentations is not directly editable, so you can either export it to a labelmap volume and edit the spacing there (you can then convert it to a segmentation again) or apply a scaling transform to the segmentation in Transforms module.</p>
<p>In the future, I would recommend to load the images using Slicer. If you try a recent Slicer Preview Release and it does not load the images then upload it somewhere (dropbox, onedrive, …) and post the link here and we update the DICOM importer as needed.</p>
<p>Using TIFF format for 3D image storage is not ideal either, due to no standard way of storing essential 3D metadata (such as origin, spacing, axis directions). Instead, you can use NRRD file format, which is very simple and works well.</p>

---

## Post #4 by @steve01 (2022-02-01 14:43 UTC)

<p>Thank you very much.</p>
<p>I’ll try it.</p>
<p>Steve</p>

---

## Post #5 by @steve01 (2022-02-04 18:42 UTC)

<p>Mr. Lasso,</p>
<p>Thank you for your help.   I was able to export as a labelmap volume and edit it, but how do I convert it back to a segmentaiton.</p>

---

## Post #6 by @lassoan (2022-02-04 19:00 UTC)

<p>In Data module you can right click on the labelmap to convert it to segmentation.</p>

---

## Post #7 by @steve01 (2022-02-04 19:41 UTC)

<p>I supplied a before and after screen shot for reference.  I must have done something wrong, although the scale bar looks correct now.  What happened to the 2D images?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35fde696d429dc6105938e34788fb61b6dbec62e.jpeg" data-download-href="/uploads/short-url/7HDhIsbvThdxiH6at9MYc4AluQ6.jpeg?dl=1" title="Screen Shot 2022-01-31 at 10.59.20 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/35fde696d429dc6105938e34788fb61b6dbec62e_2_589x500.jpeg" alt="Screen Shot 2022-01-31 at 10.59.20 AM" data-base62-sha1="7HDhIsbvThdxiH6at9MYc4AluQ6" width="589" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/35fde696d429dc6105938e34788fb61b6dbec62e_2_589x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/35fde696d429dc6105938e34788fb61b6dbec62e_2_883x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/35fde696d429dc6105938e34788fb61b6dbec62e_2_1178x1000.jpeg 2x" data-dominant-color="A0A2A8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-01-31 at 10.59.20 AM</span><span class="informations">1920×1628 188 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7a0a1610a99915edf692957ec6a35e235a36147.jpeg" data-download-href="/uploads/short-url/zkC5dJsYJ8IOJusTCWutclF29Ej.jpeg?dl=1" title="After" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f7a0a1610a99915edf692957ec6a35e235a36147_2_690x368.jpeg" alt="After" data-base62-sha1="zkC5dJsYJ8IOJusTCWutclF29Ej" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f7a0a1610a99915edf692957ec6a35e235a36147_2_690x368.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f7a0a1610a99915edf692957ec6a35e235a36147_2_1035x552.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f7a0a1610a99915edf692957ec6a35e235a36147_2_1380x736.jpeg 2x" data-dominant-color="ADB0BE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">After</span><span class="informations">1920×1025 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @lassoan (2022-02-08 20:00 UTC)

<p>Everything looks good to me. The slice viewers show cross-sections of the image with segmentations and/or labelmap volumes overlaid on it.</p>

---
