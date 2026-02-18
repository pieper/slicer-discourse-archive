# Importing images in czi file extension

**Topic ID**: 12291
**Date**: 2020-06-30
**URL**: https://discourse.slicer.org/t/importing-images-in-czi-file-extension/12291

---

## Post #1 by @Deepa (2020-06-30 10:33 UTC)

<p>Hi All,<br>
May I know how to import image files in czi file format generated from Zeiss microscope into Slicer,<br>
for performing segmentation?</p>
<p>Thanks,<br>
Deepa</p>

---

## Post #2 by @lassoan (2020-06-30 21:25 UTC)

<p>Probably the easiest is to load it using a Python package (e.g., <a href="https://pypi.org/project/czifile/">czifile</a>) then set the Python array into a volume node.</p>
<p>If you need to load this kind of images often, then you can write a short Python scripted module that makes loading available in “Add data” dialog the same way as for other formats.</p>

---

## Post #3 by @Deepa (2020-07-01 16:52 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Thank you.<br>
I tried the following in python</p>
<pre><code class="lang-auto">import czifile
from skimage import io

img = czifile.imread('file.czi')
print(img.shape)
</code></pre>
<p>The output is<br>
(1, 1, 3, 1, 48, 1024, 1024, 1)<br>
I couldn’t completely understand what each value in the output refers to</p>
<p>Does 3 denote the number of channels?</p>
<p>From what I understand 48 refers to the number of slices in the z-stack. I would like to save the z-stack corresponding to channel 1 in tiff format and load this in Slicer. Could you please offer some advice on how this can be done?</p>

---

## Post #4 by @lassoan (2020-07-01 17:17 UTC)

<p>You can use <code>numpy.squeeze()</code> to remove singular dimensions of an array. Probably there is a reason for czifile to return these many extra dimensions, so I would recommend to read its documentation.</p>

---

## Post #5 by @Deepa (2020-07-02 17:08 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a><br>
I could do the following</p>
<p><a href="https://drive.google.com/file/d/1SzbIIrW9jeCSf5bYMZ1BN2GSzANrNTA9/view?usp=sharing" rel="nofollow noopener">input</a></p>
<pre><code>from aicsimageio import AICSImage
from aicsimageio.writers import OmeTiffWriter


img = AICSImage('input.czi')
img.data  # returns 6D STCZYX numpy array
print(img.dims)  # returns string "STCZYX"
print(img.shape)  # returns tuple of dimension sizes in STCZYX order

first_channel_data = img.get_image_data("ZYX", C=1, S=0, T=0)

 with OmeTiffWriter("file.ome.tiff") as writer:
     writer.save(
         first_channel_data,
         pixels_physical_size=img.get_physical_pixel_size(),
         dimension_order="ZYX",
     )
</code></pre>
<p>The output tiff file has 3 channels. One of the channels has stained cells. But from the other two channels, I am not sure how to find out which channel can be used for 3D reconstruction of vessels<br>
in Slicer.</p>
<p>Could you please offer some advice?</p>

---

## Post #6 by @lassoan (2020-07-02 19:58 UTC)

<p>Why don’t you simple use <code>squeeze</code> as I suggested above to remove the singular dimensions set the array in a volume node by calling <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.updateVolumeFromArray">slicer.util.updateVolumeFromArray</a>?</p>
<aside class="quote no-group" data-username="Deepa" data-post="5" data-topic="12291">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepa/48/5634_2.png" class="avatar"> Deepa:</div>
<blockquote>
<p>The output tiff file has 3 channels. One of the channels has stained cells. But from the other two channels, I am not sure how to find out which channel can be used for 3D reconstruction of vessels<br>
in Slicer.</p>
</blockquote>
</aside>
<p>It depends on the color of the feature that you want to extract and color of background noise that you want to suppress. Try all combinations in “Vector To Scalar Volume” module (Luminance, Average, and each single component) and use whichever works the best.</p>

---
