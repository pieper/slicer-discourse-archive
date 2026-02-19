---
topic_id: 24565
title: "Resize An Image By Averaging"
date: 2022-07-29
url: https://discourse.slicer.org/t/24565
---

# Resize an image by averaging?

**Topic ID**: 24565
**Date**: 2022-07-29
**URL**: https://discourse.slicer.org/t/resize-an-image-by-averaging/24565

---

## Post #1 by @drakewilliams (2022-07-29 13:08 UTC)

<p>Hi,<br>
I’m working with microct images (animal) and we typically only need a small area (teeth) for analysis even though we have a much larger volume scanned (whole skull). My computer is underpowered to load the whole skull (as I’m sure is true for many in academic research). One way I can get around the computational requirements for loading the whole skull is by having an option to resize the images (i.e. instead of loading it as a 1024x1024x#slices, load it as a 256x256x#slices or even less). From there, I could quickly load the dataset and set the coordinates of the cropping volume, since resolution is not that important for cropping. The cropping volume coordinates could then be applied to the original dataset at full resolution and analysis could be performed on a much smaller, but full resolution volume. Is this possible?</p>

---

## Post #2 by @lassoan (2022-07-29 13:37 UTC)

<p>We already have this feature in SlicerMorph extension’s <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks">ImageStacks module</a>, but that only works for jpg/tiff/png stack, not for DICOM.</p>
<p>Unfortunately, reconstructing an image from DICOM files is already very complicated (they can be unevenly sliced, have different orientation, they may need to be grouped and sorted, etc.) and the GUI is already too complex for most users, so it would be hard to add preview+ROI loading there.</p>
<p>You can also increase the virtual memory size in your computer. That will make it possible to load arbitrarily large image, it will be just slow (potentially very slow).</p>
<p>If your laptop/PC does not have enough memory to load these images then you may rent a computer from any cloud provider for just doing these conversions. The loading and cropping should be very quick, so it should not cost more than a few dollars. Only the data upload may take a while, depending on your network connection speed, but you can do that while the cloud computer is offline.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> and his collaborators work a lot with such images, maybe he has some more ideas.</p>

---

## Post #3 by @drakewilliams (2022-07-29 18:03 UTC)

<p>ImageStacks is exactly what I was looking for. Thank you!</p>

---

## Post #4 by @lassoan (2023-03-21 02:09 UTC)



---
