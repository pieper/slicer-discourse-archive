# Slicer/.nrrd Coordinate Systems

**Topic ID**: 19827
**Date**: 2021-09-23
**URL**: https://discourse.slicer.org/t/slicer-nrrd-coordinate-systems/19827

---

## Post #1 by @Yoshi888 (2021-09-23 15:57 UTC)

<p>Hello everyone,</p>
<p>I am IT student and new to the medical field. I am currently working on Image Processing/Classification Tasks and working with Slicer. I still think I have some understanding issues regarding the Coordinate System used and was hoping you guys could maybe help me.</p>
<p>I currently have data in .nrrd files I work with. From the Header Information I can extract:</p>
<p>‘space’:  ‘left-posterior-superior’  → So I can assume my Data is in LPS</p>
<p>‘space directions’:</p>
<p>[ 5.98936111e-01,  6.15821439e-05, -5.15675320e-03]<br>
[-1.20481869e-08,  5.98915625e-01,  7.15087395e-03]<br>
[ 4.13286886e-02, -5.73043156e-02,  4.79947636e+00]</p>
<p>‘space origin’:</p>
<p>[-115.52378082,  -56.22384262,  -92.38769531]</p>
<p>So I assume my data is using this system? As Slicer uses RAS it transforms this data from LPS to RAS when viewing it in Slicer?</p>
<p>I would like to rescale all my images to 1 in x, y direction to make them more comparable.<br>
To do that I just have to apply a corresponding transformation matrix to my data if my understanding is correct?</p>
<p>Overall I am still confused as to what corresponds to what data in which coordinate system.</p>

---

## Post #2 by @pieper (2021-09-23 21:02 UTC)

<p>If you haven’t already you should study this page:</p>
<p><a href="https://www.slicer.org/wiki/Coordinate_systems" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Coordinate_systems</a></p>
<p>Slicer works internally in RAS but many output formats are LPS implicitly while others are implicitly RAS.  Many formats have a flag in the header that says LPS or RAS which we try to respect or you can select the reference when importing files.</p>

---

## Post #3 by @lassoan (2021-09-24 18:10 UTC)

<p>Datasets created by earlier Slicer versions may have used either LPS or RAS coordinate system in files. In recent Slicer releases by default all node types (volumes, models, markups, etc.) are saved in LPS coordinate system.</p>

---

## Post #4 by @Yoshi888 (2021-09-29 07:37 UTC)

<p>That Website was indeed very helpful, thank you!</p>
<p>So if I have understood it correctly with the Information from the Header I can transform my Data from IJK to LPS/RAS by applying the matrix.<br>
’<br>
I have ADC Maps and T2 Seq and a transformation for registration.</p>
<p>So in my Code I would then have to transform both Images to LPS and then apply the transformation from my registration and then I can  transform them back to IJK coordinates so I can proceed with my Image Processing.<br>
Is that understanding correct?</p>

---
