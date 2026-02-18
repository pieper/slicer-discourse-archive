# SampleData download is failing on MacOS preview

**Topic ID**: 44123
**Date**: 2025-08-18
**URL**: https://discourse.slicer.org/t/sampledata-download-is-failing-on-macos-preview/44123

---

## Post #1 by @muratmaga (2025-08-18 17:09 UTC)

<p>This has been going on for a while. I am posting here to increase its visibility:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/8541">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/8541" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/8541" target="_blank" rel="noopener">SampleData downloads broken in Mac 5.9 (urllib missing https)</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2025-07-08" data-time="22:40:03" data-timezone="UTC">10:40PM - 08 Jul 25 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/pieper" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

In 5.8.1 using the `downloadFile` method from `SampleData` or `slice<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">r.util` works on Mac, but on 5.9 as of the past few days it has stopped working for https endpoints.

Importantly, it works when running `PythonSlicer` but not in Slicer's python console or in scripted modules.

Seems to work fine on other platforms too.

Note that using the SampleData module to test can be misleading since many developers already have most of the datasets in their caches.  Be sure to delete the files if using SampleData to test. (e.g. `rm /Users/pieper/Library/Caches/slicer.org/Slicer/SlicerIO/MR-head.nrrd`)


## Steps to reproduce

Run these commands:
```
&gt;&gt;&gt; import urllib.request
&gt;&gt;&gt; urllib.request.urlretrieve("https://github.com/muratmaga/E15-Atlas/releases/download/v1/antspy-template.nrrd", "/tmp/a.nrrd")
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "/private/tmp/Slicer.app/Contents/lib/Python/lib/python3.12/urllib/request.py", line 240, in urlretrieve
    with contextlib.closing(urlopen(url, data)) as fp:
                            ^^^^^^^^^^^^^^^^^^
  File "/private/tmp/Slicer.app/Contents/lib/Python/lib/python3.12/urllib/request.py", line 215, in urlopen
    return opener.open(url, data, timeout)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/private/tmp/Slicer.app/Contents/lib/Python/lib/python3.12/urllib/request.py", line 515, in open
    response = self._open(req, data)
               ^^^^^^^^^^^^^^^^^^^^^
  File "/private/tmp/Slicer.app/Contents/lib/Python/lib/python3.12/urllib/request.py", line 537, in _open
    return self._call_chain(self.handle_open, 'unknown',
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/private/tmp/Slicer.app/Contents/lib/Python/lib/python3.12/urllib/request.py", line 492, in _call_chain
    result = func(*args)
             ^^^^^^^^^^^
  File "/private/tmp/Slicer.app/Contents/lib/Python/lib/python3.12/urllib/request.py", line 1420, in unknown_open
    raise URLError('unknown url type: %s' % type)
urllib.error.URLError: &lt;urlopen error unknown url type: https&gt;
&gt;&gt;&gt; 
```


## Environment
- Slicer version: Slicer-5.9-2025--07-07
- Operating system:  Mac + tested on both amd64 and arm64</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<pre><code class="lang-auto">Requesting download CTP-cardio.seq.nrrd from https://github.com/Slicer/SlicerDataStore/releases/download/SHA256/7fbb6ad0aed9c00820d66e143c2f037568025ed63db0a8db05ae7f26affeb1c2 ...
Download failed: 
Download failed (attempt 1 of 3)...
Requesting download CTP-cardio.seq.nrrd from https://github.com/Slicer/SlicerDataStore/releases/download/SHA256/7fbb6ad0aed9c00820d66e143c2f037568025ed63db0a8db05ae7f26affeb1c2 ...
Download failed: 
Download failed (attempt 2 of 3)...
Requesting download CTP-cardio.seq.nrrd from https://github.com/Slicer/SlicerDataStore/releases/download/SHA256/7fbb6ad0aed9c00820d66e143c2f037568025ed63db0a8db05ae7f26affeb1c2 ...
Download failed: 
Download failed (attempt 3 of 3)...
</code></pre>

---
