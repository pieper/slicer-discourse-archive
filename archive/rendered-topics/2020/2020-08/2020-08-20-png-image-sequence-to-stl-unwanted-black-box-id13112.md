# PNG image sequence to STL - Unwanted Black Box

**Topic ID**: 13112
**Date**: 2020-08-20
**URL**: https://discourse.slicer.org/t/png-image-sequence-to-stl-unwanted-black-box/13112

---

## Post #1 by @vincent.serantoni (2020-08-20 12:56 UTC)

<p>Hello everyone !</p>
<p>I’m a new user of 3D Slicer.<br>
For my purpose, I have an image sequence of png (uint8 - one example hereafter) image representing a bone. These image are black for the background (0) and white (255) for the bone I’m working with. Therefore I only have 2 colour in each slice (this image sequence represent a thersholding of the complete image sequence).<br>
I want to extract the bone in an .stl format. However, even after following many tutorial, I still have some issue.</p>
<p>The first one, and I think the biggest one, is that when I activate the volume rendering, all the black of the image sequence is shown. Therefore I have a solid black box around my bone (see attached image).</p>
<p>The second issue is that, using the thersholding tool in the editor menu, I’m not able to extract a readable stl file of the bone…</p>
<p>Do you have any idea ?<br>
Thank you !</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1ab1c34ec1c574cb49e98dfebc1ffddf298957f.png" data-download-href="/uploads/short-url/rDgKJ78xqr09PO6QSA7momNZICP.png?dl=1" title="Issue_3DSlicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1ab1c34ec1c574cb49e98dfebc1ffddf298957f_2_690x443.png" alt="Issue_3DSlicer" data-base62-sha1="rDgKJ78xqr09PO6QSA7momNZICP" width="690" height="443" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1ab1c34ec1c574cb49e98dfebc1ffddf298957f_2_690x443.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1ab1c34ec1c574cb49e98dfebc1ffddf298957f_2_1035x664.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1ab1c34ec1c574cb49e98dfebc1ffddf298957f_2_1380x886.png 2x" data-dominant-color="1D1D21"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Issue_3DSlicer</span><span class="informations">1432×920 49.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a52ab881ad7d2e27a5075054adc23aeb7e6f8626.png" data-download-href="/uploads/short-url/nz8jiSA9bWhIMiFIxC6PzQ8I690.png?dl=1" title="6Min_of_6Max_0000" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a52ab881ad7d2e27a5075054adc23aeb7e6f8626.png" alt="6Min_of_6Max_0000" data-base62-sha1="nz8jiSA9bWhIMiFIxC6PzQ8I690" width="266" height="500" data-dominant-color="101010"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">6Min_of_6Max_0000</span><span class="informations">801×1501 1.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Alex_Vergara (2020-08-20 14:05 UTC)

<p>Just use the Shift slider in the Volume rendering module, move it to the right all the way.</p>

---

## Post #3 by @vincent.serantoni (2020-08-20 14:17 UTC)

<p>Thank you Alex for the proposition. However this solution is not working at all…</p>

---

## Post #4 by @lassoan (2020-08-20 14:53 UTC)

<p>This is a labelmap volume (voxels are labels are not continuous scalars) and you need to indicate this to Slicer, as presets and operations for scalar volumes are different for scalar and labelmap volumes.</p>
<p>You can convert the image to model by following these steps:</p>
<ul>
<li>load the image as labelmap volume (in Add data dialog, click “Show options” and check Labelmap) - by the way, this will also make Volume rendering work immediately, without the need to tune any settings</li>
<li>Go to Data module</li>
<li>Right-click on the volume and choose to convert to segmentation</li>
<li>Right-click on the segmentation and choose to convert to model</li>
</ul>

---

## Post #5 by @vincent.serantoni (2020-08-20 17:21 UTC)

<p>Thank you for your answer.</p>
<p>However, when I import my data I deselect “single Image” and I activate “Labelmap”. But now nothing at all is happening…<br>
It seems that the option “Labelmap” is killing the loading of the images.</p>

---

## Post #6 by @lassoan (2020-08-20 17:27 UTC)

<p>“Single image” force loading a single file. If you have the volume in a list of PNGs then you must keep “Single image” option unchecked.</p>
<p>By the way, where these PNGs come from? It would be much better to save the volume properly, as a 3D nrrd or mha file, instead of storing as a list of 2D files (which has many problems, for example there is no standard way of storing 3D position, orientation, and spacing of slices).</p>

---

## Post #7 by @issakomi (2020-08-20 17:44 UTC)

<p>That image above is PNG of type “indexed color” (2 colors). In another app it loads as RGB, in Slicer as vector volume. May be converting to grey-scale image could help.</p>

---

## Post #8 by @vincent.serantoni (2020-08-21 07:16 UTC)

<p>Thank you,</p>
<p>Using ImageJ I was able to convert this image sequence into an nrrd file and now everything is working well on Slicer !</p>

---

## Post #9 by @lassoan (2020-08-21 18:04 UTC)

<p>Where do the images come from? Developers of that software should be made aware that saving a 3D volume as a PNG series is very bad practice (see <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumes.html#load-a-series-of-png-jpeg-or-tiff-images-as-volume">this note</a>) and they should implement proper saving into a 3D file format instead.</p>

---
