# Can't install extensions in latest Preview Release

**Topic ID**: 12285
**Date**: 2020-06-29
**URL**: https://discourse.slicer.org/t/cant-install-extensions-in-latest-preview-release/12285

---

## Post #1 by @BennetMontgomery (2020-06-29 21:22 UTC)

<p>I installed the latest preview build today and went to reinstall the extensions I was using, but Slicer claimed that the extensions were incompatible with the current version. Do I just need to downgrade to a version compatible with the extensions I want, or is something else wrong here?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/067681a9c1276fad3895eb2e2013c4bd8d51e49c.png" data-download-href="/uploads/short-url/VaLm7NWiMn7dMAST13dk8CPZP6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/067681a9c1276fad3895eb2e2013c4bd8d51e49c_2_690x376.png" alt="image" data-base62-sha1="VaLm7NWiMn7dMAST13dk8CPZP6" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/067681a9c1276fad3895eb2e2013c4bd8d51e49c_2_690x376.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/067681a9c1276fad3895eb2e2013c4bd8d51e49c_2_1035x564.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/067681a9c1276fad3895eb2e2013c4bd8d51e49c_2_1380x752.png 2x" data-dominant-color="FDFDFD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1049 39.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Sam_Horvath (2020-06-30 01:17 UTC)

<p>Something else I think.  I recommend trying an earlier version for now, we have been in the midst of some SSL updates and I think this is related to that.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a>  I am getting this error on the most recent Windows nightly when I try to download extensions:</p>
<pre><code class="lang-auto">"Retrieving extension metadata [ extensionId: 381453]"
"{5c738122-c1f4-4c42-a591-0e4cbe6ae535}: 99: Network access is disabled."
"Failed to retrieve metadata for extension 381453"
</code></pre>

---

## Post #3 by @BennetMontgomery (2020-06-30 14:51 UTC)

<p>It turns out the solution was just to wait. I guess the extensions server was overloaded or something similar. After a while, I was able to access the extensions menu again and download what I needed.</p>

---

## Post #4 by @Sam_Horvath (2020-06-30 14:57 UTC)

<p>Yes, we are actively working on replacing the current extension server which is definitely having issues.</p>

---
