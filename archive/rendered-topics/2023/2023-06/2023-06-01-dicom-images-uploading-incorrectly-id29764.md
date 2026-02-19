---
topic_id: 29764
title: "Dicom Images Uploading Incorrectly"
date: 2023-06-01
url: https://discourse.slicer.org/t/29764
---

# DICOM Images Uploading Incorrectly

**Topic ID**: 29764
**Date**: 2023-06-01
**URL**: https://discourse.slicer.org/t/dicom-images-uploading-incorrectly/29764

---

## Post #1 by @Owen_Baenen (2023-06-01 00:09 UTC)

<p>Hello! I have a set of cardiac MRI data that I want to import into Slicer3D for left ventricle segmentation and then exporting a surface 3d model .stl.</p>
<p>I have individual DICOM folders containing all of the DICOM images for each timestep because I want to do surface reconstruction analysis independently for each timestep.</p>
<p>Here is a dropbox link to the folder for the first timestep ‘t1’ containing 20 anonymized MRI images, 14 from the short view, 3 from a 2 chamber long view, and 3 from a 4 chamber long view.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/sh/e2onhx0w904nzbs/AACjd5UJW_L2dnuP1LcoCdCga?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon.ico" class="site-icon" width="" height="">

      <a href="https://www.dropbox.com/sh/e2onhx0w904nzbs/AACjd5UJW_L2dnuP1LcoCdCga?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/metaserver/static/images/opengraph/opengraph-content-icon-folder-dropbox-landscape.png" class="thumbnail" width="" height="">

<h3><a href="https://www.dropbox.com/sh/e2onhx0w904nzbs/AACjd5UJW_L2dnuP1LcoCdCga?dl=0" target="_blank" rel="noopener nofollow ugc">t1</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>when I load this folder directly using the DICOM importer I get a view that looks like this,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6ba1186879801f2a9fb76b25e3be0aae1f37916.png" data-download-href="/uploads/short-url/nMVUpLEOvujQIlKbf2jbjnwyzC6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6ba1186879801f2a9fb76b25e3be0aae1f37916_2_690x476.png" alt="image" data-base62-sha1="nMVUpLEOvujQIlKbf2jbjnwyzC6" width="690" height="476" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6ba1186879801f2a9fb76b25e3be0aae1f37916_2_690x476.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6ba1186879801f2a9fb76b25e3be0aae1f37916.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6ba1186879801f2a9fb76b25e3be0aae1f37916.png 2x" data-dominant-color="3D3D46"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">999×690 81.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I tried to use the DICOM patcher to make the series ID’s uniform and correct inconsistencies. This is what the view looked like then<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5f76a076cef63af498f8c37ed9be5a21ba0cd10.png" data-download-href="/uploads/short-url/pXKvhB7p57eXZd952xsQ2DeUaxG.png?dl=1" title="patchedDataSlicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b5f76a076cef63af498f8c37ed9be5a21ba0cd10_2_690x477.png" alt="patchedDataSlicer" data-base62-sha1="pXKvhB7p57eXZd952xsQ2DeUaxG" width="690" height="477" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b5f76a076cef63af498f8c37ed9be5a21ba0cd10_2_690x477.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5f76a076cef63af498f8c37ed9be5a21ba0cd10.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5f76a076cef63af498f8c37ed9be5a21ba0cd10.png 2x" data-dominant-color="3C3C45"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">patchedDataSlicer</span><span class="informations">999×691 77.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This also did not work. But I am very new to slicer3D and am not sure if I’m missing something</p>
<p>Usually one plane view looks good and I am able to traverse all the slices in that plane, however the other two planes are cropped and irregular and cannot be segmented.</p>
<p>I want to get a view where the short view, 2 chamber, and 4 chamber views are represented in each of the 3 screens and segment each individually to extract a volume/surface generation.</p>
<p>Wondering if anybody has had similar issues? or could help?<br>
Thank you!</p>

---
