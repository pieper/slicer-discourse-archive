---
topic_id: 30547
title: "Registration Of Images And Segmentations With Different Geom"
date: 2023-07-12
url: https://discourse.slicer.org/t/30547
---

# Registration of images and segmentations with different geometry (MIRACLE dataset)

**Topic ID**: 30547
**Date**: 2023-07-12
**URL**: https://discourse.slicer.org/t/registration-of-images-and-segmentations-with-different-geometry-miracle-dataset/30547

---

## Post #1 by @rfrs (2023-07-12 12:50 UTC)

<p>Dear community,</p>
<p>I started to use Slicer3D some time ago. Currently, to develop a spine segmentation model, i am using the MIRACLE dataset: <a href="https://github.com/MIRACLE-Center/CTSpine1K" rel="noopener nofollow ugc">MIRACLE-Center/CTSpine1K: A Large-Scale Dataset for Spinal Vertebrae Segmentation in Computed Tomography (github.com)</a>. Nonetheless, some of CT images and their segmentations have different geometries, e.g.: different origin and even different voxel size.</p>
<p>I tried to use the following code to register the images:</p>
<pre><code class="lang-auto">imgs = [i for i in sorted(listdir(folder_img)) if isfile(join(folder_img, i))]
#print(imgs)
fold_mask = [m for m in sorted(listdir(folder_mask)) if isfile(join(folder_mask, m))]

for img, mk in zip (imgs, fold_mask):

    name_img = os.path.splitext(img)[0]
    name_imgf = re.sub(".nii", "", name_img)

    # load volume image
    volumeNode = loadVolume(join(folder_img, img))
    # load labels
    segmentationNode = slicer.util.loadSegmentation(join(folder_mask, mk))

    originalSpacing = volumeNode.GetSpacing()
    print("Original spacing:", originalSpacing)
    originalOrigin = volumeNode.GetOrigin()
    print("Original origin:", originalOrigin)

    segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(volumeNode)
    labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")

    slicer.modules.segmentations.logic().ExportAllSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, slicer.vtkSegmentation.EXTENT_REFERENCE_GEOMETRY)
    savef = join(save_path, name_imgf + ext)
    saveNode(labelmapVolumeNode, savef)
    slicer.mrmlScene.Clear(0)
</code></pre>
<p>Nonetheless, when slicer exports the labels, it exports only a cropped version of the segmentations (same pixel numbers as the original image), but does not align the segmentation file.<br>
Have you encountered the same problem? How did you fix it?</p>
<p>Thanks a lot.<br>
Best</p>

---
