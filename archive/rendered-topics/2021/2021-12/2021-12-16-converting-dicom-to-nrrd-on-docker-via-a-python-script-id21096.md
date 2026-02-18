# Converting DICOM to NRRD on Docker via a Python script

**Topic ID**: 21096
**Date**: 2021-12-16
**URL**: https://discourse.slicer.org/t/converting-dicom-to-nrrd-on-docker-via-a-python-script/21096

---

## Post #1 by @adouv (2021-12-16 15:37 UTC)

<p>Hello, I would like to start off thanking all of you for the great work with 3D Slicer. It is truly a phenomenal piece of software! The issue we are having requires some description, so I will split this question into two main sections.</p>
<h2><a name="p-71307-h-1-setup-1" class="anchor" href="#p-71307-h-1-setup-1" aria-label="Heading link"></a>1) Setup</h2>
<p>I am working on a containerized application to perform some processing of DICOM images, and part of the pipeline involves first converting the DICOM files into an .nrrd file. Performing the conversion must be done via the 3D Slicer interface for a very particular reason (this a hard requirement for us for the time being). Therefore in order to be able to do it, we wrote a short python script to perform this conversion. The script is as follows (I have omitted part of the code related to parsing the CL arguments):</p>
<pre><code class="lang-auto">import sys
import argparse
import slicer

import DICOMLib.DICOMUtils as utils
import DICOMScalarVolumePlugin


def main():
    input_arg = sys.argv[1]
    output_arg = sys.argv[2]

    with utils.TemporaryDICOMDatabase() as db:
        utils.importDicom(input_arg, db)
        patient = db.patients()[0]
        study = db.studiesForPatient(patient)[0]
        series = db.seriesForStudy(study)[0]
        files = db.filesForSeries(series)
        reader = DICOMScalarVolumePlugin.DICOMScalarVolumePluginClass()
        loadable = reader.examineForImport([files])[0]
        node = reader.load(loadable)
        slicer.util.saveNode(node, output_arg)


if __name__ == '__main__':
    main()
    sys.exit(0)

</code></pre>
<p>We are able to run this without issues using a Windows 3D Slicer executable via the command line, as described <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#run-a-python-script-file-in-the-slicer-environment" rel="noopener nofollow ugc">here</a>.</p>
<p>Since this needs to be done in Docker, we are using the slicer-notebook image provided by <a class="mention" href="/u/lassoan">@lassoan</a> as a testing environment. This the Dockerfile that we are using for this purpose:</p>
<pre><code class="lang-auto">FROM lassoan/slicer-notebook:2021-10-15-b3077c2
WORKDIR /app

COPY dicom2nrrd.py .
</code></pre>
<h2><a name="p-71307-h-2-the-problem-2" class="anchor" href="#p-71307-h-2-the-problem-2" aria-label="Heading link"></a>2) The Problem</h2>
<p>The problem arises when trying to execute this script, as we have attempted to do it in two different ways, each yielding a different error.</p>
<h3><a name="p-71307-using-the-executable-3" class="anchor" href="#p-71307-using-the-executable-3" aria-label="Heading link"></a>Using the Executable</h3>
<p>This is similar to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#run-a-python-script-file-in-the-slicer-environment" rel="noopener nofollow ugc">this example</a>:</p>
<pre><code class="lang-auto">/home/sliceruser/Slicer/Slicer --no-splash --no-main-window --testing --python-script /app/dicom2nrrd.py --input /app/dicoms/ --output /app/temp_nrrd.nrrd
</code></pre>
<h4><a name="p-71307-the-error-message-4" class="anchor" href="#p-71307-the-error-message-4" aria-label="Heading link"></a>The error message:</h4>
<pre><code class="lang-auto">qt.qpa.xcb: could not connect to display :10
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: xcb.
</code></pre>
<p>We have seen that others had a similar issue before (<a href="https://discourse.slicer.org/t/cant-start-latest-stable-on-ubuntu-20-04/14029/2">1</a>, <a href="https://discourse.slicer.org/t/slicer-not-starting-on-linux-qt-plugin-issue/18856">2</a>) but the proposed solutions (installing the xinerama0 package) unfortunately did not work.</p>
<p>As an alternative, we also tried launching the script directly from 3D Slicer’s Python environment.</p>
<h2><a name="p-71307-using-the-python-environment-5" class="anchor" href="#p-71307-using-the-python-environment-5" aria-label="Heading link"></a>Using the Python environment</h2>
<p>This is the command used:</p>
<pre><code class="lang-auto">/home/sliceruser/Slicer/bin/PythonSlicer  /app/dicom2nrrd.py --input /app/dicoms/ --output /app/temp_nrrd.nrrd
</code></pre>
<h3><a name="p-71307-the-error-message-6" class="anchor" href="#p-71307-the-error-message-6" aria-label="Heading link"></a>The error message:</h3>
<pre data-code-wrap="No"><code class="lang-No">Traceback (most recent call last):
  File "/app/dicom2nrrd.py", line 7, in &lt;module&gt;
    import DICOMLib.DICOMUtils as utils
  File "/home/sliceruser/Slicer/lib/Slicer-4.13/qt-scripted-modules/DICOMLib/__init__.py", line 1, in &lt;module&gt;
    from .DICOMProcesses import *
  File "/home/sliceruser/Slicer/lib/Slicer-4.13/qt-scripted-modules/DICOMLib/DICOMProcesses.py", line 3, in &lt;module&gt;
    import qt
  File "/home/sliceruser/Slicer/bin/Python/qt/__init__.py", line 19, in &lt;module&gt;
    from PythonQt.private import QObject
ModuleNotFoundError: No module named 'PythonQt'
</code></pre>
<p>Scripts which do not result in the program attempting to <strong>import qt</strong> work without any issue, but as soon as we include modules which do depend on qt (in this case the DICOMProcesses module) we end up with this error message.</p>
<p>We have tried many different possible solutions, including building the containers described <a href="https://github.com/Slicer/SlicerDocker" rel="noopener nofollow ugc">here</a> as-is, as well as explicitly installing the dependencies and extracting the Slicer build manually, but we still encounter the same error. For more information, we are using Windows machines running Docker Desktop to perform these tests.</p>
<p>We would greatly appreciate any help on this, or at least some clarification on the origin of these errors, and possible solutions. Thank you very much!</p>

---

## Post #2 by @mau_igna_06 (2021-12-16 15:54 UTC)

<p>Have you tried calling Slicer like <a href="https://github.com/pieper/SlicerDockers/blob/83d04792f6c7032c9a1d8a5d1aa041994d094a86/slicer-plus/Dockerfile#L19">this</a>?</p>

---

## Post #3 by @pieper (2021-12-16 21:06 UTC)

<p>You can run arbitrary Slicer python scripts in virtual X server with this command template:</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/pieper/SlicerDockers/tree/83d04792f6c7032c9a1d8a5d1aa041994d094a86#running-a-slicer-analysis-script-in-an-instance">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/pieper/SlicerDockers/tree/83d04792f6c7032c9a1d8a5d1aa041994d094a86#running-a-slicer-analysis-script-in-an-instance" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/pieper/SlicerDockers/tree/83d04792f6c7032c9a1d8a5d1aa041994d094a86#running-a-slicer-analysis-script-in-an-instance" target="_blank" rel="noopener">GitHub - pieper/SlicerDockers at 83d04792f6c7032c9a1d8a5d1aa041994d094a86 - Running a Slicer analysis script in an instance</a></h3>

  <p><a href="https://github.com/pieper/SlicerDockers/tree/83d04792f6c7032c9a1d8a5d1aa041994d094a86#running-a-slicer-analysis-script-in-an-instance" target="_blank" rel="noopener">83d04792f6c7032c9a1d8a5d1aa041994d094a86</a></p>

  <p><span class="label1">docker config files for slicer. Contribute to pieper/SlicerDockers development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>p.s. for many dicom to nrrd conversion tasks you can also consider dcm2niix, which is much faster if that’s the only feature you need.</p>

---

## Post #4 by @ROSENty (2021-12-17 13:29 UTC)

<p>I met the same error <img src="https://emoji.discourse-cdn.com/twitter/sob.png?v=10" title=":sob:" class="emoji" alt=":sob:"> <img src="https://emoji.discourse-cdn.com/twitter/sob.png?v=10" title=":sob:" class="emoji" alt=":sob:"> <img src="https://emoji.discourse-cdn.com/twitter/sob.png?v=10" title=":sob:" class="emoji" alt=":sob:">But I want to convert RTStruct file to .vtp file, who could help me, thanks a lot</p>

---

## Post #5 by @pieper (2021-12-17 13:31 UTC)

<p>There’s a batch struct conversion script in SlicerRT that could be run in docker using a similar formula.  Be aware that RTStruct can be a tricky format due to variable vendor compliance issues, but SlicerRT is generally good at handling most cases.</p>

---

## Post #6 by @ROSENty (2021-12-17 14:18 UTC)

<p>At first, thanks for your reply <img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=10" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:"></p>

---

## Post #7 by @ROSENty (2021-12-17 14:26 UTC)

<p>I think this problem has nothing to do with “RT to .vtp” or “dicom to nrrd”, the problem is we cannot use slicer python script on docker. <img src="https://emoji.discourse-cdn.com/twitter/sob.png?v=10" title=":sob:" class="emoji" alt=":sob:"></p>

---

## Post #8 by @adouv (2022-06-03 12:18 UTC)

<p>Hi there, apologies for the very late reply, but this suggestion put us on the right track towards solving this issue. Many thanks!</p>

---
