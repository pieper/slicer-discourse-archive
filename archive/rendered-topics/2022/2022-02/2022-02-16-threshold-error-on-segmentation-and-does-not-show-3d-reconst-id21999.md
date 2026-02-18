# Threshold Error on segmentation and does not show 3D reconstruction

**Topic ID**: 21999
**Date**: 2022-02-16
**URL**: https://discourse.slicer.org/t/threshold-error-on-segmentation-and-does-not-show-3d-reconstruction/21999

---

## Post #1 by @Andreza (2022-02-16 17:30 UTC)

<p>Operating system: Windows 10 Pro<br>
Slicer version: 4.11.20210226</p>
<p>Hi, I did some segmentations on a TIFF file and obtained the 3D reconstruction of the structures.<br>
After some problems with the ruler bar (that I set after the segmentation), I tried to do a new segmentation with the same TIFF file, starting from the beggining.</p>
<p>I tried the segmenattion by threshold for 4 times, and the software returned with a failed segmentation (see picture), with some squares in the 2D images. Consequently, I couldn’t also get the 3D reconstruction when I press “Show 3D”</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/3682010fc9fe607d4d395645a9e7eb0d3391f191.jpeg" data-download-href="/uploads/short-url/7McjAIPQebe12ETAstqDDO8r97j.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3682010fc9fe607d4d395645a9e7eb0d3391f191_2_690x236.jpeg" alt="image" data-base62-sha1="7McjAIPQebe12ETAstqDDO8r97j" width="690" height="236" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3682010fc9fe607d4d395645a9e7eb0d3391f191_2_690x236.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3682010fc9fe607d4d395645a9e7eb0d3391f191_2_1035x354.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/3682010fc9fe607d4d395645a9e7eb0d3391f191.jpeg 2x" data-dominant-color="11110F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1377×471 77.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @muratmaga (2022-02-16 17:50 UTC)

<p><a class="mention" href="/u/andreza">@Andreza</a> can you provide screenshots of what the Volume Information is for your master volume that you used for segmentation and your segment geometry. For volume information go to volumes module and expand Volume Information tab get a screenshot and paste.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2875a970e3f272d10f07668ac115b6939c4be07.png" data-download-href="/uploads/short-url/nbNlmoDEUzOeVm2PnbPNHnrtlr1.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2875a970e3f272d10f07668ac115b6939c4be07_2_345x134.png" alt="image" data-base62-sha1="nbNlmoDEUzOeVm2PnbPNHnrtlr1" width="345" height="134" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2875a970e3f272d10f07668ac115b6939c4be07_2_345x134.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2875a970e3f272d10f07668ac115b6939c4be07_2_517x201.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2875a970e3f272d10f07668ac115b6939c4be07_2_690x268.png 2x" data-dominant-color="F0F0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1168×455 13.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
For segment geometry, click this button</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e379aab9360daee503dfe3b660afc973a4100c3.png" data-download-href="/uploads/short-url/21LOAG8uwBrdS8WeRTwHR9v9tx9.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0e379aab9360daee503dfe3b660afc973a4100c3_2_689x250.png" alt="image" data-base62-sha1="21LOAG8uwBrdS8WeRTwHR9v9tx9" width="689" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0e379aab9360daee503dfe3b660afc973a4100c3_2_689x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0e379aab9360daee503dfe3b660afc973a4100c3_2_1033x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0e379aab9360daee503dfe3b660afc973a4100c3_2_1378x500.png 2x" data-dominant-color="E9EDF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2461×895 198 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Andreza (2022-02-23 11:52 UTC)

<p>Hi, it goes</p>
<p>Volume information<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09cff0f7e1fd9d42a5e68845673d3ba54fe16afe.png" alt="image" data-base62-sha1="1oNObfaN6eqC033GCOvD6rzMjL0" width="499" height="291"></p>
<p>And segment geometry<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53283057c0e84855969e2d6cd104ec1e23695c6d.png" alt="image" data-base62-sha1="bRDJwppFwtCYnP4z8BXaKilFELz" width="493" height="287"></p>

---

## Post #4 by @muratmaga (2022-02-23 15:51 UTC)

<p>As you can see, they do not match, which suggest to me that you modified the image spacing value in your master volume after you created your segmentation object, as opposed to before.</p>
<p>So delete all the segmentation objects in your scene, right click on your volume and choose segment this, then proceed your segmentation.</p>
<p>Let us know if you encounter anymore issues.</p>

---

## Post #5 by @Andreza (2022-02-24 20:10 UTC)

<p>Yes, as I said, I modified the pixel size information after the segmentation was done, which I think, it explains the pixeled ROI or green quadrates.</p>
<p>I did more than 100 segmentations already.<br>
Because of this, I would use only the segmentations and their 3D reconstructions (without the ruler bar), but after some attempts to correct the ruler, the 3D reconstruction was gone (I only can observe the 2D images instead of 3D.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0d27ab4249474eb2c415e75feddff928aa9e9b1.jpeg" data-download-href="/uploads/short-url/mWHloCUULkGWQ8vR9Emb0V4dV6x.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a0d27ab4249474eb2c415e75feddff928aa9e9b1_2_690x334.jpeg" alt="image" data-base62-sha1="mWHloCUULkGWQ8vR9Emb0V4dV6x" width="690" height="334" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a0d27ab4249474eb2c415e75feddff928aa9e9b1_2_690x334.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a0d27ab4249474eb2c415e75feddff928aa9e9b1_2_1035x501.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a0d27ab4249474eb2c415e75feddff928aa9e9b1_2_1380x668.jpeg 2x" data-dominant-color="8B8C8C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1915×929 224 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @muratmaga (2022-02-24 22:52 UTC)

<p>You can use the method I described here to correctly scale your existing segmentations and your volumes.</p><aside class="quote quote-modified" data-post="23" data-topic="4656">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/ruler-in-orthographic-3d-view/4656/23">Ruler in (orthographic) 3D view</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    As you are observing, it is important to check that the imported image stack has the correct image spacing as the first step of your workflow. Since everything else (segmentations → models → measurements) are all dependent on this piece of information. This is especially true if you importing these images from 2D formats like PNG/TIFF etc which doesn’t preserve this information. 
You don’t have to redo the segmentation but it will take you a few steps to get them in correct alignment. This is wh…
  </blockquote>
</aside>


---
