---
topic_id: 26489
title: "Nrrd Volume Save A Slice"
date: 2022-11-29
url: https://discourse.slicer.org/t/26489
---

# NRRD volume - Save a slice

**Topic ID**: 26489
**Date**: 2022-11-29
**URL**: https://discourse.slicer.org/t/nrrd-volume-save-a-slice/26489

---

## Post #1 by @lucas_sd (2022-11-29 09:28 UTC)

<p>Hi everybody,</p>
<p>Im working in a new module and I have a volume NRRD. I need to save just one slice, like [:,:,Zn], in a new NRRD volume. Is there a specific command to do this? I need to get the node first?</p>
<p>Thanks, Lucas.</p>

---

## Post #2 by @lassoan (2022-12-01 01:58 UTC)

<p>You can crop the volume using Crop volume module (see code snippet <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#fit-markups-roi-to-volume">here</a>) or you can use numpy indexing to get a region of a volume and then create a new volume from that using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.addVolumeFromArray">slicer.util.addVolumeFromArray</a>. You need to copy the IJK to RAS matrix from the original volume but don’t forget to set the origin to the position of the slice that you extracted (the original volume’s origin is the position of the first slice in the original volume).</p>

---

## Post #3 by @lucas_sd (2022-12-01 03:13 UTC)

<p>Hi Andras,</p>
<p>Thanks for your help, the idea was to get a .png image of a plane of a volume. Finally, and maybe not in the most efficient way, I did this:</p>
<pre><code class="lang-auto">readdata, header = nrrd.read(volume.nrrd)
image38 = np.asarray(readdata[:,38,:]).astype(int)  #38, the specific slice.
final = Image.fromarray(manipulating_nrrd_contrast(image38, 128)) #Create an image and some work with the contrast.
final.save(f'image38.png')
</code></pre>
<p>I know .png is not recommended and its different, but for my its a requirement.</p>

---

## Post #4 by @lassoan (2022-12-01 14:23 UTC)

<p>If you don’t need the correct image geometry (origin, spacing, axis directions) then it gets really simple:</p>
<pre><code class="lang-python">slice = slicer.util.array(volumeNode)[:,38,:]
Image.fromarray(slice).save('image38.png')
</code></pre>

---

## Post #5 by @lucas_sd (2022-12-06 10:28 UTC)

<p>Hi Andras,</p>
<p>Thanks! I wonder if its possible to fix by code the contrast and orientation, before save the file.<br>
Are there some commands to fix this and set it like properties?</p>
<p>Thanks, Lucas.</p>

---

## Post #6 by @lassoan (2022-12-06 16:17 UTC)

<p>By converting into PNG you may lose information. In theory you may be able to save a 16-bit grayscale image into PNG, but most software cannot work with such images. I would recommend to use a medical image file format (nrrd, mha, …) that don’t have issue with storing the native image contrast/brightness.</p>
<p>I don’t know what you mean exactly by “fixing the orientation”. The input image is already correctly oriented. You can also crop and resample it and save it into a medical image file format, which maintains size, position, and orientation of the image slice. If you use a consumer file format, such as PNG, then there is no standard way of storing the slice position or orientation.</p>
<p>It seems that all your issues come from trying to use a file format that is not appropriate for the data you have. I would recommend to keep using the nrrd format and process it with software tools and libraries that are suitable for medical image computing. Check out torchio, monai, monailabel, etc.</p>

---
