# saggital and coronal views not loading 

**Topic ID**: 2818
**Date**: 2018-05-14
**URL**: https://discourse.slicer.org/t/saggital-and-coronal-views-not-loading/2818

---

## Post #1 by @Sydney_Brannoch (2018-05-14 19:56 UTC)

<p>Hello!</p>
<p>I am new to 3D slicer and have tried to upload my micro-CT dataset after successfully following a tutorial using pre-loaded data. I am unable to load saggital and coronal views of the dataset however. When I have tried uploading this data into Amira, it worked beautifully, however I no longer have access to that software. Any help would be appreciated-- I would like to get to segmenting!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1aa3b5c9ce4b6be34659bb24f86a5668c70be54.png" data-download-href="/uploads/short-url/rDeS3FkmdVbWYxqlNRubqwyoq6o.png?dl=1" title="3d%20slicer%20error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1aa3b5c9ce4b6be34659bb24f86a5668c70be54_2_690x388.png" alt="3d%20slicer%20error" data-base62-sha1="rDeS3FkmdVbWYxqlNRubqwyoq6o" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1aa3b5c9ce4b6be34659bb24f86a5668c70be54_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1aa3b5c9ce4b6be34659bb24f86a5668c70be54_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1aa3b5c9ce4b6be34659bb24f86a5668c70be54_2_1380x776.png 2x" data-dominant-color="A7A9AD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3d%20slicer%20error</span><span class="informations">1920×1080 185 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @jcfr (2018-05-15 18:10 UTC)

<p>It looks like only one slice of the volume was loaded. What are the dimension if you open the <code>Volumes</code> module and look at the information ?</p>
<p>I suggest you try to load the data by unchecking the “single file” option. See this page for more details: <a href="https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/LoadingData#Show_Options">https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/LoadingData#Show_Options</a></p>

---
