---
topic_id: 31253
title: "Quality Dashboard Cdash Is Not Displaying Submission Details"
date: 2023-08-20
url: https://discourse.slicer.org/t/31253
---

# Quality Dashboard (CDash) is not displaying submission details

**Topic ID**: 31253
**Date**: 2023-08-20
**URL**: https://discourse.slicer.org/t/quality-dashboard-cdash-is-not-displaying-submission-details/31253

---

## Post #1 by @jcfr (2023-08-20 20:11 UTC)

<p>As of August 19th, the results reported on our quality dashboard are incomplete.</p>
<p>This has been documented in the following issue report:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Kitware/CDash/issues/1670">
  <header class="source">

      <a href="https://github.com/Kitware/CDash/issues/1670" target="_blank" rel="noopener">github.com/Kitware/CDash</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Kitware/CDash/issues/1670" target="_blank" rel="noopener">slicer.cdash.org: Missing update, configure, build and test results</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-08-20" data-time="19:29:08" data-timezone="UTC">07:29PM - 20 Aug 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          bug report
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container"># Bug report

### Expected vs Actual Behavior

Starting after August 18th, t<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">he update, configure, build and test results are not listed anymore on `slicer.cdash.org`:

| | Expected (2023-08-17) | Actual (2023-08-20) |
|--|--|--|
| URL | https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2023-08-17&amp;filtercount=0&amp;showfilters=1 | https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2023-08-20&amp;filtercount=0&amp;showfilters=1 |
| Screenshot | ![image](https://github.com/Kitware/CDash/assets/219043/7aab6ee9-d8fa-40d3-be1c-b1cc4be0d6cd) | ![image](https://github.com/Kitware/CDash/assets/219043/7884b0eb-38bc-4fb8-8eef-5f31bbdea75e) |
| CTest &amp; CMake version  | 3.22.1 | 3.22.1 |


### CDash Version

As of August 20th, the version of CDash reported is https://github.com/Kitware/CDash/commit/6e68ccc9e

&lt;img width="50%" src="https://github.com/Kitware/CDash/assets/219043/587c8a5e-a572-43e3-83ee-ad9adcddcf4e"/&gt;


### Additional Information

* `slicer.cdash.org` corresponds to `trunk.cdash.org`

&lt;!--
Add additional information here if necessary.  Helpful information includes:
- How to reproduce the problem
- Screenshots of a UI issue
- Browser/OS information (if applicable)
- Any other information which might help us track down the bug
--&gt;</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<div class="md-table">
<table>
<thead>
<tr>
<th></th>
<th>Expected (2023-08-17)</th>
<th>Actual (2023-08-20)</th>
</tr>
</thead>
<tbody>
<tr>
<td>URL</td>
<td><a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2023-08-17&amp;filtercount=0&amp;showfilters=1" class="inline-onebox">CDash</a></td>
<td><a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2023-08-20&amp;filtercount=0&amp;showfilters=1" class="inline-onebox">CDash</a></td>
</tr>
<tr>
<td>Screenshot</td>
<td><img src="https://github.com/Kitware/CDash/assets/219043/7aab6ee9-d8fa-40d3-be1c-b1cc4be0d6cd" alt="image" width="" height=""></td>
<td><img src="https://github.com/Kitware/CDash/assets/219043/7884b0eb-38bc-4fb8-8eef-5f31bbdea75e" alt="image" width="" height=""></td>
</tr>
<tr>
<td>CTest &amp; CMake version</td>
<td>3.22.1</td>
<td>3.22.1</td>
</tr>
</tbody>
</table>
</div>

---

## Post #2 by @jcfr (2023-08-21 13:53 UTC)

<p>Issue has been identified and submissions are now reported as expected.</p>
<p>For more details, see <a href="https://github.com/Kitware/CDash/issues/1670#issuecomment-1686206658" class="inline-onebox">slicer.cdash.org: Missing update, configure, build and test results · Issue #1670 · Kitware/CDash · GitHub</a></p>

---
