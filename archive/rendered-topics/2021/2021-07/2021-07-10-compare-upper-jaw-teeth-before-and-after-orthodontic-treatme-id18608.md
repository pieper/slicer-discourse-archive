---
topic_id: 18608
title: "Compare Upper Jaw Teeth Before And After Orthodontic Treatme"
date: 2021-07-10
url: https://discourse.slicer.org/t/18608
---

# Compare upper jaw teeth before and after orthodontic treatment

**Topic ID**: 18608
**Date**: 2021-07-10
**URL**: https://discourse.slicer.org/t/compare-upper-jaw-teeth-before-and-after-orthodontic-treatment/18608

---

## Post #1 by @Nikhil_Jain (2021-07-10 03:58 UTC)

<p>how to overlap 2 volumes to observe changes using fixed landmarks? (the two volumes being 3d stl files of upper jaw teeth before and after orthodontic treatment)</p>
<p>Operating system:Windows 10<br>
Slicer version:4.13<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2021-07-12 14:04 UTC)

<p>Before you can compare two models (STL files) you need spatially align them using registration. You can find a list of recommended modules <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#model-registration">here</a>. You may also find useful information in previous discussion of this topic on this forum.</p>

---

## Post #3 by @Nikhil_Jain (2021-09-03 10:37 UTC)

<p>Thanks for the reply. I have superimposed the two files after getting them in spatial alignment. Now i want to draw a line over the mid palatine raphe, and measure the distance between the before and after position of a point on the model (eg- cusp tip of canine) on that line. Basically i want to measure the movement of the cusp tip in one 1 dimension viz the line over the mid palatine raphe<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c75e36249183d6626f62ef34b740deb7b227bd30.jpeg" data-download-href="/uploads/short-url/srGRyvUcp58zmJVVZhHVYq0AdbO.jpeg?dl=1" title="Aniket" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c75e36249183d6626f62ef34b740deb7b227bd30_2_690x402.jpeg" alt="Aniket" data-base62-sha1="srGRyvUcp58zmJVVZhHVYq0AdbO" width="690" height="402" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c75e36249183d6626f62ef34b740deb7b227bd30_2_690x402.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c75e36249183d6626f62ef34b740deb7b227bd30_2_1035x603.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c75e36249183d6626f62ef34b740deb7b227bd30_2_1380x804.jpeg 2x" data-dominant-color="6B6B60"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Aniket</span><span class="informations">1450×846 254 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> . Thanks</p>

---

## Post #4 by @lassoan (2021-09-05 01:32 UTC)

<p>You can compute distance of points from a line by copy-pasting this <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#measure-distances-of-points-from-a-line">code snippet in the script repository</a> into the Python console.</p>

---

## Post #5 by @Nikhil_Jain (2021-09-05 13:59 UTC)

<p>I want to convert my surface scan file into a 2D file. and then do measurements on the same. Kindly advise. Thanks</p>

---

## Post #6 by @lassoan (2021-09-05 19:33 UTC)

<p>Do you mean you would like to see a cross-section if the surface mesh?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a7484174d22dc7dd0c750afb3e89ea8268639406.png" data-download-href="/uploads/short-url/nRQxLGKmE4ZQVssBmWTNaw1aecC.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a7484174d22dc7dd0c750afb3e89ea8268639406_2_690x268.png" alt="image" data-base62-sha1="nRQxLGKmE4ZQVssBmWTNaw1aecC" width="690" height="268" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a7484174d22dc7dd0c750afb3e89ea8268639406_2_690x268.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a7484174d22dc7dd0c750afb3e89ea8268639406_2_1035x402.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a7484174d22dc7dd0c750afb3e89ea8268639406_2_1380x536.png 2x" data-dominant-color="53515D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1563×608 96.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>To achieve this:</p>
<ul>
<li>Show the model in slice views: in data module, right-click on the eye icon of the model and check “2D visibility”</li>
<li>Position the slice view where you want:
<ul>
<li>Option A: Hold down <code>Shift</code> key while moving the mouse over the 3D view (no need to click)</li>
<li>Option B: Use the reformat widget. To show the reformat widget, click the <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">“Reformat” button in the slice view controls</a>.</li>
</ul>
</li>
</ul>

---

## Post #7 by @Nikhil_Jain (2021-09-06 02:30 UTC)

<p>In the attached image, I want to make sure that the two red lines are parallel spatially. And then i want to measure the distance between the two green points i.e. length of the green line. (points where red lines intersect the black line)<br>
The parallelism has to be accurate.</p>
<p>How should I proceed?</p>
<p>Legend:<br>
Black line: mid palatine Raphe<br>
Red line: origin- cusp tip of canine extended to the black line<br>
2nd red line: origin: cusp tip of canine and extended parallel to the 1st red line across the black line.</p>
<p>Thanks</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4be25656e41444229cd57b2944f1a5d286032840.jpeg" data-download-href="/uploads/short-url/aPiJBMav1tk9wqqy5xjQmPaFNx6.jpeg?dl=1" title="IMG-20210905-WA0000.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4be25656e41444229cd57b2944f1a5d286032840_2_686x499.jpeg" alt="IMG-20210905-WA0000.jpg" data-base62-sha1="aPiJBMav1tk9wqqy5xjQmPaFNx6" width="686" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4be25656e41444229cd57b2944f1a5d286032840_2_686x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4be25656e41444229cd57b2944f1a5d286032840_2_1029x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4be25656e41444229cd57b2944f1a5d286032840.jpeg 2x" data-dominant-color="9C9D83"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG-20210905-WA0000.jpg</span><span class="informations">1162×846 232 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0b152ed18bd58dfcaca220713635b671d6a721c.jpeg" data-download-href="/uploads/short-url/mVyjdNiTo3MgWbaZWD4z6D0coB6.jpeg?dl=1" title="IMG-20210905-WA0001.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a0b152ed18bd58dfcaca220713635b671d6a721c_2_686x499.jpeg" alt="IMG-20210905-WA0001.jpg" data-base62-sha1="mVyjdNiTo3MgWbaZWD4z6D0coB6" width="686" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a0b152ed18bd58dfcaca220713635b671d6a721c_2_686x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a0b152ed18bd58dfcaca220713635b671d6a721c_2_1029x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0b152ed18bd58dfcaca220713635b671d6a721c.jpeg 2x" data-dominant-color="B4B251"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG-20210905-WA0001.jpg</span><span class="informations">1162×846 246 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @lassoan (2021-09-07 03:15 UTC)

<p>There are several interpretations of what you describe:</p>
<ul>
<li>A. project the the two cusp points and the mid palatine raphe line to the horizontal plane and perform the measurements in that plane</li>
<li>B. project the two cusp points to the sagittal plane that is fit to the mid palatine raphe, and measure distance between these projected points</li>
<li>C. project the two cusp points to the mid palatine raphe line and measure the distances between these projected points (this will be a 3D distance measurement but the lines will only be parallel in a horizontal view, but may not be exactly parallel in 3D)</li>
</ul>
<p>All of these are equally easy to compute, using basic coordinate geometry from the point and line endpoint coordinates. You can look up the formulae on Wikipedia and find their Python implementation on StackOverflow, but if you have trouble putting this all together then let us know which option you want to implement and we can look up the relevant code snippet for you.</p>

---

## Post #9 by @Nikhil_Jain (2021-09-07 07:46 UTC)

<p>Hello<br>
’ project the two cusp points to the sagittal plane that is fit to the mid palatine raphe, and measure distance between these projected points’ would be the most appropriate methodology for me to get the measurements I want to make.</p>
<p>One small refinement I would want in this would be to differentiate the magnitude of movement in the two axis of the sagittal plane respectively.</p>
<p>Help is much appreciated.<br>
Regards.<br>
Dr. Nikhil Jain</p>

---

## Post #10 by @lassoan (2021-09-08 04:09 UTC)

<p>In this case, the easiest is to probably rotate the model so that it coincides with the RAS axes (mid palatine raphe line will be exactly in the sagittal plane, and an additional line will define the horizontal direction). Then you can simply ignore the first coordinate value of the point and the differences in the second and third coordinate contain exactly the magnitude of movement in the anterior-posterior and inferior-superior directions.</p>
<p>The simplest way to compute this rotation transform without any Python scripting is to use the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/acpctransform.html">ACPC module</a>.</p>

---

## Post #11 by @Nikhil_Jain (2021-09-08 14:02 UTC)

<p>Hello<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a580d1a37848677318e0789d3b6a4986348349b7.png" data-download-href="/uploads/short-url/nC6M6lLJfWK9kLnKVBhAYsxuGLd.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a580d1a37848677318e0789d3b6a4986348349b7_2_436x397.png" alt="image.png" data-base62-sha1="nC6M6lLJfWK9kLnKVBhAYsxuGLd" width="436" height="397" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a580d1a37848677318e0789d3b6a4986348349b7_2_436x397.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a580d1a37848677318e0789d3b6a4986348349b7_2_654x595.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a580d1a37848677318e0789d3b6a4986348349b7.png 2x" data-dominant-color="A4A097"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">796×725 220 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The methodology would be perfect for me. Although, since this is a surface only file, I’m not sure how it will work. Also, I could not locate the ACPC module. Tried looking for it in the extensions page on the SPKC site but I couldn’t find it. How should I proceed? Is it possible to connect on Anydesk so you can show me how it’s supposed to be done and I can do it for all the scans I have. Once again, help is much appreciated.</p>
<p>Regards<br>
Dr. Nikhil Jain</p>

---

## Post #12 by @lassoan (2021-09-08 14:22 UTC)

<p>“ACPC transform” module is part of Slicer core. Hit Ctrl-F to open it using the module finder.</p>
<p>You can pick points on surface the same way as you pick points in slice views.</p>
<p>Unless somebody volunteers to do it earlier, you can join our next <a href="https://discourse.slicer.org/c/community/hangout/20">weekly meeting</a> to get help with screen sharing.</p>

---
