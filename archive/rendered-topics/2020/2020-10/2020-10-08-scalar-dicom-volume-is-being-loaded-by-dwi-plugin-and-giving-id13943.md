---
topic_id: 13943
title: "Scalar Dicom Volume Is Being Loaded By Dwi Plugin And Giving"
date: 2020-10-08
url: https://discourse.slicer.org/t/13943
---

# Scalar DICOM volume is being loaded by DWI plugin and giving errors

**Topic ID**: 13943
**Date**: 2020-10-08
**URL**: https://discourse.slicer.org/t/scalar-dicom-volume-is-being-loaded-by-dwi-plugin-and-giving-errors/13943

---

## Post #1 by @mikebind (2020-10-08 19:37 UTC)

<p>Sometimes, when I load a non-diffusion MR DICOM volume, I get errors during loading which come from DWIConvert.  Most recently, I got this, which I think is what I usually get:</p>
<pre><code>Diffusion-weighted DICOM Import (DWIConvert) standard error:

C:/Users/mikeb/AppData/Local/Temp/Slicer/__SlicerTemp__2020-10-08_12+09+45.638/Im00000 has no non-zero diffusion vectors
</code></pre>
<p>In the Data module, two volumes have appeared: “T1_mprage+c - as DWI Volume” and “27: T1_mprage+c”.  The second one seems to be exactly what I wanted, the first shows up as a DWIVolume, but there’s no diffusion information (because there isn’t any in the original DICOM). I assume something is going wrong with determining which plugin should load it, and the DWI plugin thinks it should be the one.  Is there a way for me to force the loading to use the right plugin?  In this case, the user has been prompted to choose a scalar volume, so even if they chose a directory containing a DWI volume I don’t want it to load, I only want to load a scalar volume.</p>
<p>This is the function which is currently doing the loading, which is lightly modified from an example in the script repository:</p>
<pre><code>  def loadDicomVolumeFromDirectory(self, dicomDir):
    '''Loads DICOM image files in supplied directory, returns list of loaded volume nodes and
    list of corresponding pydicom headers. 
    '''
    # This code modified from script in script repository
    loadedNodes = []
    loadedNodeHeaders = []
    #from DICOMLib import DICOMUtils
    with DICOMUtils.TemporaryDICOMDatabase() as db:
      DICOMUtils.importDicom(dicomDir, db)
      patientUIDs = db.patients()
      for patientUID in patientUIDs:
        newVolNodeIDs = DICOMUtils.loadPatientByUID(patientUID)
        for newVolnodeID in newVolNodeIDs:
          node = slicer.util.getNode(newVolnodeID)
          instanceUIDs = node.GetAttribute('DICOM.instanceUIDs').split()
          filepath = db.fileForInstance(instanceUIDs[0])
          newHeader = pydicom.dcmread(filepath)
          loadedNodeHeaders.append(newHeader)
          loadedNodes.append(node)
    return loadedNodes, loadedNodeHeaders</code></pre>

---

## Post #2 by @pieper (2020-10-08 20:15 UTC)

<p>For many vendors it’s hard to know if a file is meant to be part of a DWI study without looking at all the headers, so the dicom loader <a href="https://github.com/SlicerDMRI/SlicerDMRI/blob/master/Modules/Scripted/DMRIPlugins/DICOMDiffusionVolumePlugin.py#L20-L46">makes a guess based on heuristics</a>.</p>
<p>The easiest might be to turn off DMRI, or maybe rework the script to avoid using the plugin.  Even better could be to suggest improved logic to fix the false positives.</p>

---

## Post #3 by @mikebind (2020-10-08 20:27 UTC)

<p>Thanks, I was hoping for guidance on how to rework the script to force use of whatever plugin loads regular scalar volumes.  Is it an additional input to DICOMUtils.importDicom()?</p>

---

## Post #4 by @pieper (2020-10-08 20:50 UTC)

<p>Do you need SlicerDMRI for your script?  If your study contains some DWI and some non-DWI the best option would be to improve the plugin so it can tell the difference reliably.</p>

---

## Post #5 by @mikebind (2020-10-08 20:59 UTC)

<p>Sometimes (relatively rarely) we load and work with DWI images, so I didn’t want to remove that as an option entirely.  I looked at your link, but still don’t fully understand how the heuristics work.  If any of the given tags are present and/or non-empty is it assumed that the volume is of the type that could be handled by that plugin?</p>

---

## Post #6 by @pieper (2020-10-08 21:09 UTC)

<p>Each dicom plugin is given lists of files (all the instances in a series) and it returns a set of <code>loadables</code> corresponding to to the one or more MRML objects it can extract from the series.  Each <code>loadable</code> is assigned a <code>confidence</code> by the plugin.  Normally the most confident plugin is used, but this can be overridden by the user in the Advanced part of the dicom module.</p>
<p>The DWI plugin looks to see if the headers are consistent with things seen in DWI scans, but it’s not a perfect heuristic.  The actual heuristic currently is:<br>
</p><aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerDMRI/SlicerDMRI/blob/master/Modules/Scripted/DMRIPlugins/DICOMDiffusionVolumePlugin.py#L96-L109" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerDMRI/SlicerDMRI/blob/master/Modules/Scripted/DMRIPlugins/DICOMDiffusionVolumePlugin.py#L96-L109" target="_blank" rel="noopener">SlicerDMRI/SlicerDMRI/blob/master/Modules/Scripted/DMRIPlugins/DICOMDiffusionVolumePlugin.py#L96-L109</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="96" style="counter-reset: li-counter 95 ;">
<li>vendorName = ""</li>
<li>for vendor in self.diffusionTags:</li>
<li>  matchesVendor = True</li>
<li>  for tag in self.diffusionTags[vendor]:</li>
<li>    # Check the first three files because some tags may</li>
<li>    # not be present in the b0 image (e.g. for Siemens)</li>
<li>    for i in range(0, 3 if (len(files) &gt; 2) else len(files)):</li>
<li>      value = slicer.dicomDatabase.fileValue(files[i], tag)</li>
<li>      hasTag = value != ""</li>
<li>      if hasTag:</li>
<li>        matchesVendor &amp;= hasTag</li>
<li>  if matchesVendor:</li>
<li>    validDWI = True</li>
<li>    vendorName = vendor</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>But that can obviously be improved to minimize false positives.</p>

---

## Post #7 by @mikebind (2020-10-08 22:17 UTC)

<p>Thanks, I’ll try to contribute. So far, I’ve figured out that the volume I’m working with (Siemens T1MPRAGE) has</p>
<ul>
<li>‘0051,100b’, # “Mosiac Matrix Size”</li>
<li>‘0029,1010’, # “Siemens DWI Info”</li>
</ul>
<p>despite not being a DWI volume. It does not have any of the other tags listed for Siemens DWI volumes. I’ll try to put together a PR tomorrow which removes those two tags as criteria and fixes a bug in the vendor assignment code.</p>

---

## Post #8 by @pieper (2020-10-08 22:21 UTC)

<p>Sounds good, thanks.  Try to avoid any changes that could lead to false negatives since there may be variants of DWI files from different Siemens machines.</p>

---

## Post #9 by @mikebind (2020-10-08 22:52 UTC)

<p>I got a chance to do it now, this is the PR: <a href="https://github.com/SlicerDMRI/SlicerDMRI/pull/143" rel="noopener nofollow ugc">https://github.com/SlicerDMRI/SlicerDMRI/pull/143</a></p>
<p>It is possible, though I think unlikely, that these changes could lead to false negatives (if there are any Siemens DWI volumes which have only those two tags and none of the others).  They definitely will eliminate my false positives.</p>
<p>The vendor name assignment code was just incorrect, so even if the SlicerDMRI team decides not to drop the tags, the other changes are a bugfix which should be retained (or fixed in some other way, just don’t revert).</p>

---

## Post #10 by @pieper (2020-10-09 17:52 UTC)

<p>Thanks, the logic looks good to me.  Let’s see if the rest of the SlicerDMRI team have any comments.</p>

---
