---
topic_id: 38482
title: "Coordinate Systems"
date: 2024-09-22
url: https://discourse.slicer.org/t/38482
---

# Coordinate systems

**Topic ID**: 38482
**Date**: 2024-09-22
**URL**: https://discourse.slicer.org/t/coordinate-systems/38482

---

## Post #1 by @andrewrj (2024-09-22 14:04 UTC)

<p>I apologize if this question has already been asked. I have a sample of pre-treatment and post-treatment CBCTs that have been superimposed. I have used Markups to put control points as landmarks to obtain the x, y, and z or i, j, and k relative difference from pre-treatment to post-treatment. Compiling the data from the jsons I have found that the coordinate systems are not even close to each other. For intraclass coefficient intra-rater reliability testing the variance and mean then my coordinates are so vastly different that the ICC is 0. I am a beginner with Python and 3D Slicer so I apologize if this is very easy. How do I center the volume and transform all my landmarks consistently across my sample pre-treatment and postreatment CBCTs?</p>

---

## Post #2 by @muratmaga (2024-09-22 17:38 UTC)

<aside class="quote no-group" data-username="andrewrj" data-post="1" data-topic="38482">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/b782af/48.png" class="avatar"> andrewrj:</div>
<blockquote>
<p>pre-treatment and post-treatment CBCTs that have been superimposed.</p>
</blockquote>
</aside>
<p>this statement and this</p>
<aside class="quote no-group" data-username="andrewrj" data-post="1" data-topic="38482">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/b782af/48.png" class="avatar"> andrewrj:</div>
<blockquote>
<p>coordinate systems are not even close to each other</p>
</blockquote>
</aside>
<p>seems contradictory</p>
<p>How did you superimpose them? usually this is done by registration by putting one scan in the reference frame of the other.</p>
<aside class="quote no-group" data-username="andrewrj" data-post="1" data-topic="38482">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/b782af/48.png" class="avatar"> andrewrj:</div>
<blockquote>
<p>How do I center the volume and transform all my landmarks consistently across my sample pre-treatment and postreatment CBCTs?</p>
</blockquote>
</aside>
<p>You can center the volumes, but unless they have very similar geometries, it is not likely to create a good superimposition.</p>

---

## Post #3 by @andrewrj (2024-09-22 22:00 UTC)

<p>Thank you for your reply. In ITK SNAP, the pre-treatment CBCTs were registered and then using a voxel based superimposition method of the anterior cranial base the post-treatment CBCTs were superimposed on the pre-treatment CBCTs. So within a patient the coordinate systems are the same. Between patients the coordinate systems are different. I then placed control points as landmarks. For example, the x,y,z coordinates for a landmark in one subject is 49.382, -83.044, 36.298 and the x,y,z coordinates for a landmark in another patient is 44.208, 39.046, -212.089. Scrolling through the data, left sided landmarks can be positive for some patients and negative for other patients. For ICC I need means and variances which currently return an ICC near zero with the coordinate systems being different. In ITK SNAP and 3D Slicer the CBCTs were in RAS. My strategy, unless I’m wrong, would be to center the volumes with assumption that the head size of the pre-treatment CBCTs across patients is similar so I will at least get the coordinate systems closer together. I have been avoiding choosing a landmark to manually set the origin 0,0,0 because I don’t know how I would place it in pre-treatment and post-treatment CBCTs of the same patient exactly.</p>

---

## Post #4 by @muratmaga (2024-09-22 23:54 UTC)

<p>I am still not clear what you are trying to do.</p>
<p>For your inter-rater you should be looking at the difference of the coordinates within a patient, and probably need to turn this difference vector into a magnitude (distance) as opposed to using the coordinates. If you get a difference of two measurements c(0, -1, 1) vs c(1, 0, -1), this are essentially the same magnitude of variation.</p>
<p>If you do this, then you don’t have to worry about whether the coordinate system across cases are consistent. It only matters if the subject’s coordinate system is the same.</p>
<p>Anyways, there is a center option in slicer (under volumes module), but i don’t think it will give you what you want. It will center it based on the data extent, not center of mass. So if the field of views are not exactly the same, centering is not going to align the centers of mass. Accurate alignment is usually done with registration. If you want to have all your cases to share a common coordinate system, then you can choose one a reference and register them all to that rigidly.</p>

---

## Post #5 by @andrewrj (2024-09-25 01:13 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/4054f09293bf1ebea747c36d7c0e2ce684592739.png" data-download-href="/uploads/short-url/9b6xwhfeY8mkZM3RnS5XFN5WdwB.png?dl=1" title="Picture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/4054f09293bf1ebea747c36d7c0e2ce684592739.png" alt="Picture1" data-base62-sha1="9b6xwhfeY8mkZM3RnS5XFN5WdwB" width="399" height="500" data-dominant-color="E3E0E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Picture1</span><span class="informations">509×637 30.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks for your help. That makes sense about the center option and for the magnitude and distance for inter-rater.<br>
I think my questions is similar to this post: <a href="https://discourse.slicer.org/t/a-bit-of-confusion-about-the-slicer-coordinate-system/29883" class="inline-onebox">A bit of confusion about the slicer coordinate system</a>.<br>
I checked my settings and confirmed that patient right is screen left. In the picture I uploaded you can see for the same landmark, patients 319 and 320 in have x,y,z coordinates different than every other patient. Why is this happening only for 319 and 320?</p>

---

## Post #6 by @muratmaga (2024-09-25 02:30 UTC)

<p>Without knowing more about your study design, I cannot give an accurate answer.</p>
<p>If this table is coordinates of one patient rated by 26 different individuals (each rater is a row), clearly the raters 319 and 320 are outliers for some reason.</p>
<p>If these are 26 subjects rated by the same individual, then you cannot average coordinates like this. It is not meaningful. There is no reason to expect every subject to have a common coordinate system. Perhaps subjects 319 and 320 are upside down with respect to others for some reason. Assuming you have other raters, you need to average the coordinate of every subject by itself, and then calculate the magnitude of difference of each rater to this average (unless of course you have a standard. if you have a standard, then there is no need to calculate the average).</p>
<p>If you want to use raw coordinates as the unit of your analysis, you should do proceed with a shape analysis (which will do a joint superimposition to bring everything into a common coordinate system). You can look into the literature for generalized procrustes analysis, it is rather rich. The module is available as part of the SlicerMorph module.</p>

---
