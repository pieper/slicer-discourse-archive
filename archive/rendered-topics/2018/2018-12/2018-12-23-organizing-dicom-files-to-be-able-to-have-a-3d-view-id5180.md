# Organizing DICOM files to be able to have a 3D view

**Topic ID**: 5180
**Date**: 2018-12-23
**URL**: https://discourse.slicer.org/t/organizing-dicom-files-to-be-able-to-have-a-3d-view/5180

---

## Post #1 by @acfasano (2018-12-23 22:13 UTC)

<p>Operating system:Windows 10<br>
Slicer version:4.10<br>
Expected behavior: I received a bunch of dcm files. I importem them into SLICER but I cannot see the 3D view. One one of the series, the longitudinal view has images, but the other views seem to be onlly a single line. Some other series show only saggital view as being present. the other 02 views are lines.It seems to me that the images are there but SLICER cannot get the correct Saggital, coronal and Longitudinal views in Sync.  as anyone had this problem before ? HOw to solve it ?<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2018-12-23 22:41 UTC)

<p>Make sure to use the DICOM module to load your data (drag-and-drop the entire folder to the application window), import the folder, then load data from DICOM browser. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM" rel="nofollow noopener">DICOM module documentation</a> for details.</p>

---

## Post #3 by @acfasano (2019-01-02 18:07 UTC)

<p>Dear Andras.<br>
First of all let me wish you a wonderful 2019.<br>
On the problem at hand, I have already imported the files using the DICOM module, but for whatever reason, the images refuse to appear as a 3D view.<br>
Would you mind to take a look and let me know what is going on ?</p>
<p>The link below will download the folder with the images to your machine.<br>
Thanks<br>
Antonio</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/sh/ggusc69w7b0dqqt/AADfRKiQZcUQvENfdwl-oSCYa?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="" height="">

      <a href="https://www.dropbox.com/sh/ggusc69w7b0dqqt/AADfRKiQZcUQvENfdwl-oSCYa?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/logo_catalog/dropbox_webclip_200_vis.png" class="thumbnail" width="" height="">

<h3><a href="https://www.dropbox.com/sh/ggusc69w7b0dqqt/AADfRKiQZcUQvENfdwl-oSCYa?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox - File Deleted</a></h3>

  <p>Dropbox is a free service that lets you bring your photos, docs, and videos anywhere and share them easily. Never email yourself a file again!</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @lassoan (2019-01-02 19:21 UTC)

<p>The shared folder is empty. Please check.</p>

---

## Post #5 by @acfasano (2019-01-02 19:52 UTC)

<p>Hi, Andras,</p>
<p>Yes - You are right. My bad …<br>
Please check new link below.</p>
<p><em>(link removed as data set might have contained patient information)</em></p>
<p>Thanks<br>
Antonio</p>

---

## Post #6 by @lassoan (2019-01-02 20:28 UTC)

<p>While there were some warnings logged during data loading (<code>W: DcmItem: Length of element (7fe0,0010) is not a multiple of 2 (VR=OW)</code>) the volume ended up loading correctly:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1cd281b3916f925aeff5e26e1a5cb8d903d0e89.jpeg" data-download-href="/uploads/short-url/yv4CdQNtRyTCHr8ROVvTMWbiPi1.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f1cd281b3916f925aeff5e26e1a5cb8d903d0e89_2_672x499.jpeg" alt="image" data-base62-sha1="yv4CdQNtRyTCHr8ROVvTMWbiPi1" width="672" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f1cd281b3916f925aeff5e26e1a5cb8d903d0e89_2_672x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f1cd281b3916f925aeff5e26e1a5cb8d903d0e89_2_1008x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f1cd281b3916f925aeff5e26e1a5cb8d903d0e89_2_1344x998.jpeg 2x" data-dominant-color="575459"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1668×1240 344 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Note that you need to use Volume Rendering module if you want to see the image in the 3D view.</p>

---

## Post #7 by @lassoan (2019-01-02 20:33 UTC)

<p>You can also use Segment Editor module and its Threshold effect, followed by Islands effect / Split islands to segments to create a segmented model that can be shown in 3D:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/387fe57ad59d7ef5fb7f4ab0b18a04d1415cc2fb.jpeg" data-download-href="/uploads/short-url/83OKOIGYHvKYaNdBeQO3TLjLkn1.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/387fe57ad59d7ef5fb7f4ab0b18a04d1415cc2fb_2_690x421.jpeg" alt="image" data-base62-sha1="83OKOIGYHvKYaNdBeQO3TLjLkn1" width="690" height="421" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/387fe57ad59d7ef5fb7f4ab0b18a04d1415cc2fb_2_690x421.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/387fe57ad59d7ef5fb7f4ab0b18a04d1415cc2fb_2_1035x631.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/387fe57ad59d7ef5fb7f4ab0b18a04d1415cc2fb_2_1380x842.jpeg 2x" data-dominant-color="A2A3A4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1376 482 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
