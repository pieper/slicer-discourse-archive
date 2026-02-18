# 3D slicer 4.10 can't load structures

**Topic ID**: 4593
**Date**: 2018-10-30
**URL**: https://discourse.slicer.org/t/3d-slicer-4-10-cant-load-structures/4593

---

## Post #1 by @aseman (2018-10-30 16:02 UTC)

<p>Operating system:windows 10<br>
Slicer version:4.10<br>
Hi 3D slicer experts and all<br>
I installed 3D Slicer 4.10 ; but unfortunately , when I load structures the following error message is shown.(figure 1) ; and the CT images are not displayed(figure2). also, I can’t install any Extension from Extension Manager. Can you help me about these problems.<br>
Thanks a lot<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c4bfe03c1bcf62efdefef8a6a4fb3019dfb45e6.png" alt="" data-base62-sha1="8BpszxYZYlJhP4IQXpKvWN2sgTQ" width="429" height="149" role="presentation"></p>

---

## Post #2 by @lassoan (2018-10-30 16:03 UTC)

<p>You need to install SlicerRT extension to be able to load RT structure sets.</p>

---

## Post #3 by @aseman (2018-10-30 16:06 UTC)

<p>thank you for your guideline. but I can’t install any Extension. can you help me?</p>

---

## Post #4 by @lassoan (2018-10-30 17:02 UTC)

<p>See installation instructions <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager#Installing_an_extension">here</a>. Name of the extension that you need to install is <em>SlicerRT</em>.</p>

---

## Post #5 by @aseman (2018-10-30 20:37 UTC)

<p>Hi<br>
I’m sorry for my questions! but my problem with installing Extensions is that the page associated with Extension Manager is like the following figure ; and no Extensions are visible for selection . I installed and uninstalled the slicer several times, but it was not effective. please guide me.<br>
thank you<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a133a1b9cdb660802d6cd4146f6c8232640ac536.png" data-download-href="/uploads/short-url/n03uA0r3RKVmQ1BNUh2NkGipf5I.png?dl=1" title="extension" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a133a1b9cdb660802d6cd4146f6c8232640ac536_2_690x369.png" alt="extension" data-base62-sha1="n03uA0r3RKVmQ1BNUh2NkGipf5I" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a133a1b9cdb660802d6cd4146f6c8232640ac536_2_690x369.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a133a1b9cdb660802d6cd4146f6c8232640ac536_2_1035x553.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a133a1b9cdb660802d6cd4146f6c8232640ac536.png 2x" data-dominant-color="1A1D1E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">extension</span><span class="informations">1358×727 15.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2018-10-30 21:08 UTC)

<p>Is it an official Slicer-4.10 build? Is it possible that your computer is behind a firewall?</p>
<p>Anyway, you can follow <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager#Installing_an_extension_without_network_connection">these instructions</a> for downloading an extension using a web browser and installing it manually.</p>

---
