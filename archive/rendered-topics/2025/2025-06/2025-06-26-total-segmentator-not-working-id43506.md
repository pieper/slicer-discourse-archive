---
topic_id: 43506
title: "Total Segmentator Not Working"
date: 2025-06-26
url: https://discourse.slicer.org/t/43506
---

# Total Segmentator not working

**Topic ID**: 43506
**Date**: 2025-06-26
**URL**: https://discourse.slicer.org/t/total-segmentator-not-working/43506

---

## Post #1 by @manjula (2025-06-26 17:41 UTC)

<p>Hi, Total Segmentator worked just fine in my laptop but suddenly it stopped working</p>
<p>|Processor|13th Gen Intel(R) Core™ i9-13980HX   2.20 GHz|<br>
|Installed RAM|64.0 GB |<br>
NVIDIA RTX 4080 12GB</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "C:\Users\Manjula Herath\AppData\Local\slicer.org\Slicer 5.8.1\bin\Python\slicer\util.py", line 3303, in tryWithErrorDisplay
    yield
  File "C:/Users/Manjula Herath/AppData/Local/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules/TotalSegmentator.py", line 309, in onApplyButton
    self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),
  File "C:/Users/Manjula Herath/AppData/Local/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules/TotalSegmentator.py", line 1054, in process
    self.processVolume(inputFile, inputVolume,
  File "C:/Users/Manjula Herath/AppData/Local/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules/TotalSegmentator.py", line 1119, in processVolume
    self.log(_("Total Segmentator arguments: {options}").format(options))
KeyError: 'options'

</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/649b3581b35f4d133d02d7d516b3c9c12f7887a3.png" data-download-href="/uploads/short-url/em0hpsi3GabAq0ifzwraJ96vcZB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/649b3581b35f4d133d02d7d516b3c9c12f7887a3_2_690x425.png" alt="image" data-base62-sha1="em0hpsi3GabAq0ifzwraJ96vcZB" width="690" height="425" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/649b3581b35f4d133d02d7d516b3c9c12f7887a3_2_690x425.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/649b3581b35f4d133d02d7d516b3c9c12f7887a3_2_1035x637.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/649b3581b35f4d133d02d7d516b3c9c12f7887a3_2_1380x850.png 2x" data-dominant-color="D3D6EA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1404×866 56 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have  Cuda compilation tools, release 12.8, V12.8.61<br>
Build cuda_12.8.r12.8/compiler.35404655_0</p>
<p>I have tried uninstalling and deleting and fresh install and pretty much everything mentioned on the forum.</p>
<p>Thank you</p>

---

## Post #2 by @jamesobutler (2025-06-26 17:56 UTC)

<p>Appears to be a result of some recent changes in the following commit:</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/lassoan/SlicerTotalSegmentator/commit/0b1e90024242d18e36ae274b0685e9c4336b1c0e">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerTotalSegmentator/commit/0b1e90024242d18e36ae274b0685e9c4336b1c0e" target="_blank" rel="noopener nofollow ugc">github.com/lassoan/SlicerTotalSegmentator</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/lassoan/SlicerTotalSegmentator/commit/0b1e90024242d18e36ae274b0685e9c4336b1c0e" target="_blank" rel="noopener nofollow ugc">Mark translatable strings TotalSegmentator 3D Slicer Extension</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2025-06-25" data-time="03:46:47" data-timezone="UTC">03:46AM - 25 Jun 25 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/LuskasHusty" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/63302125?v=4" class="onebox-avatar-inline" width="20" height="20">
          LuskasHusty
        </a>
      </div>

      <div class="lines" title="changed 1 files with 59 additions and 57 deletions">
        <a href="https://github.com/lassoan/SlicerTotalSegmentator/commit/0b1e90024242d18e36ae274b0685e9c4336b1c0e" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+59</span>
          <span class="removed">-57</span>
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

<p>I have asked the developer of the commit to address the issue:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/lassoan/SlicerTotalSegmentator/pull/74#issuecomment-3009320618">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerTotalSegmentator/pull/74#issuecomment-3009320618" target="_blank" rel="noopener nofollow ugc">github.com/lassoan/SlicerTotalSegmentator</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">

    <div class="github-icon-container" title="Comment">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 2.75a.25.25 0 01.25-.25h8.5a.25.25 0 01.25.25v5.5a.25.25 0 01-.25.25h-3.5a.75.75 0 00-.53.22L3.5 11.44V9.25a.75.75 0 00-.75-.75h-1a.25.25 0 01-.25-.25v-5.5zM1.75 1A1.75 1.75 0 000 2.75v5.5C0 9.216.784 10 1.75 10H2v1.543a1.457 1.457 0 002.487 1.03L7.061 10h3.189A1.75 1.75 0 0012 8.25v-5.5A1.75 1.75 0 0010.25 1h-8.5zM14.5 4.75a.25.25 0 00-.25-.25h-.5a.75.75 0 110-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0114.25 12H14v1.543a1.457 1.457 0 01-2.487 1.03L9.22 12.28a.75.75 0 111.06-1.06l2.22 2.22v-2.19a.75.75 0 01.75-.75h1a.25.25 0 00.25-.25v-5.5z"></path></svg>
    </div>



  <div class="github-info-container">

      <h4>
        Comment by
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/15837524?u=77e23f0a30df57a25f193983b30b27790f224a1c&amp;v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a> - <a href="https://github.com/lassoan/SlicerTotalSegmentator/pull/74#issuecomment-3009320618" target="_blank" rel="noopener nofollow ugc">Mark translatable strings TotalSegmentator 3D Slicer Extension</a>
      </h4>



    <div class="branches">
      <code>main</code> ← <code>LuskasHusty:main</code>
    </div>

  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">There appears to be some string formatting issues due to changes in this PR. See<span class="show-more-container"><a href="https://github.com/lassoan/SlicerTotalSegmentator/pull/74" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden"> https://discourse.slicer.org/t/total-segmentator-not-working/43506.

@LuskasHusty Can you take a look and resolve?</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @manjula (2025-06-26 18:01 UTC)

<p>thank you so much James… <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=14" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @DouSam (2025-06-26 20:56 UTC)

<p>Hi everyone, we have committed a fix. Probably in the next nightly build (if you installed using the Extension Manager), the extension will run without errors.</p>

---

## Post #5 by @Carl_Glessgen (2025-06-27 10:09 UTC)

<p>Hello</p>
<p>Hello, where can one download the new version [c2aaf8f] (<a href="https://github.com/lassoan/SlicerTotalSegmentator/commit/c2aaf8fd6322deef35eabeeceef426f5f238337d" class="inline-onebox" rel="noopener nofollow ugc">COMP: Fix recently introduced syntax errors · lassoan/SlicerTotalSegmentator@c2aaf8f · GitHub</a>) mentionned ? The plugin from Slicer’s extension manager is still <a href="https://github.com/lassoan/SlicerTotalSegmentator/commit/2baf4d4f13989a307080cbd0bd582da3e79d44e6" rel="noopener nofollow ugc">2baf4d4</a>.</p>
<p>In short, the problem is still the same for me than the one presented above, with the KeyError ‘options’</p>
<p>Thanks for your help</p>

---

## Post #6 by @Carl_Glessgen (2025-06-27 14:19 UTC)

<p>So in the meatime I’ve made the changes suggested by the latest fix directly in the TotalSegmentator.py file (Contents/Extensions-33241/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules/).</p>
<p>Then I got the following line in the error traceback:<br>
pkg_resources.DistributionNotFound: The ‘pyarrow’ distribution was not found and is required by TotalSegmentator</p>
<p>Solved it by adding the package directly into Slicer’s Python (sudo /Applications/Slicer.app/Contents/bin/PythonSlicer -m pip install pyarrow xvfbwrapper)</p>
<p>Works fine now !</p>

---

## Post #7 by @manjula (2025-06-27 19:39 UTC)

<p>Works out of the box with Slicer 5.9.0 revision 33722 built 2025-06-27 .Thank you <a class="mention" href="/u/dousam">@DouSam</a> and <a class="mention" href="/u/jamesobutler">@jamesobutler</a></p>

---
