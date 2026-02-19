---
topic_id: 10182
title: "How To Save My Work Into Dicom Format"
date: 2020-02-10
url: https://discourse.slicer.org/t/10182
---

# How to save my work into dicom format

**Topic ID**: 10182
**Date**: 2020-02-10
**URL**: https://discourse.slicer.org/t/how-to-save-my-work-into-dicom-format/10182

---

## Post #1 by @prencekhan (2020-02-10 08:01 UTC)

<p>Hello!</p>
<p>I would like to ask how do I save my work into DICOM format? I need to save it into DICOM format because I will be import it to the treatment planning computer.</p>
<p>Thanks for your help</p>

---

## Post #2 by @Juicy (2020-02-10 09:07 UTC)

<p>What type of slicer object do you want to save as a DICOM?</p>
<p>You may find useful advice in this post: <a href="https://discourse.slicer.org/t/process-to-import-an-stl-file-and-convert-export-a-series-of-dicom-files/9906">https://discourse.slicer.org/t/process-to-import-an-stl-file-and-convert-export-a-series-of-dicom-files/9906</a></p>

---

## Post #3 by @prencekhan (2020-02-10 11:13 UTC)

<p>In the 3D slicer, I load 2 dicom images. Each dicom images is composed of 16 slice. I did subtract the two images using subtract image filter. My problem is that I want to save the result with dicom format so I can load in to the treatment planning computer. How can I do that? Thanks for your help</p>

---

## Post #4 by @timeanddoctor (2020-02-10 12:20 UTC)

<p>yes, you can export  the DICOM files by the DICOM module and click the export.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e973e499e1778fa15c016af46670fb10dbeab77.png" data-download-href="/uploads/short-url/i3Scjk79mowQZxeoDXpguqfHIJ9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e973e499e1778fa15c016af46670fb10dbeab77_2_690x92.png" alt="image" data-base62-sha1="i3Scjk79mowQZxeoDXpguqfHIJ9" width="690" height="92" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e973e499e1778fa15c016af46670fb10dbeab77_2_690x92.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e973e499e1778fa15c016af46670fb10dbeab77_2_1035x138.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e973e499e1778fa15c016af46670fb10dbeab77_2_1380x184.png 2x" data-dominant-color="F8F8F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1486×199 10.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @Juicy (2020-02-10 19:29 UTC)

<p>When you load DICOM image stacks they are loaded as a volume. Go to the Data module and find the volume which was result of the subtraction filter in the list of volumes. Then simply right click on the volume and choose ‘Export to DICOM’</p>

---

## Post #6 by @prencekhan (2020-02-12 06:06 UTC)

<p>Thank you Juicy and Li Zhenzhu. I was able to save my work in a dicom format. Problem solved.</p>
<p>But I have another one question. How can I measure the CT number of my CT image  using circular ROI with a radius of 200 mm^2 in the 3D slicer? Hope you can help me. It is my very first time using this software.</p>
<p>Thank you very much.</p>

---

## Post #7 by @Juicy (2020-02-12 07:01 UTC)

<p>I don’t know of a quick tool which does this like you have in the likes of image J or the software on the CT workstations (although there may be?)</p>
<p>The way I would do that (although there may be other ways) is to go to segment editor, then go to the paint effect.</p>
<p>You want a circular area of 200mm^2 and because the area of a circle is A = (pi * d^2) / 4 then the diameter of the circle needs to be approx 16mm (if I did my maths right).</p>
<p>Now click the small “%” button to toggle to absolute diameter mode for the paint brush size and enter the paint brush diameter as 16mm.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15541976bf5fab29b6b6b440fa21d089ebf56b7e.jpeg" data-download-href="/uploads/short-url/32GcY0sj40ENSaRP397EWiah38G.jpeg?dl=1" title="Segment editor" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/15541976bf5fab29b6b6b440fa21d089ebf56b7e_2_690x381.jpeg" alt="Segment editor" data-base62-sha1="32GcY0sj40ENSaRP397EWiah38G" width="690" height="381" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/15541976bf5fab29b6b6b440fa21d089ebf56b7e_2_690x381.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15541976bf5fab29b6b6b440fa21d089ebf56b7e.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15541976bf5fab29b6b6b440fa21d089ebf56b7e.jpeg 2x" data-dominant-color="C8C7CB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Segment editor</span><span class="informations">1034×571 84.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Then click once (do not click and drag) on the area you are interested in to paint a circle (as shown in yellow above). If you accidentally paint in the wrong spot just press the undo button.</p>
<p>Now go over to “Segment Statistics” module and enter your segmentation node (probably called “Segmentation”) and your volume as inputs. Then press apply and you will see the mean HU units of the area you have just painted on the resulting table.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d042d9ad526b1a67aff2ce218f367aee840201ea.jpeg" data-download-href="/uploads/short-url/tImxtCcOac9eOIwW5CLrM9uopBg.jpeg?dl=1" title="Segment editor2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d042d9ad526b1a67aff2ce218f367aee840201ea_2_690x487.jpeg" alt="Segment editor2" data-base62-sha1="tImxtCcOac9eOIwW5CLrM9uopBg" width="690" height="487" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d042d9ad526b1a67aff2ce218f367aee840201ea_2_690x487.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d042d9ad526b1a67aff2ce218f367aee840201ea.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d042d9ad526b1a67aff2ce218f367aee840201ea.jpeg 2x" data-dominant-color="D6D4D4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Segment editor2</span><span class="informations">808×571 66.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @prencekhan (2020-02-12 14:09 UTC)

<p>Thank you Juicy for everything. I was able to get the CT number. Problem solved again.</p>
<p>Cheers!</p>

---

## Post #9 by @prencekhan (2020-02-13 03:40 UTC)

<p>Hello Juizy, I have another question. My dicom files are only 48 and I assumed that the slice number is also 48 but the S (which I also I assumed as the slice number in the app) is from 72-216. I really need to get to slice 21. I tried to load and open slice 21 but the S sign is now 155. Why is that? Can you help me understand this. Or can you help how can I calibrate this S so that I will not be confused. Please refer to the image on what I trying to say as the S sign.</p>
<p>Thank you very much for your time and <a>Uploading: EBC2E46A-4D4C-4EC6-BF20-D282706F5041.jpeg…</a> consideration.</p>

---

## Post #10 by @Juicy (2020-02-13 06:47 UTC)

<p>Hi,</p>
<p>The picture did not work but I If you mean what I think you mean then no, S does not refer to the slice number.</p>
<p>RAS which means (Right Anterior Superior) is the coordinate system in 3d slicer it is the same as the XYZ coordinate system of the CT scanner. See more about coordinate systems <a href="https://www.slicer.org/wiki/Coordinate_systems" rel="noopener nofollow ugc">here</a></p>
<p>The origin of the scan 3D coordinate system is set up by the CT operator who will zero the machine in a certain position. If the S says 155 then this means the slice you are looking at is 155mm above the position where the operator zeroed the CT machine.</p>
<p>If you want to see which slice number you are at then you need to look at the image coordinate system or IJK coordinate system the K coordinate should tell you which slice number you are at. Assuming your scan is axial then hover your mouse over the red slice and look at the number shown in the following picture.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da51eb25367b92283c4350cc4504cdc988ed9613.jpeg" data-download-href="/uploads/short-url/v9lB5wV9qXRytxGPElJ6l4KD2j9.jpeg?dl=1" title="Forum1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/da51eb25367b92283c4350cc4504cdc988ed9613_2_690x481.jpeg" alt="Forum1" data-base62-sha1="v9lB5wV9qXRytxGPElJ6l4KD2j9" width="690" height="481" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/da51eb25367b92283c4350cc4504cdc988ed9613_2_690x481.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da51eb25367b92283c4350cc4504cdc988ed9613.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da51eb25367b92283c4350cc4504cdc988ed9613.jpeg 2x" data-dominant-color="B1B0B5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Forum1</span><span class="informations">975×681 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>But remember that slicer uses zero indexing for the K coordinate so the first ‘slice’ number is 0 so if you are looking for slice 21 then you may need to go to slice number 22 in slicer.</p>

---

## Post #11 by @prencekhan (2020-02-14 04:09 UTC)

<p>Thank you so much Juizy. Problem solved.</p>

---
