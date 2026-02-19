---
topic_id: 13739
title: "Segment Registration And Transformation"
date: 2020-09-29
url: https://discourse.slicer.org/t/13739
---

# Segment registration and transformation

**Topic ID**: 13739
**Date**: 2020-09-29
**URL**: https://discourse.slicer.org/t/segment-registration-and-transformation/13739

---

## Post #1 by @Pratik (2020-09-29 01:24 UTC)

<p>Dear all,</p>
<p>I am trying to register two geometries in slicer (image attached below) where red is defined as the fixed geometry and grey as moving geometry.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/aed096fd68e85a3411c753ac23c9a3deae347397.png" data-download-href="/uploads/short-url/oWtYQHDqn24po0xQtCSyWydKIWX.png?dl=1" title="segments" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/aed096fd68e85a3411c753ac23c9a3deae347397_2_487x500.png" alt="segments" data-base62-sha1="oWtYQHDqn24po0xQtCSyWydKIWX" width="487" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/aed096fd68e85a3411c753ac23c9a3deae347397_2_487x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/aed096fd68e85a3411c753ac23c9a3deae347397_2_730x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/aed096fd68e85a3411c753ac23c9a3deae347397_2_974x1000.png 2x" data-dominant-color="958EBC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segments</span><span class="informations">1223×1254 87.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I perform the registration, the end result is multiple transforms (also attached for reference)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36fbc510c8e9285784dd186e8a76b9181fceb198.png" data-download-href="/uploads/short-url/7QpcfU5HfhCkRvjHLo11dwde79K.png?dl=1" title="postregistration" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/36fbc510c8e9285784dd186e8a76b9181fceb198_2_544x500.png" alt="postregistration" data-base62-sha1="7QpcfU5HfhCkRvjHLo11dwde79K" width="544" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/36fbc510c8e9285784dd186e8a76b9181fceb198_2_544x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36fbc510c8e9285784dd186e8a76b9181fceb198.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36fbc510c8e9285784dd186e8a76b9181fceb198.png 2x" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">postregistration</span><span class="informations">613×563 47.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then I use the transform module to check if the registration has been correctly. I have started off with both geometries and tried different orders of the transformation (in combination with hardening transform) but the two geometries do not seem to overlap. My question is whether the registration has taken all three listed transforms into account and if my method of checking the registration using transform module is correct? Any help/suggestions would be appreciated.</p>
<p>Regards</p>
<p>Pratik</p>

---

## Post #2 by @Andinet_Enquobahrie (2020-09-29 11:46 UTC)

<p><a class="mention" href="/u/pratik">@Pratik</a></p>
<p>Please let us know which module you used to do this registration.</p>
<p>Andinet</p>

---

## Post #3 by @Pratik (2020-09-29 11:51 UTC)

<p>Dear Andinet,</p>
<p>I am using the segment registration module from silcer</p>

---

## Post #4 by @cpinter (2020-09-29 12:16 UTC)

<p>Hi <a class="mention" href="/u/pratik">@Pratik</a>,</p>
<p>I am fairly certain that the transformations are independent, i.e. the BSpline deformable and the affine transform are not related, but can be set independently. This means that if you set the <code>Deformable Transform</code> to the moving volume / segmentation, then the result should be applied correctly.</p>
<p>It’s another question if the result is good or not. You can debug where it went wrong by checking the <code>Keep intermediate nodes</code> checkbox and visualizing the results. There are two distance map images that are generated from the two segments on the geometry of the input images (that’s why you need to also specify the volumes that the segmentations correspond to!), and are registered using different methods (i.e. the affine and deformable BSpline). Try to show these distance maps on top of each other (set the moving one as foreground and set opacity to 0.5), and apply the result transformation on the moving one. We can go from here.</p>

---

## Post #5 by @Pratik (2020-09-29 14:28 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> sorry but I do not understand when you say visualising distance maps. Where do I do this from? I can visualise the intermediate geometries and also apply the transform to the moving model.</p>

---

## Post #6 by @cpinter (2020-09-29 14:58 UTC)

<p>If you turn on the option I mentioned then a lot of extra objects show up in the Data module. Two modules there will be the distance maps. You can identify them by name</p>

---

## Post #7 by @Andinet_Enquobahrie (2020-09-29 14:59 UTC)

<p>The registration approach implemented in the Segmentation Registration Module involves several steps (hence you will see several intermediate results generated). You might want to take a look at the code to understand the approach better</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerRt/SegmentRegistration/blob/master/SegmentRegistration/SegmentRegistration.py#L365-L372" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SegmentRegistration/blob/master/SegmentRegistration/SegmentRegistration.py#L365-L372" target="_blank" rel="noopener nofollow ugc">SlicerRt/SegmentRegistration/blob/master/SegmentRegistration/SegmentRegistration.py#L365-L372</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="365" style="counter-reset: li-counter 364 ;">
<li>#------------------------------------------------------------------------------
</li>
<li>def performRegistration(self):
</li>
<li>  logging.info('Performing registration workflow')
</li>
<li>  self.cropMovingVolume()
</li>
<li>  self.preAlignSegmentations()
</li>
<li>  self.resampleFixedVolume()
</li>
<li>  self.createContourLabelmaps()
</li>
<li>  return self.performDistanceBasedRegistration()
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>The last step uses the distance map based registration implementation in SlicerProstate extension</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://www.slicer.org/w/img_auth.php/6/64/Favicon.ico" class="site-icon" width="15" height="15">
      <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DistanceMapBasedRegistration" target="_blank" rel="noopener nofollow ugc">slicer.org</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="15" height="15">

<h3><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DistanceMapBasedRegistration" target="_blank" rel="noopener nofollow ugc">Documentation/Nightly/Modules/DistanceMapBasedRegistration - Slicer Wiki</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Andinet</p>

---

## Post #8 by @Pratik (2020-09-29 15:51 UTC)

<p>Hi <a class="mention" href="/u/cpinter">@cpinter</a>, I can see the two distance maps (volume) under data but cant visualise them in the 3d viewer. I only see a set of geometries presumably including the one at intermediate step.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc31fcbe88ed83a8d9cf0069b5a00d06ad16bf84.png" data-download-href="/uploads/short-url/zZ1q1KRGLNGGL3EZ9JUV3pfg1AU.png?dl=1" title="distancemap" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc31fcbe88ed83a8d9cf0069b5a00d06ad16bf84_2_690x483.png" alt="distancemap" data-base62-sha1="zZ1q1KRGLNGGL3EZ9JUV3pfg1AU" width="690" height="483" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc31fcbe88ed83a8d9cf0069b5a00d06ad16bf84_2_690x483.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc31fcbe88ed83a8d9cf0069b5a00d06ad16bf84.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc31fcbe88ed83a8d9cf0069b5a00d06ad16bf84.png 2x" data-dominant-color="F4F4F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">distancemap</span><span class="informations">909×637 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21e4875cf3ae6ed340943fc272b9a432dfa6a91d.png" data-download-href="/uploads/short-url/4PPnnITC2GnfX5RZpWWto2qzSep.png?dl=1" title="intermediate" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21e4875cf3ae6ed340943fc272b9a432dfa6a91d_2_690x461.png" alt="intermediate" data-base62-sha1="4PPnnITC2GnfX5RZpWWto2qzSep" width="690" height="461" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21e4875cf3ae6ed340943fc272b9a432dfa6a91d_2_690x461.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21e4875cf3ae6ed340943fc272b9a432dfa6a91d_2_1035x691.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21e4875cf3ae6ed340943fc272b9a432dfa6a91d_2_1380x922.png 2x" data-dominant-color="9799BF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">intermediate</span><span class="informations">1979×1325 221 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @Pratik (2020-09-29 15:52 UTC)

<p>Thanks for the code, I will look into this as well</p>

---

## Post #10 by @Pratik (2020-09-30 03:14 UTC)

<p>I could visualise the distance map (both fixed and moving) volume using volume rendering but for some reason it seems the scale of the two distance maps are off by quite a lot. Is this expected?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aad1bf04a75b37b47e6067ed91d2816f49412f3e.jpeg" data-download-href="/uploads/short-url/on8y2ANZKb122eJtAG2cXKRLkJM.jpeg?dl=1" title="distancemaps.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aad1bf04a75b37b47e6067ed91d2816f49412f3e_2_495x500.jpeg" alt="distancemaps.PNG" data-base62-sha1="on8y2ANZKb122eJtAG2cXKRLkJM" width="495" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aad1bf04a75b37b47e6067ed91d2816f49412f3e_2_495x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aad1bf04a75b37b47e6067ed91d2816f49412f3e_2_742x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aad1bf04a75b37b47e6067ed91d2816f49412f3e_2_990x1000.jpeg 2x" data-dominant-color="66667D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">distancemaps.PNG</span><span class="informations">1388×1402 205 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #11 by @labixin (2020-10-21 05:03 UTC)

<p>Hi all,</p>
<p>I am now using segment registration extension. I would like to refer to the tutorial. However, the <strong>SlicerRT_Tutorial_MRI-US-ProstateContourPropagation.pptx</strong> (<a href="https://github.com/SlicerRt/SlicerRtDoc/blob/master/tutorials/SlicerRT_Tutorial_MRI-US-ProstateContourPropagation.pptx" rel="noopener nofollow ugc">https://github.com/SlicerRt/SlicerRtDoc/blob/master/tutorials/SlicerRT_Tutorial_MRI-US-ProstateContourPropagation.pptx</a>) cannot be downloaded.</p>
<p>Is there something wrong? Hope for some advice. Thanks a lot!</p>
<p>Sincerely,</p>
<p>Crayon</p>

---

## Post #12 by @lassoan (2020-10-21 05:40 UTC)

<p>Click on the “Download” button on the page.</p>

---
