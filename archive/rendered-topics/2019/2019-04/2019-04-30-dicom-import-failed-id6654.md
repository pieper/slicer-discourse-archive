---
topic_id: 6654
title: "Dicom Import Failed"
date: 2019-04-30
url: https://discourse.slicer.org/t/6654
---

# DICOM import failed

**Topic ID**: 6654
**Date**: 2019-04-30
**URL**: https://discourse.slicer.org/t/dicom-import-failed/6654

---

## Post #1 by @prorai (2019-04-30 14:26 UTC)

<p>i saw this error in log file ,when my script for model import is failed . these are the last few lines.</p>
<pre><code>self.importedVolume = DSVPC.load(DSVPC.examineForImport([files])[0])
  File "C:/Program Files/Slicer 4.10.1/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py", line 429, in load
    addAcquisitionTransformIfNeeded=self.acquisitionGeometryRegularizationEnabled())
  File "C:/Program Files/Slicer 4.10.1/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py", line 693, in createAcquisitionTransform
    self.gridTransformFromCorners(volumeNode, self.originalCorners, self.targetCorners)
  File "C:/Program Files/Slicer 4.10.1/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py", line 599, in gridTransformFromCorners
    displacements = slicer.util.arrayFromGridTransform(gridTransform)
  File "C:\Program Files\Slicer 4.10.1\bin\Python\slicer\util.py", line 870, in arrayFromGridTransform
    nshape = tuple(reversed(displacementGrid.GetDimensions()))
AttributeError: 'NoneType' object has no attribute 'GetDimensions'</code></pre>

---

## Post #2 by @prorai (2019-05-07 07:41 UTC)

<p>i notice that this is happening after i have enabled ‘apply regularization transform’ in the application setting</p>

---

## Post #3 by @lassoan (2019-05-07 23:20 UTC)

<p>Can you load the volume successfully by using the DICOM browser user interface? (with “apply regularization transform” enabled)</p>

---

## Post #4 by @prorai (2019-05-09 07:33 UTC)

<p>yes, its working in user interface.</p>

---

## Post #5 by @lassoan (2019-05-09 16:48 UTC)

<p>Then the issue is in your script. Could you copy the script or a URL to its source code repository?</p>

---

## Post #6 by @prorai (2019-05-10 07:46 UTC)

<pre><code>    from DICOMScalarVolumePlugin import DICOMScalarVolumePluginClass
    result = utils.importDicom(self.path)
    DSVPC = DICOMScalarVolumePluginClass()
    db = slicer.dicomDatabase

    if(db.patients()):
        for patient in db.patients():
            for study in db.studiesForPatient(patient):
                for series in db.seriesForStudy(study):
                    print('looking at series ' + str(series) + ' for patient ' + str(patient))
                    files = db.filesForSeries(series)
                    if len(files) &gt;= 1:
                        self.importedVolume = DSVPC.load(DSVPC.examineForImport([files])[0])

                        # TODO use bodypart information to determine what segments are expected to be present, or some other way to determine what segments types should be created
                        import dicom
                        data = dicom.read_file(files[0])
                        # for info in data: print('file ' + str(files[0]) + ' has data: ' + str(info))
                        self.bodyPartExamined = data.get('BodyPartExamined')
                        print('dicom header has info bodyPartExamined: ' + str(self.bodyPartExamined))
</code></pre>
<p>this the area where i’m getting error , basically while importing DICOM files , one more thing i get this issue when i use --no–window mode.</p>

---

## Post #7 by @lassoan (2019-05-11 04:15 UTC)

<p>Thank you for the code, it helped a lot. The problem is that you force the DICOMScalarVolumePlugin to load all kinds of data you have in your database. You need to use the appropriate plugin for each data type.</p>
<p>If you are only interested in scalar volumes, you can keep using only DICOMScalarVolumePlugin but catch exceptions thrown by <code>DSVPC.load(...)</code>.</p>

---

## Post #8 by @prorai (2019-05-13 08:24 UTC)

<p>i’m handling the exception now, but still getting same error messages</p>

---

## Post #9 by @lassoan (2019-05-13 11:37 UTC)

<p>Yes, you will still get errors for information objects that cannot be loaded as scalar volumes, but if you catch the correct exception for them you can still load everything else.</p>

---
