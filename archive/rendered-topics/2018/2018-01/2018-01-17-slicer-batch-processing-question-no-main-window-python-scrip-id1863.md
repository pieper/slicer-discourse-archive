---
topic_id: 1863
title: "Slicer Batch Processing Question No Main Window Python Scrip"
date: 2018-01-17
url: https://discourse.slicer.org/t/1863
---

# Slicer batch processing question (--no-main-window --python-script)

**Topic ID**: 1863
**Date**: 2018-01-17
**URL**: https://discourse.slicer.org/t/slicer-batch-processing-question-no-main-window-python-script/1863

---

## Post #1 by @NaglisR (2018-01-17 16:06 UTC)

<p>Hi everyone,</p>
<p>I am trying to find the best way to quickly batch process a number of folders containing head MRI dicom files to .nii files. Basically the pipeline should work like this: import the dicom files &gt; load them as a volume &gt; save the volume as a .nii file.<br>
I am trying to do this using the slicer from terminal: <code>Slicer --no-main-window --python-script</code> (as is described in here <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_to_access_a_scripted_module_from_python_scripts" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_to_access_a_scripted_module_from_python_scripts</a>)<br>
The python script goes like this:</p>
<pre><code class="lang-auto">i = ctk.ctkDICOMIndexer()
i.addDirectory(slicer.dicomDatabase, '/home/me/Documents/25/25')
</code></pre>
<p>How can I do the next necessary steps to load the dicom files as volumes and save them as .nii files?</p>
<p>Thank you in advance</p>

---

## Post #2 by @cpinter (2018-01-17 16:19 UTC)

<p>There’s a module for a similar task</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerRt/SlicerRT/tree/master/BatchProcessing">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerRt/SlicerRT/tree/master/BatchProcessing" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerRt/SlicerRT/tree/master/BatchProcessing" target="_blank" rel="noopener">SlicerRT/BatchProcessing at master · SlicerRt/SlicerRT</a></h3>

  <p><a href="https://github.com/SlicerRt/SlicerRT/tree/master/BatchProcessing" target="_blank" rel="noopener">master/BatchProcessing</a></p>

  <p><span class="label1">Open-source toolkit for radiation therapy research, an extension of 3D Slicer. Features include DICOM-RT import/export, dose volume histogram, dose accumulation, external beam planning (TPS), struc...</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Your use case seems to be simpler than this, and most of it is contained in this module. What you need to implement in addition is the one-line command to save the loaded volume as nii.</p>

---

## Post #3 by @NaglisR (2018-01-17 16:34 UTC)

<p>Thank you for your response. What I am looking for is ways to batch process multiple files through scripting with python. Perhaps there is some tutorial or a wiki page about this kind of processing? For example, I am not able to find the command to load the imported dicom files as a volume (without the Slicer GUI because I need to to do it as a batch script). Later on I will probably need to batch process more than just loading and saving.</p>

---

## Post #4 by @fedorov (2018-01-17 23:03 UTC)

<p>This module does something similar to what you want to do: <a href="https://github.com/SlicerProstate/mpReview/blob/master/mpReviewPreprocessor.py">https://github.com/SlicerProstate/mpReview/blob/master/mpReviewPreprocessor.py</a>. Readme file here is all the documentation that we have, unfortunately: <a href="https://github.com/SlicerProstate/mpReview">https://github.com/SlicerProstate/mpReview</a>.</p>

---

## Post #5 by @cpinter (2018-01-18 01:31 UTC)

<p>Have you seen my answer above? It is I think exactly what you need.</p>

---

## Post #6 by @Davide_Punzo (2018-01-19 16:28 UTC)

<p>Hi all,</p>
<p>I have a related question :</p>
<p>it is not possible to run Slicer in batch mode (on a cluster) to make video of the volume rendering using the module Screen Capture, isn’t it? I guess for the rendering is needed to load the GUI to init the 3DView, isn’t it?</p>
<p>Moreover, (by running with only the option --python-script) Do I need to install  VirtualGL and turbovnc?</p>
<p>(additional reference <a href="http://slicer-devel-archive.65872.n3.nabble.com/Slicer-batch-mode-td4033551.html" rel="nofollow noopener">http://slicer-devel-archive.65872.n3.nabble.com/Slicer-batch-mode-td4033551.html</a>)</p>

---

## Post #7 by @lassoan (2018-01-19 16:59 UTC)

<p>Screen Capture module requires Slicer application GUI. The GUI may not need to be visible, but at least windows need to be created.</p>

---

## Post #8 by @jcfr (2018-01-19 21:24 UTC)

<aside class="quote no-group" data-username="Davide_Punzo" data-post="6" data-topic="1863">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_punzo/48/66104_2.png" class="avatar"> Davide_Punzo:</div>
<blockquote>
<p>Slicer in batch mode (on a cluster)</p>
</blockquote>
</aside>
<p>Images built off <a href="https://github.com/thewtex/docker-opengl/" class="inline-onebox">GitHub - thewtex/docker-opengl: A docker image that supports rendering graphical applications.</a> should be helpful. This what we is (will be) used for running Slicer tests on CircleCI</p>

---
