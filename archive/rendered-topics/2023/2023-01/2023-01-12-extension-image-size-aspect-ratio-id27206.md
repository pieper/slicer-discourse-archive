# Extension image size / aspect ratio

**Topic ID**: 27206
**Date**: 2023-01-12
**URL**: https://discourse.slicer.org/t/extension-image-size-aspect-ratio/27206

---

## Post #1 by @RafaelPalomar (2023-01-12 12:51 UTC)

<p>The image for the SlicerLiver extension in the extension manager looks blurry; it is probably too small.</p>
<p>Is there any specific size or aspect ratio that should be respected?</p>

---

## Post #2 by @jamesobutler (2023-01-12 22:15 UTC)

<p>The .s4ext files recommend 128x128, but based on conversations in <a href="https://github.com/Slicer/ExtensionsIndex/issues/1777" class="inline-onebox" rel="noopener nofollow ugc">Allow logos with higher resolution · Issue #1777 · Slicer/ExtensionsIndex · GitHub</a>, it seems appropriate to raise that. Maybe 512x512. I know that Slicer extension TorchIO uses a 1024x1024 PNG file (<a href="https://github.com/fepegar/SlicerTorchIO/blob/master/TorchIOTransforms/Resources/Icons/TorchIOTransforms.png" class="inline-onebox" rel="noopener nofollow ugc">SlicerTorchIO/TorchIOTransforms.png at master · fepegar/SlicerTorchIO · GitHub</a>). There was an issue with an image of 2048x2048, so there can be issues with it being too large, but evidently 1024x1024 worked for them without issue. Also typical square aspect ratio seems to be preferred when serving as an icon (QIcon) in Slicer.</p>

---

## Post #3 by @lassoan (2023-01-12 23:51 UTC)

<p>I agree that we should recommend higher resolution than 128x128. Probably today 256x256 icon is ideal as it is sufficiently high resolution and not a lot of time wasted with downloading and resampling. But we could recommend 512x512 to be a bit more future-proof (and if needed then we can downscale them to smaller size and cache it to improve performance).</p>
<p>Requiring square icon is a good idea, too, as it simplifies the extension catalog design.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> if you agree then we could add this updated info to the documentation.</p>

---
