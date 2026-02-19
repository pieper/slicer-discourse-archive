---
topic_id: 11508
title: "What Determines Dicom Import Image Type Ordering"
date: 2020-05-12
url: https://discourse.slicer.org/t/11508
---

# What determines DICOM import "Image Type" ordering?

**Topic ID**: 11508
**Date**: 2020-05-12
**URL**: https://discourse.slicer.org/t/what-determines-dicom-import-image-type-ordering/11508

---

## Post #1 by @mikebind (2020-05-12 19:27 UTC)

<p>Hello, I am importing DICOM Dixon images and am getting inconsistent ordering of the image types.  Slicer correctly identifies that there are 4 image types, but does not order them in a consistent way.  Other software (e.g. Horos) consistently orders them.   <a href="https://radiopaedia.org/articles/dixon-method?lang=us" rel="nofollow noopener">Dixon images </a> involve 4 series, a water image (W), a fat image (F), and two raw images from which the water and fat images are derived, one referred to as the in-phase (IP) and the other referred to as the opposite-phase (OP).<br>
Horos consistenly loads the water and fat pair first (in one series), then the OP series, then the IP series.</p>
<p>We have DICOM data from one patient imaging session where the whole lower half of the body was acquired in 4 slabs, each a Dixon set of 4 images.  In Slicer, slab 1 loads as follows:<br>
Image Type 1: IP<br>
Image Type 2: OP<br>
Image Type 3: F<br>
Image Type 4: W</p>
<p>Slab 2 loads in the order OP-W-IP-F<br>
Slab 3 loads in the order W-IP-F-OP<br>
Slab 4 loads in the order OP-F-W-IP</p>
<p>These slabs were all acquired on the same scanner in the same imaging session, but somehow the Slicer ordering of Image Types for each one is unique!</p>
<p>My question therefore is how Slicer assigns the order, and whether there is a way I can enforce a consistent ordering for Dixon images. Alternatively, is there a way I can incorporate the image type into the name of the imported volume?  For example, if instead of “Image Type 1” being appended to the node name, could “Image Type W” be appended?  The DICOM Metadata browser shows the (0008,0008) ImageType field as “[5] DERIVED, PRIMARY, W, W, DERIVED” for the Water images (or “[5] DERIVED, PRIMARY, OP, OP, DERIVED” for the OP images, etc.).</p>
<p>Thanks for any insight/help you can provide!</p>

---

## Post #2 by @pieper (2020-05-12 19:51 UTC)

<p>Have you tried the latest nightly build of Slicer?  We did some tweaks to the way series are subdivided based on tags a few weeks ago.</p>
<p>Also there are various ways Slicer can load images using what are called <code>DICOMPlugins</code> for example to process dMRI or PET/CT data.  I don’t recall that anyone has done anything with Dixon images, but if you can see detect pattern in the tags that you could translate into a small python script then it would be possible for the plugin to “grab” the images during import by setting a higher-than-default <code>confidence</code> when examining the files for load.  Then that plugin could organize the images in whatever way best fits the acquisition.</p>

---

## Post #3 by @mikebind (2020-05-12 19:56 UTC)

<p>Thanks, I’ve been on the 2020-4-7 build, I’ll try updating to the latest nightly.  I’ll also take a look at existing DICOM plugins to see how easy it looks to make one that does what I want.</p>

---

## Post #4 by @lassoan (2020-05-12 20:08 UTC)

<p>You can access all the DICOM tags of loaded volumes, see <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_access_tag_of_a_volume_loaded_from_DICOM.3F_For_example.2C_get_the_patient_position_stored_in_a_volume:">examples in script repository</a>.</p>
<p>If you rely on volume names in your workflow then you can write a script that automatically renames volumes after they are added to the scene, using any naming scheme.</p>

---

## Post #5 by @mikebind (2020-05-13 05:46 UTC)

<p>Thanks, that link was very helpful.  I look at the script repository all the time, and still sometimes miss when it already has the pieces I need to solve my problem. Just in case it is useful to others in the future, the Python function below (pasteable at the Slicer Python interactor prompt) will take automatically named scalar volumes loaded from Dixon DICOM series and tag them with the type of image they are (“F”, “W”, “IP”, or “OP”).  That is, it will take a name like “501: Legs_T1_Dixon - imageType 3” and change it to “501: Legs_T1_Dixon - F” if it is a “Fat” image, which is much more informative than “imageType 3”, when imageType 3 could be paired with any of the Dixon image types.</p>
<pre><code>def rename_dixon_dicom_volumes(volNodes=None):
  # substitutes the "imageType N" with the Dixon type ("F","W","OP", or "IP")
  # If volume is not a DICOM volume, then it is left unchanged
  import re
  if volNodes is None:
    # Gather all scalar volumes in the scene
    volNodes = []
    shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
    sceneItemID = shNode.GetSceneItemID()
    c = vtk.vtkCollection()
    shNode.GetDataNodesInBranch(sceneItemID,c,'vtkMRMLScalarVolumeNode')
    for idx in range(c.GetNumberOfItems()):
      volNodes.append(c.GetItemAsObject(idx))
  # Loop over all volumes, renaming only if DICOM and if node name matches r"imageType \d"
  for volNode in volNodes:
    uids = volNode.GetAttribute('DICOM.instanceUIDs') # empty for non DICOM volumes
    imageTypeField = '0008,0008' # DICOM field corresponding to ImageType
    if uids is not None:
      uid = uids.split()[0] # all of these UIDs have the same ImageType (at least so far as I tested)
      filename = slicer.dicomDatabase.fileForInstance(uid)
      imageType = slicer.dicomDatabase.fileValue(filename, imageTypeField) # looks like "DERIVED\PRIMARY\OP\OP\DERIVED"
      dixonType = imageType.split('\\')[2] # pulls out the 3rd entry in that field
      origVolName = volNode.GetName()
      # Substitute dixon type for 'imageType N'
      newName = re.sub(r'imageType \d', dixonType, origVolName)
      volNode.SetName(newName)</code></pre>

---
