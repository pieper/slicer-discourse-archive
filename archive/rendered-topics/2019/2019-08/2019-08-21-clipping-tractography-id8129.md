# Clipping Tractography

**Topic ID**: 8129
**Date**: 2019-08-21
**URL**: https://discourse.slicer.org/t/clipping-tractography/8129

---

## Post #1 by @cindy (2019-08-21 21:53 UTC)

<p>Hi all,</p>
<p>I’m looking for help to clip out a certain portion of a tract.</p>
<p>Thus far, I have created a mask at the root entry zone of the trigeminal nerve and used it for tractography seeding. I know have a fiber bundle, however I want to isolate only the portion of the nerve moving anteriorly from the brainstem. I know about the option to use a negative ROI in the tractography display module, but the entire length of all fibres within the ROI are removed - which isn’t what I’m trying to do. I am trying to eliminate any portions of my fiber bundle that is outside a region that I know my nerve should be.</p>
<p>Any help?</p>

---

## Post #2 by @ljod (2019-08-21 22:30 UTC)

<p>One option is to make a “brain mask” covering a large region where the nerve can go, but excluding the anterior region you are not interested in. If you use this as the brain mask in UKF tractography, it will stop any tracts leaving the mask.</p>

---

## Post #3 by @cindy (2019-08-21 23:23 UTC)

<p>Yea - that’s a good idea, but I already generated the tracts so I want a way to clip an existing one. Any ideas?</p>

---

## Post #4 by @ljod (2019-08-22 00:33 UTC)

<p>This module is not yet integrated but does something close to what you want, if you have some computer science or Slicer module installation experience/interest:<br>
<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/SlicerDMRI/SlicerDMRI/pull/116" target="_blank" rel="nofollow noopener">github.com/SlicerDMRI/SlicerDMRI</a>
  </header>
  <article class="onebox-body">
      <a href="https://github.com/luoh15" target="_blank" rel="nofollow noopener">
    <img alt="luoh15" src="https://avatars0.githubusercontent.com/u/37209082?v=4" class="thumbnail onebox-avatar" width="90" height="90">
  </a>

<h4>
  <a href="https://github.com/SlicerDMRI/SlicerDMRI/pull/116" target="_blank" rel="nofollow noopener">Add fiber cutting module</a>
</h4>

<div class="date">
  by <a href="https://github.com/luoh15" target="_blank" rel="nofollow noopener">luoh15</a>
  on <a href="https://github.com/SlicerDMRI/SlicerDMRI/pull/116" target="_blank" rel="nofollow noopener">05:34PM - 21 Sep 18 UTC</a>
</div>

<div class="github-commit-stats">
  <strong>2 commits</strong>
  changed <strong>10 files</strong>
  with <strong>796 additions</strong>
  and <strong>0 deletions</strong>.
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #5 by @neurohuo (2021-10-17 01:25 UTC)

<p>Thanks a lot, I think it is a very useful module.</p>

---
