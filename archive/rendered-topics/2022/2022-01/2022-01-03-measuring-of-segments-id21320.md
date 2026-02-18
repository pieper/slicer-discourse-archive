# Measuring of segments

**Topic ID**: 21320
**Date**: 2022-01-03
**URL**: https://discourse.slicer.org/t/measuring-of-segments/21320

---

## Post #1 by @mahinaz (2022-01-03 14:29 UTC)

<p>Hello<br>
I am using two mri  PD images that i have done below steps :</p>
<ol>
<li>I registered my images by simple registratio module in 3dslicer(fixed image was the image of patient in year of 2012 of his illness and the moving image was the image of patient in year of 2014 of his illness)</li>
<li>I applied median filter on two images</li>
<li>removed skull of head by Swiss skull stripper module</li>
</ol>
<p>Now i want to segment my images specially GM ; WM ; BASAL GANGLIA<br>
and then i meature its volume  and area   and then i capare them .<br>
What should i do?<br>
More explain: i segment my images by segment editor but it’s result are not exact</p>

---

## Post #2 by @lassoan (2022-01-03 14:35 UTC)

<p>You can segment the image with very high accuracy (you can segment anything that you see) using the Segment Editor module. If you start the segmentation from a low-resolution scan then you can adjust the segmentation to have higher resolution as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">here</a>.</p>

---

## Post #3 by @mahinaz (2022-01-03 21:13 UTC)

<p>Thanks for your answere; but i want to segment mi images automaticlly<br>
But by  tlThreshould effect of segment editor module i can segment it  semi automaticlly.<br>
I want to segment my images that i can know my segments…for example i want to know where is the Cortex in GM  or where is where is the Caudate in my segments and …<br>
One thing like MNI</p>

---

## Post #4 by @lassoan (2022-01-04 14:41 UTC)

<p>There are many fully automatic brain segmentation tools. Classic FreeSurfer, FSL, and several new neural network based methods. You can run the segmentation outside Slicer and load the segmentation results.</p>
<p>FreeSurfer uses an unusual coordinate system convention (relative to the input image instead of physical space), but the SlicerFreeSurfer extension has an importer that can take care of this. Other tools typically create a labelmap volume that can be loaded as a segmentation or volume.</p>

---

## Post #5 by @mahinaz (2022-01-08 20:09 UTC)

<p>i have another amateur question<br>
unfortunately i can’t install freesurfer and fsl . i don’t know why…may be it can’t be insatll on my system…<br>
now if i want to use from atlases in 3dslicer to segmentation,is there a waye in 3dslicer?<br>
and how should i access to atlases?<br>
or i have to download them? if yes ,from which site should i download them?<br>
explain: i used Mango Software too. but it can’t segment accurateely and automaticly. it also uses from Talairach and MNI atlases.<br>
but i don’t know can i use from atlases for segmentation in 3dslicer too???</p>

---

## Post #6 by @pieper (2022-01-09 16:02 UTC)

<p>Slicer’s segmentation tools are very powerful and general purpose, but if your goal is to do brain MRI segmentation then the suggestion to use specialized tools like freesurfer is really the best path.  If it’s not working on your computer then you should really try to fix that issue, either by getting a different computer, using a cloud rental-computer, or maybe just fixing the software on your current computer.</p>

---

## Post #8 by @mahinaz (2022-01-22 22:09 UTC)

<p>thanks. i segmented my images into three region GM and WM and CSF  by FSL software. my questions are:<br>
1.now i want to seperate cortical and subcortical  from  my segmentation by cropping or every other tool.<br>
how can i do thia accuratelly and automaticlly by 3dslicer?<br>
2.and then i want to meature my croped images to know  thw volume of which chapters has been reduced and compare two images. how should i do this?<br>
3.can i use Atlases like MNI and Talairach in 3dslicer for recognizing regions?</p>

---

## Post #10 by @pieper (2022-01-23 20:32 UTC)

<p>1 &amp; 2 - you shouldn’t need to crop, you can probably get what you need by loading our FSL results as a <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/index.html#segmentation">segmentation</a> and using the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html">segment statistics</a> module.</p>
<ol start="3">
<li>you could register your images to an atlas, but really it’s better to use freesurfer for that and <a href="https://github.com/PerkLab/SlicerFreeSurfer#:~:text=This%20repository%20contains%20the%20SlicerFreeSurfer,from%20FreeSurfer%20to%20Slicer%20coordinates.">import the results to slicer</a>.</li>
</ol>

---
