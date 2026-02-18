# Python example that convert the multiple-label segmentation to binary-label segmentation

**Topic ID**: 31765
**Date**: 2023-09-18
**URL**: https://discourse.slicer.org/t/python-example-that-convert-the-multiple-label-segmentation-to-binary-label-segmentation/31765

---

## Post #1 by @Liang_Ma (2023-09-18 03:08 UTC)

<p>Hello all,<br>
I have a dataset from TCIA, which are multiple-label segmentation file (NOT nrrd but dcm file). the label map is something like this that I can read out by leveraging pydicom:</p>
<pre><code class="lang-auto">{'Segment_1': {'Label': 'Liver', 'Description': 'Anatomical Structure'}, 'Segment_2': {'Label': 'Liver Remnant', 'Description': 'Anatomical Structure'}, 'Segment_3': {'Label': 'Hepatic', 'Description': 'Tissue'}, 'Segment_4': {'Label': 'Portal', 'Description': 'Tissue'}, 'Segment_5': {'Label': 'Tumor_1', 'Description': 'Morphologically Altered Structure'}}
</code></pre>
<p>Now I would like to convert such a dcm file to a binary-segmentation file for use in one project–which means basically I need to combine all non-Tumor segmentation into one category as “non-Tumor”. I found it difficult to do that in pydicom as I can not extract the segmentation geometry information.<br>
I think slicer python lib could be used for that purpose instead, but searching around I couldn’t find a good reference code.</p>
<p>Can someone help to give suggestions here?</p>

---

## Post #2 by @Liang_Ma (2023-09-18 08:47 UTC)

<p>Thanks for chatGPT, I am able to do a similar thing as below:</p>
<pre><code class="lang-auto"># 3d slicer implementation:
def valid_node(verbose:bool = False):
    segmentationNodes = slicer.mrmlScene.GetNodesByClass('vtkMRMLSegmentationNode')
    segmentationNodes.InitTraversal()
    node = segmentationNodes.GetNextItemAsObject()

    if node.IsA('vtkMRMLSegmentationNode'):
        print(f"Found a vtkMRMLSegmentationNode: {node.GetName()}")
        segmentation = node.GetSegmentation()
        numberOfSegments = segmentation.GetNumberOfSegments()
        print(f"Number of Segments: {numberOfSegments}")
        
        # Loop over all segments
        if verbose:
            for i in range(numberOfSegments):
                segmentId = segmentation.GetNthSegmentID(i)
                segment = segmentation.GetSegment(segmentId)

                # Print basic segment details
                print(f"Segment ID: {segmentId}")
                print(f"Segment Name: {segment.GetName()}")
                #print(f"Segment Color: {segment.GetColor()}")  # This will give you the RGB color as a tuple
            
        #node = segmentationNodes.GetNextItemAsObject()
        return node
    
    else:
        print(f"Node is NOT a vtkMRMLSegmentationNode: {node.GetName()}")
        return None
</code></pre>
<p>However, there is one limitation that I have to do: 1). In 3D slicer import a segmentation data file to form a segmentationNode; 2). run this script in 3D slicer python console;</p>
<p>I have many segmentation files to proceed, which are located under different folders – it is not possible to import each data file and then execute this script.</p>
<p>To speak frankly, I do not fully understand the concept of the “segmentationNodes”.  so 1st question: can someone help to explain this “node” concept?</p>
<p>my 2nd question is:  Is that possible to setup a segmentationNodes by importing a particular segmentation data file, not in GUI but by using python code? I did not find such an example code yet.</p>

---

## Post #3 by @cpinter (2023-09-18 09:00 UTC)

<p>The segmentation node concept is explained here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" class="inline-onebox">Image Segmentation — 3D Slicer documentation</a></p>
<p>I couldn’t fully understand your goal. Do you want to merge all segments into one? Or do you want to have two segments: tumor and non-tumor?</p>
<p>Can you please make a screenshot of the subject hierarchy (where we can see all segments) and explain what you want to do in that segmentation node? Thanks.</p>

---

## Post #4 by @Liang_Ma (2023-09-18 09:15 UTC)

<p>Thanks. The different data samples might have different labels. But at least it has 5 labels (4 non-Tumor and at least one Tumor)<br>
here is the segment hierarchy, which shows 4 non-Tumor and 8 Tumor area.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7ec59569ff288775a08cd8f0432ed61f74ce395f.png" data-download-href="/uploads/short-url/i5ttTVykXLzYCMRDPiitIFJbsNV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7ec59569ff288775a08cd8f0432ed61f74ce395f_2_690x302.png" alt="image" data-base62-sha1="i5ttTVykXLzYCMRDPiitIFJbsNV" width="690" height="302" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7ec59569ff288775a08cd8f0432ed61f74ce395f_2_690x302.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7ec59569ff288775a08cd8f0432ed61f74ce395f_2_1035x453.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7ec59569ff288775a08cd8f0432ed61f74ce395f_2_1380x604.png 2x" data-dominant-color="7F747C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×841 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>my goal is to find a way that can isolate two areas: Tumor and non-Tumor.</p>

---

## Post #5 by @cpinter (2023-09-18 09:17 UTC)

<p>I see, thank you. Do the segments have terminology set (double-click on color to see if you’re unsure), or do you want to only use the segment names?</p>
<p>Is the goal to merge all the tumor and all the non-tumor segments, thus having two segments?</p>

---

## Post #6 by @Liang_Ma (2023-09-18 09:40 UTC)

<p>Yes, all segmentation has “terminology set” as the below chart shows: BTW, this “terminology set” is a new concept for me as well, kindly send me some reference document to read if yuou have…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/3027ffe0b4f802b98e4874fa3024563b208c0e4f.png" data-download-href="/uploads/short-url/6S0Cgni3IxDBESUvn2RaemiJ37p.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/3027ffe0b4f802b98e4874fa3024563b208c0e4f_2_690x347.png" alt="image" data-base62-sha1="6S0Cgni3IxDBESUvn2RaemiJ37p" width="690" height="347" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/3027ffe0b4f802b98e4874fa3024563b208c0e4f_2_690x347.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/3027ffe0b4f802b98e4874fa3024563b208c0e4f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/3027ffe0b4f802b98e4874fa3024563b208c0e4f.png 2x" data-dominant-color="E4E9EC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">765×385 43.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is the goal to merge all the tumor and all the non-tumor segments, thus having two segments?<br>
Yes, but actually may not be that straightforward, for example,  because the Liver generally includes Tumor segmentation (overlap may exist)–I suspect I may need to exclude the “Tumor” segmentation from the Liver segmentaion…</p>

---

## Post #7 by @cpinter (2023-09-18 09:46 UTC)

<p>Here is some information about terminologies (“set” was supposed to be a verb, sorry about the confusion): <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/terminologies.html" class="inline-onebox">Terminologies — 3D Slicer documentation</a><br>
(feel free to browser the documentation, as you can see it is useful, and finding certain information there is not hard)</p>
<p>Basically terminologies identify a segment’s content in a standard way, to avoid the need for deduce it from the segment name, and to minimize the possibility of human error.</p>
<p>You can get the terminology string from a segment like this:</p>
<pre><code class="lang-auto">terminologyStr = vtk.mutable('')
segment.GetTag(segment.GetTerminologyEntryTagName(), terminologyStr)
</code></pre>
<p>Then you can store the string for tumor, and do a comparison in your for loop for all the segments.</p>
<p>Merging the segments together into a single segment is probably best to use the Logical operator effect in Segment Editor.</p>

---

## Post #8 by @Liang_Ma (2023-09-18 10:56 UTC)

<p>Thanks, so the terminology is mostly some “standard string information” that can help to quickly identify what the segmentation belongs to? Here is one output by using this code, for one segmentation:</p>
<pre><code class="lang-auto">terminologyStr: Segmentation~SCT^49755003^Morphologically Altered Structure~SCT^4147007^Mass~^^~Segmentation~SCT^10200004^Liver~^^
</code></pre>
<p>I am still trying to probe the way to make the multi-segmentation a binary-segmentation. I think some voxel level overlapping check may be necessary.</p>
<p>BTW, do you have some advice on my original question: "Is that possible to setup a segmentationNodes by importing a particular segmentation data file, not in GUI but by using python code? "<br>
what Ima doing is purely manual way, each time only dealing with one file–that is not acceptable for massive data files.</p>

---

## Post #9 by @lassoan (2023-09-18 13:37 UTC)

<aside class="quote no-group" data-username="Liang_Ma" data-post="8" data-topic="31765">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/liang_ma/48/66068_2.png" class="avatar"> Liang_Ma:</div>
<blockquote>
<p>"Is that possible to setup a segmentationNodes by importing a particular segmentation data file, not in GUI but by using python code?</p>
</blockquote>
</aside>
<p>You can find examples for all the commonly needed operations in the Slicer script repository. For example, how to load a file as segmentation <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#load-a-3d-image-or-model-file-as-segmentation">from nrrd</a> and <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#load-dicom-files-into-the-scene-from-a-folder">from DICOM</a>.</p>

---

## Post #10 by @Liang_Ma (2023-09-19 08:30 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks. This example works well, but it only accepts a folder path-- and it will load all dcm files in case there are multiple dcm files under the folder – Is there any API that can import a single dcm file, I did not find it in the help document.</p>
<pre><code class="lang-auto">def load_DICOM(dicomFilesDirectory):
    # instantiate a new DICOM browser
    slicer.util.selectModule("DICOM")
    dicomBrowser = slicer.modules.DICOMWidget.browserWidget.dicomBrowser
    # use dicomBrowser.ImportDirectoryCopy to make a copy of the files (useful for importing data from removable storage)
    dicomBrowser.importDirectory(dicomFilesDirectory, dicomBrowser.ImportDirectoryAddLink)
    # wait for import to finish before proceeding (optional, if removed then import runs in the background)
    dicomBrowser.waitForImportFinished()
    print(f"DCM folder {dicomFilesDirectory} load done!")
</code></pre>
<p>One more comment is: actually I do not really need to open a GUI and import a dcm file, what I need to do is setup a “segmentation node” as all segmentation operations need to be done on such a node-- does that really need to import dcm files? Can’t simply create something like a context, then operate physical dcm files one-by-one?</p>

---

## Post #11 by @pieper (2023-09-19 20:44 UTC)

<p>Once you import the data you can use the database API to find the studies of interest.  Or you can sort the dicom data into distinct directories before importing, e.g. with <a href="https://github.com/pieper/dicomsort">this tool</a>.</p>

---
