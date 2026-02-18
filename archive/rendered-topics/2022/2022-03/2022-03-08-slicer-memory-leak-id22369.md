# Slicer Memory Leak

**Topic ID**: 22369
**Date**: 2022-03-08
**URL**: https://discourse.slicer.org/t/slicer-memory-leak/22369

---

## Post #1 by @Fabyan (2022-03-08 15:02 UTC)

<p>Hello. I am working on a slicer module that loads .mha data, applies transformations from a .csv to each frame and displays the separate orientations. Currently I load the data and preprocess it by splitting the different orientations into separate .mha files for each frame and then saving them to an output file using SimpleITK. I then load them in and add them to the Slice Widget. I have a play button and a slider to scroll through the “time” if you will. My problem is while developing, I need to reload my module and in doing so I will need to reload my data. This seems to be causing memory leaks as the memory 3d Slicer is taking keeps increasing by around 1gb each time. I tried deleting the nodes and they are not there in the Data tab but still taking up memory. I was wondering if there was a way to just clear the loaded volumes, or better yet, a smarter way to display separate orientations while applying a transformation to them?</p>

---

## Post #2 by @pieper (2022-03-08 18:29 UTC)

<p>You need to be sure to release all references to data to be sure it is freed.  That means clearing it from the scene but also making sure there are no python variables still referencing the data.  Slicer itself should be good about freeing data when it’s deleted but if you can develop a sample script that indicates a memory leak in the core please let us know.</p>
<p>For developing script modules typically try to avoid freeing and reloading data if it’s big.  I do something like this in my experimental scripts:</p>
<pre><code class="lang-auto">    try:
        node = slicer.util.getNode(name)
    except slicer.util.MRMLNodeNotFoundException:
        node = loader(path)
        node.SetName(name)
    return node
</code></pre>

---

## Post #3 by @Fabyan (2022-03-08 18:41 UTC)

<p>Hi, I tried slicer.mrmlScene.RemoveNode() to clear the nodes. Slicer seems to remove them as they are gone in the Data Module, but the memory does not get freed. I am not sure if slicer is removing the allocated memory for loaded volumes? . As for avoiding freeing and reloading data I will try the given structure of code thanks</p>

---

## Post #4 by @StephenLeePeng (2023-09-28 10:02 UTC)

<p>Have you resolved this issue?<br>
I am facing the same problem recently.<br>
And I wrote a topic,</p><aside class="quote quote-modified" data-post="1" data-topic="31936">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stephenleepeng/48/11892_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/strange-memory-leak-related-with-volumenode-and-segmentationnode/31936">Strange Memory leak related with volumeNode and segmentationNode</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Environment: Slicer 4.13, Linux Ubuntu 20.04. 
Background: 
Recently, I worked with a project, need to load some nii.gz file, vtp file. 
nii.gz file is loaded as vtkMRMLScalarVolumeNode, as the vtp file is loaded by Model, then transform to vtkSegmentationNode. 
nii.gz file was generated from a series dcm files by simpleITK, which shape is: 512x512x700, about 350MB. 
vtp files was segmented from volume, every vtp file is small part of volume. 
Firstly, Iily, I load vtp file as segmentationNode, …
  </blockquote>
</aside>


---
