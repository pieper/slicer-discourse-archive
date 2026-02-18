# Slicer automatic Segmentation Error

**Topic ID**: 320
**Date**: 2017-05-16
**URL**: https://discourse.slicer.org/t/slicer-automatic-segmentation-error/320

---

## Post #1 by @Knobe_Sven (2017-05-16 10:50 UTC)

<p>Dear Slicer-Support,</p>
<p>i have a problem with automatic Segmentation with slicer 4.7.0.<br>
I tried  to segment brainstructures based on MRI-scans with module “EMSegmentation with atlas” and “EMSegmentation without Atlas”. In both cases I got an error:</p>
<p>AttributeError: ctWorkflowwidgetStep has no attribute named ‘_EMSegmentDefineInputChannelsStep_inputChannelList’.</p>
<p>I expected that error because I can’t find the possibility to select an “InputDataSet” in EM Segmenter.</p>
<p>What I’ve done before:</p>
<ol>
<li>
<pre><code>  BiasCorrection MRI-Datasets (N4ITK MRI Bias Correction)
</code></pre>
</li>
<li>
<pre><code>  Registration MRI-Data to atlasData (GENERAL REGISTRATION BRAINS)
</code></pre>
</li>
<li>
<pre><code>  Now: I want to segment automatically Brainstructures based on MRI and atlasData with EMSegmenter with/without atlas.
</code></pre>
</li>
</ol>
<p>I worked step-by-step through the following tutorial</p>
<aside class="onebox pdf">
  <header class="source">
      <a href="https://www.slicer.org/w/images/2/24/AutomaticSegmentation_SoniaPujol.pdf" target="_blank" rel="nofollow noopener">slicer.org</a>
  </header>
  <article class="onebox-body">
    <a href="https://www.slicer.org/w/images/2/24/AutomaticSegmentation_SoniaPujol.pdf" target="_blank" rel="nofollow noopener"><span class="pdf-onebox-logo"></span></a>
<h3><a href="https://www.slicer.org/w/images/2/24/AutomaticSegmentation_SoniaPujol.pdf" target="_blank" rel="nofollow noopener">AutomaticSegmentation_SoniaPujol.pdf</a></h3>

<p class="filesize">12.76 MB</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>and I can’t solve the problem by using other tutorials.</p>
<p>What should I change or try to solve the Problem?<br>
Thank you very much!</p>
<p>Best Regards,<br>
Sven Knobe</p>

---

## Post #2 by @pieper (2017-05-23 17:36 UTC)

<p>Hi -</p>
<p>Unfortunately there are some troubles with the Slicer4 version of EMSegmenter and it’s not clear when they can be addressed.</p>
<p>One option would to use the version in Slicer3, which you can download from here:</p>
<p><a href="https://www.slicer.org/slicer3-downloads/Release/" class="onebox" target="_blank">https://www.slicer.org/slicer3-downloads/Release/</a></p>
<p>Slicer3 is pretty old now, so if you have trouble running them on your system you could make use of the Slicer3 docker image.  It should be able to do what’s in the tutorial.</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">
      <a href="https://github.com/pieper/SlicerDockers/tree/master/slicer3" target="_blank">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars2.githubusercontent.com/u/126077?s=400&amp;v=4" class="thumbnail onebox-avatar" width="400" height="400">

<h3><a href="https://github.com/pieper/SlicerDockers/tree/master/slicer3" target="_blank">pieper/SlicerDockers</a></h3>

<p>docker config files for slicer. Contribute to pieper/SlicerDockers development by creating an account on GitHub.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @919 (2017-07-09 18:10 UTC)

<p>Could someone possibly create a brief tutorial on how to do this with slicer 4.6 or 4.7 with the Multi-modality MRI-based Atlas of the Brain?<br>
<a href="http://www.spl.harvard.edu/publications/item/view/2037" class="onebox" target="_blank" rel="nofollow noopener">http://www.spl.harvard.edu/publications/item/view/2037</a></p>

---
