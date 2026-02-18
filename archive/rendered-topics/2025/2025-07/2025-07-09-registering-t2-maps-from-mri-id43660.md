# Registering T2* Maps from MRI

**Topic ID**: 43660
**Date**: 2025-07-09
**URL**: https://discourse.slicer.org/t/registering-t2-maps-from-mri/43660

---

## Post #1 by @aceegreene (2025-07-09 03:17 UTC)

<p>Hi everyone - I’m very new to 3D Slicer and had a question about coregistration. We have 3D T2* maps of menisci which I want to coregister and come up with a 3D T2* map that is the average of all the individual 3D T2* maps of all the menisci we have. I have been playing around a bit in 3D Slicer with just two as a test run but having used Elastix and General (BRAINS) registration both it seems that once I register the moving volume to the fixed one, the color of the registered image in volume rendering seems to be pretty different (which I assume means it affects intensities of the T2* mapping). So I’m here wondering what the best way to go about this would be or am I on the right track and not to worry?</p>
<p>Let me know if I’m not making sense coz like I said I’m pretty new to all this. Thank you all in advance!</p>

---

## Post #2 by @Deep_Learning (2025-07-09 12:01 UTC)

<p>can you post a picture?<br>
Slicer can def do what you described: register and average.<br>
It is probably just the colormap.</p>
<p>Are they well aligned?</p>

---

## Post #3 by @aceegreene (2025-07-11 16:59 UTC)

<p>Hi, thanks for your response! Posting pictures below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d80d1107d3997d9eb3e848e18e6f61f481c023be.jpeg" data-download-href="/uploads/short-url/uPh7Y1I0avJOhY7Tp7U6qV9t8rc.jpeg?dl=1" title="Fixed Volume" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d80d1107d3997d9eb3e848e18e6f61f481c023be_2_690x460.jpeg" alt="Fixed Volume" data-base62-sha1="uPh7Y1I0avJOhY7Tp7U6qV9t8rc" width="690" height="460" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d80d1107d3997d9eb3e848e18e6f61f481c023be_2_690x460.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d80d1107d3997d9eb3e848e18e6f61f481c023be_2_1035x690.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d80d1107d3997d9eb3e848e18e6f61f481c023be_2_1380x920.jpeg 2x" data-dominant-color="9197C8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Fixed Volume</span><span class="informations">1878×1254 78.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d7f57cb15f5eae4a84f911f705c6a2848760983.jpeg" data-download-href="/uploads/short-url/6uujFbDJQ2P6mOzOhBwOT1MU0Uj.jpeg?dl=1" title="Moving Volume Transformed" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d7f57cb15f5eae4a84f911f705c6a2848760983_2_690x459.jpeg" alt="Moving Volume Transformed" data-base62-sha1="6uujFbDJQ2P6mOzOhBwOT1MU0Uj" width="690" height="459" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d7f57cb15f5eae4a84f911f705c6a2848760983_2_690x459.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d7f57cb15f5eae4a84f911f705c6a2848760983_2_1035x688.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d7f57cb15f5eae4a84f911f705c6a2848760983_2_1380x918.jpeg 2x" data-dominant-color="9296C6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Moving Volume Transformed</span><span class="informations">1890×1258 86.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/539b91b32a9450e5be8041d1b93ae5bf8cc0d2df.jpeg" data-download-href="/uploads/short-url/bVCVZEhT4uk3VYYfqYnsqpK22f5.jpeg?dl=1" title="Registered Volume" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/539b91b32a9450e5be8041d1b93ae5bf8cc0d2df_2_690x458.jpeg" alt="Registered Volume" data-base62-sha1="bVCVZEhT4uk3VYYfqYnsqpK22f5" width="690" height="458" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/539b91b32a9450e5be8041d1b93ae5bf8cc0d2df_2_690x458.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/539b91b32a9450e5be8041d1b93ae5bf8cc0d2df_2_1035x687.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/539b91b32a9450e5be8041d1b93ae5bf8cc0d2df_2_1380x916.jpeg 2x" data-dominant-color="9196C6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Registered Volume</span><span class="informations">1888×1254 82.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e2a82b2ac034358875b13d18cadc74f2c3d90fd.jpeg" data-download-href="/uploads/short-url/fIzBd0DwO2LCrs6Ak2DkjSy9zvn.jpeg?dl=1" title="Sum" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e2a82b2ac034358875b13d18cadc74f2c3d90fd_2_690x459.jpeg" alt="Sum" data-base62-sha1="fIzBd0DwO2LCrs6Ak2DkjSy9zvn" width="690" height="459" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e2a82b2ac034358875b13d18cadc74f2c3d90fd_2_690x459.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e2a82b2ac034358875b13d18cadc74f2c3d90fd_2_1035x688.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e2a82b2ac034358875b13d18cadc74f2c3d90fd_2_1380x918.jpeg 2x" data-dominant-color="9294C2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Sum</span><span class="informations">1884×1254 93.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93f569549c521b1d3ab41675b11e91db07028617.jpeg" data-download-href="/uploads/short-url/l6TYKbvIGwOQLPIzOO976pYlkfJ.jpeg?dl=1" title="Avg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93f569549c521b1d3ab41675b11e91db07028617_2_690x455.jpeg" alt="Avg" data-base62-sha1="l6TYKbvIGwOQLPIzOO976pYlkfJ" width="690" height="455" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93f569549c521b1d3ab41675b11e91db07028617_2_690x455.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93f569549c521b1d3ab41675b11e91db07028617_2_1035x682.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93f569549c521b1d3ab41675b11e91db07028617_2_1380x910.jpeg 2x" data-dominant-color="8A95C9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Avg</span><span class="informations">1880×1242 77.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So I summed the original fixed volume with the registered moving volume using the AddImageFilter and then the sum volume I got I averaged using the ShiftScaleImageFilter by setting the scale to 0.5 (both filters from the Simple Filters module).</p>
<p>Also originally the moving volume was not well aligned with the fixed volume so I transformed it to align them as close together as possible before registering.</p>
<p>Let me know if this was the right approach or a better way to do it and if it is the right approach, how do I verify from something other than the colors in the image that I did the right thing.</p>
<p>Hope all this makes sense and thanks again!</p>

---

## Post #4 by @aceegreene (2025-07-14 06:03 UTC)

<p>looking for some input from someone on this. thank you!</p>

---

## Post #5 by @aceegreene (2025-07-18 18:29 UTC)

<p>Would someone be able to help with this?</p>

---

## Post #6 by @Deep_Learning (2025-07-18 18:59 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff66f885302c9f70131b58895927f3029f8afc4f.png" data-download-href="/uploads/short-url/AromRQPxfq3RMQQi4hkjuoVi5dl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff66f885302c9f70131b58895927f3029f8afc4f_2_295x500.png" alt="image" data-base62-sha1="AromRQPxfq3RMQQi4hkjuoVi5dl" width="295" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff66f885302c9f70131b58895927f3029f8afc4f_2_295x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff66f885302c9f70131b58895927f3029f8afc4f_2_442x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff66f885302c9f70131b58895927f3029f8afc4f_2_590x1000.png 2x" data-dominant-color="CACCD2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">807×1366 54.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
It’s not 100% clear what your problem is.<br>
Looking at the 3d rendering is not very helpful.</p>
<p>I would eval the fixed, moving, registered and averaged in compare using 4 viewers.</p>
<p>You can load all four via drag and drop and evaluate.  You can scroll through and the put a cursor down with shift left click.</p>
<p>Try this to evaluate the registration quality. and when you mouse over, you can see the values.</p>

---
