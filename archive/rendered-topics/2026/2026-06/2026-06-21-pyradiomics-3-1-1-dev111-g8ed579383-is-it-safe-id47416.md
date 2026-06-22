---
topic_id: 47416
title: "pyradiomics 3.1.1.dev111+g8ed579383, is it safe?"
date: 2026-06-21
url: https://discourse.slicer.org/t/47416
last_bumped: 2026-06-21T23:18:56.105Z
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
