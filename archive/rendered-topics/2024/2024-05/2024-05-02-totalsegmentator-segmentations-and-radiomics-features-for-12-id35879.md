---
topic_id: 35879
title: "Totalsegmentator Segmentations And Radiomics Features For 12"
date: 2024-05-02
url: https://discourse.slicer.org/t/35879
---

# TotalSegmentator segmentations and radiomics features for 126K+ CT scans

**Topic ID**: 35879
**Date**: 2024-05-02
**URL**: https://discourse.slicer.org/t/totalsegmentator-segmentations-and-radiomics-features-for-126k-ct-scans/35879

---

## Post #1 by @fedorov (2024-05-02 18:08 UTC)

<p>The announcement below is reposted from Imaging Data Commons forum post here: <a href="https://discourse.canceridc.dev/t/new-in-idc-v18-totalsegmentator-segmentations-and-radiomics-features-for-nlst-cts/582" class="inline-onebox">New in IDC v18: TotalSegmentator segmentations and radiomics features for NLST CTs - Announcements - Imaging Data Commons</a></p>
<hr>
<p>IDC data release v18 went live quietly a couple of weeks ago. We have a lot in store to announce, but this time we will do it bit by bit - there are too many exciting updates!</p>
<p>The first highlight of IDC v18 is the availability of <strong>AI-generated segmentations for the National Lung Screening Trial (NLST) collection</strong>! NLST is one the largest collections we have, but until now had very few image annotations.</p>
<p>Harnessing the power of the cloud (we will discuss separately how this was done!), we applied <em>TotalSegmentator</em> to <strong>126,088 CT series from NLST to segment the total of 9,565,554 anatomic structures</strong>. We then utilized <em>pyradiomics</em> to extract first order (e.g., mean and standard deviation of intensity) and shape (e.g., volume and sphericity) features for each of the segmented structures. Both the segmentations and radiomics features are available in IDC for download under CC-BY license.</p>
<p>Manifests for these analysis results (if you want to just download the entire 14 TB of files in bulk) and a bit more details about this content are shared on Zenodo <a href="https://zenodo.org/records/8347012">here</a>.</p>
<p>You can access the segmentations in IDC Portal <a href="https://portal.imaging.datacommons.cancer.gov/explore/filters/?analysis_results_id=TotalSegmentator-CT-Segmentations">here</a>, or access them directly from 3D Slicer using <em>SlicerIDCBrowser</em> extension. The video below demonstrates how to use IDC Portal and Slicer to explore this collection.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="UGEf0ce2A_w" data-video-title="IDC release v18 highlight: TotalSegmentator segmentations and radiomics features for NLST" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=UGEf0ce2A_w" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/UGEf0ce2A_w/maxresdefault.jpg" title="IDC release v18 highlight: TotalSegmentator segmentations and radiomics features for NLST" width="" height="">
  </a>
</div>

<p>More details, demonstrations and usage instructions will be shared soon. We are working on several ideas on how to simplify access to the radiomics features. In the meantime, if you have any questions or wishes about this collection or accompanying documentation, please PM me or reply to this thread!</p>
<p>Subscribe to the forum to stay tuned for updates about this collection and other upcoming highlights about IDC v18! <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"></p>

---
