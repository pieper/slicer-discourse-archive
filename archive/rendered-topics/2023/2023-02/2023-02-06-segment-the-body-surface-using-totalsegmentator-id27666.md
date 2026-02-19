---
topic_id: 27666
title: "Segment The Body Surface Using Totalsegmentator"
date: 2023-02-06
url: https://discourse.slicer.org/t/27666
---

# Segment the body surface using TotalSegmentator

**Topic ID**: 27666
**Date**: 2023-02-06
**URL**: https://discourse.slicer.org/t/segment-the-body-surface-using-totalsegmentator/27666

---

## Post #1 by @SoYoung_Lim (2023-02-06 10:20 UTC)

<p>Hi, I love this helpful extension!<br>
I found that subset - body skin(torso) segmentation is now available!<br>
I am wondering if I can use that subset function on 3D Slicer program too. Is there anyone tried segmenting skin on 3D Slicer with total segmentator?<br>
Is it possible to use skin segmentation function after upgrade version of total segmentator?</p>

---

## Post #2 by @rbumm (2023-02-06 10:47 UTC)

<p>Hi, body/skin and pleural/pericardial effusion will probably be integrated into the TotalSegmentator extension very soon. <a class="mention" href="/u/lassoan">@lassoan</a>, just give me a short note if you want me to do this.</p>

---

## Post #3 by @SoYoung_Lim (2023-02-06 10:51 UTC)

<p>Thank you for the reply! I am looking forward to use new additional functions!</p>

---

## Post #4 by @rbumm (2023-02-06 13:19 UTC)

<p>Just see that body/skin and effusions special tasks are already implemented in the TotalSegmentator extension. Please just update the extension via the extension manager.</p>
<p>“Body trunc” segmentation with an A10G GPU and 24 GB video RAM:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/688d2a1060fc642b2730cc64e7f929522b520743.jpeg" data-download-href="/uploads/short-url/eUU6cFLQuAzr5gOGYGA4XQMRSo3.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/688d2a1060fc642b2730cc64e7f929522b520743_2_528x500.jpeg" alt="image" data-base62-sha1="eUU6cFLQuAzr5gOGYGA4XQMRSo3" width="528" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/688d2a1060fc642b2730cc64e7f929522b520743_2_528x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/688d2a1060fc642b2730cc64e7f929522b520743.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/688d2a1060fc642b2730cc64e7f929522b520743.jpeg 2x" data-dominant-color="A2667B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">584×553 89 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @rbumm (2023-02-06 14:51 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I can not yet get skin segmentation working - is there a special trick?</p>

---

## Post #6 by @lassoan (2023-02-06 14:55 UTC)

<p>Which “Segmentation task” does not do what you expect?</p>

---

## Post #7 by @rbumm (2023-02-06 15:48 UTC)

<p><a href="https://github.com/wasserth/TotalSegmentator#subtasks">Subtasks</a> refers to a <code>body: body, body_trunc, body_extremities, skin</code> task  but I only get “body_trunc” and “body_extremities” segmentations when I run our extensions “body” task, not “skin”:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/625de1b3acc171be5abf5342d038104148e022c8.png" alt="image" data-base62-sha1="e2bVOWlc2yQdMhseOfaxK2eyMmA" width="219" height="196"></p>
<p>Effusions work great.</p>

---

## Post #8 by @lassoan (2023-02-06 16:04 UTC)

<p>These are the segmentation tasks made avilable in the Slicer extension:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/lassoan/SlicerTotalSegmentator/blob/d9b4f6e7a2eae05d099836aa8d314a59df066262/TotalSegmentator/TotalSegmentator.py#L308-L314">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/d9b4f6e7a2eae05d099836aa8d314a59df066262/TotalSegmentator/TotalSegmentator.py#L308-L314" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/d9b4f6e7a2eae05d099836aa8d314a59df066262/TotalSegmentator/TotalSegmentator.py#L308-L314" target="_blank" rel="noopener">lassoan/SlicerTotalSegmentator/blob/d9b4f6e7a2eae05d099836aa8d314a59df066262/TotalSegmentator/TotalSegmentator.py#L308-L314</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="308" style="counter-reset: li-counter 307 ;">
          <li>self.tasks['total'] = {'label': 'total', 'supportsFast': True, 'supportsMultiLabel': True}</li>
          <li>self.tasks['lung_vessels'] = {'label': 'lung vessels', 'requiresPreSegmentation': True}</li>
          <li>self.tasks['cerebral_bleed'] = {'label': 'cerebral bleed', 'requiresPreSegmentation': True, 'supportsMultiLabel': True}</li>
          <li>self.tasks['hip_implant'] = {'label': 'hip implant', 'requiresPreSegmentation': True, 'supportsMultiLabel': True}</li>
          <li>self.tasks['coronary_arteries'] = {'label': 'coronary arteries', 'requiresPreSegmentation': True, 'supportsMultiLabel': True}</li>
          <li>self.tasks['body'] = {'label': 'body', 'supportsFast': True}</li>
          <li>self.tasks['pleural_pericard_effusion'] = {'label': 'pleural and pericardial effusion', 'requiresPreSegmentation': True, 'supportsMultiLabel': True}</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>If you find that something does not work in the Slicer extension that it is a good place to discuss here. If there is something wrong/unexpected in the TotalSegmentator Python package then probably the best is to create an issue directly in <a href="https://github.com/wasserth/TotalSegmentator/issues" class="inline-onebox">Issues · wasserth/TotalSegmentator · GitHub</a> (and post the link to the issue here for reference).</p>

---

## Post #9 by @lassoan (2023-02-06 16:21 UTC)

<p>I’ve had a look and it seems that only 2 of the 4 segments produced by the task is listed in the class map of the task. I’ve submitted an issue to TotalSegmentator Python package to clarify:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/wasserth/TotalSegmentator/issues/67">
  <header class="source">

      <a href="https://github.com/wasserth/TotalSegmentator/issues/67" target="_blank" rel="noopener">github.com/wasserth/TotalSegmentator</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/wasserth/TotalSegmentator/issues/67" target="_blank" rel="noopener">Skin and </a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-02-06" data-time="16:20:14" data-timezone="UTC">04:20PM - 06 Feb 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">When using the `body` task then the network computes 4 segments:
- skin.nii.gz
<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">
- body.nii.gz
- body_trunc.nii.gz
- body_extremities.nii.gz

However, in the class map only "body_trunc" and "body_extremities" show up:

https://github.com/wasserth/TotalSegmentator/blob/af44342d7b5a7f6331b33b26434b58882871a68a/totalsegmentator/map_to_binary.py#L311-L313

Is this just a bug or we should get the list of segments a task produces in some other way?</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #10 by @rbumm (2023-02-06 17:43 UTC)

<p>I´ve just tested the latest TotalSegmentator release from the command line and it produces “body.nii.gz” and “skin.nii.gz” into the segmentation folder, but it appears this has already been realized <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/807baed1f99048046348f936c4f405f157d9dd5a.png" alt="image" data-base62-sha1="ikC6xT81oymfpmUQxbca4uQ4Nho" width="240" height="127"></p>

---

## Post #11 by @lassoan (2023-02-06 18:50 UTC)

<p>Yes, we just don’t read the two extra files because they are not listed in the task outputs.</p>
<p>Jakob replied in the github issue telling that the two extra segments are derived by some simple additional image processing operations. So, I think we’ll just keep returning the two original segments in the Slicer extension (and not the derived ones).</p>

---

## Post #12 by @Aayush_Agrawal_ch21b (2024-04-04 08:39 UTC)

<p>How can this skin labelmap be downloaded/ added as one of the segments?</p>

---

## Post #13 by @lassoan (2024-04-04 15:44 UTC)

<p>To get a “skin” (body surface) segment, you can go to TotalSegmentator module, choose <code>Segmentation task</code> → <code>body</code>, and click <code>Apply</code>.</p>

---

## Post #14 by @liam26 (2026-01-15 05:24 UTC)

<p>I’m having the same issue. Were you able to resolve this?</p>

---
