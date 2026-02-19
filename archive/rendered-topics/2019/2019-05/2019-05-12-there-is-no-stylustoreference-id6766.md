---
topic_id: 6766
title: "There Is No Stylustoreference"
date: 2019-05-12
url: https://discourse.slicer.org/t/6766
---

# There is no “StylusToReference”

**Topic ID**: 6766
**Date**: 2019-05-12
**URL**: https://discourse.slicer.org/t/there-is-no-stylustoreference/6766

---

## Post #1 by @Zhao_Su (2019-05-12 12:16 UTC)

<p>There is no “StylusToReference”,When I use slicerigt.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91bba70b93d6cba509f9d7b7e84d2dbe798ebc48.png" data-download-href="/uploads/short-url/kNdhalEPHauNEa764q6GIQ8jN8I.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91bba70b93d6cba509f9d7b7e84d2dbe798ebc48_2_666x500.png" alt="image" data-base62-sha1="kNdhalEPHauNEa764q6GIQ8jN8I" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91bba70b93d6cba509f9d7b7e84d2dbe798ebc48_2_666x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91bba70b93d6cba509f9d7b7e84d2dbe798ebc48_2_999x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91bba70b93d6cba509f9d7b7e84d2dbe798ebc48_2_1332x1000.png 2x" data-dominant-color="F8F3F3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2048×1536 289 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Sunderlandkyl (2019-05-12 12:39 UTC)

<p>Some questions:</p>
<ul>
<li>Which SlicerIGT tutorial are you following?</li>
<li>What config file are you using in Plus?</li>
<li>Can you upload your log file from Plus?</li>
</ul>

---

## Post #4 by @Zhao_Su (2019-05-12 13:20 UTC)

<p>I was following U03.I didn’t create my own config file. I choose the” NDI Polaris with passive marker “ in Plus.And it was connected successfully.</p>

---

## Post #5 by @Sunderlandkyl (2019-05-12 13:50 UTC)

<p>Can you attach your log file?</p>
<p>If should be in:</p>
<blockquote>
<p>C:/Users/Username/PlusApp-2.X.Y.etc/data</p>
</blockquote>

---

## Post #6 by @Zhao_Su (2019-05-12 14:57 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/928554a237523b399a1e6395377f4f4994551324.png" data-download-href="/uploads/short-url/kUbmWY2AtedbRjXYX5noth8EiuU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/928554a237523b399a1e6395377f4f4994551324.png" alt="image" data-base62-sha1="kUbmWY2AtedbRjXYX5noth8EiuU" width="690" height="342" data-dominant-color="E5E5E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1895×940 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
There are a lot of log files,I choose one latest.<br>
sorry,I dont know how to upload files. Thanks a lot for your help!</p>

---

## Post #7 by @Sunderlandkyl (2019-05-12 17:03 UTC)

<p>Ok. within the config file, you need to specify StylusToReference as an outgoing transform.<br>
Look for the “TransformNames” element within the PlusOpenIGTLinkServer.</p>
<p>Just add the following:</p>
<blockquote>
<pre><code>    &lt;Transform Name="StylusToReference" /&gt;
</code></pre>
</blockquote>
<p>You can add or remove transforms from this section.</p>

---

## Post #8 by @Zhao_Su (2019-05-14 15:38 UTC)

<p>Sorry to bother you again. I was add that code .But there is still no “StylusToReference” under “IN” .Only one time ,there is a “StylusToTracker”.Most of time,there is nothing.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94f174abf60ae0ed7170a74ad6c733640fc9f6e1.png" alt="image" data-base62-sha1="lfBYTvDh063npowQ8E6YXtcPH7X" width="378" height="164"><br>
And there is an another question. When I click “Recording” in “Plus Remote” module, it was recording failed. Like that<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f597aeae30bd6cbfe7c29e7fb0ebac7114c57502.png" data-download-href="/uploads/short-url/z2BXpgD9fNaPNR08KtnnHzOyO9s.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f597aeae30bd6cbfe7c29e7fb0ebac7114c57502.png" alt="image" data-base62-sha1="z2BXpgD9fNaPNR08KtnnHzOyO9s" width="690" height="39" data-dominant-color="E2E2E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1201×69 3.91 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is my log file<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/2404426601df676b9f7aa865cffacb9d0c50f235.png" data-download-href="/uploads/short-url/58Cjvi7JACD7ckzsK255EVNOWXz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/2404426601df676b9f7aa865cffacb9d0c50f235.png" alt="image" data-base62-sha1="58Cjvi7JACD7ckzsK255EVNOWXz" width="690" height="351" data-dominant-color="E7E7E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1916×976 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8d80a3d0d8f8fd093d56bb681a9095a03b55a17.png" data-download-href="/uploads/short-url/uWhZP7rDhy0cZ2uaFfn61iyV6jd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8d80a3d0d8f8fd093d56bb681a9095a03b55a17.png" alt="image" data-base62-sha1="uWhZP7rDhy0cZ2uaFfn61iyV6jd" width="690" height="347" data-dominant-color="E5E5E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×966 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61160a3c4c9eacf0fa8af6931f6627f8d1efbaed.png" data-download-href="/uploads/short-url/dQRxaQbwuBRjdEVVJGR4wrXYEAB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61160a3c4c9eacf0fa8af6931f6627f8d1efbaed.png" alt="image" data-base62-sha1="dQRxaQbwuBRjdEVVJGR4wrXYEAB" width="690" height="349" data-dominant-color="E7E7E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×973 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/4339f53d7c4a121ebb67bbdd6a8c2930810fb855.png" data-download-href="/uploads/short-url/9AIadRyw2B1O0zENwPvaWkHXUUd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/4339f53d7c4a121ebb67bbdd6a8c2930810fb855.png" alt="image" data-base62-sha1="9AIadRyw2B1O0zENwPvaWkHXUUd" width="690" height="118" data-dominant-color="E6E6E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1890×325 37.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks a lot for your help!</p>

---
