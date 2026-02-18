# Importing Dicom Directory via Temporary Database

**Topic ID**: 11013
**Date**: 2020-04-06
**URL**: https://discourse.slicer.org/t/importing-dicom-directory-via-temporary-database/11013

---

## Post #1 by @Queen_Rei (2020-04-06 15:48 UTC)

<p>Hiya! I am trying to get the module I put together to run on the start-up of 3DSlicer. Right now I am getting the following error:</p>
<pre><code>  File "Z:/SegmentDicom/SegmentDicom/SegmentDicom/SegmentDicom.py", line 103, in LoadSegment
    with DICOMUtils.TemporaryDICOMDatabase() as db:
  File "Z:\Slicer 4.11.0-2020-03-24\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMUtils.py", line 306, in __enter__
    self.originalDatabaseDir = openTemporaryDatabase(self.temporaryDatabaseDir)
  File "Z:\Slicer 4.11.0-2020-03-24\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMUtils.py", line 206, in openTemporaryDatabase
    originalDatabaseDir = settings.value(slicer.dicomDatabaseDirectorySettingsKey)
AttributeError: module 'slicer' has no attribute 'dicomDatabaseDirectorySettingsKey'
</code></pre>
<p>This is the code snippet where the error is occuring</p>
<pre><code>    from DICOMLib import DICOMUtils
    loadedNodeIDs = []


    with DICOMUtils.TemporaryDICOMDatabase() as db:
      DICOMUtils.importDicom(dicomDataDir, db)
      patientUIDs = db.patients()
    for patientUID in patientUIDs:
      loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))
</code></pre>
<p>May the issue have to do with running this module on the start-up? And if it is, then is there a better way to have my module run automatically on startup~ Thank you in advance!!!</p>

---

## Post #2 by @lassoan (2020-04-06 18:25 UTC)

<p>Does the script work well if you launch it manually after Slicer is started?</p>

---

## Post #3 by @Queen_Rei (2020-04-06 18:52 UTC)

<p>Yes, it works perfectly fine after Slicer has fully loaded.<br>
I imagine that some elements need to load before running this module. In this case, is there some way I can add a delay to the module or have it load the dicom module before running?</p>

---

## Post #4 by @lassoan (2020-04-06 19:04 UTC)

<p>How do you launch your code at startup?</p>

---

## Post #5 by @Queen_Rei (2020-04-06 19:14 UTC)

<p>I just went into Application Settings and set the module to be the startup module.<br>
In code I have the logic running by having the apply button be true. Which to my understanding and the way it usually works is when the module loads the button, then the logic runs.</p>

---

## Post #6 by @lassoan (2020-04-06 19:23 UTC)

<p>At the time a module’s constructor is executed, not all the modules have been initialized yet. If you want to run in your module something at startup then you need to use <code>startupCompleted</code> signal of the application:</p>
<pre><code>slicer.app.connect("startupCompleted()", self.someMethodToRunAtStartup)</code></pre>

---

## Post #7 by @Queen_Rei (2020-04-06 20:12 UTC)

<p>Ohh! Thank you so much! This is what I have been searching for~</p>
<p>I would place this in the Widget Class of the module I created or somewhere else?</p>

---

## Post #8 by @lassoan (2020-04-06 20:52 UTC)

<p>This connection has to be created when the module is created (in the module class constructor), but it can call methods anywhere. Since widget is only created when you open the module the first time and module logic is created even later, the called method should be in the module class (or a static method in the widget or logic class).</p>

---

## Post #9 by @Queen_Rei (2020-04-08 14:00 UTC)

<p>Heya! Congrats on your anniversary!!! I believe I did what you suggested and placed the line slicer.app.connect in the Module Class.</p>
<p>I got the following error, which seems like the one I was having before.</p>
<blockquote>
<pre><code>Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "Z:\Slicer 4.11.0-2020-03-24\lib\Python\Lib\imp.py", line 170, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 678, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
  File "Z:/SegmentDicom/SegmentDicom/SegmentDicom/SegmentDicom.py", line 11, in &lt;module&gt;
    class SegmentDicom(ScriptedLoadableModule):
  File "Z:/SegmentDicom/SegmentDicom/SegmentDicom/SegmentDicom.py", line 137, in SegmentDicom
    slicer.app.connect("startupCompleted()", LoadSegment())
  File "Z:/SegmentDicom/SegmentDicom/SegmentDicom/SegmentDicom.py", line 40, in LoadSegment
    with DICOMUtils.TemporaryDICOMDatabase() as db:
  File "Z:\Slicer 4.11.0-2020-03-24\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMUtils.py", line 306, in __enter__
    self.originalDatabaseDir = openTemporaryDatabase(self.temporaryDatabaseDir)
  File "Z:\Slicer 4.11.0-2020-03-24\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMUtils.py", line 206, in openTemporaryDatabase
    originalDatabaseDir = settings.value(slicer.dicomDatabaseDirectorySettingsKey)
AttributeError: module 'slicer' has no attribute 'dicomDatabaseDirectorySettingsKey'
</code></pre>
</blockquote>

---

## Post #10 by @lassoan (2020-04-08 15:26 UTC)

<p>Maybe the signal is called too early. You can call a singleshot timer with a 1-second delay in the method that is called by startupCompleted to give some time for the DICOM module to initialize itself.</p>

---

## Post #11 by @Queen_Rei (2020-04-08 21:20 UTC)

<p>Turns out a 0.1 second delay using the solution you provided worked out! Thank you so much!!!</p>

---

## Post #12 by @Queen_Rei (2020-04-13 17:41 UTC)

<p>Hello there! I thought it be best I post in this thread since it is related.<br>
I found that when I don’t import the dicom directory manually before running the module it gives me the following error. It does work when I manually add it beforehand, but I would like to fully automate the process.</p>
<pre><code>Traceback (most recent call last):
  File "Z:/SegmentDicom/SegmentDicom/SegmentDicom/SegmentDicom.py", line 54, in ProceduralSegmentation
    loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))
  File "Z:\Slicer 4.11.0-2020-03-24\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMUtils.py", line 41, in loadPatientByUID
    raise IOError('No patient found with DICOM database UID %s' % patientUIDstr)
OSError: No patient found with DICOM database UID 1
</code></pre>
<p>This is the error that I am getting. Any idea on what I may be missing? Also happy to answer any details needed~</p>

---

## Post #13 by @lassoan (2020-04-13 17:54 UTC)

<p>You can only load images that have been already imported.</p>

---

## Post #14 by @Queen_Rei (2020-04-13 18:11 UTC)

<p>I took this code from the Nightly Script Repo for importing a dicom directory</p>
<pre><code>    dicomDataDir = "C:/Users/Public/Pictures"
    from DICOMLib import DICOMUtils
    loadedNodeIDs = []

    with DICOMUtils.TemporaryDICOMDatabase() as db:
      DICOMUtils.importDicom(dicomDataDir, db)
      patientUIDs = db.patients()
    for patientUID in patientUIDs:
      loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))
</code></pre>
<p>I put a 10 second delay just to make sure it wasn’t due to it loading right away and I found it gives me the same error and right before it this is posted:</p>
<blockquote>
<p>“DICOM indexer has successfully inserted 81 files [0.05s]”<br>
“DICOM indexer has successfully processed 82 files [0.15s]”<br>
“DICOM indexer has updated display fields for 81 files [0.02s]”</p>
</blockquote>

---

## Post #15 by @lassoan (2020-04-13 18:24 UTC)

<p>The code above is incorrectly indented, which deletes the DICOM database immediately after import is completed. See the code with correct indentation in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_load_DICOM_files_into_the_scene_from_a_folder">script repository</a>. Code indentation is not just formatting in Python, so you need to pay very close attention to it.</p>

---

## Post #16 by @Queen_Rei (2020-04-13 18:27 UTC)

<p>Wow, I completely missed that when I was pasting it in. Thanks for spotting that for me! I will do better to pay careful attention!!!</p>

---

## Post #17 by @BigBrotherHui (2021-12-24 08:04 UTC)

<p>hello,lassoan.i also have trouble in “AttributeError: module ‘slicer’ has no attribute ‘dicomDatabaseDirectorySettingsKey’”  when i just code the below code:</p>
<p>PythonQt::init();<br>
PythonQtObjectPtr context = PythonQt::self()-&gt;getMainModule();<br>
context.evalScript(“import DICOMLib”);<br>
context.evalScript(“slicer.util.selectModule(‘DICOM’)”);</p>
<p>i want import dicom by python script.but failed.i am troubled in this for 5 days.could you help me please?</p>

---

## Post #18 by @BigBrotherHui (2021-12-24 08:07 UTC)

<p>it’s very helpful to have someone’s email to sovle this trouble.</p>

---

## Post #19 by @lassoan (2022-03-13 05:26 UTC)

<p><code>slicer.dicomDatabaseDirectorySettingsKey</code> is set in the DICOM module. Probably you run this script too early, before the application has been fully started up. If you want to run a script after startup is completed then you can connect a slot to the <code>startupCompleted</code> signal of the application.</p>

---
