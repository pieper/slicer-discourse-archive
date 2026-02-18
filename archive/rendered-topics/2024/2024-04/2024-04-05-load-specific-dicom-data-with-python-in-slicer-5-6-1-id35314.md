# Load specific DICOM Data with Python in Slicer 5.6.1

**Topic ID**: 35314
**Date**: 2024-04-05
**URL**: https://discourse.slicer.org/t/load-specific-dicom-data-with-python-in-slicer-5-6-1/35314

---

## Post #1 by @paleomariomm (2024-04-05 14:31 UTC)

<p>I created this script in Python to load iteratively different CTs stored in different folders under a same root folder.</p>
<p>In some CTs I came across something unexpected. In the example of next image I loaded <strong>Patient</strong> W-584, selected the <strong>Study date</strong> 20080521 and the <strong>Series</strong> <span class="hashtag-raw">#2</span>.<br>
If I check the lower right checkbox “ADVANCED” and click on the button <strong>Examine</strong>, <em><strong>I only want to load what is squared in red in the image</strong></em>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20e1c74bc0d0acd66314b8445027f38014c53cb7.png" data-download-href="/uploads/short-url/4GT0rU0AfaEgH8T624Cv9IugIe3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20e1c74bc0d0acd66314b8445027f38014c53cb7_2_690x432.png" alt="image" data-base62-sha1="4GT0rU0AfaEgH8T624Cv9IugIe3" width="690" height="432" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20e1c74bc0d0acd66314b8445027f38014c53cb7_2_690x432.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20e1c74bc0d0acd66314b8445027f38014c53cb7_2_1035x648.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20e1c74bc0d0acd66314b8445027f38014c53cb7_2_1380x864.png 2x" data-dominant-color="F0F2F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2291×1437 439 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is the script I created to load iteratively the CTs:</p>
<pre><code class="lang-auto">import os
from DICOMLib import DICOMUtils

yourpath = r"C:/Users/mario.modesto/Desktop/test"

# walk through DICOM directory
# https://stackoverflow.com/questions/77865010/run-python-script-in-each-subfolder-automatically
for dir in os.scandir(yourpath):
    # Load DICOM files
    dicomDataDir = dir.path  # path to input folder with DICOM files
    baboon_skull  = dir.name
    loadedNodeIDs = []  # this list will contain the list of all loaded node IDs

    # 1. Load DICOM files
    # https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#dicom
    with DICOMUtils.TemporaryDICOMDatabase() as db:
        DICOMUtils.importDicom(dicomDataDir, db)
        patientUIDs = db.patients()
        for patientUID in patientUIDs:
            loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))
    # Next two lines introduced to know number which volumes and how many are
    # This is important to "2. Load volume", the "if-else" statement
    print(loadedNodeIDs)
    print(len(loadedNodeIDs))

    # 2. Load volume
    # https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#display-volume-using-volume-rendering
    logic = slicer.modules.volumerendering.logic()
    # This "if-else" is to select the second volume to skip the Topogram, which is the first
    # When there are two volumes, the topogram is the first and the full skull is the second
    if len(loadedNodeIDs) == 1:
      volumeNode = slicer.mrmlScene.GetNodeByID('vtkMRMLScalarVolumeNode1')
    else:
      volumeNode = slicer.mrmlScene.GetNodeByID('vtkMRMLScalarVolumeNode2')
</code></pre>
<p>As you can see in the <code>#2. Load volume</code>, I created a if/else statement because in some cases, the CTs have 2 sereies, and depending on the number, I select either the first or second.</p>
<p>However, how can I include in the code to load that specific DICOM data which is always named identically (<em>2: InnerEarSeq 0.6 U75u</em>)?</p>

---

## Post #2 by @pieper (2024-04-05 17:51 UTC)

<p>The message indicates irregular slice spacing (could be missing slices or it might have been acquired with variable table motion for some reason).  It means Slicer will generate an <a href="https://github.com/Slicer/Slicer/commit/3328b81211cb2e9ae16a0b49097744171c8c71c0">acquisition transform</a> to regularize the geometry and thus you get back two loaded nodes.</p>
<p>You can look at the loaded volume for that series and if you agree that the acquisition transform is the right way to fix it you can add something like this to your script:</p>
<pre><code class="lang-auto">            volumeNode = slicer.util.getNode(loadedNodeIDs[0])
            if len(loadedNodeIDs) == 2 and loadedNodeIDs[1].find("GridTransform") != -1:
                volumeNode.HardenTransform()
</code></pre>

---

## Post #3 by @paleomariomm (2024-04-15 14:01 UTC)

<p>I tried this and didn’t work <a class="mention" href="/u/pieper">@pieper</a></p>
<p>I know this warning is present (btw, I am sure the correct value is 0.60), but my question is before this part, on the loading process of this DICOM CTs.</p>
<p>In order to replicate what I am facing loading it, the CT I am using is open source on MorphoSource. You can download the DICOM files in this link:</p>
<p><a href="https://www.morphosource.org/concern/media/000058941?locale=en" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.morphosource.org/concern/media/000058941?locale=en</a></p>
<p>When you import the DICOM, it creates a lot of volumes, as specified in the original question above, rather than one single volume with all the CTs inside.</p>
<p>Can you please download it and try to load the skull CT of this baboon?</p>
<p>Best</p>

---

## Post #4 by @lassoan (2024-04-15 17:59 UTC)

<p>This data set is not a single 3D acquisition and the spacing is neither 0.5 nor 0.6. The data is acquired as 52 images, within each image the spacing is 0.6mm, but between the images the spacing is only 0.5mm. If you assume overall uniform spacing then the spacing is about 0.58mm. If the slice position fields in the DICOM header are correct then the image has varying slice spacing.</p>
<p>It is suspicious that maybe some inaccurate post-processing was applied on the data, because the slice positions along the third axis were specified with very low precision - just 1 digit after the decimal point - while 9 digits were used for positions along the first two axes.</p>
<p>Overall, Slicer handled these issues well, generally staying on the safe side (not silently ignoring inaccuracies or changing the data without asking). I agree that the user experience was not ideal, because you had to enable advanced mode and change some settings - but it was all due to trying to load the data set as a single uniformly-spaced 3D volume, while the data set is actually something else.</p>
<p>We introduced the DICOM Patcher module to allow fixing commonly occurring issues before a data set is imported into Slicer. If you often come across data sets that are messed up like this then we could add a new rule that could force the same acquisition number to all instances in the same series. Also, if you get confirmation from the authors of the data set or from the scanner manufacturer  that the spacing was actually uniform (0.5, 0.6, or 0.58) and it was just not correctly written into the DICOM file, then you could add a rule for correcting the slice position values automatically.</p>
<p>If you want to automatically harden the acquisition transform on the volume after import then you can enable that in menu: Edit / Application settings / DICOM / Acquisition geometry regularization → Harden regularization transform.</p>

---

## Post #5 by @paleomariomm (2024-04-16 11:10 UTC)

<p>Hi Andras,</p>
<p>I just emailed the Data Manager to know which is the spacing.</p>
<p>However, I still wonder how can I code if finally is 0.58 in Python. Any idea?</p>
<p>Best</p>

---

## Post #6 by @lassoan (2024-04-16 11:50 UTC)

<p>I would then recommend to add a rule to DICOM patcher module that fixes the files. You can then import and load the image as a 3D volume normally.</p>

---

## Post #7 by @paleomariomm (2024-04-16 11:56 UTC)

<p>Hi Andras, thanks for the tip. Can you share a link where I can learn on how to add a DICOM patcher?</p>

---

## Post #8 by @lassoan (2024-04-16 12:22 UTC)

<p>The DICOM Patcher module is a simple Python script that iterates through all files in a folder and applies a set of rules on it (when it starts a processing, when it starts processing each folder, each file, etc. see details <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMPatcher/DICOMPatcher.py#L759-L808">here</a>). You can add your own rule by adding a GUI option and a new rule class as it is done <a href="https://github.com/Slicer/Slicer/commit/861bc7e61a5aea3b556a907c92d585fdcb581463">here</a>. It is possible that you need to perform some action at the very end (e.g., you may want to collect all position values, analyze them, and rewrite all in the end) - in this case you can add a new method to the rule class and call that in the end.</p>

---

## Post #9 by @paleomariomm (2024-04-16 15:12 UTC)

<p>Hi Andras, thanks. I will check it tomorrow.</p>
<p>Best</p>

---

## Post #10 by @chz31 (2024-04-17 04:02 UTC)

<p>Hi Andras, thank you for the suggestions. Based on looking at the examples you provided, does that mean we can use the functions from <code>pydicom</code> to manually set up a proper spacing like 0.58 for loading all the dataset from the same dataset? Hope my understanding is all right, though I haven’t figured out how to do it yet.</p>

---

## Post #11 by @lassoan (2024-04-17 04:07 UTC)

<p>Yes, if you get confirmation from the scanner manufacturer or the technician who acquired the scan that the slice positions were incorrectly written to the file (or you consider up to 0.1mm error negligible) then you can create a rule that automatically detects such images and updates the slice positions in them.</p>
<p>If you are unsure if the slice positions are correct or not then probably the best is to only modify the acquisition number in the files, let Slicer create then regularization transform, and harden it on the image.</p>

---

## Post #12 by @chz31 (2024-04-24 03:50 UTC)

<p>Hi Andras, sorry for the late response. I am using this snippet to modify the Slice thickness of each dcm image into 0.6 and image pixels into 0.292969: <a href="https://github.com/chz31/test/blob/main/test_py_dicom.py" class="inline-onebox" rel="noopener nofollow ugc">test/test_py_dicom.py at main · chz31/test · GitHub</a>.<br>
I still got the same warning of <code>0.6 spacing was expected, 0.5 spacing was found between files</code>.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c4c0c721042cb628c83de7e020225e1a8c112c2.png" data-download-href="/uploads/short-url/fs2v0PpjqndAkWTJ7jj5CTuDCme.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c4c0c721042cb628c83de7e020225e1a8c112c2_2_690x197.png" alt="image" data-base62-sha1="fs2v0PpjqndAkWTJ7jj5CTuDCme" width="690" height="197" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c4c0c721042cb628c83de7e020225e1a8c112c2_2_690x197.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c4c0c721042cb628c83de7e020225e1a8c112c2_2_1035x295.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c4c0c721042cb628c83de7e020225e1a8c112c2_2_1380x394.png 2x" data-dominant-color="E8E8E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1912×546 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The sample data I used is the same dataset <a class="mention" href="/u/paleomariomm">@paleomariomm</a> provided <a href="https://www.morphosource.org/concern/media/000058941?locale=en" rel="noopener nofollow ugc">https://www.morphosource.org/concern/media/000058941?locale=en</a></p>

---

## Post #13 by @lassoan (2024-04-24 04:19 UTC)

<p><code>Slice Thickness</code> is characterizing how well the imaging was focused on the slice plane. It is not related the slice’s position and not used for determining the image geometry. I would recommend not to touch this field.</p>
<p>If you want to alter the slice spacing then you need to modify the <code>Image Position Patient</code> field.</p>

---

## Post #14 by @chz31 (2024-04-24 14:44 UTC)

<p>Thank you! I’ll look into it.</p>

---
