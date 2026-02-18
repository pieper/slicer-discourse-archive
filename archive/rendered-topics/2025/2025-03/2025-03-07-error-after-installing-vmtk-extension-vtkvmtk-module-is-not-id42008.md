# Error after installing VMTK extension: "vtkvmtk module is not loaded"

**Topic ID**: 42008
**Date**: 2025-03-07
**URL**: https://discourse.slicer.org/t/error-after-installing-vmtk-extension-vtkvmtk-module-is-not-loaded/42008

---

## Post #1 by @feiyu (2025-03-07 07:50 UTC)

<p>I tried to use the VMTK extension for vessel segmentation, but I can’t find it in the Modules. However, I can see that the latest version of VMTK has been downloaded in the extension manager. Can anyone help me with this?</p>

---

## Post #2 by @feiyu (2025-03-07 07:55 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/7529392667771b73c7ae5bb1fd3352015776969b.png" data-download-href="/uploads/short-url/gIsbqXffzdsfvRXUdfhjQcFvJdF.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/7529392667771b73c7ae5bb1fd3352015776969b.png" alt="image" data-base62-sha1="gIsbqXffzdsfvRXUdfhjQcFvJdF" width="690" height="435" data-dominant-color="2E3031"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">727×459 13.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/565a556c3ae36da535e50a8082364c53c6adb660.png" data-download-href="/uploads/short-url/cjUBi5OLh8sjofwWYumIQCPVxWE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/565a556c3ae36da535e50a8082364c53c6adb660_2_690x45.png" alt="image" data-base62-sha1="cjUBi5OLh8sjofwWYumIQCPVxWE" width="690" height="45" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/565a556c3ae36da535e50a8082364c53c6adb660_2_690x45.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/565a556c3ae36da535e50a8082364c53c6adb660_2_1035x67.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/565a556c3ae36da535e50a8082364c53c6adb660_2_1380x90.png 2x" data-dominant-color="252525"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1744×115 9.26 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @cpinter (2025-03-07 10:47 UTC)

<p>What Slicer version are you using? If older than 5.8 I suggest using 5.8, because we can only fix issues in the latest version. Thanks!</p>

---

## Post #4 by @lassoan (2025-03-07 12:50 UTC)

<p>Probably you have run into this issue:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/vmtk/SlicerExtension-VMTK/issues/22#issuecomment-699000634">
  <header class="source">

      <a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/22#issuecomment-699000634" target="_blank" rel="noopener">github.com/vmtk/SlicerExtension-VMTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/22#issuecomment-699000634" target="_blank" rel="noopener">Fail to instantiate module “vtkvmtk” error reported at startup</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-09-25" data-time="15:37:26" data-timezone="UTC">03:37PM - 25 Sep 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          enhancement
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This error is reported at Slicer startup if SlicerVMTK extension is installed:
<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">
```
CLI executable: C:/Users/E/AppData/Roaming/NA-MIC/Extensions-29387/SlicerVMTK/lib/Slicer-4.11/qt-loadable-modules/vtkvmtk.py
The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program.
Fail to instantiate module “vtkvmtk”
The following modules failed to be instantiated:
vtkvmtk
```</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>This is a false alarm and the message can be safely ignored, because there is no such Slicer module as “vtkvmtk”. There is a file by that name in the module folder, but it is not a Slicer module, it should not be loaded, and it is not loaded. The only problem is the error message itself.</p>
<p>Let us know if you don’t find any of the actually existing <a href="https://github.com/vmtk/SlicerExtension-VMTK?tab=readme-ov-file#usage">VMTK modules</a>.</p>

---

## Post #5 by @feiyu (2025-03-08 08:02 UTC)

<p>The version I am using is 5.8.1, the latest stable version.</p>

---

## Post #6 by @feiyu (2025-03-08 08:14 UTC)

<p>This forum recommends the VMTK extension for vascular segmentation. If the VMTK extension is not available, what would I download in the extension manager interface, and how should I use it?</p>

---

## Post #7 by @feiyu (2025-03-08 08:19 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5172ef4c8e55595fbd6f35ee62f0cf558a1b272.png" data-download-href="/uploads/short-url/up5n1TcRoAWZ0xb13Zq2SSkRrQm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5172ef4c8e55595fbd6f35ee62f0cf558a1b272_2_690x49.png" alt="image" data-base62-sha1="up5n1TcRoAWZ0xb13Zq2SSkRrQm" width="690" height="49" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5172ef4c8e55595fbd6f35ee62f0cf558a1b272_2_690x49.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5172ef4c8e55595fbd6f35ee62f0cf558a1b272_2_1035x73.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5172ef4c8e55595fbd6f35ee62f0cf558a1b272_2_1380x98.png 2x" data-dominant-color="262626"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1755×125 9.54 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I download it in the extension manager interface</p>

---

## Post #8 by @jamesobutler (2025-03-08 13:46 UTC)

<p>The SlicerVMTK extension installs Slicer modules that have names you can review at:</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/vmtk/SlicerExtension-VMTK?tab=readme-ov-file#usage">
  <header class="source">

      <a href="https://github.com/vmtk/SlicerExtension-VMTK?tab=readme-ov-file#usage" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/3102836605e8a4650afeb0dcda436f17/vmtk/SlicerExtension-VMTK?tab=readme-ov-file#usage" class="thumbnail">

  <h3><a href="https://github.com/vmtk/SlicerExtension-VMTK?tab=readme-ov-file#usage" target="_blank" rel="noopener nofollow ugc">GitHub - vmtk/SlicerExtension-VMTK</a></h3>

    <p><span class="github-repo-description">Contribute to vmtk/SlicerExtension-VMTK development by creating an account on GitHub.</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It is currently a bug that a Slicer module named vtkvmtk is attempted to be loaded.</p>

---

## Post #9 by @feiyu (2025-03-09 00:44 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5fc1d72660dc0ad34eaf81af271808531a0f4bd4.png" data-download-href="/uploads/short-url/dF6EYuje4i32PqNjXCTwz8uVZoU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5fc1d72660dc0ad34eaf81af271808531a0f4bd4.png" alt="image" data-base62-sha1="dF6EYuje4i32PqNjXCTwz8uVZoU" width="672" height="443"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">672×443 8.33 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0700f8d52d6a4567eff4f1f4eebbee7a98093c5.jpeg" data-download-href="/uploads/short-url/yj0GhrCOHoH30UY3ts1VwSwMYPX.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0700f8d52d6a4567eff4f1f4eebbee7a98093c5.jpeg" alt="image" data-base62-sha1="yj0GhrCOHoH30UY3ts1VwSwMYPX" width="681" height="452"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">681×452 91.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Comparing these two images, it is clear that simply clicking the “FULL TEXT” option revealed four loadable modules, while VMTK itself appears to be unloadable. Is this a bug in the developer’s design? I couldn’t find the latest VMTK extension tutorial on GitHub. Could you provide a link? Thank you!</p>

---

## Post #10 by @jamesobutler (2025-03-09 03:54 UTC)

<p>The bug is that vtkvmtk shows up at all as a Slicer module. It should not be there as it is not a Slicer module.</p>
<p>The SlicerVMTK extension provides a collection of Slicer modules. Some of them contain a description that included the text “VMTK” such as “Clip Vessel” which is a module provided by SlicerVMTK.</p>
<p>The complete list of Slicer modules that come with SlicerVMTK can be viewed at:</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/vmtk/SlicerExtension-VMTK?tab=readme-ov-file#usage">
  <header class="source">

      <a href="https://github.com/vmtk/SlicerExtension-VMTK?tab=readme-ov-file#usage" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/3102836605e8a4650afeb0dcda436f17/vmtk/SlicerExtension-VMTK?tab=readme-ov-file#usage" class="thumbnail">

  <h3><a href="https://github.com/vmtk/SlicerExtension-VMTK?tab=readme-ov-file#usage" target="_blank" rel="noopener nofollow ugc">GitHub - vmtk/SlicerExtension-VMTK</a></h3>

    <p><span class="github-repo-description">Contribute to vmtk/SlicerExtension-VMTK development by creating an account on GitHub.</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
