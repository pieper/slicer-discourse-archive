---
topic_id: 21451
title: "Convert Fcsv Files Into Nts Files"
date: 2022-01-13
url: https://discourse.slicer.org/t/21451
---

# Convert fcsv files into nts files

**Topic ID**: 21451
**Date**: 2022-01-13
**URL**: https://discourse.slicer.org/t/convert-fcsv-files-into-nts-files/21451

---

## Post #1 by @jusopar (2022-01-13 20:01 UTC)

<p>Is it possible to export landmarks as nts files? If not, is there a way to convert fcsv files into nts files?</p>
<p>Operating system: Windows<br>
Slicer version: 4.11.20210226<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @muratmaga (2022-01-13 20:14 UTC)

<p>Is this the nts format you are referring to? <a href="https://rdrr.io/cran/geomorph/man/readland.nts.html" class="inline-onebox" rel="noopener nofollow ugc">readland.nts: Read landmark data matrix from nts file in geomorph: Geometric Morphometric Analyses of 2D/3D Landmark Data</a></p>
<p>You can read this previous <a href="https://discourse.slicer.org/t/slicermorph-paper/18751/13">thread related getting data into MorphoJ format</a> and perhaps modify <a href="https://gist.github.com/smrolfe/f6ea90d9ff59bb306b8127b7342b4f6e" rel="noopener nofollow ugc">this example code</a> to make it work for nts format.</p>
<p>Short answer is there is no immediate way of converting fcsv to nts, without a script.</p>

---

## Post #3 by @jusopar (2022-01-13 20:20 UTC)

<p>Yes, that’s the nts format I referred to! I am planning to use it in geomorph indeed.</p>
<p>I believe this code will be of a great help! Thank you <a class="mention" href="/u/muratmaga">@muratmaga</a> !</p>

---

## Post #4 by @muratmaga (2022-01-13 22:16 UTC)

<p>İf you are going to use with geomorph, no need to convert fcsvs to nts.<br>
Use the utility functions in SlicerMorphR<br>
<code>devtools::install_github("SlicerMorph/SlicerMorphR")</code> and use the example code to import data into R<br>
Much easier!</p>

---

## Post #5 by @jusopar (2022-01-13 22:59 UTC)

<p>Perfect! Thank you so much!</p>

---
