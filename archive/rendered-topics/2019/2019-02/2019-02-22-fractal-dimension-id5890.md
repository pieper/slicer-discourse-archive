---
topic_id: 5890
title: "Fractal Dimension"
date: 2019-02-22
url: https://discourse.slicer.org/t/5890
---

# Fractal dimension

**Topic ID**: 5890
**Date**: 2019-02-22
**URL**: https://discourse.slicer.org/t/fractal-dimension/5890

---

## Post #1 by @PaoloZaffino (2019-02-22 16:58 UTC)

<p>Hi all,<br>
I’m writing to ask if a new extension can be interested for the community.<br>
In collaboration with some colleagues of mine, we wrote a python code for fractal dimension computation.<br>
We had this idea because we really struggled to find something “easy to use” (with no success), so now we would like to share our solution.<br>
For the moment it works just with 2D images, but our plan is to support also 3D volumes.</p>
<p>Do you think we can create a new scripted modules and expose it to the slicer users?</p>
<p>Thank you very much.<br>
Best.</p>
<p>Paolo</p>

---

## Post #2 by @Fernando (2019-02-25 22:50 UTC)

<p>Hi Paolo,</p>
<p>What do you use it for?</p>
<p>Best,<br>
Fernando</p>

---

## Post #3 by @fedorov (2019-02-25 23:10 UTC)

<p><a class="mention" href="/u/paolozaffino">@PaoloZaffino</a> for the sake of improved discoverability and reduced maintenance efforts, do you want to consider adding this as a new featureset to <a href="https://pyradiomics.readthedocs.io/en/latest/" rel="nofollow noopener">pyradiomics</a>? From a quick search, fractal dimension has been used for radiomics studies, e.g., see <a href="https://www.ncbi.nlm.nih.gov/pubmed/29230678" rel="nofollow noopener">https://www.ncbi.nlm.nih.gov/pubmed/29230678</a>.</p>
<p>pyradiomics already has a large and thriving community (see <a href="https://groups.google.com/forum/#!forum/pyradiomics" rel="nofollow noopener">mailing list</a> and <a href="https://github.com/Radiomics/pyradiomics" rel="nofollow noopener">github repo</a>), and is accompanied by the <a href="https://github.com/Radiomics/SlicerRadiomics" rel="nofollow noopener">SlicerRadiomics extension</a> exposing its features to the end user, so you would need to do no Slicer development, and your new features will magically become accessible to the SlicerRadiomics users. As an extra benefit, your features will be accessible in a package via PyPI and Conda, expanding the potential pool of happy users.</p>
<p>cc: <a class="mention" href="/u/joostjm">@JoostJM</a></p>
<p>suggested-by: <a class="mention" href="/u/rkikinis">@rkikinis</a></p>

---

## Post #4 by @PaoloZaffino (2019-02-27 15:52 UTC)

<p>Hi all!</p>
<p><a class="mention" href="/u/fernando">@Fernando</a> we use it to quantify vessel complexity.</p>
<p><a class="mention" href="/u/fedorov">@fedorov</a> <a class="mention" href="/u/joostjm">@JoostJM</a> thanks a lot for offering us this possibility…it would be great add our code to this project.<br>
<a class="mention" href="/u/pierangela00">@Pierangela00</a> is the PhD student that wrote the code and that is in charge of deploying it. Do you have any suggestion/guideline/policy about integrating our code into the project?</p>
<p>Thank you very much!<br>
Paolo</p>

---

## Post #5 by @fedorov (2019-02-27 16:08 UTC)

<aside class="quote no-group" data-username="PaoloZaffino" data-post="4" data-topic="5890">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/paolozaffino/48/81052_2.png" class="avatar"> PaoloZaffino:</div>
<blockquote>
<p>Do you have any suggestion/guideline/policy about integrating our code into the project?</p>
</blockquote>
</aside>
<p>Yes we do! <a href="https://github.com/Radiomics/pyradiomics/blob/master/CONTRIBUTING.rst" class="inline-onebox">pyradiomics/CONTRIBUTING.rst at master · AIM-Harvard/pyradiomics · GitHub</a></p>

---

## Post #6 by @Fernando (2019-02-28 16:30 UTC)

<aside class="quote no-group" data-username="PaoloZaffino" data-post="4" data-topic="5890">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/paolozaffino/48/81052_2.png" class="avatar"> PaoloZaffino:</div>
<blockquote>
<p><a class="mention" href="/u/fernando">@Fernando</a> we use it to quantify vessel complexity.</p>
</blockquote>
</aside>
<p>That’s very interesting and related to my work, I’m looking forward to trying the code!</p>

---

## Post #7 by @PaoloZaffino (2019-03-01 11:22 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> thanks a lot.<br>
Any suggestion about the file/place where we could put our code?<br>
Is there an already defined data structure to get/return images?</p>
<p>Thank you.</p>

---

## Post #8 by @fedorov (2019-03-01 14:47 UTC)

<p>There is already functionality to computer texture images, so maybe that is similar. I suggest you create an issue under pyradiomics, describe your code and discuss details there.</p>

---

## Post #9 by @JoostJM (2019-03-18 12:57 UTC)

<p>If I’m correct, fractal dimension features returns values on a segment level (i.e. where each values describes the entire region of interest), this would make it ideal to implement as a feature class. If it returns values per voxel (and therefore generates a parameter map), it is best implemented as an image type (=filter).</p>
<p>Both signatures are described <a href="https://pyradiomics.readthedocs.io/en/latest/developers.html#" rel="nofollow noopener">here</a>.<br>
If you require assistance, let us know by submitting a PR or issue on the github as <a class="mention" href="/u/fedorov">@fedorov</a> suggested.</p>

---
