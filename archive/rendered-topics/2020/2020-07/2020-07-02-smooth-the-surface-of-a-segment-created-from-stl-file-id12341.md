---
topic_id: 12341
title: "Smooth The Surface Of A Segment Created From Stl File"
date: 2020-07-02
url: https://discourse.slicer.org/t/12341
---

# Smooth the surface of a segment created from stl file

**Topic ID**: 12341
**Date**: 2020-07-02
**URL**: https://discourse.slicer.org/t/smooth-the-surface-of-a-segment-created-from-stl-file/12341

---

## Post #1 by @Deepa (2020-07-02 17:26 UTC)

<p>Hello,</p>
<p>I tried to use median smoothing in <code>Segment Editor</code> on a segment node created from an <a href="https://figshare.com/s/f8d884580db2e24728c1" rel="nofollow noopener">stl input</a>.</p>
<p>However, after ~15  min smoothing task didn’t complete.</p>
<p>Could someone look into it?<br>
I am trying to smooth this segment for using in VMTK’s extract centerline module. When I use this geometry without smoothing (i.e the segment node generated from original input), I am not able to extract centerlines.</p>

---

## Post #2 by @lassoan (2020-07-03 18:57 UTC)

<p>All of these meshes are pretty bad quality: their surface is not smooth, they have unnecessarily small cells, and they contain lots of mesh errors.</p>
<p>For example, “Supplemental STL File 1.stl”  has over 1500 non-manifold edges. I’ve tried to fix them using MeshLab but this file made MeshLab crash. The only way I could do something with it was to remesh it completely (load it as a segmentation, create binary labelmap representation, make that the master representation, and create closed surface representation).</p>
<p>“Supplemental STL File 3.stl” is much better. On that I was able to run Extract centerline module without any cleaning or fixing.</p>

---

## Post #3 by @Deepa (2020-07-06 05:11 UTC)

<p>Thanks a lot for looking into this.</p>
<p>I created a binary labelmap representation of  “Supplemental STL File 3.stl” to identify the image spacing.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10461b13104d3b2bf0ec0d0528db73da08796ca9.png" alt="Untitled" data-base62-sha1="2jXQ6AGFwljanJIVDXDBTQDn7JL" width="298" height="72"> .</p>
<p>The units are in mm. I would like to know if these units correspond to the actual dimensions of the geometry present in the stl file.  For instance, is it safe to consider that the values obtained in the quantification results table of <code>extract centerline</code> module are in mm?</p>

---

## Post #4 by @lassoan (2020-07-06 05:18 UTC)

<p>Extract centerline module reports results in the same unit as the point coordinates in the STL file. If those point coordinates are in millimeter then the radius is in millimeter, too.</p>

---

## Post #5 by @Deepa (2020-07-06 05:26 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="12341">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Extract centerline module reports results in the same unit as the point coordinates in the STL file.</p>
</blockquote>
</aside>
<p>Could you please suggest how to check for the units of point coordinates of the imported STL file in Slicer?</p>

---

## Post #6 by @lassoan (2020-07-06 13:29 UTC)

<p>One of the big issues with STL files is that there is no standard way of specifying what unit is used for point coordinates.</p>
<p>Unless you have an object of known size in the image, you need to ask the producer of the STL file. For 3D printing of objects at real-life size, most common units are mm (this is Slicer’s assumption) and m, but sometimes inch or tenth of an inch is used, and of course any arbitrary scaling factor can be used.</p>

---

## Post #7 by @Deepa (2020-07-10 05:57 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>When I load the multiframe tiff associated with the geometry in STL File3, I find the following Volume information</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6af114705319f4651f559acdc588f244c69f8fe.png" alt="Untitled" data-base62-sha1="zcgxmrLRfSIX5N0iJsJpTbMUrmu" width="248" height="77"></p>
<p>and I also have the information that scale of these images: 1 px = 2.31 μm from the associated study.</p>
<p>Should I replace default x = 0.352 mm,y=0.352 mm,z =1 mm in image spacing (displayed in Volume information)  with x=2.31 um, y=2.31 um, z=2.31 um</p>
<p>May I know how to interpret the units of the quantification results using the above information?</p>

---

## Post #8 by @lassoan (2020-07-11 18:46 UTC)

<p>0.352mm/pixel corresponds to 72dpi, which is probably some default value in the TIFF file writer. So, replacing spacing values by 2.31 would make sense. Then you would get all your results in micrometer unit. Note that Slicer would display mm as unit (unless you change the length unit name in application settings, but there are some limitations related to this - see details <a href="https://github.com/Slicer/Slicer/issues/5040">here</a>).</p>

---

## Post #9 by @Deepa (2020-09-12 04:48 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a><br>
I am trying to smooth vessel segments present in an <a href="https://drive.google.com/file/d/1pSMQWkjCVzUwPHsjFEAcqzdJddv_87WP/view?usp=sharing" rel="nofollow noopener">stl file</a>. I tried all the options available Median, Gaussian … with default kernel size. For some reason, all the segments disappear. Prior to smoothing, I used the island icon to retain only the largest connected component and that failed too. Could you please have a look?</p>

---

## Post #10 by @lassoan (2020-09-12 05:40 UTC)

<p>This file is an artificial network (probably reconstructed from centerline detection). It is already smooth. The faceted look is just due to surface normals are not generated by default for STL files. You can go to Surface toolbox module, enable “Normals”, and Apply.</p>

---

## Post #11 by @Deepa (2020-09-12 05:59 UTC)

<p>Thank you. When I use this model in the extract centerline module<br>
after (hitting Normals) the end points are not detected. Is this because of the “artificial network”?</p>

---

## Post #12 by @Deepa (2020-09-13 02:15 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I also tried to view a smaller subset of the network present in the stl file shared above . But the network extraction and centerline extraction didn’t find the properties of all the branches. Many endpoints are undetected in “Auto detect”. Could you please suggest how to get this working?</p>

---

## Post #13 by @Deepa (2020-09-16 01:45 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> This is a kind reminder</p>

---
