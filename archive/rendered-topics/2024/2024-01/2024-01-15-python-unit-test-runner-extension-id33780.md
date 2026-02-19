---
topic_id: 33780
title: "Python Unit Test Runner Extension"
date: 2024-01-15
url: https://discourse.slicer.org/t/33780
---

# Python Unit Test Runner Extension

**Topic ID**: 33780
**Date**: 2024-01-15
**URL**: https://discourse.slicer.org/t/python-unit-test-runner-extension/33780

---

## Post #1 by @Thibault_Pelletier (2024-01-15 12:01 UTC)

<p>Hi everyone,</p>
<p>I’m in the process of creating a Python Unit Test Runner Extension.</p>
<p>This module provides (IMO) an efficient way to develop new Python based extensions  and allows to do test driven development by having :</p>
<ul>
<li>A test runner module accessible directly from 3D Slicer to run tests in an independant 3D Slicer instance</li>
<li>A decorator which allows to run tests directly in your favorite IDE</li>
</ul>
<p>Here are a few screenshots of the extension in use :</p>
<p>test runner :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6ca54eb1800c2ba57872f369865f4577c803d438.png" data-download-href="/uploads/short-url/fv7JEdXWNZREZCIl0qARdeF2Ht6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6ca54eb1800c2ba57872f369865f4577c803d438.png" alt="image" data-base62-sha1="fv7JEdXWNZREZCIl0qARdeF2Ht6" width="325" height="500" data-dominant-color="ECEFF1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">407×626 15.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>test decorator :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/aed1345be028c3a1521ccf34c68deaaba6105b97.png" data-download-href="/uploads/short-url/oWvivouKrX7kTt3vf3H9E0CZud1.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/aed1345be028c3a1521ccf34c68deaaba6105b97_2_690x226.png" alt="image" data-base62-sha1="oWvivouKrX7kTt3vf3H9E0CZud1" width="690" height="226" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/aed1345be028c3a1521ccf34c68deaaba6105b97_2_690x226.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/aed1345be028c3a1521ccf34c68deaaba6105b97.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/aed1345be028c3a1521ccf34c68deaaba6105b97.png 2x" data-dominant-color="232426"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1016×333 33.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The module uses the following librairies for test run / discovery / reporting :</p>
<ul>
<li>pytest</li>
<li>pytest-json-report</li>
</ul>
<p>I plan to release the extension on the extension manager soon and I wanted to have the community’s feeback (especially <a class="mention" href="/u/jcfr">@jcfr</a> &amp; <a class="mention" href="/u/lassoan">@lassoan</a> ).  <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Thanks in advance,<br>
Best,<br>
Thibault</p>

---

## Post #2 by @jamesobutler (2024-01-15 13:01 UTC)

<p><a class="mention" href="/u/thibault_pelletier">@Thibault_Pelletier</a> Is this module something you created because you found that the “Self Tests” (<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/selftests.html" class="inline-onebox" rel="noopener nofollow ugc">Self Tests — 3D Slicer documentation</a>) module did not provide all the functionality that you were hoping? Could the improvements you made here possibly be integrated for the existing Self Tests module?</p>

---

## Post #3 by @Thibault_Pelletier (2024-01-15 13:13 UTC)

<p>Hi <a class="mention" href="/u/jamesobutler">@jamesobutler</a>, yes I developped this extension because the self test functionalities where too limited for my usage.</p>
<p>Basically when building bigger extensions or when wanting to split the implementation into packages, the self test becomes cumbersome to use and requires frequent restarts of the 3D Slicer UI to really test the content of the extension.</p>
<p>The extension can be integrated directly into the self test module or into 3D Slicer core directly (I don’t have any preferences). As it’s pulling PyTest and PyTest JSON Report, I wasn’t sure what was the best option and wanted to consult with the community.</p>
<p>I have just pushed the current version here :</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/KitwareMedical/SlicerPythonTestRunner">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/KitwareMedical/SlicerPythonTestRunner" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/0149d186610dbac0e94fcfde8fb3722f46ec83cc814166b61c55c6bc4f8250e9/KitwareMedical/SlicerPythonTestRunner" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/KitwareMedical/SlicerPythonTestRunner" target="_blank" rel="noopener nofollow ugc">GitHub - KitwareMedical/SlicerPythonTestRunner: Python test runner extension...</a></h3>

  <p>Python test runner extension for 3D Slicer based on PyTest and PyTest JSON Report - GitHub - KitwareMedical/SlicerPythonTestRunner: Python test runner extension for 3D Slicer based on PyTest and Py...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I have only tested it on Windows, so I’ll have to have a look on Linux to check if it works as expected.</p>
<p>Edit: I did some justifications as to the why of the lib here : <a href="https://github.com/KitwareMedical/SlicerPythonTestRunner?tab=readme-ov-file#why-this-extension" class="inline-onebox" rel="noopener nofollow ugc">GitHub - KitwareMedical/SlicerPythonTestRunner: Python test runner extension for 3D Slicer based on PyTest and PyTest JSON Report</a></p>

---

## Post #4 by @Thibault_Pelletier (2024-01-15 15:23 UTC)

<p>For information, I had a few bugs in the extension (in particular on Linux).</p>
<p>It should be usable now !</p>
<p>Best,<br>
Thibault</p>

---
