# Registration library not available

**Topic ID**: 41803
**Date**: 2025-02-21
**URL**: https://discourse.slicer.org/t/registration-library-not-available/41803

---

## Post #1 by @cpinter (2025-02-21 10:42 UTC)

<p>Hi all,</p>
<p>I spent quite some time looking for some real test data for deformable registration, without success (I only found a single femur for example, but not even an abdomen or chest that would demonstrate the capabilities of Elastix).</p>
<p>First thing I’d like to bring up is the registration library repository:</p><aside class="onebox githubrepo" data-onebox-src="https://github.com/Slicer/SlicerRegistrationLibrary">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerRegistrationLibrary" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/739e58661b130fa5bb15aeb8182d0dbf/Slicer/SlicerRegistrationLibrary" class="thumbnail">

  <h3><a href="https://github.com/Slicer/SlicerRegistrationLibrary" target="_blank" rel="noopener">GitHub - Slicer/SlicerRegistrationLibrary: Library of registration cases including...</a></h3>

    <p><span class="github-repo-description">Library of registration cases including step-by-step instructions and discussions</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
None of the links are valid (the midas server is down for years), so I think we should delete this repository unless this data is available elsewhere.</p>
<p>Second, if someone knows about some CT-CT or CT-MR test data, please let me know, I’d appreciate it.</p>
<p>Thanks a lot!</p>

---

## Post #2 by @jamesobutler (2025-02-21 14:59 UTC)

<p>You can find the datasets previously on the midas server which were uploaded to <a href="https://github.com/Slicer/slicer.kitware.com-midas3-archive" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Slicer/slicer.kitware.com-midas3-archive: This project is a snapshot of the data historically served from slicer.kitware.com/midas3</a> where you can match the SHA256 information to the dataset in the GitHub Releases area.</p>
<p>This was information was discovered in the below comment detailing the work-in-progress associated with finalizing the SlicerRegistrationLibrary from the old Slicer wiki.</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5830#issuecomment-2612655497">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5830#issuecomment-2612655497" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5830#issuecomment-2612655497" target="_blank" rel="noopener nofollow ugc">Migrate the Registration case library to ReadTheDocs</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-08-27" data-time="19:08:32" data-timezone="UTC">07:08PM - 27 Aug 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Documentation
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          good first issue
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">We would need to migrate the [Registration case library](https://www.slicer.org/<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">wiki/Documentation/Nightly/Registration/RegistrationLibrary) to more modern, sustainable infrastructure, such as Github pages or ReadTheDocs.

- Create github repository under the Slicer organization
- Move all resources (screenshots, scene files, etc.) to a github repository
- Convert all the text to markdown
- Set up page generation using readthedocs or github pages
- Add link to the new registration library from Slicer documentation</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @cpinter (2025-02-21 15:16 UTC)

<p>Ah, very nice, thank you <a class="mention" href="/u/jamesobutler">@jamesobutler</a>, great to know!</p>
<p>What should we do with the SlicerRegistrationLibrary repo though? It is not useful at all in its current state, so maybe replace the links to the archive? Seems like a lot of work.</p>

---

## Post #4 by @muratmaga (2025-02-21 16:34 UTC)

<p>We are soon going to replace the existing SlicerANTs with this antspy based implementation <a href="https://github.com/SlicerMorph/SlicerANTs" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerMorph/SlicerANTs</a></p>
<p>In addition to pairwise, it supports groupwise registration, template building and deformation morphometry (jacobian analysis). UI is a little less overwhelming than the existing extension.</p>
<p>There are still some kinks, but basic registration should be functional.</p>

---

## Post #5 by @jamesobutler (2025-02-21 16:38 UTC)

<p>The SlicerRegistrationLibrary repo is the groundwork for the replacement of registration case page on the Slicer Wiki, but it isn’t complete. Definitely work needed to regenerate the thumbnails with latest Slicer and update the links to their new location hosted through a GitHub Release asset. As you’ve noticed there is no nicely working Registration Case library that is working and it will need a champion to help complete this maintenance effort.</p>

---

## Post #6 by @cpinter (2025-02-25 13:14 UTC)

<p>Thanks for the answers!</p>
<p>Then it may be better not to keep the repository available, because it only generates confusion since none of the links in it work.</p>

---

## Post #7 by @cpinter (2025-02-25 13:15 UTC)

<p>FYI from the midas archive I managed to rescue the deformable registration example that we used for the IGRT tutorial, and uploaded it here:</p><aside class="onebox githubcommit" data-onebox-src="https://github.com/SlicerRt/SlicerRtData/commit/1d07013767307c936c6cc3f4ba5a2e14b4f49f16">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerRtData/commit/1d07013767307c936c6cc3f4ba5a2e14b4f49f16" target="_blank" rel="noopener">github.com/SlicerRt/SlicerRtData</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SlicerRt/SlicerRtData/commit/1d07013767307c936c6cc3f4ba5a2e14b4f49f16" target="_blank" rel="noopener">Add deformable registration example for ENT phantom</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2025-02-25" data-time="13:13:21" data-timezone="UTC">01:13PM - 25 Feb 25 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/cpinter" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/1325980?v=4" class="onebox-avatar-inline" width="20" height="20">
          cpinter
        </a>
      </div>

      <div class="lines" title="changed 2 files with 0 additions and 0 deletions">
        <a href="https://github.com/SlicerRt/SlicerRtData/commit/1d07013767307c936c6cc3f4ba5a2e14b4f49f16" target="_blank" rel="noopener">
          <span class="added">+0</span>
          <span class="removed">-0</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This used to be the data for the IGRT tutorial, but it was stored on the Kitware<span class="show-more-container"><a href="https://github.com/SlicerRt/SlicerRtData/commit/1d07013767307c936c6cc3f4ba5a2e14b4f49f16" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> midas server that has been taken down. The data has been rescued from
https://github.com/Slicer/slicer.kitware.com-midas3-archive/tree/main
(SHAs 219adc1edfa66e3edab379382d698f8f8ea9556cc575ac30ee146ec79c1a4855, 63f3fb263906bce3753e63ecdb9a0cb6f65be3fba6f3a0dffe486d875d18957a, and 80f251dc7300754a2c4b0611e523470dc2e8212e66a869bbdbce51e255cfd63a)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Thanks again!</p>

---
