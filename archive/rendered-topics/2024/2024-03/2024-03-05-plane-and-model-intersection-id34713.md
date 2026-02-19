---
topic_id: 34713
title: "Plane And Model Intersection"
date: 2024-03-05
url: https://discourse.slicer.org/t/34713
---

# Plane and model intersection

**Topic ID**: 34713
**Date**: 2024-03-05
**URL**: https://discourse.slicer.org/t/plane-and-model-intersection/34713

---

## Post #1 by @soukup.la (2024-03-05 11:28 UTC)

<p>Hello,<br>
I have cropped a surface model using the four planes. Now, I need to get curves or lines that correspond with the coroped model and the plane touch. So the model’s boundary edge is divided into four curves by the planes. Or, at least four corner points.</p>
<p>thank you<br>
Ladislav</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af8527eb11ecf81058f4409b80f959f29c2bf3f9.png" data-download-href="/uploads/short-url/p2IQeVNGEbUy7Av03btDf5eE5HX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af8527eb11ecf81058f4409b80f959f29c2bf3f9.png" alt="image" data-base62-sha1="p2IQeVNGEbUy7Av03btDf5eE5HX" width="651" height="500" data-dominant-color="8A7FAE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">865×664 27.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @RafaelPalomar (2024-03-05 11:46 UTC)

<p>Hello <a class="mention" href="/u/soukup.la">@soukup.la</a>. To do this you probably are going to need your own python script that:</p>
<ol>
<li>Retrieves the markups planes and the model</li>
<li>Generates new models (corresponding to the sliced contours)</li>
<li>Use <a href="https://vtk.org/doc/nightly/html/classvtkCutter.html" rel="noopener nofollow ugc">vtkCutter</a> with the geometry of the planes to generate the contours and populate your new models</li>
</ol>
<p>If you want this to be interactive, the script will be only a little more complicated as you would need to observe the markups planes and update your contour modules accordingly.</p>

---

## Post #3 by @soukup.la (2024-03-06 11:01 UTC)

<p>Hello,<br>
I have one more question related to this. When I applied vtkPoissonDiskSampler to the corpped model, it included points related to the original model too. How is it possible?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53cfd73df60421587818420cac3de25736b78533.png" data-download-href="/uploads/short-url/bXqVsWvZAPQENbVZduMOJpn8RkT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53cfd73df60421587818420cac3de25736b78533_2_508x500.png" alt="image" data-base62-sha1="bXqVsWvZAPQENbVZduMOJpn8RkT" width="508" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53cfd73df60421587818420cac3de25736b78533_2_508x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53cfd73df60421587818420cac3de25736b78533.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53cfd73df60421587818420cac3de25736b78533.png 2x" data-dominant-color="8F95BC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">529×520 34.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @RafaelPalomar (2024-03-13 07:47 UTC)

<p>Check carefully that you are applying the sampler to a cropped model. Could you provide more details about how yo do the cropping and apply the Poisson sampler? Are you using any script or a combination of script and the Slicer gui?</p>
<p>Maybe a good test could be to save the cropped model in a .vtk file then load it in a clean scene and see the effect of the Poisson sampler.</p>

---
