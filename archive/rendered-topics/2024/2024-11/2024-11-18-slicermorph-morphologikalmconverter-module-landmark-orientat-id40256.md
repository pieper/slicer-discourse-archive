---
topic_id: 40256
title: "Slicermorph Morphologikalmconverter Module Landmark Orientat"
date: 2024-11-18
url: https://discourse.slicer.org/t/40256
---

# SlicerMorph MorphologikaLMConverter module- landmark orientation issue

**Topic ID**: 40256
**Date**: 2024-11-18
**URL**: https://discourse.slicer.org/t/slicermorph-morphologikalmconverter-module-landmark-orientation-issue/40256

---

## Post #1 by @A_Auerbach (2024-11-18 21:00 UTC)

<p>Hello all,</p>
<p>I’ve used Slicer for segmentation but Checkpoint for landmarking, exporting my landmarks as Morphologika and csv files. However, to create good visualizations of my landmarks on the skull surface for publication, the best approach seems to be importing those landmarks back into Slicer.<br>
The best tool I found for this was the MorphologikaLMConverter module in SlicerMorph. However, while this mostly works (creates a file of the landmarks I can open in Slicer), it appears to be mirroring the landmarks (consistently changing the sign), resulting in a configuration that is the right size and location but incorrect orientation for matching my segmentation.</p>
<p>Does anyone have any suggestions for how to fix this/what I’m doing wrong? I realize I could probably manually fix the “-” signs in the resulting fcsv files, but it does seem like there ought to be a better solution.</p>
<p>I’ve attached screeshots of the two text files side-by-side (Morphologika (.txt) on the left, Slicer (.fcsv) on the right) as well as what the landmarks and segmentation look like together in Slicer.</p>
<p>Thank you very much!<br>
Anya Auerbach, PhD student, University of Minnesota</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b1ec5715e540629c4f946d73778bdff24512b77.jpeg" data-download-href="/uploads/short-url/1Anb7dGW47BrxN7bqOyxMmyzWMD.jpeg?dl=1" title="fcsv_orientation_screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b1ec5715e540629c4f946d73778bdff24512b77_2_690x436.jpeg" alt="fcsv_orientation_screenshot" data-base62-sha1="1Anb7dGW47BrxN7bqOyxMmyzWMD" width="690" height="436" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b1ec5715e540629c4f946d73778bdff24512b77_2_690x436.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b1ec5715e540629c4f946d73778bdff24512b77_2_1035x654.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b1ec5715e540629c4f946d73778bdff24512b77_2_1380x872.jpeg 2x" data-dominant-color="BDBCDC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fcsv_orientation_screenshot</span><span class="informations">1920×1215 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f54155e59d8df26a27c0b4aa84f358a9cc84fad.png" data-download-href="/uploads/short-url/6KGAwz0VG83u9PhZJgMtRid7M3r.png?dl=1" title="landmark_comparison" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f54155e59d8df26a27c0b4aa84f358a9cc84fad_2_690x461.png" alt="landmark_comparison" data-base62-sha1="6KGAwz0VG83u9PhZJgMtRid7M3r" width="690" height="461" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f54155e59d8df26a27c0b4aa84f358a9cc84fad_2_690x461.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f54155e59d8df26a27c0b4aa84f358a9cc84fad_2_1035x691.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f54155e59d8df26a27c0b4aa84f358a9cc84fad_2_1380x922.png 2x" data-dominant-color="E4E4E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">landmark_comparison</span><span class="informations">2350×1572 282 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2024-11-19 00:24 UTC)

<p>MorphologikaLMConverter was written years ago for one dataset and never really tested thorougly. If you are an R user, my suggestion would be to read the original Morphologika file to R, then user the SlicerMorphR’s <code>write.markup.json</code> to save them as individual files (we will drop fcsv support Slicer sometime, so better use the json format).</p>
<p>Having said that, your issue seems simple the typical LPS to RAS problem. You can create a transform matrix in which the first two diagonal values are -1, and then put these fcsv files under that transform.</p>
<p>if they line up correctly, then you can harden the transform and save the file one more time and they will be fixed.</p>

---

## Post #3 by @A_Auerbach (2024-11-20 15:44 UTC)

<p>Thank you so much, the R function worked! That was a very straightforward solution so I didn’t try the transform option.<br>
I did notice that the documentation for write.markup.json didn’t seem to show up in R - the write.markups.fcsv function did and fortunately they seemed to work the same.<br>
Anya</p>

---

## Post #4 by @muratmaga (2024-11-20 16:31 UTC)

<p>Glad that it worked.</p>
<p>if you are not seeing write.markups.json, you are using an older version of SlicerMorphR. You can update to the latest one (which soon you will need).</p>

---
