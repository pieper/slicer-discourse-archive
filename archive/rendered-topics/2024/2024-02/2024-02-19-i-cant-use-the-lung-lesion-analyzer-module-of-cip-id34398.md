---
topic_id: 34398
title: "I Cant Use The Lung Lesion Analyzer Module Of Cip"
date: 2024-02-19
url: https://discourse.slicer.org/t/34398
---

# I can't use the lung lesion analyzer module of CIP

**Topic ID**: 34398
**Date**: 2024-02-19
**URL**: https://discourse.slicer.org/t/i-cant-use-the-lung-lesion-analyzer-module-of-cip/34398

---

## Post #1 by @gokcetaniyan (2024-02-19 14:31 UTC)

<p>I want to use the lung lesion analyzer module for lung nodule segmentation and analysis of nodule characteristics. I loaded my lung CT data. Then switched to the lung analyzer module, and put the fiducial on the nodule that I wanted to segment. I ran the algorithm but got no result. The table that has nodule characteristics is empty. How can I use this module? Is there any tutorial for CIP lung lesion analyzer module?</p>

---

## Post #2 by @rbumm (2024-02-19 16:39 UTC)

<p>Regrettably, due to a lack of funding, the lung lesion analyzer has become obsolete and is incompatible with 3D Slicer version 5.6.1.</p>
<p>If you want to use it, please install 3D Slicer 4.8.0 <a href="https://slicer-packages.kitware.com/#collection/5f4474d0e1d8c75dfc70547e/folder/5f4474d0e1d8c75dfc705482" rel="noopener nofollow ugc">from here</a>.<br>
In the 4.8.0 subfolder, you find the Slicer installers and “extensions”.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66995080a9945a8b2f9510d52efb110113bea898.png" alt="image" data-base62-sha1="eDDaXgyfLfPEzClGKq4Iiwdtuju" width="479" height="261"></p>
<p>Download “26489-win-amd64-Chest_Imaging_Platform-git1e850d4-2017-12-07.zip” and unzip it. Then copy the content of “C:\Users\yourname\Dokumente&lt;extension folder&gt;\26489-win-amd64-Chest_Imaging_Platform-git1e850d4-2017-12-07\lib\Slicer-4.8” into:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eeaff822e24bb605c1c701a78216a55edfb46699.png" data-download-href="/uploads/short-url/y3wEkccFkkWoB2mRrdVfQ5cSbix.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eeaff822e24bb605c1c701a78216a55edfb46699.png" alt="image" data-base62-sha1="y3wEkccFkkWoB2mRrdVfQ5cSbix" width="690" height="401" data-dominant-color="F9F9F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">783×456 18.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And start 3D Slicer 4.8.0. With these steps, you will get the lesion analyzer working.</p>

---

## Post #3 by @rbumm (2024-02-19 16:42 UTC)

<p>A tutorial for the lung lesion analyzer is <a href="https://cip.bwh.harvard.edu/files/chestimagingplatform/files/lung_lesion_analyzer.pdf" rel="noopener nofollow ugc">here</a>.</p>

---

## Post #4 by @gokcetaniyan (2024-02-21 12:30 UTC)

<p>Thank you very much! My problem was solved <img src="https://emoji.discourse-cdn.com/twitter/pray/2.png?v=12" title=":pray:t2:" class="emoji" alt=":pray:t2:" loading="lazy" width="20" height="20"></p>

---
