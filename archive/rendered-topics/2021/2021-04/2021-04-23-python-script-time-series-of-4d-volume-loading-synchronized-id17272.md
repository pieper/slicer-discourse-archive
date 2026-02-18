# Python script : Time series of 4D volume & loading synchronized nodes

**Topic ID**: 17272
**Date**: 2021-04-23
**URL**: https://discourse.slicer.org/t/python-script-time-series-of-4d-volume-loading-synchronized-nodes/17272

---

## Post #1 by @valery (2021-04-23 12:26 UTC)

<p>Hello,</p>
<p>I’m playing with 4D data format and Slicer. I found lots of information on the forum but I’m looking for additional details.</p>
<h3><a name="p-58585-the-final-objective-1" class="anchor" href="#p-58585-the-final-objective-1" aria-label="Heading link"></a>The final objective.</h3>
<p>To load multiple 4D nifti volume (3D+time) in the sequence module and synchronise them to plot for instance the 1D profil of all datasets together. Such routine have to be done with the python script.</p>
<h3><a name="p-58585-the-current-workflow-2" class="anchor" href="#p-58585-the-current-workflow-2" aria-label="Heading link"></a>The current workflow.</h3>
<p>a) conversion of the 4D nifti in nrrd file that is the format dedicated to handle 4D data in slicer. I used the multivolume importer.  [OK]<br>
b) save the data as an nrrd. [OK] Reloading the nrrd file and plotting them work using the multivolume explorer [OK]<br>
c) Load the nrrd file as a sequence node, as suggested here [OK] <a href="https://discourse.slicer.org/t/loading-4d-volume-as-sequence-using-python-script/13076/4">link</a><br>
d) load the nrrd file as synchronized node in the sequence module ?</p>
<h3><a name="p-58585-the-questions-3" class="anchor" href="#p-58585-the-questions-3" aria-label="Heading link"></a>The questions</h3>
<p>In a) I have a warning message for</p>
<pre><code class="lang-auto">    Warning: /home/vozenne/Test_D_0.5_Q_0.75.nii.gz does not have TimeSeries intent, instead it has "Nothing"
Trying to read as TimeSeries anyway
</code></pre>
<p>That’s expected becasue the nifti format only specify the “spacing” of each direction. The 4th dimension being the time but to my knowledge, there is no specific time header per image in nifti.</p>
<ul>
<li>Q1: Is it possible to fill the TimeSeries information inside slicer  ?</li>
<li>Q2: Is it possible to change the name of the node, or to change the name of sequence node using python ?</li>
</ul>
<p>Q3 While step a), b) and c) is working , the code create two sequences (this is normal) but I wish to have one sequence with synchronized nodes, do you have any example in python for such feature ?</p>
<p>Thanks in advance<br>
Best<br>
Valéry</p>
<p>I put the code below</p>
<pre><code class="lang-auto">import numpy as np
import os 

import MultiVolumeImporter

importer = MultiVolumeImporter.MultiVolumeImporterWidget()

mvNode1 = slicer.mrmlScene.CreateNodeByClass('vtkMRMLMultiVolumeNode')
slicer.mrmlScene.AddNode(mvNode1)
niiFilePath ="/home/vozenne/Test_D_0.5_Q_0.5.nii.gz"
importer.read4DNIfTI(mvNode1, niiFilePath)
slicer.util.saveNode(mvNode1 , "/home/vozenne/Test_D_0.5_Q_0.5.nrrd")


mvNode2 = slicer.mrmlScene.CreateNodeByClass('vtkMRMLMultiVolumeNode')
slicer.mrmlScene.AddNode(mvNode2)
niiFilePath ="/home/vozenne/Test_D_1_Q_1.nii.gz"
importer.read4DNIfTI(mvNode2, niiFilePath)
slicer.util.saveNode(mvNode2 , "/home/vozenne/Test_D_1_Q_1.nrrd")

# see https://discourse.slicer.org/t/loading-4d-volume-as-sequence-using-python-script/13076/4
sequenceNode1 = slicer.util.loadNodeFromFile("/home/vozenne/Test_D_0.5_Q_0.5.nrrd", "SequenceFile")
sequenceNode2 = slicer.util.loadNodeFromFile("/home/vozenne/Test_D_1_Q_1.nrrd", "SequenceFile")
#exit()
</code></pre>

---

## Post #2 by @lassoan (2021-04-23 15:09 UTC)

<p>MultiVolume is limited to working with volumes only and can do synchronize browsing of only two volumes at a time. Sequences module does not have any of these limitations, can work with any node types (models, transforms, markups, etc) and can do synchronized browsing of any number of nodes. Due to these reasons, MultiVolume modules will be deprecated soon (there are just a few minor features that need to be made available for sequences). So, I would recommend to use Sequences instead of MultiVolume. If you save a multivolume node then you can load is a volume sequence if you choose that in the Description column in “Add data” dialog (or you can make Slicer automatically load a nrrd file as a volume sequence if the file extension is <code>.seq.nrrd</code>).</p>
<p>Nifti file format has many issues and limitations, so we have been trying to convince people to use nrrd instead (unless they actually use nifti what it is developed for - brain imaging). Why would you like to use nifti instead of nrrd?</p>
<p>For plotting time plots for many volumes, you need to write a small Python script, as MultiVolume supports plotting two, and Sequences module supports plotting only one.</p>

---

## Post #3 by @valery (2021-04-23 16:21 UTC)

<p>Thanks a lot for  the quick answer. I should explain better my issue and also answer the following question:</p>
<p>“Why would you like to use nifti instead of nrrd?”</p>
<p>Yes , this is not ideal. But the data are currently generated in NIFTI and I did know that this is not Slicer compatible for 3D+t so I convert them in nrrd. This easiest way I found to convert them in nrrd was to load them using Slicer using the multivolume importer and to save them. I wish I will remove this step in the future and not use anymore the MultiVolumeImporter.</p>
<p>But let’s forget this part I should have focus my questions.</p>
<h3><a name="p-58630-description-of-my-issue-1" class="anchor" href="#p-58630-description-of-my-issue-1" aria-label="Heading link"></a>Description of my issue</h3>
<p>Here is the new description of my issue (My terminology is maybe/surely wrong, I apologized for my bad understanding of the sequence module. )</p>
<pre><code class="lang-auto">sequenceNode1 = slicer.util.loadNodeFromFile("/home/vozenne/A.nrrd", "SequenceFile")
sequenceNode2 = slicer.util.loadNodeFromFile("/home/vozenne/B.nrrd", "SequenceFile")
</code></pre>
<ul>
<li>Using  the two previous lines of code, I can load the two .nrrd files as sequence and play them. This is perfectly working.</li>
<li>The code below create 2 sequences browser (named A_browser &amp; B_browser) with one sequence (or node ?) for each (A &amp; B respectively) .</li>
<li>In the interface , under the panel synchronized nodes,  using the [+] button I can add the sequence B to the sequence browser A_browser. Then A and B seems synchronized.</li>
</ul>
<p>But I didn’t find how to perform the final step in python.</p>
<h3><a name="p-58630-questions-2" class="anchor" href="#p-58630-questions-2" aria-label="Heading link"></a>Questions</h3>
<ul>
<li>Do you have any link to an example, or similar example ?</li>
<li>I wish learn more in detail how to use the sequence module, what/where would be the best doc/code to learn about the sequence module and the terminology ( sequence browser, sequence, and proxy  )?</li>
</ul>
<h3><a name="p-58630-plotting-3" class="anchor" href="#p-58630-plotting-3" aria-label="Heading link"></a>Plotting</h3>
<p>“For plotting time plots for many volumes”<br>
I’m effectively planning to write a small Python script, I wish to use the sequence module and find a way to plot synchronized nodes together.  Maybe in a none interactive fashion using numpy at first ?</p>
<p>Is there an equivalent of slicer.util.arrayFromVolume for the sequence module?   For instance, does a sequence with can be considered as a standard object in slicer. By the past, I succeed to write some  python scripts for plotting images , making figures on multiple datasets and typical overlay with presonnalized display configuration (with displayNode  option for instance). For doing such scripts,  I mostly copy and paste code from the forum,  example and documentation, it was perfect but now I’m a bit lost the sequence module in particular for loading and manipulating the data.</p>
<p>Thanks a lot in advance for your help,</p>

---

## Post #4 by @lassoan (2021-04-23 17:16 UTC)

<aside class="quote no-group" data-username="valery" data-post="3" data-topic="17272">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/a87d85/48.png" class="avatar"> valery:</div>
<blockquote>
<ul>
<li>under the panel synchronized nodes, using the [+] button I can add the sequence B to the sequence browser A_browser. Then A and B seems synchronized.</li>
</ul>
<p>But I didn’t find how to perform the final step in python.</p>
</blockquote>
</aside>
<p>I would recommend to load the sequences with automatic showing disabled (to prevent creating browser nodes), and then create one browser node and add all the sequences:</p>
<pre data-code-wrap="python"><code class="lang-python">sequenceFiles = ["/home/vozenne/A.nrrd", , "/home/vozenne/B.nrrd"]
browserNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSequenceBrowserNode")
for sequenceFile in sequenceFiles:
  sequenceNode = slicer.util.loadNodeFromFile(sequenceFile, "SequenceFile", {"show": False})
  browserNode.AddSynchronizedSequenceNode(sequenceNode)

# Show sequence browser toolbar
slicer.modules.sequences.showSequenceBrowser(browserNode)
</code></pre>
<aside class="quote no-group" data-username="valery" data-post="3" data-topic="17272">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/a87d85/48.png" class="avatar"> valery:</div>
<blockquote>
<p>Is there an equivalent of slicer.util.arrayFromVolume for the sequence module?</p>
</blockquote>
</aside>
<p>See <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Access_voxels_of_a_4D_volume_as_numpy_array">this example</a> in the script repository.</p>

---

## Post #5 by @valery (2021-04-23 17:33 UTC)

<p>Thanks so much, it is working perfectly.<br>
The section Sentences mentioned in the example was unknown to me, sorry.<br>
I might have other questions regarding the plotting in the close future .<br>
Best<br>
Valéry</p>

---
