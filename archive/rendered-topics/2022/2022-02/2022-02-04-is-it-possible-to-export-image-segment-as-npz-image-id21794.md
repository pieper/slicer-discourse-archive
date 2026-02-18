# Is it possible to export image + segment as .npz image?

**Topic ID**: 21794
**Date**: 2022-02-04
**URL**: https://discourse.slicer.org/t/is-it-possible-to-export-image-segment-as-npz-image/21794

---

## Post #1 by @codeenthusiast (2022-02-04 02:32 UTC)

<p>I am working on an image registration platform on VoxelMorph and it can take .npz as input. Is it possible to save the volume and segmentation of an image in 3D slicer as .npz format?</p>

---

## Post #2 by @lassoan (2022-02-04 04:22 UTC)

<p>You can get the image and segmentation as a numpy array using <code>slicer.util.arrayFromVolume</code> and <code>slicer.util.arrayFromSegmentBinaryLabelmap</code> functions (see <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#read-and-write-a-segment-as-a-numpy-array">examples</a>). You can write a numpy array to a npz file using <code>np.savez</code>.</p>
<p>I would not recommend to use npz format, though, as I don’t think there is a standard way of storing image geometry in it (image origin, spacing, axis directions). Instead, you can save the volume and segmentation as nrrd or nifti files, which contain all essential metadata. VoxelMorph can read nifti files according to its <a href="https://github.com/voxelmorph/voxelmorph#registration">tutorials</a>.</p>
<p>Let us know how it all works. Common registration problems are solved quite nicely by ElastiX and ANTs toolkits, typically under 20 seconds for rigid transform and under 1 minute for deformable transform, so there is not a huge room for practically relevant improvements (maybe for large 4D volumes?). But if VoxelMorph works much faster and it is more robust and accurate than these classic toolkits then we might look into making it available directly in Slicer.</p>

---

## Post #3 by @pieper (2022-02-04 13:51 UTC)

<p>If VoxelMorph works well please consider making a Slicer extension for it so that others can easily try it on their data.  I haven’t tried VoxelMorph, but I’ve been told it is very efficient and robust.</p>

---

## Post #4 by @codeenthusiast (2022-02-07 01:11 UTC)

<p>Thanks very much for your reply. This is very helpful.</p>
<p>I have a follow-up question for this. I have to make sure that the dimensions for all my training images is equal. Is there a way to modify the dimensions in 3D slicer so that all images are the same from a dimension perspective?</p>

---

## Post #5 by @pieper (2022-02-07 17:47 UTC)

<p>Yes, you can use <code>ResampleScalarVectorDWIVolume</code> and set a reference volume to be the same for all you data (assuming they are in the same space).</p>
<p>For some reason the documentation didn’t get into readthedocs yet, but here’s the 3.6 version of the documentation:<br>
<a href="https://www.slicer.org/wiki/Modules:ResampleScalarVectorDWIVolume-Documentation-3.6" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Modules:ResampleScalarVectorDWIVolume-Documentation-3.6</a></p>

---

## Post #6 by @jamesobutler (2022-02-07 17:50 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> The <code>ResampleScalarVectorDWIVolume</code> documentation is in the readthedocs:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/resamplescalarvectordwivolume.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/modules/resamplescalarvectordwivolume.html</a></p>

---

## Post #7 by @pieper (2022-02-07 17:54 UTC)

<p>Ah, good, thanks for finding it James.  I had searched for the module name which didn’t work.</p>

---
