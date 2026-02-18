# Tractography measurements

**Topic ID**: 7774
**Date**: 2019-07-26
**URL**: https://discourse.slicer.org/t/tractography-measurements/7774

---

## Post #1 by @amymanson (2019-07-26 16:17 UTC)

<p>Hi, I am currently using the SlicerDMRI extension to measure tract lengths in the brain. Is there any way to obtain length measurements in addition to the mean length?<br>
This is fine, but there is no way that I can see of telling whether most fibres in the selected tract are e.g. short with 1 much longer tract, or if the mean is actually a good average for the fibre lengths.<br>
Thanks,<br>
Amy</p>

---

## Post #2 by @zhangfanmark (2019-07-31 18:33 UTC)

<p>Hi</p>
<p>Measurement of fiber length has not been provided in any SlicerDMRI modules. But, we have a software package whitematteranalysis, which can output fiber length distribution. Here is the link to the package:</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://github.com/SlicerDMRI/whitematteranalysis" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars0.githubusercontent.com/u/15898279?s=400&amp;amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/SlicerDMRI/whitematteranalysis" target="_blank" rel="nofollow noopener">SlicerDMRI/whitematteranalysis</a></h3>

<p>White matter tractography clustering and more... Contribute to SlicerDMRI/whitematteranalysis development by creating an account on GitHub.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>After installation, you can use wm_quality_control_tractography.py to do a QC of the input tractography data. The output includes a pdf file that describes the distribution of fiber length.</p>
<p>Regards,<br>
Fan</p>

---

## Post #3 by @amymanson (2019-09-12 10:16 UTC)

<p>Thanks for your suggestion. I have installed the whitematteranalysis package but am not sure how to run it?<br>
Any help would be much appreciated</p>

---

## Post #4 by @ljod (2019-09-12 14:33 UTC)

<p>There is some information here about running it:<br>
<a href="https://github.com/SlicerDMRI/whitematteranalysis/wiki/2c" rel="nofollow noopener">https://github.com/SlicerDMRI/whitematteranalysis/wiki/2c</a>)-Running-the-Clustering-Pipeline-to-Cluster-a-Single-Subject-from-the-Atlas</p>
<p>I know Fan has updated documentation that needs to be made more prominent online and hopefully he will also chime in here.</p>

---
