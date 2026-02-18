# Compare two CBCT volumes

**Topic ID**: 18463
**Date**: 2021-07-01
**URL**: https://discourse.slicer.org/t/compare-two-cbct-volumes/18463

---

## Post #1 by @MelanieW (2021-07-01 16:07 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.20210226<br>
Expected behavior:<br>
I would like to compare CBCT volume difference between pre and post bone grafts of the maxilla. I have registered the two original pre and post scans using BRAINS and then applied an ROI using the converter module to crop the combined model. This appears to give me one combined image with the desired ROI.  I applied a bone segmentation threshold to view in 3D.  I thought there would be a way of seeing how much of the pre-graft and how much of the post-graft was within the registered volume so that I could look at Quantification Segment Stats. What have I done wrong? I wonder if it’s something at the registration phase - I created the output volume as a new ‘combined image’. Ideas gratefully received!<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2021-07-02 05:02 UTC)

<p>There are many tools for comparing volumes and segmentations. Could you describe what exactly you would like to compute (displacements, volumes, …)? It would help a lot if you attached an annotated image.</p>

---

## Post #3 by @MelanieW (2021-07-02 09:05 UTC)

<p>Thank you so much for your prompt reply, Andras. I would like to register two CBCT volumes of the same maxilla and quantify the volume difference in an ROI after bone grafting (peri-implant surgery) in cm3 or mm3. Ideally I would also like to know the difference in voxel value as a measure of change of relative density. The same CBCT scanner and settings are used for each scan so I don’t think I need to apply algorithms to calculate HU as really I’m trying to learn relative values rather than absolute values. There are slight positioning discrepancies in how the patients have been scanned, so I need to ensure exactly the same ROI is being quantified and compared in the pre-op and post-op scans.</p>
<p>The following example I’ve done by uploading DICOMS in 3D slicer, using segmentations to add segment, set threshold (220-3071), scissors tool to roughly crop the desired area, exported as STL file, then used Autodesk meshmixer to create a solid, meshed, smoothed model, then cloud compare to register the pre and post-op models and calculate the volumes of each in order to work out the volume of growth. I know I should be able to do the whole process with 3D slicer, which is why I’ve contacted the support crew, only I’ve encountered difficulties in applying the same ROI to the pre-op and post-op scans.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a7f49aeecca19c64bcbd99235e791fd5ff95e2c.jpeg" data-download-href="/uploads/short-url/fc7k8r9Q3XvpGhbDESrIEIgq0Hi.jpeg?dl=1" title="3CEFCEE78CCF4F9B873E24E85600BBAB.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a7f49aeecca19c64bcbd99235e791fd5ff95e2c_2_416x371.jpeg" alt="3CEFCEE78CCF4F9B873E24E85600BBAB.jpg" data-base62-sha1="fc7k8r9Q3XvpGhbDESrIEIgq0Hi" width="416" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a7f49aeecca19c64bcbd99235e791fd5ff95e2c_2_416x371.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a7f49aeecca19c64bcbd99235e791fd5ff95e2c_2_624x556.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a7f49aeecca19c64bcbd99235e791fd5ff95e2c_2_832x742.jpeg 2x" data-dominant-color="446EA4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3CEFCEE78CCF4F9B873E24E85600BBAB.jpg</span><span class="informations">1248×1112 258 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I can use the registration module, but this only allows me to visualize and toggle between pre-op and post-op scans rather than quantify the differences between them.</p>
<p>I tried out the ChangeTracker module last night, after finding the quantitativeimaging_slicer4.5.pdf support document, and used the registration option in advanced settings. That gave me the metrics below – I notice you get mLs (or cm3) but why is this in pixels, not voxels? Is Change Tracker the most accurate module to measure volume change or is there a better way to do it?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23f48d8bd371bfe662d9b82446a999f5f2b46234.jpeg" data-download-href="/uploads/short-url/584F98YnCLKWkNyqeJhdaEzGxo0.jpeg?dl=1" title="D24489C0C74E429AACF319FED690F28F.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/23f48d8bd371bfe662d9b82446a999f5f2b46234_2_559x262.jpeg" alt="D24489C0C74E429AACF319FED690F28F.jpg" data-base62-sha1="584F98YnCLKWkNyqeJhdaEzGxo0" width="559" height="262" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/23f48d8bd371bfe662d9b82446a999f5f2b46234_2_559x262.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/23f48d8bd371bfe662d9b82446a999f5f2b46234_2_838x393.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/23f48d8bd371bfe662d9b82446a999f5f2b46234_2_1118x524.jpeg 2x" data-dominant-color="423B40"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">D24489C0C74E429AACF319FED690F28F.jpg</span><span class="informations">1677×786 284 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I liked the tabular segmentation statistics in the quantification module but I’ve had to do separate segmentions for each pre-op/ post-op data sets and haven’t been able to reproduce exactly the same ROI. I must need to encorporate some kind of registration!</p>
<p>Hopefully this helps to explain by goals and problems a bit better. I’m rather novice with using these software programmes.</p>
<p>Many thanks in advance of your help.<br>
Kind regards,</p>
<p>Melanie</p>
<p>Registrar in Oral Surgery</p>

---

## Post #4 by @Jessica_Rabelo_Mina (2024-04-17 18:12 UTC)

<p>Hi Melanie! did you find how to compare? I need this!</p>

---

## Post #5 by @lassoan (2024-04-18 00:12 UTC)

<p>You can align the images using the image registration methods described <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html">here</a>. Then you can segment the regions of interest and get volume, density, etc. statistics using Segment Statistics module. Change Tracker module may be usable, too, but first you need to get all your structures segmented.</p>
<p>What may not be obvious is that it is very important to use the same region of interest in all the segmentations. This can be achieved by specifying a region of interest by a segment, copy that segment into every image segmentation, and use that as editable region (in masking settings in Segment Editor).</p>

---
