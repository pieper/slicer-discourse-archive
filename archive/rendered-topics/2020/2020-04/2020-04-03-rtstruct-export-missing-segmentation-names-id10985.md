# RTStruct Export Missing Segmentation Names

**Topic ID**: 10985
**Date**: 2020-04-03
**URL**: https://discourse.slicer.org/t/rtstruct-export-missing-segmentation-names/10985

---

## Post #1 by @rmd (2020-04-03 23:03 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.2</p>
<p>Hello Slicer Community,</p>
<p>I’m experiencing strange behavior when exporting RTStructs. Prior to Export, I have about 170 segments each representing a different biological structure as shown here:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b6eafd9224e85512b08a25dfea23e838bb8d96d6.png" data-download-href="/uploads/short-url/q6amB1qvgRZ3tDWfpU5QrUcNLO6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6eafd9224e85512b08a25dfea23e838bb8d96d6_2_690x431.png" alt="image" data-base62-sha1="q6amB1qvgRZ3tDWfpU5QrUcNLO6" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6eafd9224e85512b08a25dfea23e838bb8d96d6_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6eafd9224e85512b08a25dfea23e838bb8d96d6_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6eafd9224e85512b08a25dfea23e838bb8d96d6_2_1380x862.png 2x" data-dominant-color="CACDE3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1476×924 260 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I then export these segments to RTStruct using two methods both which show the same strange behavior:<br>
(1) Right clicking on Study and selecting export<br>
(2) programatically using the DicomRtImportExportPlugin module.</p>
<p>When I import the resulting RTStruct and image volume, I see that most or all all of the contours still exist as shown in the 3D window, but only 16 segments are found in the Subject hierarchy.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4155ef31fc706828806c87e2a369026aa358ab8.jpeg" data-download-href="/uploads/short-url/ugb0F1iZvEB4kIqwsaCbfMhjIGA.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d4155ef31fc706828806c87e2a369026aa358ab8_2_690x422.jpeg" alt="image" data-base62-sha1="ugb0F1iZvEB4kIqwsaCbfMhjIGA" width="690" height="422" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d4155ef31fc706828806c87e2a369026aa358ab8_2_690x422.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d4155ef31fc706828806c87e2a369026aa358ab8_2_1035x633.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4155ef31fc706828806c87e2a369026aa358ab8.jpeg 2x" data-dominant-color="D3D3E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1332×816 195 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It seems that somehow segments from the above photo are being grouped into segments in the below photo. I would expect that in the second photo, I would still have all ~170 segments listed on the left.</p>
<p>I looked into the rtstruct file and there were indeed only 16 elements in the (3006, 0039)  ROI Contour Sequence tag. Also, I opened the RTStruct in a different viewer, and all the contours are there but only grouped into 16 elements.</p>
<p>This all tells me that the export is not working correctly. Can anybody advise how to properly export all ~170 segments? I would need to do it using the DicomRtImportExportPlugin module.</p>
<p>Thanks<br>
Ryan</p>

---

## Post #2 by @Sunderlandkyl (2020-04-03 23:18 UTC)

<p>I can take a look at it.<br>
Can you upload the pre-export slicer scene somewhere?</p>

---

## Post #3 by @rmd (2020-04-04 01:25 UTC)

<p>Huge thanks!</p>
<p>Here is the pre-export scene:<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/ryanmdavis/TempDeleteMe" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars2.githubusercontent.com/u/7934809?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/ryanmdavis/TempDeleteMe" target="_blank" rel="nofollow noopener">ryanmdavis/TempDeleteMe</a></h3>

<p>Contribute to ryanmdavis/TempDeleteMe development by creating an account on GitHub.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #4 by @rmd (2020-04-05 17:59 UTC)

<p>A bit more information, I’m not sure if this is relevant but I am creating the image and segmentation nodes via the python interpreter. I’m wondering if the way that I’m defining the segments is impacting the export? Here is the code I’m using to define the segmentation nodes, segments, and perform the export:</p>
<pre><code>def createSegNode2(segmentationNode,imageNode,contours,name):
    # Create segmentation node where we will store segments
    #segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
    #segmentationNode.CreateDefaultDisplayNodes()

    # set up contour objects
    contoursPolyData = vtk.vtkPolyData()
    contourPoints = vtk.vtkPoints()
    contourLines = vtk.vtkCellArray()
    contoursPolyData.SetLines(contourLines)
    contoursPolyData.SetPoints(contourPoints)

    contour_count=-1
    for contour in contours:
        contour_count=contour_count+1
        with open(constants.SLICER_STATUS_LOC,"w") as file:
            file.write("For %s working on contour %d of %d: %s" % (name,contour_count,len(contours),str(contour)))
        
        startPointIndex = contourPoints.GetNumberOfPoints()
        contourLine = vtk.vtkPolyLine()
        linePointIds = contourLine.GetPointIds()
        for point in contour["points_rc"]:
            point_ras=RCS2RAS(point+[0],imageNode)
            point_ras[2]=contour["z_pos_mm"]
            linePointIds.InsertNextId(contourPoints.InsertNextPoint(point_ras))
        linePointIds.InsertNextId(startPointIndex) # make the contour line closed
        contourLines.InsertNextCell(contourLine)

    segment = slicer.vtkSegment()
    segment.SetName("_".join([name.split("_")[0]]+[name.split("_")[-1]]+name.split("_")[1:-1]))
    #segment.SetColor(segmentColor)
    segment.AddRepresentation('Planar contour', contoursPolyData)
    segmentationNode.GetSegmentation().AddSegment(segment)

# define image and segmentation nodes
imageNode=slicer.util.loadVolume(header["series_folder"]+files[0],properties={"show":False},returnNode=True)[1]
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes()
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(imageNode) 

# contours is a dictionary with contour names as keys and contour points in RCS
# here we loop through each contour and create a segmentation node. For this example, contours has about 170 key/value pairs, each representing a different structure
for seg in contours.keys():
    createSegNode2(segmentationNode,imageNode,contours[seg],seg)

# now place imageNode and segmentationNode under a new patient/study
shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
patientItemID = shNode.CreateSubjectItem(shNode.GetSceneItemID(),header["PatientID"])
studyItemID = shNode.CreateStudyItem(patientItemID,header["StudyInstanceUID"])
volumeImgShItemID = shNode.GetItemByDataNode(imageNode)
shNode.SetItemParent(volumeImgShItemID, studyItemID)
volumeSegShItemID = shNode.GetItemByDataNode(segmentationNode)
shNode.SetItemParent(volumeSegShItemID, studyItemID)

# create the dicom exporter object and the exportables
exporter = DicomRtImportExportPlugin.DicomRtImportExportPluginClass()
exportables = exporter.examineForExport(volumeSegShItemID)+exporter.examineForExport(volumeImgShItemID)

# perform the export
m=exporter.export(exportables)</code></pre>

---

## Post #5 by @cpinter (2020-04-06 08:43 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> I have a hunch that the export function has not been updated correctly after the implementation of the shared labelmaps, and the 170 segments are stored in 16 shared labelmaps that are not separated when doing the contour extraction during export.</p>

---

## Post #6 by @Sunderlandkyl (2020-04-06 13:30 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> Yes, I also had a hunch that it was connected to shared labemaps.</p>
<p>I’m taking a look at it now.</p>

---

## Post #7 by @rmd (2020-04-06 18:16 UTC)

<p>Thanks all for taking a look. If there is a quick short-term fix that would also be valuable since I was supposed to send my RTStructs to a colleague over the weekend. If that’s not possible, I totally understand.</p>
<p>I understand this is a complicated problem and sincerely appreciate the help.</p>

---

## Post #8 by @Sunderlandkyl (2020-04-06 19:09 UTC)

<p>I’ve created an issue to track this on the SlicerRT GitHub: (<a href="https://github.com/SlicerRt/SlicerRT/issues/137" rel="nofollow noopener">https://github.com/SlicerRt/SlicerRT/issues/137</a>).</p>
<p>Unfortunately it looks like my first guess was wrong and the problem is not connected to the shared labelmaps.</p>
<p>I don’t have any short-term fixes currently, but I’ll keep digging and let you know when I have a solution.</p>

---

## Post #9 by @gcsharp (2020-04-06 19:52 UTC)

<p>Thank you.  I grabbed the data and will take a look.</p>

---

## Post #10 by @gcsharp (2020-04-10 18:49 UTC)

<p>This was a plastimatch bug.  I have pushed a fix.  <a class="mention" href="/u/rmd">@rmd</a>, can you please test the Preview version?  You might need to wait for Sunday’s build to see the fix.</p>
<p>Also FYI, the structure names are stored in the ROIObservationLabel, which regrettably, has VR of “Short String.”   That means you are limited to 16 characters.  You may wish to rename your structures to something shorter!</p>

---

## Post #11 by @rmd (2020-04-10 21:51 UTC)

<p>Hi Greg</p>
<p>Sincere thanks for looking in to this, much appreciated! I’ll take a look at Sunday’s build when it’s available.</p>
<p>Also, thanks for the advice on the label names.</p>
<p>Ryan</p>

---

## Post #12 by @lassoan (2020-04-10 23:18 UTC)

<aside class="quote no-group" data-username="gcsharp" data-post="10" data-topic="10985">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>FYI, the structure names are stored in the ROIObservationLabel, which regrettably, has VR of “Short String.” That means you are limited to 16 characters. You may wish to rename your structures to something shorter!</p>
</blockquote>
</aside>
<p>It is shocking to see just how bad these first-generation DICOM RT data structures are (not just the general idea of using planar contours for representing segmentations but little details like this, too). <a class="mention" href="/u/gcsharp">@gcsharp</a> do you see any uptake of <a href="http://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_A.86.html">second-generation radiation therapy IODs</a> in current commercial systems?</p>

---

## Post #13 by @gcsharp (2020-04-11 23:37 UTC)

<p>Sadly no.  There seem to be two obstacles.  First, the current state of affairs is “just good enough” that things mostly work OK.  Second, all the vendors need to support first-generation DICOM-RT anyway.  It is hard to see a path forward.</p>

---

## Post #14 by @gcsharp (2020-04-13 13:13 UTC)

<p>I went and double checked this.  There are two places the name gets written, the other one is ROI Name which does allow LO (Long string).  So you might be ok with your naming convention.</p>

---
