---
topic_id: 438
title: "Sample Data Wiki Download Url Changed"
date: 2017-06-03
url: https://discourse.slicer.org/t/438
---

# Sample data wiki download URL changed

**Topic ID**: 438
**Date**: 2017-06-03
**URL**: https://discourse.slicer.org/t/sample-data-wiki-download-url-changed/438

---

## Post #1 by @lassoan (2017-06-03 12:12 UTC)

<p>Slicer fails to download sample data from the wiki that causes many errors (for example <a href="http://trunk.cdash.org/viewTest.php?onlyfailed&amp;buildid=1036019">http://trunk.cdash.org/viewTest.php?onlyfailed&amp;buildid=1036019</a>).</p>
<p>URLs that used to work before yesterday:<br>
<a href="http://www.slicer.org/slicerWiki/images/4/43/MR-head.nrrd" class="onebox" target="_blank">http://www.slicer.org/slicerWiki/images/4/43/MR-head.nrrd</a><br>
<a href="http://www.slicer.org/slicerWiki/images/3/31/CT-chest.nrrd" class="onebox" target="_blank">http://www.slicer.org/slicerWiki/images/3/31/CT-chest.nrrd</a><br>
<a href="http://www.slicer.org/slicerWiki/images/0/00/CTA-cardio.nrrd" class="onebox" target="_blank">http://www.slicer.org/slicerWiki/images/0/00/CTA-cardio.nrrd</a><br>
<a href="http://www.slicer.org/slicerWiki/images/0/01/DTI-Brain.nrrd" class="onebox" target="_blank">http://www.slicer.org/slicerWiki/images/0/01/DTI-Brain.nrrd</a><br>
<a href="http://www.slicer.org/slicerWiki/images/5/59/RegLib_C01_1.nrrd" class="onebox" target="_blank">http://www.slicer.org/slicerWiki/images/5/59/RegLib_C01_1.nrrd</a><br>
<a href="http://www.slicer.org/slicerWiki/images/e/e3/RegLib_C01_2.nrrd" class="onebox" target="_blank">http://www.slicer.org/slicerWiki/images/e/e3/RegLib_C01_2.nrrd</a></p>
<p>It seems that the data sets are still available on the wiki, but with a slightly different URL:<br>
<a href="https://www.slicer.org/w/images/4/43/MR-head.nrrd" class="onebox" target="_blank">https://www.slicer.org/w/images/4/43/MR-head.nrrd</a><br>
<a href="https://www.slicer.org/w/images/3/31/CT-chest.nrrd" class="onebox" target="_blank">https://www.slicer.org/w/images/3/31/CT-chest.nrrd</a></p>
<p><a class="mention" href="/u/mhalle">@mhalle</a> <a class="mention" href="/u/jcfr">@jcfr</a><br>
Could the old URLs be made to work again?<br>
In the long term, should we move sample data to Midas or use a different URL?</p>

---

## Post #2 by @pieper (2017-06-03 13:13 UTC)

<p>adding <a class="mention" href="/u/freephile">@freephile</a></p>
<p>Let’s please try to make the old url work if at all possible.</p>

---

## Post #3 by @lassoan (2017-06-03 17:34 UTC)

<p>Yes, making the old URL work again is very important, as there are tens of thousands of Slicer instances already installed that keep looking for the data at that location.</p>
<p>In new Slicer versions, should we download the data from Midas? A couple of sample data sets are already downloaded from there.</p>

---

## Post #4 by @lassoan (2017-06-03 18:14 UTC)

<p>Many extension logos are also stored on the wiki, so lots of images are missing from the extension manager, too:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/4b44e3825ac6d34cb213b6f891c5221f4b0fd7ef.png" data-download-href="/uploads/short-url/aJRp1FlIUnuOaEe0snoVZRRxO7d.png?dl=1" title="image.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/4b44e3825ac6d34cb213b6f891c5221f4b0fd7ef_2_689x332.png" width="689" height="332" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/4b44e3825ac6d34cb213b6f891c5221f4b0fd7ef_2_689x332.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/4b44e3825ac6d34cb213b6f891c5221f4b0fd7ef_2_1033x498.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/4b44e3825ac6d34cb213b6f891c5221f4b0fd7ef_2_1378x664.png 2x" data-dominant-color="DCE2E3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">2601×1255 840 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @freephile (2017-06-03 20:09 UTC)

<p>I’ll have this fixed shortly.  I moved rewrite rules into the Apache configuration to make the server faster, but obviously one of them is wrong.  I’ll be able to debug it and fix it up shortly.</p>

---

## Post #6 by @freephile (2017-06-03 21:34 UTC)

<p>OK, this should be fixed now.  A passthrough flag was the culprit.</p>
<p>In case of any additional problems, please provide the specific URL.</p>
<p>Thanks</p>

---

## Post #7 by @pieper (2017-06-03 22:04 UTC)

<p>Confirmed - thanks!</p>
<p>(extra characters…)</p>

---

## Post #8 by @jcfr (2017-06-04 02:19 UTC)

<p>Thanks Greg <img src="https://emoji.discourse-cdn.com/twitter/thumbsup.png?v=5" title=":thumbsup:" class="emoji" alt=":thumbsup:"></p>

---
