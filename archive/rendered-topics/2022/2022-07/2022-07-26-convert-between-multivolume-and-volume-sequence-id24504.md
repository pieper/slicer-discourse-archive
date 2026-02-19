---
topic_id: 24504
title: "Convert Between Multivolume And Volume Sequence"
date: 2022-07-26
url: https://discourse.slicer.org/t/24504
---

# Convert between MultiVolume and Volume Sequence?

**Topic ID**: 24504
**Date**: 2022-07-26
**URL**: https://discourse.slicer.org/t/convert-between-multivolume-and-volume-sequence/24504

---

## Post #1 by @mikebind (2022-07-26 16:36 UTC)

<p>Hello, I am interested in doing perfusion analysis on dynamic contrast enhanced MRI images using Slicer.  I see that there are two older extensions which allow this, PkModeling and DSCMRIAnalysis, both of which are CLI modules and both of which expect MultiVolumes as input.  Using a recent Slicer 5.1 preview, I still have the option to load these series as MultiVolumes using the Advanced options in the DICOM browser, but my issue is that I want to do a rigid registration step before running the analysis.  Sequence Registration is an easy solution for this and works well as long as I provide inputs in a Volume Sequence rather than a MultiVolume.  I know that MultiVolumes and Sequences are conceptually quite similar and I think that converting between the two should be pretty easy, but I haven’t found an existing method for this. Can anyone point me in the right direction?</p>
<p>I also considered trying to update the DSCMRIAnalysis extension to take Volume Sequences as input instead of MultiVolumes, but the extension is a CLI module and I think might require getting into building Slicer and compiling from source and I think that will likely take more time and learning than I have available.  A more feasible path for me seems to be to figure out how to convert a Sequence to a MultiVolume and then feed the existing CLI extension the input it expects.</p>
<p>My workflow would then be to load the perfusion images as a Volume Sequence, register using Sequence Registration, convert to MultiVolume, and run DSCMRIAnalysis.</p>

---

## Post #2 by @mikebind (2022-07-26 21:09 UTC)

<p>Found a partial answer here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/sequences.html" class="inline-onebox" rel="noopener nofollow ugc">Sequences — 3D Slicer documentation</a>.  The MultiVolume to Sequence conversion can be accomplished by saving the MultiVolume to .nrrd and then loading the nrrd as a sequence.</p>
<p>The reverse does not seem to be possible in the same way.  If we save a Sequence to nrrd, it is saved as a .seq.nrrd, and the loading options do not seem to include MultiVolume.  The MultiVolume Importer module only accepts a folder as an input, so it will not allow you to select a .seq.nrrd or a .nrrd file.  However, I think it should work to write a small python script to save each volume in a Sequence to a temporary folder and then use the MultiVolume Importer to load it as a MultiVolume.  I’m going to try this now and see if it works, and I’ll post with the result.</p>

---

## Post #3 by @pieper (2022-07-26 21:15 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="2" data-topic="24504">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>However, I think it should work to write a small python script to save each volume in a Sequence to a temporary folder and then use the MultiVolume Importer to load it as a MultiVolume.</p>
</blockquote>
</aside>
<p>That sounds like a great idea.</p>

---

## Post #4 by @mikebind (2022-07-26 22:28 UTC)

<p>OK, for the basic Sequence → MultiVolume conversion, saving individual volumes to a temporary folder and then using MultiVolume Importer works OK.  However, for DSCMRIAnalysis to work properly, the MultiVolume needs to have some of the DICOM tags stored as attributes, and these are not collected in the loading as Sequence step. However, I can restore these by copying attribute values from the original MultiVolume (from before registration) to the registered MultiVolume.  The attributes in the original are</p>
<pre><code class="lang-auto">&gt;&gt; mvOrig.GetAttributeNames()
('DICOM.instanceUIDs', 'MultiVolume.DICOM.EchoTime', 'MultiVolume.DICOM.FlipAngle', 'MultiVolume.DICOM.RepetitionTime', 'MultiVolume.FrameIdentifyingDICOMTagName', 'MultiVolume.FrameIdentifyingDICOMTagUnits', 'MultiVolume.FrameLabels', 'MultiVolume.NumberOfFrames', 'MultiVolume.ParseStrategy')
</code></pre>
<p>I think the key ones needed are the echo time, flip angle, and repetition time.  Possibly also the frame labels (these are based on the repetition time in the original).  It seems safe just to copy all of them over.</p>
<p>Final functional workflow goes as follows:</p>
<ol>
<li>Using DICOM browser, import perfusion series as a MultiVolume and as a VolumeSequence.</li>
<li>Use Sequence Registration with the “rigid (all)” preset to register the sequence to a new Volume Sequence.</li>
<li>Save the individual nodes in the registered volume sequence to individual .nrrd files in a temporary folder.</li>
<li>Open MultiVolumeImporter and point it at the temporary folder and load as MultiVolume</li>
<li>Copy the attribute values from the original MultiVolume (non-registered) to the new MultiVolume (registered).</li>
<li>Run DSCMRIAnalysis on the registered MultiVolume.</li>
</ol>
<p>Python for step 3:</p>
<pre><code class="lang-auto">import os
import os.path
outDir = os.path.join(slicer.app.temporaryPath, 'MyUniqSubDirectoryForOutput')
os.mkdir(outDir)
seqNode = getNode('vtkMRMLSequenceNode1') # use MRML ID of the loaded sequence
browserNode = slicer.modules.sequences.logic().GetFirstBrowserNodeForSequenceNode(seqNode)
for volNum in range(browserNode.GetNumberOfItems()):
    browserNode.SetSelectedItemNumber(volNum)
    volNode = browserNode.GetProxyNode(seqNode)
    saveName = 'Im%04d.nrrd' % volNum
    slicer.util.saveNode(volNode, os.path.join(outDir, saveName)
</code></pre>
<p>I found that you needed to use the browser node in the above code because <code>slicer.util.saveNode(seqNode.GetNthDataNode(volNum), saveName)</code> does not work because the internal data nodes of the sequence are not technically present in the MRML scene, only the current proxy node is, and therefore saveNode can’t find them to save and throws an error.</p>
<p>Python for step 5:</p>
<pre><code class="lang-auto">mvOrig = getNode('vtkMRMLMultiVolumeNode1') # use MRML ID for original MultiVolumeNode
mvReg = getNode('vtkMRMLMultiVolumeNode2') # use MRML ID for imported registered 
for attr in mvOrig.GetAttributeNames():
    mvReg.SetAttribute(attr, mvOrig.GetAttribute(attr))
</code></pre>

---

## Post #5 by @lassoan (2022-07-27 08:17 UTC)

<p>We need to move away from investing any time into MultiVolume infrastructure and instead spend that time with making everything compatible with Volume Sequences (so that we can phase out the limited and mostly redundant MultiVolumes). To facilitate this, I’ve submitted a <a href="https://github.com/Slicer/Slicer/pull/6482">pull request</a> that allows selecting a volume sequence (a sequence node that contains scalar volumes) as CLI module input. After the pull request is merged, volume sequence can be used everywhere instead of multivolume as input in all CLI modules.</p>
<p><a class="mention" href="/u/mikebind">@mikebind</a> it would be great if you could test this.</p>

---

## Post #6 by @mikebind (2022-07-27 15:03 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>! I will test this as soon as it is available (tomorrow’s preview build?).</p>

---

## Post #7 by @mikebind (2022-07-27 15:22 UTC)

<p>Thinking ahead, I am guessing I will need to assign attributes to the Sequence with names “MultiVolume.DICOM.EchoTime”, etc., filled in based on DICOM metadata tag values, because that is what the DSCMRIAnalysis module looks for.  Would you anticipate that working OK using SetAttribute() on the sequence node, or are there other barriers you foresee?</p>

---

## Post #8 by @lassoan (2022-07-27 15:42 UTC)

<p>All the attributes are supposed to be collected from DICOM and saved into the nrrd file the same way as it is done for MultiVolumes.</p>

---

## Post #9 by @mikebind (2022-07-27 16:30 UTC)

<p>When I load the perfusion sequence as a volume sequence, the sequence node has no attributes (<code>seqNode.GetAttributeNames()</code> produces an empty list), and the proxy node has only attributes named <code>'DICOM.instanceUIDs'</code> and <code>'Sequences.BaseName'</code>.  Am I looking in the wrong place?  I think DSCMRIAnalysis is looking for the echo time, flip angle, and series of repetition times in attributes on the base MultiVolume named <code>'MultiVolume.DICOM.EchoTime'</code> (<a href="https://github.com/QIICR/DSC_Analysis/blob/21778ff278201a113b58f4bb4023e412a1e37b58/CLI/DSCMRIAnalysis.cxx#L43" class="inline-onebox" rel="noopener nofollow ugc">DSC_Analysis/DSCMRIAnalysis.cxx at 21778ff278201a113b58f4bb4023e412a1e37b58 · QIICR/DSC_Analysis · GitHub</a>), <code>'MultiVolume.DICOM.FlipAngle'</code>, and then a series of time stamps in <code>'MultiVolume.FrameLabels'</code> which are spaced by the repetition time.</p>
<p>I think I can gather the needed metadata using the DICOM database and the instance UIDs, but I think I will need to use that metadata to assign the expected attributes on the sequence node before DSCMRIAnalysis will work as it is currently written.</p>

---

## Post #10 by @mikebind (2022-07-27 17:56 UTC)

<p>I have verified that I can get the needed metadata from the DICOM instance UIDs as follows:</p>
<pre><code class="lang-auto"># Get proxy node for desired sequence node 
browserNode = slicer.modules.sequences.logic().GetFirstBrowserNodeForSequenceNode(seqNode)
proxNode = browserNode.GetProxyNode(seqNode)
# Get sop instance UIDs list from sequence proxy node attribute 
instUIDs = proxNode.GetAttribute('DICOM.instanceUIDs').split()
# Get first DICOM file name and location from Slicer's DICOM database
dcmFileName = slicer.dicomDatabase.fileForInstance(instUIDs[0])
# Read header metadata into pydicom data set
import pydicom
ds = pydicom.dcmread(dcmFileName)
# Gather needed parameters
echoTime = ds.EchoTime
flipAngle = ds.FlipAngle
repetitionTime = ds.RepetitionTime
</code></pre>

---

## Post #11 by @mikebind (2022-08-01 21:35 UTC)

<p>I have now verified that the modifications that <a class="mention" href="/u/lassoan">@lassoan</a> made to allow Sequence input to DSCMRIAnalysis were successful.  As suspected, it is required to add some particular expected attribute tags to the Sequence before DSCMRIAnalysis will run correctly.</p>
<pre><code class="lang-auto"># First gather the echoTime, flipAngle, and repetitionTime as shown in the previous reply message
# Make list of needed frame labels
frameLabels = " ".join(["%i"%(idx*repetitionTime) for idx in range(seqNode.GetNumberOfDataNodes())])
# Add attributes to Sequence node (note that conversion is necessary from pydicom output to regular strings)
seqNode.SetAttribute('MultiVolume.DICOM.EchoTime', "%0.1f" % echoTime)
seqNode.SetAttribute('MultiVolume.DICOM.FlipAngle', "%0.1f" % flipAngle)
seqNode.SetAttribute('MultiVolume.FrameLabels', frameLabels)
</code></pre>
<p>Once these attributes are set, DSCMRIAnalysis module runs on this Sequence without error!</p>

---

## Post #12 by @lassoan (2022-08-01 22:10 UTC)

<p>Thanks for the update, it is very promising! However, it would be even nicer if this manual adding of the acquisition information was not necessary.</p>
<p>It seems that <a href="https://github.com/fedorov/MultiVolumeImporter/blob/db805948534563566f0a39c63e8d60fac0b63dcd/MultiVolumeImporterPlugin.py#L455-L461">MultiVolumeImporter DICOM plugin can write these tags into node attributes of the imported sequence</a>. Could you check why these node attributes not end up being added?</p>

---

## Post #13 by @mikebind (2022-08-01 22:20 UTC)

<p>Yes, I will look into this.  I didn’t realize these attributes should be automatically added to all sequences on import from DICOM.  That would indeed be more convenient.</p>

---

## Post #14 by @mikebind (2022-08-02 00:31 UTC)

<p>The problem is in the <code>load()</code> function: <a href="https://github.com/fedorov/MultiVolumeImporter/blob/db805948534563566f0a39c63e8d60fac0b63dcd/MultiVolumeImporterPlugin.py#L574" class="inline-onebox" rel="noopener nofollow ugc">MultiVolumeImporter/MultiVolumeImporterPlugin.py at db805948534563566f0a39c63e8d60fac0b63dcd · fedorov/MultiVolumeImporter · GitHub</a></p>
<p>The attributes come in <code>loadable.multivolume</code> for both sequences and multivolumes, but where the output multivolume is just this input multivolume (with attributes intact), the output sequence is created from scratch and never has the attributes added to it.  I’ll fix this and send a PR to the MultiVolumeImporter repo.</p>

---

## Post #15 by @lassoan (2022-08-02 09:40 UTC)

<p>That would be great, thank you!</p>

---

## Post #16 by @mikebind (2022-08-02 18:28 UTC)

<p>PR sent: <a href="https://github.com/fedorov/MultiVolumeImporter/pull/51" class="inline-onebox" rel="noopener nofollow ugc">ENH: Transfer attributes to Sequence node by mikebind · Pull Request #51 · fedorov/MultiVolumeImporter · GitHub</a></p>

---

## Post #17 by @fedorov (2022-08-02 19:05 UTC)

<p>PR merged - thank you!</p>

---

## Post #18 by @alaa (2023-03-14 03:01 UTC)

<p>may I know how to apply this practically, I am having very hard time converting volume sequence after registration to multivolume.</p>

---

## Post #19 by @mikebind (2023-03-14 15:15 UTC)

<p>What is going wrong?  The improvements above should make conversion to MultiVolume unnecessary in most situations.  Usually, you should be able to use a volume Sequence directly without conversion.</p>

---

## Post #20 by @alaa (2023-03-14 19:22 UTC)

<p>the goal of my study is to examine the change of HU across different frames for different areas in the scan.<br>
previously i used to select a larger area and plot it through multivolume explorer (slicer 4.) and get a chart that reflect the changes of HU for that area.<br>
Now, I am having more motions in the scan and I am investigating smaller areas. I am converting the multivolume to sequence volume and register the frames for motion but I can’t use this file to chart the intensity changes based on my segmentation, I was looking to convert this sequence volume to multivolume so I can process as i used to process it before through multivolume importer then multivolume explorer</p>

---

## Post #21 by @mikebind (2023-03-14 21:34 UTC)

<p>I would suggest two possible approaches, one using multivolumes, and one staying with sequences.</p>
<ul>
<li>If you want to continue to use multivolume explorer, try steps 1-5 of the reply above (<a href="https://discourse.slicer.org/t/convert-between-multivolume-and-volume-sequence/24504/4" class="inline-onebox">Convert between MultiVolume and Volume Sequence? - #4 by mikebind</a>).  This worked for me to successfully convert a registered volume sequence back to a multivolume.</li>
<li>If you are open to a different approach which will not rely on the outdated multivolume infrastructure, I would suggest segmenting your region of interest in Segment Editor with the first volume of the sequence as the master volume (setting the segmentation geometry).  Then, use the Segment Statistics module to find the average voxel value in your segment.  If you step through the frames of your sequence, you can gather the average voxel value in the segment for each frame.  Once you have verified that you can successfully carry out this process, you can automate it with a python scripted module fairly easily.</li>
</ul>

---

## Post #22 by @ashgillman (2023-11-15 06:15 UTC)

<p>Hi,<br>
Sorry to bump an old thread, but I think the context here might be useful.</p>
<p>I’m trying to use PkModelling with Volume Sequences. I run into an error:</p>
<pre><code class="lang-auto">vtkMRMLSequenceStorageNode::WriteDataInternal: No file extension recognized: /private/var/folders/_3/5s_kvnhj53x7sny2_71tf3lr0000gp/T/Slicer-gil2a4/BIJDD_vtkMRMLSequenceNodeBA.nrrd


ERROR writing file /private/var/folders/_3/5s_kvnhj53x7sny2_71tf3lr0000gp/T/Slicer-gil2a4/BIJDD_vtkMRMLSequenceNodeBA.nrrd
</code></pre>
<p>Happy to help further debug, but not sure how.</p>
<p>As far as I can tell, PkModelling (maybe all Slicer extensions?) saves out the inputs to temp files and runs a command line job on them. It tries to save them out to an .nrrd file (not sure where this is defined or if it can be changed). But the Sequence class seems only to be able to write to .mrb: <a href="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLSequenceStorageNode.cxx#L148-L203" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLSequenceStorageNode.cxx#L148-L203</a></p>
<p>Should the sequence node be able to write as a dynamic .nrrd file?</p>

---
