# Real-time Image Guided Surgery

**Topic ID**: 18477
**Date**: 2021-07-02
**URL**: https://discourse.slicer.org/t/real-time-image-guided-surgery/18477

---

## Post #1 by @Ahmet_Yildiz (2021-07-02 07:01 UTC)

<p><strong>Operating system:</strong> Windows 10<br>
<strong>Slicer version:</strong> 4.11<br>
<strong>Overall Goal:</strong> Visualizing the brain in Real-time to design and follow a trajectory using a stylus tracked with optical tracker.<br>
<strong>Problem:</strong> Present a real-time cross section of the brain with respect to Stylus. Please check attached images for illustration.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96a7c1e49e5b6c5b4218f681a786bbf8965fa97f.jpeg" alt="image" data-base62-sha1="luL2qpgv88TYcTSV98h5EOcvehx" width="399" height="323"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65fbc6627cc43758d2cda5f1e417e08428547b1d.jpeg" alt="image" data-base62-sha1="eybEhYnVjhvf2ty94KDd1n4ItZz" width="399" height="318"></p>
<p>Currently, i am in a position where the stylus is calibrated, registration took place between real and 3D model of a skull phantom and showing the stylus on a fused MRI/CT scan image using Volume Reslice Driver.<br>
My next step is to do the shown above as an attempt to design a safe trajectory.<br>
Preserving the segmented tumor and cross-section the surrounding.<br>
How doable is that? Or is it something we can create a module for?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f04d232df313af8b3eace90784500e139b9c113.jpeg" data-download-href="/uploads/short-url/mGKfjdR7j8as6VF5V5N9ZYXGzkf.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9f04d232df313af8b3eace90784500e139b9c113_2_517x226.jpeg" alt="image" data-base62-sha1="mGKfjdR7j8as6VF5V5N9ZYXGzkf" width="517" height="226" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9f04d232df313af8b3eace90784500e139b9c113_2_517x226.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9f04d232df313af8b3eace90784500e139b9c113_2_775x339.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9f04d232df313af8b3eace90784500e139b9c113_2_1034x452.jpeg 2x" data-dominant-color="37363F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1843×809 163 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thank you in advance.</p>

---

## Post #2 by @lassoan (2021-07-03 19:47 UTC)

<p>Everything that is shown in the images above is easily doable (you just need to enable the feature that you need).</p>
<p>What exactly do you miss?</p>
<p>3D display of the tumor? You can enable that by clicking “Show 3D” button in Segment Editor module.</p>

---

## Post #3 by @Ahmet_Yildiz (2021-07-03 20:01 UTC)

<p>Thank you for your reply Andras,<br>
What i am seeking is to provide an active cross-section of the brain relative to stylus motion. That is the deeper the stylus goes inside the phantom the deeper the cross section is shown in 3D view. From the image i attached previously you can see how when the stylus was far from the skull the cross section was shallow, the closer it goes the deeper the cross section without affecting the segmented tumor.<br>
Please see the Youtube video between seconds 1:20 to 1:30 the 3D overview section.</p><div class="youtube-onebox lazy-video-container" data-video-id="_BFTK6LWH5g" data-video-title="Image Guided Surgery for Brain Tumors" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=_BFTK6LWH5g" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/_BFTK6LWH5g/hqdefault.jpg" title="Image Guided Surgery for Brain Tumors" width="" height="">
  </a>
</div>

<p>Thank you so much</p>

---

## Post #4 by @ungi (2021-07-04 02:07 UTC)

<p>What happens in the 3D view in the video can be achieved by enabling “Crop” in the Volume Rendering module, and apply a transform node on the ROI used for cropping the volume in the 3D view. If that transform node is transformed by the StylusTipTo… transform, then the volume will be cropped relative to the StylusTip position. The tumor contour is a different node, a yellow surface model not cropped by the ROI, so that is always visible.</p>

---

## Post #5 by @Ahmet_Yildiz (2021-07-04 02:26 UTC)

<p>I will test it right the way!,<br>
Thank you all so much for your support.</p>

---

## Post #6 by @aysegul_sayin (2022-03-28 12:09 UTC)

<p>Hi,Ahmet_Yildiz<br>
We have a problem similar to yours. What type of navigation device are you using here? Can I contact you if possible?</p>

---
