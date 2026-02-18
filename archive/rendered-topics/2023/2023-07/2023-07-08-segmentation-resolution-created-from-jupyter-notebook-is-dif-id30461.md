# segmentation resolution created from Jupyter notebook is different than that created in 3dslicer

**Topic ID**: 30461
**Date**: 2023-07-08
**URL**: https://discourse.slicer.org/t/segmentation-resolution-created-from-jupyter-notebook-is-different-than-that-created-in-3dslicer/30461

---

## Post #1 by @ahmad_alminnawi (2023-07-08 02:11 UTC)

<p>Hi all,</p>
<p>I have been using 3dslicer for a while and wrote some Python codes for repetitive tasks.</p>
<p>When I create a segmentation in 3dslicer it would have the same resolution as the imported images (in my case 0.004x0.004x0.004) so when I threshold the segmentation and grow it using margin i can grow it by 0.004 which is 1 pixel. as shown here<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/130e23713f6d6ae89d203ae05006e9716956e000.png" data-download-href="/uploads/short-url/2IzmwZpqkyJ7nu25l27RZPuloVW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/130e23713f6d6ae89d203ae05006e9716956e000_2_690x315.png" alt="image" data-base62-sha1="2IzmwZpqkyJ7nu25l27RZPuloVW" width="690" height="315" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/130e23713f6d6ae89d203ae05006e9716956e000_2_690x315.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/130e23713f6d6ae89d203ae05006e9716956e000.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/130e23713f6d6ae89d203ae05006e9716956e000.png 2x" data-dominant-color="BEBDB9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">712×326 75.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I noticed that when I do the same using Python it says “Not feasible at current resolution” so i increased it to see what is the minimum i can grow and apparently is 0.02 meaning that the resolution is 0.02x0.02x0.02 for 1x1x1 pixel. as shown here<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a76385cfddc4060551b11fbe79f737f34b87a38a.png" data-download-href="/uploads/short-url/nSMXLvISqT6GRDk8iPbmXAy6WPo.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a76385cfddc4060551b11fbe79f737f34b87a38a_2_690x189.png" alt="image" data-base62-sha1="nSMXLvISqT6GRDk8iPbmXAy6WPo" width="690" height="189" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a76385cfddc4060551b11fbe79f737f34b87a38a_2_690x189.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a76385cfddc4060551b11fbe79f737f34b87a38a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a76385cfddc4060551b11fbe79f737f34b87a38a.png 2x" data-dominant-color="BBBBB9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">728×200 63.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>can someone help me get a 0.004x0.004x0.004 resolution using python?</p>
<p>This is my code:</p>
<h1><a name="p-97352-create-segmentation-1" class="anchor" href="#p-97352-create-segmentation-1" aria-label="Heading link"></a>Create segmentation</h1>
<p>segmentationNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLSegmentationNode”)<br>
segmentationNode.CreateDefaultDisplayNodes() # only needed for display<br>
segmentationNode.SetName(‘Segmentation’)</p>
<h1><a name="p-97352-import-the-model-into-the-segmentation-node-2" class="anchor" href="#p-97352-import-the-model-into-the-segmentation-node-2" aria-label="Heading link"></a>Import the model into the segmentation node</h1>
<p>slicer.modules.segmentations.logic().ImportModelToSegmentationNode(cylinderNode, segmentationNode)</p>
<p>Thanks in advance!</p>

---

## Post #2 by @ahmad_alminnawi (2023-07-10 10:19 UTC)

<p>Please note that when I am using Jupyter I am importing a volume model that I created and then thresholding the CT images inside that model and I think this is where things are getting weird.<br>
could it be that the volume has a low resolution? there is no “spacing” resolution for the model though. So, how can i increase the resolution of that model if that is the problem?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33c5aff41a3dca8b6f8b7ec4f1ce2a6c615c9e6e.jpeg" data-download-href="/uploads/short-url/7nZTqZFMxLvuIk8yd64b75IBOea.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33c5aff41a3dca8b6f8b7ec4f1ce2a6c615c9e6e_2_562x500.jpeg" alt="image" data-base62-sha1="7nZTqZFMxLvuIk8yd64b75IBOea" width="562" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33c5aff41a3dca8b6f8b7ec4f1ce2a6c615c9e6e_2_562x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33c5aff41a3dca8b6f8b7ec4f1ce2a6c615c9e6e.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33c5aff41a3dca8b6f8b7ec4f1ce2a6c615c9e6e.jpeg 2x" data-dominant-color="9A9D9C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">801×712 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
