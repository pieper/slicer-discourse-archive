# Importing PBS files 

**Topic ID**: 18401
**Date**: 2021-06-29
**URL**: https://discourse.slicer.org/t/importing-pbs-files/18401

---

## Post #1 by @manuela_lizarazu (2021-06-29 16:13 UTC)

<p>Slicer version: 4.11</p>
<p>Can PSB files be uploaded into slicer? I am working with photoshop and I have 96 images with 4800 pixels each, a really big file (PBS file is the only saving option I have), and I need to import it into slicer. What would be the easiest way to do this?</p>

---

## Post #2 by @lassoan (2021-06-30 02:17 UTC)

<p>Slicer (and I guess most if not all other open-source software) will not be able to open proprietary file formats, such as Adobe’s PSB. If Photoshop itself cannot save it in an open file format then you probably need to crop the image in Photoshop and save piece by piece (or resize the image so that you can save it as one file).</p>
<p>How did you end up with having large images in Photoshop? Did you try to stitch microscopy or microCT images in Photoshop?</p>

---

## Post #3 by @manuela_lizarazu (2021-06-30 02:27 UTC)

<p>I scanned histology slides using EPSON V19. I need a really high resolution to be able to see what I need in the image, reason why they are really big. I am going to try to separate them and save them as Tiffs files and then try to upload all of them into Slicer. I think this would be the only way to not lose resolution and be able to read into slider. If there are more ideas please let me know, I am happy to try everything to make this work.</p>
<p>I have not try to stitch microscopy or microCT images, but knowing that I can’t lose resolution do you think this would be a good idea? If so, how can I get this done?</p>
<p>Thanks!</p>
<p>El El mar, jun. 29, 2021 a la(s) 9:17 p. m., Andras Lasso via 3D Slicer Community &lt;<a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a>&gt; escribió:</p>

---

## Post #4 by @lassoan (2021-06-30 02:42 UTC)

<p>Have you tried to scan and save images into all supported file formats (tiff, jpeg, png, bmp, …) using the software that came with your scanner? There are also many third-party scanning software that you may try. You might get help tips for high-resolution scanning on the <a href="https://forum.image.sc/t/welcome-to-the-imagej-forum/8">ImageJ forum</a>, as many people in that community use flatbed scanners to acquire high-resolution images.</p>

---
