# High resolution 3D model from CT scans from multiple planes?

**Topic ID**: 34112
**Date**: 2024-02-02
**URL**: https://discourse.slicer.org/t/high-resolution-3d-model-from-ct-scans-from-multiple-planes/34112

---

## Post #1 by @jakezw (2024-02-02 10:45 UTC)

<p>hi, I have dicom data in the three major planes (axial coronal sagittal)<br>
I can load all 3 into the 3D reconstruction viewer and it displays fantastic, with high level detail of the scanned head.<br>
I wish to export this as a model, but as I’ve learned, I need to segment the area I want out, and create a 3D model first from the segmentation. However, using the segmentation tool, like using threshold, only let’s me work in one plane. If I create a model using the segmentation tool in the axial plane for example, it creates a fairly poor model in comparison to the 3D reconstruction using all 3 planes.<br>
Is there a way to better create a high resolution and high polygon 3D exportable object using all planes and better pixel resolution?</p>

---

## Post #2 by @pieper (2024-02-02 11:33 UTC)

<p>CT scans are usually acquired in a single plane and other planes would be reconstructed from that acquisition.  Maybe you can add some screenshots to demonstrate what you are seeing and we can advise you more specifically.</p>

---

## Post #3 by @jakezw (2024-02-02 16:49 UTC)

<p>sure, so basically like this. I have reformated sag and cor planes that was done by the CT scanner at time of imaging, the reformats are very high quality and not pixelated like the auto reformats that 3D slicer creates from the Axial scans.<br>
In the volume rendering module, I can select all three of these CT scans to view on the 3D renderer and it creates a very nice and high resolution 3D reconstruction using all three planes.<br>
                    <a href="https://i.imgur.com/yEyDnnn.png" target="_blank" rel="noopener nofollow ugc" class="onebox">
            <img src="https://i.imgur.com/yEyDnnn.png" width="690" height="316">
          </a>

</p>
<p>Now, if I want to convert this to a 3D model, It’s my understanding I have to segment this, using the segment editor and threshold tool to select the bone, it does a pretty good job at grabbing all the bone and creating a map to eventually generate the 3D model with, but it is only using the CT images in the Axial plane<br>
                    <a href="https://i.imgur.com/wsa72zB.png" target="_blank" rel="noopener nofollow ugc" class="onebox">
            <img src="https://i.imgur.com/wsa72zB.png" width="658" height="500">
          </a>

</p>
<p>so needless to say, when I generate the 3D model, it becomes “stepped” and loses a lot of the quality, as it’s only using one plane to generate the model, as opposed to a volume re-construction using several planes.<br>
the pixel size also is pretty large, I have a powerful GPU so I wanted to create a 3D reconstruction with as much vertex data as possible, but it seems it can only move in one plane and have fairly large pixel rendering, resulting in a 3D re-construction that isn’t as high polygon as I would like.<br>
                    <a href="https://i.imgur.com/G69sovP.png" target="_blank" rel="noopener nofollow ugc" class="onebox">
            <img src="https://i.imgur.com/G69sovP.png" width="690" height="332">
          </a>

<br>
I am wondering if there is a way to increase this resolution, or further create a model using the cor and seg CT data I have to create a model that is more similar to the one that is created for the volume rendering?</p>

---

## Post #4 by @jakezw (2024-02-02 22:43 UTC)

<p>After digging around various resources and trying different things I found a tool that helps me build what i want. Not sure if 3D slicer has similar functionality or not, but I have found that InVesalius 3 is able to do what I want. It is able to take my Axial scans and the reformatted Cor and Seg scans and combine them into a high resolution object, creating reconstructed slices from all three planes and then I can segment the scan using thresholds on all the original and interpolated slices, it’s able to follow the bone area down to the CT pixel and creates a smooth and high polygon exportable model.<br>
Of course it’s less feature rich than slicer, but it does seem its a little more suited for creating an exportable model and able to use multiple planes to generate that reconstruction.<br>
                    <a href="https://i.imgur.com/kFJiJMT.png" target="_blank" rel="noopener nofollow ugc" class="onebox">
            <img src="https://i.imgur.com/kFJiJMT.png" width="690" height="399">
          </a>

</p>

---

## Post #5 by @pieper (2024-02-04 16:13 UTC)

<p>Is your data possible to share publicly?  If not, can you replicate any differences between InVesalius and Slicer using public data?  I’m sure the Slicer team wants to be sure we have the best possible reconstruction algorithms.</p>
<p>I’m still a bit skeptical that using the coronal and sagittal reconstructions would add any extra detail.  More likely there’s a difference in the surface generation and smoothing that explains what you are seeing.</p>

---
