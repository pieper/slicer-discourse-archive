# Adding many models to hierarchy

**Topic ID**: 13513
**Date**: 2020-09-16
**URL**: https://discourse.slicer.org/t/adding-many-models-to-hierarchy/13513

---

## Post #1 by @mfolson (2020-09-16 23:08 UTC)

<p>I am trying to create a label map for 100+ STLs. I was able to do this by importing all STLs as models, grouping them under a model hierarchy, importing the model hierarchy as a segmentation, and then exporting that segmentation as a Labelmap. Seems like it worked pretty well, but was tedious. My questions are:</p>
<ol>
<li>Is there a better method to go from multiple STL files to a Labelmap? I want each STL to have a separate value.</li>
<li>Is there a trick to grouping models under a model hierarchy? Doing this in the models module often is finicky and leads to crashes. I tried doing this in the subject hierarchy as well, but after placing them into the folder, they do not show up this way in the models module.</li>
</ol>
<p>Many thanks,<br>
Matt</p>

---

## Post #2 by @lassoan (2020-09-17 00:59 UTC)

<p>This should work robustly and much faster in recent Slicer-4.11 releases compared to Slicer-4.10 (using Subject hierarchy): you can put all your models into a folder and right-click and choose “Convert models to segmentation node”.</p>
<p>If you want to make this even more automated then you write a short python script for this (probably not more than 10-20 lines of code).</p>

---

## Post #3 by @mfolson (2020-09-17 16:09 UTC)

<p>Perfect, yes, I was using 4.10.2. I’ll try it out in the latest releases and then work on the python code. Good idea. Thank you!</p>

---
