# radiomics problem

**Topic ID**: 34809
**Date**: 2024-03-10
**URL**: https://discourse.slicer.org/t/radiomics-problem/34809

---

## Post #1 by @mhs (2024-03-10 13:52 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/813d1750ec1e2ca07bb13dbba04434884ecb6850.jpeg" data-download-href="/uploads/short-url/iritNT2DNKNxI8i5GVvHwdpnBRK.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/813d1750ec1e2ca07bb13dbba04434884ecb6850_2_690x423.jpeg" alt="image" data-base62-sha1="iritNT2DNKNxI8i5GVvHwdpnBRK" width="690" height="423" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/813d1750ec1e2ca07bb13dbba04434884ecb6850_2_690x423.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/813d1750ec1e2ca07bb13dbba04434884ecb6850_2_1035x634.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/813d1750ec1e2ca07bb13dbba04434884ecb6850.jpeg 2x" data-dominant-color="67666B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1074×659 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>why i use radiomics to image feature extraction but no data</p>

---

## Post #2 by @pieper (2024-03-10 16:37 UTC)

<p>You should check the error log.  It’s possible you need to update to the latest.  You might be seeing this issue:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/AIM-Harvard/SlicerRadiomics/issues/80#issuecomment-1880191661">
  <header class="source">

      <a href="https://github.com/AIM-Harvard/SlicerRadiomics/issues/80#issuecomment-1880191661" target="_blank" rel="noopener">github.com/AIM-Harvard/SlicerRadiomics</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/AIM-Harvard/SlicerRadiomics/issues/80#issuecomment-1880191661" target="_blank" rel="noopener">Error extracting features</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-12-03" data-time="16:52:05" data-timezone="UTC">04:52PM - 03 Dec 23 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2024-01-09" data-time="04:12:26" data-timezone="UTC">04:12AM - 09 Jan 24 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/DanXieJY" target="_blank" rel="noopener">
          <img alt="DanXieJY" src="https://avatars.githubusercontent.com/u/113625444?v=4" class="onebox-avatar-inline" width="20" height="20">
          DanXieJY
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Hi, I've been trying to use the newly updated SlicerRadiomics package to extract<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> radiomics features, but the error below prompted every time I clicked apply. There were only table titles in the tables. At first I thought it was due to the setting of my machine. But after I tried 3 different machines, including win and linux, the same thing happened. I've tried Slicer 5.3-5.6, and even manually changed the py files but nothing worked. Hope someone could help me fix this problem. Thanks!!

[2023-12-04 00:42:47] I: radiomics.script: Processing input...
[2023-12-04 00:42:47] E: radiomics.script: Error extracting features!
Traceback (most recent call last):
  File "/home/ubuntu/Slicer-5.6.0-linux-amd64/slicer.org/Extensions-32390/SlicerRadiomics/lib/python3.9/site-packages/radiomics/scripts/__init__.py", line 135, in run
    results = self._processCases(caseGenerator)
  File "/home/ubuntu/Slicer-5.6.0-linux-amd64/slicer.org/Extensions-32390/SlicerRadiomics/lib/python3.9/site-packages/radiomics/scripts/__init__.py", line 233, in _processCases
    setting_overrides = self._parseOverrides()
  File "/home/ubuntu/Slicer-5.6.0-linux-amd64/slicer.org/Extensions-32390/SlicerRadiomics/lib/python3.9/site-packages/radiomics/scripts/__init__.py", line 353, in _parseOverrides
    settingsSchema = yaml.safe_load(schema)['mapping']['setting']['mapping']
  File "/home/ubuntu/Slicer-5.6.0-linux-amd64/slicer.org/Extensions-32390/SlicerRadiomics/lib/python3.9/site-packages/ruamel/yaml/main.py", line 1105, in safe_load
    error_deprecation('safe_load', 'load', arg="typ='safe', pure=True")
  File "/home/ubuntu/Slicer-5.6.0-linux-amd64/slicer.org/Extensions-32390/SlicerRadiomics/lib/python3.9/site-packages/ruamel/yaml/main.py", line 1037, in error_deprecation
    raise AttributeError(s)
AttributeError: 
"safe_load()" has been removed, use

  yaml = YAML(typ='safe', pure=True)
  yaml.load(...)

instead of file "/home/ubuntu/Slicer-5.6.0-linux-amd64/slicer.org/Extensions-32390/SlicerRadiomics/lib/python3.9/site-packages/radiomics/scripts/__init__.py", line 353

settingsSchema = yaml.safe_load(schema)['mapping']['setting']['mapping']</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @mhs (2024-03-11 03:16 UTC)

<p>how do i update to the latest version</p>

---

## Post #4 by @pieper (2024-03-11 11:56 UTC)

<p>You can get the latest preview release as described here:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html</a></p>

---
