# Create sphere brush to edit voxels values in scanners image without fixed position

**Topic ID**: 3521
**Date**: 2018-07-19
**URL**: https://discourse.slicer.org/t/create-sphere-brush-to-edit-voxels-values-in-scanners-image-without-fixed-position/3521

---

## Post #1 by @Laura (2018-07-19 08:41 UTC)

<p>Good morning,</p>
<p>I would need some help to finish my project as an intern working on segmentation of an organ on 3D Slicer.<br>
I have a segmented organ with white pixels over a black background (a vtkMRMLScalarVolumeNode).</p>
<p>I would like to add some missing white voxels to my segmented organ and erase others.<br>
I have tried working on Segment editor but it doesn’t work as I need.</p>
<p>I am looking for another way to do this but I don’t know how to proceed :</p>
<ul>
<li>how can I create a sphere brush (in 3D) in python which would be able to browse / scan my image (as a numpy array if necessary) thanks to mouse clicks’ of the user on the image</li>
<li>then, if the user clicks, tell to the sphere to turn the pixels of my image from their value to another one that I choose<br>
?<br>
Does someone have an idea ?</li>
</ul>
<p>I have read lots and lots of comments / topics / codes but I can’t find anything that I understand and able to add to my code easily (I am new on 3D Slicer)<br>
Thanks a lot in advance for your help<br>
Laura</p>

---

## Post #2 by @jamesobutler (2018-07-19 12:05 UTC)

<p>What type of data are you working with? MRI/CT/Ultrasound?</p>
<p>Also you write</p>
<blockquote>
<p>I have a segmented organ with white pixels over a black background</p>
</blockquote>
<p>but what Segment Editor effect did you use to do this? It sounds like you have instead just manipulated your 3D volume with image processing.</p>
<p>The effects in Segment Editor are used to create a 3D segment object. This isn’t used to modify the pixel values of your original image data.</p>

---

## Post #3 by @Laura (2018-07-19 12:13 UTC)

<p>First, thanks a lot for your answer !</p>
<p>At the beginning I have a scanner volume that I upload in dicom<br>
Then, I do some personalized image processing on my own in the python script and so at the end I have my segmented organ. In this segmented organ volume, my organ is white and all the other pixels that are not considered as my organ are black.</p>
<p>However, I would like to correct this segmentation by adding some pixels that have been forgotten to my segmented organ so put them at white.</p>
<p>On segment editor, I have tried “paint” but I don’t succeed in transferring the “painting area” into my organ segmented just to create only one volume image …</p>
<p>I have to admit that I am totally lost<br>
Thanks in advance if you could help<br>
Laura</p>

---

## Post #4 by @pieper (2018-07-19 12:32 UTC)

<p>Hi <a class="mention" href="/u/laura">@Laura</a> - maybe a few screen captures would help us understand your scenario better so we can help out.  I suspect what you want to do is use the results of your image processing as a labelmap based segmentation in Slicer that you can then operate on using the other effects in the Segment Editor.  Then you can access the results of editing via python to use for whatever other purposes you have in mind.</p>

---

## Post #5 by @Laura (2018-07-19 12:43 UTC)

<p>Thanks a lot !<br>
I try to be clear but it is difficult when you work for 6 months on a python script to explain what you imagine easily, sorry !</p>
<p>This is the initial volume scanner that I have when I upload :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d28fb959fc95bf0dac2161e55c56e1dfdef29a1.jpeg" data-download-href="/uploads/short-url/hRdujvKTq7L3zLs0DjtS3eG0OC5.jpg?dl=1" title="ircadvolinitial" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d28fb959fc95bf0dac2161e55c56e1dfdef29a1_2_690x276.jpg" alt="ircadvolinitial" data-base62-sha1="hRdujvKTq7L3zLs0DjtS3eG0OC5" width="690" height="276" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d28fb959fc95bf0dac2161e55c56e1dfdef29a1_2_690x276.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d28fb959fc95bf0dac2161e55c56e1dfdef29a1_2_1035x414.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d28fb959fc95bf0dac2161e55c56e1dfdef29a1_2_1380x552.jpg 2x" data-dominant-color="323239"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ircadvolinitial</span><span class="informations">1680×673 243 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then, I made some treatments to get that (with transparency first to see the result) :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e6213f0a04e1bcc36f273f2dac3ea0af7e24de9.jpeg" data-download-href="/uploads/short-url/dsX0Ou2cIqjaw0NR5B3nMGHCRXb.jpg?dl=1" title="finalvol" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5e6213f0a04e1bcc36f273f2dac3ea0af7e24de9_2_690x278.jpg" alt="finalvol" data-base62-sha1="dsX0Ou2cIqjaw0NR5B3nMGHCRXb" width="690" height="278" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5e6213f0a04e1bcc36f273f2dac3ea0af7e24de9_2_690x278.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5e6213f0a04e1bcc36f273f2dac3ea0af7e24de9_2_1035x417.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5e6213f0a04e1bcc36f273f2dac3ea0af7e24de9_2_1380x556.jpg 2x" data-dominant-color="404047"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">finalvol</span><span class="informations">1680×677 203 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The same image without the background original image is that : (where the organ has pixel 255 and the others pixels of the image are 0)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c62d4f49e13de83ce9174e05ff3bb19db4ca9e62.png" data-download-href="/uploads/short-url/sh9C7cX1iAdlxRtyRttAsFm9zEK.png?dl=1" title="volfinalcolors0255" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c62d4f49e13de83ce9174e05ff3bb19db4ca9e62_2_690x278.png" alt="volfinalcolors0255" data-base62-sha1="sh9C7cX1iAdlxRtyRttAsFm9zEK" width="690" height="278" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c62d4f49e13de83ce9174e05ff3bb19db4ca9e62_2_690x278.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c62d4f49e13de83ce9174e05ff3bb19db4ca9e62_2_1035x417.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c62d4f49e13de83ce9174e05ff3bb19db4ca9e62_2_1380x556.png 2x" data-dominant-color="47464D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">volfinalcolors0255</span><span class="informations">1680×679 32.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So, this is on this image that I would like to add white pixels (255) in some different voxels positions that I can’t defined…I would like that the user is able to click on voxel that he wants to convert as “voxels that belong to the organ segmented”</p>
<p>I hope that this is a little bit more clear with pictures !</p>
<p>Do you know a way to do that ?</p>
<p>Thanks a lot !<br>
Laura</p>

---

## Post #6 by @pieper (2018-07-19 13:21 UTC)

<p>Yes, that’s a huge help!  I have a better idea now.  What you can do is change your VolumeFinal into a segmentation first by making it a labelmap in the Volumes-&gt;Volume Information panel and then importing it into a Segmentation using the Segmentations module.  Once you have that, you can use the Segment Editor to add and remove parts of the label.  Then you can export it back to a labelmap or other things as needed.  Hope that helps.</p>
<p>Here’s the step to convert scalar volume to labelmap:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a932e91c9f8b7738fd7f0db73c71e8970c20fb2f.jpeg" alt="image" data-base62-sha1="o8NLBZAUtVXNZqAqD8xbMsJrzb1" width="559" height="118"></p>
<p>Here’s the place to import a labelmap to a segmentation:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ecc69dfb65ccf87a212891a0eb2696fc4cb5c87f.jpeg" alt="image" data-base62-sha1="xMCdwU21q36pjgaBigMjQGu5IR1" width="512" height="196"></p>

---

## Post #7 by @Laura (2018-07-19 13:31 UTC)

<p>I think that it is what I want to do but I look for doing it through my python script so I wil tell you if I have problems to do it pedagogically for a surgeon user !<br>
Thanks a lot, I would never think about doing these different steps in this order !<br>
Laura</p>

---

## Post #8 by @pieper (2018-07-19 14:00 UTC)

<p>Glad to know this is progress for you  <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>Once you know how you want things to work via the GUI, you can make them work via python scripting too.  If you search this forum for keywords segmentation and python and labelmap you’ll find lots of snippets.</p>
<p>This might be what you need:</p>
<aside class="quote quote-modified" data-post="10" data-topic="2360">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/import-labelmap-to-segmentation-node-in-batch-processing/2360/10">Import labelmap to segmentation node - in batch processing</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    There were a couple of problems: 

It is not enough to create the segmentation node but you need to also add to the scene. You can use slicer.mrmlScene.AddNewNodeByClass to create a node and add it to the scene in one step.

slicer.util.loadVolume loads file as scalar volume, while ImportLabelmapToSegmentationNode expects a labelmap volume; you need to use slicer.util.loadLabelVolume instead
Relative path was used for the input image. I’m not sure what is the working directory of Slicer. It is s…
  </blockquote>
</aside>


---

## Post #9 by @Laura (2018-07-19 14:50 UTC)

<p>Thank you so so much for your help !!!<br>
Laura</p>

---

## Post #10 by @Laura (2018-07-20 11:34 UTC)

<p>Good afternoon,</p>
<p>I have almost finished to do this thanks to your explanation but I have a problem at the last step : to convert my labelmapvolume into a scalarvolumenode…<br>
I have done this :</p>
<blockquote>
<p>def CorrectionFinale(self, masterVolumeNode, inputVolCor):<br>
# Etape 1 : creer un labelmap de mon volume final</p>
<pre><code>volumesLogic = slicer.modules.volumes.logic()
vollabel= volumesLogic.CreateAndAddLabelVolume(slicer.mrmlScene, inputVolCor, "labelmapfoie" )
labelmaptocorrect = volumesLogic.CreateLabelVolumeFromVolume(slicer.mrmlScene, vollabel, inputVolCor)    

# Etape 2 : Importation du labelmap dans le module segmentation pour creer une segmentation
segmentationNode = slicer.vtkMRMLSegmentationNode()
slicer.mrmlScene.AddNode(segmentationNode)
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetName("CorrectionSegmentationFoie")	
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(inputVolCor)
segmentationLogic = slicer.modules.segmentations.logic()
importlabelmaptocorrect = segmentationLogic.ImportLabelmapToSegmentationNode (labelmaptocorrect, segmentationNode)
segmentationNode.CreateClosedSurfaceRepresentation()

# Etape 3 : Correction de la segmentation par les effets paint / erase 
editorWidget = slicer.modules.segmenteditor.createNewWidgetRepresentation()
editorWidget.setMRMLScene(slicer.app.mrmlScene())
editorWidget.show()

labelmaptocorrect.GetImageData().Modified()
labelmaptocorrect.Modified()
</code></pre>
<p>def ExportFinal(self, masterVolumeNode):<br>
# Exporter le labelmap node de la segmentation<br>
seg = slicer.util.getNode(‘CorrectionSegmentationFoie’)<br>
labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLLabelMapVolumeNode’,‘LabelFoiefinal’)</p>
<pre><code>foiesegfin = slicer.modules.segmentations.logic().ExportAllSegmentsToLabelmapNode(seg, labelmapVolumeNode)
a = slicer.util.array('LabelFoiefinal')
volumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode',"VolumeFoieSegmente")
foieseg = slicer.util.updateVolumeFromArray(volumeNode, a)
</code></pre>
</blockquote>
<p>To explain, my first function creates my labelmap from my segmented organ volume, then import this labelmap into the segmentation module and finally do the different corrections thanks to “Segment editor”.</p>
<p>My second function is here to convert my labelmap corrected by Segment Editor into volume : to do that, I use the “export” to labelmap to update this labelmap. Then, I convert into array (a) my last labelmap.<br>
However, to convert from numpy array to vtkMRMLScalarVolumeNode, I don’t succeed…<br>
Maybe I have mixed up the features ?</p>
<p>I have also a little additional question : how can I check the ‘sphere brush’ in my ‘Segment editor’ module and force my “MasterVolume” to be my “labelmapfoie” ?</p>
<p>Thanks a lot for your help !<br>
Laura</p>

---
