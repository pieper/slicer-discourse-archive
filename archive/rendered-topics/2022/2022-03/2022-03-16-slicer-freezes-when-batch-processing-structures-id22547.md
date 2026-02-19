---
topic_id: 22547
title: "Slicer Freezes When Batch Processing Structures"
date: 2022-03-16
url: https://discourse.slicer.org/t/22547
---

# Slicer freezes when batch processing structures

**Topic ID**: 22547
**Date**: 2022-03-16
**URL**: https://discourse.slicer.org/t/slicer-freezes-when-batch-processing-structures/22547

---

## Post #1 by @JosephBae (2022-03-16 19:08 UTC)

<p>Hi! This is my first post in the forums, so please forgive if it is improperly placed. I’ve tried to search the forums a bit for this issue, and have definitely found some useful threads to get me to this point, but am now at a bit of a loss.</p>
<p>Adapting some code from the SlicerRT folks, I’ve created a script that suits my particular use case for processing structure sets for multiple patients in batch mode. Essentially, I am uploading a reference image and structure set for each patient into my DICOM database, and then using the following script to convert a set of identified structure sets into .nii files for each patient.</p>
<p>This seems to mostly work, but always results in Slicer not responding for up to 30 mins to an hour until the script finishes going through all patients or sometimes even crashing entirely. I’m not sure what might be causing that specifically, or if there might be a better way to achieve what I am trying to achieve.</p>
<pre><code class="lang-auto">import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import argparse
from DICOMLib import DICOMUtils
import pandas as pd
import os
import numpy as np
bad=[]
slicer.mrmlScene.Clear(0)
outputdir="INSERT OUTPUT DIR HERE"
TVNames=vtk.vtkStringArray()
all_patients = slicer.dicomDatabase.patients()
StructKey=pd.read_csv("INSERT PATH TO CSV WITH STRUCTURE NAMES HERE")
DesiredStructs=("Tumor","Nodes","Peritumoral","LeftNeck","RightNeck")
for ROI in DesiredStructs:
    if not os.path.isdir(os.path.join(outputdir,ROI)):
        os.mkdir(os.path.join(outputdir,ROI))
for patient in all_patients:
    slicer.mrmlScene.Clear(0)
    DICOMUtils.loadPatientByUID(patient)
    volumeNodes = slicer.util.getNodesByClass('vtkMRMLSegmentationNode')
    CTNodes= slicer.util.getNodesByClass('vtkMRMLScalarVolumeNode')
    Currentdfrow=StructKey.loc[StructKey['MRN']==int(TestMRN)]
    for ROI in DesiredStructs:
        counter=0 #track if we found a structure. Sometimes our file key has a typo
        if type(Currentdfrow[ROI].iloc[0])==np.float64 or type(Currentdfrow[ROI].iloc[0])==float:
            continue # Move on if we don't find a structure name for this patient
        DesiredIDs=[]
        for target in Currentdfrow[ROI].iloc[0].split(', '): #sometimes we have multiple structures for a single thing split by commas. for example GTV1,GTV2
            DesiredIDs.append(target) #add names from our target spreadsheet into our list 
        for myNode in volumeNodes:
            shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
            ShItemID = shNode.GetItemByDataNode(myNode)
            ParentID = shNode.GetItemParent(ShItemID)    
            GPAID = shNode.GetItemParent(ParentID)
            MRN = shNode.GetItemAttribute(GPAID, 'DICOM.PatientID')
            desiredList=vtk.vtkStringArray()
            children = vtk.vtkIdList()
            shNode.GetItemChildren(ShItemID, children)
            DesiredSegmentID = vtk.vtkStringArray()
            DesiredCTNode=CTNodes[0]
            for i in range(children.GetNumberOfIds()):
                child = children.GetId(i)
                segmentName=shNode.GetItemAttribute(child,'segmentID')

                if segmentName in DesiredIDs:
                    DesiredSegmentID.InsertNextValue(segmentName)
                    counter=1
            if counter==0:
                bad.append(ROI+"__"+MRN) #couldn't find a structure matchning names in our desired list
                continue
            filename=os.path.join(outputdir,ROI,ROI+"__"+MRN+".nii.gz")
            referenceVolumeShItem = shNode.GetItemByDataNode(DesiredCTNode) 
            ROINode=slicer.vtkMRMLLabelMapVolumeNode()
            slicer.mrmlScene.AddNode(ROINode)
            slicer.modules.segmentations.logic().ExportSegmentsToLabelmapNode(myNode,DesiredSegmentID, ROINode, DesiredCTNode)
            myStorageNode = ROINode.CreateDefaultStorageNode()
            myStorageNode.SetFileName(os.path.join(outputdir,filename))
            myStorageNode.WriteData(ROINode)
</code></pre>

---

## Post #2 by @lassoan (2022-03-16 19:25 UTC)

<p>Slicer is expected to not respond to any user requests during batch processing. If you make the script do a lot of processing then then it may be normal that you need to wait hours for the operation to complete.</p>
<p>To see what takes long time you can add logs or <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/overview.html#python-debugging">run the script in a Python debugger</a> and step through the code. If you find anything specific that looks unreasonable (e.g., indexing a single patient data set takes tens of minutes) then let us know.</p>

---

## Post #3 by @JosephBae (2022-03-16 19:45 UTC)

<p>Thanks for the information! Will see if there’s anything wonky going on with the runtimes, but I’d guess the time things are taking are not unreasonable.</p>

---

## Post #4 by @lassoan (2022-03-16 20:23 UTC)

<p>If you find that running everything in one batch (without restarting Slicer) is less stable then it might be due to keeping unneeded things in memory. You can reorganize the script or your data folders to process one or a maybe up to a few dozens of patients in one session and then restart Slicer.</p>

---
