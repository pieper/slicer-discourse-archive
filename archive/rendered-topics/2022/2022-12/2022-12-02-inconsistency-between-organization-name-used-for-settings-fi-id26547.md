# Inconsistency between organization name used for settings files and for macOS bundle identifier

**Topic ID**: 26547
**Date**: 2022-12-02
**URL**: https://discourse.slicer.org/t/inconsistency-between-organization-name-used-for-settings-files-and-for-macos-bundle-identifier/26547

---

## Post #1 by @jcfr (2022-12-02 07:22 UTC)

<p>There are inconsistencies between the organization associated with the <a href="https://slicer.readthedocs.io/en/5.2/user_guide/settings.html#settings-file-location">settings file location</a> and the value set as macOS bundle identifier.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Settings file location</th>
<th>macOS bundle identifier</th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed360beb0c0ea77af0bf6a4c9dd24bc6158ed508.png" data-download-href="/uploads/short-url/xQsXbTqF5tx0Jw7cTsX9WVj3Uhi.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed360beb0c0ea77af0bf6a4c9dd24bc6158ed508_2_690x174.png" alt="image" data-base62-sha1="xQsXbTqF5tx0Jw7cTsX9WVj3Uhi" width="690" height="174" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed360beb0c0ea77af0bf6a4c9dd24bc6158ed508_2_690x174.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed360beb0c0ea77af0bf6a4c9dd24bc6158ed508.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed360beb0c0ea77af0bf6a4c9dd24bc6158ed508.png 2x" data-dominant-color="F9F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">705×178 19.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></td>
<td></td>
</tr>
</tbody>
</table>
</div><p>These correspond to the default values associated with the following variables:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>CMake variable</th>
<th>Default value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Slicer_ORGANIZATION_NAME</code></td>
<td><code>NA-MIC</code><sup class="footnote-ref"><a href="#footnote-86990-1" id="footnote-ref-86990-1">[1]</a></sup></td>
</tr>
<tr>
<td><code>Slicer_ORGANIZATION_DOMAIN</code></td>
<td><code>www.na-mic.org</code> <sup class="footnote-ref"><a href="#footnote-86990-2" id="footnote-ref-86990-2">[2]</a></sup></td>
</tr>
<tr>
<td><code>Slicer_MACOSX_BUNDLE_GUI_IDENTIFIER</code></td>
<td><code>org.slicer.slicer</code><sup class="footnote-ref"><a href="#footnote-86990-3" id="footnote-ref-86990-3">[3]</a></sup></td>
</tr>
</tbody>
</table>
</div><p><strong>Question:</strong> Should we update the value of <code>Slicer_ORGANIZATION_NAME</code> and <code>Slicer_ORGANIZATION_DOMAIN</code> to respectively be <code>Slicer</code> and <code>www.slicer.org</code> (<code>slicer.org</code>) ?</p>
<hr class="footnotes-sep">

<ol class="footnotes-list">
<li id="footnote-86990-1" class="footnote-item"><p><a href="https://github.com/Slicer/Slicer/blob/v5.2.1/CMake/SlicerApplicationOptions.cmake#L67">https://github.com/Slicer/Slicer/blob/v5.2.1/CMake/SlicerApplicationOptions.cmake#L67</a> <a href="#footnote-ref-86990-1" class="footnote-backref">↩︎</a></p>
</li>
<li id="footnote-86990-2" class="footnote-item"><p><a href="https://github.com/Slicer/Slicer/blob/v5.2.1/CMake/SlicerApplicationOptions.cmake#L60">https://github.com/Slicer/Slicer/blob/v5.2.1/CMake/SlicerApplicationOptions.cmake#L60</a> <a href="#footnote-ref-86990-2" class="footnote-backref">↩︎</a></p>
</li>
<li id="footnote-86990-3" class="footnote-item"><p><a href="https://github.com/Slicer/Slicer/blob/v5.2.1/CMake/SlicerApplicationOptions.cmake#L126">https://github.com/Slicer/Slicer/blob/v5.2.1/CMake/SlicerApplicationOptions.cmake#L126</a> <a href="#footnote-ref-86990-3" class="footnote-backref">↩︎</a></p>
</li>
</ol>

---

## Post #2 by @jamesobutler (2022-12-02 12:42 UTC)

<p>Yes, using Slicer as the organization makes sense. I was recently helping a user find the settings file in AppData and they had trouble finding it because it wasn’t immediately obvious that Slicer was under a NA-MIC organization directory.</p>

---

## Post #3 by @lassoan (2022-12-03 05:15 UTC)

<p>I think the only remaining activity of the NA-MIC organization is the Project Week (<a href="https://projectweek.na-mic.org/">https://projectweek.na-mic.org/</a>), but I think even that is only a label that is attached to the group of organizers. So, it would be probably more accurate to say that today Slicer is developed by the Slicer community (<a href="http://www.slicer.org">www.slicer.org</a>) and not the NA-MIC community (<a href="http://www.na-mic.org">www.na-mic.org</a>) and we could reflect that by changing the organization name/domain on all platforms.</p>

---

## Post #4 by @pieper (2022-12-03 15:59 UTC)

<p>Yes, I think that using Slicer consistently would be more logical.  It’s always been weird that the config paths on mac and linux aren’t consistent so clearing that up too would be nice.</p>

---

## Post #5 by @jamesobutler (2022-12-23 17:45 UTC)

<p>To follow up on this:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6750">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6750" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/6750" target="_blank" rel="noopener nofollow ugc">ENH: Change organization name and domain to Slicer from NA-MIC</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>jamesobutler:slicer-organization-name</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2022-12-23" data-time="17:45:20" data-timezone="UTC">05:45PM - 23 Dec 22 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
            <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
            jamesobutler
          </a>
        </div>

        <div class="lines" title="1 commits changed 5 files with 10 additions and 10 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/6750/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+10</span>
            <span class="removed">-10</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">See discussion at https://discourse.slicer.org/t/inconsistency-between-organizat<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6750" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">ion-name-used-for-settings-files-and-for-macos-bundle-identifier/26547</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @jcfr (2023-08-22 14:02 UTC)

<p>For completeness, the organization name and domain were ultimately changed from <code>Slicer</code> to <code>slicer.org</code>.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6879">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6879" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/6879" target="_blank" rel="noopener">Change organization name and domain to slicer.org from Slicer</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>lassoan:change-organization-name</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-03-12" data-time="14:01:37" data-timezone="UTC">02:01PM - 12 Mar 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="2 commits changed 5 files with 10 additions and 10 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/6879/files" target="_blank" rel="noopener">
            <span class="added">+10</span>
            <span class="removed">-10</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Commit https://github.com/Slicer/Slicer/commit/b0b9be57cb7d1a1e462143ec74e3d37d2<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6879" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">71d114d modified the organization name to Slicer from NA-MIC, which caused a name clash with the Slicer executable.

This commit changes the organization name to slicer.org. The final decision on the used organization name has not been made yet, this commit is a quick fix to resolve a blocking issue.

see https://github.com/Slicer/Slicer/issues/6878

We also change the organization domain name from www.slicer.org to slicer.org for consistency.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
