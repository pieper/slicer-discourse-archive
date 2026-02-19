---
topic_id: 35690
title: "Imageaugmenter Extension Released"
date: 2024-04-23
url: https://discourse.slicer.org/t/35690
---

# ImageAugmenter extension released!

**Topic ID**: 35690
**Date**: 2024-04-23
**URL**: https://discourse.slicer.org/t/imageaugmenter-extension-released/35690

---

## Post #1 by @ciro.raggio (2024-04-23 17:54 UTC)

<p>We are happy to announce that the <a href="https://extensions.slicer.org/view/ImageAugmenter/32818/linux" rel="noopener nofollow ugc">ImageAugmenter</a> extension is now available in the preview release of 3D Slicer. This new extension lets you easily augment your medical image datasets without writing a single line of code.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4de46a6aab4b53c9d00abad606845ede1d99564.jpeg" data-download-href="/uploads/short-url/nwuwOq6dKf9gwainhcvmskmxfhO.jpeg?dl=1" title="1713547600423" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a4de46a6aab4b53c9d00abad606845ede1d99564_2_690x420.jpeg" alt="1713547600423" data-base62-sha1="nwuwOq6dKf9gwainhcvmskmxfhO" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a4de46a6aab4b53c9d00abad606845ede1d99564_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a4de46a6aab4b53c9d00abad606845ede1d99564_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a4de46a6aab4b53c9d00abad606845ede1d99564_2_1380x840.jpeg 2x" data-dominant-color="77787A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1713547600423</span><span class="informations">1915×1166 186 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The extension includes more than 20 transformations based on the MONAI framework, letting the user set almost all parameters for each transformation. It also faithfully respects the name and meaning of the parameters, so you can easily consult the documentation to understand the meaning of each parameter and transformation here: <a href="https://docs.monai.io/en/latest/transforms.html" rel="noopener nofollow ugc">https://docs.monai.io/en/latest/transforms.html</a>.</p>
<p>If you want, you can also choose the path for your masks. This lets you apply augmentation to images and masks at the same time, while keeping the pairing between them even when you use random transformations.</p>
<p>In addition, you can preview the result of all transformations directly in Slicer, allowing you to change parameters more quickly until you are completely satisfied with the result. Once you’re done, you can save the images in the folder of your choice, maintaining the same hierarchy as the files you used as input! Of course, you can also use PyTorch-compatible GPUs (when available) if you want to speed up the computation.</p>
<p><a href="https://ciroraggio.github.io/SlicerImageAugmenter/tutorial" rel="noopener nofollow ugc">Here</a> you will find a tutorial on how to use it, as well as a link to download sample data and a link to the repository.</p>
<p>If there are features you would like to see added, or if you have any feedback about this extension, please let us know.</p>
<p>We hope you enjoy it and find it useful for your research!</p>
<p><a class="mention" href="/u/paolozaffino">@PaoloZaffino</a> <a class="mention" href="/u/mfs78">@mfs78</a></p>

---
