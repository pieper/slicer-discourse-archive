# How to overlay more than two volumes

**Topic ID**: 8860
**Date**: 2019-10-22
**URL**: https://discourse.slicer.org/t/how-to-overlay-more-than-two-volumes/8860

---

## Post #1 by @sthirumal (2019-10-22 15:33 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.1</p>
<p>I am wondering if there is a way to overlay more than just two volumes. I know we can overlay two by setting them to foreground and background, but is there a way to add more layers? Reason being, I am using Slicer to look at 2D cell images, where each image highlights different proteins in the cell.</p>
<p>Expected behavior:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/593ae7e8ca99af9e1d3f9757df2b5a75be84bf33.png" data-download-href="/uploads/short-url/cJmHps4hgEBuK1YReUYCf7bRicr.png?dl=1" title="expected%20output%20-%20slicer%20forum" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/593ae7e8ca99af9e1d3f9757df2b5a75be84bf33_2_500x500.png" alt="expected%20output%20-%20slicer%20forum" data-base62-sha1="cJmHps4hgEBuK1YReUYCf7bRicr" width="500" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/593ae7e8ca99af9e1d3f9757df2b5a75be84bf33_2_500x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/593ae7e8ca99af9e1d3f9757df2b5a75be84bf33.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/593ae7e8ca99af9e1d3f9757df2b5a75be84bf33.png 2x" data-dominant-color="8C834B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">expected%20output%20-%20slicer%20forum</span><span class="informations">626×626 688 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The above is 3 images overlaid together, which is what I would like to be able to do. (This image was created in a different program)</p>
<p>Actual behavior:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bda6a3f1ff24bd39fc61596e912b54765e76b953.png" data-download-href="/uploads/short-url/r3JgzGSPdvqjufypzhZ684wUTE7.png?dl=1" title="actual%20output%20-%20slicer%20forum" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bda6a3f1ff24bd39fc61596e912b54765e76b953_2_525x500.png" alt="actual%20output%20-%20slicer%20forum" data-base62-sha1="r3JgzGSPdvqjufypzhZ684wUTE7" width="525" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bda6a3f1ff24bd39fc61596e912b54765e76b953_2_525x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bda6a3f1ff24bd39fc61596e912b54765e76b953.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bda6a3f1ff24bd39fc61596e912b54765e76b953.png 2x" data-dominant-color="524400"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">actual%20output%20-%20slicer%20forum</span><span class="informations">714×680 765 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The above image is from Slicer with only 2 images overlaid.</p>

---

## Post #2 by @pieper (2019-10-22 15:49 UTC)

<p>This is not currently supported (the two-layer limitation is pretty hard coded right now).  But it is something we would like to support for multi-channel use cases like you describe.</p>

---

## Post #3 by @lassoan (2019-10-22 16:05 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> do you envision changing the slice view pipeline or just adding a module that can create an RGB volume from a vector volume?</p>
<p><a class="mention" href="/u/sthirumal">@sthirumal</a> You can create a colored image by combining any number of volumes into a single volume using custom rules by writing a couple of lines of Python code. See this example for combining two volumes into a third volume: <a href="https://discourse.slicer.org/t/creating-volume-from-numpy/658/18" class="inline-onebox">Creating Volume from Numpy</a>. You can modify it to create a colored volume by creating a new vector volume instead of cloning the input scalar volume.</p>

---

## Post #4 by @pieper (2019-10-22 16:29 UTC)

<p>I don’t have a specific implementation in mind - I hope to learn more about the specific needs before forming a plan.</p>
<p><a class="mention" href="/u/blowekamp">@blowekamp</a> walked me through some use cases at Project Week and my current general thought is that we could have a version/variant of the Vector To Scalar module that allows you to assign primary colors to different channels of an input volume and then display it as a RGB image.  Or maybe a scalar volume with the channels mapped to different numerical ranges with a custom color lookup.  Another possibility would be custom node and display node types.</p>
<p>I’m not sure which approach would be best for segmentation, quantification, etc.</p>
<p>Of course a lot of this microscopy data is also large, so we need to also think about handling that aspect of things.</p>

---

## Post #5 by @blowekamp (2019-10-22 17:14 UTC)

<p>For the labeled microscopy case, you will generally have an image with many channels, or multiple images with channels. It is good to be able to assign each channel or molecular “marker” a string label and a color, then select which channels to visualize.</p>
<p>This is a rough block of SimpleITK code to do some of the work in a command line utility:</p>
<pre><code class="lang-auto">        # matplotlib named colors: https://matplotlib.org/3.1.0/gallery/color/named_colors.html
        color_list = ["red", "green", "blue", "cyan", "magenta", "yellow"]
        if len(image_list) == 3:
            color_list = ["cyan", "magenta", "yellow"]

        rescale = False
        out = None
        for img, marker, color_name in zip(image_list, marker_list, cycle(color_list)):

            color = mcolors.get_named_colors_mapping()[color_name]
            rgb_color = mcolors.to_rgb(color)

            print("Colorizing {0} with {1} [{2}]...".format(marker, color_name, rgb_color))
            img = sitk.Cast(img, sitk.sitkFloat32)
            if rescale:
                img = sitk.RescaleIntensity(img, outputMaximum=255)

            img = sitk.Compose([c * img for c in rgb_color])

            if out is None:
                out = img
            else:
                out += img

        del image_list
        out = sitk.Clamp(out, sitk.sitkVectorUInt8, 0, 255)
</code></pre>

---
