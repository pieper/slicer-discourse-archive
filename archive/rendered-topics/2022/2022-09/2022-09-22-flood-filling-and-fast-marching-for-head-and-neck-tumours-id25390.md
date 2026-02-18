# Flood filling and fast marching for Head and Neck tumours

**Topic ID**: 25390
**Date**: 2022-09-22
**URL**: https://discourse.slicer.org/t/flood-filling-and-fast-marching-for-head-and-neck-tumours/25390

---

## Post #1 by @MPhilip (2022-09-22 09:13 UTC)

<p>Hi,</p>
<p>I was trying to use fast marching to segment Head and Neck tumours. But I don’t think I’m getting a satisfactory result. Below is an image of the segmentation done using fast marching. What could be the issue?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1242579ad5622971885716d3bddb6d4ee97e969.jpeg" data-download-href="/uploads/short-url/ryBATtaxkny6pnV24Nd5Wue5IEh.jpeg?dl=1" title="Capture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1242579ad5622971885716d3bddb6d4ee97e969_2_690x228.jpeg" alt="Capture1" data-base62-sha1="ryBATtaxkny6pnV24Nd5Wue5IEh" width="690" height="228" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1242579ad5622971885716d3bddb6d4ee97e969_2_690x228.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1242579ad5622971885716d3bddb6d4ee97e969_2_1035x342.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1242579ad5622971885716d3bddb6d4ee97e969_2_1380x456.jpeg 2x" data-dominant-color="A9AAB0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture1</span><span class="informations">1913×633 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>While I used the flood filling method, if the set intensity tolerance is 2 or 3 and if doesn’t give me the needed result, can I adjust the intensity tolerance level and neighbourhood size? I tried that but it doesn’t seem to affect the image. It seems like I must know the intensity tolerance and neighbourhood size before clicking on the image. Is there a way to readjust those parameters to generate the intended result?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7be25b00caa21d45fb9133ae3c7df064e934447c.png" data-download-href="/uploads/short-url/hFVGYPZTFfutBQJd3FFvnqtqiC0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7be25b00caa21d45fb9133ae3c7df064e934447c_2_690x282.png" alt="image" data-base62-sha1="hFVGYPZTFfutBQJd3FFvnqtqiC0" width="690" height="282" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7be25b00caa21d45fb9133ae3c7df064e934447c_2_690x282.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7be25b00caa21d45fb9133ae3c7df064e934447c_2_1035x423.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7be25b00caa21d45fb9133ae3c7df064e934447c_2_1380x564.png 2x" data-dominant-color="B4B4BA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1916×785 97.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Are these semi-automatic methods suitable for segmenting head and neck tumours? Is there any other semi-automatic segmentation method other than watershed, grow from seeds(though both seemed identical to me), threshold and just enough interaction methods which will work fine on head and neck tumours?</p>
<p>Slicer version: 4.13.0-2022-01-27<br>
Many thanks in advance</p>

---
