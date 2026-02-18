# Loading patient DICOM files containing multiple Volume Sequences

**Topic ID**: 29711
**Date**: 2023-05-29
**URL**: https://discourse.slicer.org/t/loading-patient-dicom-files-containing-multiple-volume-sequences/29711

---

## Post #1 by @EvanMcNabb (2023-05-29 15:10 UTC)

<p>Hi I am having an issue loading a patient dicom list (i.e., the entire patient) that contains multiple Volume Sequences. I am ultimately trying to open these data on the python CLI but I can replicate the behaviour in the UI as well.</p>
<p>In this example I have two multi volume MRI series (a dual echo and DWI with 2 b-values). If I examine each series individually, I see there is a <code>MultiVolume</code> Reader available and can select to open it as a Volume Sequence. Works great. If you examine the patient (which auto selects all the series), then only the Dual Echo has a <code>MultiVolume</code> Reader available and the DWI only has a <code>Scalar Volume</code> importer now. It’s not a case where Scalar Volume is selected by default and I can manually click a MultiVolume importer, it simply doesn’t exist any longer.</p>
<p>This can be seen using the python CLI as well. I am using the strategy from a previous post where you iterate over a file list with user-defined <code>pluginClassNames</code>. If I choose <code>pluginClassNames=["MultiVolumeImporterPlugin", "DICOMScalarVolumePlugin"]</code> I can see this same behaviour shown below.</p>
<p><strong>Dual Echo folder alone finds a <code>MultiVolumeImporterPlugin </code></strong></p>
<pre><code class="lang-auto">&lt;MultiVolumeImporterPlugin.MultiVolumeImporterPluginClass object at 0x000001C5E5872670&gt;
Ax Dualecho FSPGR BH - as a 2 frames Volume Sequence by EchoTime

&lt;MultiVolumeImporterPlugin.MultiVolumeImporterPluginClass object at 0x000001C5E5872670&gt;
Ax Dualecho FSPGR BH - as a 2 frames Volume Sequence by ImagePositionPatient+InstanceNumber
 
&lt;MultiVolumeImporterPlugin.MultiVolumeImporterPluginClass object at 0x000001C5E5872670&gt;
Ax Dualecho FSPGR BH - as a 2 frames MultiVolume by EchoTime
 
&lt;MultiVolumeImporterPlugin.MultiVolumeImporterPluginClass object at 0x000001C5E5872670&gt;
Ax Dualecho FSPGR BH - as a 2 frames MultiVolume by ImagePositionPatient+InstanceNumber
 
&lt;DICOMScalarVolumePlugin.DICOMScalarVolumePluginClass object at 0x000001C5E5872190&gt;
5: Ax Dualecho FSPGR BH
</code></pre>
<p><strong>DWI folder alone finds a <code>MultiVolumeImporterPlugin</code></strong></p>
<pre><code class="lang-auto">&lt;MultiVolumeImporterPlugin.MultiVolumeImporterPluginClass object at 0x000001C5E2C6F280&gt;
Ax DWI BH  b-500 Free Breathing - as a 2 frames Volume Sequence by ImagePositionPatient+InstanceNumber
 
&lt;MultiVolumeImporterPlugin.MultiVolumeImporterPluginClass object at 0x000001C5E2C6F280&gt;
Ax DWI BH  b-500 Free Breathing - as a 2 frames MultiVolume by ImagePositionPatient+InstanceNumber
 
&lt;DICOMScalarVolumePlugin.DICOMScalarVolumePluginClass object at 0x000001C5E2C6F310&gt;
13: Ax DWI BH  b-500 Free Breathing
</code></pre>
<p><strong>Patient folder containing both series cannot find <code>MultiVolumeImporterPlugin</code> for both</strong></p>
<pre><code class="lang-auto">&lt;MultiVolumeImporterPlugin.MultiVolumeImporterPluginClass object at 0x000001C5E58729D0&gt;
Ax Dualecho FSPGR BH - as a 2 frames Volume Sequence by EchoTime
 
&lt;MultiVolumeImporterPlugin.MultiVolumeImporterPluginClass object at 0x000001C5E58729D0&gt;
Ax DWI BH  b-500 Free Breathing - as a 2 frames Volume Sequence by ImagePositionPatient+InstanceNumber
 
&lt;MultiVolumeImporterPlugin.MultiVolumeImporterPluginClass object at 0x000001C5E58729D0&gt;
Ax Dualecho FSPGR BH - as a 2 frames MultiVolume by EchoTime
 
&lt;MultiVolumeImporterPlugin.MultiVolumeImporterPluginClass object at 0x000001C5E58729D0&gt;
Ax DWI BH  b-500 Free Breathing - as a 2 frames MultiVolume by ImagePositionPatient+InstanceNumber
 
&lt;DICOMScalarVolumePlugin.DICOMScalarVolumePluginClass object at 0x000001C5E5872460&gt;
5: Ax Dualecho FSPGR BH
 
&lt;DICOMScalarVolumePlugin.DICOMScalarVolumePluginClass object at 0x000001C5E5872460&gt;
13: Ax DWI BH  b-500 Free Breathing
</code></pre>
<p>Any possible way to add both as Volume Sequences?</p>
<p>Thanks!</p>

---

## Post #2 by @ATAKAN_Isik (2023-05-29 16:44 UTC)

<p>Open Slicer Gui and Select Preferences. In DICOM menu you can see loading setting set as volume sequences not multi-volume and try.<br>
Keep us informed.<br>
Good Luck</p>

---

## Post #3 by @EvanMcNabb (2023-05-29 18:09 UTC)

<p>It’s already set to prefer volume sequences. That’s not the question I’m asking.</p>
<p>I have no issues loading dicom series as volume sequence one at a time. The problem lies in loading <em>multiple</em> volume sequences in a list of series.</p>

---

## Post #4 by @ATAKAN_Isik (2023-05-29 18:49 UTC)

<p>had u tried load each series and examine with multiVolume Explorer ? maybe your DWI data has a scalar tensor then u need to decompose series and merge into one dicom. Also i can see just one b value on your DWI series .is b0 omitting or default value of b0 is 0 ?</p>

---

## Post #5 by @EvanMcNabb (2023-05-29 20:07 UTC)

<p>Thanks for the reply. No I haven’t used MultiVolume explorer yet. As for the b0, I think that’s just the name of the sequence. There is a T2/b0 series in the same folder.</p>
<p>The DWI (and dual echo) both load as volume sequences which is what I want. You just have to load them one at a time. What I would like to do is load an entire patient that contains both of these series, and have them both load as volume sequences. (I would like to get this functionality implemented so that I can do this on the CLI)</p>
<p>I have janky CLI solution now which is to iterate over the subdirectories and use each of them as a temporary dicom database. While it works, I feel like I’m missing something and should be able to load multiple sequences in one load call on the top level directory.</p>

---

## Post #6 by @lassoan (2023-05-29 20:22 UTC)

<p>Thanks for reporting this. Since DICOM does not specify how applications should sort and group slices in a series or study to make up volumes  (and manufacturers very often implement the DICOM standard incorrectly anyway), we had to complement complex heuristics that try to guess what interpretation a user may want for the selection in the DICOM browser.</p>
<p>If you select an entire study then Slicer will attempt to reconstruct volumes from multiple series in the study. If this reconstruction seems more appropriate than the reconstruction from each series then it may change how the data is loaded by default.</p>
<p>The loadable that you miss when you select an entire study is <code>Ax Dualecho FSPGR BH - as a 2 frames ... by ImagePositionPatient+InstanceNumber</code>. This is because this is a very special case of loading by ImagePositionPatient+InstanceNumber, which was added for reading some incorreclty stored GE DSC MRI scans, which required lumping together multiple series before splitting them by ImagePositionPatient+InstanceNumber.</p>
<p>Unfortunately, this series detection/grouping mechanism becomes much more complicated (and more time consuming) if we also need to figure out which series should be lumped together.</p>
<p>I would recommend to have a look at <code>MultiVolumeImporterPlugin.py</code> (around the code that handles the <code>ImagePositionPatient+InstanceNumber</code> case) and see if you can improve the detection mechanism.</p>

---

## Post #7 by @EvanMcNabb (2023-05-29 21:18 UTC)

<p>Thank you for the explanation, appreciate it.</p>
<p>I managed to somewhat get this working using slicer’s dicom tools. I added a second pass with a new <code>loadableSuffix</code>. Then a second set of <code>loadableNodeIDs</code> can be generated where you find <code>Volume Sequence as EchoTime</code> or <code>Volume Sequence as ImagePatientPosition+InstanceNumber</code>. I swear I tried this idea earlier but I couldn’t get it working.</p>
<p>Fair to say the issue is solved. It works for the CLI now which is what I was after.</p>
<p>The UI still doesn’t handle this though, but I guess that’s because of the reasons you listed.</p>
<p>I can look at that code, thanks for pointing out the file.</p>

---

## Post #8 by @ATAKAN_Isik (2023-05-30 10:11 UTC)

<p>I think your dwi data has one b value so it is not actually mutlivolume for diffusion weight could you find any example set with multiple b value and try it with multi echo</p>

---
