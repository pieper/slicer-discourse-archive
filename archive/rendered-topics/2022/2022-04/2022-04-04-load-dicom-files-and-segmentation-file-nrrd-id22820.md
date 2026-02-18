# Load DICOM files and segmentation file (.nrrd)

**Topic ID**: 22820
**Date**: 2022-04-04
**URL**: https://discourse.slicer.org/t/load-dicom-files-and-segmentation-file-nrrd/22820

---

## Post #1 by @SergioReinosa (2022-04-04 15:01 UTC)

<p>Hi guys,</p>
<p>I have to do a python script that must open a DICOM series from a folder and load a segmentation in that same scene. It has a part that loads the series and other that loads a segmentation. Both parts work perfectly when used isolated, but when combined it fails sometimes.</p>
<p>I think it is because it tries to load the .nrrd before the DICOM is completely loaded. I’ve been trying to introduce some comprobations to see if it is loaded completely but it didn’t work.</p>
<p>Here is my complete code:</p>
<pre><code class="lang-auto">def main():

    # ----- Load of DICOM series ----------

    loadedNodeIDs = []  # this list will contain the list of all loaded node IDs

    if len(sys.argv) &gt; 1:
        dicomDataDir = sys.argv[1]
        dicomDataDir.encode('unicode_escape')
    else:
        dicomDataDir = r'C:\Users\Sergio\Desktop\Slicer\OriginalDICOM'

    DICOMUtils.importDicom(dicomDataDir)
    dicomFiles = slicer.util.getFilesInDirectory(dicomDataDir)
    loadablesByPlugin, loadEnabled = DICOMUtils.getLoadablesFromFileLists([dicomFiles])
    loadedNodeIDs = DICOMUtils.loadLoadables(loadablesByPlugin)
    #loadedNodeIDs.getNodesByClass("vtkMRMLScalarVolumeNode")
    while(not slicer.util.getNodesByClass("vtkMRMLScalarVolumeNode")): # Kind of comprobation to see if there is any volume loaded so it doesnt try to load the segmentation so early, I think it crashes if it does so
        sys.sleep(2)
        continue

    # ------ Load of segmentation ----------

    seg = slicer.util.loadSegmentation(r'C:\Users\Sergio\Desktop\Slicer\Python\F0QalYvbzsoZhi.nrrd')
    seg.GetSegmentation().SetConversionParameter("Smoothing factor", "0.30")
    seg.CreateClosedSurfaceRepresentation() 

slicer.app.connect("startupCompleted()",main()) ### SEGUNDO PARAMETRO LAS INSTRUCCIONES A REALIZAR, EN ESTE CASO HABRÍA QUE HACER UNA FUNCIÓN
</code></pre>
<p>It just crashes, does not show any error message, and it crashes less times when the .nrrd is smaller and more when it is bigger.</p>

---

## Post #2 by @lassoan (2022-04-05 04:22 UTC)

<p>Does it work well if you use the latest Slicer Preview Release?</p>

---

## Post #3 by @SergioReinosa (2022-04-05 08:43 UTC)

<p>No, it doesn’t, I don’t know exactly why. I’ve tried the 4.13-2022-03-19 version and the 4.13-2022-04-01 version, this last one I just downloaded it, even though it says there is a 2022-04-04 one.</p>
<p>I have it working properly for the moment in the last stable version, the 4.11-20210226, but I found another problem. In this version it loads everything ok, but the segmentation does not display in 3D, it appears hidden so you have to go to the segmentEditor and set every segment visible. The code is the same.</p>
<p>Is there any way that I can introduce in my script to set all segments visible?</p>
<p>Thank you for your reply.</p>

---

## Post #4 by @lassoan (2022-04-07 12:46 UTC)

<p>Don’t use the latest Slicer Stable Release, it is too old and will be replaced by the latest Slicer Preview Release very soon.</p>
<p>If no Slicer core changes are made then the date of the installer remains the same. So, a few days difference compared to today’s date is completely normal.</p>
<p><code>sys.sleep(2)</code> just blocks the application for a while, it will not make any difference except slice w down the loading. You can use <code>slicer.app.processEvents()</code> for allowing all modules react to the loading of a new data set.</p>

---
