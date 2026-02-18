# How to Load anyway option

**Topic ID**: 12479
**Date**: 2020-07-10
**URL**: https://discourse.slicer.org/t/how-to-load-anyway-option/12479

---

## Post #1 by @Anand_Mulay (2020-07-10 15:13 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/379d46afb1df004a5315b7f4c4b8534b600705cb.png" alt="image" data-base62-sha1="7VZdQLuUzLWsFkGxfjfYNBeImT1" width="503" height="118"></p>
<p>How can i pass this option when i’m loading the scalarVolume thought a script.<br>
this is my code in script</p>
<pre data-code-wrap="python"><code class="lang-python">DSVPC = DICOMScalarVolumePluginClass()
        db = slicer.dicomDatabase

        if(db.patients()):
            for patient in db.patients():
                for study in db.studiesForPatient(patient):
                    for series in db.seriesForStudy(study):
                        print('looking at series ' + str(series) + ' for patient ' + str(patient))
                        files = db.filesForSeries(series)
                        if len(files) &gt;= 1:
                            try:
                                self.importedVolume = DSVPC.load(DSVPC.examineForImport([files])[0])
                            except Exception as e:
                                logging.exception('Error at DSVPC.Load, Exception: '+ str(e))
</code></pre>
<p>cause its loading in editor with Regularization transform option turned on but it doesnt when i try load it through the script, i think because of the load anyway option we have in the editor.</p>

---

## Post #2 by @lassoan (2020-07-10 16:43 UTC)

<p>DICOM GUI is clearly separated from logic in recent Slicer-4.11 versions, so there should be no problems like this.</p>
<p>For example, see how you can load DICOM files using Slicer-4.11: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_load_DICOM_files_into_the_scene_from_a_folder">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_load_DICOM_files_into_the_scene_from_a_folder</a></p>

---
