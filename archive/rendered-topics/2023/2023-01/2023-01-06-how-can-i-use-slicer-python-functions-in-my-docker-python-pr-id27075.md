---
topic_id: 27075
title: "How Can I Use Slicer Python Functions In My Docker Python Pr"
date: 2023-01-06
url: https://discourse.slicer.org/t/27075
---

# How can I use slicer python functions in my docker python programs?

**Topic ID**: 27075
**Date**: 2023-01-06
**URL**: https://discourse.slicer.org/t/how-can-i-use-slicer-python-functions-in-my-docker-python-programs/27075

---

## Post #1 by @Rajesh_Ds (2023-01-06 06:02 UTC)

<p>I am trying to implement some medical image segmentation and visualization python programs on an aws instance. Later i want to build a docker image too. Just wanted to know what are the steps to be followed to make this happen on my aws linux instance. Could anyone help me with this.</p>

---

## Post #2 by @Rajesh_Ds (2023-01-06 08:28 UTC)

<p>I was trying to execute a python program with slicer functions, using the following command line</p>
<p>cmd = [“xvfb-run”,“-a”,“Slicer”,“–testing”, “–no-splash”,“–launcher-verbose”, “–python-script”, os.p$</p>
<p>process = subprocess.Popen(cmd)</p>
<p>and it throwed an error log as follows:</p>
<p>error: Application does NOT exists [/usr/bin/bin/SlicerApp-real]</p>

---

## Post #3 by @Rajesh_Ds (2023-01-06 08:29 UTC)

<p>Version of slicer is Slicer-4.13.0-2021-09-02-linux-amd64</p>

---

## Post #4 by @pieper (2023-01-06 15:01 UTC)

<p>This example shows how to run slicer python in a docker instance:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/pieper/SlicerDockers#running-a-slicer-analysis-script-in-an-instance">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/pieper/SlicerDockers#running-a-slicer-analysis-script-in-an-instance" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/23a9d1ef2057302379ea0c0d519a449ce8d7ef49dbe185be9b7119f376928be6/pieper/SlicerDockers" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/pieper/SlicerDockers#running-a-slicer-analysis-script-in-an-instance" target="_blank" rel="noopener">GitHub - pieper/SlicerDockers: docker config files for slicer</a></h3>

  <p>docker config files for slicer. Contribute to pieper/SlicerDockers development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
