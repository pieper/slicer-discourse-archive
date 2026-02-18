# Samsung SonoAce 4D ultrasound mvl file loading

**Topic ID**: 12452
**Date**: 2020-07-09
**URL**: https://discourse.slicer.org/t/samsung-sonoace-4d-ultrasound-mvl-file-loading/12452

---

## Post #1 by @zurgany (2020-07-09 00:30 UTC)

<p>Hi,<br>
Thank you for accepting me!<br>
I am new here, I am trying to import dicom files from a Samsung sonoace machine, but I am getting error!<br>
Thank you!</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35009b97113023e9f1b9070efce7c1cd6eedc1b8.jpeg" alt="3dslicer error" data-base62-sha1="7ySBHtgJAU45Mg4EvdrY1ynVeEE" width="510" height="149"></p>

---

## Post #2 by @lassoan (2020-07-09 00:38 UTC)

<p>Try loading it with most recent Slicer Preveiew Release.</p>
<p>If that does not work either then please provide us an example image. Preferably image some object of known size (not patient image), to avoid patient privacy issues and so that we can verify correct sizing. Upload the file somewhere and just post the link here.</p>

---

## Post #3 by @zurgany (2020-07-09 01:13 UTC)

<p>Yes, that was the latest preview.<br>
The study contains all kinds of files!<br>
.MVL<br>
.3DH<br>
.BMP<br>
.CNE<br>
and files without extension which I assume are the dicom files.<br>
The DICOM files size is about 2.3 Meg.<br>
I tried the .MVL files, but all I got was horizontal lines!<br>
I will try removing personal data and put the folder on google drive and share it later!</p>
<p>Best regards,<br>
Jabbar Ali</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d83cf585a413e17b572258abae9d9ef5bb23fd37.jpeg" data-download-href="/uploads/short-url/uQVJKbTUvSIQIFkl0Y4DgBqSq47.jpeg?dl=1" title="3dslicer mvl.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d83cf585a413e17b572258abae9d9ef5bb23fd37_2_690x388.jpeg" alt="3dslicer mvl.jpg" data-base62-sha1="uQVJKbTUvSIQIFkl0Y4DgBqSq47" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d83cf585a413e17b572258abae9d9ef5bb23fd37_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d83cf585a413e17b572258abae9d9ef5bb23fd37_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d83cf585a413e17b572258abae9d9ef5bb23fd37_2_1380x776.jpeg 2x" data-dominant-color="666670"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3dslicer mvl.jpg</span><span class="informations">3840×2160 1 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @zurgany (2020-07-09 01:56 UTC)

<p>Thank you very much for your reply!<br>
I forgot to add a link to the MVL file I used in that screenshot!<br>
Here is the link:<br>
<a href="https://drive.google.com/file/d/1pG72s4rrLHN1T167HsakNsy8cl6bNbZE/view?usp=sharing" rel="nofollow noopener">https://drive.google.com/file/d/1pG72s4rrLHN1T167HsakNsy8cl6bNbZE/view?usp=sharing</a><br>
I really appreciate your help!</p>

---

## Post #5 by @lassoan (2020-07-09 02:31 UTC)

<p>You can find instructions for loading Samsung mvl files here: <a href="https://discourse.slicer.org/t/new-extension-rawimageguess-for-loading-of-images-from-unrecognized-file-format/9219" class="inline-onebox">New extension: RawImageGuess - for loading of images from unrecognized file format</a></p>

---

## Post #6 by @zurgany (2020-07-09 02:41 UTC)

<p>Thank you very much!<br>
Yes, I do have this extension, It gives same results like in the screenshot.<br>
Jay</p>

---

## Post #7 by @zurgany (2020-07-09 03:16 UTC)

<p>Thanks a lot!<br>
I am sure you are aware of this software.<br>
Searching on the internet, I found this website:<br>
</p><aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://3dprintedultrasounds.com/wp-content/uploads/2017/07/cropped-2017-10-12-32x32.png" class="site-icon" width="16" height="16">
      <a href="https://3dprintedultrasounds.com/baby-slice-o-software/" target="_blank" rel="nofollow noopener">3dprintedultrasounds.com</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="16" height="16">

<h3><a href="https://3dprintedultrasounds.com/baby-slice-o-software/" target="_blank" rel="nofollow noopener">BabySliceO ultrasound conversion software to print 3D baby models</a></h3>

<p>BabySliceO ultrasound to stl conversion software enables you to convert ultrasound data sets from most manufacturers in 3D files that can be printed on any 3D printer for the creation of 3D baby models.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
I wonder, how did they manage to open MVL files?<br>
Thank you,<br>
Jay

---

## Post #8 by @lassoan (2020-07-09 13:32 UTC)

<p>You can load these files with a few minute of work (as shown in the RawImageGuess module demo video).</p>
<p>If you want to access these files more conveniently then you can find a student or developer who can analyze the file format and develop a reader for it with a few days of work (it is much faster if you can get the file format specification from Samsung). You can also buy BabySliceO, but as far as I know it it costs a few thousand $ and it cannot export the file into an open format, so you can only view/process it in that software.</p>

---

## Post #9 by @zurgany (2020-07-09 13:41 UTC)

<p>I really appreciate your efforts, thank you very much!<br>
I just want to know if the mvl files I have worth the effort, I don’t know if they have the necessary information to generate a 3d model!<br>
I watched the demo video and tried myself, but couldn’t reach anywhere!<br>
Were you able to download the MVL file?<br>
<a href="https://drive.google.com/file/d/1pG72s4rrLHN1T167HsakNsy8cl6bNbZE/view?usp=sharing" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/file/d/1pG72s4rrLHN1T167HsakNsy8cl6bNbZE/view?usp=sharing</a><br>
Thank you again<br>
Jay</p>

---

## Post #10 by @lassoan (2020-07-09 17:41 UTC)

<p>You can load the volume with these parameters (I determined by moving the sliders one by one, as explained in the video):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9d73f48f1baeeed2819d99b661c403cbdfde2ef.jpeg" data-download-href="/uploads/short-url/oetRaiVhKs8Dp8peud5iESSpqDZ.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9d73f48f1baeeed2819d99b661c403cbdfde2ef_2_690x419.jpeg" alt="image" data-base62-sha1="oetRaiVhKs8Dp8peud5iESSpqDZ" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9d73f48f1baeeed2819d99b661c403cbdfde2ef_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9d73f48f1baeeed2819d99b661c403cbdfde2ef_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9d73f48f1baeeed2819d99b661c403cbdfde2ef_2_1380x838.jpeg 2x" data-dominant-color="A7A4A5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2254×1370 787 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>You can load the image very easily by placing the header file that RawImageGuess module generates (<a href="https://1drv.ms/u/s!Arm_AFxB9yqHu70NgbUTmP7yvKe1sA?e=gGYN5q">SingleVolume.nhdr</a>) into the same folder as your image file (1.mvl) and drag-and-dropping this header file on the the Slicer application window.</p>

---

## Post #11 by @zurgany (2020-07-09 18:08 UTC)

<p>Mr. Andras,<br>
You are very talented! I am so glad that my file really has information.<br>
I did reach the 512 value on the x dimension, but could not determine the rest!<br>
I will try with different files and see where I can reach!</p>
<p>I have contacted Samsung and asked for a viewer to open the MVL files, their USA representative promised to help.</p>

---

## Post #12 by @lassoan (2020-07-09 18:14 UTC)

<p>I’ve also found a 4D sequence in the file (you can read it with <a href="https://1drv.ms/u/s!Arm_AFxB9yqHu70Ow3KQa3Lt5hNJIQ?e=z0tLjv">Movie4D.seq.nhdr</a> header):</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55a8b46f30a8727544dfe6e5954c7eb9f08dba91.gif" alt="SlicerCapture" data-base62-sha1="cdM24ow5H6u8XdHswKwr4QIL78Z" width="354" height="352"></p>

---

## Post #13 by @zurgany (2020-07-09 18:19 UTC)

<p>Amazing!<br>
My wife is the sonographer, I am a mechanical engineer, I am trying to 3d print the babies, but it is a really long process  for me!<br>
Again, That is an amazing work an relatively short time!</p>

---

## Post #14 by @lassoan (2020-07-09 19:06 UTC)

<aside class="quote no-group" data-username="zurgany" data-post="13" data-topic="12452">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/c5a1d2/48.png" class="avatar"> zurgany:</div>
<blockquote>
<p>My wife is the sonographer, I am a mechanical engineer, I am trying to 3d print the babies, but it is a really long process for me!</p>
</blockquote>
</aside>
<p>Ultrasound image segmentation is hard, as there is lots of noise in the image and surfaces are blurry. Also, the images are usually incomplete due to acoustic shadowing and limited field of view.</p>
<p>That’s why professional baby 3D printing services employ artists, who warp existing generic baby 3D models to the surface patches visible on ultrasound. This way they always get a full and realistic image, with visible details taken from the actual baby. This is not an easy skill to learn and it involves image segmentation (in 3D Slicer) and 3D modeling (Blender, Rhino, etc.), but the results are amazing.</p>

---

## Post #15 by @zurgany (2020-07-09 23:37 UTC)

<p>I was following this video</p><div class="youtube-onebox lazy-video-container" data-video-id="UHq0uyDvhaA" data-video-title="View your baby ultrasound and create 3D printable model using free software" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=UHq0uyDvhaA" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/UHq0uyDvhaA/maxresdefault.jpg" title="View your baby ultrasound and create 3D printable model using free software" width="" height="">
  </a>
</div>
<p>
But at segment editor, I couldn’t find “Create surface”<br>
Is it not available in the latest version? Or, probably moved somewhere?</p>
<p>Thank you!</p>

---

## Post #16 by @muratmaga (2020-07-10 00:51 UTC)

<p>That video is almost 3 years old. THe button now says “Show 3D”.</p>

---

## Post #17 by @zurgany (2020-07-10 01:07 UTC)

<p>Thank you very much!</p>
<p>Best regards,<br>
Jabbar Ali</p>

---

## Post #18 by @zurgany (2020-07-10 02:07 UTC)

<p>But, why are steps after create surface which is now show 3D, these steps do not work! I couldn’t see a 3d similar to the video and also was not able to use, or get results from, for example, scissors, Erase and so on??<br>
Thank you,</p>

---
