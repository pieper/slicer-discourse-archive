---
topic_id: 36611
title: "Error In Opening Files Using Slicer 5 6 2"
date: 2024-06-05
url: https://discourse.slicer.org/t/36611
---

# Error in Opening Files using Slicer 5.6.2

**Topic ID**: 36611
**Date**: 2024-06-05
**URL**: https://discourse.slicer.org/t/error-in-opening-files-using-slicer-5-6-2/36611

---

## Post #1 by @MPARHAM (2024-06-05 15:49 UTC)

<p>Hi Slicer Community,</p>
<p>I am working on a research project and need to redo my segmentations. However, I am encountering an issue when trying to open files in 3D Slicer. Here are the files I have in my folder:</p>
<ul>
<li>2024-03-05-Scene.nnrd</li>
<li>2024-03-05-Scene.mrml</li>
<li>2401 CO T1 FS mDIXON GD.scene</li>
<li>Segmentation.seg.nnrd</li>
</ul>
<p>When I try to open these files, the 3D volume only shows up in the axial view.</p>
<p>Could someone help me resolve this issue?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/affe6c7c117bacf24b6c786738cda568401d1049.png" data-download-href="/uploads/short-url/p6UEMllbCEucIEbG0ehZMgHTSsN.png?dl=1" title="Error_3D_Model" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/affe6c7c117bacf24b6c786738cda568401d1049_2_690x387.png" alt="Error_3D_Model" data-base62-sha1="p6UEMllbCEucIEbG0ehZMgHTSsN" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/affe6c7c117bacf24b6c786738cda568401d1049_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/affe6c7c117bacf24b6c786738cda568401d1049_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/affe6c7c117bacf24b6c786738cda568401d1049_2_1380x774.png 2x" data-dominant-color="91929F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Error_3D_Model</span><span class="informations">1921×1080 250 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-06-06 03:34 UTC)

<p>You loaded a screenshot: 2024-03-02-Scene.png. This image is 2D (single-slice 3D), so it only shows up in the red slice view.</p>
<p>NRRD files store 3D image and segmentations.</p>

---

## Post #3 by @MPARHAM (2024-06-12 19:02 UTC)

<p>Hi Team,</p>
<p>I think I’ve identified the issue. Here are the potential causes for the error:</p>
<ol>
<li>Incorrect data upload</li>
<li>Version error introduced in Slicer 5.6.2</li>
</ol>
<p>The error occurs when trying to upload previously segmented data in version 5.6.1, specifically with the following files:</p>
<ul>
<li>2024-03-05-Scene.nnrd</li>
<li>2024-03-05-Scene.mrml</li>
<li>2401 CO T1 FS mDIXON GD.scene</li>
<li>Segmentation.seg.nnrd</li>
</ul>
<p>No PNG files were uploaded into 3D Slicer.</p>
<p>When I upload these files, I get a random screenshot in the panels instead of the expected coronal, sagittal, axial, and 3D views. For instance, a screenshot of the DICOM Database appears, which I never took. You can see this issue in the attached image.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d31545a89a348146bd70dd142d5c8717136dd52f.png" data-download-href="/uploads/short-url/u7kjVZjKHNVJzISqA8JVI1EPwL5.png?dl=1" title="Error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d31545a89a348146bd70dd142d5c8717136dd52f_2_690x369.png" alt="Error" data-base62-sha1="u7kjVZjKHNVJzISqA8JVI1EPwL5" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d31545a89a348146bd70dd142d5c8717136dd52f_2_690x369.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d31545a89a348146bd70dd142d5c8717136dd52f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d31545a89a348146bd70dd142d5c8717136dd52f.png 2x" data-dominant-color="9C8DA0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Error</span><span class="informations">1005×538 67.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In the left panel, the expected data is visible, but an extra set of segmentations is added with an underscore suffix (e.g., *_1). To solve this issue, you need to delete these extra files. Once deleted, the views should display the correct content.<br>
Additionally, this solution should also fix the 3D model not centering correctly, as mentioned in a previous post.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3b4508de68944a187a43c0a1328b9510a553d5f.jpeg" data-download-href="/uploads/short-url/pDJMXdxbWCmos3zDJsVP138a9zN.jpeg?dl=1" title="Expected_View" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3b4508de68944a187a43c0a1328b9510a553d5f_2_690x375.jpeg" alt="Expected_View" data-base62-sha1="pDJMXdxbWCmos3zDJsVP138a9zN" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3b4508de68944a187a43c0a1328b9510a553d5f_2_690x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3b4508de68944a187a43c0a1328b9510a553d5f_2_1035x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3b4508de68944a187a43c0a1328b9510a553d5f_2_1380x750.jpeg 2x" data-dominant-color="76767D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Expected_View</span><span class="informations">1920×1044 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2024-06-12 22:57 UTC)

<p>Everything appeara to work as expected. The segmentation is in the scene twice, because loading the scene (.mrml file) loads all the data that you had in the scene and you also loaded the .seg.nrrd file. You have also loaded the screenshot that was automatically generated qhen you saved the scene.</p>
<p>The solution is to only load the .mrml file.</p>

---
