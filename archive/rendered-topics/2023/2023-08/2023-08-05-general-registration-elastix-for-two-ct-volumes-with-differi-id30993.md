# General Registration (Elastix) for two CT-Volumes with differing Voxel Size

**Topic ID**: 30993
**Date**: 2023-08-05
**URL**: https://discourse.slicer.org/t/general-registration-elastix-for-two-ct-volumes-with-differing-voxel-size/30993

---

## Post #1 by @chris_nik (2023-08-05 10:06 UTC)

<p>Dear Community,</p>
<p>my goal is to automatically align two CT-Volumes that have different voxel sizes. I concluded it is best to use the General Registration (Elastix) module. By creating an Output transform and applying it to the original moving volume, I managed to preserve the original voxel size of both volumes. Result of the alignment was good.<br>
My question is, how does the Slicer algorithm match the two volumes in this case? Does it divide the voxels of the larger-voxel-volume or does it combine voxels of the smaller-voxel-volume (I suppose it depends how I define the fixed and moving volume, the voxels of the moving volume get adapted to the fixed one)? If this is the case, does the accuracy of the alignment get influenced by the choice of fixed and moving volume (I supposed it could be better to choose the smaller-voxel-volume as the moving one, because it contains more infromation and smaller voxels are combined resulting in more accurate adapted voxels, compared to the case where larger voxels are divided into smaller ones with equal density)?</p>
<p>Cheers</p>

---

## Post #2 by @lassoan (2023-08-06 23:42 UTC)

<p>The similarity metric computation ignores the voxel size, it just takes samples from the images at random physical 3D coordinates. It does not matter what you choose as fixed or moving image, as sample positions are are random in physical space, not snapped to voxel center positions.</p>
<p>The computed transform is not related to the input image voxels either: the transformation defines a continuous mapping between two physical 3D spaces.</p>

---
