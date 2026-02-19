---
topic_id: 18980
title: "Fiducial Registration Wizard Automatic And Manual Registrati"
date: 2021-07-29
url: https://discourse.slicer.org/t/18980
---

# Fiducial registration wizard automatic and manual registration

**Topic ID**: 18980
**Date**: 2021-07-29
**URL**: https://discourse.slicer.org/t/fiducial-registration-wizard-automatic-and-manual-registration/18980

---

## Post #1 by @parvaneh.a (2021-07-29 21:35 UTC)

<p>Operating system: ubuntu 20<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:<br>
Hi,<br>
I have some questions regarding automatic and manual registration in Fiducial registration wizard. I am using them in my research. I would be thankful if you could provide more information about what exactly manual and automatic do?<br>
when I am using automatic, at the same time, I also define fiducial points in ‘from’ and  ‘to’ sections. Does automatic means that it ignores my selected points and automatically identifies some fiducial points from any part of the volume?</p>
<p>What is the objective function of optimization problem in this wizard?<br>
Is there any paper that explains the mathematical background of the registration applied in  Fiducial registration wizard ?</p>
<p>Thanks,<br>
Best,<br>
Golnoush</p>

---

## Post #2 by @ungi (2021-07-31 21:55 UTC)

<p>Hi,</p>
<p>The implementation is open source, so you may look up the details. For the registration algorithm, this implementation is used: <a href="https://github.com/Kitware/VTK/blob/master/Common/Transforms/vtkLandmarkTransform.cxx" class="inline-onebox" rel="noopener nofollow ugc">VTK/vtkLandmarkTransform.cxx at master · Kitware/VTK · GitHub</a><br>
They say in the comment that the algorithm is based on Horn’s 1987 paper: “Closed-form solution of absolute orientation using unit quaternions”<br>
The objective function is distance between point pairs.</p>
<p>Automatic mode just means that if you add more points, you don’t need to press the update button to recalculate the results. I prefer unchecking the auto-update button, so if I accidentally move a point with my mouse, it doesn’t spoil my registration.</p>

---

## Post #3 by @parvaneh.a (2021-08-01 21:39 UTC)

<p>Thanks a lot  for your helpful answer.<br>
However, I  still have problem in difference between ‘Automatic’ and ‘manual’ in ‘point matching method’ and my below question for automatic one is still not answered. My question was the difference between manual and automatic not auto-update which is right below those two options. Auto-update (which is the one you explained) is available for both automatic and manual registration but what is exactly the difference between automatic and manual options? I have added the picture of the two options of automatic and manual which are my target question .</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a392ac1d474d7075a51e1db8d8c54f84553a7c9.png" data-download-href="/uploads/short-url/8j4aJfsHJKwRchYLKhyC9uoGeg1.png?dl=1" title="Screenshot from 2021-08-01 17-39-25" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a392ac1d474d7075a51e1db8d8c54f84553a7c9_2_402x500.png" alt="Screenshot from 2021-08-01 17-39-25" data-base62-sha1="8j4aJfsHJKwRchYLKhyC9uoGeg1" width="402" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a392ac1d474d7075a51e1db8d8c54f84553a7c9_2_402x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a392ac1d474d7075a51e1db8d8c54f84553a7c9_2_603x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a392ac1d474d7075a51e1db8d8c54f84553a7c9.png 2x" data-dominant-color="EAEAEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2021-08-01 17-39-25</span><span class="informations">691×858 76.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/238020aaedcf45963bcc5da8e860af05e066493f.png" data-download-href="/uploads/short-url/543dRwbpTkVMTROSxTuWNEE90UT.png?dl=1" title="Screenshot from 2021-08-01 17-39-11" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/238020aaedcf45963bcc5da8e860af05e066493f_2_378x500.png" alt="Screenshot from 2021-08-01 17-39-11" data-base62-sha1="543dRwbpTkVMTROSxTuWNEE90UT" width="378" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/238020aaedcf45963bcc5da8e860af05e066493f_2_378x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/238020aaedcf45963bcc5da8e860af05e066493f_2_567x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/238020aaedcf45963bcc5da8e860af05e066493f.png 2x" data-dominant-color="E5E5E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2021-08-01 17-39-11</span><span class="informations">677×894 75 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>when I am using automatic, at the same time, I also define fiducial points in ‘from’ and ‘to’ sections. Does automatic means that it ignores my selected points and automatically identifies some fiducial points from any part of the volume?</p>
<p>Thanks in adavnce</p>

---

## Post #4 by @lassoan (2021-08-02 01:04 UTC)

<p>Automatic point matching determines the order of fixed and moving points automatically (and I think it can also deal with missing points). If you turn this off then you must have the same points in the the same order in the two lists.</p>

---
