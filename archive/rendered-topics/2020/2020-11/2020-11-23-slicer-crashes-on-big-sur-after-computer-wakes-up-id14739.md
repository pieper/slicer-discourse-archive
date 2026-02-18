# Slicer crashes on Big Sur after computer wakes up

**Topic ID**: 14739
**Date**: 2020-11-23
**URL**: https://discourse.slicer.org/t/slicer-crashes-on-big-sur-after-computer-wakes-up/14739

---

## Post #1 by @pll_llq (2020-11-23 09:49 UTC)

<p>Hi,</p>
<p>I’m experiencing some strange behaviours with several apps after upgrading my 16 inch MBP to macOS 11.0.1. Slicer is one of them.</p>
<p>When I use an iPad as a second Sidecar display after the computer wakes from sleep Slicer crashes.</p>
<p>If it doesn’t crash - the UI becomes unresponsive and if scaled it looks like this<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b6f734c8492bec3996d995900d3726fa3168f7cb.jpeg" data-download-href="/uploads/short-url/q6Axg0pqXT2uAIxmno1xLaDIC4H.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b6f734c8492bec3996d995900d3726fa3168f7cb_2_690x266.jpeg" alt="image" data-base62-sha1="q6Axg0pqXT2uAIxmno1xLaDIC4H" width="690" height="266" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b6f734c8492bec3996d995900d3726fa3168f7cb_2_690x266.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b6f734c8492bec3996d995900d3726fa3168f7cb_2_1035x399.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b6f734c8492bec3996d995900d3726fa3168f7cb_2_1380x532.jpeg 2x" data-dominant-color="9A9A9A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2806×1084 543 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>When I was debugging a similar issue for Sublime Text disabling gpu buffering helped preventing unresponsive UI.</p>
<p>As far as I tried to debug the issue in slicer I can only replicate the crash if the python interpreter is present in the app layout. I have the system crash log if it might help.<br>
I’ve tried to change GPU raycasting to CPU raycasting in the application setting but that didn’t help.</p>
<p>Is there any way to disable GPU buffering of some sort like I did to solve the issue in Sublime?<br>
Maybe any other advice on how to debug this?</p>

---

## Post #2 by @lassoan (2020-11-24 20:12 UTC)

<p>Thanks for reporting this. We have had 2 reports of Slicer crashing on mac after coming back from sleep, but they were all isolated, non-reproducible cases, so we could not act on them. It is great that you have a way to reproduce this problem because it means that we can fix it. I’ve added a bug report for this:</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/5315" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5315" target="_blank" rel="noopener">Crash on MacOS after coming back from sleep</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-11-24" data-time="20:05:08" data-timezone="UTC">08:05PM - 24 Nov 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-11-26" data-time="19:17:43" data-timezone="UTC">07:17PM - 26 Nov 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars0.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">"When I use an iPad as a second Sidecar display after the computer wakes from sleep Slicer crashes."
See more information here:...</p>
</div>

<div class="labels">
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">type:bug</span>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>As a first step, could you send the crash report that macOS generates? Especially the call stack (beginning of the file) is informative, because it tell which library is the culprit (almost surely Qt) and which method. We can then find what other application developers did, when they encountered this problem and adopt one of those solutions.</p>

---

## Post #3 by @pll_llq (2020-11-25 05:58 UTC)

<p>Thanks for you reply <a class="mention" href="/u/lassoan">@lassoan</a><br>
Here’s the crash log<br>
</p><aside class="onebox githubgist">
  <header class="source">
      <a href="https://gist.github.com/piiq/8703e7eaacac7fd9a8f30ea8f8f68cf2" target="_blank" rel="noopener nofollow ugc">gist.github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://gist.github.com/piiq/8703e7eaacac7fd9a8f30ea8f8f68cf2" target="_blank" rel="noopener nofollow ugc">https://gist.github.com/piiq/8703e7eaacac7fd9a8f30ea8f8f68cf2</a></h4>
<h5>gistfile1.txt</h5>
<pre><code class="Text">Process:               Slicer [8928]
Path:                  /Applications/Medical Imaging/Slicer.app/Contents/MacOS/Slicer
Identifier:            ???
Version:               4.11.20200930 (4.11.20200930)
Code Type:             X86-64 (Native)
Parent Process:        ??? [1]
Responsible:           Slicer [8928]
User ID:               501

Date/Time:             2020-11-23 12:43:31.083 +0300</code></pre>
This file has been truncated. <a href="https://gist.github.com/piiq/8703e7eaacac7fd9a8f30ea8f8f68cf2" target="_blank" rel="noopener nofollow ugc">show original</a>

<p>
</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @lassoan (2020-11-25 21:43 UTC)

<p>Thank you, this is interesting. It seems to be an error in the DICOM database. Can you try if it makes a difference if you create a new DICOM database? (in DICOM module)</p>

---

## Post #5 by @pll_llq (2020-11-26 18:24 UTC)

<p>Thanks for the suggestion <a class="mention" href="/u/lassoan">@lassoan</a>. The main “non-standard” thing with the dicom database is that it frequently contains images that have non-ascii characters in the “patient name” tag (cyrillic). I saw earlier that some programs don’t yet have unicode support, for example ITK-Snap can’t load images from paths that contain non-ascii characters.</p>
<p>I don’t usually use DICOMs as I try to stick to Nifti files in general, but I did some more debugging with the DICOM database.</p>
<p>Here’s what I’ve found</p>
<ol>
<li>I have an older database in the main folder where the database is expected to be<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5cf65544797175cab7e9f9a5b772d0bf5118f49f.png" data-download-href="/uploads/short-url/dgnGZFBhi3chRVwdkmvArh2GDPV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cf65544797175cab7e9f9a5b772d0bf5118f49f_2_690x149.png" alt="image" data-base62-sha1="dgnGZFBhi3chRVwdkmvArh2GDPV" width="690" height="149" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cf65544797175cab7e9f9a5b772d0bf5118f49f_2_690x149.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cf65544797175cab7e9f9a5b772d0bf5118f49f_2_1035x223.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cf65544797175cab7e9f9a5b772d0bf5118f49f_2_1380x298.png 2x" data-dominant-color="F0F0E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1720×372 35.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdfcf3f4ce7d804325bdd8b008e3e70146a2f9d2.png" data-download-href="/uploads/short-url/r6IbQFctBuTQrPh99E3XdCdDvfs.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bdfcf3f4ce7d804325bdd8b008e3e70146a2f9d2_2_690x192.png" alt="image" data-base62-sha1="r6IbQFctBuTQrPh99E3XdCdDvfs" width="690" height="192" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bdfcf3f4ce7d804325bdd8b008e3e70146a2f9d2_2_690x192.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bdfcf3f4ce7d804325bdd8b008e3e70146a2f9d2_2_1035x288.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bdfcf3f4ce7d804325bdd8b008e3e70146a2f9d2_2_1380x384.png 2x" data-dominant-color="E7E7EF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1740×486 65.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ol>
<p>So I was using a proper external display, I’ve upgraded the dicom database and everything was fine. No issues.<br>
But then I recalled that the issue appeared when I used an iPad as a sidecar display. I’ve connected the iPad to the mac, and after I received an absolutely meaningful error notification from macOS<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2202c2caa7098cc2b170a8baa53cef929162739.png" data-download-href="/uploads/short-url/rHjyDsjZzY0RZMMkeu3ppYlBlep.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2202c2caa7098cc2b170a8baa53cef929162739_2_576x500.png" alt="image" data-base62-sha1="rHjyDsjZzY0RZMMkeu3ppYlBlep" width="576" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2202c2caa7098cc2b170a8baa53cef929162739_2_576x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2202c2caa7098cc2b170a8baa53cef929162739.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2202c2caa7098cc2b170a8baa53cef929162739.png 2x" data-dominant-color="555452"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">606×526 34.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
the app crashed with the following log</p><aside class="onebox githubgist" data-onebox-src="https://gist.github.com/piiq/41f1b588c366041ed542018fc30e1e98">
  <header class="source">

      <a href="https://gist.github.com/piiq/41f1b588c366041ed542018fc30e1e98" target="_blank" rel="noopener nofollow ugc">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/piiq/41f1b588c366041ed542018fc30e1e98" target="_blank" rel="noopener nofollow ugc">https://gist.github.com/piiq/41f1b588c366041ed542018fc30e1e98</a></h4>

  <h5>gistfile1.txt</h5>
  <pre><code class="Text">Process:               Slicer [53353]
Path:                  /Applications/Medical Imaging/Slicer.app/Contents/MacOS/Slicer
Identifier:            ???
Version:               4.11.20200930 (4.11.20200930)
Code Type:             X86-64 (Native)
Parent Process:        ??? [1]
Responsible:           Slicer [53353]
User ID:               501

Date/Time:             2020-11-26 21:10:28.977 +0300</code></pre>
   This file has been truncated. <a href="https://gist.github.com/piiq/41f1b588c366041ed542018fc30e1e98" target="_blank" rel="noopener nofollow ugc">show original</a>

<p>
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>So I can replicate the issue only with an iPad as a sidecar display, and not with a physical external or internal display</p>
<p>I personally am fine just knowing these limitations and I don’t know if many slicer users use sidecar. If this is an issue that might influence all mac users in the future, maybe it is worth looking into it. If it only relates to sidecar - I personally doubt that many users will run into it.</p>

---

## Post #6 by @lassoan (2020-11-26 19:14 UTC)

<p>Thanks for the additional information.</p>
<p>Current stable release fully supports international characters (utf8) everywhere. If you run into any issues then let us know.</p>
<p>The crash in this latest report seems to be due to a low level display driver or Qt bug that probably Apple or Qt developers will fix in the future. We could report the error and nag developers to make it happen faster, but it is probably not worth the effort.</p>

---
