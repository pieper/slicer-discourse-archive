# DICOM database re-indexing between preview and 4.10.2

**Topic ID**: 7592
**Date**: 2019-07-15
**URL**: https://discourse.slicer.org/t/dicom-database-re-indexing-between-preview-and-4-10-2/7592

---

## Post #1 by @fedorov (2019-07-15 14:57 UTC)

<p>I noticed that DICOM database gets re-indexed on the first launch of DICOM browser. I understand why this might be needed every time preview is launched, but if this re-index happens both in 4.10 and in preview every time I switch between the versions (even if I don’t touch the database). It takes several minutes for a small database with ~10 subjects and &lt;10 series per subject. Is this the expected behavior or a bug?</p>

---

## Post #2 by @lassoan (2019-07-15 15:21 UTC)

<p>This is expected but I agree that the wait can be quite inconvenient when you switch between stable and preview builds frequently.</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a> What do you think about saving database folder to the version-specific <code>Slicer-NNN.ini</code> when the user chooses to create a new database (and when determining the database folder, first DatabaseDirectory key would be first searched in <code>Slicer-NNN.ini</code> and if not found then in <code>Slicer.ini</code>)? This would allow using different databases for different Slicer versions.</p>

---

## Post #3 by @cpinter (2019-07-15 15:37 UTC)

<p>Yes this is an inconvenience for sure. This makes me not want to use the stable, just to avoid the DB update.</p>
<p>I think what <a class="mention" href="/u/lassoan">@lassoan</a> suggests would be an acceptable solution. I will touch this part of the code soon (to make sure no dialog pops up when running automatic tests), and then I will do this too if this is OK.</p>

---

## Post #4 by @lassoan (2019-07-16 12:21 UTC)

<p>Sounds great, thanks in advance.</p>

---

## Post #5 by @fedorov (2019-07-16 12:31 UTC)

<p>Yes, this would be great. I actually didn’t realize it is not possible to have separate databases until I tried that as a workaround.</p>
<p>Would it make sense to even prompt the user to make a copy of the database at the time it is converted?</p>

---

## Post #6 by @cpinter (2019-07-16 13:46 UTC)

<p>I think it would. However, these features will only be actually useful in the next 4 months, until RSNA and 5.0. After that, I hope that we won’t have to change the database for several years again.</p>

---

## Post #7 by @fedorov (2019-07-16 14:09 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="6" data-topic="7592">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>these features will only be actually useful in the next 4 months, until RSNA and 5.0</p>
</blockquote>
</aside>
<p>It would be nice, but I am not that optimistic. It takes time for the extensions to get updated, for the users to develop confidence in new release. There are extensions that have not been updated for ITK5. Speaking for the extensions I’ve been contributing to, we are still far from fixing all those that were broken by the switch to python 3. Since coverage of python code in extensions is quite limited (at least for our extensions), many of those issues go unnoticed, and dashboard can be deceptive, until someone tries to use the module. And some of those python3 changes can be very tricky (at least to me). One example is here: <a href="https://github.com/QIICR/QuantitativeReporting/issues/240" class="inline-onebox">segmentation export broken in 4.10.2 · Issue #240 · QIICR/QuantitativeReporting · GitHub</a>. Realistically, we should anticipate users to turn to previous stable release for the functionality they are not able to find, for whatever reason, in the latest release.</p>

---

## Post #8 by @lassoan (2019-07-16 14:20 UTC)

<p>I don’t think any developer would have the capacity support anything more than the latest stable and latest preview versions. We would want users to use the latest stable and report any errors that they find, instead of letting them to use old releases.</p>
<p>The current DICOM database schema is very good first step, but I expect many significant improvements in the DICOM browser in the coming years and some of them will require schema update (thumbnail support, custom comments, storage of any nodes in the database, etc.).</p>

---

## Post #9 by @fedorov (2019-07-16 14:25 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="7592">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I don’t think any developer would have the capacity support anything more than the latest stable and latest preview versions. We would want users to use the latest stable and report any errors that they find, instead of letting them to use old releases.</p>
</blockquote>
</aside>
<p>Yes, but, realistically, it does happen that developers that contributed functionality for a specific release no longer have resources to maintain or upgrade it for the subsequent release. Especially when those upgrades are non-trivial. You won’t have to try hard to find examples. Unfortunately, it is often challenging to secure resources for maintaining existing functionality - much easier to get money to develop “new” and “innovative” stuff …</p>
<p>Allowing users to have separate databases for different releases seems like a reasonable compromise. From personal experience, I know users often have multiple versions of Slicer installed to be able to use tools they like.</p>
<p>Just sharing my experience. You guys are the ones who do the work, so it’s your call what is appropriate to implement, given the resources you have available.</p>

---

## Post #10 by @cpinter (2019-07-16 14:46 UTC)

<p>Back to the separate databases.</p>
<p>How would we prompt the user to save the existing database? What makes most sense to me right now is that there would be a directory selection window right after clicking “Update database”, and if a sensible (non-empty, not the same as the existing folder) is made, then copy the database there before updating.</p>
<p>After that, it would be up to the user to know that for the previous version they used before they updated the database with a new version, they need to switch to the database copy they just made. I don’t know if we can facilitate this in any way.</p>

---

## Post #11 by @fedorov (2019-07-16 14:48 UTC)

<p>I think this approach is sensible. Along the points made by Andras, there is only that much user can expect from developers to support the use of multiple versions of Slicer.</p>

---

## Post #12 by @cpinter (2019-08-15 16:50 UTC)

<p>Please see the implementation and its explanation in this PR:<br>
<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/commontk/CTK/pull/876" target="_blank" rel="nofollow noopener">github.com/commontk/CTK</a>
  </header>
  <article class="onebox-body">
      <a href="https://github.com/cpinter" target="_blank" rel="nofollow noopener">
    <img alt="cpinter" src="https://avatars0.githubusercontent.com/u/1325980?v=4" class="thumbnail onebox-avatar" width="90" height="90">
  </a>

<h4>
  <a href="https://github.com/commontk/CTK/pull/876" target="_blank" rel="nofollow noopener">ENH: Allow updating DICOM database into different folder; Allow appli…</a>
</h4>

<div class="date">
  by <a href="https://github.com/cpinter" target="_blank" rel="nofollow noopener">cpinter</a>
  on <a href="https://github.com/commontk/CTK/pull/876" target="_blank" rel="nofollow noopener">04:47PM - 15 Aug 19 UTC</a>
</div>

<div class="github-commit-stats">
  <strong>1 commits</strong>
  changed <strong>7 files</strong>
  with <strong>347 additions</strong>
  and <strong>215 deletions</strong>.
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---
