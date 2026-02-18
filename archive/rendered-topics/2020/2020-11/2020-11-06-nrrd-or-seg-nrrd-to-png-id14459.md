# NRRD or SEG.NRRD to PNG

**Topic ID**: 14459
**Date**: 2020-11-06
**URL**: https://discourse.slicer.org/t/nrrd-or-seg-nrrd-to-png/14459

---

## Post #1 by @LuckyLuke (2020-11-06 06:58 UTC)

<p>So I have a request from somene to export his DICOM and NRRD files 5 of them into a set of PNG images.</p>
<p>Images are to be numbered and saved without losing any info, in other words either a lossless compression format or no compression at all.</p>
<p>What can I do now?</p>
<p>I have no idea why exactly he needs them saved as PNGs</p>

---

## Post #2 by @lassoan (2020-11-06 14:13 UTC)

<p>You can load the DICOM files and export the segmentation to labelmap volumes (using the GUI), then save them into a series of png as shown at the end of <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Rasterize_a_model_and_save_it_to_a_series_of_image_files">this script</a> (starting from line <code>outputLabelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass...</code>).</p>

---

## Post #3 by @LuckyLuke (2020-11-28 12:40 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="14459">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>utputLabelmapV</p>
</blockquote>
</aside>
<p>dear lassoan, first of all I want to thank you for all of your help. May God bless you sir.</p>
<p>Concerning this script, IF I understood you correctly, I just have to make a py file that contains this and then save it by running this script?</p>
<pre data-code-wrap="python"><code class="lang-python">outputLabelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(seg, outputLabelmapVolumeNode, referenceVolumeNode)
outputLabelmapVolumeArray = (slicer.util.arrayFromVolume(outputLabelmapVolumeNode) * outputVolumeLabelValue).astype('int8')

# Write labelmap volume to series of TIFF files
pip_install("imageio")
import imageio
for i in range(len(outputLabelmapVolumeArray)):
    imageio.imwrite(f'{outputDir}/image_{i:03}.tiff', outputLabelmapVolumeArray[i])
</code></pre>
<p>is this loseless? Will I lose some of the information?</p>

---

## Post #4 by @lassoan (2020-11-28 18:51 UTC)

<p>By saving into a series of 2D images, you lose 3D image geometry information (origin, spacing, and axis directions), so you cannot properly process the image in physical space. You also make your life harder and slow things down by storing your volume in hundreds of files instead of a single 3D image file.</p>

---

## Post #5 by @LuckyLuke (2020-11-28 20:15 UTC)

<p>I understand that orientation will be lost along with spacing and axis and direction.</p>
<p>But someone wants to print an entire set of images for some reason and also to share them only whatever and whichever they pick.</p>
<p>It is something they discovered on the scan and made high resolution scan of it.</p>
<p>Now they don’t want to always come and take screenshots or whatever but would simply like to have the entire thing in a set of pngs and just pick whichever png they want and send it to their colleague.</p>
<p>that is what they told me when they said they want it as pngs sequence.</p>

---

## Post #6 by @LuckyLuke (2020-11-28 20:16 UTC)

<p>so that is why my question is narrowly about the image color and resolution loss. If some information would be lost and if the lines I selected out are the correct ones. I can just enclose them in a notepadfile.py and then just run it?</p>

---
