---
topic_id: 16555
title: "Elastix Error 3Dslicer"
date: 2021-03-15
url: https://discourse.slicer.org/t/16555
---

# Elastix error_ 3dslicer

**Topic ID**: 16555
**Date**: 2021-03-15
**URL**: https://discourse.slicer.org/t/elastix-error-3dslicer/16555

---

## Post #1 by @sara_sharifi (2021-03-15 20:52 UTC)

<p>Hi</p>
<p>Windows7-64</p>
<p>Slicer4.11</p>
<p>Elastix windows64 v4.8</p>
<p>For NiFTI format (CT images) after apply General registration(elastix) module for 2 data I have this Error: Command ‘elastix’ returned non-zero exit status 4294967294.</p>
<p>Please help me how to solve this problem</p>
<p>thank you</p>

---

## Post #2 by @lassoan (2021-03-30 04:54 UTC)

<p>The problem should be fixed now. Update SlicerElastix extension (if you use latest Slicer Stable Release) or update Slicer and install SlicerElastix extension (if you use latest Slicer Preview release), and let us know if you run into any problems.</p>

---

## Post #3 by @sara_sharifi (2021-03-30 18:25 UTC)

<p>Thanks it’s ok very good thanks so much</p>

---

## Post #4 by @k.e_caliskan (2022-03-15 07:52 UTC)

<p>hi everyone<br>
The error was not fixed for me even though I followed all the instructions regarding this error. Is there any new solution for this error message?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58068ca3cfe80004999b91043c43608cc2fda4ae.png" data-download-href="/uploads/short-url/cyI33MdaHL95s4snA7q1mtrtYrc.png?dl=1" title="resim" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58068ca3cfe80004999b91043c43608cc2fda4ae.png" alt="resim" data-base62-sha1="cyI33MdaHL95s4snA7q1mtrtYrc" width="408" height="500" data-dominant-color="F4F5EF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">resim</span><span class="informations">486×595 20 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2022-03-19 13:54 UTC)

<p>Can you check if you get this error if you register the Slicer sample data sets as described here: <a href="https://github.com/lassoan/SlicerElastix/#register-two-volumes" class="inline-onebox">GitHub - lassoan/SlicerElastix: This extension makes available Elastix medical image registration toolkit (http://elastix.isi.uu.nl/) available in Slicer.</a> ?</p>
<p>Have you installed any software that uses ITK into system folders or folders that are listed in your <code>PATH</code> environment variable?</p>

---
