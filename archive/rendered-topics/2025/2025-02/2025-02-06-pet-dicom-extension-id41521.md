# PET DICOM extension

**Topic ID**: 41521
**Date**: 2025-02-06
**URL**: https://discourse.slicer.org/t/pet-dicom-extension/41521

---

## Post #1 by @akmal871026 (2025-02-06 03:22 UTC)

<p>Hello,</p>
<p>There is no PetDicom Extension in version 5.8.0.</p>
<p>I TRIED TO INSTALL FROM FOLDER, BUT error pop up</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3211ff74d725b545d5ce08813dcd3d3973300a5.png" data-download-href="/uploads/short-url/wphm2vSTnDryeB6zfeDdLyI7WG9.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3211ff74d725b545d5ce08813dcd3d3973300a5.png" alt="Capture" data-base62-sha1="wphm2vSTnDryeB6zfeDdLyI7WG9" width="339" height="150"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">339×150 3.35 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>THE EXTENSION CAN DOWNLOADED HERE<br>
<a href="https://github.com/QIICR/Slicer-PETDICOMExtension" rel="noopener nofollow ugc">https://github.com/QIICR/Slicer-PETDICOMExtension</a></p>

---

## Post #2 by @jamesobutler (2025-02-06 03:57 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> can you or someone you know for this project fix the build error for this extension? If no longer maintained and it is broken should the extension be archived to no longer be in the Slicer extension index?</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.cdash.org/viewBuildError.php?buildid=3679199">
  <header class="source">
      <img src="https://slicer.cdash.org/favicon.ico" class="site-icon" width="32" height="32">

      <a href="https://slicer.cdash.org/viewBuildError.php?buildid=3679199" target="_blank" rel="noopener nofollow ugc">slicer.cdash.org</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.cdash.org/viewBuildError.php?buildid=3679199" target="_blank" rel="noopener nofollow ugc">CDash</a></h3>

  <p>
            CDash is an open source, web-based software testing server. CDash aggregates, analyzes, and displays the
            results of software testing processes submitted from clients located around the world. CDash is a part of a
           ...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @fedorov (2025-02-06 19:30 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> this must be something to do with the extensions build system. The extension has not been modified in a very long time.</p>
<p>Found this related discussion: <a href="https://discourse.slicer.org/t/slicerrt-build-fails-with-new-dcmtk/40177/5" class="inline-onebox">SlicerRT build fails with new DCMTK - #5 by cpinter</a>.</p>
<p>What should I make out of these cdash errors?</p>
<p><a href="https://slicer.cdash.org/viewBuildError.php?buildid=3680439">https://slicer.cdash.org/viewBuildError.php?buildid=3680439</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/453851e579f64a75244874918899a72562a4d758.png" data-download-href="/uploads/short-url/9SlBQ1dVKQC5mZMsCby4X2YePfq.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/453851e579f64a75244874918899a72562a4d758_2_690x437.png" alt="image" data-base62-sha1="9SlBQ1dVKQC5mZMsCby4X2YePfq" width="690" height="437" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/453851e579f64a75244874918899a72562a4d758_2_690x437.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/453851e579f64a75244874918899a72562a4d758_2_1035x655.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/453851e579f64a75244874918899a72562a4d758_2_1380x874.png 2x" data-dominant-color="E9EAEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2004×1270 196 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @jamesobutler (2025-02-06 19:33 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="3" data-topic="41521">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>The extension has not been modified in a very long time.</p>
</blockquote>
</aside>
<p>If the extension has not been modified in a very long time then it wouldn’t surprise me that changes to latest Slicer core dependencies or C++ standards results in the extension no longer building. Building the extension and issuing appropriate fixes would be necessary.</p>

---

## Post #5 by @fedorov (2025-02-06 19:34 UTC)

<p>Are there any dev guidances about updating extensions to account for any such changes?</p>

---

## Post #6 by @jamesobutler (2025-02-06 19:44 UTC)

<p>The SlicerRT post that you found seems relevant so I would suggest following the same resolution posted in that thread to PET DICOM. I assume it is also doing some linking against DCMTK?</p>

---

## Post #7 by @Mik (2025-02-07 11:16 UTC)

<p>Greetings,</p>
<p>I’ve made a <a href="https://github.com/QIICR/Slicer-PETDICOMExtension/pull/24" rel="noopener nofollow ugc">PR</a>. That’s a fix, similar to the SlicerRT linking problem, which appeared after DCMTK-3.6.8 update.</p>

---

## Post #8 by @fedorov (2025-02-07 14:41 UTC)

<p>Thank you <a class="mention" href="/u/mik">@Mik</a>! Hope this does it - I merged your PR.</p>

---
