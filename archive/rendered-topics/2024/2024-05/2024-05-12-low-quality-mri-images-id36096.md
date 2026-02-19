---
topic_id: 36096
title: "Low Quality Mri Images"
date: 2024-05-12
url: https://discourse.slicer.org/t/36096
---

# Low quality MRI images

**Topic ID**: 36096
**Date**: 2024-05-12
**URL**: https://discourse.slicer.org/t/low-quality-mri-images/36096

---

## Post #1 by @SPGesus (2024-05-12 00:25 UTC)

<p>Hello, I have found some resources on my problem, but no actual solutions.</p>
<p>I got an MRI and I would like to convert my brain into a model I can print. There are a few tutorials, and so far this youtube version is my best one</p>
<div class="youtube-onebox lazy-video-container" data-video-id="k1WIpwV-8lE" data-video-title="How To 3D Print Your Brain In A Few Simple Steps - TUTORIAL 2022" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=k1WIpwV-8lE" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/k1WIpwV-8lE/maxresdefault.jpg" title="How To 3D Print Your Brain In A Few Simple Steps - TUTORIAL 2022" width="" height="">
  </a>
</div>

<p>My problem is only one set of images are clear. When I view the images through the philips dicom viewer provided to me, it’s fine.</p>
<p>But when I view it through 3d slicer half the data is garbage, which prevents me from selecting my brain to turn into a 3d model.</p>
<p>to start off I get the following errors when opening up my files</p>
<pre><code class="lang-auto">1: Unnamed Series [Scalar Volume]: Reference image in series does not contain geometry information. Please use caution.

1: 662A78BB2741A01 [Scalar Volume]: Reference image in series does not contain geometry information. Please use caution.

4: MRA 3D TOF [Scalar Volume]: Image slices are not equally spaced (2.39997 spacing was expected, 0.600071 spacing was found between files C:/Users/user/Downloads/Databasemri/dicom/06d1a48e/f0701ac3/7497f1535a96b00d888d1b6e37b893e0.dcm and C:/Users/user/Downloads/Databasemri/dicom/06d1a48e/f0701ac3/09c8d150787d31c770a547524f322802.dcm).  Slicer will apply a transform to this series trying to regularize the volume. Please use caution.

</code></pre>
<p>I’m not sure if this is useful, but I’m posting it just in case</p>
<p>After the import I get a lot of data from what I have seen others do, is not typical<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc1aefc94c1acf33b3c405670d9cbf20060529b3.png" data-download-href="/uploads/short-url/vp8KOmHLX2bUREFq9l3GeNktZkL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc1aefc94c1acf33b3c405670d9cbf20060529b3_2_376x500.png" alt="image" data-base62-sha1="vp8KOmHLX2bUREFq9l3GeNktZkL" width="376" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc1aefc94c1acf33b3c405670d9cbf20060529b3_2_376x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc1aefc94c1acf33b3c405670d9cbf20060529b3_2_564x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc1aefc94c1acf33b3c405670d9cbf20060529b3.png 2x" data-dominant-color="2B2B2B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">641×852 71.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>That aside, I have one view of clear data, and then the two other views essentially being junk<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de958e29e90e3c37a56b8fc006e25dff38fd5cae.jpeg" data-download-href="/uploads/short-url/vL4pZB1fiAK0RZgInNhpDv0WN1s.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de958e29e90e3c37a56b8fc006e25dff38fd5cae_2_439x500.jpeg" alt="image" data-base62-sha1="vL4pZB1fiAK0RZgInNhpDv0WN1s" width="439" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de958e29e90e3c37a56b8fc006e25dff38fd5cae_2_439x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de958e29e90e3c37a56b8fc006e25dff38fd5cae_2_658x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de958e29e90e3c37a56b8fc006e25dff38fd5cae_2_878x1000.jpeg 2x" data-dominant-color="3C3D47"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1046×1191 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have the good data of the other views, 3d slicer just isn’t allowing me to view them at the same time?</p>
<p>Ultimately my question is, is there a way for me to take the good parts of 3 different files to make it into one master file for 3d slicer to use? or is my data more or less junk for what I am trying to accomplish.</p>

---

## Post #2 by @pieper (2024-05-12 14:48 UTC)

<p>These threads should help explain:</p>
<aside class="quote quote-modified" data-post="1" data-topic="15847">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/guy_ma/48/9776_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/trying-to-take-three-different-volumes-to-create-one-3d-model-beginner-of-3d-slicer/15847">Trying to take three different volumes to create one 3d model (beginner of 3d slicer)</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Operating system:Windows 10 
Slicer version: Latest 
Expected behavior: I want to use the views that I set in the panels for the 3d model 
Actual behavior: Only uses one volume, which makes the 3d model poor quality (because the other two views are pixelated 
Im not sure exactly how to do this. I had an MRI recently, and I want to make an interactive model with the scans I got. But when I set it at only one of the volumes, only one of the views is good quality. So I tried setting the other two w…
  </blockquote>
</aside>

<aside class="quote quote-modified" data-post="1" data-topic="2941">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/f19dbf/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941">Combining volumes - what am I missing?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Operating system: Mac - High Sierra 
Slicer version: 4.8.1 
Expected behavior: One perfect, high resolution volume 
Actual behavior: Three volumes, each one being high resolution in only one plane (sagittal, coronal, transverse) 
I have been using 3D Slicer for many months and I’m slowly learning the ropes. I am using it to produce anatomical boney models, and have probably created between 10-15 models. 
After loading CT scans from their DICOM folder I always get several volumes, often with the …
  </blockquote>
</aside>


---
