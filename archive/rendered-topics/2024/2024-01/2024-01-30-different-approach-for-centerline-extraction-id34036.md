---
topic_id: 34036
title: "Different Approach For Centerline Extraction"
date: 2024-01-30
url: https://discourse.slicer.org/t/34036
---

# Different approach for centerline extraction

**Topic ID**: 34036
**Date**: 2024-01-30
**URL**: https://discourse.slicer.org/t/different-approach-for-centerline-extraction/34036

---

## Post #1 by @nmg-earthling (2024-01-30 02:57 UTC)

<p>Hello Slicer Community,<br>
I have some scripts written for a client about 9 or 10 years ago for automated centerline extraction (and calculating metrics for those centerlines) that I developed with VMTK.  The client recently decided they wanted to start using this functionality again (I don’t think they have used it for three or four years.  The code is run inside a docker container in an old version of ubuntu which no longer builds (which is different than <a href="https://discourse.slicer.org/t/vmtk-extract-centerline-with-python-console/31596" class="inline-onebox">VMTK Extract Centerline with python console</a> where doing the extraction inside Slicer is ok).<br>
My first approach was to try and get conda or pip installs of vtk and VMTK to work together but it seems like the packages have not been kept up to date.  I saw in a thread (which I don’t have handy at the moment) that Andras suggested that the Slicer team’s focus has been on the Slicer project and not supporting side projects like VMTK.  Fair enough, so it seems like I am at a crossroads between centerline extraction automation like in this thread <a href="https://discourse.slicer.org/t/vmtk-extract-centerline-with-python-console/31596/7" class="inline-onebox">VMTK Extract Centerline with python console - #7 by mikebind</a> and having a contained Slicer environment like this thread <a href="https://discourse.slicer.org/t/running-slicer-without-gui/11720/16" class="inline-onebox">Running Slicer without GUI? - #16 by jakehockman</a>.  I have taken the slicer notebook docker container as a template <a href="https://github.com/Slicer/SlicerDocker/tree/main/slicer-notebook" class="inline-onebox" rel="noopener nofollow ugc">SlicerDocker/slicer-notebook at main · Slicer/SlicerDocker · GitHub</a> updated it a little bit to a newer bullseye image and removed the Juypter notebook pieces.  It seems like I have an image with slicer installed with my python scripts (updated to python 3 since the original was in 2.7). I’ve seen instructions to run scripts in Slicer something like this:<br>
xvfb-run -a /opt/slicer/Slicer/Slicer --no-main-window --python-script /opt/app/Python/app.py</p>
<p>Can I run python scripts directly with the Slicer python interpreter though and get around xvfb and Slicer?  Something like this:<br>
/opt/slicer/Slicer/ /opt/app/Python/app.py</p>
<p>I’m hoping that I’m very close, since I have scripts that worked in vmtk several years ago.</p>
<p>Thank you in advance!</p>

---

## Post #2 by @wesselk (2024-01-30 17:13 UTC)

<p>From my understanding of the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html" rel="noopener nofollow ugc">documentation</a> and <a href="https://discourse.slicer.org/t/slicer-no-main-window-python-script-in-windows-command-prompt-not-working/6481/25">this comment</a> from the man himself, yes unless you need the slicer modules.  SlicerPython is like a prepackaged virtual environment, it includes vmtk and can be run from cmd but you’ll need to have the user interface open for access to slicer.app, slicer.mrmlScene, slicer.modules, slicer.moduleNames.  You can also use other flags to help your automation routine like --no-main-window and --exit-after-startup.</p>

---

## Post #3 by @nmg-earthling (2024-01-30 20:45 UTC)

<p>Thank you Kyle,<br>
I missed that page in the documentation though, it’s mostly geared towards using scripts inside of Slicer but between that and Andras’ comment it seems like I figured out how to get my dependencies added but still I get this error:</p>
<pre><code class="lang-auto">    from vmtk import vtkvmtk
ModuleNotFoundError: No module named 'vmtk'
</code></pre>
<p>It was my understanding that slicer came packaged with vmtk, do I need to load vmtk seperately somehow?</p>

---

## Post #4 by @wesselk (2024-02-01 17:15 UTC)

<p>I ran into that same problem and made <a href="https://discourse.slicer.org/t/installing-slicer-extensions-from-cmd-with-python/32017">another post</a> which got great answers, hopefully it helps.</p>

---

## Post #5 by @nmg-earthling (2024-02-02 19:53 UTC)

<p>Thank you Kyle,<br>
Looks like I’m missing the SlicerVMTK extension.  Kyle, did you install it via the install.sh script in the docker examples or somehow directly?</p>

---

## Post #6 by @wesselk (2024-02-05 16:33 UTC)

<p>I downloaded the compressed files for each extension I needed from the slicer extension catalogue and then ran the following in the slicer console:</p>
<pre><code class="lang-auto">slicer.app.extensionsManagerModel().installExtension('/path/to/myextension.zip')
</code></pre>

---

## Post #7 by @nmg-earthling (2024-02-07 21:24 UTC)

<p>It looks like I was able to get the SlicerVTMK extension to install (after adding many apt-get calls to the docker container.  So I have something like this in install.h</p>
<pre><code class="lang-auto">...
echo "Install SlicerVMTK extension"
$slicer_executable -c '
em = slicer.app.extensionsManagerModel()
extensionName = "SlicerVMTK"
if int(slicer.app.revision) &gt;= 30893:
    # Slicer-5.0.3 or later
    em.updateExtensionsMetadataFromServer(True, True)
    if not em.downloadAndInstallExtensionByName(extensionName, True):
         raise ValueError(f"Failed to install {extensionName} extension")
    # Wait for installation to complete
    # (in Slicer-5.4 downloadAndInstallExtensionByName has a waitForComplete flag
    # so that could be enabled instead of running this wait loop)
    import time
    while not em.isExtensionInstalled(extensionName):
        slicer.app.processEvents()
        time.sleep(0.1)
...
</code></pre>
<p>However when I try to run my script I still get an error that vmtk isn’t available:</p>
<pre><code class="lang-auto">  File "/opt/app/Python/CenterLines.py", line 7, in &lt;module&gt;
    from  vmtkCustomSeedSelector2 import vmtkBranchSeedSelector
  File "/opt/app/Python/vmtkCustomSeedSelector2.py", line 9, in &lt;module&gt;
    from vmtk import vtkvmtk
ModuleNotFoundError: No module named 'vmtk'
</code></pre>
<p>So I did some searching and it seems like SlicerVMTK has some different ways of referencing vmtk.  So in the SlicerVMTK extension the there is an ExtractCenterline.py fiie</p><aside class="onebox githubblob" data-onebox-src="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/ExtractCenterline/ExtractCenterline.py">
  <header class="source">

      <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/ExtractCenterline/ExtractCenterline.py" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/ExtractCenterline/ExtractCenterline.py" target="_blank" rel="noopener nofollow ugc">vmtk/SlicerExtension-VMTK/blob/master/ExtractCenterline/ExtractCenterline.py</a></h4>


      <pre><code class="lang-py">import os
import unittest
import logging
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
from slicer.util import VTKObservationMixin

#
# ExtractCenterline
#

class ExtractCenterline(ScriptedLoadableModule):
    """Uses ScriptedLoadableModule base class, available at:
    https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
    """

    def __init__(self, parent):
        ScriptedLoadableModule.__init__(self, parent)
        self.parent.title = "Extract Centerline"
        self.parent.categories = ["Vascular Modeling Toolkit"]
</code></pre>



  This file has been truncated. <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/ExtractCenterline/ExtractCenterline.py" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<pre><code class="lang-auto">...
    def extractCenterline(self, surfacePolyData, endPointsMarkupsNode, curveSamplingDistance=1.0):
        """Compute centerline.
        This is more robust and accurate but takes longer than the network extraction.
        :param surfacePolyData:
        :param endPointsMarkupsNode:
        :return:
        """

        import vtkvmtkComputationalGeometryPython as vtkvmtkComputationalGeometry
...
</code></pre>
<p>But when I try to import it in my scripts I get an error:</p>
<pre><code class="lang-auto">import vtkvmtkComputationalGeometryPython as vtkvmtkComputationalGeometry
  ModuleNotFoundError: No module named 'vtkvmtkComputationalGeometryPython'
</code></pre>
<p>Does anyone have any advice on what I’m doing wrong here?</p>

---
