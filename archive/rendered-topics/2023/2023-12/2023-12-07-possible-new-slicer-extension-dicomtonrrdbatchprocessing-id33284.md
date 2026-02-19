---
topic_id: 33284
title: "Possible New Slicer Extension Dicomtonrrdbatchprocessing"
date: 2023-12-07
url: https://discourse.slicer.org/t/33284
---

# Possible New Slicer Extension - DICOMToNRRDBatchProcessing

**Topic ID**: 33284
**Date**: 2023-12-07
**URL**: https://discourse.slicer.org/t/possible-new-slicer-extension-dicomtonrrdbatchprocessing/33284

---

## Post #1 by @amyers (2023-12-07 14:33 UTC)

<p>Hi,</p>
<p>I’m looking to contribute a new slicer extension that takes a DICOM directory of patients and outputs NRRD files for each patient’s series into a DICOM conforming folder hierarchy Patient/Study/Series. So, there’d be a single NRRD file in each generated series directories.</p>
<p>I explored saving a NRRD file from the GUI, but I can’t select multiple patients for saving a NRRD file.</p>
<p>Before I put the time in for making this extension, is there anything I may have overlooked where this functionality already exists and this extension is unnecessary?</p>
<p>Thank you,<br>
Alex</p>

---

## Post #2 by @pieper (2023-12-07 14:40 UTC)

<p>It would be useful to have a standard module for this.  I do this kind of operation fairly often and I find that usually I need to write a customize script for each set of DICOM data due to some weird quirk of the data or something unique about the acquisitions, but probably there are standard use cases that could be handled by a custom extension.</p>
<p>Here’s a skeleton sample:<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#batch-processing" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#batch-processing</a></p>
<p>Here’s an example from a customized use case where some required data came from external files.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/pieper/SleepEEGSynthSeg/blob/main/QC-2023/qc-prep-2023-04-26.py">
  <header class="source">

      <a href="https://github.com/pieper/SleepEEGSynthSeg/blob/main/QC-2023/qc-prep-2023-04-26.py" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/SleepEEGSynthSeg/blob/main/QC-2023/qc-prep-2023-04-26.py" target="_blank" rel="noopener">pieper/SleepEEGSynthSeg/blob/main/QC-2023/qc-prep-2023-04-26.py</a></h4>


      <pre><code class="lang-py">"""

exec(open("/homes/3/sdp21/Desktop/alta1/users/QC.2023/qc-prep-2023-04-26.py").read())

/autofs/cluster/pubsw/arch/CentOS8-x86_64/packages/slicer/Slicer-5.2.2-linux-amd64/slicer522 

Slicer with customizecd loader:

export LD_LIBRARY_PATH=/space/alta/1/users/pieper/slicer/openssl:/space/alta/1/users/pieper/slicer/krb5/src/lib
/space/alta/1/users/pieper/download/Slicer-5.2.1-linux-amd64/Slicer --python-script /homes/3/sdp21/Desktop/alta1/users/QC.2023/qc-prep-2023-04-26.py |&amp; tee qc-prep-2023-04-26.log

"""

try:
    import pandas
except ModuleNotFoundError:
    pip_install("pandas")
    import pandas

from DICOMLib import DICOMUtils
</code></pre>



  This file has been truncated. <a href="https://github.com/pieper/SleepEEGSynthSeg/blob/main/QC-2023/qc-prep-2023-04-26.py" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @amyers (2023-12-22 17:09 UTC)

<p>From pull request: <a href="https://github.com/Slicer/Slicer/pull/7502" class="inline-onebox" rel="noopener nofollow ugc">ENH: DICOM To NRRD Module Implementation by alex-myers · Pull Request #7502 · Slicer/Slicer · GitHub</a> <a class="mention" href="/u/lassoan">@lassoan</a> suggested I add this as a SandBox extension; however, I was originally thinking adding this as a Slicer extension.<br>
<a class="mention" href="/u/pieper">@pieper</a> suggested a standard module so I went down that path. If there is a similar custom extension base class similar to ScriptedLoadedModule where it’s not too much work, I’m fine with that.<br>
So should this be a Slicer extension, a PerkLab SandBox slicer extension, or a Slicer module? I’ll be using this in tangent with a production DICOM viewer BTW.</p>

---

## Post #4 by @lassoan (2023-12-22 19:50 UTC)

<p>It can become a Slicer core module, but I think it is too early. It will take some time for the module to become more generally usable and work well for a wide range of data. If it is in Slicer Stable Release then you can update it just once in every few months. If it is in an extension then you can update it every day.</p>
<p>Sandbox is a general-purpose collection of maturing Slicer modules, so I think it is a good place for this module. Adding a new extension and maintaining it has some overhead, so it would make sense if we have at least 1-2 more modules for DICOM batch processing - or if the module becomes very robust and capable, so we don’t want to keep it in “sandbox” anymore but we don’t want to move it to Slicer core (e.g., to keep it easier to make changes).</p>
<p>I would suggest to submit to the Sandbox now and decide on its final place later.</p>

---

## Post #5 by @amyers (2023-12-26 13:42 UTC)

<p>Ok. For the time being, I’ll be putting this task off for 3-6 months then I’ll re-assign it, or complete it. Right now, I have a solution for my current project, and I just have higher priorities at the moment.</p>
<p>Nonetheless, the bulk of the logic is already taken into account, and simply adding a checkbox for scalar volumes only should suffice in the sandbox.</p>
<p>Thank you for your feedback for potential invalid characters, that alone was worth the code review.</p>

---
