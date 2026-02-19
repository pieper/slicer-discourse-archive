---
topic_id: 6160
title: "Multiple Issues With Extension Builds"
date: 2019-03-15
url: https://discourse.slicer.org/t/6160
---

# Multiple issues with extension builds

**Topic ID**: 6160
**Date**: 2019-03-15
**URL**: https://discourse.slicer.org/t/multiple-issues-with-extension-builds/6160

---

## Post #1 by @fedorov (2019-03-15 17:43 UTC)

<p>There are several issues that are new (at least to me):</p>
<ul>
<li>at least some extensions are not listed 3 times (e.g. SlicerElastix is listed only once), which to me means they were not built on all platforms</li>
<li>maybe I am mistaken, but I vaguely recall there used to be OS icons indicating the platform used to build specific artifact - those are gone now</li>
<li>if inclusion of “clang” is supposed to indicate macOS, then there is only one line in the table that was built on mac (no idea what extension it packages, since it is called " <a href="http://slicer.cdash.org/buildSummary.php?buildid=1537174">macOS-clang-8.0.0-64bits-QT5.10.0-Release</a>")</li>
<li>can someone look at the issue below: <a href="http://slicer.cdash.org/viewBuildError.php?buildid=1537220" class="inline-onebox">CDash</a> - looks like a factory problem?</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62ad204a59f7b79172674b24546416bdb1eb4e45.png" data-download-href="/uploads/short-url/e4VIdip0hrpcqTvXrMF7FrnOCCV.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62ad204a59f7b79172674b24546416bdb1eb4e45_2_690x339.png" alt="image" data-base62-sha1="e4VIdip0hrpcqTvXrMF7FrnOCCV" width="690" height="339" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62ad204a59f7b79172674b24546416bdb1eb4e45_2_690x339.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62ad204a59f7b79172674b24546416bdb1eb4e45_2_1035x508.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62ad204a59f7b79172674b24546416bdb1eb4e45.png 2x" data-dominant-color="F0F1F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1329×654 51.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @fedorov (2019-03-15 17:54 UTC)

<p>Related to this, maybe we should add an entry to FAQ for users updating Slicer installation with a new nightly.</p>
<p>When I do this, I usually over-write my previous nightly. But the problem with this approach is that at the time I do it, I don’t have an easy way to know whether I am “fortunate” to have extensions that I need available in the new nightly. It might be practical to make users aware of this issue, and recommend users to keep their old nightly until they confirm the extensions they need are available.</p>

---

## Post #3 by @cpinter (2019-03-19 17:46 UTC)

<p>Today’s dashboard has a successful DCMQI and QuantitativeReporting build and packages:<br>
<a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercombine=or&amp;filtercombine=or&amp;filtercount=2&amp;showfilters=1&amp;filtercombine=or&amp;field1=label&amp;compare1=63&amp;value1=DCMQI&amp;field2=label&amp;compare2=63&amp;value2=QuantitativeReporting" class="onebox" target="_blank" rel="nofollow noopener">http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercombine=or&amp;filtercombine=or&amp;filtercount=2&amp;showfilters=1&amp;filtercombine=or&amp;field1=label&amp;compare1=63&amp;value1=DCMQI&amp;field2=label&amp;compare2=63&amp;value2=QuantitativeReporting</a></p>
<p>I do tend to see the error message sometimes that you posted though.</p>

---

## Post #4 by @jamesobutler (2019-03-19 21:07 UTC)

<p>From another post about similar problems finalizing/uploading the extension:</p>
<aside class="quote" data-post="1" data-topic="4819">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/operation-too-slow-less-than-1-bytes-sec-transferred-the-last-120-seconds/4819">"Operation too slow. Less than 1 bytes/sec transferred the last 120 seconds"</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    I’ve seen this in several extension builds over the past two nights, causing build (or upload?) failure: 
Operation too slow.  Less than 1 bytes/sec transferred the last 120 seconds
  </blockquote>
</aside>

<aside class="quote" data-post="2" data-topic="4819">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/operation-too-slow-less-than-1-bytes-sec-transferred-the-last-120-seconds/4819/2">"Operation too slow. Less than 1 bytes/sec transferred the last 120 seconds"</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Thanks for the note. 
Waiting we finalize the transition to a new system to manage extension, I will ask our sysadmin to setup daily restart of the server at noon.
  </blockquote>
</aside>


---
