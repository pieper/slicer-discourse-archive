---
topic_id: 16280
title: "Creating Roi From Structure"
date: 2021-03-01
url: https://discourse.slicer.org/t/16280
---

# Creating ROI from Structure

**Topic ID**: 16280
**Date**: 2021-03-01
**URL**: https://discourse.slicer.org/t/creating-roi-from-structure/16280

---

## Post #1 by @toyama (2021-03-01 08:43 UTC)

<p>I want to use Registration QA to find Inverce consistency and Jacobian.<br>
I wanted to set the RTstructure to ROI, but I could not.<br>
When I set the segment to model, I could set the model to ROI. (Fig1) However, when I change the ROI, the value is the same. (Fig2.3)<br>
If there is a way to create an ROI from a RTstructure, please let me know.<br>
Fig1<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a3046458e224f3a1620b648a9d06c5b6760ba3f.png" alt="image" data-base62-sha1="cRQoNvKMij3EGKlidh5UPjv6B6n" width="567" height="147"><br>
Fig2<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a560ea3599fdec38426cb97aca566640fb82028.png" alt="image" data-base62-sha1="aBBHZcPj3d1qkIMW9uswQ4jb7Qs" width="567" height="214"><br>
Fig3<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5e654a0cc2bc668cf90ec54d2560832db72e0bb.png" alt="image" data-base62-sha1="seHxE0MaVGgL8kZRaApuuMDBK9d" width="567" height="210"></p>

---

## Post #2 by @lassoan (2021-03-01 14:36 UTC)

<p>I’m not sure if RegistrationQA developers read the Slicer forum. If you don’t get answer here then you can post an issue to the <a href="https://github.com/gsi-biomotion/SlicerRegistrationQA">extension’s repository</a>.</p>

---

## Post #3 by @toyama (2021-03-02 07:04 UTC)

<p>Thank you for your answer.<br>
I’ve posted to the SlicerRT Git you gave me.<br>
I have looked at various posts about ROI and I was wondering if it is possible to create ROIs from contours or complex ROIs like contours. In my current situation, I can only create a rectangular ROI.</p>

---

## Post #4 by @lassoan (2021-03-04 03:24 UTC)

<p>You can create arbitrary shaped “region of interest” using Segment Editor.</p>

---

## Post #6 by @toyama (2021-03-04 08:06 UTC)

<p>I would like to ask a question again.<br>
I created an ROI using the Segment Editor, but it could not be used as an ROI in RegistrationQA, which I consulted before. So I tried to create a complex ROI like the red segment using Fig’s ROI tool and MarkupsCurve, but it did not work. Is it possible to create complex shapes with these tools?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e6e92f4bf7660bc2f837602f1db44e1c0933c1c.png" alt="image" data-base62-sha1="23FAtLHco9d3NxJzNkJPOWTB6gs" width="159" height="217"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4cb0916edc5d0168e6e32e8b527d67657538117.jpeg" data-download-href="/uploads/short-url/umsdY3v0v2zFmUs63xwMe26PPWT.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d4cb0916edc5d0168e6e32e8b527d67657538117_2_690x461.jpeg" alt="image" data-base62-sha1="umsdY3v0v2zFmUs63xwMe26PPWT" width="690" height="461" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d4cb0916edc5d0168e6e32e8b527d67657538117_2_690x461.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d4cb0916edc5d0168e6e32e8b527d67657538117_2_1035x691.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4cb0916edc5d0168e6e32e8b527d67657538117.jpeg 2x" data-dominant-color="7B7983"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1294×865 155 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @lassoan (2021-03-07 15:05 UTC)

<p>Developer of this extension is not active anymore here or on github, so most likely he will not be able to help you.</p>
<p>However, I’ve just tried the latest Slicer Preview Release and you can choose to compute statistics in an arbitrary segment, by right-clicking on the segmentation node and choosing Registration QA → Assign node to → Contour → Reference phase or Moving phase.</p>

---

## Post #8 by @toyama (2021-03-08 09:04 UTC)

<p>Thank you for your answer. In addition, I would like to ask you  questions.<br>
・If Stable Release will be released soon, I would like to use Stable Release instead of Preview Release, does the next Stable Release correspond to  Preview Release(version4.13.0)?<br>
・In Preview Release (version 4.13.0), were you able to specify any segment in the Reference phase or Moving phase without specifying an ROI, and calculate each indicator (Inverse consistency, Jacobian determinant) in that segment?<br>
I’m sorry for my poor English. It would be great if you could answer.</p>

---

## Post #9 by @lassoan (2021-03-08 16:00 UTC)

<p>A new Slicer Stable Release was created 2 weeks ago. It has the same features as the Slicer preview release (in these 2 weeks we made some internal infrastructure changes and minor fixes and improvements).</p>
<p>RegistrationQA works exactly the same way in both the stable and preview releases. You can either specify a ROI (box shaped region) or a segment (arbitrary shape region) to compute the statistics.</p>
<p>You can also use Inverse consistency and Jacobian determinant modules to get the metric values as 3D volume then use Segment Statistics module to get statistics per segment.</p>

---

## Post #10 by @toyama (2021-03-09 08:43 UTC)

<p>Thank you for your answer.<br>
I am using the version of the slicer that was released on Feb. 26 for windows.<br>
When I specified the segments as you taught me before (Fig1), all segments took the same value.<br>
Fig2 shows the table.<br>
Fig1<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19d95bffef49879bef55e7543d536dad6c831e15.png" data-download-href="/uploads/short-url/3GFCSsSPSSOFDSh8Qg8byNtF2f3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19d95bffef49879bef55e7543d536dad6c831e15_2_690x254.png" alt="image" data-base62-sha1="3GFCSsSPSSOFDSh8Qg8byNtF2f3" width="690" height="254" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19d95bffef49879bef55e7543d536dad6c831e15_2_690x254.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19d95bffef49879bef55e7543d536dad6c831e15.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19d95bffef49879bef55e7543d536dad6c831e15.png 2x" data-dominant-color="C0C1CA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">984×363 51.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Fig2<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43f665dd117791dee0c32a4e5a4987f3c6fc6bab.png" alt="image" data-base62-sha1="9HdTwFy1qCshpZM5Rvi6tKsIAht" width="571" height="339"><br>
When I click on “Create ROI around segments” to specify the segments, the ROI is created, but it is a rectangle. (Fig3)<br>
Fig3<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94975429666ba949521baeb7c09ce8e3ba52c4a5.jpeg" data-download-href="/uploads/short-url/lcuSVKNTlGmVOvgM2q0qjXrFsPj.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/94975429666ba949521baeb7c09ce8e3ba52c4a5_2_690x277.jpeg" alt="image" data-base62-sha1="lcuSVKNTlGmVOvgM2q0qjXrFsPj" width="690" height="277" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/94975429666ba949521baeb7c09ce8e3ba52c4a5_2_690x277.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/94975429666ba949521baeb7c09ce8e3ba52c4a5_2_1035x415.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/94975429666ba949521baeb7c09ce8e3ba52c4a5_2_1380x554.jpeg 2x" data-dominant-color="807588"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1923×772 264 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
If there is anything wrong with my procedure, please let me know.</p>

---

## Post #11 by @lassoan (2021-03-09 13:24 UTC)

<p>As far as I remember, I’ve read in the module documentation that only one segment is supported. If you want to analyze multiple segments at once, you can compute the metric for the complete volume using RegistrationQA and then use Segment Statistics module to get average metric value in each segment.</p>
<p>In Slicer terms, ROI is a box-shaped region.</p>

---

## Post #12 by @toyama (2021-03-10 09:02 UTC)

<p>Thank you for your answer.<br>
I am going to use the segment statics module to find Inverse Consistency, etc. as you suggested.<br>
I have created a Displacement Field using Registration Quality Assurance and moved it to Segment Statics. However, when I used the segment statics module, the result was as shown in Fig. 1, and the value could not be obtained. I selected Scalar Volume Statics because Scalar Volume Statics had the average of the values and so on, but I could only get the values for the closed surface statics.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d11bcb852a22c2774b684834f2208607d4b6f2f.png" data-download-href="/uploads/short-url/dhkpcAwxU3y4KYPLOzkrRmTMWKP.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d11bcb852a22c2774b684834f2208607d4b6f2f_2_690x398.png" alt="image" data-base62-sha1="dhkpcAwxU3y4KYPLOzkrRmTMWKP" width="690" height="398" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d11bcb852a22c2774b684834f2208607d4b6f2f_2_690x398.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d11bcb852a22c2774b684834f2208607d4b6f2f_2_1035x597.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d11bcb852a22c2774b684834f2208607d4b6f2f.png 2x" data-dominant-color="B6ADBD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1288×744 77.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Is there any reason for the failure?</p>

---

## Post #13 by @lassoan (2021-03-11 04:14 UTC)

<p>Statistics can be only computed for scalar volume, not for vector volume. Instead of computing statistics for the displacement field, compute statistics for the metrics (inverse consistency, Jacobian determinant, etc.).</p>

---

## Post #14 by @toyama (2021-03-11 05:32 UTC)

<p>Thank you for your answer.<br>
I checked the data, and both Displacement Field-invConsist and Displacement Field-jacobian are scalar volumes.However, statistics could not be obtained.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7666bf6ae11e7f90c5fbca680ec1f84c7d8a4213.png" data-download-href="/uploads/short-url/gTqtBv4gheyXA4u0r45FHe5DeWT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7666bf6ae11e7f90c5fbca680ec1f84c7d8a4213.png" alt="image" data-base62-sha1="gTqtBv4gheyXA4u0r45FHe5DeWT" width="690" height="231" data-dominant-color="E2EBF1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">691×232 10.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @lassoan (2021-03-11 05:42 UTC)

<p>They need to be single-component scalar volumes. If they are then scalar volume statistics work. If not, then you can save the scene as .mrb, upload to somewhere (dropbox, onedrive, google drive, …), post the link here, and we’ll have a look.</p>

---

## Post #16 by @toyama (2021-03-11 06:02 UTC)

<p>Here is a link to Dropbox. Please check it out. mrb files contain data other than scalar volumes, but please be patient.<br>
(.mrb)</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="16" height="16">
      <a href="https://www.dropbox.com/s/bxv4rzlqp89lvom/2021-03-11-Scene.mrb?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-unknown-large.png" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://www.dropbox.com/s/bxv4rzlqp89lvom/2021-03-11-Scene.mrb?dl=0" target="_blank" rel="noopener nofollow ugc">2021-03-11-Scene.mrb</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<p>
(scalar volume)</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="16" height="16">
      <a href="https://www.dropbox.com/sh/ihdpbji6ptqs6aq/AAC-5JIN1zZNXjyDNopAUWYya?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-folder_dropbox-large.png" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://www.dropbox.com/sh/ihdpbji6ptqs6aq/AAC-5JIN1zZNXjyDNopAUWYya?dl=0" target="_blank" rel="noopener nofollow ugc">ScalarVolume_55</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #17 by @toyama (2021-03-12 07:06 UTC)

<p>I’ll add a note.<br>
I also tried another method.<br>
I tried to create a vector field using Registration&gt;Quality Assurance&gt;Inverse Consistency, Jacobian Filter, convert the created vector field to a scalar volume using the Vector to Scalar Volume module, and then calculate the statistics using Segment Statistics.<br>
However the result was as shown in the image and could not be calculated.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/51f0b03cb341dbe2b5b4c3cad67c1481780107a5.png" data-download-href="/uploads/short-url/bGSlyublVwbFhc116O8i23Yn0z3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/51f0b03cb341dbe2b5b4c3cad67c1481780107a5.png" alt="image" data-base62-sha1="bGSlyublVwbFhc116O8i23Yn0z3" width="690" height="498" data-dominant-color="EFEFEF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">707×511 4.73 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
