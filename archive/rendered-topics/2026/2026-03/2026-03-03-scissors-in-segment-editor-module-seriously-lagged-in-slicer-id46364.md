---
topic_id: 46364
title: "Scissors In Segment Editor Module Seriously Lagged In Slicer"
date: 2026-03-03
url: https://discourse.slicer.org/t/46364
---

# Scissors in Segment Editor module seriously lagged in Slicer 5.10.0

**Topic ID**: 46364
**Date**: 2026-03-03
**URL**: https://discourse.slicer.org/t/scissors-in-segment-editor-module-seriously-lagged-in-slicer-5-10-0/46364

---

## Post #1 by @VincentYu (2026-03-03 06:52 UTC)

<p>Operating system: Windwos 11;<br>
Slicer version: 5.10.0</p>
<p>Recently I update Slicer from 5.8.1 to 5.10.0, and I found that sometimes the scissors in Segment Editor took very long computing time. After several small experiments, I found if the trajectory of the scissors is “outside“ the segment region and draw the trajectory slowly, this delay will happen. But this problem won’t happen in Slier 5.8.1 in the same condition (same segmentation nrrd, same “outside“ and “slow” trajectory).</p>
<p>Sometimes I want to cut segments carefully so I slow my drawing speed, and the computation may take several minutes to finish just one cutting.</p>
<p>Anyone can reproduce this problem?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f04a46aedfa4338ef5eb057145602bca267dd2ea.jpeg" data-download-href="/uploads/short-url/yhHJbeUVZSKm4HoQszsIST3V4bE.jpeg?dl=1" title="圖片" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f04a46aedfa4338ef5eb057145602bca267dd2ea_2_690x410.jpeg" alt="圖片" data-base62-sha1="yhHJbeUVZSKm4HoQszsIST3V4bE" width="690" height="410" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f04a46aedfa4338ef5eb057145602bca267dd2ea_2_690x410.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f04a46aedfa4338ef5eb057145602bca267dd2ea_2_1035x615.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f04a46aedfa4338ef5eb057145602bca267dd2ea_2_1380x820.jpeg 2x" data-dominant-color="BEC4D7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">圖片</span><span class="informations">1380×820 193 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The segmentation .nrrd is in the link below:</p>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1HE4sBEIIe-277wOZpnW8lgdO3uvbDcG9/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1HE4sBEIIe-277wOZpnW8lgdO3uvbDcG9/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1HE4sBEIIe-277wOZpnW8lgdO3uvbDcG9/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1HE4sBEIIe-277wOZpnW8lgdO3uvbDcG9/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">SEG (MRI nerve).seg.nrrd</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @cpinter (2026-03-03 11:31 UTC)

<p>Thanks for the detailed report!</p>
<p>I loaded the segmentation you shared in 5.8.1 and 5.10, and I was able to reproduce the issue. In 5.10 using the scissors was much slower.</p>
<p>Can you please create an issue on GitHub? The same description and file share will do just great. Thanks a lot!</p>

---

## Post #3 by @VincentYu (2026-03-03 13:02 UTC)

<p>Thank you for your quick reply!</p>
<p>I’ve created an issue on Slicer’s GitHub.</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/9055">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/9055" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/9055" target="_blank" rel="noopener nofollow ugc">Scissors in Segment Editor module seriously lagged in Slicer 5.10.0</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2026-03-03" data-time="12:57:49" data-timezone="UTC">12:57PM - 03 Mar 26 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/gitVincentYu" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/32505480?v=4" class="onebox-avatar-inline" width="20" height="20">
          gitVincentYu
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Operating system: Windwos 11;
Slicer version: 5.10.0

Recently I update Slicer f<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">rom 5.8.1 to 5.10.0, and I found that sometimes the scissors in Segment Editor took very long computing time. After several small experiments, I found if the trajectory of the scissors is “outside“ the segment region and draw the trajectory slowly, this delay will happen. But this problem won’t happen in Slier 5.8.1 in the same condition (same segmentation nrrd, same “outside“ and “slow” trajectory).

Sometimes I want to cut segments carefully so I slow my drawing speed, and the computation may take several minutes to finish just one cutting.

The segmentation .nrrd is in the link below:
https://drive.google.com/file/d/1HE4sBEIIe-277wOZpnW8lgdO3uvbDcG9/view?usp=sharing

This issue was also [posted on 3D Slicer Forum](https://discourse.slicer.org/t/scissors-in-segment-editor-module-seriously-lagged-in-slicer-5-10-0/46364/1).

Thank you!</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
