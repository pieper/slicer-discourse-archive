---
topic_id: 13469
title: "Issue While Exporting Stl Model"
date: 2020-09-13
url: https://discourse.slicer.org/t/13469
---

# issue while exporting stl model

**Topic ID**: 13469
**Date**: 2020-09-13
**URL**: https://discourse.slicer.org/t/issue-while-exporting-stl-model/13469

---

## Post #1 by @sandy (2020-09-13 13:10 UTC)

<p>Operating system: window 7<br>
Slicer version:4.10.2<br>
Expected behavior: should export proper model<br>
Actual behavior: the problem is in exporting stl or obj model from slicer software meanwhile importing it into the cura , its displaying the file has been corrupted or invalid file<br>
so  what further tweaks i have to do for this</p>

---

## Post #2 by @pieper (2020-09-13 14:28 UTC)

<aside class="quote no-group" data-username="sandy" data-post="1" data-topic="13469">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/2bfe46/48.png" class="avatar"> sandy:</div>
<blockquote>
<p>importing it into the cura , its displaying the file has been corrupted or invalid file</p>
</blockquote>
</aside>
<p>I don’t know what “cura” is, but the STL files produced by Slicer should work fine in most 3D printing tools and viewers.  Why don’t you try some others and see if it’s an issue with the data file or that software.  If you think you are generating a bad file with Slicer, please describe your exact steps and share any example data if possible.</p>

---

## Post #3 by @jamesobutler (2020-09-13 19:42 UTC)

<p>It looks like <a href="https://en.wikipedia.org/wiki/Cura_(software)" rel="nofollow noopener">Cura</a> might complain if your STL has too many polygons such as:</p>
<p><code>AssertionError: File too large, got 603979776 triangles which exceeds the maximum of 10000000</code></p>
<p>Is your model large in size and in number of polygons?</p>

---

## Post #4 by @sandy (2020-09-14 04:08 UTC)

<p>file is small itself and hence I exported it from segmentation editor option i resolved my issue<br>
thnks jamesobutler</p>

---

## Post #5 by @sandy (2020-09-14 04:12 UTC)

<ol>
<li>first i imported dicom file and selected volume rendering option of ct bones structure</li>
<li>then did some tweaks in segment editor and exported the file through segmention option earlier</li>
<li>maybe for this option stl didnt come properly as i imported respected stl in meshmixir also<br>
4.so when i exported stl through segmentation which is in segment editor option it worked properly<br>
donno what could be miracle???</li>
</ol>

---
