# segment comparison and mesh statistics

**Topic ID**: 4242
**Date**: 2018-10-01
**URL**: https://discourse.slicer.org/t/segment-comparison-and-mesh-statistics/4242

---

## Post #1 by @fisher (2018-10-01 14:46 UTC)

<p>Recently I have done some work about segmentation,and it come to evaluate the results.<br>
First,I want to evaluate the dice similarity coefficient(DSC) and HD ,I know the module of segment comparison may help me, but I just want to know whether this module is based on 3D(volume). If not, how can i do it with the help of 3d slicer.<br>
Second,I have found some relevant information about mesh statistics ,and this module can evaluate two mesh.I want to know what does the “min”,“max”“mean” represent? Some say they are about HD? And whether can i use it to evaluate the results.<br>
Thanks a lot!!!</p>

---

## Post #2 by @cpinter (2018-10-01 15:25 UTC)

<p>Segment comparisons Dice and Hausdorff are both considering 3D. The module is in the SlicerRT extension.</p>
<p>I’m not sure I understand the question about min/max/mean. Do you mean int the Segment Statistics module? The segment statistics metrics are about the segments themselves and about the volume in the original anatomical volume the segment masks (e.g. min/max/mean HU for that segment in the CT). The statistics in Segment Comparison (max/mean/95%) are related to the Hausdorff distances. There are many Hausdorff distances measured (one for each surface point of the segment), and you can get their max, mean, and 95th percentile.</p>

---

## Post #3 by @fisher (2018-10-02 02:59 UTC)

<p>thanks a lot.What u said have helped me a lot.<br>
But the question about min/max/mean and so on is not  in the Segment statistics module but the mesh statistics.<br>
I have done all my work on other platforms, so i have got many segmentation objects in pairs.So maybe the results of mesh statistics is a way to represent HD?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb80d3b023273f68c677c853e843249649963c4b.png" data-download-href="/uploads/short-url/qKJir0lxCsq53GxazfJnJnX4GG7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb80d3b023273f68c677c853e843249649963c4b.png" alt="image" data-base62-sha1="qKJir0lxCsq53GxazfJnJnX4GG7" width="690" height="356" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1118×577 18.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @cpinter (2018-10-02 12:27 UTC)

<p>If you just want regular statistics for your segments, then I suggest using the Segment Statistics module.</p>
<p>Based on the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MeshStatistics">wiki page</a> of Mesh Statistics, it can do basic statistics, but on special data types (“MeshStatistics only works on a model that contains stored surface distances computed with the ModelToModelDistance module”). Is this special data type necessary for you?</p>

---
