---
topic_id: 47637
title: "Segment tooth enamel and pulp from TotalSegmentator tooth-by-tooth"
date: 2026-07-15
url: https://discourse.slicer.org/t/47637
last_bumped: 2026-07-19T18:11:58.498Z
---

# Segment tooth enamel and pulp from TotalSegmentator tooth-by-tooth

**Topic ID**: 47637
**Date**: 2026-07-15
**URL**: https://discourse.slicer.org/t/segment-tooth-enamel-and-pulp-from-totalsegmentator-tooth-by-tooth/47637

---

## Post #1 by @r_vorup (2026-07-15 14:23 UTC)

<p>Hello all,</p>
<p>I have used the TotalSegmentator to segment a CBCT scan of upper and lower jaw, and have gotten each tooth in an individual segment. I now want to split each tooth into dentine and enamel, for them to be 3D printed in different materials. I have tried to use thresholding within the segment to separate the enamel, but since the tooth output from the TotalSegmentator is a bit “blocky”, the thresholded enamel is more smooth than the existing segment, leaving me with the “slats” as seen in the image. Most of these are not islands and are therefore very tedious to remove. Does anyone have a suggest on how to solve this?</p>
<p>Since the purpose is 3D printing a complete jaw where teeth should fit perfectly into the bone, I’m trying to avoid smoothing until I can do a joint smoothing of all tooth parts and bone in the same go, to hopefully not move any boudaries. I hope this makes sense.</p>
<p>Thank you for any input!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08d34fa067428245d116b00baa8a9bad6270b86b.jpeg" data-download-href="/uploads/short-url/1g4ychlpLgijBHxq5ZjQBTt4PeH.jpeg?dl=1" title="dentine_enamel_split" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08d34fa067428245d116b00baa8a9bad6270b86b_2_655x500.jpeg" alt="dentine_enamel_split" data-base62-sha1="1g4ychlpLgijBHxq5ZjQBTt4PeH" width="655" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08d34fa067428245d116b00baa8a9bad6270b86b_2_655x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08d34fa067428245d116b00baa8a9bad6270b86b_2_982x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08d34fa067428245d116b00baa8a9bad6270b86b.jpeg 2x" data-dominant-color="9A90C0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">dentine_enamel_split</span><span class="informations">1161×885 81 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @finetjul (2026-07-16 07:04 UTC)

<p>If the problem is only in 3D and not in 2D, it probably means that you need to check the 2D to 3D “smoothing” parameter.</p>

---

## Post #3 by @r_vorup (2026-07-16 10:51 UTC)

<p>Thank you for the suggestion, but it is present also in 2D, so it is not just a question of the 3D visualization.</p>

---

## Post #4 by @finetjul (2026-07-16 12:51 UTC)

<p>I’m not sure to understand what you “thresholded” then.</p>
<p>You could use the segmented tooth as a “mask” to then apply the threshold. You are ensured that the thresholded voxels only belong to the previously segmented voxels.</p>

---

## Post #5 by @Lukon (2026-07-19 18:11 UTC)

<p>I wrote an extension that performs anatomical segmentation of a tooth starting from micro-CT. It separates the tooth into enamel and dentin using a threshold-based segmentation pipeline.</p>
<p>I am not very familiar with CBCT scans, and I have never tested the extension with them, but it might work for your use case.</p>
<p>The extension is currently still in code review and is not available through the Slicer Extension Manager. However, you can install it manually by importing the main branch of the extension:</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/lukaskonietzka/SlicerToothAnalyser">
  <header class="source">

      <a href="https://github.com/lukaskonietzka/SlicerToothAnalyser" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/d9f43b338e27f3f2f43debdf2ab20bc7/lukaskonietzka/SlicerToothAnalyser" class="thumbnail">

  <h3><a href="https://github.com/lukaskonietzka/SlicerToothAnalyser" target="_blank" rel="noopener nofollow ugc">GitHub - lukaskonietzka/SlicerToothAnalyser: This 3D Slicer Extension provides specialized...</a></h3>

    <p><span class="github-repo-description">This 3D Slicer Extension provides specialized preprocessing, segmentation, and analysis features tailored for the analysis of tooth anatomy and pathology starting from µCT</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
