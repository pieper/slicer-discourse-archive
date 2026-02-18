# Location of "SlicerRadiomics" output in 3D Slicer

**Topic ID**: 20028
**Date**: 2021-10-05
**URL**: https://discourse.slicer.org/t/location-of-slicerradiomics-output-in-3d-slicer/20028

---

## Post #1 by @Sari_Khalil (2021-10-05 18:31 UTC)

<p>I’m a new user of 3D slicer and my goal is to extract radiomic features using the “SlicerRadiomics” extension. I don’t know where the output table for these features is being saved. As you can see in the screenshot, I have the segmentation selected, all features checked, and output table set to “whereami”. Clicking apply seems to do something, but I cannot control nor do I know where the radiomic features are going?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d1fdc057518c0a80ca8f48140a34e143d24b163.jpeg" data-download-href="/uploads/short-url/1S6sS73zLMBqcCQchJIfbV70yOL.jpeg?dl=1" title="Screen Shot 2021-10-05 at 2.20.43 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0d1fdc057518c0a80ca8f48140a34e143d24b163_2_510x500.jpeg" alt="Screen Shot 2021-10-05 at 2.20.43 PM" data-base62-sha1="1S6sS73zLMBqcCQchJIfbV70yOL" width="510" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0d1fdc057518c0a80ca8f48140a34e143d24b163_2_510x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0d1fdc057518c0a80ca8f48140a34e143d24b163_2_765x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0d1fdc057518c0a80ca8f48140a34e143d24b163_2_1020x1000.jpeg 2x" data-dominant-color="3B3A39"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-10-05 at 2.20.43 PM</span><span class="informations">1309×1283 225 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Note I’m using 3D slicer on a Mac and I don’t know where the</p>

---

## Post #2 by @pieper (2021-10-05 18:53 UTC)

<p>They should appear in the table on the lower right of the display (the column headers are there but the rows are empty).  Check the application logs (Help-&gt;Report a bug menu) to see if there’s an indication why it didn’t complete.</p>

---

## Post #3 by @Sari_Khalil (2021-10-13 14:07 UTC)

<p>Thanks!, I checked the logs and the error is this: “ValueError: Error reading mask Filepath or SimpleITK object”</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38f63f6a2e88fa6dd795ca39301b15ac5258636f.png" data-download-href="/uploads/short-url/87UjWnBx7JkK8ZwinZwgfTXXs5h.png?dl=1" title="Screen Shot 2021-10-13 at 10.05.40 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38f63f6a2e88fa6dd795ca39301b15ac5258636f.png" alt="Screen Shot 2021-10-13 at 10.05.40 AM" data-base62-sha1="87UjWnBx7JkK8ZwinZwgfTXXs5h" width="690" height="181" data-dominant-color="323232"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-10-13 at 10.05.40 AM</span><span class="informations">1418×372 53 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @pieper (2021-10-13 17:35 UTC)

<p>Check that your temporary directory exists (or create a new one).  Sometimes an OS upgrade or other system operation can invalidate the directory.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1c3b64ba48b50bffca6524b32210ee9fd7ad171.png" data-download-href="/uploads/short-url/pmzP3veB32PgK48QLxwbcL3rD7H.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1c3b64ba48b50bffca6524b32210ee9fd7ad171_2_690x137.png" alt="image" data-base62-sha1="pmzP3veB32PgK48QLxwbcL3rD7H" width="690" height="137" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1c3b64ba48b50bffca6524b32210ee9fd7ad171_2_690x137.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1c3b64ba48b50bffca6524b32210ee9fd7ad171.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1c3b64ba48b50bffca6524b32210ee9fd7ad171.png 2x" data-dominant-color="DEDEE1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">843×168 29.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @Antonio_Tavares (2023-12-05 21:21 UTC)

<p>Hi, sorry to dig up an old thread, but I’m having a similar problem. I have just installed 3D Slicer (I’m using 5.2.0) and the Radiomics module, but after I finished the segmentation and tried to extract radiomics features, no output table appears.</p>
<p>I get this in the error log. I’ve tried setting a new Temp folder but it did not work. Any help is much appreciated!</p>
<p>ReadImageInformation: Error reading C:/Users/Ant�nio/AppData/Local/Temp/Slicer/BEAAE_vtkMRMLScalarVolumeNodeB.nrrd:</p>
<p>[nrrd] nrrdLoad: fopen(“C:/Users/Antnio/AppData/Local/Temp/Slicer/BEAAE_vtkMRMLScalarVolumeNodeB.nrrd”,“rb”) failed: No such file or directory</p>
<p>[2023-12-05 21:19:01] I: radiomics.script: Processing results…</p>
<p>[2023-12-05 21:19:01] I: radiomics.script: Finished segment-based extraction successfully…</p>
<hr>
<p>EDIT:<br>
As soon as I posted this, I realized there might be a problem with my windows username having a diacritic…I used another folder outside of my users folder and it worked. So, if you’re having that problem, check that out.</p>

---
