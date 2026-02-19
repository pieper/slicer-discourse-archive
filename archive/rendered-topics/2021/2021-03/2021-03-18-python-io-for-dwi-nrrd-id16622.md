---
topic_id: 16622
title: "Python Io For Dwi Nrrd"
date: 2021-03-18
url: https://discourse.slicer.org/t/16622
---

# Python IO for DWI nrrd

**Topic ID**: 16622
**Date**: 2021-03-18
**URL**: https://discourse.slicer.org/t/python-io-for-dwi-nrrd/16622

---

## Post #1 by @styner (2021-03-18 19:13 UTC)

<p>Quick question: Is there a way to use Slicer’s python package outside of Slicer or an alternative way to read DWI NRRD files in python? I am trying to load/save NAMIC style DWI NRRD files in python (pynrrd does not interpret the DWI specific fields)</p>
<p>Any help is much appreciated<br>
Martin</p>

---

## Post #2 by @pieper (2021-03-18 19:21 UTC)

<p>Hi <a class="mention" href="/u/styner">@styner</a> - I don’t know if this is possible for your workflow, but the <code>PythonSlicer</code> executable is a vanilla python that almost all packages can pip install to.  So if you use that as your base you can use any parts of Slicer along with the rest of the python stack.  I tend to do that instead of virtualenvs or other ways of isolating python environments.</p>
<p>If that doesn’t work for you maybe we can think of other ideas.</p>

---

## Post #3 by @styner (2021-03-18 19:45 UTC)

<p>Thanks Steve, That’s certainly one possibility, but it also makes it significantly harder for certain uses. E.g. we do a lot of our deep learning via anaconda. So, I would have to customize Anaconda to PythonSlicer instead of its Python version. Not necessarily the best option also if I would like to later update my anaconda distribution.</p>
<p>When using other DWI formats (such as NIFTI, which is IMO inferior to NRRD when it comes to DWI/DTI), I have the option to use nibabel (e.g. for a multi-shell sparse facile model from the DWI in dipy).  I would like such a solution where I can use nibabel for DWI in NIFTI and another package for Slicer-style DWI in NRRD.</p>
<p>Martin</p>

---

## Post #4 by @pieper (2021-03-18 19:52 UTC)

<p>We have it on our wish list to modularize the slicer libraries into python packages, but there’s a lot of cmake work for that to happen.</p>
<p>Another option for your case would be to use these converters:</p>
<aside class="onebox githubfolder">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/pnlbwh/conversion#introduction" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars.githubusercontent.com/u/3407942?s=400&amp;amp;v=4" class="thumbnail onebox-full-image" width="60" height="60">

<h3><a href="https://github.com/pnlbwh/conversion#introduction" target="_blank" rel="noopener">pnlbwh/conversion - Introduction</a></h3>


  <p><span class="label1">Various mri conversion/modification scripts. Contribute to pnlbwh/conversion development by creating an account on GitHub.</span></p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #5 by @styner (2021-03-18 20:01 UTC)

<p>That converter may indeed solve quite a bit of our problem, as we can read the DWI NRRD data and convert it to a nifti internal data structure (no need to write it to disk) and then use it with any NIFTI based package (such as dipy). And conversely, we can do the same to get the NIFTI into NRRD data structure if needed.</p>
<p>We were thinking about a conversion solution via DWIConvert, but this python based converter would be better as we don’t have to use disk space for the conversion (less space needs and much faster).</p>
<p>Thanks<br>
Martin</p>

---

## Post #6 by @lassoan (2021-03-18 20:02 UTC)

<aside class="quote no-group" data-username="styner" data-post="3" data-topic="16622">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/styner/48/1024_2.png" class="avatar"> styner:</div>
<blockquote>
<p>That’s certainly one possibility, but it also makes it significantly harder for certain uses. E.g. we do a lot of our deep learning via anaconda. So, I would have to customize Anaconda to PythonSlicer instead of its Python version. Not necessarily the best option also if I would like to later update my anaconda distribution.</p>
</blockquote>
</aside>
<p>Is there anything specific in your Anaconda environment that you think you could not pip-install into Slicer’s Python environment?</p>
<p>Another option is to run certain Python functions in Slicer’s Python environment - the same way as you do it when you need to use multiple virtual Python environments for other reasons (e.g., because there are conflicting requirements between various Python package versions).</p>

---
