---
topic_id: 31104
title: "Info Behind Dicom Tag Decay Corrected 0018 9758"
date: 2023-08-11
url: https://discourse.slicer.org/t/31104
---

# Info behind Dicom tag - Decay Corrected(0018,9758)

**Topic ID**: 31104
**Date**: 2023-08-11
**URL**: https://discourse.slicer.org/t/info-behind-dicom-tag-decay-corrected-0018-9758/31104

---

## Post #1 by @appos (2023-08-11 13:28 UTC)

<p>I seem to have a few doubts so please try to answer these individually.</p>
<ol>
<li>
<p>There seems to be a DICOM tag Decay Corrected(0018,9758). The enumerated values are YES and NO. I have a situation in which this values is YES. If I am not wrong, this suggests that the decay correction has already been applied on the total_dose(0018,1074). Then, SUV value then can be calculated by<br>
SUVbwScaleFactor = (weight * 1000 / Total_Dose(0018,1074))<br>
SUVbw = (stored pixel value in Pixel_Data (7FE0,0010) * Rescale_Slope (0028,1053) + Rescale_Intercept (0028,1052)) * SUVbwScaleFactor</p>
</li>
<li>
<p>Lets assume Decay Corrected(0018,9758) is NO. I also have a decay factor tag (0054,1321). Then is this calculation correct<br>
SUVbwScaleFactor = (weight * 1000) / (Total_Dose(0018,1074) * decay_factor (0054,1321))<br>
SUVbw = (stored pixel value in Pixel_Data (7FE0,0010) * Rescale_Slope (0028,1053) + Rescale_Intercept (0028,1052)) * SUVbwScaleFactor</p>
</li>
</ol>
<p>These are links which I have referred</p>
<ul>
<li>List item</li>
</ul>
<p><a href="https://qibawiki.rsna.org/index.php/Standardized_Uptake_Value_(SUV)" class="onebox" target="_blank" rel="noopener nofollow ugc">https://qibawiki.rsna.org/index.php/Standardized_Uptake_Value_(SUV)</a></p>
<ul>
<li>List item</li>
</ul>
<aside class="onebox pdf" data-onebox-src="https://qibawiki.rsna.org/images/6/62/SUV_vendorneutral_pseudocode_happypathonly_20180626_DAC.pdf">
  <header class="source">

      <a href="https://qibawiki.rsna.org/images/6/62/SUV_vendorneutral_pseudocode_happypathonly_20180626_DAC.pdf" target="_blank" rel="noopener nofollow ugc">qibawiki.rsna.org</a>
  </header>

  <article class="onebox-body">
    <a href="https://qibawiki.rsna.org/images/6/62/SUV_vendorneutral_pseudocode_happypathonly_20180626_DAC.pdf" target="_blank" rel="noopener nofollow ugc"><span class="pdf-onebox-logo"></span></a>

<h3><a href="https://qibawiki.rsna.org/images/6/62/SUV_vendorneutral_pseudocode_happypathonly_20180626_DAC.pdf" target="_blank" rel="noopener nofollow ugc">SUV_vendorneutral_pseudocode_happypathonly_20180626_DAC.pdf</a></h3>

  <p class="filesize">18.99 KB</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
