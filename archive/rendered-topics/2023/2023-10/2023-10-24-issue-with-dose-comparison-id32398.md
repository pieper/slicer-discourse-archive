# Issue with dose comparison

**Topic ID**: 32398
**Date**: 2023-10-24
**URL**: https://discourse.slicer.org/t/issue-with-dose-comparison/32398

---

## Post #1 by @yasaman_kiumarsi (2023-10-24 16:28 UTC)

<p>Operating system: windows10<br>
Slicer version:5.2.2<br>
Expected behavior:<br>
Actual behavior: When I click dose comparison, the software closes after a few seconds.</p>

---

## Post #2 by @Sunderlandkyl (2023-10-24 19:16 UTC)

<p>Can you try on the latest stable release?</p>
<p>Can you also provide data to help reproduce the issue?</p>

---

## Post #3 by @yasaman_kiumarsi (2023-11-11 06:52 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc2363a5f894f23fd6e5b95f16676f227829ccdd.png" data-download-href="/uploads/short-url/vpqRBB8R9hVLQlMfbZ9E5OwYeiF.png?dl=1" title="Screenshot (17)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc2363a5f894f23fd6e5b95f16676f227829ccdd_2_690x387.png" alt="Screenshot (17)" data-base62-sha1="vpqRBB8R9hVLQlMfbZ9E5OwYeiF" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc2363a5f894f23fd6e5b95f16676f227829ccdd_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc2363a5f894f23fd6e5b95f16676f227829ccdd_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc2363a5f894f23fd6e5b95f16676f227829ccdd.png 2x" data-dominant-color="A9A9A1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (17)</span><span class="informations">1366×768 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am sending you a picture as an attachment, after a few seconds the software closes. My reference dose was the output from MATLAB, which I somehow converted into dose format so that the software for dose measurement accepts it as the dose volume, and I compared it with the dose that I obtained from TPS and I filled  the rest of the parts according to the image.</p>

---

## Post #4 by @yasaman_kiumarsi (2023-11-11 07:05 UTC)

<p>Operating system: 10<br>
Slicer version: 5.2.2<br>
Expected behavior:<br>
Actual behavior:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc2363a5f894f23fd6e5b95f16676f227829ccdd.png" data-download-href="/uploads/short-url/vpqRBB8R9hVLQlMfbZ9E5OwYeiF.png?dl=1" title="Screenshot (17)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc2363a5f894f23fd6e5b95f16676f227829ccdd_2_690x387.png" alt="Screenshot (17)" data-base62-sha1="vpqRBB8R9hVLQlMfbZ9E5OwYeiF" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc2363a5f894f23fd6e5b95f16676f227829ccdd_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc2363a5f894f23fd6e5b95f16676f227829ccdd_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc2363a5f894f23fd6e5b95f16676f227829ccdd.png 2x" data-dominant-color="A9A9A1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (17)</span><span class="informations">1366×768 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
When I use RT Slicer from dose comparison, after clicking on dose comparison, the software closes after a few seconds and does not work.<br>
I am sending you a picture as an attachment, after a few seconds the software closes. My reference dose was the output from MATLAB, which I somehow converted into dose format so that the software for dose measurement accepts it as the dose volume, and I compared it with the dose that I obtained from TPS and the rest of the parts according to the image. I filled.</p>

---

## Post #5 by @yasaman_kiumarsi (2023-11-11 08:06 UTC)

<p>Operating system: 10<br>
Slicer version: 5.4.0<br>
Expected behavior:<br>
Actual behavior: How to fill the dose comparison parts in RT Slicer? I mean, how much should I place in Mask structure, Gamma volume and other parts?</p>

---

## Post #6 by @cpinter (2023-11-13 11:13 UTC)

<p>Also posted here</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/7380">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/7380" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/7380" target="_blank" rel="noopener">Dose comparison parts in RT Slicer</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-11-12" data-time="09:23:49" data-timezone="UTC">09:23AM - 12 Nov 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/Y-kiumarsi" target="_blank" rel="noopener">
          <img alt="Y-kiumarsi" src="https://avatars.githubusercontent.com/u/150583859?v=4" class="onebox-avatar-inline" width="20" height="20">
          Y-kiumarsi
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

How to fill the dose comparison parts in RT Slicer? I mean, how mu<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ch should I place in Mask structure, Gamma volume and other parts?

When I use RT Slicer from dose comparison, after clicking on dose comparison, the software closes after a few seconds and does not work. I am sending you a picture as an attachment, after a few seconds the software closes. My reference dose was the output from MATLAB, which I somehow converted into dose format so that the software for dose measurement accepts it as the dose volume, and I compared it with the dose that I obtained from TPS and the rest of the parts according to the image I filled.

When I use RT Slicer from dose comparison, after clicking on dose comparison, the software closes after a few seconds and does not work. I don't know if there is a problem in filling the dose comparison fields or if it is another problem --&gt;

   When I use RT Slicer from dose comparison, after clicking on dose comparison, the software closes after a few seconds and does not work. I am sending you a picture as an attachment, after a few seconds the software closes. My reference dose was the output from MATLAB, which I somehow converted into dose format so that the software for dose measurement accepts it as the dose volume, and I compared it with the dose that I obtained from TPS and the rest of the parts according to the image I filled.

When I use RT Slicer from dose comparison, after clicking on dose comparison, the software closes after a few seconds and does not work. I don't know if there is a problem in filling the dose comparison fields or if it is another problem
![Screenshot (17)](https://github.com/Slicer/Slicer/assets/150583859/b38c7535-f3ff-41cd-ae36-9ed71302e49f)


## Environment
Operating system:  windows 10
Slicer version: 5.4.0</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
