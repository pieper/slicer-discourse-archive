---
topic_id: 24042
title: "Integrate Python File With 3D Slicer"
date: 2022-06-25
url: https://discourse.slicer.org/t/24042
---

# Integrate python file with 3d slicer

**Topic ID**: 24042
**Date**: 2022-06-25
**URL**: https://discourse.slicer.org/t/integrate-python-file-with-3d-slicer/24042

---

## Post #1 by @gfurnari (2022-06-25 10:06 UTC)

<p>Hi everyone, i’m trying to use python code to automate a process that uses 3d slicer’s modules + some functions that i made myself. So basically i need to call 3d slicer’s modules, slicer.util, etc from my file, just like doing that on python console on 3d slicer, and interact with 3d slicer using my python file (i hope it’s clear what my problem is).<br>
I tried to create a new module with extension wizard but when i call “from slicer.util import …” it tells me that slicer.util is not found.<br>
Could it be an environment problem?</p>
<p>Thank you very much for your help.</p>

---

## Post #2 by @pieper (2022-06-25 16:19 UTC)

<p>Be sure you follow the examples carefully.  This tutorial is a good one to show all the steps:</p>
<aside class="onebox googledocs" data-onebox-src="https://docs.google.com/presentation/d/1JXIfs0rAM7DwZAho57Jqz14MRn2BIMrjB17Uj_7Yztc/edit#slide=id.g41f90baec_028">
  <header class="source">

      <a href="https://docs.google.com/presentation/d/1JXIfs0rAM7DwZAho57Jqz14MRn2BIMrjB17Uj_7Yztc/edit#slide=id.g41f90baec_028" target="_blank" rel="noopener">docs.google.com</a>
  </header>

  <article class="onebox-body">
    <a href="https://docs.google.com/presentation/d/1JXIfs0rAM7DwZAho57Jqz14MRn2BIMrjB17Uj_7Yztc/edit#slide=id.g41f90baec_028" target="_blank" rel="noopener"><span class="googledocs-onebox-logo g-slides-logo"></span></a>

<h3><a href="https://docs.google.com/presentation/d/1JXIfs0rAM7DwZAho57Jqz14MRn2BIMrjB17Uj_7Yztc/edit#slide=id.g41f90baec_028" target="_blank" rel="noopener">Developing extension in 3D Slicer</a></h3>

<p>Developing and contributing extensions for 3D Slicer Andrey Fedorov, PhD, Brigham and Women’s Hospital/Harvard Medical School Jean-Christophe Fillion-Robin, Kitware Inc. Steve Pieper, PhD, Isomics Inc. fedorov@bwh.harvard.edu First presented: Nov 18,...</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>There are more examples here:<br>
<a href="https://www.slicer.org/wiki/Documentation/4.10/Training#Tutorials_for_software_developers" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/4.10/Training#Tutorials_for_software_developers</a></p>
<p>If there’s a specific spot in one of the tutorials where things don’t work for you let us know which steps you followed.</p>

---

## Post #3 by @gfurnari (2022-06-25 17:15 UTC)

<p>Thank you <a class="mention" href="/u/pieper">@pieper</a> for your quick reply. I’ll follow theese tutorials and let you know if i can’t solve the problem.</p>

---
