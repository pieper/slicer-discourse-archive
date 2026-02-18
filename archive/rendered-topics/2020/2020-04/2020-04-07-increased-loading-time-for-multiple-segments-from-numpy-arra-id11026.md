# Increased loading time for multiple segments from numpy array

**Topic ID**: 11026
**Date**: 2020-04-07
**URL**: https://discourse.slicer.org/t/increased-loading-time-for-multiple-segments-from-numpy-array/11026

---

## Post #1 by @EricM (2020-04-07 08:09 UTC)

<p>Hello Slicer community,</p>
<p>I have a performance problem, and I would like to reach out to you to see if there is something simple I can do to speed up the process.</p>
<p>I have developped an annotation module in Slicer that works bug-free. Annotators segment lesions on CT images (512x512x198) and answer questions about the segments. I have created a personalized “save” feature that saves the non-overlapping segments into a single numpy array (encoded by the integer of the Segment number) and the questions and answers as a json all in a hdf5 file. Annotators open unfinished cases by selecting them in a QComboBox, which sets off a <code>currentIndexChanged</code> event connected to my load function <code>onLoadHDF5</code>. The function reads the hdf5, gets the segments from the numpy array, loads each one into a vtkMRMLLabelMapVolumeNode and then imports the labelmap into the segmentation node.</p>
<p>Below is a shortened version of the code I am using for this</p>
<pre><code class="lang-auto">def onLoadHDF5(self,hdf5_filename):

    #Read hdf5 into memory
    with h5py.File(self.local_hdf5_filename,"r") as gtFile:
      gt_dicts = gtFile['dicts'][::]
      gt_voxels = gtFile['voxels']
      lesionOverlapArray = gt_voxels['SegmentationOverlap'][::]

    #extract ground truth dictionaries
    lsnDict = loads(gt_dicts[1])

    #Fill in Number of Segments in List
    for segmentName,segmentDict in lsnDict.items(): #segmentName = 'Lesion 1', #segmentDict is a dictionary containing questions and answers about the lesion
      segmentIDNo = segmentName.split(' ')[1]
      
      labelMapVolumeNode = slicer.vtkMRMLLabelMapVolumeNode()
      labelMapVolumeNode.CopyOrientation(self.volumeNode) #self.volumeNode is the reference CT image(512x512x198)
      segmentArray = (lesionOverlapArray == int(segmentIDNo)).astype(int)
      
      slicer.util.updateVolumeFromArray(labelMapVolumeNode,segmentArray)
      slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(labelMapVolumeNode,self.segmentationNode)

      #Code to load Segment Questions
</code></pre>
<p>Currently, I have a very complicated case with over 250 segments on one image, and it takes a very long time to load the segments into Slicer with the method I am using above (saving is similar too).</p>
<p>I recently timed the time it took to go through each loop in the for loop to load the segment into slicer. What I wasn’t expecting was that the time increased for each loop even though the code is the same. For example, the first loop took 0.91s, and by the last loop, it took 5.58s! This resulted in about 14 minutes of loading time for this particular case.</p>
<p>My questions are</p>
<ul>
<li>
<p>Why does the time increase per loop? Is it a memory problem?</p>
</li>
<li>
<p>Since this is a function connected to an event, I can’t do anything else within Slicer, and the segments don’t load until the very end (and not one by one with each loop). Could this also induce memory problems (maybe the program stores everything into memory until the function finishes executing instead of “dumping” the segments into the segmentation node one by one)?</p>
</li>
</ul>
<p>Thank you for any insights for this problem, and thanks for an amazing software!</p>

---

## Post #2 by @lassoan (2020-04-07 16:17 UTC)

<p>Incremental slowdown in software is most commonly caused  by memory leaks. Is memory usage of your application increasing in each iteration?</p>

---

## Post #3 by @EricM (2020-04-08 08:40 UTC)

<p>Hi Andras,<br>
Thanks for your answer. I’m not sure how to investigate memory leaks. After a quick Google search, I opened the program “resmon” in Windows 10 (<a href="https://www.groovypost.com/howto/monitor-pc-memory-performance-usage/" rel="noopener nofollow ugc">link here</a>). The orange curve should be the contribution of Slicer.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce464f93f39e6661df492cf891eb89494b842efd.png" data-download-href="/uploads/short-url/tqMZWZjElAjk3cOFq286ohFYU2h.png?dl=1" title="resource-monitor" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce464f93f39e6661df492cf891eb89494b842efd_2_568x500.png" alt="resource-monitor" data-base62-sha1="tqMZWZjElAjk3cOFq286ohFYU2h" width="568" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce464f93f39e6661df492cf891eb89494b842efd_2_568x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce464f93f39e6661df492cf891eb89494b842efd_2_852x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce464f93f39e6661df492cf891eb89494b842efd.png 2x" data-dominant-color="CDD1CB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">resource-monitor</span><span class="informations">1043×918 163 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Throughout the loading process, it stayed around 8-12% CPU Usage and 57% Maximum Frequency (don’t know what that means), and 23% Used Physical Memory. However, I have no idea if this is how I’m supposed to inspect memory leaks. In fact, it just looks like Slicer is using almost all of my 12 CPUs (apparently 10% of each), but I don’t see any orange curve in the Memory section…</p>
<p>Thanks again for any insights,<br>
Eric</p>

---

## Post #4 by @lassoan (2020-04-08 21:02 UTC)

<p>Memory usage is shown on the “Memory” tab. If numbers for SlicerApp-real.exe are constantly increasing then probably you are leaking memory (you don’t release unused memory).</p>

---

## Post #6 by @EricM (2020-04-09 08:18 UTC)

<p>Apologies. Perhaps I wasn’t clear. The above screenshot of my computer activity was taken while I was loading the complicated case into Slicer (a couple minute in, actually). I did not see the blue curve in the Memory section increase, and I didn’t see any orange curves (Slicer) in the Memory section. Moreover, the percent of used physical memory always stayed around 24%. The only changes I saw while loading the case into Slicer was an increase in the CPU usage. In the CPU part, the orange curve appears, indicating - I guess - that Slicer is using my CPUs to load the data, but the percent CPU usage stayed low around 10%. I validated this in the “Memory” tab too. The screenshot below was during loading as well.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2dff0dc82efef45e435fd2cdccf9a9a24ef38511.png" data-download-href="/uploads/short-url/6yTW3Syzy85cgtUQeDrFMQLSRwZ.png?dl=1" title="resource-monitor_memory" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2dff0dc82efef45e435fd2cdccf9a9a24ef38511_2_690x495.png" alt="resource-monitor_memory" data-base62-sha1="6yTW3Syzy85cgtUQeDrFMQLSRwZ" width="690" height="495" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2dff0dc82efef45e435fd2cdccf9a9a24ef38511_2_690x495.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2dff0dc82efef45e435fd2cdccf9a9a24ef38511.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2dff0dc82efef45e435fd2cdccf9a9a24ef38511.png 2x" data-dominant-color="C2CDCD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">resource-monitor_memory</span><span class="informations">956×687 145 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Moreover, you can see that I still have a lot of free memory left. I have a total of 64G, so it should be plenty despite the large number of segmentations, but please correct me if I am wrong.</p>
<p>Does this mean that memory is not an issue?</p>
<p>Otherwise, is there a way to rewrite my function or connect the QComboBox such that, as each vtkMRMLLabelMapVolumeNode is pushed to the SegmentationNode in my for loop, I can “release the unused memory” and make the Segment appear in Slicer in real time (and not wait for the entire for loop to finish)? This might be a general Qt question than something specific to Slicer.</p>
<p>Thanks again for any suggestions.</p>

---

## Post #7 by @lassoan (2020-04-09 18:46 UTC)

<p>Thanks for all the information. Based on what you described, it does not seem to be a memory problem after all.</p>
<p>We have greatly improved performance of dealing with many segments in Slicer-4.11. So, if you are still using Slicer-4.10 then upgrade to latest Slicer Preview Release now.</p>
<p>Are your segments overlapping or you have a single 3D voxel array? If you have a single 3D array then you can import all the segments at once (using ImportLabelmapToSegmentationNode), and then update segment names of the already imported segments. This bulk import should be much faster than adding segments one by one.</p>

---

## Post #8 by @EricM (2020-07-02 15:37 UTC)

<p>Hi Andras,</p>
<p>Thanks for the tip! I didn’t realize I could upload a 3D array and have Slicer import the different labels as the different segments. It’s so simple - and yes, this worked like a charm.</p>
<p>Eric</p>

---
