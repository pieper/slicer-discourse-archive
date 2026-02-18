# Installer integrity check fail

**Topic ID**: 26966
**Date**: 2022-12-28
**URL**: https://discourse.slicer.org/t/installer-integrity-check-fail/26966

---

## Post #1 by @Maksym_Hladchuk (2022-12-28 23:48 UTC)

<p>Hello, i uploaded the picture for the error, pretty much the installer doesnt work and an error message saying installer integrity check fail comes out(NSIS error), i tried downloading both the stable release and the preview one but neither work, someone else had this problem or its probably a problem of my pc?</p>
<p>Thanks a lot for the attention</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8bc3b24a96a3323e9543c91022126d7bc9a5287b.png" alt="NSIS" data-base62-sha1="jWpE3CINmePkbCMcTn6GjjX4aTh" width="482" height="274"></p>

---

## Post #2 by @jcfr (2022-12-29 06:12 UTC)

<h3><a name="p-88201-verifying-checksum-1" class="anchor" href="#p-88201-verifying-checksum-1" aria-label="Heading link"></a>Verifying checksum</h3>
<p>Windows installer is expected to have its checksum (SHA512) be:</p>
<pre><code class="lang-auto">1c71bf558ebdb37e39dcdbb6109f7ec1787feb7c463880025c9835345ba6672775fa1e879e1f4e8319711fd497741e82179cd8e7572b0341de34f0103a02b09c
</code></pre>
<p>Could you confirm the package you downloaded is not corrupted ?</p>
<p>To compute the checksum associated with the file you locally downloaded, here are the steps:</p>
<ol>
<li>
<p>Start power shell</p>
</li>
<li>
<p>Adapt and run the following command:</p>
</li>
</ol>
<pre><code class="lang-auto">Get-Filehash -path c:\path\to\Downloads\Slicer-5.2.1-win-amd64.exe -algorithm SHA512 | fl
</code></pre>
<h3><a name="p-88201-looking-up-expected-checksum-2" class="anchor" href="#p-88201-looking-up-expected-checksum-2" aria-label="Heading link"></a>Looking up expected checksum</h3>
<p>Waiting we improve the download site to explicitly list the checksum, you may be able to identify the checksum of specific packages going to <code>https://slicer-packages.kitware.com</code>.</p>
<p>For example, here is how to identify the checksum for <code>Slicer-5.2.1-win-amd64.exe </code></p>
<ol>
<li>
<p>Go to  <a href="https://slicer-packages.kitware.com/#item/637f7a7f517443dc5dc73276">https://slicer-packages.kitware.com/#item/637f7a7f517443dc5dc73276</a></p>
</li>
<li>
<p>Display item infos</p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/8761031abed4083be34797d0311ec4efe8a53989.png" data-download-href="/uploads/short-url/jjCiYoqzL3EfNSOJYVX8hmmGFT3.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/8761031abed4083be34797d0311ec4efe8a53989_2_517x338.png" alt="image" data-base62-sha1="jjCiYoqzL3EfNSOJYVX8hmmGFT3" width="517" height="338" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/8761031abed4083be34797d0311ec4efe8a53989_2_517x338.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/8761031abed4083be34797d0311ec4efe8a53989_2_775x507.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/8761031abed4083be34797d0311ec4efe8a53989_2_1034x676.png 2x" data-dominant-color="AFB0B1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2837×1857 271 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Maksym_Hladchuk (2022-12-29 10:22 UTC)

<p>Hello,</p>
<p>Thaks you so much for your detailed answer, my first downloads were corrupted, i usually use an application for my downloads, and apparently it didn’t work for the installer of slicer, by using the browser to download(google) it worked, im sorry for the inconvenience, i never had this problem with the download app.</p>

---
