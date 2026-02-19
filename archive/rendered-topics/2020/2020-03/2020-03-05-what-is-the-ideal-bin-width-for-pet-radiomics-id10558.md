---
topic_id: 10558
title: "What Is The Ideal Bin Width For Pet Radiomics"
date: 2020-03-05
url: https://discourse.slicer.org/t/10558
---

# What is the ideal bin width for PET radiomics?

**Topic ID**: 10558
**Date**: 2020-03-05
**URL**: https://discourse.slicer.org/t/what-is-the-ideal-bin-width-for-pet-radiomics/10558

---

## Post #1 by @Nora (2020-03-05 15:58 UTC)

<p>Hi all,</p>
<p>I’m trying to extract the radiomic features from PET images using Pyradiomics extension on 3DSlicer.<br>
The default settings for the binwidth is 25, however, that’s can’t calculate some features like the GLCMs.</p>
<ul>
<li>
<p>What is the ideal bin width you suggest to made my study comparable to other studies done on slicer?</p>
</li>
<li>
<p>Do I have to do any other step to my dicom files before importing them on slicer for segmentation and feature extractions?</p>
</li>
</ul>
<p>Appreciate your help.</p>
<p>Regards,</p>
<p>Nora</p>

---

## Post #2 by @fedorov (2020-03-05 20:58 UTC)

<blockquote>
<p>What is the ideal bin width you suggest to made my study comparable to other studies done on slicer?</p>
</blockquote>
<p>If you want to use bin width comparable with other studies, I recommend you should look what bin width was used for PET analysis in published studies. Bin width selection will need to be made based on the intensity distribution for your data, perhaps for the distribution within the regions you will be analyzing.</p>
<p>You can collect intensity distribution statistics for a segmented region using the <a href="https://slicer.readthedocs.io/en/latest/user_guide/module_segmentstatistics.html">SegmentStatistics module</a>.</p>
<blockquote>
<p>Do I have to do any other step to my dicom files before importing them on slicer for segmentation and feature extractions?</p>
</blockquote>
<p>You should be able to import your DICOM data into Slicer without any additional steps.</p>

---

## Post #3 by @fedorov (2020-03-05 21:00 UTC)

<p>This article might be helpful to answer your question, I think:</p>
<p>Leijenaar, R. T. H., Nalbantov, G., Carvalho, S., van Elmpt, W. J. C., Troost, E. G. C., Boellaard, R., Aerts, H. J. W. L., Gillies, R. J. &amp; Lambin, P. The effect of SUV discretization in quantitative FDG-PET Radiomics: the need for standardized methodology in tumor texture analysis. <em>Sci. Rep.</em> <strong>5,</strong> 11075 (2015).</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://www.ncbi.nlm.nih.gov/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4525145/" target="_blank">PubMed Central (PMC)</a>
  </header>
  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:132/69;"><img src="https://www.ncbi.nlm.nih.gov/corehtml/pmc/pmcgifs/pmc-logo-share.png" class="thumbnail" width="132" height="69"></div>

<h3><a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4525145/" target="_blank">The effect of SUV discretization in quantitative FDG-PET Radiomics: the need...</a></h3>

<p>FDG-PET-derived textural features describing intra-tumor heterogeneity are increasingly investigated as imaging biomarkers. As part of the process of quantifying heterogeneity, image intensities (SUVs) are typically resampled into a reduced number of...</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @Nora (2020-03-09 14:39 UTC)

<p>Thanks Andrey.<br>
Your answer have helped me to improve my understanding.</p>
<p>Cheers,</p>
<p>Nora</p>

---

## Post #5 by @lrc_09 (2022-05-19 02:41 UTC)

<p>I have read some papers, for PET images, you can set the bin width to 0.4. bin size and bin width are two different parameters.</p>

---
