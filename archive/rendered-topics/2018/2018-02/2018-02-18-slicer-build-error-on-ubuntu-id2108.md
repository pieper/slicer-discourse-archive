# Slicer build error on Ubuntu

**Topic ID**: 2108
**Date**: 2018-02-18
**URL**: https://discourse.slicer.org/t/slicer-build-error-on-ubuntu/2108

---

## Post #1 by @AhmadHossam10 (2018-02-18 14:03 UTC)

<p>Operating system: Ubuntu 17.10.1<br>
Slicer version: latest version<br>
Expected behavior: build successful<br>
Actual behavior: build failed</p>
<p>I contacted you before with my problem with ubuntu 17.10 and you fixed it after I cloned your new version. I encountered this problem while building the slicer and I have no solution for it</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1dd3beb79c60da296eaee03250bddf48637fff3d.png" data-download-href="/uploads/short-url/4fRvvtViarcLPDROnPTK2UWjaTX.png?dl=1" title="Screenshot%20from%202018-02-18%2002-20-23" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1dd3beb79c60da296eaee03250bddf48637fff3d_2_690x388.png" alt="Screenshot%20from%202018-02-18%2002-20-23" data-base62-sha1="4fRvvtViarcLPDROnPTK2UWjaTX" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1dd3beb79c60da296eaee03250bddf48637fff3d_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1dd3beb79c60da296eaee03250bddf48637fff3d_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1dd3beb79c60da296eaee03250bddf48637fff3d_2_1380x776.png 2x" data-dominant-color="412338"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202018-02-18%2002-20-23</span><span class="informations">1920×1080 431 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/8446cb5f45d1d4ea9213341cfff49b77b77d16dd.png" data-download-href="/uploads/short-url/iSaHyduu17TdMsizIvVnPtUmau1.png?dl=1" title="Screenshot%20from%202018-02-18%2002-21-24" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8446cb5f45d1d4ea9213341cfff49b77b77d16dd_2_690x388.png" alt="Screenshot%20from%202018-02-18%2002-21-24" data-base62-sha1="iSaHyduu17TdMsizIvVnPtUmau1" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8446cb5f45d1d4ea9213341cfff49b77b77d16dd_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8446cb5f45d1d4ea9213341cfff49b77b77d16dd_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8446cb5f45d1d4ea9213341cfff49b77b77d16dd_2_1380x776.png 2x" data-dominant-color="37172C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202018-02-18%2002-21-24</span><span class="informations">1920×1080 333 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2018-02-18 14:05 UTC)

<p>This seems to be a duplicate of this post:</p>
<aside class="quote quote-modified" data-post="19" data-topic="2082">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ahmadhossam10/48/1246_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/3d-slicer-build-error-with-gcc-7-on-ubuntu-17-04/2082/19">3D Slicer Build Error with GCC 7 on Ubuntu 17.04</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Everything is fixed except for an error in simpleITK there’s a file that’s not found. Would you please solve this issue ?  <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/8446cb5f45d1d4ea9213341cfff49b77b77d16dd.png" data-download-href="/uploads/short-url/iSaHyduu17TdMsizIvVnPtUmau1.png?dl=1" title="Screenshot%20from%202018-02-18%2002-21-24" rel="noopener nofollow ugc">[Screenshot%20from%202018-02-18%2002-21-24]</a><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1dd3beb79c60da296eaee03250bddf48637fff3d.png" data-download-href="/uploads/short-url/4fRvvtViarcLPDROnPTK2UWjaTX.png?dl=1" title="Screenshot%20from%202018-02-18%2002-20-23" rel="noopener nofollow ugc">[Screenshot%20from%202018-02-18%2002-20-23]</a>
  </blockquote>
</aside>


---

## Post #3 by @AhmadHossam10 (2018-02-18 14:08 UTC)

<p>yes i want any help because I have been trying for so many times</p>

---

## Post #4 by @lassoan (2018-02-18 14:13 UTC)

<p>This seems to be a common error,  unrelated to Slicer. Do a Google search for solutions. For example:</p>
<p><a href="https://sourceforge.net/p/pythonqt/discussion/631393/thread/69eb9ccb/" class="onebox" target="_blank">https://sourceforge.net/p/pythonqt/discussion/631393/thread/69eb9ccb/</a></p>

---

## Post #5 by @AhmadHossam10 (2018-02-18 14:18 UTC)

<p>okay I will try thanks</p>

---

## Post #6 by @chir.set (2018-02-18 14:36 UTC)

<p>You could install qtbase5-private-dev, the missing file is part of this package.</p>
<p>Sidenote : you can redirect error messages to a text file and copy/paste the relevant part in blockquote, rather than uploading screenshots, it’s hard to read.</p>
<p>Example for an error log file with timestamp  :<br>
make -j4 2&gt; $HOME/tmp/slicer_build_$(date +%F_%H%M%S).log</p>

---

## Post #7 by @AhmadHossam10 (2018-02-18 14:55 UTC)

<p>I will try thanks very much</p>

---
