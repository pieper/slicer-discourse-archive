---
topic_id: 20359
title: "New Physician Annotated Dcm Files Not Loading"
date: 2021-10-26
url: https://discourse.slicer.org/t/20359
---

# New physician-annotated .dcm files not loading

**Topic ID**: 20359
**Date**: 2021-10-26
**URL**: https://discourse.slicer.org/t/new-physician-annotated-dcm-files-not-loading/20359

---

## Post #1 by @BoneArtist (2021-10-26 11:47 UTC)

<p>The original .dcm files work fine, but my client recently annotated new versions of the study with color demarcations. Although these new versions are also .dcm files, they will not load as a scalar volume.<br>
The originals were 130KB in size while the new (non-loadable) versions are 4,129K in size.<br>
Thanks for any ideas. The client isn’t able to describe anything he might have done differently.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c67a7c1ff6e5b16b20cc43d29a31ec5770a85aea.jpeg" data-download-href="/uploads/short-url/sjOXCZDjVp1giz9dV9J5QZdu78u.jpeg?dl=1" title="sample_IM-0001-0056" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c67a7c1ff6e5b16b20cc43d29a31ec5770a85aea_2_690x482.jpeg" alt="sample_IM-0001-0056" data-base62-sha1="sjOXCZDjVp1giz9dV9J5QZdu78u" width="690" height="482" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c67a7c1ff6e5b16b20cc43d29a31ec5770a85aea_2_690x482.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c67a7c1ff6e5b16b20cc43d29a31ec5770a85aea_2_1035x723.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c67a7c1ff6e5b16b20cc43d29a31ec5770a85aea_2_1380x964.jpeg 2x" data-dominant-color="2B2B2A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sample_IM-0001-0056</span><span class="informations">1418×991 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18f0f94728642211c61e94a75f03e0c36bae6b45.png" alt="slicer error message" data-base62-sha1="3yDK4FVIcQTLVl8eAcsJ6I4t79z" width="500" height="105"></p>

---

## Post #2 by @lassoan (2021-10-26 11:57 UTC)

<p>As described in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#images">documentation</a>, you need to install QuantitiveReporting or SlicerRT extension to import DICOM Segmentation Object or DICOM RT structure set information objects.</p>
<p>We know we cannot expect users to read documentation, so we added an informational message that tells this during DICOM import, but probably it is not the right time (users just click on it and don’t realize that the error that they get during loading is related). We are going to improve this, see details here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/4753">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/4753" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/4753" target="_blank" rel="noopener">Advise users which extensions to install to load special file or DICOM formats</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-21" data-time="00:44:10" data-timezone="UTC">12:44AM - 21 Mar 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:enhancement
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          priority:low
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Users often don't know that Slicer can load additional type of file formats and <span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">DICOM files if they install extensions.

Slicer should recommend users to install applicable extensions and allow automatic installation by a few clicks.

Extensions could declare what kind of file formats and DICOM files it can load (or save) in their s4ext file.

See related discussion here: https://github.com/Slicer/Slicer/issues/4678</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @BoneArtist (2021-10-28 21:55 UTC)

<p>Thanks! I discovered that turning the images into grayscale with Gimp and overwriting them allowed them to be imported. Photoshop also allowed grayscale, but my metadata was altered in odd ways. They appear to have 1mm spacing now instead of 1.2mm, but I can fix in Blender for this task to segment a tumor.</p>

---

## Post #4 by @lassoan (2021-10-29 02:11 UTC)

<p>General-purpose image processing applications, such as Gimp, Photoshop, or Blender are OK to use for final editing of DICOM images for publishing or presentations. However, they are expected to cause random data loss/corruption in any exported medical image metadata, which may not even be immediately obvious. Therefore, never even consider using images processed in general-purpose artistic image editing software for any medical image computing applications.</p>

---
