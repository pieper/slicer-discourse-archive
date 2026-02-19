---
topic_id: 2877
title: "How Do I Smooth The Shape Of A Structure"
date: 2018-05-22
url: https://discourse.slicer.org/t/2877
---

# How do i smooth the shape of a structure?

**Topic ID**: 2877
**Date**: 2018-05-22
**URL**: https://discourse.slicer.org/t/how-do-i-smooth-the-shape-of-a-structure/2877

---

## Post #1 by @Jana.az (2018-05-22 15:23 UTC)

<p>How do i smooth the shape of a structure? I have imported a sphere from brainlab iplan rt to 3D slicer so i can calculate the surface area. But for a specific radius, in 3D slicer the surface area is bigger than the theoretical calculation of a surface area using the formula 4<em>pi</em>r^2. It is because the sphere imported is not a perfect sphere. So how do i smooth the surface?</p>

---

## Post #2 by @lassoan (2018-05-22 18:14 UTC)

<p>Have you imported the sphere from DICOM RT structure set?<br>
How have you computed the surface area?<br>
How large is the error relative to the total volume?<br>
Can you attach a screenshot?</p>

---

## Post #3 by @Jana.az (2018-05-23 09:15 UTC)

<p>The sphere is imported from DICOM RT structure.<br>
The surface area is computed when i did segmentation and exported the structure to models, i went to the models’ module and clicked on the information. The volume had a difference of 0.3 cm^3 from the theoretical and the one computed in iplan RT, which we can say is acceptable.<br>
However, the surface area had a difference of 10 cm^2 because as i said the sphere is not a perfect sphere, i’ll attach a screenshot of the sphere<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de97aadc74e7fcae81f88ad0b596ee2475cc3a51.jpeg" data-download-href="/uploads/short-url/vL8Wyht3smv53Gwpzy2BrBSk3AJ.jpg?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de97aadc74e7fcae81f88ad0b596ee2475cc3a51_2_690x387.jpg" alt="Untitled" data-base62-sha1="vL8Wyht3smv53Gwpzy2BrBSk3AJ" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de97aadc74e7fcae81f88ad0b596ee2475cc3a51_2_690x387.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de97aadc74e7fcae81f88ad0b596ee2475cc3a51_2_1035x580.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de97aadc74e7fcae81f88ad0b596ee2475cc3a51.jpeg 2x" data-dominant-color="AEB0AC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">1366×768 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>So i need a method to transform this sphere to a circular form and not small adjacent segments like in the photo, because this is I guess why the surface area is different.</p>

---

## Post #4 by @Jana.az (2018-05-23 09:21 UTC)

<p>This is a screenshot of the difference of calculations, this sphere is imported from iplan rt<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40e68f86d9b855ece3db224b113539a839ab39c1.jpeg" data-download-href="/uploads/short-url/9g8wZ6JL5VEMGgVHNN0824byJa1.jpg?dl=1" title="Untitled2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/40e68f86d9b855ece3db224b113539a839ab39c1_2_690x387.jpg" alt="Untitled2" data-base62-sha1="9g8wZ6JL5VEMGgVHNN0824byJa1" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/40e68f86d9b855ece3db224b113539a839ab39c1_2_690x387.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/40e68f86d9b855ece3db224b113539a839ab39c1_2_1035x580.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40e68f86d9b855ece3db224b113539a839ab39c1.jpeg 2x" data-dominant-color="A3A3B1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled2</span><span class="informations">1366×768 200 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @lassoan (2018-05-23 16:05 UTC)

<p>I’ve done a quick test and the surface computation in Slicer seems to be accurate - well below 1%.</p>
<ul>
<li>download a sample head MRI data set</li>
<li>create sphere shaped segment of 20mm radius</li>
<li>compute surface and volume =&gt; Surface area: 5024.96 (error: -0.03%), Volume: 33489.18 (error: -0.06%)</li>
<li>rasterize it with on a volume’s voxel grid</li>
<li>compute surface and volume =&gt; Surface area: 5042.75 (error: 0.32%), Volume: 33631.30 (error: 0.36%)</li>
</ul>
<p>You can find the script here: <a href="https://gist.github.com/lassoan/179776ffaaa57f4958906596f890fc67" class="inline-onebox">This example shows how to compute volume and surface area of a segment in 3D Slicer · GitHub</a><br>
You can click on “Raw” view and copy-paste the code into Slicer’s Python console.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/921318e78784c8a8990b602d54ab043a4b36ad89.png" data-download-href="/uploads/short-url/kQeCPYHWmQCxEOUDTYBvYhgr4Vz.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/921318e78784c8a8990b602d54ab043a4b36ad89_2_647x500.png" alt="image" data-base62-sha1="kQeCPYHWmQCxEOUDTYBvYhgr4Vz" width="647" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/921318e78784c8a8990b602d54ab043a4b36ad89_2_647x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/921318e78784c8a8990b602d54ab043a4b36ad89_2_970x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/921318e78784c8a8990b602d54ab043a4b36ad89.png 2x" data-dominant-color="D1C8C9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1168×902 207 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Try using Segment Statistics module to compute surface, volume, and other segment properties. It uses the same algorithms as the models module, but Segment Statistics does everything directly on the segmentation node (less chance to mess things up by performing manual steps) and computes properties for both closed surface and labelmap representations.</p>
<p>You may adjust smoothing factor of the closed surface representation (in Segmentations module: Representations / Close surface / Update / Binary labelmap → Closed surface / Smoothing factor) to make the surface smoother, but the default setting should work well.</p>
<p>If you still have problems, then upload the RTSTRUCT DICOM file somewhere and post the link here so that we can investigate.</p>

---

## Post #6 by @Jana.az (2018-05-27 09:43 UTC)

<p>The sphere created inside the 3d slicer compute the volume and surface area correctly. But i’m talking about the sphere created in iplan RT and imported to a dicom RT structure and opened in 3d Slicer. Here i found the screenshots uploaded above, and the big difference in surface area.</p>
<p>Regarding the Segment statistics modle, when i try to update from binary labelmap so i can use the smoothing factor on my RT structure sphere, the software crashes and i can’t do anything until i close it and open it again. So i can’t use the effects of Segment editor module on my dicom RT Structure.</p>

---

## Post #7 by @lassoan (2018-05-27 13:09 UTC)

<p>These should never happen and most likely there is just caused by some trivial issue that is easy to fix.</p>
<p>Could you share the DICOM RTSTRUCT and image file (upload to Dropbox/OneDrive/Google drive and copy the link here)?</p>
<aside class="quote no-group" data-username="Jana.az" data-post="6" data-topic="2877">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/8797f3/48.png" class="avatar"> Jana.az:</div>
<blockquote>
<p>when i try to update from binary labelmap so i can use the smoothing factor on my RT structure sphere, the software crashes</p>
</blockquote>
</aside>
<p>Could you send the application log? After you restart Slicer, select in menu: Help / Report a bug, and select the previous session in the listbox, then copy the text. If the text is long then upload somewhere and copy the link here.</p>
<p>By the way, BrainLab can also export segmentation as DICOM segmentation object, which is a more exact representation of segmentation than the legacy RTSTRUCT object. <a class="mention" href="/u/fedorov">@fedorov</a>, <a class="mention" href="/u/pieper">@pieper</a> do you know how to export DICOM segment object from BrainLab?</p>

---

## Post #8 by @fedorov (2018-05-28 13:40 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="2877">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/fedorov">@fedorov</a>, <a class="mention" href="/u/pieper">@pieper</a> do you know how to export DICOM segment object from BrainLab?</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> I personally never used Brainlab, and I don’t have access to a system to try it myself, so I can’t answer that question. But if <a class="mention" href="/u/jana.az">@Jana.az</a> could let me know the name of the specific product (Brainlab has different products) and the version, I can ask someone at Brainlab who might be able to help.</p>

---
