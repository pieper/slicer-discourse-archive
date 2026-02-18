# Registration and contour comparison

**Topic ID**: 13645
**Date**: 2020-09-23
**URL**: https://discourse.slicer.org/t/registration-and-contour-comparison/13645

---

## Post #1 by @BORIPHAT (2020-09-23 06:14 UTC)

<p>Hello,<br>
I would like to compare two data sets. The first CT data set is Reference data and the second data is deformed data. I would like to know “How much the second data deformed”?</p>
<ol>
<li>How to registration between data set 1 and 2?  Firstly, I try to open two Dicom files for comparing but it can open only one data set.</li>
<li>How to analyze the contour for the metrics  (Dice Similarity Coefficient and Hausdorff distances).  Firstly, I try to use the Segment Comparison module but It can choose only one data in two segments but I would like to compare two Dicom files.</li>
</ol>
<p>Thank you very much</p>

---

## Post #2 by @Andinet_Enquobahrie (2020-09-23 11:40 UTC)

<p>Hello, <a class="mention" href="/u/boriphat">@BORIPHAT</a></p>
<aside class="quote no-group" data-username="BORIPHAT" data-post="1" data-topic="13645" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/67e7ee/48.png" class="avatar"> BORIPHAT:</div>
<blockquote>
<ol>
<li>How to registration between data set 1 and 2?  Firstly, I try to open two Dicom files for comparing but it can open only one data set.</li>
</ol>
</blockquote>
</aside>
<p>You definitely want to spend some time going over the Registration tutorial to learn on how to do this</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Registration" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/Training#Registration</a></p>
<aside class="quote no-group" data-username="BORIPHAT" data-post="1" data-topic="13645" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/67e7ee/48.png" class="avatar"> BORIPHAT:</div>
<blockquote>
<ol start="2">
<li>How to analyze the contour for the metrics  (Dice Similarity Coefficient and Hausdorff distances).  Firstly, I try to use the Segment Comparison module but It can choose only one data in two segments but I would like to compare two Dicom files.</li>
</ol>
</blockquote>
</aside>
<p>You will have to segment the two Dicom files first if you would like to do this.</p>
<p>Please go over the segmentation tutorials.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation</a></p>
<p>Hope this helps<br>
Andinet</p>

---

## Post #3 by @BORIPHAT (2020-09-24 02:32 UTC)

<p>Thank you so much for your quick reply. I choose only one folder and have 2 data subset in this folder for comparison. When I click on DATA &gt;Choose directory to Add &gt; select folder. It shows more than 2 nodes. How can I import files?  <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06a327f22b187de3b81cf8a02514063a00b03026.png" data-download-href="/uploads/short-url/WIqlN79pIXWfaDdapVKPtAYnlQ.png?dl=1" title="D2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06a327f22b187de3b81cf8a02514063a00b03026_2_236x500.png" alt="D2" data-base62-sha1="WIqlN79pIXWfaDdapVKPtAYnlQ" width="236" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06a327f22b187de3b81cf8a02514063a00b03026_2_236x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06a327f22b187de3b81cf8a02514063a00b03026_2_354x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06a327f22b187de3b81cf8a02514063a00b03026_2_472x1000.png 2x" data-dominant-color="ECECEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">D2</span><span class="informations">517×1092 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2020-09-24 03:36 UTC)

<p>Please use the DICOM module to import and load DICOM data sets. See some more information here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#data-loading-and-saving">https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#data-loading-and-saving</a></p>

---
