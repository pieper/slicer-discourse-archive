---
topic_id: 5030
title: "2D Ultrasound Dicom Measurement Units"
date: 2018-12-10
url: https://discourse.slicer.org/t/5030
---

# 2D Ultrasound Dicom Measurement Units

**Topic ID**: 5030
**Date**: 2018-12-10
**URL**: https://discourse.slicer.org/t/2d-ultrasound-dicom-measurement-units/5030

---

## Post #1 by @MGH_CURT (2018-12-10 15:48 UTC)

<p>Operating system: Windows 10</p>
<p>Slicer version: 4.8.1</p>
<p>Expected behavior: When reading <strong>ultrasound</strong> dicom images to perform measurements, Slicer should read in the dicom metadata’s SequenceOfUltrasoundRegions.Item_1.PhysicalDeltaX to reflect pixel to actual cm/mm values.</p>
<p>Actual behavior: When reading <strong>ultrasound</strong> dicom images to perform measurements, Slicer is reading pixel distance instead, outputting significantly different number when measuring.</p>
<p>Manual adjustment for each us dicom image is possible by tweaking the settings of the coefficient for the length measurement. However, it is cumbersome and we believe it is an easy fix for the Slicer development team to adjust measurement units for ultrasound dicom files accordingly. In the Dropbox link below are 5 anonymized ultrasound dicom files for testing.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/sh/26ity4rabrpdeyd/AADNhZ5eixHuMGHrevMt933La?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="" height="">

      <a href="https://www.dropbox.com/sh/26ity4rabrpdeyd/AADNhZ5eixHuMGHrevMt933La?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/metaserver/static/images/spectrum-icons/generated/content/content-folder_dropbox-large.png" class="thumbnail" width="" height="">

<h3><a href="https://www.dropbox.com/sh/26ity4rabrpdeyd/AADNhZ5eixHuMGHrevMt933La?dl=0" target="_blank" rel="noopener nofollow ugc">slicer_forum_anon</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Thanks! <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>

---
