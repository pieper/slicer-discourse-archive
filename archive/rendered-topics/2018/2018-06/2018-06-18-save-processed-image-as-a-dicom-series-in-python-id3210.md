---
topic_id: 3210
title: "Save Processed Image As A Dicom Series In Python"
date: 2018-06-18
url: https://discourse.slicer.org/t/3210
---

# Save processed image as a DICOM series, in python

**Topic ID**: 3210
**Date**: 2018-06-18
**URL**: https://discourse.slicer.org/t/save-processed-image-as-a-dicom-series-in-python/3210

---

## Post #1 by @gdenunzio (2018-06-18 10:07 UTC)

<p>Hi all,<br>
as it may be seen in my other post, <a href="https://discourse.slicer.org/t/rotation-of-a-ct-image-around-the-rt-isocenter-in-python/3203/2">“Rotation of a CT image around the RT isocenter, in python”</a>,<br>
I have succeeded in applying a rotation to my DICOM volume. I still have to be sure that the rotation is around the desired point, but first I wish to complete my code.<br>
I need now to save the rotated image as a DICOM series (with or without a DICOMDIR file) so that I can read it back into the TPS software.<br>
In other tools I’ve seen, this may be obtained by a call to a function which also gets as input a model DICOM series from which to import  some parameters and tags.<br>
How does it work in 3D Slicer? Should I send the image to the DICOM database and then export it?<br>
I really have no idea.<br>
It should be done programmatically, no GUI interaction.<br>
Thanks<br>
Giorgio</p>

---

## Post #2 by @lassoan (2018-06-18 13:58 UTC)

<p>I think this question has come up a few times already, see for example the answer here: <a href="https://discourse.slicer.org/t/dicom-export-of-segmentation-node/313/5">DICOM export of segmentation node</a>.</p>
<p>Slicer can build a CT image from scratch. I would recommend to start with exporting from GUI first, and once it confirmed to be working as expected, do the same using Python scripting.</p>
<p>Let us know if you have specific questions.</p>

---

## Post #3 by @gdenunzio (2018-06-22 10:15 UTC)

<p>Dear Andras,<br>
thanks for your kind reply!<br>
You are right, the question has come other times, but at present I have not found a working example. I admit I have had very little time to devote, so I’ll probably be luckier in the next future.</p>
<p>As to the link you gave, it is now broken: I’ve found the Author and written to him: he told the example is now old and does not work any more.  I’ll search further.</p>
<p>Anyway: here is a specific question.<br>
in my code I can now save the rotated volume as nnrd and it works. If I want to save as a DICOM series, should I first send the image node to the DICOM database, then export from there? Sorry, I know I should study more, before trying to build something…</p>
<p>Thanks<br>
Giorgio</p>

---

## Post #4 by @lassoan (2018-06-22 13:44 UTC)

<aside class="quote no-group" data-username="gdenunzio" data-post="3" data-topic="3210">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/67e7ee/48.png" class="avatar"> gdenunzio:</div>
<blockquote>
<p>he told the example is now old and does not work any more</p>
</blockquote>
</aside>
<p>Have you posted the question on the forum publicly or contacted someone privately? Private messages are not ideal, since you only rely on a single person to answer, and if you learn something then it will not be visible to the community.</p>
<p>If you don’t have much time then instead of writing an exporter script, it may be faster to export the files manually, as shown in this tutorial:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="nzWf4xHy1BM" data-video-title="Create DICOM files from CT volume and segmentation" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=nzWf4xHy1BM" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/nzWf4xHy1BM/maxresdefault.jpg" title="Create DICOM files from CT volume and segmentation" width="" height="">
  </a>
</div>


---

## Post #5 by @gdenunzio (2018-06-22 15:45 UTC)

<p>Hi, thanks again!</p>
<blockquote>
<p>Have you posted the question on the forum publicly or contacted someone privately?</p>
</blockquote>
<p>The link you gave me, i.e. <a href="https://discourse.slicer.org/t/dicom-export-of-segmentation-node/313">“DICOM export of segmentation node”</a><br>
led to a broken link to <a href="https://www.dropbox.com/s/j4cmpv5x7hupewy/20160826_DICOMVolumeExport_MatthewMouawad.py?dl=0" rel="noopener nofollow ugc">https://www.dropbox.com/s/j4cmpv5x7hupewy/20160826_DICOMVolumeExport_MatthewMouawad.py?dl=0</a><br>
which was a code by Matthew Mouawad,<br>
So I searched for Matthew on the Internet, I found him and directly wrote to him, who confirmed that his code is old and would not work now. He did not give the code to me anyway yet.</p>
<p>As to</p>
<blockquote>
<p>Private messages are not ideal, since … if you learn something then<br>
it will not be visible to the community.</p>
</blockquote>
<p>as you can see, I am reporting in my messages all the code I am writing, so I’m going to share everything I get to.</p>
<blockquote>
<p>If you don’t have much time then instead of writing an exporter script,<br>
it may be faster to export the files manually, as shown in this tutorial:</p>
</blockquote>
<p>Thanks for the link. I’ll watch it. Anyway, this is not a good option for me because I want to explore a whole space of rotation parameters, with the generation of dozens of rotated CT volumes, so I cannot save each transformed volume manually.</p>
<p>I am now studying this code:<br>
<a href="https://github.com/SlicerRt/SegmentRegistration/blob/master/ProstateMRIUSContourPropagation/ProstateMRIUSContourPropagation.py" rel="noopener nofollow ugc">https://github.com/SlicerRt/SegmentRegistration/blob/master/ProstateMRIUSContourPropagation/ProstateMRIUSContourPropagation.py</a><br>
which has DICOM export, but I still have to understand many things. Moreover, looking at the lines which actually perform the export:</p>
<pre><code># Open DICOM export dialog, selecting the study to export
exportDicomDialog = slicer.qSlicerDICOMExportDialog(None)
exportDicomDialog.setMRMLScene(slicer.mrmlScene)
exportDicomDialog.execDialog(deformedMrStudyShItemID)
</code></pre>
<p>they open the dialog and select the volume, but the dialog stil needs interaction with the user (a mouse click) for saving, so… ok, as I said I am still trying to understand.<br>
Thank you very much.<br>
Giorgio</p>

---

## Post #6 by @gdenunzio (2018-06-22 18:55 UTC)

<p>Here I am again, and here is the code snippet I’ve got to, for DICOM series saving (with some references in the comments):</p>
<pre><code>    # http://apidocs.slicer.org/master/classvtkMRMLSubjectHierarchyNode.html
    # shNode is a vtkMRMLSubjectHierarchyNode
    shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)

    # get the id of the first (and only) node in the node hierarchy, which is the patient
    # parent is shNode.GetSceneItemID()
    patientID = shNode.GetItemByPositionUnderParent (shNode.GetSceneItemID(), 0)
    # now get the id of the study
    studyID = shNode.GetItemByPositionUnderParent (patientID, 0)

    # Open DICOM export dialog, selecting the study to export
    exportDicomDialog = slicer.qSlicerDICOMExportDialog(None)
    exportDicomDialog.setMRMLScene(slicer.mrmlScene)
    exportDicomDialog.execDialog(studyID)
</code></pre>
<p>It kind of works: the dialog is open, the study after rotation is selected, I only have to:</p>
<ol>
<li>decide  where to save the series, by clicking in the Output Folder field, and inserting the directory of my choice</li>
<li>click on Export.</li>
</ol>
<p>Can I make these operations automatic? That is…</p>
<ol>
<li>How to set the output folder?</li>
<li>How to automatically execute the saving, without clicking?</li>
</ol>
<p>Perhaps some exportDicomDialog.setProperty() ?<br>
Thanks!<br>
Giorgio</p>

---

## Post #7 by @lassoan (2018-06-22 19:39 UTC)

<p>You can use the GUI to perform batch operations, but in general it is recommended to use logic classes, as it was done in the post that I’ve linked to.</p>
<p>Here is a complete working script, which exports a volume node to a selected folder:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_a_volume_to_DICOM_file_format" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_a_volume_to_DICOM_file_format</a></p>

---

## Post #8 by @lassoan (2018-06-22 19:43 UTC)

<p>By the way, why do you need to export so many DICOM images? Most image analysis applications that are flexible enough so that you can create batch processing scripts are also flexible enough to read non-DICOM images. What software do you use for further processing the exported DICOM files?</p>

---

## Post #9 by @gdenunzio (2018-06-23 10:20 UTC)

<p>Thanks Andras! I really don’t know how I could miss this very useful page…<br>
I’ve now implemented the code: I’ve understood how to create new nodes, to assign parents etc, to explore nodes by the “Data” icon in the tool bar, and to save as DICOM series the node I want (by selecting the good node by the right index).<br>
But…<br>
There is a problem again, and I am not understanding what’s going on.</p>
<p>After running, I see the rotated image in Slicer GUI, so the rotation was applied. The code succesfully saves the node to DICOM.</p>
<p>Then I close Slicer, I restart it and I load back the series just saved. Apart from this message:</p>
<p>“Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 0.000141992 mm, tolerance threshold is 0.001 mm)”</p>
<p>what matters is that I see the rotated volume in Slicer GUI, so everything is ok, isn’t it?<br>
Nope.</p>
<p>In fact, if I read the saved volume  by another DICOM reading tool (I tried with Sante Dicom Viewer and by Dicompyler) the volume is NOT rotated. Also, if I read single slices (I’ve tried with Pixillion, a non-specific image viewer) the slices are not rotated.</p>
<p>Moreover, even if in the Slicer GUI I see a rotated image, the mouse pointer shows “out of frame” for pixels that should be within the slice, had the rotation really be applied to the image space (the volume should be rotated, but the frame should be visualized as a square with horizontal base, not inclined).</p>
<p>My only hypothesis is: the rotation (which was around Z)  was written in the DICOM fields but the volume was not really rotated. This would be strange anyway because I applied multiple transforms (hoping to chain them), but OK, it is the only hypothesis.</p>
<p>So I thought to reslice and see what happens. Unfortunately, after resampling, no change anyway! As before, Slicer loads the resliced volume and shows the rotation, while the other DICOM viewers don’t.</p>
<p>By the way, another strange thing is that the various slices of the saved volume have each different WL/WW, with a horrible visual effect.</p>
<p>Again, any hint is welcome, I am getting mad…<br>
Thanks<br>
The current code follows (I’ve just dropped some comments; I’ll soon make it more readable with some function defs).<br>
Giorgio</p>
<pre><code>import argparse, sys, shutil, os, logging
import vtk, qt, ctk, slicer
import DICOMLib
from DICOMLib import DICOMUtils

def main(argv):
  print('STARTING!')
  try:
    parser = argparse.ArgumentParser(description="to be done")
    parser.add_argument("-i", "--input-folder", dest="input_folder", metavar="PATH",
                        default="-", required=True, help="Folder of input DICOM files (can contain sub-folders)")
    parser.add_argument("-o", "--output-folder", dest="output_folder", metavar="PATH",
                        default=".", help="Folder to save converted datasets")
    args = parser.parse_args(argv)
    if args.input_folder == "-":
      print('Please specify input DICOM study folder!')
    if args.output_folder == ".":
      print('Current directory is selected as output folder (default). To change it, please specify --output-folder')

    # Convert to python path style
    args.input_folder = args.input_folder.replace('\\', '/')
    args.output_folder = args.output_folder.replace('\\', '/')

    logging.info("Importing DICOM data from " + args.input_folder)
    DICOMUtils.openTemporaryDatabase()
    DICOMUtils.importDicom(args.input_folder)
    logging.info("Loading first patient into Slicer")
    patient = slicer.dicomDatabase.patients()[0]
    DICOMUtils.loadPatientByUID(patient)
    #logging.info(patient) # it is just a string containing the id number
	
    # APPLY TRANSFORMS, THEN SAVE	
    #
    node_key = 'vtkMRMLScalarVolumeNode*'
    sv_nodes = slicer.util.getNodes(node_key)
    
    for imageNode in sv_nodes.values(): 
		
        # Apply transform   https://www.vtk.org/doc/nightly/html/classvtkTransform.html   (Scale, Translate, RotateX, ...)
        logging.info("Applying transform")

        # Two ways, they seem equivalent, to be better understood
        var = True
        if var:
            vTransform = vtk.vtkTransform()
            vTransform.Translate(-0.88, 35.4, 5.65)  # translate by -isocenter
            vTransform.RotateZ(10)  # The angle is in degrees
            vTransform.Translate(0.88, -35.4, -5.65)
            imageNode.ApplyTransform(vTransform)
        else:
            transform = slicer.vtkMRMLLinearTransformNode()
            scene = slicer.mrmlScene
            scene.AddNode(transform) 
            imageNode.SetAndObserveTransformNodeID(transform.GetID())
            vTransform = vtk.vtkTransform()
            vTransform.Translate(-0.88, 35.4, 5.65)  # translate by -isocenter
            vTransform.RotateZ(10)  # The angle is in degrees
            vTransform.Translate(0.88, -35.4, -5.65)
            transform.SetAndObserveMatrixTransformToParent(vTransform.GetMatrix())
            #transform.SetMatrixTransformToParent(vTransform.GetMatrix())	
	          
	      # harden transform
        # https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting
        logic = slicer.vtkSlicerTransformLogic()
        logic.hardenTransform(imageNode)

        # Resample 
        doResample = True
        if doResample:
            logging.info("Resampling")
            #
            # Create output volume
            resampledImageNode = slicer.vtkMRMLScalarVolumeNode()
            resampledImageNode.SetName('Resampled')
            slicer.mrmlScene.AddNode(resampledImageNode)
            # Resample
            resampleParameters = {'outputPixelSpacing':'0,0,0', 'interpolationType':'lanczos', 'InputVolume':imageNode, 'OutputVolume':resampledImageNode.GetID()}
            slicer.cli.run(slicer.modules.resamplescalarvolume, None, resampleParameters, wait_for_completion=True)

        # DICOM
        #
        logging.info("Saving as DICOM series")
        # http://apidocs.slicer.org/master/classvtkMRMLSubjectHierarchyNode.html
        # shNode is a vtkMRMLSubjectHierarchyNode
        shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)

        # get the id of the first (and only) node in the node hierarchy, which is the patient
        # parent is shNode.GetSceneItemID()
        patientID = shNode.GetItemByPositionUnderParent (shNode.GetSceneItemID(), 0)
        # now get the id of the study
        studyID = shNode.GetItemByPositionUnderParent (patientID, 0)

        #volumeID = shNode.GetItemByPositionUnderParent (studyID, 0)   # original
        volumeID = shNode.GetItemByPositionUnderParent (studyID, 1)    # resampled

        #patientItemID = shNode.CreateSubjectItem(shNode.GetSceneItemID(), "Test patient")
        #studyItemID = shNode.CreateStudyItem(patientItemID, "Test study")
        #shNode.SetItemParent(volumeID, studyItemID)

        import DICOMScalarVolumePlugin
        exporter = DICOMScalarVolumePlugin.DICOMScalarVolumePluginClass()
        exportables = exporter.examineForExport(volumeID)
        for exp in exportables:
            exp.directory = args.output_folder
        exporter.export(exportables)

     #   slicer.mrmlScene.Clear(0)

  except Exception, e:
    print e
#  sys.exit()
  return

if __name__ == "__main__":
  main(sys.argv[1:])</code></pre>

---

## Post #10 by @gdenunzio (2018-06-23 10:24 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="3210" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>By the way, why do you need to export so many DICOM images? Most image analysis applications that are flexible enough so that you can create batch processing scripts are also flexible enough to read non-DICOM images. What software do you use for further processing the exported DICOM files?</p>
</blockquote>
</aside>
<p>The following image processing procedure is not in my hands: I know the images will be reloaded in a radiation Therapy treatment planning system, but at present there is no more info, as it is an in-fieri project. So I prefer to stick with DICOM series as the output of my code.<br>
Thanks<br>
Giorgio</p>

---

## Post #11 by @gdenunzio (2018-06-23 13:33 UTC)

<p>I’ve found this:<br>
<a href="https://discourse.slicer.org/t/image-with-hardened-transform-returns-to-original-when-opened-outside-slicer/431/2">https://discourse.slicer.org/t/image-with-hardened-transform-returns-to-original-when-opened-outside-slicer/431/2</a><br>
which is exactly what is happening to me!<br>
I now have to see how to call this “Resample Image (BRAINS)” from python.<br>
Thanks<br>
best<br>
Giorgio</p>

---

## Post #12 by @lassoan (2018-06-23 13:56 UTC)

<aside class="quote no-group" data-username="gdenunzio" data-post="10" data-topic="3210">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/67e7ee/48.png" class="avatar"> gdenunzio:</div>
<blockquote>
<p>reloaded in a radiation Therapy treatment planning system</p>
</blockquote>
</aside>
<p>I was just asking how the images are analyzed, as Slicer has an extensive adaptive radiation therapy toolkit (SlicerRT extension), which can be used to analyze and compare treatment plans.</p>

---

## Post #13 by @lassoan (2018-06-23 14:37 UTC)

<aside class="quote no-group" data-username="gdenunzio" data-post="11" data-topic="3210">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/67e7ee/48.png" class="avatar"> gdenunzio:</div>
<blockquote>
<p>I now have to see how to call this “Resample Image (BRAINS)” from python.</p>
</blockquote>
</aside>
<p>Yes, you need to harden a transform on the volume before saving or exporting.</p>
<p>“Resample Image (BRAINS)” resamples a volume in the exact same geometry as the chosen reference volume.</p>
<p>If you use a recent nightly version of Slicer, then you can also simply call <code>myVolumeNode.HardenTransform()</code> which performs only the minimum amount of resampling (it does not resample the volume if the transformation can be accomplished by adjusting image origin, spacing, and axis directions), and computes the updated extent automatically.</p>

---

## Post #14 by @lassoan (2018-06-23 14:56 UTC)

<aside class="quote no-group" data-username="gdenunzio" data-post="9" data-topic="3210">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/67e7ee/48.png" class="avatar"> gdenunzio:</div>
<blockquote>
<p>By the way, another strange thing is that the various slices of the saved volume have each different WL/WW, with a horrible visual effect.</p>
</blockquote>
</aside>
<p>In which software you see this? Can you reproduce it with Slicer sample data sets?</p>
<aside class="quote no-group" data-username="gdenunzio" data-post="9" data-topic="3210">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/67e7ee/48.png" class="avatar"> gdenunzio:</div>
<blockquote>
<p>The current code follows</p>
</blockquote>
</aside>
<p>The forum is not suitable for collaborating on code that is longer than a few lines, so if you share code then upload to GitHub instead and just post the link here.</p>
<aside class="quote no-group" data-username="gdenunzio" data-post="9" data-topic="3210">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/67e7ee/48.png" class="avatar"> gdenunzio:</div>
<blockquote>
<p>Moreover, even if in the Slicer GUI I see a rotated image, the mouse pointer shows “out of frame” for pixels that should be within the slice, had the rotation really be applied to the image space (the volume should be rotated, but the frame should be visualized as a square with horizontal base, not inclined).</p>
</blockquote>
</aside>
<p>This is a wrong assumption. DICOM stores image position and orientation, therefore it is not necessary to resample the image to apply arbitrary translations and rotations. Since information is lost and image quality is decreased when you resample a rotated image (unless you resample on a very high resolution grid, which is usually not a practical solution), it should be avoided, if possible.</p>
<p>You will only see the image content rotated in a “non-rotated” volume if you resample the volume using a non-rotated volume as reference. But again, this should not be necessary and somewhat lossy operation.</p>
<p>In contrast to most other software, Slicer exposes inherent complexities in medical image computing, which may be hidden in clinical software (to make things simpler and safer for users; but it means that there are many limitations, many operations are simply prohibited) and in custom in-house software (which often make incorrect assumptions, such as “image axis directions are always the same as anatomical axis directions”). Fortunately, Slicer has all the necessary tools to deal with these complexities, you just have to learn what is happening and why, and how you want to deal with them.</p>

---

## Post #15 by @gdenunzio (2018-07-07 18:09 UTC)

<p>Here I am again!<br>
I had other work to do and time elapses fast… now back to the problem.</p>
<p>Thanks Andras!</p>
<blockquote>
<p>In which software you see this? Can you reproduce it with Slicer sample data sets?</p>
</blockquote>
<p>The problem was only in Sante DICOM Viewer. I’ve later remarked that other viewers correctly use the same WL/WW in all the slides, so clarifying this has lower priority (but I’ll do it for completeness).</p>
<blockquote>
<p>The forum is not suitable for collaborating on code that is longer than a few lines, so if you share code then upload to GitHub instead and just post the link here.</p>
</blockquote>
<p>Here you are:<br>
<a href="https://github.com/giorgio-denunzio/3DSlicer" rel="noopener nofollow ugc">https://github.com/giorgio-denunzio/3DSlicer</a></p>
<blockquote>
<p>This is a wrong assumption. DICOM stores image position and orientation, therefore it is not necessary to resample the image to apply arbitrary translations and rotations.</p>
</blockquote>
<p>OK I see: the transformations are within the DICOM metadata, they are not actually applied to the voxels (with all the interpolation stuff etc).<br>
It is the task of the reading software, to understand, show, take into account the transformations.</p>
<p>Otherwise, if I need to actually take the voxels and move them in a non-rotated space, I should use “Resample Image (BRAINS)”.</p>
<p>Now, I:</p>
<ul>
<li>exported the series (rotated with the software you can see at my github site)</li>
<li>checked it with various DICOM reader, such as Amide, which sees the rotation</li>
<li>asked my colleagues in the hospital to reimport it into the Treatment Planning System.</li>
</ul>
<p>Here is what happened:</p>
<ul>
<li>Software “Monaco” does not allow the import, and gets out of the import dialog with no result</li>
<li>Software “Oncentra” recognizes the rotation (because, even if the image is shown non-rotated, a beam cast at 0* appears rotated); unfortunately, when trying to start calculations, the software gives an error (on SSD, Source-Surface Distance) and refuses to go on.</li>
</ul>
<p>As a conclusion, the problem is still to be solved, with two options:</p>
<ol>
<li>understand how to make the created series “good” for the TPS</li>
<li>understand how to use the “Resample Image (BRAINS)” from python, even if this means interpolation, which is not so good.</li>
</ol>
<p>Any hint will be really welcome!<br>
Thanks<br>
Giorgio</p>

---
