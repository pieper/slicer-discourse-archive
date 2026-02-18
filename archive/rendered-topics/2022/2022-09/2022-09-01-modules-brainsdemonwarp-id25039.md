# Modules:BRAINSDemonWarp

**Topic ID**: 25039
**Date**: 2022-09-01
**URL**: https://discourse.slicer.org/t/modules-brainsdemonwarp/25039

---

## Post #1 by @Chuan (2022-09-01 09:47 UTC)

<p>Hi,</p>
<p>Does 3d slicer reomove the module of BRAINSDemonWarp in the high version?<br>
I can use V4.10.2 to do the DemonRegistration but I cannot find it in V5.0.3.</p>
<p>Best regards,<br>
Chuan</p>

---

## Post #2 by @jamesobutler (2022-09-01 13:00 UTC)

<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5255">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5255" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5255" target="_blank" rel="noopener nofollow ugc">Demon Registration (BRAINS) and Vector Demon Registration (BRAINS) no longer available in 4.11</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-10-19" data-time="09:35:25" data-timezone="UTC">09:35AM - 19 Oct 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2021-06-23" data-time="04:15:00" data-timezone="UTC">04:15AM - 23 Jun 21 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/keith272" target="_blank" rel="noopener nofollow ugc">
          <img alt="keith272" src="https://avatars.githubusercontent.com/u/73105917?v=4" class="onebox-avatar-inline" width="20" height="20">
          keith272
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Enhancement
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">In Slicer 4.10.2, Demon Registration (BRAINS) and Vector Demon Registration (BRA<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">INS) were available under Registration &gt; Specialized, but have disappeared in Slicer 4.11. I haven't seen any mention of their removal so perhaps it is actually a bug.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<blockquote>
<p>Yes. Those tools were not maintained, and we have no record of anyone using them for many many years.</p>
</blockquote>
<blockquote>
<p>Now ANTS registration is available in Slicer (via SlicerANTS extension), which should be sufficient. Especially since BRAINS, Elastix, Plastimatch, and other registration modules are available, too.</p>
</blockquote>

---

## Post #3 by @Chuan (2022-09-13 12:14 UTC)

<p>Thank you very much!</p>

---

## Post #4 by @Chuan (2024-11-28 07:58 UTC)

<p>Hi James,</p>
<p>Do you know where can I find the python code of Demon Registration used in Slicer3D 4.10? Out of some reasons, I still need to test this module.</p>
<p>Best regards,<br>
Chuan</p>

---

## Post #5 by @jamesobutler (2024-11-28 11:28 UTC)

<p>It is part of the BRAINSTools as specified by reviewing the code as of say the 4.10.2 tag <a href="https://github.com/Slicer/Slicer/blob/v4.10.2" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Slicer/Slicer at v4.10.2</a></p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/17a1edfe600430d25ee025868a11d84063ff6522/SuperBuild.cmake#L267">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/17a1edfe600430d25ee025868a11d84063ff6522/SuperBuild.cmake#L267" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/17a1edfe600430d25ee025868a11d84063ff6522/SuperBuild.cmake#L267" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/17a1edfe600430d25ee025868a11d84063ff6522/SuperBuild.cmake#L267</a></h4>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="257" style="counter-reset: li-counter 256 ;">
          <li>  USE_ICCDEF:BOOL=OFF</li>
          <li>  USE_BRAINSPosteriorToContinuousClass:BOOL=OFF</li>
          <li>  USE_DebugImageViewer:BOOL=OFF</li>
          <li>  BRAINS_DEBUG_IMAGE_WRITE:BOOL=OFF</li>
          <li>  USE_BRAINSTransformConvert:BOOL=ON</li>
          <li>  USE_DWIConvert:BOOL=${Slicer_BUILD_DICOM_SUPPORT} ## Need to figure out library linking</li>
          <li>  USE_BRAINSDemonWarp:BOOL=ON</li>
          <li>  USE_BRAINSRefacer:BOOL=OFF</li>
          <li>  )</li>
          <li>Slicer_Remote_Add(BRAINSTools</li>
          <li class="selected">  GIT_REPOSITORY "${EP_GIT_PROTOCOL}://github.com/Slicer/BRAINSTools.git"</li>
          <li>  GIT_TAG "87da22c2e365da72d3c0dea2634c4efa73dbeab3" # 2017-12-09</li>
          <li>  LICENSE_FILES "http://www.apache.org/licenses/LICENSE-2.0.txt"</li>
          <li>  OPTION_NAME Slicer_BUILD_BRAINSTOOLS</li>
          <li>  OPTION_DEPENDS "Slicer_BUILD_CLI_SUPPORT;Slicer_BUILD_CLI"</li>
          <li>  LABELS REMOTE_MODULE</li>
          <li>  VARS ${BRAINSTools_options}</li>
          <li>  )</li>
          <li>list_conditional_append(Slicer_BUILD_BRAINSTOOLS Slicer_REMOTE_DEPENDENCIES BRAINSTools)</li>
          <li>if(Slicer_BUILD_BRAINSTOOLS)</li>
          <li>  # This is added to SlicerConfig and is useful for extension depending on BRAINSTools</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
which gets you to this branch:</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/Slicer/BRAINSTools/tree/slicer-2017-12-09-v4.7.1-b045970">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Slicer/BRAINSTools/tree/slicer-2017-12-09-v4.7.1-b045970" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/Slicer/BRAINSTools/tree/slicer-2017-12-09-v4.7.1-b045970" target="_blank" rel="noopener nofollow ugc">GitHub - Slicer/BRAINSTools at slicer-2017-12-09-v4.7.1-b045970</a></h3>

  <p><a href="https://github.com/Slicer/BRAINSTools/tree/slicer-2017-12-09-v4.7.1-b045970" target="_blank" rel="noopener nofollow ugc">slicer-2017-12-09-v4.7.1-b045970</a></p>

  <p><span class="label1">WARNING: This is NOT the official upstream BRAINSTools git repository</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>There appears to also have been an interface through SimpleITK.</p>

---

## Post #6 by @Chuan (2024-11-28 14:56 UTC)

<p>Amazing! Thank you James, even though I cannot understand how you find it, It looks like a decryption reasoning. Thank you very much,  I didn’t find it in this whole morning!</p>

---

## Post #7 by @Chuan (2024-11-28 15:08 UTC)

<p>Now I checked it, unfortunately it is not in Python. The reason I would like to check is now I am using the demonregistration in SimpleITK, but the results differ a lot from what I got in Demon Registration in Slicer3D. Seems the algorithm used in Slicer3D is more matured because it has more parameters that can be played with.</p>

---
