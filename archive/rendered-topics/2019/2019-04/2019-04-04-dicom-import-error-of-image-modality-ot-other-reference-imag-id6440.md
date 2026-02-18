# DICOM import error of image modality OT ("other"): ‘Reference image in series does not contain geometry information.’

**Topic ID**: 6440
**Date**: 2019-04-04
**URL**: https://discourse.slicer.org/t/dicom-import-error-of-image-modality-ot-other-reference-image-in-series-does-not-contain-geometry-information/6440

---

## Post #1 by @crisrubio23 (2019-04-04 10:10 UTC)

<p>Hello, I’m trying to get the 3D image of an OT of a mouse from DICOM images but this error also appears, could anyone help me? In case it was different, I tried the option load data (with .bmp extension) but it didn’t work.<br>
Here there are some images: <a href="https://www.dropbox.com/sh/rdr9hq70n7dsjx1/AADQr5k8VC7HycAhkZExHGe5a?dl=0" rel="nofollow noopener">https://www.dropbox.com/sh/rdr9hq70n7dsjx1/AADQr5k8VC7HycAhkZExHGe5a?dl=0</a></p>
<p>Thank you so much</p>

---

## Post #2 by @pieper (2019-04-04 21:16 UTC)

<p><a class="mention" href="/u/crisrubio23">@crisrubio23</a> -</p>
<p>Thanks for sharing the data - the dicom headers on those are very minimal and not really valid.  Like the error message says, there’s no geometry information so they cannot be converted to a volume.  You probably need to see if you can get the data in a different format or write a small script to convert them to something like nrrd.</p>

---

## Post #3 by @crisrubio23 (2019-04-08 08:51 UTC)

<p>Thank you for the reply! The original images where with extension .bmp but when I tried to upload them to the software, in order to visualize something, I needed to upload just one image (selecting the volume option, instead of scalar, and without selecting the option single image). This way I was able to see something on the screen. However, when selecting volume rendering an image like eddyogi appeared… Why does this happen? Is it because I need better images?<br>
Here is the data in .bmp: <a href="https://www.dropbox.com/sh/sf3acdykxdnyfg6/AABjcAewntuBd2F-Nff0AlBVa?dl=0" rel="nofollow noopener">https://www.dropbox.com/sh/sf3acdykxdnyfg6/AABjcAewntuBd2F-Nff0AlBVa?dl=0</a></p>

---

## Post #4 by @lassoan (2019-04-08 20:21 UTC)

<p>In your DICOM data sets, image modality is set to OT (“other”), which means that it is not image data.</p>
<aside class="quote no-group" data-username="crisrubio23" data-post="3" data-topic="6440">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/f04885/48.png" class="avatar"> crisrubio23:</div>
<blockquote>
<p>when selecting volume rendering an image like eddyogi appeared…</p>
</blockquote>
</aside>
<p>What is “eddyogi”??</p>
<p>A few issues with your BMP files:</p>
<ul>
<li>Your BMP images store grayscale image as contain 24-bit RGB image, so before you do any processing or volume rendering, you need to convert it to a simple scalar volume using Vector to Scalar volume module.</li>
<li>BMP files store image intensity on 8 bits, while you typically need &gt;12 bits for storing full dynamic range of CT images. Reduced dynamic range means that if you change window/level of the volume then the image will appear much noisier and/or details will be lost.</li>
<li>Volume rendering of a 1GB data set may require high-end graphics hardware. You may consider using Crop volume module to crop the image to the region of interest and/or make voxel size larger by a factor of 2 to 4 along each axis (set Spacing scale parameter to 4; if that works, you can try smaller values).</li>
</ul>
<p>Volume rendering after vector to scalar conversion and resampling by a factor of 4:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed2f51f398f866e0f82046ba976097b355c1a267.jpeg" data-download-href="/uploads/short-url/xQexGNKpDlE7CfTdQ8cC8MKzhKT.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ed2f51f398f866e0f82046ba976097b355c1a267_2_690x373.jpeg" alt="image" data-base62-sha1="xQexGNKpDlE7CfTdQ8cC8MKzhKT" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ed2f51f398f866e0f82046ba976097b355c1a267_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ed2f51f398f866e0f82046ba976097b355c1a267_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ed2f51f398f866e0f82046ba976097b355c1a267_2_1380x746.jpeg 2x" data-dominant-color="7B7A7E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 529 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I would recommend to ask developers of the software that generated these DICOM files to use CT imaging modality instead and include all mandatory DICOM fields of <a href="http://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_A.3.3.html">CT Image IOD</a>. If this is too hard for them, then they may implement exporting to .nrrd of .mha format instead. They could also try to export into 16-bit TIFF file format (not ideal, due to no widely used standard for specifying 3D image geometry).</p>

---

## Post #5 by @muratmaga (2019-04-09 04:02 UTC)

<p><a class="mention" href="/u/crisrubio23">@crisrubio23</a><br>
Is this dataset from Bruker/Skyscan microCT (that’s the only microCT with default image format as BMP that I am aware of).</p>
<p>If it is, you can try the SkyscanReconImport from our SlicerMorph project. Unfortunately, it is not an official extension yet, but you can download from:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/SlicerMorph/" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/062a1f25b89185a2de5647b18ceedc3b3565a2bdae6071fa2951662397c17885/SlicerMorph/SlicerMorph" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/SlicerMorph/SlicerMorph/" target="_blank" rel="noopener">GitHub - SlicerMorph/SlicerMorph: Extensions to conduct 3D morphometrics in...</a></h3>

  <p>Extensions to conduct 3D morphometrics in Slicer. Contribute to SlicerMorph/SlicerMorph development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>At least it should help you get your data into Slicer accurately (ie., there should be no artifact that is not originally present in the data). However, <a class="mention" href="/u/lassoan">@lassoan</a>’s comments about intensity ranges still apply.</p>
<p>Also seriously, what is eddyogi? Sounds so cool.</p>

---

## Post #6 by @crisrubio23 (2019-04-11 14:19 UTC)

<p>Thank you so much for the help. I tried this but my mouse doesn’t look as the one that you showed. It looks something like this, like if it was not a solid image, how can I make it solid to be able to edit it (cut different parts and stay only with the ones of interest)?. I have tried resampling at 4 and 3 because with 2 it gave me an error, and varying some parameters from the left and still didn’t work. Do you have any idea of why this happen and how can I solve it? Because I really need to edit the 3D image and in this way it doesn’t let me to make a segmentation…<br>
Thank you again!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/952645ae9b6e385a7ad55c8693db7ab75dc905e3.jpeg" data-download-href="/uploads/short-url/lhr8JBRD3msBFJCdadF1bARNTaj.jpeg?dl=1" title="SlicerImage" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/952645ae9b6e385a7ad55c8693db7ab75dc905e3_2_690x370.jpeg" alt="SlicerImage" data-base62-sha1="lhr8JBRD3msBFJCdadF1bARNTaj" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/952645ae9b6e385a7ad55c8693db7ab75dc905e3_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/952645ae9b6e385a7ad55c8693db7ab75dc905e3_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/952645ae9b6e385a7ad55c8693db7ab75dc905e3_2_1380x740.jpeg 2x" data-dominant-color="9B99A6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerImage</span><span class="informations">1918×1030 516 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Ps: “eddyogi” was another user, I didn’t know how to comment other users <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #8 by @lassoan (2019-04-11 16:38 UTC)

<p>You can tune volume rendering settings to make different regions opaque or transparent. There are many segmentation tools to delineate various structures in your data set.</p>
<p>There is so much you can do with volumetric data and we would be happy to help you with that, but please create new topics for those questions. This topic was about importing the data and it seems to work well.</p>

---
