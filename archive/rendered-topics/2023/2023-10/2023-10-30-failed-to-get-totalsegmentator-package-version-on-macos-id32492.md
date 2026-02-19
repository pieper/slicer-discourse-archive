---
topic_id: 32492
title: "Failed To Get Totalsegmentator Package Version On Macos"
date: 2023-10-30
url: https://discourse.slicer.org/t/32492
---

# Failed to get TotalSegmentator package version on macOS

**Topic ID**: 32492
**Date**: 2023-10-30
**URL**: https://discourse.slicer.org/t/failed-to-get-totalsegmentator-package-version-on-macos/32492

---

## Post #1 by @fedorov (2023-10-30 19:15 UTC)

<p>FYI - on a Mac, when I push the button to get package version information, I am getting this error:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34bb9561891c634a0235273ffafab51f2df58376.png" data-download-href="/uploads/short-url/7wuIUd4dcY1JRLLdnCOB7E7MZhQ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34bb9561891c634a0235273ffafab51f2df58376_2_690x256.png" alt="image" data-base62-sha1="7wuIUd4dcY1JRLLdnCOB7E7MZhQ" width="690" height="256" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34bb9561891c634a0235273ffafab51f2df58376_2_690x256.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34bb9561891c634a0235273ffafab51f2df58376.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34bb9561891c634a0235273ffafab51f2df58376.png 2x" data-dominant-color="444642"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">776×288 55 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Traceback:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/Applications/Slicer 2.app/Contents/bin/Python/slicer/util.py", line 3146, in tryWithErrorDisplay
    yield
  File "/Applications/Slicer 2.app/Contents/Extensions-32251/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py", line 300, in onPackageInfoUpdate
    self.ui.packageInfoTextBrowser.plainText = self.logic.installedTotalSegmentatorPythonPackageInfo().rstrip()
  File "/Applications/Slicer 2.app/Contents/Extensions-32251/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py", line 564, in installedTotalSegmentatorPythonPackageInfo
    versionInfo = subprocess.check_output([shutil.which('PythonSlicer'), "-m", "pip", "show", "TotalSegmentator"]).decode()
  File "/Applications/Slicer 2.app/Contents/lib/Python/lib/python3.9/subprocess.py", line 424, in check_output
    return run(*popenargs, stdout=PIPE, timeout=timeout, check=True,
  File "/Applications/Slicer 2.app/Contents/lib/Python/lib/python3.9/subprocess.py", line 528, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/Applications/Slicer 2.app/Contents/bin/../bin/PythonSlicer', '-m', 'pip', 'show', 'TotalSegmentator']' returned non-zero exit status 1.
</code></pre>

---

## Post #2 by @lassoan (2023-10-30 19:19 UTC)

<p>Have you already installed TotalSegmentator?</p>
<p>What do you see if you start a command terminal and run this?</p>
<pre><code>/Applications/Slicer 2.app/Contents/bin/../bin/PythonSlicer -m pip show TotalSegmentator
</code></pre>

---

## Post #3 by @fedorov (2023-10-30 19:26 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="32492">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Have you already installed TotalSegmentator?</p>
</blockquote>
</aside>
<p>I installed the extension, and didn’t think I need to install something else. I did not realize that TotalSegmentator is not installed until I try to “Apply”. I guess it might be good to disable buttons that are not applicable, but since no one else raised this other than me, it is definitely not a priority.</p>

---

## Post #4 by @lassoan (2023-10-30 19:43 UTC)

<p>Agreed. We should display a more meaningful message. I’ve added an issue to track this:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/lassoan/SlicerTotalSegmentator/issues/44">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerTotalSegmentator/issues/44" target="_blank" rel="noopener">github.com/lassoan/SlicerTotalSegmentator</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/lassoan/SlicerTotalSegmentator/issues/44" target="_blank" rel="noopener">Print more meaningful message if package information is requested before installing TotalSegmentator</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-10-30" data-time="19:42:35" data-timezone="UTC">07:42PM - 30 Oct 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">See details here: https://discourse.slicer.org/t/failed-to-get-totalsegmentator-<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">package-version-on-macos/32492</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @rbumm (2023-10-30 19:48 UTC)

<p>One should either load a volume and press “Apply” (which should install TotalSegmentator if not already there)  or “Force reinstall” (under “Advanced”).</p>

---
