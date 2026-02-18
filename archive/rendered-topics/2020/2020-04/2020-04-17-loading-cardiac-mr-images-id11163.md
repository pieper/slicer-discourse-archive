# Loading Cardiac MR images

**Topic ID**: 11163
**Date**: 2020-04-17
**URL**: https://discourse.slicer.org/t/loading-cardiac-mr-images/11163

---

## Post #1 by @sarvpriya1985 (2020-04-17 18:18 UTC)

<p>Hi everyone,</p>
<p>I tried to load a single dicom image of Cardiac MRI (IMAGE ATTACHED)<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/25fd18a8c5c92f7d74aa06c01e580faab457178e.jpeg" data-download-href="/uploads/short-url/5q3VdaWil1PqHxXmCqcRz3KSux8.jpeg?dl=1" title="Screen Shot 2020-04-17 at 1.02.01 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/25fd18a8c5c92f7d74aa06c01e580faab457178e_2_559x500.jpeg" alt="Screen Shot 2020-04-17 at 1.02.01 PM" data-base62-sha1="5q3VdaWil1PqHxXmCqcRz3KSux8" width="559" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/25fd18a8c5c92f7d74aa06c01e580faab457178e_2_559x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/25fd18a8c5c92f7d74aa06c01e580faab457178e_2_838x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/25fd18a8c5c92f7d74aa06c01e580faab457178e_2_1118x1000.jpeg 2x" data-dominant-color="3A3A3A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-04-17 at 1.02.01 PM</span><span class="informations">1414×1264 201 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>However, once I loaded the image into slicer, I am seeing something different and not the exact image.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a7d98c9bcb61ba6ed0a891c9f12dce1fd55b9913.png" data-download-href="/uploads/short-url/nWRPKxAB987IvMVZbNFieug46yv.png?dl=1" title="Screen Shot 2020-04-17 at 12.59.46 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7d98c9bcb61ba6ed0a891c9f12dce1fd55b9913_2_690x437.png" alt="Screen Shot 2020-04-17 at 12.59.46 PM" data-base62-sha1="nWRPKxAB987IvMVZbNFieug46yv" width="690" height="437" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7d98c9bcb61ba6ed0a891c9f12dce1fd55b9913_2_690x437.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7d98c9bcb61ba6ed0a891c9f12dce1fd55b9913_2_1035x655.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7d98c9bcb61ba6ed0a891c9f12dce1fd55b9913_2_1380x874.png 2x" data-dominant-color="2D2E3A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-04-17 at 12.59.46 PM</span><span class="informations">4184×2650 476 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>.</p>
<p>Also, is it possible to load MR dicom images with their .ROI files in dicom. (since initially I was not able to load them into slicer, I did segmentation of myocardium in another software Mazda)- But would like to upload those in Slicer Pyradiomics.</p>
<p>I would appreciate all the help.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #2 by @lassoan (2020-04-17 18:26 UTC)

<p>This looks good. You see intersections of the single oblique slice with the axial, sagittal, coronal directions - which are single lines. You can click rotate to volume plane button in slice view controller to align slice views with the oblique slice plane.</p>
<p>DICOM can store an ROI many different ways. Slicer can import ROI from DICOM stored as DICOM RT structure set (if SlicerRT extension is installed) or segmentation object (if QuantitativeReporting extension is installed).</p>

---

## Post #3 by @sarvpriya1985 (2020-04-17 19:18 UTC)

<p>Hi Andras,<br>
Thanks. I got the loading done perfectly after clicking the volume plane button.</p>
<p>Regarding loading roi files, i installed both extensions but i am not seeing them in my loaded extensions. I am attaching the type of files i have<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/8867a1c63a9b34ad1c7b219ac0dcfa28c1c4afa2.jpeg" data-download-href="/uploads/short-url/jsGXUIQ99V9RUXji4QBSYA0U6bw.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8867a1c63a9b34ad1c7b219ac0dcfa28c1c4afa2_2_690x128.jpeg" alt="Capture" data-base62-sha1="jsGXUIQ99V9RUXji4QBSYA0U6bw" width="690" height="128" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8867a1c63a9b34ad1c7b219ac0dcfa28c1c4afa2_2_690x128.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/8867a1c63a9b34ad1c7b219ac0dcfa28c1c4afa2.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/8867a1c63a9b34ad1c7b219ac0dcfa28c1c4afa2.jpeg 2x" data-dominant-color="FAFBFA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">843×157 11.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>  and snapshot of the installed extensions<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f503405ee95897380f6d2f0fb642c5066e4c99dd.png" data-download-href="/uploads/short-url/yXtWGaTV2tpd6g8biI0a88Qf1tb.png?dl=1" title="2020-04-17" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f503405ee95897380f6d2f0fb642c5066e4c99dd_2_690x388.png" alt="2020-04-17" data-base62-sha1="yXtWGaTV2tpd6g8biI0a88Qf1tb" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f503405ee95897380f6d2f0fb642c5066e4c99dd_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f503405ee95897380f6d2f0fb642c5066e4c99dd_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f503405ee95897380f6d2f0fb642c5066e4c99dd_2_1380x776.png 2x" data-dominant-color="F5F5F6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2020-04-17</span><span class="informations">1920×1080 222 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> . Please let me know what i should do next to see both roi and image. I hope once installed I can somehow save it as a mask (possibly) and run pyradiomics.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #4 by @lassoan (2020-04-17 19:36 UTC)

<p>COPD 10 ED.roi is probably not in DICOM format, but some proprietary file. Does it show up as a series in Slicer’s DICOM module?</p>

---

## Post #5 by @sarvpriya1985 (2020-04-17 19:41 UTC)

<p>It’s not in dicom format. The software gives these .roi file only which can be loaded on top of dicom image.</p>

---

## Post #6 by @sarvpriya1985 (2020-04-17 20:18 UTC)

<p>Hi Andras,<br>
I can do segmentation again if this is not possible. However, how should i save the mask. Once i export it as labelmap, how should i and in which format save it. I plan to use the same mask for deep learning later on, so that i don’t have to do segmentation again.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #7 by @lassoan (2020-04-17 23:41 UTC)

<p>You can save the segmentation as seg.nrrd file. It is a simple .nrrd image file with some extra optional metadata (segment name, color, etc.).</p>
<p>Use a very recent Slicer Preview release, because then your segmentation is saved as a simple 3D volume (if segments don’t overlap), which is easier to handle than the older 4D volume format.</p>
<p>If you work with lots of data sets then you may find <a href="https://github.com/JoostJM/SlicerCaseIterator">CaseIterator extension</a> (if you work with many volumes) or <a href="https://github.com/SlicerIGT/aigt">SlicerAIGT</a> useful (if you segment hundreds of time points in a time sequence).</p>

---

## Post #8 by @sarvpriya1985 (2020-04-18 17:07 UTC)

<p>Thanks a lot Andras.</p>
<p>Right now I have only two dicom images per patient to segment, so I guess it won’t be much. I will download Caselterator too and then will try figuring out that as well.</p>
<p>Thanks again,<br>
Sarv</p>

---

## Post #9 by @demchenkovaanna89 (2025-11-21 19:02 UTC)

<p>Hello! I can’t break the movie sequence into sections; for some reason, only one section is displayed</p>

---
