# How can one check if Slicer's DICOM database already exists?

**Topic ID**: 30159
**Date**: 2023-06-20
**URL**: https://discourse.slicer.org/t/how-can-one-check-if-slicers-dicom-database-already-exists/30159

---

## Post #1 by @Justin_Kirby (2023-06-20 16:53 UTC)

<p>I’m working on the TCIABrowser extension, which polls The Cancer Imaging Archive for available datasets and allows the user to directly download and import its DICOM data into Slicer.  While performing testing I noticed that the extension fails if I perform a fresh installation of Slicer and immediately try to download some data.  The issue is that if you haven’t already gone to the “Add DICOM Data” module yet, Slicer hasn’t created the DICOM database.  As a result, when our extension tries to import the data to the database it fails.  Is there a way we can check from our python code to see if the DICOM database exists and create it if there isn’t one?</p>

---

## Post #2 by @lassoan (2023-06-20 16:58 UTC)

<p>You can call <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOM/DICOM.py#L491">DICOMFileDialog.createDefaultDatabase()</a> to ensure that a DICOM database exists. If the function returns False then it means that the function failed to create a default DICOM database and you may ask the user to take care of it (e.g,. by going to the DICOM module and choosing a writable folder).</p>

---

## Post #3 by @SL2027 (2023-06-20 21:52 UTC)

<p>I’m working with Justin on the TCIABrowser extension. I tried to call DICOMFileDialog.createDefaultDatabase() inside TCIABrowser.py, and the python console in 3D Slicer threw an error saying there was no module named “dicomDatabase” in slicer. But when I manually import slicer and check the modules it has inside the console, I was able to find dicomDatabase. I checked the library path for slicer in both the code and the console, turned out they are using the identical path to import slicer. What might be the problem here?</p>

---

## Post #4 by @jamesobutler (2023-06-21 00:21 UTC)

<p>I’m not sure where you are calling this code in TCIABrowser. If it is part of setup you will want to define the DICOM module as a dependency for TCIABrowser if it is becoming a new dependency. That will make sure it loads first and then your module.</p>
<p>The DICOM module may also do additional setup after the startupCompleted signal so you may have to delay your usage of it as well as part of code executed after the startupCompleted signal. See the following thread below:</p>
<aside class="quote" data-post="9" data-topic="17128">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/module-executable-file/17128/9">Module executable file</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    It is possible you are trying to access it too early. Maybe do some of the setup in the module widget’s setup function. Or connect a slot to the startupCompleted signal and do it there. To connect: 
slicer.app.connect("startupCompleted()", self.onStartupCompleted)
  </blockquote>
</aside>


---

## Post #5 by @SL2027 (2023-06-21 03:30 UTC)

<p>Really appreciate your comment, this has resolved my issue.</p>

---
