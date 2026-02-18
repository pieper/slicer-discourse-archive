# MRI PET fusion "add scalar volumes" new volume with color & opacity settings

**Topic ID**: 40559
**Date**: 2024-12-07
**URL**: https://discourse.slicer.org/t/mri-pet-fusion-add-scalar-volumes-new-volume-with-color-opacity-settings/40559

---

## Post #1 by @anguilmot (2024-12-07 14:02 UTC)

<p>Hello everyone,</p>
<p>I’d like to create a DICOM serie from a MR-PET fusion.<br>
I have coregistred the two volumes.</p>
<p>I’d like to create a new volume with “add scalar volumes” module, using specific color and opacity settings for the two previous volumes (used in the general scene, cf image)</p>
<ul>
<li>Volume 1 “MR”, color “Grey”, auto level, opacity 1</li>
<li>Volume 2 “PET”, color “PET-Rainbow2” with window/level w: 8000 L: 5000, opacity 0.4</li>
</ul>
<p>I tried the command downhere in python console but it doesn’t work.<br>
Any help ?</p>
<p>I’m using 3Dslicer 5.6.2.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12844c986f62db480e7295edac0870dd8923a687.jpeg" data-download-href="/uploads/short-url/2DO2JTQ20cSzLj4KTQOLnhRp0IT.jpeg?dl=1" title="3Dslicer color &amp; opacity setting" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12844c986f62db480e7295edac0870dd8923a687_2_690x293.jpeg" alt="3Dslicer color &amp; opacity setting" data-base62-sha1="2DO2JTQ20cSzLj4KTQOLnhRp0IT" width="690" height="293" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12844c986f62db480e7295edac0870dd8923a687_2_690x293.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12844c986f62db480e7295edac0870dd8923a687_2_1035x439.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12844c986f62db480e7295edac0870dd8923a687_2_1380x586.jpeg 2x" data-dominant-color="3D3C3B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3Dslicer color &amp; opacity setting</span><span class="informations">1915×814 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<pre><code class="lang-auto"># Import necessary modules
import slicer

# Load volumes (replace with the paths to your actual volume files if needed)
volume1 = slicer.util.getNode('MR')  # Load MR volume
volume2 = slicer.util.getNode('PET')  # Load PET volume

# Set display parameters for MR volume
mr_display = volume1.GetDisplayNode()
mr_display.SetAndObserveColorNodeID('vtkMRMLColorTableNodeGrey')
mr_display.SetAutoWindowLevel(True)
mr_display.SetOpacity(1.0)

# Set display parameters for PET volume
pet_display = volume2.GetDisplayNode()
pet_display.SetAndObserveColorNodeID('vtkMRMLColorTableNodePET-Rainbow2')
pet_display.SetWindow(8000)
pet_display.SetLevel(5000)
pet_display.SetOpacity(0.4)

# Use Add Scalar Volumes module to create a fused volume
fused_volume = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode', 'FusedVolume')

parameters = {
    'inputVolume1': volume1,
    'inputVolume2': volume2,
    'outputVolume': fused_volume,
    'scaleFactor1': 1.0,  # Weight for MR
    'scaleFactor2': 1.0,  # Weight for PET
}

slicer.cli.run(slicer.modules.addscalarvolumes, None, parameters, wait_for_completion=True)

# Visualize the fused volume
fused_display = fused_volume.GetDisplayNode()
fused_display.SetAndObserveColorNodeID('vtkMRMLColorTableNodeGrey')  # Adjust color as needed
slicer.util.setSliceViewerLayers(background=fused_volume, foreground=volume2, foregroundOpacity=0.4)
</code></pre>

---

## Post #2 by @pieper (2024-12-07 16:24 UTC)

<aside class="quote no-group" data-username="anguilmot" data-post="1" data-topic="40559">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ecb155/48.png" class="avatar"> anguilmot:</div>
<blockquote>
<p>I’d like to create a DICOM serie from a MR-PET fusion.</p>
</blockquote>
</aside>
<p>How do you intend to use the result?  If you make a color image the typical DICOM container would be a SecondaryCapture (screen grab) but this is really just for display.  Do you plan to send this to some other system?</p>

---

## Post #3 by @anguilmot (2024-12-08 08:32 UTC)

<p>Actually, I’d like to be able to export the images to another viewer to share the results of 3DSlicer more easily.</p>
<p>Similarly, is there a solution to export labelled markups to DICOM series?<br>
(in order to compare the maxima of several intensity maps)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4c7b07df11906e7a632a50de4d70fe9483bded5.jpeg" data-download-href="/uploads/short-url/wDSH8WyRZZyfCyABPAPz5wrEVMx.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4c7b07df11906e7a632a50de4d70fe9483bded5.jpeg" alt="image" data-base62-sha1="wDSH8WyRZZyfCyABPAPz5wrEVMx" width="446" height="385"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">446×385 42.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you,</p>

---

## Post #4 by @pieper (2024-12-08 15:42 UTC)

<p>You should check what the other viewer supports, but if it’s a typical radiology system it probably only supports secondary capture for this kind of image.</p>
<p>In Slicer you can use the ScreenCapture module to acquire sweeps, or you can get them easily programmatically.  This will capture the rendered composite image plus whatever markups you have.</p>
<p>For whatever reason I don’t think we’ve ever hooked this up to make dicom secondary captures, but this would be a very reasonable thing to do using something like <a href="https://support.dcmtk.org/docs/img2dcm.html" class="inline-onebox">DCMTK: img2dcm: Convert standard image formats into DICOM format</a>.</p>

---
