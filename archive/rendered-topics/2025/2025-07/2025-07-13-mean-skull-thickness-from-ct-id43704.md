---
topic_id: 43704
title: "Mean Skull Thickness From Ct"
date: 2025-07-13
url: https://discourse.slicer.org/t/43704
---

# Mean Skull Thickness from CT

**Topic ID**: 43704
**Date**: 2025-07-13
**URL**: https://discourse.slicer.org/t/mean-skull-thickness-from-ct/43704

---

## Post #1 by @TSatMGB (2025-07-13 20:00 UTC)

<p>Hey Everyone!</p>
<p>I’m currently working on a research project studying skull thickness and its relation to concussion risk using clinical CT scans. I’m using 3D Slicer for segmentation and measurement and would appreciate some guidance from the community to ensure I’m following best practices.</p>
<p>Project Overview:</p>
<ul>
<li>Retrospective study of ~400 patients</li>
<li>Goal: Extract mean/min/max skull thickness and mean HU density from CT scans</li>
<li>3D Slicer 5.8.1 on Windows (also tried on a Mac)</li>
<li>I’m currently using the CQ500 dataset for testing purposes because I thought it mimics actual clinical CTs best</li>
</ul>
<p>The density data is pretty easy to get using the Segment Statistics Tool but the mean Thickness is hard to calculate.</p>
<p>What I’ve Tried:</p>
<ul>
<li>BoneThicknessMapping: Runs, but Scalar Bar issues with newer version of Slicer, Seems to not recognize the entire skull as color mapping stops about half way. Exporting values not worked out.</li>
<li>ModelToModelDistance: Tried inner/outer surface comparison, but inner surface often distorted (e.g., swollen geometry), leading to inaccurate thickness.</li>
</ul>
<p>I even tried using Stradwin/Stradview but ran into issues with the .ply skull model for import.</p>
<p>Any help with verifying this approach or suggesting more robust alternatives would be greatly appreciated. I’m comfortable using the interface but not a coder.</p>
<p>Thanks in advance for your support!</p>

---

## Post #2 by @gntreece (2025-10-11 10:58 UTC)

<p>Stradview is a more specialised tool for some things, including cortical bone mapping. So this should be what you need for your specific task. There shouldn’t be an issue with loading a ply file, so perhaps you could let me know what the problem is and I can then fix it?</p>
<p>All the best,</p>
<p>Graham Treece (Stradview author)</p>

---
