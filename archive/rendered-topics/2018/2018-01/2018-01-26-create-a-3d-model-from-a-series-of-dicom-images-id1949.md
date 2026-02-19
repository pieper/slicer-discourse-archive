---
topic_id: 1949
title: "Create A 3D Model From A Series Of Dicom Images"
date: 2018-01-26
url: https://discourse.slicer.org/t/1949
---

# Create a 3D model from a series of DICOM images

**Topic ID**: 1949
**Date**: 2018-01-26
**URL**: https://discourse.slicer.org/t/create-a-3d-model-from-a-series-of-dicom-images/1949

---

## Post #1 by @Philip_Miller_MD (2018-01-26 20:09 UTC)

<p>Operating system: Windows 10<br>
Slicer version: the latest<br>
Expected behavior:  create a 3D model from DICOM images…that were created by converting jpgs into dicom<br>
Actual behavior: Each dicom image got imported as if it were it’s own patient.  So, 26  new patients with a series of 1 dicom image as opposed to 1 patient with a series of 26 dicom images.  I need the later to make a 3 d image.</p>

---

## Post #2 by @pieper (2018-01-26 20:39 UTC)

<p>A lot depends on what tool you use to convert jpg to dicom.</p>
<p>Probably better to try loading the jpg files directly:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/FAQ#How_to_load_data_from_a_sequence_of_jpg.2C_tif.2C_or_png_files.3F" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.8/FAQ#How_to_load_data_from_a_sequence_of_jpg.2C_tif.2C_or_png_files.3F</a></p>

---

## Post #3 by @Philip_Miller_MD (2018-01-29 03:15 UTC)

<p>Great. Let me try this</p>

---

## Post #4 by @Philip_Miller_MD (2018-01-29 03:36 UTC)

<p>OK. so I followed the process and the JPGS appeared to load into something but I can’t find them after they are imported and the Volume  does not have a name and I can’t modify any of the settings, they are grayed out.  <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/799132a0e797d6bd345b012f909f61d392413e4e.jpeg" data-download-href="/uploads/short-url/hlqReRUnfyLkTluMPTAJDJLOLDw.jpg?dl=1" title="2018-01-28_22-32-12" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/799132a0e797d6bd345b012f909f61d392413e4e_2_690x491.jpg" alt="2018-01-28_22-32-12" data-base62-sha1="hlqReRUnfyLkTluMPTAJDJLOLDw" width="690" height="491" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/799132a0e797d6bd345b012f909f61d392413e4e_2_690x491.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/799132a0e797d6bd345b012f909f61d392413e4e.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/799132a0e797d6bd345b012f909f61d392413e4e.jpeg 2x" data-dominant-color="AAA9AD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2018-01-28_22-32-12</span><span class="informations">836×596 90.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a213f9b8915d5ac4d819a892330e555058dc4f1c.jpeg" data-download-href="/uploads/short-url/n7O98R6koXNEarlp8VdaWNhZH3K.jpg?dl=1" title="2018-01-28_22-30-58" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a213f9b8915d5ac4d819a892330e555058dc4f1c_2_570x500.jpg" alt="2018-01-28_22-30-58" data-base62-sha1="n7O98R6koXNEarlp8VdaWNhZH3K" width="570" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a213f9b8915d5ac4d819a892330e555058dc4f1c_2_570x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a213f9b8915d5ac4d819a892330e555058dc4f1c_2_855x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a213f9b8915d5ac4d819a892330e555058dc4f1c_2_1140x1000.jpg 2x" data-dominant-color="E4E3E8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2018-01-28_22-30-58</span><span class="informations">1156×1014 416 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @lassoan (2018-01-29 15:50 UTC)

<p>Choose only a <strong>single file</strong> of the sequence. You can find here a video as well:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/UserInterface#How_to_load_data_from_a_sequence_of_jpg.2C_tif.2C_or_png_files.3F" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/UserInterface#How_to_load_data_from_a_sequence_of_jpg.2C_tif.2C_or_png_files.3F</a></p>

---

## Post #6 by @Philip_Miller_MD (2018-01-30 01:47 UTC)

<p>That looked straight forward, but when I tried it, only one image of the 26 loaded. How do I get all of them to load?  <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c64d97e427d557816d30b070a8050eb70a3f0972.jpeg" data-download-href="/uploads/short-url/sigMujRZZ15sjntU5iO4G6r07ke.jpg?dl=1" title="2018-01-29_20-37-39" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c64d97e427d557816d30b070a8050eb70a3f0972_2_690x251.jpg" alt="2018-01-29_20-37-39" data-base62-sha1="sigMujRZZ15sjntU5iO4G6r07ke" width="690" height="251" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c64d97e427d557816d30b070a8050eb70a3f0972_2_690x251.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c64d97e427d557816d30b070a8050eb70a3f0972_2_1035x376.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c64d97e427d557816d30b070a8050eb70a3f0972.jpeg 2x" data-dominant-color="F6F6F6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2018-01-29_20-37-39</span><span class="informations">1183×431 52.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a662e4a4101ab8e25807ce8a12d5574a11e8754.jpeg" data-download-href="/uploads/short-url/aCafLbJhs56cfdsPSw1GtJQEWjO.jpg?dl=1" title="2018-01-29_20-38-55" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a662e4a4101ab8e25807ce8a12d5574a11e8754_2_537x500.jpg" alt="2018-01-29_20-38-55" data-base62-sha1="aCafLbJhs56cfdsPSw1GtJQEWjO" width="537" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a662e4a4101ab8e25807ce8a12d5574a11e8754_2_537x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a662e4a4101ab8e25807ce8a12d5574a11e8754_2_805x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a662e4a4101ab8e25807ce8a12d5574a11e8754.jpeg 2x" data-dominant-color="555561"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2018-01-29_20-38-55</span><span class="informations">822×765 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77f75346552c7c1d5b4b7f0b55ff344df31aaca5.jpeg" data-download-href="/uploads/short-url/h7gI4ZRIAdnCSM0MUvN8eal7RD7.jpg?dl=1" title="2018-01-29_20-41-18" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/77f75346552c7c1d5b4b7f0b55ff344df31aaca5_2_690x447.jpg" alt="2018-01-29_20-41-18" data-base62-sha1="h7gI4ZRIAdnCSM0MUvN8eal7RD7" width="690" height="447" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/77f75346552c7c1d5b4b7f0b55ff344df31aaca5_2_690x447.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77f75346552c7c1d5b4b7f0b55ff344df31aaca5.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77f75346552c7c1d5b4b7f0b55ff344df31aaca5.jpeg 2x" data-dominant-color="E4E5E5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2018-01-29_20-41-18</span><span class="informations">731×474 86.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>see video here:   <a href="https://www.screencast.com/t/eTowM5ypu7fX" rel="noopener nofollow ugc">https://www.screencast.com/t/eTowM5ypu7fX</a></p>
<p>And access to the files here:</p>
<p><a href="https://drive.google.com/open?id=1XhaGbwnN34g8cRzSgk7mJnj7uTJlhjc8" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/open?id=1XhaGbwnN34g8cRzSgk7mJnj7uTJlhjc8</a></p>
<p>I am very grateful for all of your assistance.</p>
<p>PJM</p>

---

## Post #7 by @pieper (2018-01-30 15:31 UTC)

<p>Hi Philip -</p>
<p>Thanks for sharing the data - I can see now the issue is that while the filenames are correct to form a volume, it turns out the files aren’t all the same sizes.  The snippet from the error log below gives the details.</p>
<p>If you know that the files have consistent pixel sizes (acquired at the same scale) then you can crop or pad them all to the same dimensions and then the will load.  From a quick look it’s not clear to me how well they will align in 3D and if there’s enough out of plane resolution to make a good 3D model.</p>
<pre><code class="lang-auto">Description: ImageIO returns IO region that does not fully contain the requested regionRequested region: ImageRegion (0x7ffeefbfc630)
  Dimension: 3
  Index: [0, 0, 0]
  Size: [5672, 3373, 1]
StreamableRegion region: ImageRegion (0x7ffeefbfc668)
  Dimension: 3
  Index: [0, 0, 0]
  Size: [5520, 3548, 1]
</code></pre>
<p>There are lots of ways to manipulate your data with various scripts and applications.  If you want a GUI application and have windows then Irfanview can be a handy tool as shown in this tutorial.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://diaryofdennis.com/2012/07/11/tutorial-converting-batch-rename-and-batch-resize-your-photos-with-irfanview/">
  <header class="source">
      <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e236f592fcf00e1682eb94de4bc786dce749f969.jpeg" class="site-icon" width="32" height="32">

      <a href="https://diaryofdennis.com/2012/07/11/tutorial-converting-batch-rename-and-batch-resize-your-photos-with-irfanview/" target="_blank" rel="noopener" title="03:32PM - 11 July 2012">Diary of Dennis – 11 Jul 12</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:372/330;"><img src="http://diaryofdennis.files.wordpress.com/2012/07/batchconversionrenametut1.jpg?fit=440%2C330" class="thumbnail" width="372" height="330"></div>

<h3><a href="https://diaryofdennis.com/2012/07/11/tutorial-converting-batch-rename-and-batch-resize-your-photos-with-irfanview/" target="_blank" rel="noopener">Tutorial: Converting, Batch Rename and Batch Resize your Photos with IrfanView</a></h3>

  <p>There is often the problem that you took tons of photos you want to use anywhere, for example online but the size of all your photos are too big. Also you are sometimes not happy with the names of …</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>-Steve</p>

---

## Post #8 by @lassoan (2018-01-30 20:14 UTC)

<p>I’ve also noticed that slices seem to be misaligned with each other (there is translation and rotation between neighbor slices). You would need to spatially register slices to each other before you can display it as a 3D volume. I think <a href="http://imagej.net/Fiji">Fiji</a> has such registration tools and it can also save the image stack as an .mha file that Slicer can load directly.</p>

---

## Post #9 by @Philip_Miller_MD (2018-01-30 20:54 UTC)

<p>OK…can I just hire you???   !!</p>

---

## Post #10 by @lassoan (2018-01-30 23:07 UTC)

<aside class="quote no-group" data-username="Philip_Miller_MD" data-post="9" data-topic="1949" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/ac91a4/48.png" class="avatar"> Philip_Miller_MD:</div>
<blockquote>
<p>OK…can I just hire you</p>
</blockquote>
</aside>
<p>It should not be necessary! If this is a one-off case then I (or others who are more experienced in histology slice registration) can create a Slicer-compatible volume for you from the data set that you provided.</p>
<p>If you need to create volumes from slices regularly, then you need to come up with a processing workflow. Slice registration may be a critical point of the workflow, as it may be difficult to find matching points between slices and your sample may also deform while it is being sliced. For now probably your best bet is to either come up with a slicing and imaging protocol that provides aligned slices; or retrospectively align them in Fiji. Later, if you need highly optimized workflow, then probably you would want to have a slice stack registration available in Slicer, so that you can do everything in one software.</p>

---

## Post #11 by @Philip_Miller_MD (2018-02-01 17:20 UTC)

<p>OK…so, I used the first one to get all images of the proper dimension, and then to invert the colors so I could keep white bone and black air.   They imported correctly, but I think all as seperate volumes though they appear to be all linked and I can scorll through them.  BUT, how do I get a volume rendering???</p>
<p>See video.    <a href="https://www.screencast.com/t/vtBM0x1nk" rel="nofollow noopener">https://www.screencast.com/t/vtBM0x1nk</a></p>
<p>Thanks for all of your assistance!</p>

---

## Post #12 by @Philip_Miller_MD (2018-02-01 17:23 UTC)

<p>And…I saved them with this information…if it helps…</p>
            <video title="02.01.2018-12.21.10" width="695" height="616" style="max-width:100%" controls="">
              <source src="https://content.screencast.com/users/pmiller23/folders/Snagit/media/9695d44e-2ffa-4ba1-ab0a-22c8ece93b8c/02.01.2018-12.21.MP4"></source>
            </video>


---

## Post #13 by @lassoan (2018-02-01 18:30 UTC)

<aside class="quote no-group" data-username="Philip_Miller_MD" data-post="11" data-topic="1949">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/ac91a4/48.png" class="avatar"> Philip_Miller_MD:</div>
<blockquote>
<p>how do I get a volume rendering</p>
</blockquote>
</aside>
<p>Go to volume rendering, select your volume, and click the eye icon to show the volume.</p>
<p>Probably the volume will look flat, as by default slice spacing is the same along all axes. To fix that, go to Volumes module, open Volume information section, and set the third value of Image spacing to the higher value (the value should be the same as the space between your image slices, in mm). For correct dimensions within the slice, set the first two values of Image spacing to the size of one pixel (in mm).</p>

---

## Post #14 by @Philip_Miller_MD (2018-02-01 23:39 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d8776e694e5ff4b51c738d2dcbbc88e97e08a02.jpeg" data-download-href="/uploads/short-url/4de4Ps31wG8w2rRHwoyAnh0YiFc.jpg?dl=1" title="Progress" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1d8776e694e5ff4b51c738d2dcbbc88e97e08a02_2_618x500.jpg" alt="Progress" data-base62-sha1="4de4Ps31wG8w2rRHwoyAnh0YiFc" width="618" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1d8776e694e5ff4b51c738d2dcbbc88e97e08a02_2_618x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1d8776e694e5ff4b51c738d2dcbbc88e97e08a02_2_927x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1d8776e694e5ff4b51c738d2dcbbc88e97e08a02_2_1236x1000.jpg 2x" data-dominant-color="81777C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Progress</span><span class="informations">1607×1299 397 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #15 by @pieper (2018-02-02 00:16 UTC)

<p>The right answer for the pixel spacing depends on how the images were acquired and that info is probably not recorded in the jpg files.  Sometimes people include a ruler in the photo for reference and make a note of the spacing of the slice cuts.  Without that you can probably only estimate the size based on an average size of a reference structure.</p>

---

## Post #16 by @Philip_Miller_MD (2018-02-02 01:22 UTC)

            <video title="02.01.2018-20.15.16" width="695" height="498" style="max-width:100%" controls="">
              <source src="https://content.screencast.com/users/pmiller23/folders/Snagit/media/6b3c5716-77e0-4039-86d3-99448067a71d/02.01.2018-20.15.MP4"></source>
            </video>


---

## Post #17 by @Philip_Miller_MD (2018-02-02 01:29 UTC)

<p>Oh, and while we’re at it…I had to save tons of files after I did this…which one woudl I open up to get this all back?</p>

---

## Post #18 by @muratmaga (2018-02-02 04:53 UTC)

<p>If you are still looking for exporting a 3D model after your segmentation, make sure to go to ‘Segmentations’ module, scroll down and find ‘export/import labelmaps/models’ section.<br>
Choose your segment that has your segmentation and export is a model file.<br>
After that use regular Save As to save your model (it defaults to VTK polygon format, change it to stl/ply/obj)</p>
<p>M</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/677f06bdf711468707faf594c72c7993f90d2513.png" data-download-href="/uploads/short-url/eLzkAGZovUCazoJL65K1uagmWFJ.png?dl=1" title="77C3A3DB5AF54B56A741600A3E5A8000.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/677f06bdf711468707faf594c72c7993f90d2513.png" width="690" height="0" data-dominant-color="BFCDDB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">77C3A3DB5AF54B56A741600A3E5A8000.png</span><span class="informations">708×1 83 Bytes</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #19 by @Philip_Miller_MD (2018-02-03 01:41 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7ee7011967f1902b865b5a3de0d719f83b19a444.jpeg" data-download-href="/uploads/short-url/i6D5jpdiWYSUHULbZxXfiaG9cFe.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7ee7011967f1902b865b5a3de0d719f83b19a444_2_374x500.jpeg" alt="image" data-base62-sha1="i6D5jpdiWYSUHULbZxXfiaG9cFe" width="374" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7ee7011967f1902b865b5a3de0d719f83b19a444_2_374x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7ee7011967f1902b865b5a3de0d719f83b19a444_2_561x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7ee7011967f1902b865b5a3de0d719f83b19a444_2_748x1000.jpeg 2x" data-dominant-color="8C8780"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2138×2851 1.11 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>I press export and nothing happens.</p>

---

## Post #20 by @Philip_Miller_MD (2018-02-03 01:48 UTC)

<p>And when I try to save there is no .obj option <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01f060e905189d5259dc171dc1096adbed213621.jpeg" data-download-href="/uploads/short-url/h9u8Lj4jhZxEsHyQgCFuiJU5Kp.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01f060e905189d5259dc171dc1096adbed213621_2_666x500.jpeg" alt="image" data-base62-sha1="h9u8Lj4jhZxEsHyQgCFuiJU5Kp" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01f060e905189d5259dc171dc1096adbed213621_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01f060e905189d5259dc171dc1096adbed213621_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01f060e905189d5259dc171dc1096adbed213621_2_1332x1000.jpeg 2x" data-dominant-color="A3A19E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">4032×3024 2.89 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #21 by @muratmaga (2018-02-03 02:39 UTC)

<p>It is normal that there is no OBJ option, because it didn’t export your polygonial model in the previous step. Are you sure the segment you are trying to export model from is the same that you did your segmentation on? Please review the segment selection at the top of the page on the ‘Segmentation’ module. I can’t think why it would be blank otherwise?</p>
<p>It is always harder to learn a workflow with a new datasets. Because you are not certain whether it is failing for your specific dataset or you are skipping steps.</p>
<p>Did you try this video tutorial? You can replace their spine segment data with a built-in data from Slicer’s sample data distribution (e.g. chest CT would work as a test)</p>

---

## Post #22 by @Philip_Miller_MD (2018-02-03 18:39 UTC)

<p>I was able to finally see it as a file to save and converted it to .obj, but was surprised to see that it was exported as only a 1kb file…And this was formed from 26  layers of 2MB slices…  What else might I be doing wrong??<br>
Which video tutorial?   And where do I go for the best tutorials for this?</p>

---

## Post #23 by @Philip_Miller_MD (2018-02-03 19:07 UTC)

<p>I got it…I had  forgotten to color the segment.  Now it should do it OK…At last it’s taking really Lon time to render!!!</p>

---

## Post #24 by @muratmaga (2018-02-04 05:03 UTC)

<p>Sorry forgot to paste the link to the tutorial. I think you should do the segment editor tutorial and watch this</p>
<aside class="quote quote-modified" data-post="1" data-topic="700">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-video-tutorial-for-segment-editor-lumbar-spine-segmentation-for-3d-printing/700">New video tutorial for Segment editor - lumbar spine segmentation for 3D printing</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    This is the first part of a video tutorial series that teaches how to use Segment editor. This tutorial explains how to create a 3D-printable lumbar spine segment that can be used for lumbar puncture training: 

The video tutorial was created by Hilary Lia (PerkLab, Queen’s University), with help from <a class="mention" href="/u/cpinter">@cpinter</a>, <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/ungi">@ungi</a>. 
Please post your comments here about how useful this tutorial format is, what did you like/what to improve, what topics/techniques/anatomical structures you would be int…
  </blockquote>
</aside>
<p><a href="http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html" class="onebox" target="_blank" rel="noopener">http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/677f06bdf711468707faf594c72c7993f90d2513.png" data-download-href="/uploads/short-url/eLzkAGZovUCazoJL65K1uagmWFJ.png?dl=1" title="77C3A3DB5AF54B56A741600A3E5A8000.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/677f06bdf711468707faf594c72c7993f90d2513.png" width="690" height="0" data-dominant-color="BFCDDB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">77C3A3DB5AF54B56A741600A3E5A8000.png</span><span class="informations">708×1 83 Bytes</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
