---
topic_id: 34005
title: "Unable To Build Slicercustomapptemplate In Windows"
date: 2024-01-28
url: https://discourse.slicer.org/t/34005
---

# Unable to build SlicerCustomAppTemplate in Windows

**Topic ID**: 34005
**Date**: 2024-01-28
**URL**: https://discourse.slicer.org/t/unable-to-build-slicercustomapptemplate-in-windows/34005

---

## Post #1 by @apparrilla (2024-01-28 00:34 UTC)

<p>I´m trying to build my first Custom Slicer App using SlicerCustomAppTemplate project but I can´t even to build the basic one.<br>
Windows 11. VS 2022. Cmake 3.28.1<br>
My steps:</p>
<ul>
<li>Create D:\D2 forder and run cookiecutter gh:KitwareMedical/SlicerCustomAppTemplate on it.</li>
<li>Open CMake. Select source (D:\D2\SlicerCustomAppTemplate) and output (D:\D2\SR) folders. Add Qt5_DIR path in C:/Qt/5.15.2/msvc2019_64/lib/cmake/Qt5. Add bool CMAKE_CONFIGURATION_TYPES string Release. Then, Configure and Generate.</li>
</ul>
<p>Cmake shows this values<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61bd6618b42e75a80043250b95ff6ed68259696a.png" data-download-href="/uploads/short-url/dWE6bkyDcuonFxXrhxsE6P3JCwG.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61bd6618b42e75a80043250b95ff6ed68259696a_2_493x375.png" alt="image" data-base62-sha1="dWE6bkyDcuonFxXrhxsE6P3JCwG" width="493" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61bd6618b42e75a80043250b95ff6ed68259696a_2_493x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61bd6618b42e75a80043250b95ff6ed68259696a_2_739x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61bd6618b42e75a80043250b95ff6ed68259696a_2_986x750.png 2x" data-dominant-color="F0F0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2122×1612 296 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/016834b1a337426a609be353aedcc0d08ed8e403.png" data-download-href="/uploads/short-url/crJIJpHXcjkHI3Qv4NKuRfG1PB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/016834b1a337426a609be353aedcc0d08ed8e403_2_426x375.png" alt="image" data-base62-sha1="crJIJpHXcjkHI3Qv4NKuRfG1PB" width="426" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/016834b1a337426a609be353aedcc0d08ed8e403_2_426x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/016834b1a337426a609be353aedcc0d08ed8e403_2_639x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/016834b1a337426a609be353aedcc0d08ed8e403_2_852x750.png 2x" data-dominant-color="EEEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1843×1620 317 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6fbe91cb449b46224355314dcdd025e430de45d7.png" data-download-href="/uploads/short-url/fWxi8oI94SdqvjjEORByYddVBk3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fbe91cb449b46224355314dcdd025e430de45d7_2_417x375.png" alt="image" data-base62-sha1="fWxi8oI94SdqvjjEORByYddVBk3" width="417" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fbe91cb449b46224355314dcdd025e430de45d7_2_417x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fbe91cb449b46224355314dcdd025e430de45d7_2_625x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fbe91cb449b46224355314dcdd025e430de45d7_2_834x750.png 2x" data-dominant-color="F3F3F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1803×1621 199 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>VS ALL_BUILD project compile crashed and this is the error message:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f79feaf87d22a7501331f1c53f2396de3d834f7.png" data-download-href="/uploads/short-url/dCCJpGfBpfBjVoTjze16dvKwjif.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f79feaf87d22a7501331f1c53f2396de3d834f7_2_690x27.png" alt="image" data-base62-sha1="dCCJpGfBpfBjVoTjze16dvKwjif" width="690" height="27" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f79feaf87d22a7501331f1c53f2396de3d834f7_2_690x27.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f79feaf87d22a7501331f1c53f2396de3d834f7_2_1035x40.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f79feaf87d22a7501331f1c53f2396de3d834f7_2_1380x54.png 2x" data-dominant-color="2D2D2D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3190×126 28.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>
<p>I´m sure I´m doing something wrong but I´m stacked… Some idea what should be the problem?<br>
Thanks in advance</p>

---

## Post #2 by @jamesobutler (2024-01-28 01:19 UTC)

<p>A change in the file formats of the README from text file to markdown file caused this issue. Make the same type changes in your local source as the following linked PR (see below). Once that PR is integrated then new runs of the custom app template project should create a custom app template that builds successfully.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/KitwareMedical/SlicerCustomAppTemplate/pull/55">
  <header class="source">

      <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/pull/55" target="_blank" rel="noopener nofollow ugc">github.com/KitwareMedical/SlicerCustomAppTemplate</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/pull/55" target="_blank" rel="noopener nofollow ugc">Update slicer-application-properties.cmake</a>
      </h4>

    <div class="branches">
      <code>KitwareMedical:main</code> ← <code>brandus1:patch-1</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-12-28" data-time="10:27:31" data-timezone="UTC">10:27AM - 28 Dec 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/brandus1" target="_blank" rel="noopener nofollow ugc">
            <img alt="brandus1" src="https://avatars.githubusercontent.com/u/62740047?v=4" class="onebox-avatar-inline" width="20" height="20">
            brandus1
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 1 additions and 1 deletions">
          <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/pull/55/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+1</span>
            <span class="removed">-1</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">README Extension update for latest slicer compatibility</p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @apparrilla (2024-01-28 12:06 UTC)

<p>Right!!! I compile it and works!<br>
Thanks so much…</p>

---
