# ABL Temporal Bone Segmentation Module

**Topic ID**: 16494
**Date**: 2021-03-12
**URL**: https://discourse.slicer.org/t/abl-temporal-bone-segmentation-module/16494

---

## Post #1 by @DAT_Minh (2021-03-12 14:37 UTC)

<p>Dear Andras <a class="mention" href="/u/lassoan">@lassoan</a> .<br>
I posted this topic 1 month ago. I’m segmenting temporal bone using ABL Temporal Bone Segmentation. I stuck at step 2: Rigid registration because the my data and atlas is too far off (Too many samples map outside moving image buffer: 188 / 1117). I’ve installed SlicerElastix, Slicer version 4.11.20200930.<br>
Can you make a detailed YouTube video on how to automatically segment temporal bone? This is really important to me. I very appreciate your help. Thank you.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba38fdd57c2d745680abf78370781d94dd775175.png" data-download-href="/uploads/short-url/qzoUCLS55DKz85yi9QQYNB88l13.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba38fdd57c2d745680abf78370781d94dd775175.png" alt="image" data-base62-sha1="qzoUCLS55DKz85yi9QQYNB88l13" width="499" height="500" data-dominant-color="F3F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">597×598 17.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @DAT_Minh (2021-06-10 02:34 UTC)

<p>Dear <a class="mention" href="/u/lassoan">@lassoan</a><br>
I’ve completed rigid registration. For the next step, can you show me the address or link of ABL inference or Docker host? I can’t find it. There are some lines of ABL inference code on Github but I don’t know how to use.<br>
I appreciate your help very much. Thank you.<br>
Best regards.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca4231187abe53b55f616650b242ad1f39e909bf.png" alt="04a_inferenceremote" data-base62-sha1="sRggnPI0GWZLCL82IFxRcp3kdHN" width="576" height="257"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef87521ef0a523aa52e8cce338d3f1dee2a72000.png" alt="20210610_060938" data-base62-sha1="yaY2psu9eZbTgjlOKX9mWAYDJIs" width="597" height="253"></p>

---

## Post #3 by @lassoan (2021-06-10 23:42 UTC)

<p>I don’t know much about this extension. I would recommend to submit an issue to their repository (and copy the issue number here for reference).</p>

---

## Post #4 by @Johann (2021-06-14 13:24 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/dat_minh">@DAT_Minh</a>.<br>
I run inference and the process stopped at 30%. Here’s the message log:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d708d9a4cfd4f9bd497190f35c76c789450bb01b.png" data-download-href="/uploads/short-url/uGhChRBFAOiqwRlOcZt0oDQV4uL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d708d9a4cfd4f9bd497190f35c76c789450bb01b_2_690x227.png" alt="image" data-base62-sha1="uGhChRBFAOiqwRlOcZt0oDQV4uL" width="690" height="227" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d708d9a4cfd4f9bd497190f35c76c789450bb01b_2_690x227.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d708d9a4cfd4f9bd497190f35c76c789450bb01b_2_1035x340.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d708d9a4cfd4f9bd497190f35c76c789450bb01b.png 2x" data-dominant-color="EAEEF3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1368×451 30.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Does it contain issue number? Can you debug the code from docker?</p>

---

## Post #5 by @lassoan (2021-06-17 03:58 UTC)

<p>Have you set up the required server as described <a href="https://github.com/Auditory-Biophysics-Lab/Slicer-ABLTemporalBoneSegmentation#dependencies">here</a> in the extension’s documentation?</p>

---

## Post #6 by @DAT_Minh (2021-06-20 04:55 UTC)

<p>I don’t know how to set up the server. Can you make a video? Thank you <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #7 by @lassoan (2021-06-20 11:18 UTC)

<p>Setup instructions are available at the link in my previous post. I have never set up the server myself, so I cannot give any more specific information.</p>

---

## Post #8 by @DAT_Minh (2021-06-20 23:57 UTC)

<p>Thank you. I followed the instruction but don’t know how to do</p>

---

## Post #9 by @lassoan (2021-06-21 00:36 UTC)

<p>I would recommend to submit this question as an issue to the extension’s repository. Describe what steps you performed and at what point you got stuck (what you did, what you expected to happen, and what happened instead). Post here a link to the submitted issue so that people who will run into the same issue in the future can find how the problem got resolved.</p>

---

## Post #10 by @FUFU (2022-09-13 09:06 UTC)

<p>hello I also met the trouble .Can you tell me how to solve it ? thank you.Error:<br>
My problem is<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56d2bd23ee6c091804d1b8b4348f60ef13422e7c.png" alt="1663059954099" data-base62-sha1="co4zeCdHbPMm3sVLZewO8784Th2" width="540" height="302"><br>
Command ‘elastix’ returned non-zero exit status 1.</p>

---

## Post #12 by @Young_Wang (2022-12-01 00:34 UTC)

<p>hi <a class="mention" href="/u/johann">@Johann</a>, i wonder if you have figured it out how to use this extension?</p>

---

## Post #13 by @evan (2022-12-10 00:00 UTC)

<p>Reference to the GitHub Issue used to track the issue that <a class="mention" href="/u/dat_minh">@DAT_Minh</a> mentioned:</p><aside class="onebox githubissue" data-onebox-src="https://github.com/Auditory-Biophysics-Lab/Slicer-ABLTemporalBoneSegmentation/issues/8">
  <header class="source">

      <a href="https://github.com/Auditory-Biophysics-Lab/Slicer-ABLTemporalBoneSegmentation/issues/8" target="_blank" rel="noopener nofollow ugc">github.com/Auditory-Biophysics-Lab/Slicer-ABLTemporalBoneSegmentation</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Auditory-Biophysics-Lab/Slicer-ABLTemporalBoneSegmentation/issues/8" target="_blank" rel="noopener nofollow ugc">Elastix compatibility "Too many samples map outside moving image buffer"</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-11-30" data-time="18:47:14" data-timezone="UTC">06:47PM - 30 Nov 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/young-oct" target="_blank" rel="noopener nofollow ugc">
          <img alt="young-oct" src="https://avatars.githubusercontent.com/u/61168470?v=4" class="onebox-avatar-inline" width="20" height="20">
          young-oct
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">I was excited when I found out about this module, and thank you for all your wor<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">k. Currently I'm stuck at step 2 and I got the error message saying: 
"command elsatix return to non-zero exit status 1 error."

&lt;img width="1503" alt="Screenshot 2022-11-30 at 14 18 11" src="https://user-images.githubusercontent.com/61168470/204880516-399145d8-ca63-4acb-aed8-c750e1a850d9.png"&gt;

Any help is greatly appreciated. 
@ben-connors @jamesobutler @e-simpson</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #14 by @DR.DHARAM_SINGH_RATH (2023-05-22 06:39 UTC)

<p>Can anyone help? Even after hardening doing everything not able to segment can anyone solve this issue create a video to solve this issue let me inform I am it is very useful extension only we are not able to go beyond 7 per cent after rigid registration step2</p>
<p>itk::ExceptionObject (0x7fdbb6707300)</p>
<p>Location: “ElastixTemplate - Run()”</p>
<p>File: /Volumes/D/S/S-0-E-b/SlicerElastix-build/elastix/Common/CostFunctions/itkAdvancedImageToImageMetric.hxx</p>
<p>Line: 916</p>
<p>Description: ITK ERROR: AdvancedMattesMutualInformationMetric(0x7fdbb701aa00): Too many samples map outside moving image buffer: 48 / 1117</p>
<p>Error occurred during actual registration.</p>
<p>Errors occurred!</p>
<p>Error: Command ‘elastix’ returned non-zero exit status 1.</p>

---
