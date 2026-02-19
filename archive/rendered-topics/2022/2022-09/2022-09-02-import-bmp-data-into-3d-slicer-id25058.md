---
topic_id: 25058
title: "Import Bmp Data Into 3D Slicer"
date: 2022-09-02
url: https://discourse.slicer.org/t/25058
---

# Import bmp data into 3D Slicer

**Topic ID**: 25058
**Date**: 2022-09-02
**URL**: https://discourse.slicer.org/t/import-bmp-data-into-3d-slicer/25058

---

## Post #1 by @Trailer (2022-09-02 20:50 UTC)

<p>Hello,</p>
<p>I am brand new to slicer 3D.  I have a series of .bmp images from a micro-ct from bruker (skyscan).</p>
<p>I am trying to import them into slicer 3D but keep getting the error:</p>
<p><code>Error: Loading C:/Users/tommy/Desktop/images/1_image0000_voi__bin_0550.bmp -  load failed.</code></p>
<p>Cant slicer3D load <code>.bmp</code> images? Am I  missing something?</p>
<p>I clicked on <code>Data</code> → <code>Choose Files(s) to Add</code> → loaded a file → ticked <code>Show Options</code> → unticked <code>Single File</code></p>
<p>Kind Regards</p>

---

## Post #2 by @lassoan (2022-09-02 22:33 UTC)

<p>I’ve just tested this and in the latest Slicer Stable Release (Slicer-5.0.3) and it worked well. Most likely that the issue is that one of the bmp files in the folder have different size or their naming scheme cannot be detected automatically.</p>
<p>To load image stacks, I would recommend to use ImageStacks module in SlicerMorph extension, as it is much faster, more robust, and offers quick preview and cropping.</p>

---

## Post #3 by @Trailer (2022-09-03 11:07 UTC)

<p>Hello Mr Lasso,</p>
<p>Unfortunatly, I am not able to it. I noticed that I cannot even import 1 image.<br>
I had to convert the images with imageJ to another format (tiff) and then I could load them into slicer3D.<br>
Thanks for the help</p>

---

## Post #4 by @lassoan (2022-09-03 12:55 UTC)

<p>Can you upload a few example bmp images somewhere and post the link here?</p>

---

## Post #5 by @Trailer (2022-09-03 16:08 UTC)

<p>I will leave one example here: <a href="https://we.tl/t-5fB1PlRsIY" class="inline-onebox" rel="noopener nofollow ugc">WeTransfer - Send Large Files &amp; Share Photos Online - Up to 2GB Free</a></p>
<p>Thanks for the support!</p>

---

## Post #6 by @ebrahim (2022-09-05 02:09 UTC)

<p>I tried this image and also got it to fail to load in Slicer. It seems to be a bit depth issue:</p>
<ul>
<li>The bmp <a class="mention" href="/u/trailer">@Trailer</a> shared has a bit depth of 1.</li>
<li>Converting the image to 24 bit or 256 bit BMP made it load into slicer without trouble</li>
<li>Probably Slicer uses <code>vtkBMPReader</code> to read the image, and when I feed the original image into a program that only calls vtkBMPReader I get the error<pre data-code-wrap="txt"><code class="lang-nohighlight">2022-09-04 22:02:36.386 (   0.005s) [        DED6B780]       vtkBMPReader.cxx:212    ERR| vtkBMPReader (0x55aadaaf69d0): Only BMP depths of (8,24) are supported. Not 1
</code></pre>
So it’s vtkBMPReader’s limitation, but Slicer is still failing to report this error message properly. In Slicer I just get<pre data-code-wrap="txt"><code class="lang-nohighlight">Error: Loading /home/ebrahim/Desktop/image_770.bmp -  load failed.
</code></pre>
rather than the informative VTK error. So the error reporting aspect is a Slicer issue</li>
</ul>

---

## Post #7 by @lassoan (2022-09-05 12:39 UTC)

<p>Slicer uses ITK to load images. You can report this to ITK to see if they are willing to extend ITK to support such bmp images. Since bmp format is rarely used nowadays and binary variant is even more of a niche, they will probably not give high priority for this development, so you might need to wait for some funded project to require this, or contribute developer time or funding yourself. I would recommend exporting in a more commonly used file format, such as png or tiff.</p>

---

## Post #8 by @Hao_Li (2022-09-05 19:32 UTC)

<p><a class="mention" href="/u/trailer">@Trailer</a> Hi, I happen to work with skyscan and 3d slicer. I did a work around and Downloaded a DICOM converter. Then import DICOM. Or use image j, open bmp sequence and save as nrrd file.</p>

---

## Post #9 by @lassoan (2022-09-06 00:39 UTC)

<p>SlicerMorph has a <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/SkyscanReconImport">Skyscan importer module</a> it may worth a try.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> do you have any advice on reading such images?</p>

---

## Post #10 by @muratmaga (2022-09-06 17:49 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="25058">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> do you have any advice on reading such images?</p>
</blockquote>
</aside>
<p>Unfortunately no. Never worked with binary BMPs before.</p>

---
