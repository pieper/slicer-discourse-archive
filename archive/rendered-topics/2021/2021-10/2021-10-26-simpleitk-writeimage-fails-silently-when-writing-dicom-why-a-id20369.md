# SimpleITK WriteImage() fails *silently* when writing DICOM -- why? And what to do?

**Topic ID**: 20369
**Date**: 2021-10-26
**URL**: https://discourse.slicer.org/t/simpleitk-writeimage-fails-silently-when-writing-dicom-why-and-what-to-do/20369

---

## Post #1 by @masonbogue (2021-10-26 19:55 UTC)

<p>Here’s what’s happening (at the Slicer Python console):</p>
<pre><code class="lang-auto">import SimpleITK as sitk
sitk.WriteImage(slices[0], "C:\\Users\\username\\test\\0000.mhd") # works fine
sitk.WriteImage(slices[0], "C:\\Users\\username\\test\\0000.nrrd") # works fine
sitk.WriteImage(slices[0], "C:\\Users\\username\\test\\0000.dcm") # does nothing, gives no error message, just does nothing
# using sitk.ImageFileWriter().Execute() gives the same behavior, incidentally
</code></pre>
<p>Overall, this is a very frustrating situation, because I had written a script that outputs DICOM files using SimpleITK (I am converting some MHDs to DICOM for further processing), and since SimpleITK is a part of Slicer, I assumed that I could run it in Slicer. And if I am doing something <em>wrong</em>, then I feel that I at least deserve some kind of notice like: “ERROR: We disabled writing DICOM because [reason]!”.</p>
<p>The script works perfectly on my laptop with a standalone SimpleITK library, but on my work desktop I cannot install standalone SimpleITK (ugh) so I thought I would try to run it inside of Slicer, which I am allowed to install. Now I am afraid I will have to rewrite the script in order to use Slicer’s internal DICOM modules, which will require a few days of reading, probably. And all because of this one function!</p>
<p>I am curious to know:</p>
<ul>
<li>
<p>Has anyone else used SimpleITK ImageFileWriter/WriteImage to write DICOM files from Slicer scripts? Is there a way to fix the problem?</p>
</li>
<li>
<p>Is there a good way to export a SimpleITK image object as DICOM from Slicer? Or more generally to convert an .mhd/.raw file pair to a DICOM series (I have the tags stored separately)?</p>
</li>
<li>
<p>Can someone please consider adding an error message to be printed when <code>SimpleITK.WriteImage()</code> fails?</p>
</li>
</ul>
<p>The only script example for exporting an image as DICOM is this, which starts with object types I don’t recognize and uses a bunch of functionality I was hoping to avoid:</p>
<pre><code class="lang-auto">volumeNode = getNode("CTChest")
outputFolder = "c:/tmp/dicom-output"

# Create patient and study and put the volume under the study
shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
patientItemID = shNode.CreateSubjectItem(shNode.GetSceneItemID(), "test patient")
studyItemID = shNode.CreateStudyItem(patientItemID, "test study")
volumeShItemID = shNode.GetItemByDataNode(volumeNode)
shNode.SetItemParent(volumeShItemID, studyItemID)

import DICOMScalarVolumePlugin
exporter = DICOMScalarVolumePlugin.DICOMScalarVolumePluginClass()
exportables = exporter.examineForExport(volumeShItemID)
for exp in exportables:
  exp.directory = outputFolder

exporter.export(exportables)
</code></pre>

---

## Post #2 by @lassoan (2021-10-26 20:17 UTC)

<aside class="quote no-group" data-username="masonbogue" data-post="1" data-topic="20369">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/c77e96/48.png" class="avatar"> masonbogue:</div>
<blockquote>
<p>Overall, this is a very frustrating situation, because I had written a script that outputs DICOM files using SimpleITK (I am converting some MHDs to DICOM for further processing), and since SimpleITK is a part of Slicer, I assumed that I could run it in Slicer. And if I am doing something <em>wrong</em> , then I feel that I at least deserve some kind of notice like: “ERROR: We disabled writing DICOM because [reason]!”.</p>
</blockquote>
</aside>
<p>Creation of valid DICOM files is very complex and not done very often. You need to provide lots of required metadata to have a chance of generating a valid DICOM file. You need to generate new UIDs for some fields, while cross-referencing existing UIDs in other fields.</p>
<p>Not creating a file at all is a robust way of indicating that something went wrong and SimpleITK may also log errors or set error codes somewhere. But I agree that it would be better if you got a more clear indication of error, such as returning an error code or throw an exception. I would recommend to start a discussion about this on the <a href="https://discourse.itk.org/">ITK forum</a>.</p>
<aside class="quote no-group" data-username="masonbogue" data-post="1" data-topic="20369">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/c77e96/48.png" class="avatar"> masonbogue:</div>
<blockquote>
<p>Now I am afraid I will have to rewrite the script in order to use Slicer’s internal DICOM modules, which will require a few days of reading, probably. And all because of this one function!</p>
</blockquote>
</aside>
<p>Creating DICOM files is very hard. If you can figure out a solution in a few days then you are very lucky.</p>
<aside class="quote no-group" data-username="masonbogue" data-post="1" data-topic="20369">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/c77e96/48.png" class="avatar"> masonbogue:</div>
<blockquote>
<p>Has anyone else used SimpleITK ImageFileWriter/WriteImage to write DICOM files from Slicer scripts? Is there a way to fix the problem?</p>
</blockquote>
</aside>
<p>There should be no difference in how SimpleITK works in Slicer or elsewhere, but if you find that something behaves differently in Slicer then let us know.</p>
<aside class="quote no-group" data-username="masonbogue" data-post="1" data-topic="20369">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/c77e96/48.png" class="avatar"> masonbogue:</div>
<blockquote>
<p>Is there a good way to export a SimpleITK image object as DICOM from Slicer? Or more generally to convert an .mhd/.raw file pair to a DICOM series (I have the tags stored separately)?</p>
</blockquote>
</aside>
<p>An mhd/raw file does not contain enough data that would allow creation of a valid DICOM file.</p>
<p>If you load the DICOM file into Slicer then it stores essential metadata that is used automatically when you export the file, so the process should be fairly straightforward. Note that an mhd image can be stored in DICOM in different ways, for example it can be a CT/MR/PT/US/XA/… image IOD, Segmentation Object IOD, or RT Structure Set IOD.</p>
<p>SimpleITK requires you to provide required metadata in a metadata dictionary in the reader. I’m sure there are many examples on the web.</p>
<aside class="quote no-group" data-username="masonbogue" data-post="1" data-topic="20369">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/c77e96/48.png" class="avatar"> masonbogue:</div>
<blockquote>
<p>Can someone please consider adding an error message to be printed when <code>SimpleITK.WriteImage()</code> fails?</p>
</blockquote>
</aside>
<p>See above, contact SimpleITK developers.</p>
<aside class="quote no-group" data-username="masonbogue" data-post="1" data-topic="20369">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/c77e96/48.png" class="avatar"> masonbogue:</div>
<blockquote>
<p>The only script example for exporting an image as DICOM is this, which starts with object types I don’t recognize and uses a bunch of functionality I was hoping to avoid</p>
</blockquote>
</aside>
<p>The code snippet above is fairly simple, considering the underlying complexity of the operation. Creation of patient/study/etc. is not needed if you start from a DICOM study, so it really just takes 6-8 lines of code.</p>

---

## Post #3 by @masonbogue (2021-10-26 20:26 UTC)

<p>The script works – it has worked, dozens of times, running locally. I have successfully created a DICOM series, from an MHD, using SimpleITK, with the script.</p>
<p>And yes, you’re right: if you don’t set the metadata, SimpleITK complains. Locally. On Slicer it doesn’t. And if you follow the complaints it gives – locally – it will, eventually, work, and generate a DICOM file. It wasn’t <em>that</em> hard – I’ve done it!</p>
<p>So I don’t understand why it’s necessary to be so condescending?</p>
<aside class="quote no-group">
<blockquote>
<p>SimpleITK requires you to provide required metadata in a metadata dictionary in the reader. I’m sure there are many examples on the web.</p>
</blockquote>
</aside>
<p>Like, seriously, why? You think I didn’t spend several hours searching the Internet before posting this thread? All to be made fun of by someone who thinks I don’t know what DICOM is?</p>
<p>So: I’m sorry. I suppose the complaint about the error message was too loud. I’ll just leave now, and remember not to ask for help.</p>

---

## Post #4 by @lassoan (2021-10-26 21:18 UTC)

<p>I’m sorry I didn’t want to offend you. If you can point out specific comments from my post above that you did not find appropriate then let me know, I would like to learn what to avoid in the future.</p>
<p>From the additional information that you provided it seems that the problem is that some SimpleITK outputs (maybe those that are printed on the stdout/stderr) do not show up in Slicer’s Python console. I’ll have a look if I can reproduce this behavior.</p>

---

## Post #5 by @lassoan (2021-10-26 21:31 UTC)

<p>The behavior using SimpleITK in latest Slicer Stable Release and in a recent Slicer Preview Release on Windows look good:</p>
<pre><code class="lang-python">&gt;&gt;&gt; import SampleData
&gt;&gt;&gt; import SimpleITK as sitk
&gt;&gt;&gt; import sitkUtils
&gt;&gt;&gt; inputVolumeNode = SampleData.SampleDataLogic().downloadMRHead()
&gt;&gt;&gt; slices = sitkUtils.PullVolumeFromSlicer(inputVolumeNode)
&gt;&gt;&gt; import SimpleITK as sitk
&gt;&gt;&gt; sitk.WriteImage(slices[0], "C:\\tmp\\0000.mhd") # works fine
&gt;&gt;&gt; sitk.WriteImage(slices[0], "C:\\tmp\\0000.nrrd") # works fine
&gt;&gt;&gt; sitk.WriteImage(slices[0], "C:\\tmp\\0000.dcm") # works fine
&gt;&gt;&gt; sitk.WriteImage(slices[0], "C:\\nonexisting\\0000.dcm") # throws error as expected
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "C:\Users\andra\AppData\Local\NA-MIC\Slicer 4.13.0-2021-10-18\lib\Python\lib\site-packages\simpleitk-2.1.1-py3.6-win-amd64.egg\SimpleITK\extra.py", line 394, in WriteImage
    return writer.Execute(image)
  File "C:\Users\andra\AppData\Local\NA-MIC\Slicer 4.13.0-2021-10-18\lib\Python\lib\site-packages\simpleitk-2.1.1-py3.6-win-amd64.egg\SimpleITK\SimpleITK.py", line 7503, in Execute
    return _SimpleITK.ImageFileWriter_Execute(self, *args)
RuntimeError: Exception thrown in SimpleITK ImageFileWriter_Execute: D:\D\P\Slicer-0-build\ITK\Modules\IO\ImageBase\src\itkImageIOBase.cxx:698:
ITK ERROR: GDCMImageIO(000001FA949D5470): Could not open file: C:\nonexisting\0000.dcm for writing.
Reason: No such file or directory
&gt;&gt;&gt; 
&gt;&gt;&gt; 
</code></pre>
<p>If you can provide steps that reproduce the silent DICOM writing failure then I can investigate further. I can imagine that some low-level component, such as GDCM does not propagate error/warning messages to higher levels just logs to the console, which may show up in the Slicer application log, but may not printed to the Python console.</p>

---

## Post #6 by @jamesobutler (2021-10-26 21:46 UTC)

<aside class="quote no-group" data-username="masonbogue" data-post="1" data-topic="20369">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/c77e96/48.png" class="avatar"> masonbogue:</div>
<blockquote>
<p>The script works perfectly on my laptop with a standalone SimpleITK library</p>
</blockquote>
</aside>
<p>Hi <a class="mention" href="/u/masonbogue">@masonbogue</a>, can you provide information about what version of SimpleITK you were using when it was working for you on your laptop? Slicer builds SimpleITK from source so the version in Slicer may be different from the version that you were using if you had installed into a system python on your machine. This appears to be the biggest variable between when it was working for you and now when it is not working for you. Also please provide us with information about which version of Slicer you were using.</p>

---

## Post #7 by @masonbogue (2021-10-26 23:47 UTC)

<p>Hi,</p>
<p>After spending some more time working with this code, I can understand why you might have adopted a somewhat more whimsical tone than I was expecting. Being told over and over “writing DICOM files is very hard” sounded… I don’t know… like you thought I wasn’t trying. I was too short-tempered myself.</p>
<p>It turns out that the example needs very little modification. The current script is now short enough to post – the old one had <em>dozens</em> of lines setting various DICOM attributes – and it looks like this:</p>
<pre data-code-wrap="python"><code class="lang-python">
import os
import DICOMScalarVolumePlugin
import slicer, slicer.util

def convert_file(infile, outdir):
      fileName = os.path.basename(infile).split(".")[0]
      ptName = fileName[0:7]


      if not slicer.util.loadVolume(infile):
            print("ERROR: Cannot load MHD " + infile)
      volumeNode = slicer.util.getNode(fileName)

      # Create patient and study and put the volume under the study
      shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
      patientItemID = shNode.CreateSubjectItem(shNode.GetSceneItemID(), ptName)
      studyItemID = shNode.CreateStudyItem(patientItemID, fileName)
      volumeShItemID = shNode.GetItemByDataNode(volumeNode)
      shNode.SetItemParent(volumeShItemID, studyItemID)
      shNode.SetItemAttribute(studyItemID, "DICOM.Modality", "CT")   # *this* didn't work
      shNode.SetItemAttribute(studyItemID, "DICOM.RescaleType", "HU") # neither did *this*

      import DICOMScalarVolumePlugin
      exporter = DICOMScalarVolumePlugin.DICOMScalarVolumePluginClass()
      exportables = exporter.examineForExport(volumeShItemID)
      for exp in exportables:
            exp.directory = outdir

      exporter.export(exportables)

</code></pre>
<p>So, now I can produce DICOM files! I was surprised at first by all of the long variable names, but in order to do simple things I don’t need to figure them all out.</p>
<p>Unfortunately, I seem to have reproduced this bug (cf. the commented lines above):</p>
<aside class="quote" data-post="1" data-topic="3399">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f07891/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/rescale-type-attribute-when-creating-dicom-series/3399">Rescale type attribute when creating DICOM series</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello, 
I’m using Slicer to create a downsampled CT series, and I was able to do that just fine, except that it appears the “Rescale type” attribute was changed from HU to US. Due to that I cannot export the images anymore in the other program I’m using (Treatment Planning Station). 
Is there any way to keep this attribute unchanged, or to revert it back to its original value ? 
Thanks ! 
Antoine
  </blockquote>
</aside>

<p>I know this is probably frustrating for Andreas, because he had put in a fix (thank you!) for it at lines 176-9 of this file:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Modules/CLI/CreateDICOMSeries/CreateDICOMSeries.cxx">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Modules/CLI/CreateDICOMSeries/CreateDICOMSeries.cxx" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Modules/CLI/CreateDICOMSeries/CreateDICOMSeries.cxx" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/main/Modules/CLI/CreateDICOMSeries/CreateDICOMSeries.cxx</a></h4>


      <pre><code class="lang-cxx">/*=========================================================================

This plugin is based on the Insight Toolkit example
ImageReadDicomWrite. It has been modified for GenerateCLP style
command line processing and additional features have been added.

=========================================================================*/
#if defined(_MSC_VER)
#pragma warning ( disable : 4786 )
#endif

#include &lt;ctime&gt;

#include "itkImageFileReader.h"
#include "itkImageFileWriter.h"
#include "itkExtractImageFilter.h"
#include "itkShiftScaleImageFilter.h"
#include "itkGDCMImageIO.h"
#include "itkMetaDataObject.h"

</code></pre>



  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/main/Modules/CLI/CreateDICOMSeries/CreateDICOMSeries.cxx" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Unfortunately, the fix doesn’t seem to apply for me, because when I try to import the file into the TPS, it complains about an invalid rescaleType, which is probably being set to “US” by GDCM.</p>
<p>So I think my new question is: <strong>in what Slicer version is this fix found?</strong> I am on Slicer 4.10.2. I may be able to convince IT to upgrade us. Is there any other way to set the rescaleType when exporting an image as DICOM? (Previously I did this by <code>image_slice.SetMetaData("0028|1054", "HU")</code> with a SimpleITK object)</p>
<p>Thanks for your help,<br>
Mason</p>

---

## Post #8 by @jamesobutler (2021-10-27 01:19 UTC)

<aside class="quote no-group" data-username="masonbogue" data-post="7" data-topic="20369">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/c77e96/48.png" class="avatar"> masonbogue:</div>
<blockquote>
<p>So I think my new question is: <strong>in what Slicer version is this fix found?</strong> I am on Slicer 4.10.2.</p>
</blockquote>
</aside>
<p>When you go to the commit <a href="https://github.com/Slicer/Slicer/commit/cf00276be8a53dc46e033a17fd21e4e974981389" class="inline-onebox" rel="noopener nofollow ugc">ENH: Improve CreateDICOMSeries module · Slicer/Slicer@cf00276 · GitHub</a> on GitHub, at the bottom (see image below) it will show you which tag/version it was first included in. So it was first included in Slicer stable release 4.11.20210226 which is the current Slicer stable that you can download from <a href="https://download.slicer.org/" rel="noopener nofollow ugc">https://download.slicer.org/</a>.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae6b14b6e4a0d9f1584b55332ac4e0e5244c8845.png" alt="image" data-base62-sha1="oSYuYHrHPpBS8qPMpJJVIQucCBT" width="540" height="487"></p>
<p>I would highly suggest you move away from Slicer 4.10 even outside of this bug because there have been lots of improvements to Slicer since Fall 2018 when it was originally released. Slicer 4.10 is using Python 2 for one thing which has gone End-Of-Life since Jan 1st, 2020. SimpleITK 1.1 was being used in Slicer 4.10 and a new version can’t be installed because latest SimpleITK has dropped Python 2 support. Latest Slicer Preview uses SimpleITK 2.1.1 which is the latest stable release.</p>
<p>I will also note that Slicer 4.10 issues are not investigated by developers and here on the forum you’re going to be encouraged to use latest Slicer Stable or latest Slicer Preview. There is usually limited resources so generally there is only time available to improve the current versions which will help more people in the community rather than trying to debug issues in old outdated versions. Always here to help when using latest software!</p>

---

## Post #9 by @lassoan (2021-10-27 01:36 UTC)

<p>I’ve tried to run my short test script above in Slicer-4.10.2 and the last line failed silently. The same line failed with a loud error exception and printed a meaningful error message on latest Slicer Stable Release and recent Slicer Preview Release. Probably error handling of the DICOM writer was implemented in SimpleITK after Slicer-4.10.2 was released. So, the missing error report issue will be fixed if you update Slicer.</p>
<p>The current Slicer Stable Release does not need an administrator account to install: you can run the installer as a normal user and Slicer is set up in your user’s folder by default. Some hospitals manage to prevent running even user-mode installers, in that case you can install Slicer on any computer and copy all the files to a USB stick and run it from there (or you can copy the files to your computer and run from there), because Slicer is also fully portable now. If even USB drive access is disabled, then you probably need to ask an IT admin to install Slicer for you.</p>

---

## Post #10 by @zahra_mrtz (2024-05-11 07:51 UTC)

<p>Hello masonbogue<br>
I’m so glad to see your question especially I find out your script works at the end. Actually I’m working in image processing and I need to convert a mhd image to dicom. I worked with this script but didn’t work for me.<br>
(script link: <a href="https://simpleitk.readthedocs.io/en/master/link_DicomSeriesFromArray_docs.html" class="inline-onebox" rel="noopener nofollow ugc">Dicom Series From Array — SimpleITK 2.0rc2 documentation</a>)<br>
Is it possible share your script that work fine (with copy right law of course)?<br>
I would be appreciated so much for your help.</p>

---
