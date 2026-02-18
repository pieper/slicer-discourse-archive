# Problem in computing centerline

**Topic ID**: 22603
**Date**: 2022-03-19
**URL**: https://discourse.slicer.org/t/problem-in-computing-centerline/22603

---

## Post #1 by @A_Khabarkhaan (2022-03-19 22:42 UTC)

<p>Hi<br>
I’m trying to create centerline of a shape (the sample cerebral aneurysm in the site and others) I face to the below warning:</p>
<p>Warning: in …\Common\DataModel\vtkPolyData.cxx, line 982<br>
vtkPolyData (0000024c243cd6b0): bulding vtk_line 0 with only one point, but vtk_line needs at least two points. Check the input.</p>
<p>I test with various input models but the results were the same!</p>
<p>Please guide me to resolve it.<br>
Thanks</p>

---

## Post #2 by @lassoan (2022-03-19 22:43 UTC)

<p>Have you tried using VMTK via 3D Slicer’s VMTK extension?</p>

---

## Post #3 by @A_Khabarkhaan (2022-03-20 08:40 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="22603">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>VMTK</p>
</blockquote>
</aside>
<p>Thank you for your response.<br>
No, I installed the package with name ‘VMTK-1.4.0-Python3.6-Windows-x86_64.exe’ and used it.<br>
I created some screenshots from the procedure and uploaded with this message.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c25997dc0b96ab3e1170b1cb0a13bf005af653f0.jpeg" data-download-href="/uploads/short-url/rJiA4uZwTKKgnk6grGYYdT8dEo8.jpeg?dl=1" title="001" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c25997dc0b96ab3e1170b1cb0a13bf005af653f0_2_634x500.jpeg" alt="001" data-base62-sha1="rJiA4uZwTKKgnk6grGYYdT8dEo8" width="634" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c25997dc0b96ab3e1170b1cb0a13bf005af653f0_2_634x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c25997dc0b96ab3e1170b1cb0a13bf005af653f0.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c25997dc0b96ab3e1170b1cb0a13bf005af653f0.jpeg 2x" data-dominant-color="F1F6FA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">001</span><span class="informations">700×552 55.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4fd925c2da6daae23a171cfe3d30e7f1e57002e6.jpeg" data-download-href="/uploads/short-url/bomXiYd4QN8QJF7EUUMjuKIuzCm.jpeg?dl=1" title="003" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4fd925c2da6daae23a171cfe3d30e7f1e57002e6_2_641x500.jpeg" alt="003" data-base62-sha1="bomXiYd4QN8QJF7EUUMjuKIuzCm" width="641" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4fd925c2da6daae23a171cfe3d30e7f1e57002e6_2_641x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4fd925c2da6daae23a171cfe3d30e7f1e57002e6_2_961x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4fd925c2da6daae23a171cfe3d30e7f1e57002e6.jpeg 2x" data-dominant-color="31344B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">003</span><span class="informations">1201×936 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/334096adf9b706c81adba9b719e38a2557e727e5.jpeg" data-download-href="/uploads/short-url/7joJlyhZPJuwp3coYnHMRyfRB09.jpeg?dl=1" title="004" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/334096adf9b706c81adba9b719e38a2557e727e5_2_642x500.jpeg" alt="004" data-base62-sha1="7joJlyhZPJuwp3coYnHMRyfRB09" width="642" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/334096adf9b706c81adba9b719e38a2557e727e5_2_642x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/334096adf9b706c81adba9b719e38a2557e727e5.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/334096adf9b706c81adba9b719e38a2557e727e5.jpeg 2x" data-dominant-color="E5E9EC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">004</span><span class="informations">886×690 71.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2022-03-20 11:52 UTC)

<p>I don’t know what is that package, but you can segment vessels and extract centerline using a convenient GUI in 3D Slicer, using VMTK extension. Short demo:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="yi07mjr3JeU" data-video-title="New vessel branch extraction module for 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=yi07mjr3JeU" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/yi07mjr3JeU/maxresdefault.jpg" title="New vessel branch extraction module for 3D Slicer" width="" height="">
  </a>
</div>


---

## Post #5 by @A_Khabarkhaan (2022-03-21 03:23 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="22603">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>nt GUI in 3D Slicer, using VMTK extension. Short demo:</p>
</blockquote>
</aside>
<p>By using 3D slicer, the problem has been solved.<br>
Thanks</p>

---
