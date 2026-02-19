---
topic_id: 494
title: "Using 3Dslicer For Optical Coherence Tomography St Judes"
date: 2017-06-13
url: https://discourse.slicer.org/t/494
---

# Using 3DSlicer for Optical Coherence Tomography (St Jude's)

**Topic ID**: 494
**Date**: 2017-06-13
**URL**: https://discourse.slicer.org/t/using-3dslicer-for-optical-coherence-tomography-st-judes/494

---

## Post #1 by @Jaytee (2017-06-13 16:06 UTC)

<p>Hi Everyone,</p>
<p>I’m very new to 3D slicer, I just downloaded it to try get some 3D images for a case report but having some trouble.</p>
<p>Not sure if anyone has experience in using the St Jude’s OCT system (used in cardiology for imaging inside the coronary arteries, <a href="https://www.sjm.com/optis/index.html" rel="noopener nofollow ugc">https://www.sjm.com/optis/index.html</a>). This system can export a DICOM file which I’ve then tried loading into 3DSlicer however the ‘DICOM’ importer doesn’t work, when I examine the file it comes up with:<br>
“Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly. Use with caution.  Reference image in series does not contain geometry information.  Please use caution.”</p>
<p>Using the Add Data widget allows the study to load but it doesn’t give a 3D image or allow editing. It does make a volume render which I’ve tried using the ‘Crop Volume’ module but this just crashed the program.</p>
<p>Anyone have any idea of what to do? I’ve posted a quick screenshot below.</p>
<p>Cheers,<br>
Justin</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/fb13dc3df5396f0f88faa5d0ded748c6ef45fe57.png" data-download-href="/uploads/short-url/zP8owM1oSwG27xz4dUoOfyo7R79.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/fb13dc3df5396f0f88faa5d0ded748c6ef45fe57_2_690x376.png" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/fb13dc3df5396f0f88faa5d0ded748c6ef45fe57_2_690x376.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/fb13dc3df5396f0f88faa5d0ded748c6ef45fe57_2_1035x564.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/fb13dc3df5396f0f88faa5d0ded748c6ef45fe57_2_1380x752.png 2x" data-dominant-color="6D696F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">1920×1048 504 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2017-06-13 16:12 UTC)

<aside class="quote no-group" data-username="Jaytee" data-post="1" data-topic="494">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/65b543/48.png" class="avatar"> Jaytee:</div>
<blockquote>
<p>Using the Add Data widget allows the study to load but it doesn’t give a 3D image or allow editing.</p>
</blockquote>
</aside>
<p>The image looks good, it’s a 3D volume, as it shows up with significant extent in three orthogonal slice viewers.</p>
<p>Volume rendering and most editing operations are only supported for grayscale volumes, so you have to convert your color image to grayscale, using <code>Vector to Scalar volume</code> module.</p>
<p>It might be better to export your OCT as a grayscale (scalar) volume - you can then apply any colormaps after you load that into Slicer.</p>

---

## Post #3 by @lassoan (2017-06-13 16:13 UTC)

<p>If you cannot scroll in any of the slice viewers, then maybe only a screen capture is saved.</p>
<p>Can you share a data set? (preferably phantom data; make sure no patient data is contained in the files)</p>

---

## Post #4 by @Jaytee (2017-06-14 02:38 UTC)

<p>I can scroll through the 2d pictures and the orthogonal views work… I’ll<br>
try make it grayscale and also upload a anonymous dicom to Dropbox, just<br>
need to export again from work…</p>

---

## Post #5 by @Jaytee (2017-06-14 10:54 UTC)

<p>I managed to use the Vector to Scalar Volume module to make it grayscale but it still wouldn’t allow me to edit or 3D render… I tried to export this version but same thing. The workstation with the originals doesn’t have a grayscale export function…</p>
<p>I’ve uploaded a low res version of the file here: <a href="https://www.dropbox.com/s/l03x5x54rtf3gvi/IMG001?dl=0" rel="nofollow noopener">https://www.dropbox.com/s/l03x5x54rtf3gvi/IMG001?dl=0</a> , if there are any other hints I’d be happy to hear it!</p>

---

## Post #6 by @cpinter (2017-06-14 11:59 UTC)

<p>3D rendering: Go to Volume Rendering module, select the scalar volume (output of the conversion step), then click the eye icon next to the volume selector. You’ll need to select a transfer function, for me MR-Default seems to work well with your data. Adjust with the Shift slider. If it’s slow, switch to VTK GPU Ray Casting.</p>
<p>Editing: What do you mean exactly? Segmenting out regions of interest? Go to Segment Editor and use the editor effects.</p>
<p>If you’d like to see the scalar volume similarly to the RGB image, go to Volumes module, choose the scalar volume, and select the lookup table called Inferno (or any other that you like).</p>

---

## Post #7 by @MHB (2018-03-06 04:35 UTC)

<p>Following up on this, I am trying to process some OCT data in the form of a series of 2D images, but am having little/no luck with volume rendering. These are already in grayscale and seem to show up fine in volume module, but I don’t know which knows to tweak to get a reasonable result.<br>
Images: <a href="https://www.dropbox.com/sh/ce95fzhimgtrdgt/AABB2B7ISsy10lqKd9OeFPHha?dl=0" rel="nofollow noopener">https://www.dropbox.com/sh/ce95fzhimgtrdgt/AABB2B7ISsy10lqKd9OeFPHha?dl=0</a></p>

---

## Post #8 by @pieper (2018-03-06 16:02 UTC)

<p>This data worked for me once I converted to scalar (even though the bmp files are grayscale they actually have three equal rgb components)</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/VectorToScalarVolume" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Modules/VectorToScalarVolume</a></p>

---

## Post #9 by @PaoloZaffino (2020-04-22 09:53 UTC)

<p>Hi all,<br>
I’m trying to import the exemplary dicom file, but I get nothing loaded.</p>
<p>Any idea?</p>
<p>Thanks a lot.<br>
Paolo</p>

---

## Post #10 by @lassoan (2020-04-22 13:28 UTC)

<p>Currently <a href="https://github.com/Slicer/Slicer/issues/3168">Slicer does not support loading of color DICOM images</a>. It would probably not too hard to add, but since color images are almost always screen captures that are not suitable for further analysis or processing, there hasn’t been enough motivation to dedicate time for that.</p>
<p>This DICOM image is a screen capture, too (8-bit, with some unknown color table, burnt-in annotations, etc.), so not usable for much. Instead of such derived image, the original data should be exported to DICOM, if possible. As a workaround, you can use ITK’s image reader by circumventing the DICOM module (just drag-and-dropping a single file to the Slicer application window).</p>

---

## Post #11 by @PaoloZaffino (2020-04-22 15:19 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>!<br>
By dopping the file into the main window it works!</p>

---
