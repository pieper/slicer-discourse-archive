# X-Ray Phase Contrast Volume Reconstructions  

**Topic ID**: 6596
**Date**: 2019-04-24
**URL**: https://discourse.slicer.org/t/x-ray-phase-contrast-volume-reconstructions/6596

---

## Post #1 by @matdonoghue (2019-04-24 20:33 UTC)

<p>Hi all,</p>
<p>I am doing a bit of research in x-ray phase contrast imaging. Part of the research is to demonstrate that this new imaging technique can be used for soft tissue volume reconstruction. The image slices demonstrate that glandular breast tissue can be clearly distinguished from the denser in situ  ductal carcinoma. This is however not the case for the volume rendering and I believe the issue stems from the pixel values in the slices ranging from 1.2x10^-7 to 1.75x10^-7. I attached an image and will also attach a link to a drop box with the image slices. If anyone has any suggestions on how to improve the volume rendering please let me know.</p>
<p>Thanks,</p>
<p>Matthew</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75b435e2141eeb48ff0efc58387044d72d81afe0.png" alt="image" data-base62-sha1="gNfXIBE4zsrjYytUVL3SmIbStmo" width="609" height="488"></p>
<p><a href="https://www.dropbox.com/sh/l80ywcjqd127i6h/AADpiQG6Te7wDx2Q6CgviIQ9a?dl=0" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.dropbox.com/sh/l80ywcjqd127i6h/AADpiQG6Te7wDx2Q6CgviIQ9a?dl=0</a></p>

---

## Post #2 by @pieper (2019-05-24 17:45 UTC)

<p>The data seems not to have exported right.  I get lots of these warnings when I try to load:</p>
<blockquote>
<p>TIFFReadDirectory: Warning, Unknown field with tag 50839 (0xc697) encountered.</p>
</blockquote>
<p>Also when I spot check one image I see that the values are very small as you say.  If you can export the data another way so it loads as a volume you can rescale the pixel values in Slicer pretty easily (<code>a = array('Tiff*'); a*= 1e9</code> then save and reload the file to get a better window/level).</p>

---

## Post #3 by @lassoan (2019-05-24 18:38 UTC)

<p>I’ve checked this now and the problem is that the folder contains two image series, each with different slice size. Since file name prefixes are almost the same, Slicer tries to load them as one stack and fails.</p>
<p>You can load the two series if you separate the files into two folders:</p>
<ul>
<li>TiffSaver-tomo0111.nrrd … TiffSaver-tomo0476.tif</li>
<li>TiffSaver-tomo00000.tif … TiffSaver-tomo00180.tif</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c8b01472f0bca01b0f2e6ef73ed4bb658cf962c.jpeg" data-download-href="/uploads/short-url/k3iF5mxvq40P66gAv8PdrSgeZty.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c8b01472f0bca01b0f2e6ef73ed4bb658cf962c_2_690x462.jpeg" alt="image" data-base62-sha1="k3iF5mxvq40P66gAv8PdrSgeZty" width="690" height="462" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c8b01472f0bca01b0f2e6ef73ed4bb658cf962c_2_690x462.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c8b01472f0bca01b0f2e6ef73ed4bb658cf962c_2_1035x693.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c8b01472f0bca01b0f2e6ef73ed4bb658cf962c.jpeg 2x" data-dominant-color="4D4E55"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1370×919 335 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I would recommend to use the new utility functions for getting and updating the voxel array:</p>
<pre><code class="lang-auto">volNode = getNode('Tiff*')
a=arrayFromVolume(volNode)
a*= 1e10
arrayFromVolumeModified(volNode)
</code></pre>

---

## Post #4 by @matdonoghue (2019-05-24 18:55 UTC)

<p>Thanks so much, apologies for the incorrect images being uploaded as well.  I noticed that there also some images missing too. I can upload the correct tiff files when I get into work on Monday. The advice you’ve given me already has been a great help.</p>

---

## Post #5 by @matdonoghue (2019-05-27 11:19 UTC)

<p>I have the link for the correct series of slices below <a href="https://www.dropbox.com/s/p9tq32mdcpkyaav/cropped3.tif?dl=0" rel="nofollow noopener">https://www.dropbox.com/s/p9tq32mdcpkyaav/cropped3.tif?dl=0</a></p>
<p>I am new to 3-D slicer is there a document that describes how to access and use the utility functions? I can not find anything on it.</p>
<p>Kind regards,</p>
<p>Matthew</p>

---

## Post #6 by @lassoan (2019-05-27 12:34 UTC)

<aside class="quote no-group" data-username="matdonoghue" data-post="5" data-topic="6596">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/f19dbf/48.png" class="avatar"> matdonoghue:</div>
<blockquote>
<p>is there a document that describes how to access and use the utility functions?</p>
</blockquote>
</aside>
<p>The functions are documented here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#module-slicer.util" class="inline-onebox">slicer — 3D Slicer documentation</a></p>

---
