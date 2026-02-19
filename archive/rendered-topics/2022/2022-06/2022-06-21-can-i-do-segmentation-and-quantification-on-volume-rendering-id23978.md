---
topic_id: 23978
title: "Can I Do Segmentation And Quantification On Volume Rendering"
date: 2022-06-21
url: https://discourse.slicer.org/t/23978
---

# Can I do segmentation and quantification on volume-rendering image?

**Topic ID**: 23978
**Date**: 2022-06-21
**URL**: https://discourse.slicer.org/t/can-i-do-segmentation-and-quantification-on-volume-rendering-image/23978

---

## Post #1 by @user4 (2022-06-21 05:06 UTC)

<p>Hi all,<br>
I can use Segement Editor Module to make a segmentation in 2D view here<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8b8b9988d13f2d8e6e9e6fb25eeae4e6551849e.jpeg" data-download-href="/uploads/short-url/o4zZa3NDuaDlckDI0VEd2XVMDOS.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a8b8b9988d13f2d8e6e9e6fb25eeae4e6551849e_2_690x388.jpeg" alt="image" data-base62-sha1="o4zZa3NDuaDlckDI0VEd2XVMDOS" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a8b8b9988d13f2d8e6e9e6fb25eeae4e6551849e_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a8b8b9988d13f2d8e6e9e6fb25eeae4e6551849e_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a8b8b9988d13f2d8e6e9e6fb25eeae4e6551849e_2_1380x776.jpeg 2x" data-dominant-color="787878"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 89.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Then, I can use Segement Statistics Module to do some quantitative things here.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fdf760e0b75abf918ee301f3c9c8c296c5d6e89e.png" data-download-href="/uploads/short-url/AeGNXJKRnPVerkqXUdz2RmqcSoS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fdf760e0b75abf918ee301f3c9c8c296c5d6e89e_2_690x388.png" alt="image" data-base62-sha1="AeGNXJKRnPVerkqXUdz2RmqcSoS" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fdf760e0b75abf918ee301f3c9c8c296c5d6e89e_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fdf760e0b75abf918ee301f3c9c8c296c5d6e89e_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fdf760e0b75abf918ee301f3c9c8c296c5d6e89e_2_1380x776.png 2x" data-dominant-color="B0B0B2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2560×1440 377 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
As the above results shown,I can get the Minimum,Maximum and Mean so on.<br>
Now,I do some Scalar Opacity Mapping to see bones inside the sample data volume as follows,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/04fe10f5f55f62235a5a7a00d8ba3ba80de9e71c.png" data-download-href="/uploads/short-url/Iaf99VKLb6rXnDxNtFkepw1Xsg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/04fe10f5f55f62235a5a7a00d8ba3ba80de9e71c_2_690x388.png" alt="image" data-base62-sha1="Iaf99VKLb6rXnDxNtFkepw1Xsg" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/04fe10f5f55f62235a5a7a00d8ba3ba80de9e71c_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/04fe10f5f55f62235a5a7a00d8ba3ba80de9e71c_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/04fe10f5f55f62235a5a7a00d8ba3ba80de9e71c_2_1380x776.png 2x" data-dominant-color="BFC1DF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2560×1440 411 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Here is my question,I want to do a segmentation like this,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8da04d922d85c5c406c3d453f4ad70c266265441.png" data-download-href="/uploads/short-url/kcSLNxs5s0G7COyQCKuMSMiIkI9.png?dl=1" title="1655787510312" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8da04d922d85c5c406c3d453f4ad70c266265441_2_690x388.png" alt="1655787510312" data-base62-sha1="kcSLNxs5s0G7COyQCKuMSMiIkI9" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8da04d922d85c5c406c3d453f4ad70c266265441_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8da04d922d85c5c406c3d453f4ad70c266265441_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8da04d922d85c5c406c3d453f4ad70c266265441_2_1380x776.png 2x" data-dominant-color="C1C3E1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1655787510312</span><span class="informations">2560×1440 301 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I am more interested in the bones or some other parts of the volume after rendering and I want to do some quantification.For example,the bones marked in red,I need to know the Minimum,Maximum,etc.<br>
Sure I know I can take a screenshot and do the quantification outside Slicer,but I wonder if it is possible to do it inside Slicer.<br>
Can someone give me any advice?<br>
Thank you in advance for your help!</p>

---

## Post #2 by @lassoan (2022-06-21 05:33 UTC)

<p>Segmenting the bones in CT is usually easy. The main challenges are holes inside the bones (below the dense cortical bone the internal cancellous bone regions can be quite sparse) and separation of bones. There are many approaches, so to be able to advise you, we would need to know a bit more about your clinical goal (what you want to measure exactly, for what purpose, with what accuracy, etc.).</p>

---

## Post #3 by @user4 (2022-06-21 06:12 UTC)

<p>Thanks Andras,<br>
In fact, the bones are just an example, I am more concerned about whether there is a module or python code for Slicer that supports such operations.I want to segment the ROI on the rendered image, then measure and calculate the mean of the ROI. It doesn’t matter what data I use, nor the area of the ROI.</p>

---

## Post #4 by @muratmaga (2022-06-21 18:27 UTC)

<p>Short answer no. But as <a class="mention" href="/u/lassoan">@lassoan</a> said bone segmentation is really simple, usually a threshold follow by collected components, with or without morphological operations (dilation/erosion). After that you can use the segment statistics to get min/max/mean intensity within that segment.</p>
<p>If you are only interested long bones, you can potentially use the crop volume with an ROI that’s under  a transformation, and crop out just that region. It will be far less precise than segmentation (since ROI can only be a rectangular prism).</p>

---
