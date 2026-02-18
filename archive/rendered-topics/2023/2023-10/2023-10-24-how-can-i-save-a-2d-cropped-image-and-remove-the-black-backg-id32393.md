# How can I save a 2D cropped image and remove the black background?

**Topic ID**: 32393
**Date**: 2023-10-24
**URL**: https://discourse.slicer.org/t/how-can-i-save-a-2d-cropped-image-and-remove-the-black-background/32393

---

## Post #1 by @Kelly_Lee (2023-10-24 05:17 UTC)

<p>I have cropped an image using the “crop volume” function, and now I want to save it as a 2D image in a PNG file. How can I save it, and make sure that the background isn’t black like in the image? thanks!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92c9943dba99e4f0b5747df99a3c869a4741a805.png" data-download-href="/uploads/short-url/kWxAH38E7CVkF8YF0uRhbbqeAGV.png?dl=1" title="TEST" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92c9943dba99e4f0b5747df99a3c869a4741a805_2_527x499.png" alt="TEST" data-base62-sha1="kWxAH38E7CVkF8YF0uRhbbqeAGV" width="527" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92c9943dba99e4f0b5747df99a3c869a4741a805_2_527x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92c9943dba99e4f0b5747df99a3c869a4741a805_2_790x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92c9943dba99e4f0b5747df99a3c869a4741a805.png 2x" data-dominant-color="010101"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">TEST</span><span class="informations">949×899 5.54 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-10-24 13:18 UTC)

<p>If you only need it for publication/presentation purposes then you can zoom in and right-click to copy the image to the clipboard. In PowerPoint, Word, etc. you can crop it further.</p>
<p>If you want to export the image for further processing or analysis then you can right-click on the image and choose “Export to file…”. If your image is 2D then you can save as .png. If it is a 3D image then it can be saved in a 3D image file format, such as .nrrd.</p>

---

## Post #3 by @Kelly_Lee (2023-10-25 00:22 UTC)

<p>Thank you for your response. I’d like to ask you why I don’t have the “Export to file…” option when I right-click. Thanks again.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0b4eec55440c5c14a7f7e7fca582981bf34439f.png" alt="圖片1" data-base62-sha1="ruLjTkkRcUeNkiZxIIYyGYXvrz1" width="499" height="442"></p>

---

## Post #4 by @lassoan (2023-10-25 01:09 UTC)

<p>“Export to file” is available in the right-click menu in the data tree in Data module.</p>

---

## Post #5 by @Kelly_Lee (2023-10-25 02:22 UTC)

<p>Thank you for your response. However, when I choose to export the Crop Volume, an “Export error” occurs. (I want to analyze the images and save them as simple 2D images without any enlargement in PNG format.) Thank you again for your response.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/121892d43f834976f329016d6badabbad0a6ff28.png" alt="Q3" data-base62-sha1="2A5f4jFDQEdtJmg4sNnjMhmt5dm" width="621" height="409"></p>

---

## Post #6 by @lassoan (2023-10-26 04:59 UTC)

<p>Most medical images use 16 bits per voxel, while jpg only works with 8, so you won’t be able to use this file format (unless you rescale or cast your image, risking significant information loss). If you really abosolutely must use 2D image stacks then you can choose TIFF format, but that would mean you lose image spacing and axes orientation information. I would strongly recommend to save your image in a proper 3D file format (so that you can later load the image without any information loss). You can easily load nrrd images in Python using pynrrd.</p>

---

## Post #7 by @Kelly_Lee (2023-10-26 07:55 UTC)

<p>Thank you very much for your response.</p>

---
