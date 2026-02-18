# How to create 3 channel image from different DICOMs?

**Topic ID**: 16481
**Date**: 2021-03-11
**URL**: https://discourse.slicer.org/t/how-to-create-3-channel-image-from-different-dicoms/16481

---

## Post #1 by @coconutattitude (2021-03-11 17:09 UTC)

<p>Hi, is there a way to combine different DICOMS into a single image in Slicer? I have several examinations, and I want to reproduce this AI segmentation: <a href="https://pytorch.org/hub/mateuszbuda_brain-segmentation-pytorch_unet//" class="inline-onebox" rel="noopener nofollow ugc">U-Net for brain MRI | PyTorch</a> However, It asks for specific input images:<br>
“Input image is a 3-channel brain MRI slice from pre-contrast, FLAIR, and post-contrast sequences, respectively.”</p>
<p>Is there any way to export DICOM or TIF that has different examination per channel?</p>

---

## Post #2 by @JanWitowski (2021-03-11 22:56 UTC)

<p>You probably can, you would have to load three series (pre-contrast, FLAIR and postcontrast), then <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Accessing_Volume_data_as_numpy_array" rel="noopener nofollow ugc">access pixel arrays from your loaded volumes</a>, and then stack them with e.g. <code>numpy.stack</code> or <code>torch.stack</code> to get your three channels matrix. I’m not sure why you would necessarily need Slicer for this specific task, though, this is probably easier to do with some scripting using SimpleITK or Pydicom (maybe even directly in your PyTorch DataLoader).</p>

---
