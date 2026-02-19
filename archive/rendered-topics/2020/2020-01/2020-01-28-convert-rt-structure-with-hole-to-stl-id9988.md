---
topic_id: 9988
title: "Convert Rt Structure With Hole To Stl"
date: 2020-01-28
url: https://discourse.slicer.org/t/9988
---

# Convert rt structure with hole to stl

**Topic ID**: 9988
**Date**: 2020-01-28
**URL**: https://discourse.slicer.org/t/convert-rt-structure-with-hole-to-stl/9988

---

## Post #1 by @ali (2020-01-28 17:46 UTC)

<p>Hi all,</p>
<p>I am able to convert a simple ROI (or rt sturcture) made in our treatment planning system into an STL file for 3D printing. What I want to do is convert an ROI with a hole in it into an STL file. To start out, I made a simple shape with a hole in the treatment planning system. I tried using the same process, but there was no hole. As you can see from the screenshot, Slicer is able to show the outline of the hole, but the hole is not visible in the 3D view nor is it visible in printer’s slicing software.</p>
<p>Please advise,</p>
<p>Ali</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fe9880206f281fbcb255b9de213e67feba9cc3a.jpeg" data-download-href="/uploads/short-url/kx6CeJtsteRdO2iUk5AuRcSu83M.jpeg?dl=1" title="box_with_hole_01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8fe9880206f281fbcb255b9de213e67feba9cc3a_2_690x373.jpeg" alt="box_with_hole_01" data-base62-sha1="kx6CeJtsteRdO2iUk5AuRcSu83M" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8fe9880206f281fbcb255b9de213e67feba9cc3a_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8fe9880206f281fbcb255b9de213e67feba9cc3a_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8fe9880206f281fbcb255b9de213e67feba9cc3a_2_1380x746.jpeg 2x" data-dominant-color="AEA6B0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">box_with_hole_01</span><span class="informations">1920×1040 353 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @manjula (2020-01-28 18:42 UTC)

<p>Hi,</p>
<p>you need to convert the models to segmentations.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f06197f71171fb1d1d7c2b79427ebaf7eebb4320.png" data-download-href="/uploads/short-url/yivGxZaseZEMhippNqMir3B1BAI.png?dl=1" title="Screenshot from 2020-01-28 19-36-32" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f06197f71171fb1d1d7c2b79427ebaf7eebb4320_2_690x388.png" alt="Screenshot from 2020-01-28 19-36-32" data-base62-sha1="yivGxZaseZEMhippNqMir3B1BAI" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f06197f71171fb1d1d7c2b79427ebaf7eebb4320_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f06197f71171fb1d1d7c2b79427ebaf7eebb4320_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f06197f71171fb1d1d7c2b79427ebaf7eebb4320_2_1380x776.png 2x" data-dominant-color="70717E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-01-28 19-36-32</span><span class="informations">1920×1080 180 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The use the segmentation editor and use logical operator to subtract the one from the other.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30f2efe471f9a42dcc990fc813fa2874402df060.png" data-download-href="/uploads/short-url/6Z1plI7K3bWRXaZTQWRyAtQejkc.png?dl=1" title="Screenshot from 2020-01-28 19-36-43" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/30f2efe471f9a42dcc990fc813fa2874402df060_2_690x388.png" alt="Screenshot from 2020-01-28 19-36-43" data-base62-sha1="6Z1plI7K3bWRXaZTQWRyAtQejkc" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/30f2efe471f9a42dcc990fc813fa2874402df060_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/30f2efe471f9a42dcc990fc813fa2874402df060_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/30f2efe471f9a42dcc990fc813fa2874402df060_2_1380x776.png 2x" data-dominant-color="6C6F83"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-01-28 19-36-43</span><span class="informations">1920×1080 196 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Then you can use the the export it as a stl model from the segment editor.</p>
<p>Also you can simply export the created models as two separate models  as stl files and use Blender or meshmixer and do the substraction. As long as you do not move the objects  coordinates will be preserved and  for planning purposes you can import it back to 3D Slicer as well. Just make sure you don’t move the objects around.</p>
<p>We use  second workflow because blender allows much much more functionality when it come to modelling and 3D printing.</p>

---

## Post #3 by @lassoan (2020-01-28 20:13 UTC)

<aside class="quote no-group" data-username="ali" data-post="1" data-topic="9988">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/8c91f0/48.png" class="avatar"> ali:</div>
<blockquote>
<p>As you can see from the screenshot, Slicer is able to show the outline of the hole, but the hole is not visible in the 3D view nor is it visible in printer’s slicing software.</p>
</blockquote>
</aside>
<p>DICOM RTSTRUCT uses a set of parallel contours to define a segment.</p>
<p>Having a hole in a segment is a very special case as it actually cannot be represented with planar contours. The DICOM standard describes a workaround, the “keyhole” technique. What treatment planning system did you use to create the RTSTRUCT? Does it support “keyhole” technique? Can you provide a sample RTSTRUCT so that we can verify if Slicer’s importer works correctly?</p>
<p>Do DICOM import and STL export work as expected for structures that don’t have hole in the slicing plane?</p>

---

## Post #4 by @ali (2020-02-07 01:45 UTC)

<p>Good news: With the suggestions from manjula, I was able to test this process to successfully make a box with holes in it.</p>
<p>Bad news: For my actual process, I will need to subtract 5-20 structures from the main structure. It will be possible, but tedious using 3DSlicer. Is there a more recommended software for this use case?</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> We use RayStation. Reading about this “keyhole” technique <a href="http://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.8.8.6.3.html" rel="nofollow noopener">here</a>, I looked at some wall contours made my RayStation. However, these ROIs did not have the design described in the link. They simply had a contour inside another one.</p>

---

## Post #5 by @lassoan (2020-02-07 02:05 UTC)

<aside class="quote no-group" data-username="ali" data-post="4" data-topic="9988">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/8c91f0/48.png" class="avatar"> ali:</div>
<blockquote>
<p>RayStation. However, these ROIs did not have the design described in the link. They simply had a contour inside another one</p>
</blockquote>
</aside>
<p>That would be a pretty harsh violation of the DICOM standard. If you provide an example data set then I can follow up with them.</p>
<aside class="quote no-group" data-username="ali" data-post="4" data-topic="9988">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/8c91f0/48.png" class="avatar"> ali:</div>
<blockquote>
<p>Bad news: For my actual process, I will need to subtract 5-20 structures from the main structure. It will be possible, but tedious using 3DSlicer. Is there a more recommended software for this use case?</p>
</blockquote>
</aside>
<p>That’s fine. Once you figured out a processing workflow using GUI, you can automate all tedious steps by writing a short Python script. Look around for examples in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">script repository</a> and let us know if you cannot find an example for automating some of the steps in your workflow.</p>

---

## Post #6 by @ali (2020-02-07 23:15 UTC)

<p>Thank you.</p>
<p>Actually, now that I got the “thing with holes” stl export process prototyped, the next phase is to write a (python) program to create the hole objects I need, given the main object. Glad to learn I can use python to interact with 3D Slicer. Looks like, I can then use 3D Slicer’s python extension capability to “put the holes into the main object”, so to speak.</p>
<p>I have not experience writing gui programs though. Do you think (down the line, with some help) it is reasonable to end up with a (single, self-contained) module in 3D Slicer for this (whole) procedure? That will help other professionals adopt this technique. Somehow, I thought I had to use C++ to interact with 3D Slicer on a programmatic level.</p>

---

## Post #7 by @Juicy (2020-02-08 05:58 UTC)

<p>Yes you can write scripted modules (in python) for slicer which you can use just like any other module. You can add buttons, input selectors etc. You can call other modules to do things for you so you can do all your work in one ‘self contained module’.</p>
<p>See some info on python scripting <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting" rel="nofollow noopener">here</a> and the script repository above.</p>
<p>Once you have a script which works  check out the developer tutorials on <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Tutorials_for_software_developers" rel="nofollow noopener">this page</a> for tutorials on how to make your script into a scripted module</p>
<p>Although in python slicer uses a lot of libraries so it can be hard to get your head around all the syntax. I have figured out how to do most things I need from the script repository. Anything you can’t figure out you can post here on the forum.</p>

---
