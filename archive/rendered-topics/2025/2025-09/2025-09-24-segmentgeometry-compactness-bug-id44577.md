# SegmentGeometry compactness bug?

**Topic ID**: 44577
**Date**: 2025-09-24
**URL**: https://discourse.slicer.org/t/segmentgeometry-compactness-bug/44577

---

## Post #1 by @cliftong (2025-09-24 21:41 UTC)

<p>Hi <a class="mention" href="/u/jmhuie">@jmhuie</a> ! I have a weird behavior happening with SegmentGeometry that I’m hoping you can help me understand.</p>
<p>We are calculating the cross-sectional area and properties of a segment with slices aligned with the green view and setting a custom neutral axis (90 degrees). We set our slices to 1% (which results in 101 data rows).</p>
<p>However, we’d also like to calculate the compactness of each slice. When we add in the compactness measurement, our output is now 201 rows and the calculated compactness value is 1 in every row (which it very clearly should not be). Here’s are two images of the segment in the green window (at two different slice locations):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/958c91faed7375758632a65cdfb3cba80ffd7560.png" data-download-href="/uploads/short-url/lkYjqQIWtryvRCDteIxHcJTcGIw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/958c91faed7375758632a65cdfb3cba80ffd7560.png" alt="image" data-base62-sha1="lkYjqQIWtryvRCDteIxHcJTcGIw" width="303" height="223"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">404×298 39.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f1ae9af8e3d108205d8337df2e7df730dc87b87.png" data-download-href="/uploads/short-url/mHvzQVnZppTu9Gm2U7kiSuqho1h.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f1ae9af8e3d108205d8337df2e7df730dc87b87.png" alt="image" data-base62-sha1="mHvzQVnZppTu9Gm2U7kiSuqho1h" width="303" height="224"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">404×299 42.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The data output we get when we select compactness:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/1466a9ecde92b80eb065e2111e08de8c5bae771e.png" data-download-href="/uploads/short-url/2UtvleimBJVJnUyQz4XZKwnDN8O.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/1466a9ecde92b80eb065e2111e08de8c5bae771e_2_517x110.png" alt="image" data-base62-sha1="2UtvleimBJVJnUyQz4XZKwnDN8O" width="517" height="110" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/1466a9ecde92b80eb065e2111e08de8c5bae771e_2_517x110.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/1466a9ecde92b80eb065e2111e08de8c5bae771e_2_775x165.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/1466a9ecde92b80eb065e2111e08de8c5bae771e_2_1034x220.png 2x" data-dominant-color="EEE9D9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1125×241 51 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And some of the python output that seems to show some struggles:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/1294eb1a2f89040a750b6663143a2d84a8fcb9cf.png" data-download-href="/uploads/short-url/2EnEkUmQ5dQ8NDX2ZOVLAM3THhd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/1294eb1a2f89040a750b6663143a2d84a8fcb9cf_2_690x198.png" alt="image" data-base62-sha1="2EnEkUmQ5dQ8NDX2ZOVLAM3THhd" width="690" height="198" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/1294eb1a2f89040a750b6663143a2d84a8fcb9cf_2_690x198.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/1294eb1a2f89040a750b6663143a2d84a8fcb9cf_2_1035x297.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/1294eb1a2f89040a750b6663143a2d84a8fcb9cf.png 2x" data-dominant-color="FEF6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1215×349 96.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any idea what could be going wrong? I’ve tried this in 3 different versions of Slicer in case there was a compatibility issue (results here shown for 5.9.0-2025-09-23).</p>
<p>Thanks!</p>

---

## Post #2 by @muratmaga (2025-09-24 22:10 UTC)

<p>I also suggest opening an issue on the actual repository of the extension. THere is no guarantee that <a class="mention" href="/u/jmhuie">@jmhuie</a> is actively tracking the forum, but an issue on the github repo will trigger a notification to him (and other developers).</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/jmhuie/SlicerBiomech">
  <header class="source">

      <a href="https://github.com/jmhuie/SlicerBiomech" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/8085e85ae524853648a845b80a9e008c/jmhuie/SlicerBiomech" class="thumbnail">

  <h3><a href="https://github.com/jmhuie/SlicerBiomech" target="_blank" rel="noopener nofollow ugc">GitHub - jmhuie/SlicerBiomech: Extension for the collection and analysis of...</a></h3>

    <p><span class="github-repo-description">Extension for the collection and analysis of biomechanical data from 3D specimen data</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @jmhuie (2025-09-25 05:45 UTC)

<aside class="quote no-group" data-username="cliftong" data-post="1" data-topic="44577">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/67e7ee/48.png" class="avatar"> cliftong:</div>
<blockquote>
<p>However, we’d also like to calculate the compactness of each slice. When we add in the compactness measurement, our output is now 201 rows and the calculated compactness value is 1 in every row (which it very clearly should not be).</p>
</blockquote>
</aside>
<p>Hi Glenna,</p>
<p>I was able to replicate this issue. I think there might some misunderstanding about how compactness is calculated. To do this with SegmentGeometry, you need to select a second segment that is a solid version of your main segment. You have to make this segment yourself; I typically do it using SurfaceWrapSolidify. For an example of this, if you look at the sample dataset you’ll see there is a segment called “Humerus” and one called “Humerus_solid”. Give that a go and let me know how it works!</p>
<aside class="quote no-group" data-username="cliftong" data-post="1" data-topic="44577">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/67e7ee/48.png" class="avatar"> cliftong:</div>
<blockquote>
<p>And some of the python output that seems to show some struggles:</p>
</blockquote>
</aside>
<p>These errors were unrelated to your problem and due to SegmentGeometry being out of date with recent versions of 3D Slicer. You’re question prompted me to update the module so you should not get those errors anymore if you update and use Slicer 5.8.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="44577">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>THere is no guarantee that <a class="mention" href="/u/jmhuie">@jmhuie</a> is actively tracking the forum, but an issue on the github repo will trigger a notification to him (and other developers).</p>
</blockquote>
</aside>
<p>Thanks Murat! I do occasionally check the forum for questions and get notifications when I’m tagged.</p>

---
