---
topic_id: 24850
title: "Tips For Getting Started Loading And Batch Segmenting Files"
date: 2022-08-21
url: https://discourse.slicer.org/t/24850
---

# Tips for getting started loading and batch segmenting files with Slicer in python?

**Topic ID**: 24850
**Date**: 2022-08-21
**URL**: https://discourse.slicer.org/t/tips-for-getting-started-loading-and-batch-segmenting-files-with-slicer-in-python/24850

---

## Post #1 by @Mike_Flanigan (2022-08-21 07:58 UTC)

<p>I’m new to Slicer and am working on a project trying to automate a few Slicer steps for many files by creating a python script and then running it without opening the Slicer GUI.</p>
<p>I’ve been reading through sections in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" rel="noopener nofollow ugc">the slicer docs</a> in particular the “Run a Python script file in the Slicer environment” seems to be what I’m trying to do.</p>
<p>The part I’m stuck on is the very first step of how to load a file (tif file as a Volume) in slicer through python. I’d really appreciate any tips or example code on how to do this part!</p>
<p>For bigger picture context, I have a folder with dozens of .tif files from CTs. I’d like to run a script that will for each .tif file replicate the following steps I’ve been doing in the Slicer GUI:</p>
<ul>
<li>Load the tif file as a Volume (Add data button)</li>
<li>Segment based on a threshold</li>
<li>Select remove island based on a known location (background CT scan equipment)</li>
<li>Save the segmentation quantification &amp; a .stl file of the 3d model</li>
</ul>
<p>Thanks!</p>

---

## Post #2 by @pieper (2022-08-22 15:23 UTC)

<p>That process sounds very feasible.  You’ll need to put together snippets of functionality from the script repository.  I saw there weren’t specific batch processing examples so I put in a few examples <a href="https://github.com/Slicer/Slicer/pull/6508/files">in this PR</a>.</p>

---

## Post #3 by @Mike_Flanigan (2022-09-05 22:52 UTC)

<p>Thank you!<br>
That script got me well ahead and working.<br>
I do have two follow up questions now, but they’re rather distinct so I’ve made them new questions:</p>
<ol>
<li><a href="https://discourse.slicer.org/t/remove-largest-island-functionality/25110" class="inline-onebox">Remove largest island functionality?</a></li>
<li><a href="https://discourse.slicer.org/t/export-volume-or-segment-to-stl-file-with-python/25111" class="inline-onebox">Export volume (or segment?) to stl file with python</a></li>
</ol>

---

## Post #4 by @muratmaga (2022-09-06 05:17 UTC)

<p>Check this script example for running island tool and exporitng the segmentation and writing to the disk:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SlicerMorph/Scripts#2-run-an-image-processing-pipeline-on-a-folder-of-volumes">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/Scripts#2-run-an-image-processing-pipeline-on-a-folder-of-volumes" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/86b9de2c26925ed33403bfebd5558d6c498595e2621c86ed6ac7b93cc5ac64a3/SlicerMorph/Scripts" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/SlicerMorph/Scripts#2-run-an-image-processing-pipeline-on-a-folder-of-volumes" target="_blank" rel="noopener nofollow ugc">GitHub - SlicerMorph/Scripts</a></h3>

  <p>Contribute to SlicerMorph/Scripts development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
