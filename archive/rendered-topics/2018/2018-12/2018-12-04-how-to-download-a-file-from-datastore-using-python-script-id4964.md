---
topic_id: 4964
title: "How To Download A File From Datastore Using Python Script"
date: 2018-12-04
url: https://discourse.slicer.org/t/4964
---

# How to download a file from datastore using python script?

**Topic ID**: 4964
**Date**: 2018-12-04
**URL**: https://discourse.slicer.org/t/how-to-download-a-file-from-datastore-using-python-script/4964

---

## Post #1 by @brhoom (2018-12-04 22:21 UTC)

<p>Hi,</p>
<p>I am trying to add testing part to my module using public images from <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DataStore" rel="nofollow noopener">datastore</a>. How can I download the image with python script?</p>
<p>Thanks!</p>

---

## Post #2 by @jamesobutler (2018-12-04 23:52 UTC)

<p>I’m not familiar with the DataStore module, but there are several Slicer modules that use data from the SampleData module for testing purposes. See <a href="https://github.com/Slicer/Slicer/blob/2e5dcf178d0d26d359a10437aa16223e3a594e2f/Modules/Scripted/SegmentStatistics/SegmentStatistics.py#L653-L654" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/2e5dcf178d0d26d359a10437aa16223e3a594e2f/Modules/Scripted/SegmentStatistics/SegmentStatistics.py#L653-L654</a> for an example.</p>

---

## Post #3 by @lassoan (2018-12-05 04:49 UTC)

<p>You can download sample data sets from any URL (MIDAS, GitHub, etc.) using SampleData module:</p>
<pre><code class="lang-auto">import SampleData
loadedNodes = SampleData.SampleDataLogic().downloadFromSource(SampleData.SampleDataSource(
    nodeNames='fixed', 
    fileNames='fixed.nrrd', 
    uris='http://slicer.kitware.com/midas3/download/item/157188/small-mr-eye-fixed.nrrd'))
</code></pre>

---

## Post #4 by @brhoom (2018-12-05 08:16 UTC)

<p>Thanks all for the provided information. I used a workaround which works for me as I want the sample to be downloaded in a specific location.</p>
<p>I have only a problem with midas link as the file is created before it is downloaded completely which makes loadVolume fail. For now I am using a different server.</p>
<pre><code>try:         
    print("Downloading cochlea sample image ...")
    import urllib
    imgLaWebLink = "https://mtixnat.uni-koblenz.de/owncloud/index.php/s/eMvm9LHNHEHoZg3/download"
    #imgLaWebLink = "http://slicer.kitware.com/midas3/download/item/381221/P100001_DV_L_a"
    urllib.urlretrieve (imgLaWebLink , self.outputPath+"/imgA.nrrd" )
except Exception as e:
              print("Error: can not download sample file  ...")
              print(e)   
              return -1
#end try-except 
[success, inputVolumeNode] = slicer.util.loadVolume( self.outputPath+"/imgA.nrrd", returnNode=True)</code></pre>

---

## Post #5 by @lassoan (2018-12-06 02:26 UTC)

<p>SampleData uses urllib under the hood but has a number of additional features that might be relevant for some use cases. For example downloaded data sets are cached (this is probably the most significant, as downloading a large data set may take tens of seconds), failed, partial, and corrupted downloads are automatically reset/restarted, nodes can be loaded from of zip files (zip files are automatically unpacked), callback can be set for progress reporting, the same data source can be registered with SampleData module to appear in the module’s GUI.</p>

---
