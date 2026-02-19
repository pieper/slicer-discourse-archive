---
topic_id: 26820
title: "Bug Slicer Util Loadvolume Does Not Accept Pathlib Path Only"
date: 2022-12-19
url: https://discourse.slicer.org/t/26820
---

# Bug: slicer.util.loadVolume does not accept pathlib Path (only string)

**Topic ID**: 26820
**Date**: 2022-12-19
**URL**: https://discourse.slicer.org/t/bug-slicer-util-loadvolume-does-not-accept-pathlib-path-only-string/26820

---

## Post #1 by @Alistair_McCutcheon (2022-12-19 09:26 UTC)

<p>My slicer is version 5.2.1</p>
<p>This runs successfully:</p>
<pre><code class="lang-auto">slicer.util.loadVolume(str(pathlib.Path(segmentation_dir_path) / "img_0.nii.gz"))
</code></pre>
<p>With the following message:</p>
<pre><code class="lang-auto">Loaded volume from file: /home/redacted/redacted/redacted/redacted/redacted/redacted/redacted/Public_Patient0/img_0.nii.gz. Dimensions: 200x249x292. Number of components: 1. Pixel type: float.


"Volume" Reader has successfully read the file "/home/redacted/redacted/redacted/redacted/redacted/redacted/redacted/Public_Patient0/img_0.nii.gz" "[0.20s]"
</code></pre>
<p>This crashes:</p>
<pre><code class="lang-auto">slicer.util.loadVolume(pathlib.Path(segmentation_dir_path) / "img_0.nii.gz")
</code></pre>
<p>With the following stacktrace:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/home/redacted/redacted/redacted/Main/Main.py", line 325, in onLoadSegmentationDirectory
    slicer.util.loadVolume(segmentation_dir_path / "img_0.nii.gz")
  File "/opt/Slicer-5.2.1-linux-amd64/bin/Python/slicer/util.py", line 937, in loadVolume
    return loadNodeFromFile(filename, filetype, properties, returnNode)
  File "/opt/Slicer-5.2.1-linux-amd64/bin/Python/slicer/util.py", line 699, in loadNodeFromFile
    raise RuntimeError(errorMessage)
RuntimeError: Failed to load node from file: /home/redacted/redacted/redacted/redacted/redacted/redacted/redacted/Public_Patient0/img_0.nii.gz
Error: Loading  -  load failed.
</code></pre>

---

## Post #2 by @lassoan (2022-12-19 19:16 UTC)

<p>By crash do you mean that the application actually crashed, or just the image was not loaded?</p>
<p><code>pathlib.Path</code> objects are not supported yet in Slicer’s Python API. It would require much more work for Slicer developers to support it than for users to add the <code>str()</code>, so it has not been high on the priority list. I’ve added an issue to keep track of this request:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6741">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6741" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6741" target="_blank" rel="noopener">Make Slicer API compatible with pathlib</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-12-19" data-time="19:13:09" data-timezone="UTC">07:13PM - 19 Dec 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:enhancement
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          good first issue
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Is your feature request related to a problem? Please describe.

Developers <span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">would like to use pathlib.Path directly as input for Slicer API calls where a path-like object is expected.

## Describe the solution you'd like

Allow developers to pass paths as pathlib.Path object.

## Additional context

https://discourse.slicer.org/t/bug-slicer-util-loadvolume-crashes-when-given-a-pathlib-path-instead-of-a-string/26820</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Would you consider contributing to Slicer by adding <code>pathlib.Path</code> support to the methods that you are using, for example for <a href="https://github.com/Slicer/Slicer/blob/main/Base/Python/slicer/util.py#L918">loadVolume</a>?</p>

---

## Post #3 by @Alistair_McCutcheon (2022-12-21 00:24 UTC)

<p>The image was just not loaded (ie, the entire program did NOT crash), sorry for not being clear.</p>
<p>I’ve submitted a pull requested with the change to support pathlib.Path (more generally, it will assume the <strong>str</strong> method of the object will return the path). I’ve done this for both loadNodeFromFile and loadNodesFromFile (loadVolume calls loadNodeFromFile).</p>

---

## Post #4 by @jamesobutler (2022-12-21 02:45 UTC)

<aside class="quote no-group" data-username="Alistair_McCutcheon" data-post="3" data-topic="26820">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alistair_mccutcheon/48/13980_2.png" class="avatar"> Alistair_McCutcheon:</div>
<blockquote>
<p>I’ve submitted a pull requested with the change to support pathlib.Path (more generally, it will assume the <strong>str</strong> method of the object will return the path)</p>
</blockquote>
</aside>
<p>Here is the link to the mentioned pull request:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6743">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6743" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/6743" target="_blank" rel="noopener nofollow ugc">ENH: Allow using pathlib.Path object for paths in slicer.util </a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>AlistairMcCutcheon:loadNodeFromFileUsingAnyClassImplementingStr</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2022-12-21" data-time="00:12:15" data-timezone="UTC">12:12AM - 21 Dec 22 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/AlistairMcCutcheon" target="_blank" rel="noopener nofollow ugc">
            <img alt="AlistairMcCutcheon" src="https://avatars.githubusercontent.com/u/87926838?v=4" class="onebox-avatar-inline" width="20" height="20">
            AlistairMcCutcheon
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 6 additions and 2 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/6743/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+6</span>
            <span class="removed">-2</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Issue: https://github.com/Slicer/Slicer/issues/6741
Topic: https://discourse.sl<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6743" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">icer.org/t/bug-slicer-util-loadvolume-crashes-when-given-a-pathlib-path-instead-of-a-string/26820</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
