---
topic_id: 26191
title: "How To Load Dicom Into Volumes From A Folder"
date: 2022-11-11
url: https://discourse.slicer.org/t/26191
---

# How to load dicom into volumes from a folder?

**Topic ID**: 26191
**Date**: 2022-11-11
**URL**: https://discourse.slicer.org/t/how-to-load-dicom-into-volumes-from-a-folder/26191

---

## Post #1 by @jay1987 (2022-11-11 08:05 UTC)

<p>i use the script in the document below<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3607ff86ad0cd5a2c9d71c2eeb7794054218d75.png" alt="image" data-base62-sha1="u9VuLPmAprvXr5c3ytOmC0jAkrb" width="537" height="117"><br>
and it has the error<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5fe1d34fdcc41110b431fa4bdaf5296ebedd7cc.png" data-download-href="/uploads/short-url/pXYRgiiI18h49RwQnEiLrBp7Tcg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5fe1d34fdcc41110b431fa4bdaf5296ebedd7cc.png" alt="image" data-base62-sha1="pXYRgiiI18h49RwQnEiLrBp7Tcg" width="690" height="118" data-dominant-color="1E1E1E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">966×166 5.54 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2022-11-11 14:53 UTC)

<p>The Slicer API is kept being improved. Therefore, if you use a code snippet from the script repository, make sure that you use examples that are for your Slicer version.</p>
<p>If you use the latest documentation (<a href="https://slicer.readthedocs.io/en/latest/">https://slicer.readthedocs.io/en/latest/</a>) then you need to use the latest Slicer Preview Release.</p>
<p>If you use a different Slicer version then choose the corresponding documentation version in the lower-left corner in documentation page:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f426a9fff820f911239a62446dbf17758ca6e61f.png" alt="image" data-base62-sha1="yPRl5zKMlspVoHvO61BVo2HyagT" width="569" height="204"></p>
<p>If you use the example corresponding to your Slicer version and you get an error such as <code>module 'slicer' has no attribute ...</code> then most likely you are not running the script in the Slicer application’s Python environment, but you are using the Python executable. The Python executable does not import any of the application classes, so features that depend on these classes, such as DICOM import/export are not available. You need to run your script in the Slicer application executable as shown <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#run-a-python-script-file-in-the-slicer-environment">here</a>.</p>

---

## Post #3 by @jay1987 (2022-11-13 00:55 UTC)

<p>thank you lassoan,but how to find the 4.11 version document now,the base framework we use is Slicer 4.11,it’s hard to change it to 5.x<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f156c91f31417bcc8a003df420b76d74e2d4fc7a.png" data-download-href="/uploads/short-url/yqZ0tK6LHkTxz8Y1ewvofZeobNM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f156c91f31417bcc8a003df420b76d74e2d4fc7a_2_690x341.png" alt="image" data-base62-sha1="yqZ0tK6LHkTxz8Y1ewvofZeobNM" width="690" height="341" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f156c91f31417bcc8a003df420b76d74e2d4fc7a_2_690x341.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f156c91f31417bcc8a003df420b76d74e2d4fc7a_2_1035x511.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f156c91f31417bcc8a003df420b76d74e2d4fc7a_2_1380x682.png 2x" data-dominant-color="E1E3E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1892×936 64.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2022-11-13 02:07 UTC)

<p>By using such an old version you are ignoring all our efforts that we invested into improving Slicer in the past few years. Please upgrade to the current stable version. If something prevents you from doing that then let us know, maybe we can help.</p>
<p>Before 4.13 we stored Slicer documentation on this wiki: <a href="https://www.slicer.org/wiki/Documentation/4.10/Developers">https://www.slicer.org/wiki/Documentation/4.10/Developers</a></p>

---

## Post #5 by @jay1987 (2022-11-13 02:12 UTC)

<p>thank you lassoan<br>
where can i find the slicer release note for every version?</p>

---

## Post #6 by @lassoan (2022-11-13 02:59 UTC)

<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/Slicer/Slicer/wiki/Release-Details">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Slicer/Slicer/wiki/Release-Details" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/53e49615eae99f6c43ed0812362a2832b50cc20ea4202b9f4c1371c812c74484/Slicer/Slicer" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/Slicer/Slicer/wiki/Release-Details" target="_blank" rel="noopener">Release Details · Slicer/Slicer Wiki</a></h3>

  <p>Multi-platform, free open source software for visualization and image computing. - Release Details · Slicer/Slicer Wiki</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
