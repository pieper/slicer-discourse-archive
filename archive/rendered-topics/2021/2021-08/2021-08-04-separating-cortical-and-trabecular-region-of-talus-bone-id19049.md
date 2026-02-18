# Separating Cortical and trabecular region of Talus bone

**Topic ID**: 19049
**Date**: 2021-08-04
**URL**: https://discourse.slicer.org/t/separating-cortical-and-trabecular-region-of-talus-bone/19049

---

## Post #1 by @Manav_Kothari (2021-08-04 06:55 UTC)

<p>I am interested in separating cortical and trabecular region of Talus bone and generate individual STL file. There is one add-on in Analyze Direct software named Bone Microarchitecture Analysis (BMA). Is there any similar function in Slicer as well?</p>
<p>Thanking You</p>

---

## Post #2 by @pieper (2021-08-04 14:41 UTC)

<p>I’m not sure if they have the same functionality as the software you mentioned, but these might help:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/Extensions/BoneTextureExtension" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/4.10/Extensions/BoneTextureExtension</a></p>
<p><a href="https://pyradiomics.readthedocs.io/en/latest/index.html" class="onebox" target="_blank" rel="noopener">https://pyradiomics.readthedocs.io/en/latest/index.html</a></p>

---

## Post #3 by @muratmaga (2021-08-04 15:28 UTC)

<aside class="quote no-group quote-modified" data-username="pieper" data-post="2" data-topic="19049">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/Extensions/BoneTextureExtension" class="inline-onebox">Documentation/4.10/Extensions/BoneTextureExtension - Slicer Wiki</a></p>
</blockquote>
</aside>
<p>Unfortunately bone texture extension is not functional for sometime now.</p>

---

## Post #4 by @pieper (2021-08-04 15:53 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="19049">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Unfortunately bone texture extension is not functional for sometime now.</p>
</blockquote>
</aside>
<p>What’s not working?  It seems to be building right, as least on windows, and I don’t see any issues in the tracker.</p>
<p><a href="https://slicer.cdash.org/build/2346236" class="onebox" target="_blank" rel="noopener">https://slicer.cdash.org/build/2346236</a></p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/Kitware/BoneTextureExtension/issues">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Kitware/BoneTextureExtension/issues" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/dc4a5d733d8b3b587b9b2eaefcbfa861a82494cf5465800bfe8930b5b9528ea0/Kitware/BoneTextureExtension" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/Kitware/BoneTextureExtension/issues" target="_blank" rel="noopener">Issues · Kitware/BoneTextureExtension</a></h3>

  <p>Slicer extensions for computing feature maps of N-Dimensional images using well-known texture analysis methods. - Issues · Kitware/BoneTextureExtension</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @muratmaga (2021-08-04 15:56 UTC)

<p>Yes, extension was built but the feature maps did not compute/displayed for quite sometime. But looks like they just fixed it, haven’t it tried it yet though.</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Kitware/BoneTextureExtension/issues/22">
  <header class="source">

      <a href="https://github.com/Kitware/BoneTextureExtension/issues/22" target="_blank" rel="noopener nofollow ugc">github.com/Kitware/BoneTextureExtension</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Kitware/BoneTextureExtension/issues/22" target="_blank" rel="noopener nofollow ugc">Bonetexture in 3D Slicer won’t compute/display feature maps</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2019-10-16" data-time="14:40:49" data-timezone="UTC">02:40PM - 16 Oct 19 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2021-07-13" data-time="09:14:14" data-timezone="UTC">09:14AM - 13 Jul 21 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/lcw918" target="_blank" rel="noopener nofollow ugc">
          <img alt="lcw918" src="https://avatars.githubusercontent.com/u/56546797?v=4" class="onebox-avatar-inline" width="20" height="20">
          lcw918
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">3dslicer: 4.10.02
Dell G7  7590
Win10 10.0.17763</p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
