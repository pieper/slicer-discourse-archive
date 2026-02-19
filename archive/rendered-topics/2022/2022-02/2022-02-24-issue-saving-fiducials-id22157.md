---
topic_id: 22157
title: "Issue Saving Fiducials"
date: 2022-02-24
url: https://discourse.slicer.org/t/22157
---

# Issue saving fiducials

**Topic ID**: 22157
**Date**: 2022-02-24
**URL**: https://discourse.slicer.org/t/issue-saving-fiducials/22157

---

## Post #1 by @anromero (2022-02-24 14:43 UTC)

<p>I’ve been using 3D Slicer for a while, but I noticed that last time I opened it and tried landmarking specimens that there is no “Export as…” option when I right click on the markups in the data or markups module. I noticed this started happening after I updated to version 4.11.20210226. Is this no longer an option for exporting markups as .fcsv? It seems that the only way I can do it is to use the save icon in the top left corner, and when I do that it says that there is some sort of error.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/663a91ef650dd7bceef8f8407e11a1152fa9dd11.png" data-download-href="/uploads/short-url/eAmbDKag9K59oInhveoR3FXMQ3T.png?dl=1" title="Screen Shot 2022-02-24 at 8.37.29 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/663a91ef650dd7bceef8f8407e11a1152fa9dd11_2_690x343.png" alt="Screen Shot 2022-02-24 at 8.37.29 AM" data-base62-sha1="eAmbDKag9K59oInhveoR3FXMQ3T" width="690" height="343" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/663a91ef650dd7bceef8f8407e11a1152fa9dd11_2_690x343.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/663a91ef650dd7bceef8f8407e11a1152fa9dd11_2_1035x514.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/663a91ef650dd7bceef8f8407e11a1152fa9dd11.png 2x" data-dominant-color="EBEEF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-02-24 at 8.37.29 AM</span><span class="informations">1052×524 70 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jamesobutler (2022-02-24 14:46 UTC)

<p>“Export as…” was previously available as part of the SlicerMorph extension. It was recently <a href="https://github.com/SlicerMorph/SlicerMorph/commit/56ca0f827c3999dc547f726d46db3fff506602a1" rel="noopener nofollow ugc">removed</a> from SlicerMorph because the feature is now available in the latest Slicer Preview. Since SlicerMorph specifies to the use latest version of its extension in both Slicer stable (4.11.20210226) and latest Slicer Preview that means “Export As…” is no longer available from SlicerMorph when using Slicer stable. You will need to switch to using latest Slicer Preview available from <a href="https://download.slicer.org/" rel="noopener nofollow ugc">https://download.slicer.org/</a>.</p>

---

## Post #3 by @muratmaga (2022-02-24 15:30 UTC)

<aside class="quote no-group" data-username="anromero" data-post="1" data-topic="22157">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/anromero/48/10120_2.png" class="avatar"> anromero:</div>
<blockquote>
<p>I can do it is to use the save icon in the top left corner, and when I do that it says that there is some sort of error.</p>
</blockquote>
</aside>
<p>That’s is really not an error, but a warning about the pitfalls of fcsv format, and that you should probably be careful with it.</p>
<p>There will soon be a new stable release of Slicer, which will be based on the current preview. We have done a lot of additions to the markup module (iincluding a new toolbar and additional features to support LM templates, missing points etc). I think you will find beneficial switching to the preview version. While doing that also consider, whether you want to start saving your markups in JSON format. Because some of the new features (LM state, placed) are not fully supported in fcsv.</p>
<p>You don’t have to do the transition immediately, but seeing that you are actively collecting lots of data, you should consider whether you want to stick with an old format that might give you problems in few years, or switch now.</p>
<p>In SlicerMorphR we support loading JSON format into R as easily as fcsv, so from that end that is entirely transparent.</p>

---
