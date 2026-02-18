# Tractography - bad quality

**Topic ID**: 6191
**Date**: 2019-03-18
**URL**: https://discourse.slicer.org/t/tractography-bad-quality/6191

---

## Post #1 by @eNable_Polska (2019-03-18 13:08 UTC)

<p>I<code>d like to ask you about resolution of my images. Sorry about my English We take MRI with tractography, GE machine. I saw the tractography made of this research and it looked good. I</code>d like to build it in slicer, but I cant.<br>
I import data without any problems, I use converter DICOM-NRRD from DRMI package, save data as nrrd. I followed the tutorial “how to ….”<br>
I have a problem with image resolution. I tried different directions COR, AX, SAG without success.<br>
Here is link to data series (anonymised) <a href="https://www.dropbox.com/s/xitd0i1kbhf8j1n/DWI_DICOM.zip?dl=0" class="inline-onebox" rel="noopener nofollow ugc">Dropbox - File Deleted - Simplify your life</a><br>
and screenshot from slicer<br>
Could you help me and tell how to improve quality of tractography?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7aa516e67f422b2dca439e7fbc93b3a52a6c3db.png" data-download-href="/uploads/short-url/zkWQ548DxfGcQ6Snz6DZrlTOfFN.png?dl=1" title="2019-03-17-Scene" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7aa516e67f422b2dca439e7fbc93b3a52a6c3db_2_690x457.png" alt="2019-03-17-Scene" data-base62-sha1="zkWQ548DxfGcQ6Snz6DZrlTOfFN" width="690" height="457" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7aa516e67f422b2dca439e7fbc93b3a52a6c3db_2_690x457.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7aa516e67f422b2dca439e7fbc93b3a52a6c3db_2_1035x685.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7aa516e67f422b2dca439e7fbc93b3a52a6c3db_2_1380x914.png 2x" data-dominant-color="62637D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2019-03-17-Scene</span><span class="informations">1393×924 159 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @eNable_Polska (2019-03-18 19:29 UTC)

<p>Grrrrr, I send bad exam, this is correct</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/s/jpxzpqzeyndykfc/Exam.zip?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="" height="">

      <a href="https://www.dropbox.com/s/jpxzpqzeyndykfc/Exam.zip?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/logo_catalog/dropbox_webclip_200_vis.png" class="thumbnail" width="" height="">

<h3><a href="https://www.dropbox.com/s/jpxzpqzeyndykfc/Exam.zip?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox - File Deleted</a></h3>

  <p>Dropbox is a free service that lets you bring your photos, docs, and videos anywhere and share them easily. Never email yourself a file again!</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
Sorry</p>

---

## Post #3 by @ljod (2019-04-02 19:17 UTC)

<p>Hello. I’m sorry about the late response. The reason this has happened is most likely that DWIConvert is not properly handling your diffusion MRI scan. We have a new module that will be available to use the DCM2nii tool within Slicer. This will become available in the nightly build version of Slicer. However, there have been some internal code updates to Slicer so we need to adapt SlicerDMRI to these for it to become available again in the nightly.</p>
<p>In the meantime, it is possible to use the software dcm2niix to convert from a large variety of DWI DICOM files to nifti and now also nrrd formats. Please see more information from Chris_Rorden here:</p><aside class="quote quote-modified" data-post="17" data-topic="4793">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/bc79bd/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/not-working-dwi-component/4793/17">Not working "DWI Component"</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I converted dicom format in nii. Uploaded new images. This format is not set on the panel in the program How to convert now to nrrd? (DiconToNrrd? FSLToNrrd?) 
[image]
  </blockquote>
</aside>


---
