# Slicer elastix on Mac

**Topic ID**: 5434
**Date**: 2019-01-21
**URL**: https://discourse.slicer.org/t/slicer-elastix-on-mac/5434

---

## Post #1 by @Mel (2019-01-21 04:36 UTC)

<p>Hi<br>
I cannot get sequence registration module to work on MAc. I am using slicer 4.10 and installed elastix separately and tried specifying the path on general registration. Could you please help. Thanks</p>

---

## Post #2 by @cpinter (2019-02-21 15:02 UTC)

<p>Sorry for the super late answer!</p>
<p>Unfortunately we don’t have an Elastix for Mac due to technical issues for a while now, see</p><aside class="quote" data-post="1" data-topic="4531">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicerelastix-extension-not-available-on-mac/4531">SlicerElastix extension not available on Mac</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi all, 
I wanted to show a Mac user the SlicerElastix extension but it was not there. After a bit of investigation, it turns out that it does not build at least since February. 
Here’s the <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=label&amp;compare1=63&amp;value1=Elastix">latest dashboard</a> and the <a href="http://slicer.cdash.org/viewBuildError.php?buildid=1411238">error</a> (and the <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2018-02-17&amp;filtercount=1&amp;showfilters=1&amp;field1=label&amp;compare1=63&amp;value1=Elastix">oldest available dashboard</a>). 
Does anyone know what is needed in order to fix this? Can someone who usually develops on Mac check it out? Elastix is a great registration tool, we should have it in 4.10. 
Thanks, 
csaba
  </blockquote>
</aside>

<p>We’re doing our best to fix it.</p>

---

## Post #3 by @cpinter (2019-02-21 15:15 UTC)

<p>I’m sorry it seems that the Mac build is fine now. Please try <a href="http://slicer.kitware.com/midas3/api/rest?method=midas.bitstream.download&amp;name=Slicer-4.11.0-2019-02-18-macosx-amd64.dmg&amp;checksum=4c9302df4c6e3b60b012249722b72e88" rel="nofollow noopener">this nightly package</a>.</p>

---

## Post #4 by @Alex_Vergara (2019-02-21 15:46 UTC)

<p>It is working on stable now, confirmed on Mac 10.14<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/3924972cced7a7017541540425e201e863bcbebe.png" alt="imagen" data-base62-sha1="89vBRnaBbFhODfFaBYKRe24607Y" width="586" height="350"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc2c7aaf7174dfbcdafcf829981d1f3f801dd6a8.png" data-download-href="/uploads/short-url/t8cHpXM5VpQF92w9ybb32fZhMDe.png?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc2c7aaf7174dfbcdafcf829981d1f3f801dd6a8_2_504x500.png" alt="imagen" data-base62-sha1="t8cHpXM5VpQF92w9ybb32fZhMDe" width="504" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc2c7aaf7174dfbcdafcf829981d1f3f801dd6a8_2_504x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc2c7aaf7174dfbcdafcf829981d1f3f801dd6a8.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc2c7aaf7174dfbcdafcf829981d1f3f801dd6a8.png 2x" data-dominant-color="EBEBEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">565×560 51.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
