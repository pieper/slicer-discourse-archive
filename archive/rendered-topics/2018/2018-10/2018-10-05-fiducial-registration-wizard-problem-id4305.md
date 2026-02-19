---
topic_id: 4305
title: "Fiducial Registration Wizard Problem"
date: 2018-10-05
url: https://discourse.slicer.org/t/4305
---

# Fiducial Registration Wizard Problem

**Topic ID**: 4305
**Date**: 2018-10-05
**URL**: https://discourse.slicer.org/t/fiducial-registration-wizard-problem/4305

---

## Post #1 by @jrhodes (2018-10-05 20:45 UTC)

<p>I have two STL models with tracking markers on them. I am trying to register them using the fiducial registration wizard in Slicer but I’m not having luck.</p>
<p>Are there any good step-by-step tutorials out there for registering two STL models against each other? I have been using the “Pivot Calibration” PPT on the website but I am having trouble.</p>

---

## Post #2 by @lassoan (2018-10-06 02:51 UTC)

<p>Have you completed all relevant <a href="http://www.slicerigt.org/wp/user-tutorial/">SlicerIGT tutorials</a>?</p>
<p>It is not clear what you would like to do:</p>
<ul>
<li>A. Determine transform between tracking markers and STL model (so that you can see the true position of tracked models in the scene). These is referred to as “patient registration” in SlicerIGT tutorials. We usually do this by first calibrating a pointer (a.k.a. stylus; a short stick with a sharp tip) using pivot calibration module, then use Fiducial registration wizard to collect point coordinates by touching landmark points on the physical object with the tracked pointer, and mark the same points in the model node in the scene.</li>
<li>B. Register two STL models to each other. You can do this using Fiducial registration wizard. Such registration is not needed in most IGT workflows.</li>
</ul>

---

## Post #3 by @J.vd.Zee (2022-11-14 15:09 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> &amp; <a class="mention" href="/u/jrhodes">@jrhodes</a>,</p>
<p>This problem is still relevant for me today. I am currently struggling with this fiducial registration wizzard.</p>
<p>I have a 3D printed bone model with four fiducial locations and a rigid body attached to it. After following the landmark registration method regarding the Slicer IGT Tutorials I do not succeed in accurate registration. The problem is that I would like to replace the ‘origin’ after doing a fiducial registration to the current location of the rigid body. So this is more or less an extended workaround, as they did in the tutorial. See the attached image files.</p>
<ul>
<li>I the did pivot calibration to retrieve the stylustipToStylus transformation and the ReferenceToRas transformation following the ‘Brain surgery navigation’ tutorial of SlicerIGT tutorials.</li>
<li>Do the RasPoints or ReferencePoints be attached to the transformation matrix of the rigid body?</li>
<li>Do I have to attach the rigid body transformation matrix to the bone model before the registration or not?</li>
</ul>
<p>I will appreciate your help as I am stuck at the moment.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6cf76dbf92dd815ec5dc8583aa4d0d693a78a9f3.png" alt="image" data-base62-sha1="fxXGbjwCs7Af0HcHlyZWnoDfbcD" width="462" height="187"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/dad34ef02ae8f0c786bae8bb78e257aa1a225978.jpeg" data-download-href="/uploads/short-url/vdOOvnqZit7iIEHLCUanczDqIgE.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/dad34ef02ae8f0c786bae8bb78e257aa1a225978.jpeg" alt="image" data-base62-sha1="vdOOvnqZit7iIEHLCUanczDqIgE" width="690" height="472" data-dominant-color="989692"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">920×630 67.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
