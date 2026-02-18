# segmentation labels are siplayed incorrectly in python

**Topic ID**: 31369
**Date**: 2023-08-26
**URL**: https://discourse.slicer.org/t/segmentation-labels-are-siplayed-incorrectly-in-python/31369

---

## Post #1 by @sepehr (2023-08-26 02:13 UTC)

<p>hello, I am trying to segment the lung (label 1,purple) and lung opacities (label 2,yellow) from ct scan images. after I finish segmenting in the slicer I save the labels as a nifti file. when I try to visualize the segmented areas in jupyter notebook label 1 and label 2 segments are mixed up. I mean that for some of the slices label 1 is displayed as purple and for others label 2 is displayed as purple. I run the following code in jupyter:</p>
<blockquote>
<p>Blockquote<br>
data = nib.load(sample_path)<br>
label = nib.load(sample_path_label)</p>
</blockquote>
<p>ct = data.get_fdata()<br>
mask = label.get_fdata().astype(int)</p>
<p>fig = plt.figure()<br>
camera = Camera(fig)  # Create the camera object from celluloid</p>
<p>for i in range(ct.shape[2]):  # Axial view<br>
plt.imshow(ct[:,:,i], cmap=“bone”)<br>
mask_ = np.ma.masked_where(mask[:,:,i]==0, mask[:,:,i])<br>
plt.imshow(mask_, alpha=0.5)<br>
# plt.axis(“off”)<br>
camera.snap()  # Store the current slice<br>
plt.tight_layout()<br>
animation = camera.animate()  # Create the animation</p>
<blockquote>
<p>Blockquote</p>
</blockquote>

---
