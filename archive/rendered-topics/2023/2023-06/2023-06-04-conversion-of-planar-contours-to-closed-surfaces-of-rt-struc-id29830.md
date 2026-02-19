---
topic_id: 29830
title: "Conversion Of Planar Contours To Closed Surfaces Of Rt Struc"
date: 2023-06-04
url: https://discourse.slicer.org/t/29830
---

# Conversion of planar contours to closed surfaces of RT Structs is corrupted

**Topic ID**: 29830
**Date**: 2023-06-04
**URL**: https://discourse.slicer.org/t/conversion-of-planar-contours-to-closed-surfaces-of-rt-structs-is-corrupted/29830

---

## Post #1 by @nathanbmnt (2023-06-04 20:25 UTC)

<p>Hello,<br>
I have brain RT structs exported from the software “MIM” which when I import into Slicer via SlicerRT have corrupted closed surfaces.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0ba634dfde64c773b27ba431019d324d58299df.jpeg" data-download-href="/uploads/short-url/tMuEbjSJNz1d2E7cKsuH2ip8V7V.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d0ba634dfde64c773b27ba431019d324d58299df_2_690x291.jpeg" alt="image" data-base62-sha1="tMuEbjSJNz1d2E7cKsuH2ip8V7V" width="690" height="291" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d0ba634dfde64c773b27ba431019d324d58299df_2_690x291.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d0ba634dfde64c773b27ba431019d324d58299df_2_1035x436.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d0ba634dfde64c773b27ba431019d324d58299df_2_1380x582.jpeg 2x" data-dominant-color="70767A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×811 93.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>As you can see the slice fill has patches missing and points are connected that shouldn’t be. An MRI is the background volume but I’ve made it black because this is anonymous patient data. Any ideas why this is happening?</p>

---

## Post #2 by @lassoan (2023-06-05 00:13 UTC)

<p>It may be just a rendering artifact. Could you please check if the appearance is fixed if you create “Closed surface” representation from n Segmentations module?</p>

---

## Post #3 by @nathanbmnt (2023-06-05 00:42 UTC)

<p>When the RT struct is loaded a closed surface representation is automatically created. So per your suggestion I removed the closed surface rep:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/029fa27d59bbcbc99e91665b6c77dc8af766155c.png" data-download-href="/uploads/short-url/ncYbBPwmGzUXZZbB0KraPUXz2c.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/029fa27d59bbcbc99e91665b6c77dc8af766155c.png" alt="image" data-base62-sha1="ncYbBPwmGzUXZZbB0KraPUXz2c" width="690" height="121" data-dominant-color="D2DEE4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">748×132 6.05 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
then created it again by clicking create<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2ca9054d6e9906ffb1199cfd81df441cf1703915.png" alt="image" data-base62-sha1="6n58iJJjeU4nbnYD7n6a7STVU6p" width="556" height="45"><br>
exact same result<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99d500e655d55dc8b6a37a91145eac7826d8135e.png" data-download-href="/uploads/short-url/lWRptvXhmXsmBxUzqKs1Pem0qBw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99d500e655d55dc8b6a37a91145eac7826d8135e_2_610x500.png" alt="image" data-base62-sha1="lWRptvXhmXsmBxUzqKs1Pem0qBw" width="610" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99d500e655d55dc8b6a37a91145eac7826d8135e_2_610x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99d500e655d55dc8b6a37a91145eac7826d8135e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99d500e655d55dc8b6a37a91145eac7826d8135e.png 2x" data-dominant-color="090808"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">892×730 14.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I’ve uploaded the RT struct here</p><aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1Ls1-rHzo3d7VXdOnZ5Yg7p_IJYSePPVu/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1Ls1-rHzo3d7VXdOnZ5Yg7p_IJYSePPVu/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1Ls1-rHzo3d7VXdOnZ5Yg7p_IJYSePPVu/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1Ls1-rHzo3d7VXdOnZ5Yg7p_IJYSePPVu/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">0298slicerForum.zip</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @lassoan (2023-06-05 03:56 UTC)

<p>This structure set has lots of errors. There slightly non-parallel contours and slightly inconsistent distance between contour planes. There also seem to be a number of left-to-right direction cuts in the contours (see orange arrows; maybe they are keyholes, but then there should be holes in the cross-sections, but no holes are visible).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9db0675bcce3a739a729f16cebc682363c66962.png" data-download-href="/uploads/short-url/oeBX17L1joVAxKej54DV2zZgG3g.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a9db0675bcce3a739a729f16cebc682363c66962_2_650x500.png" alt="image" data-base62-sha1="oeBX17L1joVAxKej54DV2zZgG3g" width="650" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a9db0675bcce3a739a729f16cebc682363c66962_2_650x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a9db0675bcce3a739a729f16cebc682363c66962_2_975x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a9db0675bcce3a739a729f16cebc682363c66962_2_1300x1000.png 2x" data-dominant-color="B880AA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1334×1025 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Some of the contour visualization problems are due to the default slice plane (in red</p>
<ul>
<li>in default axial direction) is not parallel with the contours, which makes the cuts extra complicated. If you load the source image (that was used to create the contours) then you can align the slice views with the contour planes, which will somewhat reduce the rendering artifacts. However, the problem is primarily not the rendering of these complex intersections (and in your screenshot you have already made this alignment, probably because you loaded the referenced image).</li>
</ul>
<p>The general problem is that RT structure set is not suitable as a general-purpose 3D shape representation and here you are trying to use it for representing a complex shape. RT structure set usually works acceptably for simple, smooth shapes - such as hand-drawn contours. However, automatic segmentation methods that derive complex shapes directly from image content are usually too complex to be represented in an RT structure set. Even if a software can save a complex 3D shape and reconstruct it consistently from the saved file, other software applications may not be able to reproduce the same shape, because there are so many ways to resolve ambiguities and numerical inaccuracies.</p>
<p>If you don’t work with radiation treatment planning systems then I would recommend to just avoid RT structure sets (use DICOM Segmentation object instead). If you must use RT structure set because you must import the results into a treatment planning system that only supports RT structure sets then you can try to simplify the shape and reduce the number of contours.</p>

---

## Post #5 by @nathanbmnt (2023-06-05 19:03 UTC)

<p>MIM has a menu option for “Save surface segmentation” that I used and it created a “SEG” series file<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c430749dbf73d5f034db2eaf36f48e05d155012.png" alt="image" data-base62-sha1="aSDTwEgIof1r7o4Ev3UmCWSe6MG" width="429" height="41"><br>
However now when I try to load it into Slicer along with the associated volume I see this error window<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39e196573dac920e63be12f7917b635aa242658f.png" data-download-href="/uploads/short-url/8g2x7SY1qw6qJOnngvW9OuACbRZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39e196573dac920e63be12f7917b635aa242658f.png" alt="image" data-base62-sha1="8g2x7SY1qw6qJOnngvW9OuACbRZ" width="690" height="307" data-dominant-color="F2F3F4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1004×448 19.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I click OK and see this<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b56ff70d4a294a2c367d4151c7aa78f068e8b2a6.png" data-download-href="/uploads/short-url/pT4iYROR2cx2h6CUu95YxQJSo1E.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b56ff70d4a294a2c367d4151c7aa78f068e8b2a6.png" alt="image" data-base62-sha1="pT4iYROR2cx2h6CUu95YxQJSo1E" width="690" height="204" data-dominant-color="F5F5F0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">776×230 8.68 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>MIM also has a tool to clean each axial slice<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15d6a9de425876446fd6aea9b9d4c5820f2f3973.png" data-download-href="/uploads/short-url/37bWmMalxMWFYHRkGdByAcn9NNF.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15d6a9de425876446fd6aea9b9d4c5820f2f3973.png" alt="image" data-base62-sha1="37bWmMalxMWFYHRkGdByAcn9NNF" width="690" height="305" data-dominant-color="413737"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1018×451 8.41 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I used this and also smoothed the contour. After loading into slicer the closed surface is a lot less corrupted:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9ff9229263614d2a98511d7f50dcc3a9c495fc9.png" data-download-href="/uploads/short-url/zFArNtR66SFpDrJfhsCrNzgYwMF.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9ff9229263614d2a98511d7f50dcc3a9c495fc9_2_690x218.png" alt="image" data-base62-sha1="zFArNtR66SFpDrJfhsCrNzgYwMF" width="690" height="218" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9ff9229263614d2a98511d7f50dcc3a9c495fc9_2_690x218.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9ff9229263614d2a98511d7f50dcc3a9c495fc9_2_1035x327.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9ff9229263614d2a98511d7f50dcc3a9c495fc9_2_1380x436.png 2x" data-dominant-color="6E7379"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3837×1216 301 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Do you know why the DICOM SEG is not loading?</p>

---

## Post #6 by @lassoan (2023-06-05 19:06 UTC)

<p>Slicer supports loading of DICOM Segmentation IOD (via QuantitativeReporting extension).</p>
<p>However, DICOM Surface Segmentation IOD is not yet supported. It should not be hard to add support for it (you could write an importer Python script), but surface segmentation IOD is rarely used in medical image computing, so there has not been any demand for importing it. You could create a topic for it in the <a href="https://discourse.slicer.org/c/support/feature-requests/9">“Feature requests” category</a> and if it gathers enough votes then we’ll work on it.</p>

---

## Post #7 by @pieper (2023-06-05 22:19 UTC)

<p>Here’s a thread on options for surface segmentations:</p>
<aside class="quote" data-post="1" data-topic="1125">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/df705f/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/load-dicom-surface-segmentation-objects/1125">Load DICOM Surface Segmentation Objects</a> <a class="badge-category__wrapper " href="/c/support/feature-requests/9"><span data-category-id="9" data-parent-category-id="11" data-drop-close="true" class="badge-category --has-parent" title="This category is for submitting ideas about what enhancements or new features should be added to 3D Slicer. Make your voice heard by voting on feature requests - by opening the topic and clicking the Vote button or by creating a new topics. Slicer developers will make it a priority to work on feature requests that have more votes."><span class="badge-category__name">Feature requests</span></span></a>
  </div>
  <blockquote>
    Slicer version: 4.6.2 
Hi, 
I just wondered, if there is any possibility to load DICOM Surface Segmentation Objects, as described in the DICOM Supplement 132 with the 3D Slicer. 
Thank you in advance! <img width="20" height="20" src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title="slight_smile" alt="slight_smile" class="emoji"> 
Best regards 
Julia
  </blockquote>
</aside>


---

## Post #8 by @issakomi (2023-06-05 23:05 UTC)

<p>The script to view SEG surface is <a href="https://gist.github.com/issakomi/29e48917e77201f2b73bfa5fe7b30451" rel="noopener nofollow ugc">here</a>, it works. S. options at the beginning to save as VTK or STL to load into Slicer, the script itself only shows the SEG mesh.</p>

---
