---
topic_id: 25329
title: "Change The Slicers Name And Icon"
date: 2022-09-19
url: https://discourse.slicer.org/t/25329
---

# Change the Slicer's name and icon

**Topic ID**: 25329
**Date**: 2022-09-19
**URL**: https://discourse.slicer.org/t/change-the-slicers-name-and-icon/25329

---

## Post #1 by @miniminic (2022-09-19 08:43 UTC)

<p>How to change this Slicer’s name and icon<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d88b52a15ff195cb42c966dff3ffdb65c0941a0d.jpeg" data-download-href="/uploads/short-url/uTDD8F13XiElmtE6Vng12GsnLDn.jpeg?dl=1" title="屏幕截图" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d88b52a15ff195cb42c966dff3ffdb65c0941a0d_2_690x307.jpeg" alt="屏幕截图" data-base62-sha1="uTDD8F13XiElmtE6Vng12GsnLDn" width="690" height="307" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d88b52a15ff195cb42c966dff3ffdb65c0941a0d_2_690x307.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d88b52a15ff195cb42c966dff3ffdb65c0941a0d.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d88b52a15ff195cb42c966dff3ffdb65c0941a0d.jpeg 2x" data-dominant-color="2B2B2B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">屏幕截图</span><span class="informations">966×431 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @jamesobutler (2022-09-19 11:35 UTC)

<p>You can use the <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" rel="noopener nofollow ugc">SlicerCustomAppTemplate</a> to create a customized version of Slicer with a new name, logo, style sheets, default module, etc…</p>
<p>See this article about SlicerCAT which is an example implementation of a SlicerCustomApp</p>
<p><a href="https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/</a></p>

---

## Post #3 by @miniminic (2022-09-19 11:37 UTC)

<p>Do I have to use SlicerCAT to customize these things? I have made a lot of changes in Slicer, and I don’t want to use SlicerCAT to rewrite and edit them, at least not yet</p>

---

## Post #4 by @jamesobutler (2022-09-19 14:34 UTC)

<p>SlicerCustomApp was specifically created for all these customizations that you desire so you shouldn’t just be hacking a fork of the Slicer git repo to try and achieve the same thing as you will be wasting work.</p>
<p>With a SlicerCustomApp you can specify the git repo of Slicer that you want to use. So in the SlicerCAT example of a SlicerCustomApp see this section:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/KitwareMedical/SlicerCAT/blob/e651f197f56e3378ce094378dd29631c08b25a33/CMakeLists.txt#L14-L18">
  <header class="source">

      <a href="https://github.com/KitwareMedical/SlicerCAT/blob/e651f197f56e3378ce094378dd29631c08b25a33/CMakeLists.txt#L14-L18" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/KitwareMedical/SlicerCAT/blob/e651f197f56e3378ce094378dd29631c08b25a33/CMakeLists.txt#L14-L18" target="_blank" rel="noopener nofollow ugc">KitwareMedical/SlicerCAT/blob/e651f197f56e3378ce094378dd29631c08b25a33/CMakeLists.txt#L14-L18</a></h4>



    <pre class="onebox"><code class="lang-txt">
      <ol class="start lines" start="14" style="counter-reset: li-counter 13 ;">
          <li>FetchContent_Populate(slicersources</li>
          <li>  GIT_REPOSITORY git://github.com/Slicer/Slicer</li>
          <li>  GIT_TAG        39be4408f084b3e5d632b373a4985cd7fa6c661b</li>
          <li>  GIT_PROGRESS   1</li>
          <li>  )</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @miniminic (2022-09-20 02:19 UTC)

<p>Okay, thank you very much.</p>

---
