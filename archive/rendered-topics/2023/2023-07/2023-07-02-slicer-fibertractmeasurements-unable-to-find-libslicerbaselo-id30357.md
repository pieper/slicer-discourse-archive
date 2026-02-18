# Slicer FiberTractMeasurements unable to find libSlicerBaseLogic

**Topic ID**: 30357
**Date**: 2023-07-02
**URL**: https://discourse.slicer.org/t/slicer-fibertractmeasurements-unable-to-find-libslicerbaselogic/30357

---

## Post #1 by @jhlegarreta (2023-07-02 22:52 UTC)

<p>Hi,<br>
I am trying to run <a href="https://github.com/SlicerDMRI/whitematteranalysis" rel="noopener nofollow ugc">WMA</a> on a given dataset. The process runs fine until the moment where the <code>FiberTractMeasurements</code> module in Slicer is called. The tool writes the following to the std output:</p>
<pre><code class="lang-auto">&lt;wm_apply_ORG_atlas_to_subject&gt; Report diffusion measurements of fiber clusters.
Importing whitematteranalysis package.
&lt;wm_diffusion_measurements&gt;. Starting scalar measurement extraction.

=====input directory======
 {my_data}/FiberClustering/SeparatedClusters/tracts_commissural
=====output directory=====
 {my_data}/FiberClustering/SeparatedClusters
=====3D Slicer====
 /opt/Slicer-5.2.2-linux-amd64/NA-MIC/Extensions-31382/SlicerDMRI/lib/Slicer-5.2/cli-modules/FiberTractMeasurements
==========================
/opt/Slicer-5.2.2-linux-amd64/NA-MIC/Extensions-31382/SlicerDMRI/lib/Slicer-5.2/cli-modules/FiberTractMeasurements:
error while loading shared libraries: libSlicerBaseLogic.so: cannot open shared object file: No such file or directory

&lt;wm_diffusion_measurements&gt;
Measurements done at: {my_data}/FiberClustering/SeparatedClusters/diffusion_measurements_commissural.csv
</code></pre>
<p>No CSV file is effectively written after the <code>libSlicerBaseLogic</code> library not being found. A <code>find</code> shows that the library is there:</p>
<pre><code class="lang-auto">$ find /opt/Slicer-5.2.2-linux-amd64/ -name libSlicerBaseLogic.so
/opt/Slicer-5.2.2-linux-amd64/lib/Slicer-5.2/libSlicerBaseLogic.so
</code></pre>
<p>I had a look at the <a href="https://slicer.cdash.org/index.php?project=SlicerStable" rel="noopener nofollow ugc">CDash dashboard</a>, including the <a href="https://slicer.cdash.org/viewTest.php?onlyfailed&amp;buildid=3077318" rel="noopener nofollow ugc">Linux SlicerDMRI build</a> but did not find any relevant information.</p>
<p>How can I investigate/debug further/fix this issue?</p>
<p>I have tried computing the measures from the GUI but no file is being written.</p>
<p>Thanks.</p>

---

## Post #2 by @pieper (2023-07-03 14:44 UTC)

<p>I’m guessing that this script was developed on Mac, where the shared library paths are baked into the executable.  On linux you need to use Slicer’s launch environment.  Easiest would be to run</p>
<p><code>Slicer --launch bash</code></p>
<p>to create a shell with the right environment and run the whitematteranalysis scripts in that shell.</p>

---

## Post #3 by @jhlegarreta (2023-07-03 17:27 UTC)

<p>Thanks for the answer Steve.</p>
<p>The script I am using calls to <code>wm_apply_ORG_atlas_to_subject.sh</code>, but it is not being found within Slicer’s launch environment:</p>
<pre><code class="lang-auto">wm_apply_ORG_atlas_to_subject.sh: not found
</code></pre>
<p>If I give it its absolute path, then the immediately next WMA script called by the former (<code>wm_register_to_atlas_new.py</code>) is not found. Adding the absolute path where the WMA scripts are installed to the <code>PATH</code> env variable does not help either.</p>
<p>Slicer comes with a Python 3.9 version; my default is Python 3.10, and have installed WMA following the website’s instructions. A <code>pip show whitematteranalysis</code> within the launch environment results in a</p>
<pre><code class="lang-auto">ModuleNotFoundError: No module named 'importlib.readers'
</code></pre>
<p>Do I need to install it within Slicer’s launch environment?</p>

---

## Post #4 by @pieper (2023-07-03 17:35 UTC)

<p>I haven’t used whitematteranalysis much, but yes, when I did it I used Slicer’s python environment.</p>
<p>Maybe <a class="mention" href="/u/zhangfanmark">@zhangfanmark</a> or <a class="mention" href="/u/ljod">@ljod</a> can suggest where to look for instructions?</p>

---

## Post #5 by @jhlegarreta (2023-07-03 18:44 UTC)

<p>BTW, I now realize that another discourse thread reported the same error in another discourse threadh, and that I even confirmed that I was having the issue:</p><aside class="quote quote-modified" data-post="1" data-topic="28439">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/41988e/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/no-csv-file-in-diffusionmessurements-folder-in-wma/28439">No CSV file in DiffusionMessurements folder in WMA</a> <a class="badge-category__wrapper " href="/c/community/slicerdmri/16"><span data-category-id="16" data-parent-category-id="12" data-drop-close="true" class="badge-category --has-parent" title="The SlicerDMRI extension provides diffusion MRI tools including tensor estimation, tractography, and quantification."><span class="badge-category__name">SlicerDMRI</span></span></a>
  </div>
  <blockquote>
    Hi there, I am doing whitematteranalysis along with WMA tutorial: <a href="https://github.com/SlicerDMRI/whitematteranalysis/blob/master/doc/subject-specific-tractography-parcellation.md" class="inline-onebox" rel="noopener nofollow ugc">whitematteranalysis/subject-specific-tractography-parcellation.md at master · SlicerDMRI/whitematteranalysis · GitHub</a>. In the last step of tutorial, " 8. Fiber tract diffusion measurements", I could not get any CSV file in the created new DiffusionMeasurements folder with error message of below: 

brain@l4n:~/Desktop/WMA_tutorial_data$ wm_diffusion_measurements.py ./FiberClustering/SeparatedClusters/tracts_commissural/ ./Diffusion…
  </blockquote>
</aside>

<p>Sorry for the cross-posting <img src="https://emoji.discourse-cdn.com/twitter/upside_down_face.png?v=12" title=":upside_down_face:" class="emoji" alt=":upside_down_face:" loading="lazy" width="20" height="20">.</p>
<p>This has also been reported to the WMA repository as an ongoing issue:</p><aside class="onebox githubissue" data-onebox-src="https://github.com/SlicerDMRI/whitematteranalysis/issues/122#issuecomment-1481034903">
  <header class="source">

      <a href="https://github.com/SlicerDMRI/whitematteranalysis/issues/122#issuecomment-1481034903" target="_blank" rel="noopener nofollow ugc">github.com/SlicerDMRI/whitematteranalysis</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SlicerDMRI/whitematteranalysis/issues/122#issuecomment-1481034903" target="_blank" rel="noopener nofollow ugc">Error: python setup.py bdist_wheel</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-03-08" data-time="04:46:37" data-timezone="UTC">04:46AM - 08 Mar 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/fumiado" target="_blank" rel="noopener nofollow ugc">
          <img alt="fumiado" src="https://avatars.githubusercontent.com/u/124753201?v=4" class="onebox-avatar-inline" width="20" height="20">
          fumiado
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Hi, while I am trying to install whitematteranalysis with 'pip install git+https<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">://github.com/SlicerDMRI/whitematteranalysis.git', there was an error message below:
[Anaconda Prompt (miniconda3).txt](https://github.com/SlicerDMRI/whitematteranalysis/files/10917234/Anaconda.Prompt.miniconda3.txt)
 Would anyone tell me how to solve this error?
I am using Windoows, Python 3.10, Miniconda 3.

Thank you,</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @jhlegarreta (2023-07-03 19:03 UTC)

<p>Another element in the WMA folder that may play a role in all this is this one:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerDMRI/whitematteranalysis/blob/master/slicer/installWMA.sh">
  <header class="source">

      <a href="https://github.com/SlicerDMRI/whitematteranalysis/blob/master/slicer/installWMA.sh" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerDMRI/whitematteranalysis/blob/master/slicer/installWMA.sh" target="_blank" rel="noopener nofollow ugc">SlicerDMRI/whitematteranalysis/blob/master/slicer/installWMA.sh</a></h4>


      <pre><code class="lang-sh">#!/bin/sh

INSTALLFOLDER=/Applications/WhiteMatterAnalysis
WMAFOLDER=$(pwd)/..
PYTHONVERSION=3.6.0

mkdir -p $INSTALLFOLDER
cd $INSTALLFOLDER

git clone https://github.com/pyenv/pyenv
PREFIX=$INSTALLFOLDER/python-build pyenv/plugins/python-build/install.sh

$INSTALLFOLDER/python-build/bin/python-build $PYTHONVERSION $INSTALLFOLDER/python
$INSTALLFOLDER/python/bin/pip install $WMAFOLDER 


</code></pre>




  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Not sure this is necessary, even on macOS (the <code>INSTALLFOLDER</code> is certainly a hard-coded macOS path); even if the parent folder says <code>slicer</code>, there are no paths related to Slicer in this script.</p>

---

## Post #7 by @ljod (2023-07-03 19:19 UTC)

<p>Hi I hope Fan can chime in because he wrote this part and uses it frequently <a class="mention" href="/u/zhangfanmark">@zhangfanmark</a></p>

---

## Post #8 by @jhlegarreta (2023-07-05 12:46 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> Where can we start investigating this? I am very much willing to help fixing this. Thanks.</p>

---

## Post #9 by @pieper (2023-07-05 17:12 UTC)

<p>At one point I worked on applying the WMA pipeline to sets of data and ran the whole process out of Slicer’s python environment, including the part where it launched the FiberTractMeasurements.  This code includes some odd workarounds (like calling eddy current correction on a remote machine) but it did basically work so you might be able to start from here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/pieper/SlicerDMRI/blob/batchtract/Modules/Scripted/BatchTract/BatchTract.py">
  <header class="source">

      <a href="https://github.com/pieper/SlicerDMRI/blob/batchtract/Modules/Scripted/BatchTract/BatchTract.py" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/SlicerDMRI/blob/batchtract/Modules/Scripted/BatchTract/BatchTract.py" target="_blank" rel="noopener">pieper/SlicerDMRI/blob/batchtract/Modules/Scripted/BatchTract/BatchTract.py</a></h4>


      <pre><code class="lang-py">import glob
import json
import os
import shutil
import subprocess
import unittest
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *

#
# BatchTract
#

class BatchTract(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
</code></pre>



  This file has been truncated. <a href="https://github.com/pieper/SlicerDMRI/blob/batchtract/Modules/Scripted/BatchTract/BatchTract.py" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #10 by @jhlegarreta (2023-07-05 22:17 UTC)

<p>Thanks Steve.</p>
<p>Not sure this would work, as even when I try to use the “FiberTractMeasurements” module from within the GUI no CSV/output is being written. Anyways, gave it a try with a reduced version of your script (with the paths adapted to my case):</p><aside class="onebox githubgist" data-onebox-src="https://gist.github.com/jhlegarreta/d90ff3b70b3d85271a4afc953d76be14">
  <header class="source">

      <a href="https://gist.github.com/jhlegarreta/d90ff3b70b3d85271a4afc953d76be14" target="_blank" rel="noopener nofollow ugc">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/jhlegarreta/d90ff3b70b3d85271a4afc953d76be14" target="_blank" rel="noopener nofollow ugc">https://gist.github.com/jhlegarreta/d90ff3b70b3d85271a4afc953d76be14</a></h4>

  <h5>fibertractmeasurements_slicerpy_anon.py</h5>
  <pre><code class="Python"># -*- coding: utf-8 -*-

import subprocess

#import slicer
#from slicer.ScriptedLoadableModule import *


def run_command(command, out_path):
</code></pre>
    This file has been truncated. <a href="https://gist.github.com/jhlegarreta/d90ff3b70b3d85271a4afc953d76be14" target="_blank" rel="noopener nofollow ugc">show original</a>

<p>
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Launched from a terminal like</p>
<pre><code class="lang-auto">$ ./Slicer --no-main-window --python–script ~/path/to/fibertractmeasurements_slicerpy.py
</code></pre>
<p>It fails with</p>
<pre><code class="lang-auto">qSlicerMarkupsModulePrivate::addToolBar: no main window is available, toolbar is not added
qSlicerSequencesModulePrivate::addToolBar: no main window is available, toolbar is not added
Ignore argument received via command-line (not a valid URL or existing local file):  "--pythonâ\u0080\u0093script"Local filepath received via command-line:  "/home/path/to/fibertractmeasurements_slicerpy.py"
virtual bool qSlicerFreeSurferImporterScalarOverlayReader::load(const IOProperties&amp;)  failed: missing fileName or modelNodeId property
static void qSlicerIOManager::showLoadNodesResultDialog(bool, vtkMRMLMessageCollection*) Errors occurred while loading nodes: "Error: Loading /home/path/to/fibertractmeasurements_slicerpy.py -  load failed.\n"
</code></pre>
<p>The script does exist in the provided path.</p>
<p>If I try a simple</p>
<pre><code class="lang-auto">$ ./Slicer --no-main-window --python-code "print("Hello")"
</code></pre>
<p>I get an error</p>
<pre><code class="lang-auto">qSlicerMarkupsModulePrivate::addToolBar: no main window is available, toolbar is not added
qSlicerSequencesModulePrivate::addToolBar: no main window is available, toolbar is not added
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
NameError: name 'Hello' is not defined
</code></pre>
<p>So what am I missing?</p>

---

## Post #11 by @zhangfanmark (2023-07-06 05:17 UTC)

<p>Hi Jon,</p>
<p>Please take a look at my reply in the other post, which should fix the issue you have here:</p>
<aside class="quote quote-modified" data-post="6" data-topic="28439">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zhangfanmark/48/4451_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/no-csv-file-in-diffusionmessurements-folder-in-wma/28439/6">No CSV file in DiffusionMessurements folder in WMA</a> <a class="badge-category__wrapper " href="/c/community/slicerdmri/16"><span data-category-id="16" data-parent-category-id="12" data-drop-close="true" class="badge-category --has-parent" title="The SlicerDMRI extension provides diffusion MRI tools including tensor estimation, tractography, and quantification."><span class="badge-category__name">SlicerDMRI</span></span></a>
  </div>
  <blockquote>
    Hi <a class="mention" href="/u/fumi">@Fumi</a> <a class="mention" href="/u/jhlegarreta">@jhlegarreta</a> 
I looked in the the issue that you were facing. 
On MacOS (mine is Ventura 13.2.1), it is working properly for me as it is. Please see the below screenshot for my setting to run the wm_diffusion_measurements script using Slicer 5.2.2 stable release: 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45d477da36fe3176a0cdca20725cf2a02f4e2a61.jpeg" data-download-href="/uploads/short-url/9XK9Hi1qKqNTNS1tnbtUIP1UrsZ.jpeg?dl=1" title="image" rel="noopener nofollow ugc">[image]</a> 
On Ubuntu (mine is 20.04.4 LTS), I also saw the issue about missing lib files when using  Slicer 5.2.2 when directly call the FiberTractMeasurements module in the CLI mode. In this case, we would need to use Slicer L…
  </blockquote>
</aside>

<p>Regards,<br>
Fan</p>

---

## Post #12 by @jhlegarreta (2023-07-06 14:35 UTC)

<p>So the solution in the <a href="https://discourse.slicer.org/t/no-csv-file-in-diffusionmessurements-folder-in-wma/28439/6">other post</a> <a href="https://discourse.slicer.org/t/no-csv-file-in-diffusionmessurements-folder-in-wma/28439/7">worked for me</a>. Thanks <a class="mention" href="/u/zhangfanmark">@zhangfanmark</a>.</p>

---
