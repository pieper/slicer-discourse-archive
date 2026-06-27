---
topic_id: 47416
title: "pyradiomics 3.1.1.dev111+g8ed579383, is it safe?"
date: 2026-06-21
url: https://discourse.slicer.org/t/47416
last_bumped: 2026-06-26T13:50:26.564Z
---

# pyradiomics 3.1.1.dev111+g8ed579383, is it safe?

**Topic ID**: 47416
**Date**: 2026-06-21
**URL**: https://discourse.slicer.org/t/pyradiomics-3-1-1-dev111-g8ed579383-is-it-safe/47416

---

## Post #1 by @aujinen (2026-06-21 23:18 UTC)

<p>I downloaded PyRadiomics using <code>git clone https://github.com/AIM-Harvard/pyradiomics</code> and installed it using <code>uv sync</code> according to the contents of “pyproject.toml” with C++ build tools of Microsoft “Build Tools for Visual Studio 2026”.<br>
The displayed PyRadiomics version is<br>
“pyradiomics 3.1.1.dev111+g8ed579383”<br>
Is this safe?<br>
It seems to be working correctly, but there’s no official information on versions above 3.1.0, which is confusing.<br>
With the advancement of AI, malware protection is essential for “uv” and libraries in “PyPI”, so I had set the environment variable “UV_MALWARE_CHECK” to “1” before running uv sync.<br>
Details in following URL (Sorry Japanese)</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://qiita.com/aujinen/items/035674c54ce138aa7a80">
  <header class="source">
      <img src="https://cdn.qiita.com/assets/favicons/public/production-c620d3e403342b1022967ba5e3db1aaa.ico" class="site-icon" alt="" width="120" height="120">

      <a href="https://qiita.com/aujinen/items/035674c54ce138aa7a80" target="_blank" rel="noopener nofollow ugc">Qiita</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/362;"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-user-contents.imgix.net%2Fhttps%253A%252F%252Fcdn.qiita.com%252Fassets%252Fpublic%252Farticle-ogp-background-afbab5eb44e0b055cce1258705637a91.png%3Fixlib%3Drb-4.1.1%26w%3D1200%26blend64%3DaHR0cHM6Ly9xaWl0YS11c2VyLXByb2ZpbGUtaW1hZ2VzLmltZ2l4Lm5ldC9odHRwcyUzQSUyRiUyRmF2YXRhcnMwLmdpdGh1YnVzZXJjb250ZW50LmNvbSUyRnUlMkY1NTkxOTg1MSUzRnYlM0Q0P2l4bGliPXJiLTQuMS4xJmFyPTElM0ExJmZpdD1jcm9wJm1hc2s9ZWxsaXBzZSZiZz1GRkZGRkYmZm09cG5nMzImcz05YjI4ODkzMTIwM2Q1Y2E0NmJmYjQwZTBkNWU3ZjcxMw%26blend-x%3D120%26blend-y%3D467%26blend-w%3D82%26blend-h%3D82%26blend-mode%3Dnormal%26s%3D38038ef2dbbf7901ec7153fb1c46c221?ixlib=rb-4.1.1&amp;w=1200&amp;fm=jpg&amp;mark64=aHR0cHM6Ly9xaWl0YS11c2VyLWNvbnRlbnRzLmltZ2l4Lm5ldC9-dGV4dD9peGxpYj1yYi00LjEuMSZ3PTk2MCZoPTMyNCZ0eHQ9dXYlMjAlRTMlODElQTclMjBQeVJhZGlvbWljcyUyMCVFMyU4MiU5MiVFNyVCMCVBMSVFNCVCRSVCRiVFMyU4MSVBQiVFMyU4MiVBNCVFMyU4MyVCMyVFMyU4MiVCOSVFMyU4MyU4OCVFMyU4MyVCQyVFMyU4MyVBQiVFMyU4MSU5OSVFMyU4MiU4QiZ0eHQtYWxpZ249bGVmdCUyQ3RvcCZ0eHQtY29sb3I9JTIzMUUyMTIxJnR4dC1mb250PUhpcmFnaW5vJTIwU2FucyUyMFc2JnR4dC1zaXplPTU2JnR4dC1wYWQ9MCZzPTkyNDE1N2YwOTIwMzljNDAxZTExY2FhMGFiZTc5NTVi&amp;mark-x=120&amp;mark-y=112&amp;blend64=aHR0cHM6Ly9xaWl0YS11c2VyLWNvbnRlbnRzLmltZ2l4Lm5ldC9-dGV4dD9peGxpYj1yYi00LjEuMSZ3PTgzOCZoPTU4JnR4dD0lNDBhdWppbmVuJnR4dC1jb2xvcj0lMjMxRTIxMjEmdHh0LWZvbnQ9SGlyYWdpbm8lMjBTYW5zJTIwVzYmdHh0LXNpemU9MzYmdHh0LXBhZD0wJnM9MGVkZGVmNjRhNjc3MWZhODkxNTNiNGVjODczNTJjMzE&amp;blend-x=242&amp;blend-y=480&amp;blend-w=838&amp;blend-h=46&amp;blend-fit=crop&amp;blend-crop=left%2Cbottom&amp;blend-mode=normal&amp;s=ab090d30be99fb0f8501c23811970106" class="thumbnail" alt="" width="690" height="362"></div>

<h3><a href="https://qiita.com/aujinen/items/035674c54ce138aa7a80" target="_blank" rel="noopener nofollow ugc">uv で PyRadiomics を簡便にインストールする - Qiita</a></h3>

  <p>Windows11・PowerShellでの手順 【注意】 今回、デフォルトのpythonが3.12の状態でインストールされていたため、自動的に3.12が設定されました。pyproject.toml内には requires-python ="&gt;=3.9" と記述されてお...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @aujinen (2026-06-22 08:07 UTC)

<p>I found “pyradiomics 3.1.1.dev111+g8ed579383” by google search at following URL.</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/AIM-Harvard/pyradiomics/issues/929">
  <header class="source">

      <a href="https://github.com/AIM-Harvard/pyradiomics/issues/929" target="_blank" rel="noopener nofollow ugc">github.com/AIM-Harvard/pyradiomics</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/AIM-Harvard/pyradiomics/issues/929" target="_blank" rel="noopener nofollow ugc">Package install seems to be broken</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2025-07-08" data-time="17:54:43" data-timezone="UTC">05:54PM - 08 Jul 25 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/mvinet99" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/98126900?v=4" class="onebox-avatar-inline" width="20" height="20">
          mvinet99
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Hello,

I have tried installing the Pyradiomics package using pip, conda, and fr<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">om source, and none of the options work for installing. I have tried installing on different python versions and with all previous pyraiodimics package versions and nothing has built correctly. Is anyone else having difficulties with installing? Has anyone else been able to recently install correctly? Thanks in advance for the help.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I’m not sure why the original site didn’t have a clear explanation of version 3.1.1 and how to “uv sync,” but it seems that the official information hasn’t been updated despite the content being changed to 3.1.1, resulting in an incomplete discrepancy. Alternatively, there might be a serious bug lurking in version 3.1.1 itself.</p>
<p>Does anyone have any more detailed information?</p>
<p>Personally, I’m happy that the functionality I need has been confirmed, but I think that if things continue like this, everyone won’t be able to use 3.1.1 with peace of mind.</p>

---

## Post #3 by @aujinen (2026-06-25 02:56 UTC)

<p>The reason I wanted to install a standalone version of PyRadiomics—separate from 3D Slicer—is to create educational content that allows students to experience the actual process of radiomics image analysis calculations step-by-step.</p>
<p>Preliminary testing using Excel has already been conducted (see below).</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/aujinen/Microsoft-Excel-sheets-with-Macro-VB">
  <header class="source">

      <a href="https://github.com/aujinen/Microsoft-Excel-sheets-with-Macro-VB" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/be493226f30119182a3c38ad7df9e4d4/aujinen/Microsoft-Excel-sheets-with-Macro-VB" class="thumbnail">

  <h3><a href="https://github.com/aujinen/Microsoft-Excel-sheets-with-Macro-VB" target="_blank" rel="noopener nofollow ugc">GitHub - aujinen/Microsoft-Excel-sheets-with-Macro-VB: Japanese</a></h3>

    <p><span class="github-repo-description">Japanese</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a href="https://github.com/aujinen/Microsoft-Excel-sheets-with-Macro-VB/blob/master/Convolution-Radiomics-Wavelet.xlsx" title="Convolution-Radiomics-Wavelet.xlsx" rel="noopener nofollow ugc">Convolution-Radiomics-Wavelet.xlsx</a></p>
<p>I have forked the original PyRadiomics repository and named it “PyRadiomics_edu.” Aside from the added <code>workspace</code> folder and a minimal README file, I have left the original content entirely unchanged and plan to add the educational materials within the <code>workspace</code> folder.</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/aujinen/pyradiomics_edu">
  <header class="source">

      <a href="https://github.com/aujinen/pyradiomics_edu" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/a4302641bc5988334a014b93c38a53ff/aujinen/pyradiomics_edu" class="thumbnail">

  <h3><a href="https://github.com/aujinen/pyradiomics_edu" target="_blank" rel="noopener nofollow ugc">GitHub - aujinen/pyradiomics_edu: Educational version forked from Open-source python...</a></h3>

    <p><span class="github-repo-description">Educational version forked from Open-source python package for the extraction of Radiomics features from 2D and 3D images and binary masks. Support: https://discourse.slicer.org/c/community/radiomics</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>When I downloaded the aforementioned forked “PyRadiomics_edu” repository using <code>git clone</code> and installed it following the same procedure with <code>uv sync</code>, the version became:<br>
<code>pyradiomics 0.1.dev1340+g15a938dad</code><br>
<strong>(is not 3.1.0 , 3.1.1)</strong><br>
If anyone knows the reason for this, I would appreciate your guidance.<br>
Additionally, please let me know if this practice is inappropriate, and I will delete the forked repository.</p>

---

## Post #4 by @aujinen (2026-06-26 13:50 UTC)

<p>Found it!<br>
It turned out to be the result of dynamic version management in <code>uv</code>, following the specifications in <code>pyproject.toml</code>.</p>
<p>“How to add dynamic versioning to uv projects”</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://pydevtools.com/handbook/how-to/how-to-add-dynamic-versioning-to-uv-projects/">
  <header class="source">
      <img src="https://pydevtools.com/favicon.ico" class="site-icon" alt="" width="48" height="48">

      <a href="https://pydevtools.com/handbook/how-to/how-to-add-dynamic-versioning-to-uv-projects/" target="_blank" rel="noopener nofollow ugc">pydevtools.com</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/362;"><img src="https://pydevtools.com/images/social/how-to-add-dynamic-versioning-to-uv-projects-social.png" class="thumbnail" alt="" width="690" height="362"></div>

<h3><a href="https://pydevtools.com/handbook/how-to/how-to-add-dynamic-versioning-to-uv-projects/" target="_blank" rel="noopener nofollow ugc">How to add dynamic versioning to uv projects</a></h3>

  <p>Set up Git-based automatic version numbering in uv projects using uv-dynamic-versioning.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
