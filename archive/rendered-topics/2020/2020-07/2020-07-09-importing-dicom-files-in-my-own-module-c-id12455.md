---
topic_id: 12455
title: "Importing Dicom Files In My Own Module C"
date: 2020-07-09
url: https://discourse.slicer.org/t/12455
---

# Importing DICOM files in my own module C++

**Topic ID**: 12455
**Date**: 2020-07-09
**URL**: https://discourse.slicer.org/t/importing-dicom-files-in-my-own-module-c/12455

---

## Post #1 by @DavidCai1246 (2020-07-09 03:47 UTC)

<p>I would like to import DICOM files in my own module by calling the import function in the “DICOM” module without actually switching to the “DICOM” module. Is this possible to do?</p>
<p>I was thinking of calling the import functions in the “DICOM” module in the backend, but the DICOM module is written in python and my module is in C++.</p>
<p>The python code is something like this:</p>
<blockquote>
<p>plugin = slicer.modules.dicomPlugins<a>’DICOMScalarVolumePlugin’</a><br>
loadables = plugin.examineFiles(dicom_fileList)<br>
if len(loadables) &gt; 1:<br>
print(“Multiple DICOM scans detected! Not proceeding”)<br>
sys.exit(1)<br>
volume = plugin.load(loadables[0])</p>
</blockquote>

---

## Post #2 by @lassoan (2020-07-09 13:43 UTC)

<p>The DICOM browser and indexer are written in C++, so you can access them directly from C++. DICOM <em>loader</em> plugins are mostly implemented in Python, so you need to call Python from C++.</p>
<p>You can either use CPython or PythonQt API. For example, to run a Python command and get value of a variable using PythonQt API:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Base/QTGUI/qSlicerSettingsGeneralPanel.cxx#L99-L102" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Base/QTGUI/qSlicerSettingsGeneralPanel.cxx#L99-L102" target="_blank">Slicer/Slicer/blob/master/Base/QTGUI/qSlicerSettingsGeneralPanel.cxx#L99-L102</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="99" style="counter-reset: li-counter 98 ;">
<li>PythonQt::init();</li>
<li>PythonQtObjectPtr context = PythonQt::self()-&gt;getMainModule();</li>
<li>context.evalScript(QString("slicerrcfilename = getSlicerRCFileName()\n"));</li>
<li>QVariant slicerrcFileNameVar = context.getVariable("slicerrcfilename");</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @DavidCai1246 (2020-07-09 20:21 UTC)

<p>Thank you very much!</p>

---

## Post #4 by @DavidCai1246 (2020-07-10 18:52 UTC)

<p>I’m currently trying to use PythonQt in my project. One issue I found is that I cannot pass arguments into my python script. my python script that I want to run is:</p>
<pre><code>def dicom2file(path_to_dicom_dir,output_path):
    
## Grab indivial DICOM slices into a filelist
excluded_extensions = ['.txt', '.csv', '.xml', '.tag', '.nii']
dicom_fileList = [os.path.join(path_to_dicom_dir,file) for file in os.listdir(path_to_dicom_dir)
                    if not file.endswith( tuple(excluded_extensions) ) ]
# Loading DICOM using the ScalarVolumePlugin
plugin = slicer.modules.dicomPlugins['DICOMScalarVolumePlugin']()
loadables = plugin.examineFiles(dicom_fileList)
if len(loadables) &gt; 1:
    print("Multiple DICOM scans detected! Not proceeding")
    sys.exit(1)
volume = plugin.load(loadables[0])

## Save the DICOM volume in scalar volume format
slicer.util.saveNode(volume, output_path)

## To-do: exits should be move to high-level wrapper
#exit()
</code></pre>
<p>I need to pass in 2 arguments <code>path_to_dicom_dir</code> and <code>output_path</code><br>
Is there a way for me to pass arguments into my python script in C++ with pythonQT or should I use something else?</p>

---

## Post #5 by @lassoan (2020-07-10 20:18 UTC)

<p>You can set simple input values by writing their values in the executed string. For setting more complicated input objects or getting output objects, you can add/get variables in the context. See lots of examples in <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/Widgets/qSlicerDICOMExportDialog.cxx">qSlicerDICOMExportDialog.cxx</a>.</p>

---

## Post #6 by @DavidCai1246 (2020-07-10 21:05 UTC)

<p>I will look into it, thank you so much!</p>

---
