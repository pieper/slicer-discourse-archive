# TotalSegmentator heartchambers high res not working

**Topic ID**: 37524
**Date**: 2024-07-23
**URL**: https://discourse.slicer.org/t/totalsegmentator-heartchambers-high-res-not-working/37524

---

## Post #1 by @Ione_Ianniruberto (2024-07-23 16:33 UTC)

<p>Hi,<br>
I have CT images and I would like to segment all the heart chambers using the heartchambers highres tool. However it works fine for some images while for others there are two possible outomes: it dosen’t recognize the left vetricle or the nii.gz file is genereted but is empty. How can I solve this problem? Is this releted to the image quality?<br>
Thanks<br>
Ione</p>

---

## Post #2 by @lassoan (2024-07-23 16:33 UTC)

<p>Which Slicer extension are you using for this?</p>

---

## Post #3 by @jamesobutler (2024-07-23 16:56 UTC)

<p>If using TotalSegmentator, I would suggest following up on this existing issue:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/wasserth/TotalSegmentator/issues/334">
  <header class="source">

      <a href="https://github.com/wasserth/TotalSegmentator/issues/334" target="_blank" rel="noopener nofollow ugc">github.com/wasserth/TotalSegmentator</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/wasserth/TotalSegmentator/issues/334" target="_blank" rel="noopener nofollow ugc">Poor cardiac segmentations, including highres</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-07-15" data-time="20:52:36" data-timezone="UTC">08:52PM - 15 Jul 24 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/yakovdan" target="_blank" rel="noopener nofollow ugc">
          <img alt="yakovdan" src="https://avatars.githubusercontent.com/u/2789897?v=4" class="onebox-avatar-inline" width="20" height="20">
          yakovdan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Hello, 
I'm using the latest TotalSegmentator to segment the heart in CT scans.<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> Visually inspecting the output I can see that the output is very roughly correct but large parts of the heart remain unlabeled. I suspect there's an issue with my preprocessing. 

My CT  scans are composed of 512x512 slices with a pixel spacing of about 0.7mm and a slice thickness of 1.25mm. Axially, the scans are variable but include the chest and upper abdomen. Since TotalSegmentator expects 1.5mm slices, I've accounted for that by resampling. I've examined small dataset, a subset of TotalSegmentator's train dataset, and noticed that the slices are 255x255. I've also noticed that the orientation in the training dataset for Total Segmentator is such that the positive axial direction is from feet to head. I couldn't find any information on pixel spacing and any information at all regarding the heart_highres dataset, neither on github nor in the paper.

Can you please specify in detail the input format parameters that TotalSegmentator expects, both for the "total" task and for "heart_highres"?  I mean input dimensions in all axes, pixel spacings, slices thickness, orientations, etc. 

Thank you</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @lassoan (2024-07-23 17:53 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> Thank you for the additional information.</p>
<p><a class="mention" href="/u/ione_ianniruberto">@Ione_Ianniruberto</a> I would recommend to check open issues in <a href="https://github.com/wasserth/TotalSegmentator/issues">TotalSegmentator’s issue tracker</a>. If others have already described similar behavior then add your comments there. If all other existing open issues are unrelated then you can create a new issue. Please post the link to the existing or newly created issue here (so that people who have similar questions can follow the discussion over there).</p>

---
