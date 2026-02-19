---
topic_id: 29024
title: "Ras Coordinate System World Coordinate System"
date: 2023-04-20
url: https://discourse.slicer.org/t/29024
---

# RAS Coordinate system != World Coordinate system?

**Topic ID**: 29024
**Date**: 2023-04-20
**URL**: https://discourse.slicer.org/t/ras-coordinate-system-world-coordinate-system/29024

---

## Post #1 by @dsa934 (2023-04-20 09:42 UTC)

<p>Operating system: window 10<br>
Slicer version: 5.2.1</p>
<p>Hi, I have a question about coordinate systems.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/6845843bf7884f73d27d7d6a2f6c9c41c6b7875a.png" data-download-href="/uploads/short-url/eSqAUOSvi3p51zOGEbcQVyTNViO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/6845843bf7884f73d27d7d6a2f6c9c41c6b7875a_2_690x325.png" alt="image" data-base62-sha1="eSqAUOSvi3p51zOGEbcQVyTNViO" width="690" height="325" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/6845843bf7884f73d27d7d6a2f6c9c41c6b7875a_2_690x325.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/6845843bf7884f73d27d7d6a2f6c9c41c6b7875a_2_1035x487.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/6845843bf7884f73d27d7d6a2f6c9c41c6b7875a_2_1380x650.png 2x" data-dominant-color="CBCCE6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1984×937 207 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>After some experimentation, I found out that the direction of the x,y axis in the WCS( world coordinate system) and the direction of the x,y axis of the 3D slicer are opposite. What is the reason for this?</p>
<p>( In right fig )  F-1 : [0,0,0] , F_1-1 : [100,0,0] , F_3-1 : [ 0, 100, 0] , F_4-1 : [0, 0, 100]</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #2 by @lassoan (2023-04-20 12:41 UTC)

<p>DICOM and most medical imaging software uses the <strong>LPS coordinate system</strong> for storing all data. Axis directions of this coordinate system are patient left, posterior, and superior. Unit is millimeters. There is no universal standard for choice of origin, but it is often some geometric center of the imaging system or chosen to be near the center of some object of interest.</p>
<p><strong>RAS coordinate system</strong> is almost the same as the LPS coordinate system, except the axis directions are patient right, anterior, superior, i.e., the sign of the first two coordinates is inverted. This coordinate system was still popular in the early 2000s when development of Slicer was started, especially in neuroimaging software, therefore Slicer developers chose to use the RAS coordinate system.</p>
<p>Slicer still uses RAS coordinate system for storing coordinate values internally for all data types, but for compatibility with other software, it assumes that all data in files are stored in LPS coordinate system (unless the coordinate system in the file is explicitly stated to be RAS). To achieve this, whenever Slicer reads or writes a file, it may need to flip the sign of the first two coordinate axes to convert the data to RAS coordinate system.</p>
<p>You can either keep using RAS coordinate system in your files and specify that in the file header, or switch to use LPS coordinate system.</p>

---

## Post #3 by @dsa934 (2023-04-20 13:32 UTC)

<p>When I opened a point ([x,y,z]) and mesh in 3d slicer, the point was close to the mesh in other tools, but there was a phenomenon that it was far away in 3d slicer.</p>
<p>I understand everything you said if you mean that all the metadata you worked on without using the slicer will be displayed in the LPS coordinate system in the 3d slicer. ( double check )</p>

---

## Post #4 by @lassoan (2023-04-20 16:34 UTC)

<p>If you don’t specify coordinate system in a file (mesh, markup, image, …) then Slicer will assume it is in LPS and so the sign of the first two coordinates will be inverted during loading.</p>

---

## Post #5 by @dsa934 (2023-04-21 01:56 UTC)

<p>What is the default option ?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b91b3d6ef77b106915d6b9a74c3ff2e78d46452.jpeg" data-download-href="/uploads/short-url/1ElpW5FY5gBnywFai1LeFCpysoi.jpeg?dl=1" title="Screenshot_20230421_083515_NAVER" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b91b3d6ef77b106915d6b9a74c3ff2e78d46452_2_230x500.jpeg" alt="Screenshot_20230421_083515_NAVER" data-base62-sha1="1ElpW5FY5gBnywFai1LeFCpysoi" width="230" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b91b3d6ef77b106915d6b9a74c3ff2e78d46452_2_230x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b91b3d6ef77b106915d6b9a74c3ff2e78d46452_2_345x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b91b3d6ef77b106915d6b9a74c3ff2e78d46452_2_460x1000.jpeg 2x" data-dominant-color="EDEEEE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20230421_083515_NAVER</span><span class="informations">1080×2340 178 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>if default option == RAS coordinate system ,</p>
<p>why did you add the RAS option in drop box ?</p>

---

## Post #6 by @lassoan (2023-04-21 02:22 UTC)

<p>Slicer versions until a few years ago still used RAS coordinate system in mesh files. The RAS option allows loading them correctly in the current Slicer version.</p>

---

## Post #7 by @dsa934 (2023-04-27 01:12 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>What exactly does it mean that the slicer uses the RAS coordinate system?</p>
<p>Let’s assume that we are working on setting a focal point for a certain mesh target.</p>
<p>a) web_tool ( not a slicer ) : fp = [ -28, 4, 26]</p>
<p>b) slicer                              : fp = [ 28, -4 , 26]</p>
<p>According to you, the slicer follows the RAS coordinate system and the other external tools follow the LPS coordinate system (if no coordinates are specified).</p>
<p>However, I’m not sure why these a) and b) match exactly when rendering in vtk.<br>
Also, if you want to map the coordinates of the focal point created by operation a) in the slicer to the mesh, you must select the RAS coordinate system when loading the mesh into the slicer so that it maps correctly to the mesh, and if you set default (LPS), they will not match.</p>
<p>Does the view of the slicer follow the RAS coordinate system, and is it saved as LPS when saving after work?</p>

---

## Post #8 by @lassoan (2023-04-27 01:26 UTC)

<aside class="quote no-group" data-username="dsa934" data-post="7" data-topic="29024">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dsa934/48/17907_2.png" class="avatar"> dsa934:</div>
<blockquote>
<p>Does the view of the slicer follow the RAS coordinate system, and is it saved as LPS when saving after work?</p>
</blockquote>
</aside>
<p>Exactly. The coordinate system is converted when reading/writing files.</p>
<p>Images and transforms are always saved in LPS coordinate system (this became de facto standard 10-20 years ago).</p>
<p>Models and markups are saved in LPS by default, too. You can force RAS in the saving options, but I would not recommend it, unless you need it for compatibility with some legacy software. (The option is there because Slicer started to transition to LPS coordinate system in these files relatively more recently, maybe about 5-10 years ago.)</p>

---

## Post #9 by @dsa934 (2023-04-27 04:11 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>I’m still curious about one thing.</p>
<p>You said that the slicer assumes that the work done by all ‘tools’ except the slicer is saved as an LPS coordinate system.</p>
<p>Load the following two files in the slicer.  ( Mesh(MeshFromWeb), Markups(MarkupFromWeb) )</p>
<p>As both follow the LPS coordinate system, markups should exist on the mesh, but they do not.</p>
<p>To adjust the markup position, if the mesh is forcibly loaded into the RAS coordinate system, the markups will exist on the mesh.</p>
<p>If I didn’t force the RAS coordinate system when I saved ‘Mesh&amp;Markups’ in Web, can you explain why this is happening?</p>

---

## Post #10 by @dsa934 (2023-05-03 07:28 UTC)

<p>The mesh data was loaded through the slicer and the coordinates of the markup node were written directly, so the x-axis and y-axis +,- sign conversion did not occur, so I’m sorry.</p>

---
