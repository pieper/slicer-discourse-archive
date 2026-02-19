---
topic_id: 22085
title: "Unnamed Series As A Scalar Volume"
date: 2022-02-21
url: https://discourse.slicer.org/t/22085
---

# Unnamed Series as a Scalar Volume

**Topic ID**: 22085
**Date**: 2022-02-21
**URL**: https://discourse.slicer.org/t/unnamed-series-as-a-scalar-volume/22085

---

## Post #1 by @dicom (2022-02-21 14:16 UTC)

<p>Dear all,</p>
<p>I am new to Dicom and Slicer3D. I am trying to open a Dicom image (PET) with Slicer3D and I got this error message:</p>
<pre><code class="lang-auto">
"DICOM indexer has successfully inserted 200 files [0.09s]"
"DICOM indexer has successfully processed 200 files [0.19s]"
"DICOM indexer has updated display fields for 1 files [0.01s]"
Imported a DICOM directory, checking for extensions
Found CommandLine Module, target is  /home/Software/Slicer-4.11.20210226-linux-amd64/NA-MIC/Extensions-29738/PETDICOMExtension/lib/Slicer-4.11/cli-modules/SUVFactorCalculator
ModuleType: CommandLineModule
SUV Factor Calculator command line: 

/home/Software/Slicer-4.11.20210226-linux-amd64/NA-MIC/Extensions-29738/PETDICOMExtension/lib/Slicer-4.11/cli-modules/SUVFactorCalculator --returnparameterfile /tmp/Slicer/46864_CKzkHa2WTH.params --petDICOMPath /tmp/tmprlh1_teo --petSeriesInstanceUID 1.2.276.0.7230010.3.1.4.2088271309.2146774.1645448741.472356 --rwvmDICOMPath /home/Software/test/final__baseline_test --seriesDescription PET SUV Factors --seriesNumber 1000 --instanceNumber "1" 

SUV Factor Calculator standard output:

saving numbers to /tmp/Slicer/46864_CKzkHa2WTH.params

SUV Factor Calculator standard error:

Missing some parameters...
ERROR: Failed to compute SUV


SUV Factor Calculator completed with errors


Traceback (most recent call last):
  File "/home/Software/Slicer-4.11.20210226-linux-amd64/lib/Slicer-4.11/qt-scripted-modules/DICOMLib/DICOMUtils.py", line 678, in getLoadablesFromFileLists
    loadablesByPlugin[plugin] = plugin.examine(fileLists)
  File "/home/Software/Slicer-4.11.20210226-linux-amd64/NA-MIC/Extensions-29738/PETDICOMExtension/lib/Slicer-4.11/qt-scripted-modules/DICOMPETSUVPlugin.py", line 127, in examine
    rwvmFile = self.generateRWVMforFileList(fileList)
  File "/home/Software/Slicer-4.11.20210226-linux-amd64/NA-MIC/Extensions-29738/PETDICOMExtension/lib/Slicer-4.11/qt-scripted-modules/DICOMPETSUVPlugin.py", line 169, in generateRWVMforFileList
    raise RuntimeError("SUVFactorCalculator CLI did not complete cleanly")
RuntimeError: SUVFactorCalculator CLI did not complete cleanly
DICOM Plugin failed: SUVFactorCalculator CLI did not complete cleanly
Loading with imageIOName: GDCM
DICOM plugin failed to load '1: Unnamed Series' as a 'Scalar Volume'.
Traceback (most recent call last):
  File "/home/Software/Slicer-4.11.20210226-linux-amd64/lib/Slicer-4.11/qt-scripted-modules/DICOMLib/DICOMUtils.py", line 719, in loadLoadables
    loadSuccess = plugin.load(loadable)
  File "/home/Software/Slicer-4.11.20210226-linux-amd64/bin/../lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py", line 509, in load
    self.setVolumeNodeProperties(volumeNode, loadable)
  File "/home/Software/Slicer-4.11.20210226-linux-amd64/bin/../lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py", line 471, in setVolumeNodeProperties
    displayNode.SetAndObserveColorNodeID(slicer.modules.colors.logic().GetPETColorNodeID(slicer.vtkMRMLPETProceduralColorNode.PETheat))
UnboundLocalError: local variable 'displayNode' referenced before assignment
</code></pre>
<p>I looked at several similar topic in this forum and this error message probably comes from my DICOM format implementation. I followed the inputs from the FAQ for debbuging (<a href="https://www.slicer.org/wiki/Documentation/4.10/FAQ/DICOM" class="inline-onebox" rel="noopener nofollow ugc">Documentation/4.10/FAQ/DICOM - Slicer Wiki</a>) but the Patient name, patient ID, and series instance UID fields are neither empty or missing in my configuration. Therefore I do not know what else I can check.</p>
<p>Please find my dataset at this link: <a href="https://drive.google.com/drive/folders/127ATybREng6PCKhTeMtJ9fe1j5FuBcUd?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">DICOM_files - Google Drive</a></p>
<p>Let me know if you need all the DICOM instructions I defined.</p>
<p>Best,<br>
M.</p>

---

## Post #2 by @lassoan (2022-02-21 19:00 UTC)

<p>Please latest Slicer Preview Release and let us know if the problem persists.</p>

---

## Post #3 by @dicom (2022-02-21 19:01 UTC)

<p>Dear Andras,</p>
<p>Thanks a lot for helping.<br>
I have the latest Slice Preview Release but still have the problem</p>
<p>Best,<br>
Marina</p>

---

## Post #4 by @lassoan (2022-02-25 15:30 UTC)

<p>Thanks for testing. The image appears as all black when you load it into Slicer because the same SOP instance UID was used in all the files. DICOM export is very complicated, there are many rules to follow, so if you need to create images from scratch then I would recommend to inspect the content of DICOM files coming from clinical scanners and use the freely available DICOM standard to understand each field and why it is there.</p>
<p>The PETDICOM extension throws errors because it misses some of the fields required for computing SUV:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/QIICR/Slicer-PETDICOMExtension/blob/4feafda0a4a58132e50ad527726622a65ac061e5/SUVFactorCalculatorCLI/SUVFactorCalculator.cxx#L692-L697">
  <header class="source">

      <a href="https://github.com/QIICR/Slicer-PETDICOMExtension/blob/4feafda0a4a58132e50ad527726622a65ac061e5/SUVFactorCalculatorCLI/SUVFactorCalculator.cxx#L692-L697" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/QIICR/Slicer-PETDICOMExtension/blob/4feafda0a4a58132e50ad527726622a65ac061e5/SUVFactorCalculatorCLI/SUVFactorCalculator.cxx#L692-L697" target="_blank" rel="noopener">QIICR/Slicer-PETDICOMExtension/blob/4feafda0a4a58132e50ad527726622a65ac061e5/SUVFactorCalculatorCLI/SUVFactorCalculator.cxx#L692-L697</a></h4>



    <pre class="onebox">      <code class="lang-cxx">
        <ol class="start lines" start="692" style="counter-reset: li-counter 691 ;">
            <li>if ( (parsingDICOM) &amp;&amp;</li>
            <li>     (list.injectedDose != 0.0) &amp;&amp;</li>
            <li>     (list.patientWeight != 0.0) &amp;&amp;</li>
            <li>     (list.seriesReferenceTime.compare("MODULE_INIT_NO_VALUE") != 0) &amp;&amp;</li>
            <li>     (list.injectionTime.compare("MODULE_INIT_NO_VALUE") != 0) &amp;&amp;</li>
            <li>     (list.radionuclideHalfLife.compare("MODULE_INIT_NO_VALUE") != 0) )</li>
        </ol>
      </code>
    </pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
