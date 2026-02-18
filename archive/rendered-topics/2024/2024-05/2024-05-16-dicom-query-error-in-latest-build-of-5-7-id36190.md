# DICOM query error in latest build of 5.7

**Topic ID**: 36190
**Date**: 2024-05-16
**URL**: https://discourse.slicer.org/t/dicom-query-error-in-latest-build-of-5-7/36190

---

## Post #1 by @pearsonm (2024-05-16 04:16 UTC)

<p>Hello,</p>
<p>When I do a DICOM query using the current testing version, the query is performed but results are not displayed.<br>
Slicer: 5.7.0-2024-05-13 r32855 / 3802d81<br>
Distributor ID: Ubuntu<br>
Description:    Ubuntu 23.10<br>
Release:        23.10<br>
Codename:       mantic</p>
<p>There are multiple copies of the following error</p>
<pre><code class="lang-auto">'DisplayedNumberOfStudies', 'DisplayedFieldsUpdatedTimestamp', 'Connections')VALUES ( NULL, ?, ?, ?, ?, ?, ?, ?, ?, NULL, NULL, NULL, NULL) 
[Qt] Error: 
[Qt] Parameter count mismatch
[Qt] SQL failed: 
[Qt] SELECT Connections FROM Patients WHERE UID= ? 
[Qt] Error: 
[Qt] Parameter count mismatch
[Qt] SQL failed: 
[Qt] UPDATE Patients SET Connections = :connectionsData WHERE UID = :uid 
[Qt] Error: 
[Qt] Parameter count mismatch
[Qt] SQL failed: 
</code></pre>
<p>This error occurs in both a local build and the current build on <a href="http://slicer.org" rel="noopener nofollow ugc">slicer.org</a>.<br>
I tried creating a new DICOM DB and deleting all preferences but the error persisted.</p>
<p>I can still import DICOM files from a local directory and the new files show up in the database so the problem seems to be cfind related.</p>
<p>My previous build from April does not have the error.</p>
<p>Any ideas?</p>
<p>Mark</p>

---

## Post #2 by @pieper (2024-05-16 12:26 UTC)

<p><a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> could you have a look?</p>

---

## Post #3 by @Davide_Punzo (2024-05-16 13:19 UTC)

<p>Thanks for reporting Mark!</p>
<p>I fixed it in <a href="https://github.com/commontk/CTK/pull/1203/commits/4ac8f132bb2fbff0023f898d323b82a97de3192b" class="inline-onebox" rel="noopener nofollow ugc">ENH+BUG for the visual DICOM browser by Punzo · Pull Request #1203 · commontk/CTK · GitHub</a></p>
<p>the issue was that I didn’t updated the schema file which is used only by the old query/retrieve widget (and this widget unfortunately seems to lacks an automated real scenario test).</p>
<p>I am not sure when the PR will be merged. For the moment, you can checkout the PR for your local build. I will give an update as soon as the PR will be merged <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Also please feel free to try the new query/retrieve of the experimental visual DICOM browser (more info at <a href="https://discourse.slicer.org/t/new-feature-visual-dicom-browser/33874" class="inline-onebox">New Feature: visual DICOM browser</a>). Any feedback would be very appreciated.</p>

---

## Post #4 by @Davide_Punzo (2024-05-20 17:36 UTC)

<p>PRs have been merged (thanks <a class="mention" href="/u/lassoan">@lassoan</a>), so in tomorrow Slicer preview you should have the fix <a class="mention" href="/u/pearsonm">@pearsonm</a> <a class="mention" href="/u/pieper">@pieper</a></p>
<p>Reference:</p><aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7751">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7751" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7751" target="_blank" rel="noopener nofollow ugc">BUG: Update CTK to fix Visual DICOM Browser</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>Punzo:visualDICOMBrowserENH</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2024-05-18" data-time="08:12:05" data-timezone="UTC">08:12AM - 18 May 24 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/Punzo" target="_blank" rel="noopener nofollow ugc">
            <img alt="Punzo" src="https://avatars.githubusercontent.com/u/7985338?v=4" class="onebox-avatar-inline" width="20" height="20">
            Punzo
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 1 additions and 1 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7751/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+1</span>
            <span class="removed">-1</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Contains these CTK fixes and improvements:

Revision: acfc526a2a7f646dd9cd27d2<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7751" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">a35625825302ee4a
Author: Davide Punzo &lt;punzodavide@hotmail.it&gt;
Date: Fri May 17 06:07:02 2024 +0200
Message:
BUG: Ensure all studies metadata are queried before filtering

Revision: 4ac8f132bb2fbff0023f898d323b82a97de3192b
Author: Davide Punzo &lt;punzodavide@hotmail.it&gt;
Date: Thu May 16 15:15:12 2024 +0200
Message:
BUG: Update dicom-qr-schema.sql to version 0.8.1

Revision: 9eda3b8baa9d7f9ea109770e5c348f086a735e88
Author: Davide Punzo &lt;punzodavide@hotmail.it&gt;
Date: Wed May 15 19:57:28 2024 +0200
Message:
BUG: Conceal empty patient and study widgets during filtering

Revision: 890e51bfc02f9d9c028300423752af255c85027c
Author: Davide Punzo &lt;punzodavide@hotmail.it&gt;
Date: Tue May 14 15:16:48 2024 +0200
Message:
BUG: Match thumbnail background color to rendered image

Revision: 5767aff7c2a5bdd6c2a288a723f2abdc6c8a9388
Author: Davide Punzo &lt;punzodavide@hotmail.it&gt;
Date: Tue May 14 15:11:12 2024 +0200
Message:
BUG: Remove white box from selected thumbnails

Revision: 831a5415987c07cf46da566f061f0c9bb210537f
Author: Davide Punzo &lt;punzodavide@hotmail.it&gt;
Date: Tue May 14 15:06:22 2024 +0200
Message:
BUG: Adjust thumbnail rendering for OS scaling compatibility

Revision: 5bef417a02120351d617038cd411ce28d86bb70a
Author: Davide Punzo &lt;punzodavide@hotmail.it&gt;
Date: Tue May 14 11:09:59 2024 +0200
Message:
ENH: Autoselect last inserted patient during DICOM import

Revision: ab95f3f2bb89df8bc67786237391bd59ed762b15
Author: Davide Punzo &lt;punzodavide@hotmail.it&gt;
Date: Tue May 7 12:06:50 2024 +0200
Message:
BUG: Standardize DICOM Tags to upper case</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/commontk/CTK/pull/1203">
  <header class="source">

      <a href="https://github.com/commontk/CTK/pull/1203" target="_blank" rel="noopener nofollow ugc">github.com/commontk/CTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/commontk/CTK/pull/1203" target="_blank" rel="noopener nofollow ugc">ENH+BUG for the visual DICOM browser</a>
      </h4>

    <div class="branches">
      <code>commontk:master</code> ← <code>Punzo:visualDICOMBrowserENH</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2024-05-07" data-time="10:07:36" data-timezone="UTC">10:07AM - 07 May 24 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/Punzo" target="_blank" rel="noopener nofollow ugc">
            <img alt="Punzo" src="https://avatars.githubusercontent.com/u/7985338?v=4" class="onebox-avatar-inline" width="20" height="20">
            Punzo
          </a>
        </div>

        <div class="lines" title="8 commits changed 16 files with 418 additions and 138 deletions">
          <a href="https://github.com/commontk/CTK/pull/1203/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+418</span>
            <span class="removed">-138</span>
          </a>
        </div>
      </div>
  </div>
</div>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
