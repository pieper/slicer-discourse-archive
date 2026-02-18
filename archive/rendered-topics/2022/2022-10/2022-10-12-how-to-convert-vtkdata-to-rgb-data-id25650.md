# How to convert vtkData to RGB data?

**Topic ID**: 25650
**Date**: 2022-10-12
**URL**: https://discourse.slicer.org/t/how-to-convert-vtkdata-to-rgb-data/25650

---

## Post #1 by @user4 (2022-10-12 08:31 UTC)

<p>Hi,all.<br>
Here is one red slice of my image data(.vtk format)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99ce1ffbad7de7a3bc42614a86473c0f17144d1a.jpeg" data-download-href="/uploads/short-url/lWCFLmSvthAQczRbdzMwhuAoqYG.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99ce1ffbad7de7a3bc42614a86473c0f17144d1a.jpeg" alt="image" data-base62-sha1="lWCFLmSvthAQczRbdzMwhuAoqYG" width="685" height="500" data-dominant-color="676566"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">898×655 52.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I get this slice with the following code,</p>
<pre><code class="lang-auto">volume_node = slicer.util.getNode("vtkMRMLScalarVolumeNode1")
image = slicer.util.arrayFromVolume(volume_node)
red_slice = image[50,:,:]
</code></pre>
<p>However,its voxels are raw values which is not in [0,255] range.If I take a screenshot on this red slice and get a .png format picture,its pixels can convert into range [0,255].<br>
I want to know if there is a way to convert the slice with the raw data.<br>
This pseudocode is used to illustrate the idea.</p>
<pre><code class="lang-auto">red_slice = image[50,:,:]  # image is raw data, voxels are not in [0,255]
gray_red_slice = convert_to_gray_image(image[50,:,:])  # some function/methods to convert the intensity values
</code></pre>
<p>Thanks in advance for your help and advice!</p>

---

## Post #2 by @ebrahim (2022-10-12 14:10 UTC)

<p>You could transform the values into the [0,255] range by shifting and scaling them:</p>
<pre><code class="lang-python">a = red_slice.min()
b = red_slice.max()
gray_red_slice = 255 * (red_slice-a) / (b-a)
</code></pre>

---
