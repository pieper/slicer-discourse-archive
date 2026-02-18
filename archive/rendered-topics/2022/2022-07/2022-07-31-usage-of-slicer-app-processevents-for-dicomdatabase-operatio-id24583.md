# Usage of slicer.app.processEvents() for dicomDatabase operations

**Topic ID**: 24583
**Date**: 2022-07-31
**URL**: https://discourse.slicer.org/t/usage-of-slicer-app-processevents-for-dicomdatabase-operations/24583

---

## Post #1 by @dvbower (2022-07-31 19:03 UTC)

<p>I have written a simple method to copy and rename DICOM files from my slicer database.  A code snippet is provided below.  I run this code within the slicer python interpreter.  It works, but I do not know if every <code>slicer.app.processEvents()</code> call is necessary.  Based on trial and error testing it seems to be required to update the slicer interpreter with information from the logging commands (since this loop can involve lots of files it’s helpful to have a real-time output (logger) to the slicer python interpreter).</p>
<p>Also, once the method has finished running, slicer is very laggy.  Do I need to do something else at the end of the method to clear some memory or refresh the interface?  Currently I rectify this issue by closing slicer and restarting (not ideal, but it seems to solve the lag issue).</p>
<p>I looked at the API documentation (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html" class="inline-onebox" rel="noopener nofollow ugc">slicer package — 3D Slicer documentation</a>), but I don’t see a reference to <code>slicer.app.processEvents()</code>.  Thanks!</p>
<pre><code>def copy_files(self, dry_run=True):
    db = slicer.dicomDatabase
    # make a new directory for output data
    out_dir = Path(db.databaseDirectory, "out")
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    patientList = db.patients()
    for patient in patientList:
        logger.info(f"Working on Patient: {patient}")
        studyList = db.studiesForPatient(patient)
        slicer.app.processEvents()
        for study in studyList:
            logger.info(f"Working on Study: {study}")
            seriesList = db.seriesForStudy(study)
            slicer.app.processEvents()
            for series in seriesList:
                logger.info(f"Working on Series: {series}")
                fileList = db.filesForSeries(series)
                slicer.app.processEvents()
                for filein in fileList:
                    # do stuff
                    pass
</code></pre>

---

## Post #2 by @cpinter (2022-08-01 12:28 UTC)

<p>I don’t see any reason for a slowdown like what you mention. Of course the “do stuff” part may be the reason but we don’t see that. What exactly started to lag?</p>
<p>Calling processEvents does not seem to be necessary, but if you want the log to appear real-time as you say you need it. Alternatively you can look at the log file instead of the Python window, and then you can remove the processEvents calls.</p>

---

## Post #3 by @dvbower (2022-08-03 10:00 UTC)

<p>OK thanks.  The lagging could be due to another process so I will continue to investigate.</p>

---
