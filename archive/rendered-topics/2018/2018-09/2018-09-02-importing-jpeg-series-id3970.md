# Importing jpeg series

**Topic ID**: 3970
**Date**: 2018-09-02
**URL**: https://discourse.slicer.org/t/importing-jpeg-series/3970

---

## Post #1 by @opetne (2018-09-02 20:27 UTC)

<p>Dear members,</p>
<p>I have a series of jpeg images from a cat head sections. I wanted to import them as a series. I tried to import as a volume but without a success. After searching a solution, I opened the series in ImageJ and exported as a Nifti file. In ImageJ it looked all perfect but it was strange that the original some 864 MB file became a 4.2GB Nifti file. After opening this in Slicer I got a 3x3 series in bw. The original series were RGB images. What could happened?<br>
The original files had a long and strange name, could it be the reason?</p>
<p>Ors<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44ff26f6e4751009878ecc9112c9a52073751b20.png" alt="sorozat" data-base62-sha1="9Qn808xD7kCCsdu6fWmuztKtvzi" width="353" height="210"></p>

---

## Post #2 by @muratmaga (2018-09-03 15:19 UTC)

<p>Hi<br>
if all your images are all in identical dimensions, you should be able to import them into slicer as a JPEG series. At the load menu, uncheck single file.</p>
<p>I don’t think slicer has a lot of support for RGB images (e.g. you won’t be able to render resultant image in 3d, without coverting to a scalar volume). I am also not sure if segmentation works with RGB images.</p>
<p>What do you want to do in slicer with this dataset?</p>

---

## Post #3 by @pieper (2018-09-03 15:31 UTC)

<p>Slicer tries to guess the image order based on numbers in the filenames, so you may need to give them simpler names like image0001.jpg, image0002.jpg etc.  IrfanView for the pc has a bulk renamer if you don’t have other options (e.g. writing a script).</p>
<p>It makes sense that the uncompressed volume would be so big compared to the jpegs.</p>

---

## Post #4 by @opetne (2018-09-03 16:19 UTC)

<p>Dear Murat,</p>
<p>I tried to import them as a volume as you mentioned but it didn’t work. This is wh, I tried to insert this step with ImageJ.</p>
<p>If I tried just a simple volume import, only one cross section appeared and in sagittal and horizontal view there was nothing.</p>
<p>Ors</p>
<p>Murat Maga <a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a> ezt írta (időpont: 2018. szept. 3., Hét 17:29):</p>

---
