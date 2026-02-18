# Running Slicer without GUI?

**Topic ID**: 11720
**Date**: 2020-05-26
**URL**: https://discourse.slicer.org/t/running-slicer-without-gui/11720

---

## Post #1 by @lennymartinez (2020-05-26 17:36 UTC)

<p>I’ve installed Slicer on an Ubuntu cloud instance (AWS/GCP) and I want to run it with a self-made extension and no GUI… Is there documentation on the slicer site that I’m missing to be able to do this? I’ve found info about using Python to do things, but I want to essentially go: Slicer, do this task, using this folder, and put the output in this location.</p>

---

## Post #2 by @pieper (2020-05-26 19:08 UTC)

<p>Is docker an option for you?  <a href="https://github.com/pieper/SlicerDockers#running-a-slicer-analysis-script-in-an-instance">Here’s an example</a> of a command line tool based on Slicer and <a href="https://github.com/QIICR/dcmheat/blob/master/docker/SlicerConvert.py">this is another one</a>.  If you don’t use docker you would need a different way of having a desktop to access all of Slicer.  If you don’t need graphics you might be able to get by with PythonSlicer and access just logic classes.</p>
<p>Maybe you can describe your processing task in more detail if you need more explicit suggestions.</p>

---

## Post #3 by @lennymartinez (2020-05-26 19:19 UTC)

<p>I have dicom images I want to turn into OBJ models using an extension that’s already made. My idea was to use a form to upload the images to AWS/GCP and there have Slicer take them as input with the extension and then output the obj. The extension segments the file to create a 3D render.</p>
<p>I’ve never worked with docker, but I can check it out as well as PythonSlicer.</p>

---

## Post #4 by @lassoan (2020-05-26 19:41 UTC)

<p>If you don’t want to learn Javascript to create a frontend, then it is also an option to create a web application using Slicer Jupyter notebook and <a href="https://voila.readthedocs.io/en/stable/using.html">Voila</a>.</p>
<p>You can use standard IPython widgets for file upload/download/display. Voila takes care of selectively locking down the notebook, so users can still interact with widgets but they will not see or able to modify code in the notebook.</p>
<p>See a number of example web applications here:</p>
<p><a href="https://voila-gallery.org/" class="onebox" target="_blank">https://voila-gallery.org/</a></p>
<p>They are all hosted on the free binder service and a new container is created for each user from scratch, so initial loading of the page may take a minute, but of if you set up your own server then page loading should be instantaneous.</p>

---

## Post #5 by @Davide_Cester (2020-05-29 19:54 UTC)

<aside class="quote no-group" data-username="lennymartinez" data-post="1" data-topic="11720">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lennymartinez/48/6918_2.png" class="avatar"> lennymartinez:</div>
<blockquote>
<p>I want to essentially go: Slicer, do this task, using this folder, and put the output in this location</p>
</blockquote>
</aside>
<p>From my recent experience on headless Slicer on Ubuntu, I think something like the following on the command line could be one way to go:</p>
<pre><code>xvfb-run -a /slicer_path/Slicer --no-splash --python-script mycode.py
</code></pre>
<p>here “xvfb” is a package you need to install on your Ubuntu instance. Running “xvfb-run program” will start “program” with a dummy graphical interface, otherwise it complains that it can’t connect to X server.</p>
<p>If it works for you, you can put everything you want in mycode.py.</p>

---

## Post #6 by @Jeff_Pennal (2020-10-09 19:39 UTC)

<p>Hi Lenny, this isn’t directly related to your question, but I am working on a similar project (DICOM -&gt; OBJ). Is the extension that you are using something that is custom to your project or an open source extension. If its open source, would you mind sharing a link to it?</p>
<p>Thanks,<br>
Jeff</p>

---

## Post #7 by @kpopuri (2020-10-29 20:50 UTC)

<p>thanks! it works like magic</p>

---

## Post #8 by @fpsiddiqui91 (2021-03-24 09:20 UTC)

<p>Hi, I have been working on developing a web app as suggested by <a class="mention" href="/u/lassoan">@lassoan</a> following this link:</p>
<aside class="quote quote-modified" data-post="1" data-topic="11569">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/run-slicer-in-your-web-browser-as-a-jupyter-notebook-or-as-a-full-application/11569">Run Slicer in your web browser - as a Jupyter notebook or as a full application</a> <a class="badge-category__wrapper " href="/c/announcements/7"><span data-category-id="7" style="--category-badge-color: #ED207B; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="Low-traffic category for 3D Slicer, extension, and community news and announcements."><span class="badge-category__name">Announcements</span></span></a>
  </div>
  <blockquote>
    It has been possible to use Slicer from Jupyter notebooks but the most recent Slicer Preview Release takes this to a whole new level. 
<a href="https://mybinder.org/v2/gh/slicer/SlicerNotebooks/master" rel="noopener nofollow ugc">Click here to try a few example interactive notebooks now</a> - or see a short video demonstrating the new features: 

  <a href="https://www.youtube.com/watch?v=oZ3_cRXX2QM" target="_blank" rel="noopener nofollow ugc">
    [Medical image processing in your web browser using Jupyter notebooks and 3D Slicer]
  </a>


Highlights: 

Improved interactive use

You can now use IPython widgets (sliders, buttons, etc.) to control Slicer or adjust processing and visualization…
  </blockquote>
</aside>

<p>. I successfully created a Slicer Jupyter notebook. However, on integrating with Voila I have some issues.</p>
<p>The application fails to launch, even after several tries.</p>
<p>This happens as soon as I add “docker” and “start” file in my repository.</p>
<p>Am I missing some thing? Can you provide any example repository which works with slicer jupyter notebook and voila.</p>
<p>For your reference, my repository link is:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/FaizanSiddiqui91/Slicer_binder">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/FaizanSiddiqui91/Slicer_binder" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/168efe2d2799cdfec85773b18cf614870eccd855a4417499d9b49499d021a2e4/FaizanSiddiqui91/Slicer_binder" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/FaizanSiddiqui91/Slicer_binder" target="_blank" rel="noopener nofollow ugc">GitHub - FaizanSiddiqui91/Slicer_binder</a></h3>

  <p>Contribute to FaizanSiddiqui91/Slicer_binder development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @lassoan (2021-03-24 15:50 UTC)

<p>Does everything work well (Slicer kernel starts without problems) if you don’t use Voila?</p>

---

## Post #10 by @fpsiddiqui91 (2021-03-24 15:52 UTC)

<p>Thank you for your reply <a class="mention" href="/u/lassoan">@lassoan</a>. Yes, slicer works well. I just need to integrate it with Viola. I think I am missing something in the Docker file.<br>
I have tried slicer in my other repository. It works well. I am following your repository. Just the integration with viola is a bit difficult.</p>

---

## Post #12 by @fpsiddiqui91 (2021-03-24 21:31 UTC)

<p>hi <a class="mention" href="/u/lassoan">@lassoan</a> . This is the example I have been following to generate my own repository and notebook. It works fine. The problem arises only when I try to run the app through Voila.</p>
<aside class="onebox githubfolder">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/slicer/SlicerNotebooks/tree/7e61957c0b9ee180c49b9f2e86eec738b037dd82" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars.githubusercontent.com/u/324362?s=400&amp;amp;v=4" class="thumbnail onebox-full-image" width="60" height="60">

<h3><a href="https://github.com/slicer/SlicerNotebooks/tree/7e61957c0b9ee180c49b9f2e86eec738b037dd82" target="_blank" rel="noopener nofollow ugc">Slicer/SlicerNotebooks</a></h3>

<p><a href="https://github.com/slicer/SlicerNotebooks/tree/7e61957c0b9ee180c49b9f2e86eec738b037dd82" target="_blank" rel="noopener nofollow ugc">7e61957c0b9ee180c49b9f2e86eec738b037dd82</a></p>

  <p><span class="label1">Examples that illustrate how to use 3D Slicer via Jupyter notebooks in Python</span></p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Can you help me with this?<br>
Thanks alot</p>

---

## Post #13 by @lassoan (2021-04-09 01:23 UTC)

<p>For reference, this has been discussed at the weekly developer meeting: <a href="https://discourse.slicer.org/t/2021-04-06-hangout/16953/3" class="inline-onebox">2021.04.06 Hangout - #3 by jcfr</a></p>

---

## Post #14 by @jakehockman (2021-11-07 16:34 UTC)

<p>I had trouble importing DICOM files using xvfb. I kept receiving database not open/filenotfound errors when using the DICOMUtils.TemporaryDICOMDatabase(). I was running ubuntu 21 on GCS. In case anyone else has this issue, manually setting the database solved the issue.</p>
<pre><code class="lang-auto">dicomDataDir = 'path/to/dicoms'
dbDir = 'path/to/database'

db = ctk.ctkDICOMDatabase()
db.openDatabase(dbDir)
slicer.dicomDatabase = db

import DICOMLib
DICOMLib.importDicom(dicomDataDir)
dicomFiles = slicer.util.getFilesInDirectory(dicomDataDir)
loadablesByPlugin, loadEnabled = DICOMLib.getLoadablesFromFileLists([dicomFiles])
loadedNodeIDs = DICOMLib.loadLoadables(loadablesByPlugin)

</code></pre>

---

## Post #15 by @lassoan (2021-11-07 17:13 UTC)

<p>Could you please copy here the command that launches Slicer and the full console output?</p>

---

## Post #16 by @jakehockman (2021-11-07 18:11 UTC)

<p>Yes here they are. I tried the method in the script repository and also a second attempt from here:<a href="https://discourse.slicer.org/t/fastest-way-to-load-dicom/9317/2" class="inline-onebox">Fastest way to load DICOM - #2 by lassoan</a></p>
<p><strong>slicer_load_scans_debug.py</strong></p>
<pre><code class="lang-auto">dicomDataDir = 'path/to/dicoms'

loadedNodeIDs = []

from DICOMLib import DICOMUtils

with DICOMUtils.TemporaryDICOMDatabase() as db:
	DICOMUtils.importDicom(dicomDataDir, db)
	patientUIDs = db.patients()
	for patientUID in patientUIDs:
		loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))
</code></pre>
<p><strong>Command</strong></p>
<pre><code class="lang-auto">xvfb-run -a Slicer-4.11.20210226-linux-amd64/Slicer --no-splash --no-main-window --python-script 'startup/slicer_load_scans_debug.py'
</code></pre>
<p><strong>Output:</strong></p>
<pre><code class="lang-auto">
qSlicerSequencesModulePrivate::addToolBar: no main window is available, toolbar is not added
Switching to temporary DICOM database: /tmp/Slicer-neureal2020/20211107_173523_TempDICOMDatabase
TagCacheDatabase adding table
Patient ID is empty, using studyInstanceUID (#########) as patient ID # repeats x169
"DICOM indexer has successfully inserted 169 files [0.14s]"
"DICOM indexer has successfully processed 169 files [0.18s]"
Patient ID is empty, using studyInstanceUID (#########) as patient ID #repeats x169
"DICOM indexer has updated display fields for 169 files [0.07s]"
Loading with imageIOName: GDCM
vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /tmp/Slicer-user/scan_name_TempDICOMDatabase/path/to/dicoms/FILE12 does not exist.
Algorithm vtkITKArchetypeImageSeriesScalarReader(0x5826580) returned failure for request: vtkInformation (0x58278e0)
  Debug: Off
  Modified Time: 128579
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0
Could not read scalar volume using GDCM approach.  Error is: FileNotFoundError
Loading with imageIOName: DCMTK
vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file Archetype file /tmp/Slicer-user/scan_name_TempDICOMDatabase/path/to/dicoms/FILE12 does not exist.
Algorithm vtkITKArchetypeImageSeriesScalarReader(0x38bdd60) returned failure for request: vtkInformation (0x5a45430)
  Debug: Off
  Modified Time: 128662
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0
Could not read scalar volume using DCMTK approach.  Error is: FileNotFoundError
</code></pre>
<p>This was the second attempt:</p>
<p><strong>slicer_load_scans_debug.py</strong></p>
<pre><code class="lang-auto">import DICOMLib
import re
DICOMLib.importDicom(dicomDataDir)
dicomFiles = slicer.util.getFilesInDirectory(dicomDataDir)
loadablesByPlugin, loadEnabled = DICOMLib.getLoadablesFromFileLists([dicomFiles])
loadedNodeIDs = DICOMLib.loadLoadables(loadablesByPlugin)
for loadedNodeID in loadedNodeIDs:
    node = slicer.mrmlScene.GetNodeByID(loadedNodeID)
    safeFileName = re.sub(r'(?u)[^-\w.]', '', node.GetName().strip().replace(' ', '_'))
    slicer.util.saveNode(node, '{0}/{1}.nrrd'.format(outputDir, safeFileName))
</code></pre>
<p><strong>Output</strong></p>
<pre><code class="lang-auto">qSlicerSequencesModulePrivate::addToolBar: no main window is available, toolbar is not added
Patient ID is empty, using studyInstanceUID (#########) as patient ID # repeats x169
"DICOM indexer has successfully inserted 169 files [0.14s]"
"DICOM indexer has successfully processed 169 files [0.18s]"
Patient ID is empty, using studyInstanceUID (#########) as patient ID #repeats x169
"DICOM indexer has updated display fields for 169 files [0.07s]"
Loading with imageIOName: GDCM
Could not load  "/tmp/Slicer-user/scan_name_TempDICOMDatabase/path/to/dicoms/FILE12" 
DCMTK says:  No such file or directory
File /tmp/Slicer-user/scan_name_TempDICOMDatabase/path/to/dicoms/FILE12 could not be initialized.
No geometry information available for DICOM data, skipping corner calculations
</code></pre>
<p>It goes on to give me errors related to saving the .nrrd. I could not reproduce the database not found error, apologies.</p>

---

## Post #17 by @lassoan (2021-11-07 18:16 UTC)

<p>Please try with the latest Slicer Preview Release.</p>
<p>If it fails exactly the same way then check if there referred <code>/tmp/Slicer-user/scan_name_TempDICOMDatabase/path/to/dicoms/FILE12</code> file exists or not.</p>

---

## Post #18 by @jakehockman (2021-11-07 20:17 UTC)

<p>Thanks for your reply. I retried on the latest Preview Release and I got the same error with an additional line saying “Failed to find patient…”:</p>
<pre><code class="lang-auto">"DICOM indexer has successfully processed 169 files [0.18s]"
Patient ID is empty, using studyInstanceUID (#########) as patient ID #repeats x169
Failed to find patient with PatientsName= and PatientID=
</code></pre>
<p>I made copies of the DICOM files and added PatientID and PatientName metadata. I reran and got the same error without that extra line, so it must be unrelated.</p>
<p>With regards to your second comment, I used the following code and the file does not exist.</p>
<pre><code class="lang-auto">with DICOMUtils.TemporaryDICOMDatabase() as db:
	DICOMUtils.importDicom(dicomDataDir, db)
	os.system('ls {}'.format(db.databaseDirectory))

Output:
ctkDICOM.sql
ctkDICOMTagCache.sql
</code></pre>
<p>Also just to be clear, I ran the same <strong>slicer_load_scans_debug.py</strong> with a GUI on my laptop and it loaded the scans without errors.</p>

---

## Post #19 by @lassoan (2021-11-07 23:08 UTC)

<p>Your first example did not contain the node saving part. The second example used the Slicer DICOM database. So, I created a new script (based on the example in the Slicer script repository + adding your node saving) and it worked well for me:</p>
<pre><code class="lang-python">dicomDataDir = r"c:\tmp\eclipse-8.1.20-phantom-ent-ctonly"
outputDir = r"c:\tmp\output"

from DICOMLib import DICOMUtils
import re

try:
    loadedNodeIDs = []  # this list will contain the list of all loaded node IDs
    from DICOMLib import DICOMUtils
    with DICOMUtils.TemporaryDICOMDatabase() as db:
        DICOMUtils.importDicom(dicomDataDir, db)
        patientUIDs = db.patients()
        for patientUID in patientUIDs:
            loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))

    for loadedNodeID in loadedNodeIDs:
        node = slicer.mrmlScene.GetNodeByID(loadedNodeID)
        safeFileName = re.sub(r'(?u)[^-\w.]', '', node.GetName().strip().replace(' ', '_'))
        print(f"Saving {safeFileName}...")
        slicer.util.saveNode(node, '{0}/{1}.nrrd'.format(outputDir, safeFileName))

finally:
    exit()
</code></pre>
<p>I’ve executed by this command (powershell and tee are used to redirect the output so that I can see it, but should not be needed on linux/macOS):</p>
<pre><code class="lang-auto">powershell ".\Slicer.exe --no-splash --no-main-window --python-script 'c:\Users\andra\AppData\Local\NA-MIC\Slicer 4.13.0-2021-11-03\slicer_load_scans_debug.py' 2&gt;&amp;1 | tee out.txt"
</code></pre>
<p>I saw that you used relative paths - I’m not sure what they should be resolved to, so I used absolute paths everywhere. You may try to do that, too.</p>

---
