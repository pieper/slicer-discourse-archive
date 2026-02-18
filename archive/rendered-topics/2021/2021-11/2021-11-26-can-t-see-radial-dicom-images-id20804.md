# Can´t see radial dicom images

**Topic ID**: 20804
**Date**: 2021-11-26
**URL**: https://discourse.slicer.org/t/can-t-see-radial-dicom-images/20804

---

## Post #1 by @Maria_Lopes (2021-11-26 19:04 UTC)

<p>Hi.<br>
I loaded radial dicom images from MRI and, I can´t see the whole volume. Just appears one image at a time and on the other anatomical planes the black screen and the bar.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3b7d23d556580564e47af54e18abf6b566b86c2.png" data-download-href="/uploads/short-url/pDRiKuPZPz0jR9pf3nbDBrYPVhU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3b7d23d556580564e47af54e18abf6b566b86c2_2_690x257.png" alt="image" data-base62-sha1="pDRiKuPZPz0jR9pf3nbDBrYPVhU" width="690" height="257" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3b7d23d556580564e47af54e18abf6b566b86c2_2_690x257.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3b7d23d556580564e47af54e18abf6b566b86c2_2_1035x385.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3b7d23d556580564e47af54e18abf6b566b86c2.png 2x" data-dominant-color="171716"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1277×476 44.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Or occurs this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/200fca3980fd8e30b02e6256ad27ff7935ecaf4e.jpeg" data-download-href="/uploads/short-url/4zD6KoJorNfY0pYPOb28Rsm1p7w.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/200fca3980fd8e30b02e6256ad27ff7935ecaf4e_2_690x319.jpeg" alt="image" data-base62-sha1="4zD6KoJorNfY0pYPOb28Rsm1p7w" width="690" height="319" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/200fca3980fd8e30b02e6256ad27ff7935ecaf4e_2_690x319.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/200fca3980fd8e30b02e6256ad27ff7935ecaf4e_2_1035x478.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/200fca3980fd8e30b02e6256ad27ff7935ecaf4e_2_1380x638.jpeg 2x" data-dominant-color="61616A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1909×884 230 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Someone can help me?</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2021-11-28 04:04 UTC)

<p>The slice view shows the intersection of the slice plane and the selected image. Since the acquired image is only a single slice, the intersection is just a line. You can make the slice view dynamically follow the image by using Volume Reslice Driver module in SlicerIGT extension.</p>
<p>Slicer can also reconstruct the rotational acquisition to a 3D volume or 4D volume sequence using the <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/Reconstruct4DCineMRI.md">“Reconstruct 4D cine-MRI” module</a> in SlicerHeart extension.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="hIxr9OKBvQ8" data-video-title="Reconstruct 3D or 4D cardiac volumes from sparse 2D frame set" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=hIxr9OKBvQ8" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/hIxr9OKBvQ8/maxresdefault.jpg" title="Reconstruct 3D or 4D cardiac volumes from sparse 2D frame set" width="" height="">
  </a>
</div>


---

## Post #3 by @Maria_Lopes (2021-11-29 12:28 UTC)

<p>Thank you so much for your help.<br>
I tried that, but appear this error and then the images are blurry and I cant segment it. Because I cant distinguish the cartilage of hip, due to bad quality of images when submited of this process .<br>
I need segment  the radial images of hip.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd9c0a094fc15c020d5c95c07f0fd32cc5bf574e.png" data-download-href="/uploads/short-url/Abx6YmyLdFT8ovW785tfyeuufAG.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd9c0a094fc15c020d5c95c07f0fd32cc5bf574e_2_690x368.png" alt="image" data-base62-sha1="Abx6YmyLdFT8ovW785tfyeuufAG" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd9c0a094fc15c020d5c95c07f0fd32cc5bf574e_2_690x368.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd9c0a094fc15c020d5c95c07f0fd32cc5bf574e_2_1035x552.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd9c0a094fc15c020d5c95c07f0fd32cc5bf574e_2_1380x736.png 2x" data-dominant-color="9F9FAE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1916×1023 265 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/5496ab4e149150d221a8efc61d2824de5d6267b8.jpeg" data-download-href="/uploads/short-url/c4iUI7IrDuA2ZpWREX0avIseEiI.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5496ab4e149150d221a8efc61d2824de5d6267b8_2_690x351.jpeg" alt="image" data-base62-sha1="c4iUI7IrDuA2ZpWREX0avIseEiI" width="690" height="351" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5496ab4e149150d221a8efc61d2824de5d6267b8_2_690x351.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5496ab4e149150d221a8efc61d2824de5d6267b8_2_1035x526.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5496ab4e149150d221a8efc61d2824de5d6267b8_2_1380x702.jpeg 2x" data-dominant-color="ACADBD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×977 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2021-11-29 12:54 UTC)

<p>You can increase the resolution of the output image by setting a smaller spacing value.</p>
<p>How do you envision to use the images if not reconstructing a Cartesian volume from them? What is the overall goal of your What is the overall goal of your project?</p>

---

## Post #5 by @Maria_Lopes (2021-11-29 13:30 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/3476ed5cf676f7d809b7eba280701fcba84d34c3.jpeg" data-download-href="/uploads/short-url/7u7CZ9UjmZDD4Pb2EEqD6xC3w4z.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3476ed5cf676f7d809b7eba280701fcba84d34c3_2_690x359.jpeg" alt="image" data-base62-sha1="7u7CZ9UjmZDD4Pb2EEqD6xC3w4z" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3476ed5cf676f7d809b7eba280701fcba84d34c3_2_690x359.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3476ed5cf676f7d809b7eba280701fcba84d34c3_2_1035x538.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3476ed5cf676f7d809b7eba280701fcba84d34c3_2_1380x718.jpeg 2x" data-dominant-color="A1A1B1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1000 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This is the cartesian volume that are you talking about?</p>
<p>My goal is to reconstruct the human hip in 3D using radial MRI images. Later, I also need to reconstruct the hip joint articular cartilage.<br>
The doctor said that the best images to segment are the radials.</p>
<p>I thought to go to the semgment editor and segment the images obtained through the" Reconstruct 4D cine-MRI".</p>
<p>thank you for your kindness</p>

---

## Post #6 by @lassoan (2021-11-29 13:49 UTC)

<aside class="quote no-group" data-username="Maria_Lopes" data-post="5" data-topic="20804">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/maria_lopes/48/9640_2.png" class="avatar"> Maria_Lopes:</div>
<blockquote>
<p>This is the cartesian volume that are you talking about?</p>
</blockquote>
</aside>
<p>Yes, it is the volume reconstructed to have parallel slices.</p>
<aside class="quote no-group" data-username="Maria_Lopes" data-post="5" data-topic="20804">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/maria_lopes/48/9640_2.png" class="avatar"> Maria_Lopes:</div>
<blockquote>
<p>My goal is to reconstruct the human hip in 3D using radial MRI images. Later, I also need to reconstruct the hip joint articular cartilage.</p>
</blockquote>
</aside>
<p>Without having a Cartesian volume, you can only do very limited measurements or processing, as you can only process each 2D slice separately. For example, you can measure local features (thickness, diameter, cross-sectional area) or define contours that may be used for reconstructing very thin structures.</p>
<p>For reconstructing 3D shapes, measuring volumes, 3D surface areas, etc. a Cartesian volume representation (this is what “Reconstruct 4D cine-MRI” module creates) is generally more suitable.</p>

---

## Post #7 by @Maria_Lopes (2021-11-29 16:13 UTC)

<p>But… Why the volume is not clear? I can´t see the bone.</p>
<p>I don´t want the radial images reconstructed on the axial, sagital and coronal planes. I want segment radial images.<br>
I tried  the Volume Reslice Driver that you indicated, and then I went to the segment editor (using grow from seeds) , to segment only radial images but it´s not possible. I don´t know why… How can I do?</p>
<p>I can only paint the rectangular slice that appears in the image. It´s not possible paint the other parts of the bone.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76d25a96b6072fc8f010f02a31d9f5289a07ac3a.jpeg" data-download-href="/uploads/short-url/gX91oOrcCW9DMfL7ThF7LtErtai.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76d25a96b6072fc8f010f02a31d9f5289a07ac3a_2_690x316.jpeg" alt="image" data-base62-sha1="gX91oOrcCW9DMfL7ThF7LtErtai" width="690" height="316" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76d25a96b6072fc8f010f02a31d9f5289a07ac3a_2_690x316.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76d25a96b6072fc8f010f02a31d9f5289a07ac3a_2_1035x474.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76d25a96b6072fc8f010f02a31d9f5289a07ac3a_2_1380x632.jpeg 2x" data-dominant-color="A1A3B1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×882 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @lassoan (2021-11-29 16:27 UTC)

<aside class="quote no-group" data-username="Maria_Lopes" data-post="7" data-topic="20804">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/maria_lopes/48/9640_2.png" class="avatar"> Maria_Lopes:</div>
<blockquote>
<p>But… Why the volume is not clear? I can´t see the bone.</p>
</blockquote>
</aside>
<p>You can set as high output resolution as you need.</p>
<aside class="quote no-group" data-username="Maria_Lopes" data-post="7" data-topic="20804">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/maria_lopes/48/9640_2.png" class="avatar"> Maria_Lopes:</div>
<blockquote>
<p>I don´t want the radial images reconstructed on the axial, sagital and coronal planes. I want segment radial images.</p>
</blockquote>
</aside>
<p>It would be awesome if high-resolution arbitrarily oriented slices could be used for creating high-resolution 3D segmentations. However, the issue is that between your high-resolution slices there are huge gaps where you don’t know anything about the bone shape. How do you want do deal with this?</p>
<p>I would recommend to build a 3D Cartesian volume and segment that. Nice and simple. You can choose any resolution that your computer can handle.</p>
<p>You can choose to segment each slice. For this, you need to create a segmentation sequence (add a segmentation node under the same sequence browser node of your image sequence). But this would just give you a set of disconnected binary labelmaps. What would you do with such a series of single-slice binary labelmaps?</p>
<p>You could also “segment” a structure by adding a closed curve node at each slice (then you don’t need to set up a new a sequence, you could just add a new node for each slice). However, the problem remains: what do you do with those closed contours?</p>
<p>We need more information about your overall goal - what is the clinical problem you want to address and how, and then we can give further advice on how to achieve that.</p>

---
