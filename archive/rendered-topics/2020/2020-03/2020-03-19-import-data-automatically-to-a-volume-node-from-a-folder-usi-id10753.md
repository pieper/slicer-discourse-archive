# Import data automatically to a volume node from a folder using command line

**Topic ID**: 10753
**Date**: 2020-03-19
**URL**: https://discourse.slicer.org/t/import-data-automatically-to-a-volume-node-from-a-folder-using-command-line/10753

---

## Post #1 by @Tokai (2020-03-19 20:41 UTC)

<p>Operating system: win10<br>
Slicer version: 4.10.2<br>
Expected behavior:<br>
Actual behavior:<br>
Hi,<br>
I have two folders containing .IMA files. I want to load  them automatically into slicer using the folder paths and then perform registration between them.<br>
So, I need to do first<br>
# Load Volume<br>
[ success,movingVolumeNode ] = slicer.util.loadVolume(Movinfilename,returnNode=True)<br>
[ success, fixedVolumeNode] = slicer.util.loadVolume(Fixedfilename,returnNode=True)<br>
And then<br>
logic = SomeRegistrationLogic()<br>
…<br>
logic.registerVolumes(fixedVolumeNode, movingVolumeNode, outputVolumeNode)</p>
<p>But slicer.util.loadVolume takes a file not a directory. So my question is how can I import each of these directories using a python script and get them as volume node ?</p>

---

## Post #2 by @pieper (2020-03-19 21:04 UTC)

<p>Hi -</p>
<p>By .IMA files I guess you mean dicom?  You can try some of the methods in <a href="https://github.com/Slicer/Slicer/commits/master/Modules/Scripted/DICOMLib/DICOMUtils.py">DICOMUtils</a>.  Also here’s a script that takes a directory of dicoms on the command line and makes volumes out of them.  I haven’t tried this in a while and it may need some tweaking for the current Slicer.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/QIICR/dcmheat/blob/master/docker/SlicerConvert.py" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/QIICR/dcmheat/blob/master/docker/SlicerConvert.py" target="_blank">QIICR/dcmheat/blob/master/docker/SlicerConvert.py</a></h4>
<pre><code class="lang-py">import os
import sys

def setDICOMReaderApproach(approach):
    import DICOMScalarVolumePlugin
    approaches = DICOMScalarVolumePlugin.DICOMScalarVolumePluginClass.readerApproaches()
    if approach not in approaches:
        raise ValueError("Unknown dicom approach: %s\nValid options are: %s" % (approach, approaches))
    approachIndex = approaches.index(approach)
    settings = qt.QSettings()
    settings.setValue('DICOM/ScalarVolume/ReaderApproach', approachIndex)


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--dcmtk", help="use dcmtk to parse dicom (exclusive with --gdcm)", action="store_true")
parser.add_argument("--gdcm", help="use dcmtk to parse dicom (exclusive with --dcmtk)", action="store_true")
parser.add_argument("--no-quit", help="For debugging, don't exit Slicer after converting", action="store_true")
parser.add_argument("--input", help="Input DICOM directory")
parser.add_argument("--output", help="Output directory")
</code></pre>

  This file has been truncated. <a href="https://github.com/QIICR/dcmheat/blob/master/docker/SlicerConvert.py" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @Tokai (2020-03-19 21:53 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a><br>
The “db” error is fixed.<br>
It would be db =slicer.app.dicomDatabase().<br>
However it runs successfully and execute<br>
<code>"No scalar volumes parsed from the input DICOM dataset! Aborting."</code><br>
Meaning no nodes!! Do you have any idea?<br>
However it shows that it is imported in the slicer. But needs to be loaded in the GUI.</p>

---

## Post #5 by @Tokai (2020-03-19 22:46 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a><br>
I got another example from <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/DICOMUtils.py" rel="nofollow noopener">here</a>.<br>
dicomDataDir = “c:/my/folder/with/dicom-files”  # input folder with DICOM files<br>
loadedNodeIDs = []  # this list will contain the list of all loaded node IDs<br>
from DICOMLib import DICOMUtils<br>
with DICOMUtils.TemporaryDICOMDatabase() as db:<br>
DICOMUtils.importDicom(dicomDataDir, db)<br>
patientUIDs = db.patients()<br>
for patientUID in patientUIDs:<br>
loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))<br>
But before I can check for volume node, it throws error:<br>
loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))<br>
TypeError: ‘bool’ object is not iterable</p>

---

## Post #6 by @lassoan (2020-03-19 23:12 UTC)

<p>We recently reworked the DICOM browser. You need to use latest Slicer Preview Release for this last example (few days old release should be still OK, several weeks old may work differently).</p>

---

## Post #7 by @Tokai (2020-03-19 23:20 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,<br>
Do you have any suggestion to fix this code (slicer 4.10.2) or another working example to load dicoms from folder and access as volume node using python scripting ?</p>

---

## Post #8 by @lassoan (2020-03-19 23:55 UTC)

<p>Slicer-4.10 will soon be retired and Slicer-4.11 will be promoted to be the new stable release, so I would recommend to use most recent Slicer-4.11 version.</p>

---

## Post #9 by @Tokai (2020-03-20 09:29 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a><br>
So I found a simpler way. Simple providing the a single file of the folder in below method do the task. It loads all the files automatically.<br>
slicer.util.loadVolume(‘single_file_of_folder’) .</p>
<p>Can you please tell me  How can I set  this loaded volume node as the fixed or moved volume from command line to perform landmark registration? I do not want use the gui.<br>
Thanks</p>

---

## Post #10 by @pieper (2020-03-24 19:56 UTC)

<aside class="quote no-group" data-username="Tokai" data-post="9" data-topic="10753">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tokai/48/4851_2.png" class="avatar"> Tokai:</div>
<blockquote>
<p>Can you please tell me How can I set this loaded volume node as the fixed or moved volume from command line to perform landmark registration? I do not want use the gui.</p>
</blockquote>
</aside>
<p>Probably easiest to look at the self test code for ideas:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/LandmarkRegistration/blob/master/LandmarkRegistration.py#L984-L1013">
  <header class="source">

      <a href="https://github.com/Slicer/LandmarkRegistration/blob/master/LandmarkRegistration.py#L984-L1013" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/LandmarkRegistration/blob/master/LandmarkRegistration.py#L984-L1013" target="_blank" rel="noopener">Slicer/LandmarkRegistration/blob/master/LandmarkRegistration.py#L984-L1013</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="984" style="counter-reset: li-counter 983 ;">
          <li>    interator.SetControlKey(1)</li>
          <li>  interator.SetEventPosition(*start)</li>
          <li>  for step in range(steps):</li>
          <li>    frac = float(step+1)/steps</li>
          <li>    x = int(start[0] + frac*(end[0]-start[0]))</li>
          <li>    y = int(start[1] + frac*(end[1]-start[1]))</li>
          <li>    interator.SetEventPosition(x,y)</li>
          <li>    style.OnMouseMove()</li>
          <li>  interator.SetShiftKey(0)</li>
          <li>  interator.SetControlKey(0)</li>
          <li></li>
          <li>def setUp(self):</li>
          <li>  """ Do whatever is needed to reset the state - typically a scene clear will be enough.</li>
          <li>  """</li>
          <li>  slicer.mrmlScene.Clear(0)</li>
          <li></li>
          <li>def runTest(self,scenario=None):</li>
          <li>  """Run as few or as many tests as needed here.</li>
          <li>  """</li>
          <li>  self.setUp()</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/LandmarkRegistration/blob/master/LandmarkRegistration.py#L984-L1013" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #11 by @Tokai (2020-03-24 20:00 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a>,<br>
I followed the exact example and it got solved <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
However, It is important that in my case I had to update the transform node from python script.</p>

---
