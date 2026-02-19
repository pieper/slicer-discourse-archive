---
topic_id: 24556
title: "How To Access Realtime Outside Signs"
date: 2022-07-29
url: https://discourse.slicer.org/t/24556
---

# How to access realtime outside signs?

**Topic ID**: 24556
**Date**: 2022-07-29
**URL**: https://discourse.slicer.org/t/how-to-access-realtime-outside-signs/24556

---

## Post #1 by @whu (2022-07-29 05:40 UTC)

<p>Dear All,</p>
<pre><code>   How to access a real-time external signal source? And displayed on the slice interface.

   I have a device that generates real-time coordinate information （using usb interface） and simulates navigation, hoping to correspond with the scanned CT data.

   Thanks for any suggestion.
</code></pre>

---

## Post #2 by @pieper (2022-07-29 15:27 UTC)

<p>One option is to integrate a driver for the device with PLUS <a href="https://plustoolkit.github.io/">https://plustoolkit.github.io/</a></p>

---

## Post #3 by @whu (2022-08-08 07:17 UTC)

<p>Maybe this is the second topic using NDI device.<br>
the first as :  <a href="https://discourse.slicer.org/t/navigation-with-ndi-aurora-polaris-tracker/905" class="inline-onebox">Navigation with NDI Aurora/Polaris tracker</a><br>
Here I have connected the NDI trakSTAR using PLUS server + OpenIGTLinkIF. As image showed below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13c598d37fa71938fd0bdffbfd43cb4841dbb06a.png" data-download-href="/uploads/short-url/2OUq8hzBtAph4lO9p20VlDadSqK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13c598d37fa71938fd0bdffbfd43cb4841dbb06a.png" alt="image" data-base62-sha1="2OUq8hzBtAph4lO9p20VlDadSqK" width="594" height="500" data-dominant-color="F1F4F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">802×675 8.82 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Here my question is how to get or show the data from the IGT above ?<br>
thanks for any suggestion. <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @mau_igna_06 (2022-08-08 08:20 UTC)

<p>I think you just need to open the client in Slicer and look at the transforms in the transforms module</p>
<p>Hope it helps</p>

---

## Post #5 by @whu (2022-08-08 08:40 UTC)

<p>can you give a simple UI picture ?  I am not  familiar with Slicer Application.</p>
<p>I tried the IGT Remote,</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/1471de6cd3c77d2546cfbd17a4037042211e451d.png" data-download-href="/uploads/short-url/2URvLffrUrBbyQxHYUikvw5RxOl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/1471de6cd3c77d2546cfbd17a4037042211e451d.png" alt="image" data-base62-sha1="2URvLffrUrBbyQxHYUikvw5RxOl" width="690" height="432" data-dominant-color="F7F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">735×461 24.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>the Slicer software crashed soon…</p>

---

## Post #6 by @mau_igna_06 (2022-08-08 08:51 UTC)

<p>Please look at the docunentation:<br>
<a href="https://www.slicer.org/wiki/Modules:OpenIGTLinkIF-Documentation-3.4" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Modules:OpenIGTLinkIF-Documentation-3.4</a></p>
<p>There are pictures there</p>

---

## Post #7 by @whu (2022-08-08 09:21 UTC)

<p>thanks very much. that version is little eary.</p>
<p>the new UI is as below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9a01dc3aa44d848a64f58a3816282fbd1f511dc.png" data-download-href="/uploads/short-url/xkKiu1K3ZPgEuNhFOnssNT3AuJe.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9a01dc3aa44d848a64f58a3816282fbd1f511dc.png" alt="image" data-base62-sha1="xkKiu1K3ZPgEuNhFOnssNT3AuJe" width="677" height="500" data-dominant-color="F2F3F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">800×590 10.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I still can not get the data（transform）.</p>

---

## Post #8 by @whu (2022-08-11 02:36 UTC)

<p>Still waiting for the answers,thanks</p>

---

## Post #9 by @whu (2022-08-11 07:20 UTC)

<p>As your suggestion, using Slicer 3.6.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a42f1122c10f0334f0122088c5370df28b0341b.png" alt="image" data-base62-sha1="8jp78KZu2FqZ1S6eGUHrrAPC4hJ" width="469" height="285"><br>
No more choose as in the tutorials.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/1763f6f526f6ccc9f648f0c295ef264cb93132fd.png" data-download-href="/uploads/short-url/3kV9CpWjqUCPrhSdXfcgxD2fk2F.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/1763f6f526f6ccc9f648f0c295ef264cb93132fd_2_690x294.png" alt="image" data-base62-sha1="3kV9CpWjqUCPrhSdXfcgxD2fk2F" width="690" height="294" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/1763f6f526f6ccc9f648f0c295ef264cb93132fd_2_690x294.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/1763f6f526f6ccc9f648f0c295ef264cb93132fd_2_1035x441.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/1763f6f526f6ccc9f648f0c295ef264cb93132fd_2_1380x588.png 2x" data-dominant-color="EFEEF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1447×617 62.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
so, the result,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d5018b4b3b255a267cc0e0c1e42de2f53c672fa.png" data-download-href="/uploads/short-url/dju0FeAGGCUhItO7YR0x30GNSnU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d5018b4b3b255a267cc0e0c1e42de2f53c672fa_2_690x217.png" alt="image" data-base62-sha1="dju0FeAGGCUhItO7YR0x30GNSnU" width="690" height="217" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d5018b4b3b255a267cc0e0c1e42de2f53c672fa_2_690x217.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d5018b4b3b255a267cc0e0c1e42de2f53c672fa_2_1035x325.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d5018b4b3b255a267cc0e0c1e42de2f53c672fa_2_1380x434.png 2x" data-dominant-color="B0AFE6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1400×441 19.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The locator model shows up , but it dose not move around in the 3D view.<br>
…sorry…<br>
Still for answers.</p>

---
