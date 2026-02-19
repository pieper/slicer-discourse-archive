---
topic_id: 12174
title: "Extract Images From Dicom"
date: 2020-06-23
url: https://discourse.slicer.org/t/12174
---

# Extract images from Dicom

**Topic ID**: 12174
**Date**: 2020-06-23
**URL**: https://discourse.slicer.org/t/extract-images-from-dicom/12174

---

## Post #1 by @Melodicpinpon (2020-06-23 11:26 UTC)

<p>Good aftrenoon,</p>
<p>I would like to export each slice of a dicom as an image.<br>
Ideally, it should be a sequence of png. slices with transparency; but it can also be a sequence of jpg, or a movie that respects the proportions of the slices (with a regular speed of movement through the volume).<br>
I have seen a topic covering this subject but did not understand what was the final solution.</p>
<p>Thank you for your help,</p>

---

## Post #2 by @Melodicpinpon (2020-06-23 12:02 UTC)

<p>This software, ‘IRFANVIEW’ does the job:<a href="https://www.youtube.com/watch?v=JatzYqDHftM;" rel="nofollow noopener">https://www.youtube.com/watch?v=JatzYqDHftM;</a><br>
but I guess that it can be done within 3DSlicer…</p>

---

## Post #3 by @dave3d (2020-06-23 12:58 UTC)

<p>It would be a really simple script in SimpleITK.  Something like this:</p>
<pre><code>import SimpleITK as sitk
img = sitk.ReadImage("source_image.dcm")
sitk.WriteImage(img, "target_image.png")</code></pre>

---

## Post #4 by @Mik (2020-06-23 13:00 UTC)

<p>If you need an open source converter, you can try a <a href="https://xmedcon.sourceforge.io/Main/Faq" rel="nofollow noopener">(X)MedCon</a>.</p>

---

## Post #5 by @lassoan (2020-06-23 13:27 UTC)

<p>A simple solution in Slicer is to use Screen Capture module. You can choose a slice view, position range, and number of images to export. Slicer offers a couple of features that the trivial export methods cannot directly do:</p>
<ul>
<li>save output as image sequence, animated GIF, or video</li>
<li>save markups, segmentations, etc. overlaid on the image (as you see it in the slice viewer)</li>
<li>create a lightbox (contact sheet) that shows slices on a single page (in recent Slicer versions)</li>
<li>save reformatted views (current orientation of the selected slice view is used)</li>
</ul>

---

## Post #6 by @Melodicpinpon (2020-06-23 13:35 UTC)

<p>Ooh, great, that’s exactly what I needed; thank you. By the way, is it possible to transform the black into a transparent at the moment of the screen capture?</p>

---

## Post #7 by @Melodicpinpon (2020-06-23 14:07 UTC)

<p>I achieve to visualise very contrasted dicoms inside blender after using a video of it as a mask, but I have very little control on it, since the alpha is recorded all at once and cannot be tweaked based on the original image…</p>

---

## Post #8 by @lassoan (2020-06-23 20:35 UTC)

<p>It is not clear what you are trying to achieve. Can you post a few screenshots?</p>
<p>Do you want to change image opacity depending on image intensity? Since Blender can do everything (it is the 3D Slicer of 3D modeling), I’m sure you can set this up there.</p>

---

## Post #9 by @Melodicpinpon (2020-06-24 10:26 UTC)

<p>Yes actually I have been trying to use the blender addon called ‘OrtogOnBlender’ (which is more a side version of Blender since) for a few days but keep on failing to use it; therefore I tried to do it by myself with the default 2.8 version and achieve to do it through two techniques:<br>
-the first passes through the conversion of a video sequence of the dicom, used a a mask on a white color, into a png-image sequence(serie) with alpha channel. It works well for contrasted images of bones.<br>
-the second is to import the dicom as images without alpha channel inside Blender, with an offset between the slices, and to set up a material based on nodes that tells the image to convert its black colour into transparent alpha; and it works even better since I can control not only the darkness but the transparency from the source.<br>
My problem is that each image has a different texture and therefore a different material, and that I need to plug the input driver of the alpha(transparency) into the color output of the texture, instead of the alpha output (as it is set by default). There is no way to batch this very simple action on hundreds of images without scripting and I do not write scripts… Nearly every other action, beside of nodes can be done simultaneously(multiple select and Alt-click the change), but not inside a node tree… I asked about it on several Blender forums but did not get any answer because there isn’t any, I think…</p>

---

## Post #10 by @lassoan (2020-06-24 15:36 UTC)

<p>It is not clear what you are trying to achieve. Can you post a few screenshots that shows what you have now and what is still not right?</p>

---

## Post #11 by @Melodicpinpon (2020-06-26 08:50 UTC)

<p>First method: how to convert a video into an image sequence with alpha channel (works well but gives very little control on the transparency)<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/2512308ad46c6c02f0684c6a15cb83294caf3fe3.png" data-download-href="/uploads/short-url/5hWDwulsCHaSdoV9wIpmInWx1BN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2512308ad46c6c02f0684c6a15cb83294caf3fe3_2_690x420.png" alt="image" data-base62-sha1="5hWDwulsCHaSdoV9wIpmInWx1BN" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2512308ad46c6c02f0684c6a15cb83294caf3fe3_2_690x420.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2512308ad46c6c02f0684c6a15cb83294caf3fe3_2_1035x630.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2512308ad46c6c02f0684c6a15cb83294caf3fe3_2_1380x840.png 2x" data-dominant-color="3F4041"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1905×1161 212 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Second method:importing the images without transparency and converting the black into transparent on each image (best option to control the transparency but no way to batch-use the setup on several images at the same time without scripting)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d49e39adba1ba00a9714ae589cc877fdd4fff3ce.jpeg" data-download-href="/uploads/short-url/ukUdDgtRnT1KzmD2Zy8yuWnzHTU.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d49e39adba1ba00a9714ae589cc877fdd4fff3ce_2_690x401.jpeg" alt="image" data-base62-sha1="ukUdDgtRnT1KzmD2Zy8yuWnzHTU" width="690" height="401" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d49e39adba1ba00a9714ae589cc877fdd4fff3ce_2_690x401.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d49e39adba1ba00a9714ae589cc877fdd4fff3ce_2_1035x601.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d49e39adba1ba00a9714ae589cc877fdd4fff3ce_2_1380x802.jpeg 2x" data-dominant-color="3F3F40"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1908×1109 391 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> of the original slice.<br>
And this is (one of) the (few) setup(s) proposed by default, when importing the image as a plane within blender.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52a0422444e7ddca66d5cfea03dcef30096eaf52.jpeg" data-download-href="/uploads/short-url/bMWvhsyq53FAaX99pwmcSLDW0Bs.jpeg?dl=1" title="screenshot.525" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52a0422444e7ddca66d5cfea03dcef30096eaf52_2_499x500.jpeg" alt="screenshot.525" data-base62-sha1="bMWvhsyq53FAaX99pwmcSLDW0Bs" width="499" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52a0422444e7ddca66d5cfea03dcef30096eaf52_2_499x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52a0422444e7ddca66d5cfea03dcef30096eaf52_2_748x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52a0422444e7ddca66d5cfea03dcef30096eaf52_2_998x1000.jpeg 2x" data-dominant-color="3E3F40"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshot.525</span><span class="informations">1145×1147 192 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I hope that helps…</p>

---

## Post #12 by @lassoan (2020-06-26 15:40 UTC)

<p>How would you like these slices to appear? As a volume? Or as a stack of slices (only the top-most slice content actually visible)? Can you draw a sketch, or photoshop an image that you would like to end up having?</p>

---

## Post #13 by @Melodicpinpon (2020-07-13 12:00 UTC)

<p>I’d like to be able to use the tools of this addon : <a href="https://www.youtube.com/watch?v=wB6RX6cHNHM&amp;list=UU3mvEp43suARFFv3BO4KJYA&amp;index=21" rel="nofollow noopener">https://www.youtube.com/watch?v=wB6RX6cHNHM&amp;list=UU3mvEp43suARFFv3BO4KJYA&amp;index=21</a>   ;<br>
<a href="https://www.youtube.com/watch?v=J4Jv13XwNPU" rel="nofollow noopener">https://www.youtube.com/watch?v=J4Jv13XwNPU</a><br>
The main tool that I need is to import a bunch of images (each slice) and to have the possibility to tweak the range of values showed. with a color ramp for exemple. I create a topic on the blender forum, you might be interested by the last post that is illustrated: <a href="http://blenderclan.tuxfamily.org/html/modules/newbb/viewtopic.php?topic_id=50034&amp;forum=1" rel="nofollow noopener">http://blenderclan.tuxfamily.org/html/modules/newbb/viewtopic.php?topic_id=50034&amp;forum=1</a></p>

---

## Post #14 by @lassoan (2020-07-13 14:14 UTC)

<p>This is available in Slicer’s “Volume rendering” module. You can get started quickly by choosing a preset and adjusting “Shift” slider. You also have full control over opacity, color, and gradient transfer functions so that you can make any selected intensity range visible and control its color and extract contours.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/aecb926a827e3f61dbc0a488b36aae637f0497bf.jpeg" data-download-href="/uploads/short-url/oWjeiTN6Soad5VC58elK7BBhnqL.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aecb926a827e3f61dbc0a488b36aae637f0497bf_2_690x331.jpeg" alt="image" data-base62-sha1="oWjeiTN6Soad5VC58elK7BBhnqL" width="690" height="331" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aecb926a827e3f61dbc0a488b36aae637f0497bf_2_690x331.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aecb926a827e3f61dbc0a488b36aae637f0497bf_2_1035x496.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aecb926a827e3f61dbc0a488b36aae637f0497bf_2_1380x662.jpeg 2x" data-dominant-color="D3CDCB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2855×1371 756 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>It should be much easier to use than Blender’s tool (as it is developed specifically for displaying clinical images) and it works with 4D volumes, can be combined with all the other quantification and analysis features, etc.</p>
<p>We’ll soon enable multi-volume rendering, which allows proper mixing of overlapping volumes (multiple volumes or different parts of the same volume rendered with different settings).</p>

---

## Post #15 by @lassoan (2021-01-06 15:37 UTC)

<p>A post was split to a new topic: <a href="/t/export-images-with-markups/15377">Export images with markups</a></p>

---

## Post #16 by @Melodicpinpon (2025-02-03 14:48 UTC)

<p>Hello everyone,<br>
I’m back on this issue: I need to export a series of images from either a multilayer tif, or a .nrrd volume. My purpose is to try and visualize these in another software to add other functions.</p>

---

## Post #17 by @park (2025-02-03 14:58 UTC)

<p>Hi <a class="mention" href="/u/melodicpinpon">@Melodicpinpon</a></p>
<p>This is the code to capture images with a transparent background in the 3D view.<br>
You can achieve a similar result in the 2D Slice view with slight modifications.</p>
<pre><code class="lang-auto"># Caputer 3D rendering window with transparent background
def c(path = 0):
    renderWindow = slicer.app.layoutManager().threeDWidget(0).threeDView().renderWindow()
    renderWindow.SetAlphaBitPlanes(1)
    wti = vtk.vtkWindowToImageFilter()
    wti.SetInput(renderWindow)
    wti.SetInputBufferTypeToRGBA()
    writer = vtk.vtkPNGWriter()
    now = datetime.datetime.now()
    if path == 0:
        nowDatetime = now.strftime('%Y-%m-%d-%H-%M-%S')
        writer.SetFileName("D:\\capture"+nowDatetime+".png")
    else:
        writer.SetFileName(path)

    writer.SetInputConnection(wti.GetOutputPort())
    writer.Write()


def d():
    viewNodeID = "vtkMRMLViewNode1"
    cap = ScreenCapture.ScreenCaptureLogic()
    view = cap.viewFromNode(slicer.mrmlScene.GetNodeByID(viewNodeID))
    now = datetime.datetime.now()
    nowDatetime = now.strftime('%Y-%m-%d-%H-%M-%S')
    cap.captureImageFromView(view, "D:\\capture"+nowDatetime+".png")
</code></pre>

---

## Post #19 by @Melodicpinpon (2025-02-24 13:45 UTC)

<p>I struggle with this script and many variations to effectively export these .png from a specific volume.</p>
<p>Isn’t there any default function to convert a volume into .png?<br>
It seems to be a pretty common function.</p>

---
