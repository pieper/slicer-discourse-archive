# Pytorch extension installation

**Topic ID**: 30929
**Date**: 2023-08-02
**URL**: https://discourse.slicer.org/t/pytorch-extension-installation/30929

---

## Post #1 by @KSL (2023-08-02 09:56 UTC)

<p>Hello, I’ve been using total segmentator in Slicer 5.2.2 for quite sometime. Because of hardware issues, I detete slicer. When I reinstall slicer 5.2.2 and try to run total segmentator,I receive the message “PyTorch 1.8.1 + cpu  is not compatible with this module…”. Previously, I’ve been running total segmentator tool with CPU (which is Intel iris Xe graphics) as I do not have dedicated GPU. I need help to fix this problem. Thank you.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/160cc8615f7f93b16f25d20d91bf9954c52f82d8.jpeg" data-download-href="/uploads/short-url/393TfUfZOcgBQ0vnU4WKAlpWja0.jpeg?dl=1" title="Screenshot 2023-08-02 111221" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/160cc8615f7f93b16f25d20d91bf9954c52f82d8_2_690x460.jpeg" alt="Screenshot 2023-08-02 111221" data-base62-sha1="393TfUfZOcgBQ0vnU4WKAlpWja0" width="690" height="460" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/160cc8615f7f93b16f25d20d91bf9954c52f82d8_2_690x460.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/160cc8615f7f93b16f25d20d91bf9954c52f82d8_2_1035x690.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/160cc8615f7f93b16f25d20d91bf9954c52f82d8_2_1380x920.jpeg 2x" data-dominant-color="B3B3B8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-08-02 111221</span><span class="informations">1920×1280 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @ebrahim (2023-08-02 14:53 UTC)

<p>You can use the SlicerPyTorch extension and see if you can configure it to install the correct version.</p>
<p>Or you can generate a pytorch install command from here: <a href="https://pytorch.org/get-started/locally/" class="inline-onebox" rel="noopener nofollow ugc">Start Locally | PyTorch</a></p>
<p>For example setting it to use CPU the pip install command it gives is</p>
<pre><code class="lang-sh">pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
</code></pre>
<p>so you can achieve this in your slicer python environment by opening the slicer python console and doing the following:</p>
<pre><code class="lang-py">slicer.util.pip_install("torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu")
</code></pre>
<p>Consider first doing</p>
<pre><code class="lang-auto">slicer.util.pip_uninstall("torch")
</code></pre>
<p>to remove the old version – idk if it does that automatically</p>

---

## Post #3 by @lassoan (2023-08-02 15:04 UTC)

<p>CPU version of PyTorch is fine, you just need more recent PyTorch version than 1.8.1 for current TotalSegmentator version.</p>

---

## Post #4 by @KSL (2023-08-03 10:42 UTC)

<p>I have installed  PyTorch. However, the same problem persists.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbfbbba669075be9c86d7faba5218d6e077c4a58.png" data-download-href="/uploads/short-url/vo3TTpct6e1lGRQa4xR9KmC6PBC.png?dl=1" title="ABC" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbfbbba669075be9c86d7faba5218d6e077c4a58_2_455x500.png" alt="ABC" data-base62-sha1="vo3TTpct6e1lGRQa4xR9KmC6PBC" width="455" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbfbbba669075be9c86d7faba5218d6e077c4a58_2_455x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbfbbba669075be9c86d7faba5218d6e077c4a58_2_682x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbfbbba669075be9c86d7faba5218d6e077c4a58.png 2x" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ABC</span><span class="informations">904×993 36 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24ed28bf2ce17d1862684e67b2c62027a9cadc38.png" data-download-href="/uploads/short-url/5gFiBCd6QB2ijUv37inArGkcLtm.png?dl=1" title="A" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24ed28bf2ce17d1862684e67b2c62027a9cadc38_2_690x268.png" alt="A" data-base62-sha1="5gFiBCd6QB2ijUv37inArGkcLtm" width="690" height="268" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24ed28bf2ce17d1862684e67b2c62027a9cadc38_2_690x268.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24ed28bf2ce17d1862684e67b2c62027a9cadc38_2_1035x402.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24ed28bf2ce17d1862684e67b2c62027a9cadc38.png 2x" data-dominant-color="D9D7D8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">A</span><span class="informations">1045×406 53.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @muratmaga (2023-08-03 22:46 UTC)

<p>Your screenshot and error message says you are using Slicer 5.2.1. Please try with 5.2.2 (latest stable) and report back.</p>

---

## Post #6 by @Dex2046 (2023-08-04 06:53 UTC)

<aside class="quote no-group" data-username="KSL" data-post="4" data-topic="30929">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/82dd89/48.png" class="avatar"> KSL:</div>
<blockquote>
<p>.</p>
</blockquote>
</aside>
<p>I used slicer5.3，uninstall pytorch, reinstall pytorch as the error message said set version &gt;=1.12</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbe4fd36e554b684857785fd3e5730921300b8af.png" alt="屏幕截图 2023-08-04 145235" data-base62-sha1="vnhaIPwqhhNFcDIItSqfVNRoTnh" width="487" height="267"></p>

---

## Post #7 by @KSL (2023-08-04 10:39 UTC)

<p>Sir, I am using both 5.2.1 and 5.2.2 version. It did not work in both.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/712114ef8d5e358fbc6131fa7cb406929d102563.png" data-download-href="/uploads/short-url/g8MPytcavHqBhMsFLtbM7GbaKIz.png?dl=1" title="Bc" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/712114ef8d5e358fbc6131fa7cb406929d102563_2_690x266.png" alt="Bc" data-base62-sha1="g8MPytcavHqBhMsFLtbM7GbaKIz" width="690" height="266" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/712114ef8d5e358fbc6131fa7cb406929d102563_2_690x266.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/712114ef8d5e358fbc6131fa7cb406929d102563.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/712114ef8d5e358fbc6131fa7cb406929d102563.png 2x" data-dominant-color="DCDBDB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bc</span><span class="informations">1027×396 49 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
