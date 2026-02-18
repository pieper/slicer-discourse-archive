# Tests failing in docker container in no window mode

**Topic ID**: 8357
**Date**: 2019-09-10
**URL**: https://discourse.slicer.org/t/tests-failing-in-docker-container-in-no-window-mode/8357

---

## Post #1 by @Alex_Vergara (2019-09-10 08:46 UTC)

<p>I am testing my extensions in a docker container and I have messages like this one</p>
<pre><code class="lang-auto">1: Traceback (most recent call last):
1:   File "/usr/src/Slicer-build/Slicer-build/lib/Slicer-4.11/qt-scripted-modules/DICOM.py", line 115, in performPostModuleDiscoveryTasks
1:     self.setDetailsPopup(DICOMWidget.getSavedDICOMDetailsWidgetType()())
1:   File "/usr/src/Slicer-build/Slicer-build/lib/Slicer-4.11/qt-scripted-modules/DICOMLib/DICOMWidgets.py", line 1019, in __init__
1:     super(DICOMDetailsWindow, self).__init__(dicomBrowser, parent)
1:   File "/usr/src/Slicer-build/Slicer-build/lib/Slicer-4.11/qt-scripted-modules/DICOMLib/DICOMWidgets.py", line 988, in __init__
1:     DICOMDetailsBase.__init__(self, dicomBrowser)
1:   File "/usr/src/Slicer-build/Slicer-build/lib/Slicer-4.11/qt-scripted-modules/DICOMLib/DICOMWidgets.py", line 94, in __init__
1:     self.promptForDatabaseDirectory()
1:   File "/usr/src/Slicer-build/Slicer-build/lib/Slicer-4.11/qt-scripted-modules/DICOMLib/DICOMWidgets.py", line 526, in promptForDatabaseDirectory
1:     self.dicomBrowser.schemaUpdateAutoCreateDirectory = True
1: AttributeError: 'NoneType' object has no attribute 'schemaUpdateAutoCreateDirectory'
</code></pre>
<p>The test command is like</p>
<pre><code class="lang-auto">1: Test command: /usr/src/Slicer-build/Slicer-build/Slicer "--no-splash" "--testing" "--launcher-additional-settings" "/builds/dosimetry4d-build/AdditionalLauncherSettings.ini" "--no-main-window" "--additional-module-paths" "/builds/dosimetry4d-build/lib/Slicer-4.11/qt-scripted-modules" "/builds/dosimetry4d-build/lib/Slicer-4.11/cli-modules" "/builds/dosimetry4d-build/lib/Slicer-4.11/qt-loadable-modules" "--python-code" "import slicer.testing; slicer.testing.runUnitTest(['/builds/dosimetry4d-build/Dosimetry4D/Logic', '/builds/project-0/Dosimetry4D/Logic'], 'Dosimetry4DTest')"
</code></pre>
<p>I have tried to write the <code>DatabaseDirectory</code> variable inside the ini with</p>
<pre><code class="lang-auto">sed  '/\[General\]/a DatabaseDirectory=/usr/src/SlicerDB' /builds/dosimetry4d-build/AdditionalLauncherSettings.ini
</code></pre>
<p>and also to set up a function that forces slicer to have a temporal database as in the DICOMWidgets example like this one</p>
<pre><code class="lang-python">    def forceSlicerDB():
        '''
        forces Slicer to initialize a temporary database
        '''
        if not hasattr(slicer, 'dicomDatabase') or not hasattr(slicer.modules, 'dicom'):
            databaseDirectory = Path("/usr/src/SlicerDB")
            databaseDirectory.touch()
            DICOMLib.DICOMWidgets.settings.setValue('DatabaseDirectory', str(databaseDirectory))
            slicer.dicomDatabase = ctk.ctkDICOMDatabase()
            slicer.dicomDatabase.openDatabase(str(databaseDirectory / "ctkDICOM.sql"), "SLICER")
            slicer.app.setDICOMDatabase(slicer.dicomDatabase)
            DICOMLib.setDatabasePrecacheTags()

            # slicer.modules.DICOMInstance.performPostModuleDiscoveryTasks()
</code></pre>
<p>But no success so far, what am I doing wrong in these approaches?<br>
Calling <code>slicer.modules.DICOMInstance.performPostModuleDiscoveryTasks()</code> just raises a non database exception</p>
<pre><code class="lang-auto">1: Traceback (most recent call last):
1:   File "/usr/src/Slicer-build/Slicer-build/lib/Slicer-4.11/qt-scripted-modules/DICOM.py", line 115, in performPostModuleDiscoveryTasks
1:     self.setDetailsPopup(DICOMWidget.getSavedDICOMDetailsWidgetType()())
1:   File "/usr/src/Slicer-build/Slicer-build/lib/Slicer-4.11/qt-scripted-modules/DICOMLib/DICOMWidgets.py", line 1019, in __init__
1:     super(DICOMDetailsWindow, self).__init__(dicomBrowser, parent)
1:   File "/usr/src/Slicer-build/Slicer-build/lib/Slicer-4.11/qt-scripted-modules/DICOMLib/DICOMWidgets.py", line 988, in __init__
1:     DICOMDetailsBase.__init__(self, dicomBrowser)
1:   File "/usr/src/Slicer-build/Slicer-build/lib/Slicer-4.11/qt-scripted-modules/DICOMLib/DICOMWidgets.py", line 94, in __init__
1:     self.promptForDatabaseDirectory()
1:   File "/usr/src/Slicer-build/Slicer-build/lib/Slicer-4.11/qt-scripted-modules/DICOMLib/DICOMWidgets.py", line 526, in promptForDatabaseDirectory
1:     self.dicomBrowser.schemaUpdateAutoCreateDirectory = True
1: AttributeError: 'NoneType' object has no attribute 'schemaUpdateAutoCreateDirectory'
</code></pre>

---

## Post #2 by @lassoan (2019-09-11 13:53 UTC)

<p>Try the latest version. We’ve submitted a fix yesterday to only show the database folder update popup if DICOM module is activated.</p>

---

## Post #3 by @Alex_Vergara (2019-09-12 11:59 UTC)

<p>Tested with lastest version, errors are gone now! Thanks</p>

---
