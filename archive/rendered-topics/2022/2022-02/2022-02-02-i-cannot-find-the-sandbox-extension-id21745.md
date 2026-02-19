---
topic_id: 21745
title: "I Cannot Find The Sandbox Extension"
date: 2022-02-02
url: https://discourse.slicer.org/t/21745
---

# I cannot find the Sandbox extension

**Topic ID**: 21745
**Date**: 2022-02-02
**URL**: https://discourse.slicer.org/t/i-cannot-find-the-sandbox-extension/21745

---

## Post #1 by @Kawtar_Lakrad (2022-02-02 02:57 UTC)

<p>Operating system: Windows 11<br>
Slicer version: v4.11<br>
Expected behavior: Find the sandbox extension<br>
Actual behavior: I can’t find the sandbox extension, although all the others are existing.<br>
I was wondering if there is any other way to download this extension.</p>

---

## Post #2 by @lassoan (2022-02-02 02:59 UTC)

<p>The nightly build of Sandbox failed (a new feature was added yesterday and one required file was not added to the repository). The problem is now fixed, so it will be available again tomorrow. But if you need it right now then follow the instructions <a href="https://discourse.slicer.org/t/new-feature-basic-support-for-physically-based-rendering-pbr/21725/3">here</a>.</p>

---

## Post #3 by @Kawtar_Lakrad (2022-02-04 22:17 UTC)

<p>I still can’t get it even if I followed the instructions, do you think there is another reason for this?</p>

---

## Post #4 by @Kawtar_Lakrad (2022-02-05 05:29 UTC)

<p>When I try to install it manually this is what I get.<br>
Thank you for your help.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99b089b5e6ba8fe599aff31f0a6c8d6bd6a8b447.png" alt="Screenshot 2022-02-05 002821" data-base62-sha1="lVBhAKm4iR6fJUw1wo40S19I7aL" width="508" height="113"></p>

---

## Post #5 by @manjula (2022-02-05 05:57 UTC)

<p>Try the latest preview release. | You are using the stable version now</p>

---

## Post #6 by @lassoan (2022-02-08 19:40 UTC)

<aside class="quote no-group" data-username="Kawtar_Lakrad" data-post="4" data-topic="21745" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kawtar_lakrad/48/13528_2.png" class="avatar"> Kawtar_Lakrad:</div>
<blockquote>
<p>When I try to install it manually this is what I get.<br>
Thank you for your help.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99b089b5e6ba8fe599aff31f0a6c8d6bd6a8b447.png" alt="Screenshot 2022-02-05 002821" data-base62-sha1="lVBhAKm4iR6fJUw1wo40S19I7aL" width="508" height="113"></p>
</blockquote>
</aside>
<p>It seems that you downloaded the content of the extension’s github repository. That is a zip file, but it is not an extension package. You cannot install that zip file in the extensions manager. You can build extension packages as described in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html">developer guide</a>, but users don’t need to go through this process.</p>
<p>Users can install extensions by a few clicks from the extensions server as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#install-extensions">here</a>.</p>

---

## Post #7 by @Kawtar_Lakrad (2022-02-15 05:39 UTC)

<p>Thank you so much.<br>
I tried the latest preview release, and I found the Sandbox extension finally.<br>
Now I am having an issue with gel dosimetry analysis module, I can’t get the slicelets window to show (It is working perfectly in the previous release).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d446e5791c1d470eaf75ce9e11662716eb17e31.png" data-download-href="/uploads/short-url/hSaio7FitNLRUBmKUWfI4rvXzAR.png?dl=1" title="Screenshot 2022-02-15 003707" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d446e5791c1d470eaf75ce9e11662716eb17e31_2_690x369.png" alt="Screenshot 2022-02-15 003707" data-base62-sha1="hSaio7FitNLRUBmKUWfI4rvXzAR" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d446e5791c1d470eaf75ce9e11662716eb17e31_2_690x369.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d446e5791c1d470eaf75ce9e11662716eb17e31_2_1035x553.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d446e5791c1d470eaf75ce9e11662716eb17e31_2_1380x738.png 2x" data-dominant-color="485B43"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-02-15 003707</span><span class="informations">1916×1027 255 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @Kawtar_Lakrad (2022-02-15 21:23 UTC)

<p>this is what I get whenever I try to show slicelets (gel dosimetry analysis)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/3006d46cec682dcd9e4f6174f685cd641a31f1d5.png" data-download-href="/uploads/short-url/6QRybk2JNFYUidWw18AmcLvlWPH.png?dl=1" title="Screenshot 2022-02-15 162134" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/3006d46cec682dcd9e4f6174f685cd641a31f1d5.png" alt="Screenshot 2022-02-15 162134" data-base62-sha1="6QRybk2JNFYUidWw18AmcLvlWPH" width="690" height="361" data-dominant-color="2B2121"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-02-15 162134</span><span class="informations">1426×747 69.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @jamesobutler (2022-02-15 21:31 UTC)

<p>The change from <code>SetSliceIntersectionVisibility</code> to <code>SetIntersectingSlicesVisibility</code> in <a href="https://github.com/Slicer/Slicer/commit/bc5d5b45fcb1949a2545ee1c2e2c1f35976698ac" class="inline-onebox" rel="noopener nofollow ugc">ENH: Add interactive slice intersections widget · Slicer/Slicer@bc5d5b4 · GitHub</a> may have been a more disruptive change than intended.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/dgmato">@dgmato</a><br>
Since it required an update to the script repository in the linked commit below, the old method name may have been frequently used in various scripts. Therefore it would probably be good to maintain the older method with some deprecation if we want to stick with this renamed method. I personally don’t think the new method name was necessary. However there is still the change from accessing the method from the slice composite node to now the slice display node.</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/3edd84ddba681786be9e916124126fc858592598">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/3edd84ddba681786be9e916124126fc858592598" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/3edd84ddba681786be9e916124126fc858592598" target="_blank" rel="noopener nofollow ugc">DOC: Update snippet to turn on slice intersections</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2022-01-31" data-time="14:11:54" data-timezone="UTC">02:11PM - 31 Jan 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/dgmato" target="_blank" rel="noopener nofollow ugc">
          <img alt="dgmato" src="https://avatars.githubusercontent.com/u/10816661?v=4" class="onebox-avatar-inline" width="20" height="20">
          dgmato
        </a>
      </div>

      <div class="lines" title="changed 1 files with 3 additions and 3 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/3edd84ddba681786be9e916124126fc858592598" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+3</span>
          <span class="removed">-3</span>
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


---

## Post #10 by @lassoan (2022-02-15 21:55 UTC)

<p>The rename was very important to clarify its meaning. <code>SliceIntersectionVisibility</code> may refer to either “visibility of this slice in other slice views”, or “visibility of other slices in this slice view”. In the slice display node there is already a <code>SliceIntersectionVisibility</code> property (that specifies if this slice should be shown in other views) so we had to add a new property that specifies if slice intersections should be shown in this slice view.</p>
<p>I’ll see if there is a way to access the slice display node from the slice composite node, and if there is a way then I’ll add a method there (marked as deprecated) to allow some more time for developers to update their code instead of forcing them to update immediately.</p>

---

## Post #11 by @Kawtar_Lakrad (2022-02-16 00:42 UTC)

<p>So is there something I can do know or should I just wait for an update?</p>

---

## Post #12 by @lassoan (2022-02-16 01:36 UTC)

<p>This particular issue will be fixed in tomorrow’s Slicer Preview Release. Let us know if something still does not work right.</p>

---

## Post #13 by @lassoan (2022-02-18 22:57 UTC)

<p>A post was split to a new topic: <a href="/t/gel-dosimetry-registration-step-fails/22059">Gel dosimetry registration step fails</a></p>

---

## Post #14 by @lassoan (2023-11-13 02:42 UTC)

<p>2 posts were split to a new topic: <a href="/t/save-line-profile-as-csv-file/32768">Save line profile as CSV file</a></p>

---
