---
topic_id: 23061
title: "Loading Terminology File When Editing A Segmentation"
date: 2022-04-20
url: https://discourse.slicer.org/t/23061
---

# Loading terminology file when editing a segmentation

**Topic ID**: 23061
**Date**: 2022-04-20
**URL**: https://discourse.slicer.org/t/loading-terminology-file-when-editing-a-segmentation/23061

---

## Post #1 by @DeepaKrishnaswamy (2022-04-20 21:01 UTC)

<p>Hi,</p>
<p>I am working on a module that uses a terminology file to define regions/colors. When I first add a segment to a node, the terminology file I’ve specified is automatically chosen.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e8cb6c1dc9618c0aec401dae6dc2b7ef55b1e30.png" alt="image" data-base62-sha1="kl3hidWsOVP1yhA8gDoQRoleQhy" width="557" height="408"></p>
<p>I then draw a segment and save the file. When I load the file back in, and go to add an another segment, the terminology file is not longer the one that was automatically set. Instead, it defaults to the name of the segmentation node, and I have to select the terminology file from the dropdown menu.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/0493dde77e52339800a87ca6d3cf354642916aa4.png" alt="Screenshot 2022-04-20 165636" data-base62-sha1="EuId2fGWXTv8i5bfaf1EWlPbLu" width="554" height="407"></p>
<p>Is there a way for the terminology file I want to be automatically chosen with the additional segment? I did see that once I select the file I want, any additional segment I add automatically uses that file.</p>
<p>Thanks!</p>

---

## Post #2 by @cpinter (2022-04-22 11:52 UTC)

<p>This is a use case that is not perfectly handled as it is in the latest Slicer. I had to do the same (if I understand your problem correctly), and decided to do this workaround, as I didn’t have time starting to fix the terminology feature (which is quite complex so I expect it a relatively large work if we need to consider and test every use case):</p>
<pre><code class="lang-auto">  #------------------------------------------------------------------------------
  @vtk.calldata_type(vtk.VTK_STRING)
  def onSegmentAdded(self, caller, eventId, callData=None):
    """
    Called when a segment is added.
    Set custom terminology context to new segment

    :param VTKObject caller: The VTKObject which initiated the callback (the segmentation node)
    :param int eventId: ID of the event which was called.
      Note: The event argument seems to be always 'NoEvent' regardless which event is observed
    :param int callData: Event data passed along with the callback, containing the segment ID
    :return void:
    """
    del eventId  # to eliminate PyLint complaint about an unused argument
    segmentationNode = caller
    segmentID = callData

    segment = segmentationNode.GetSegmentation().GetSegment(segmentID)
    segment.SetTag(slicer.vtkSegment.GetTerminologyEntryTagName(),
      'Custom segmentation category and type~Custom^95759010^Segmentation~^^~^^~Anatomic codes - DICOM master list~^^~^^')  # This you'll need to edit to match the metadata of your terminology
</code></pre>
<p>And of course you have to set up observation:</p>
<pre><code class="lang-auto">      # Observe segment added event so that the terminology context can be set instead of the default
      self.segmentationNodeObserverTags.append(segmentationNode.AddObserver(
        slicer.vtkSegmentation.SegmentAdded, self.moduleWidget.onSegmentAdded))
</code></pre>

---

## Post #3 by @DeepaKrishnaswamy (2022-05-06 20:31 UTC)

<p>I actually realized that the issue is when I load a file that contains a segment, and not with adding an additional segment. Now when I load the file, for each existing segment I assign the terminology entry I want. When I go to add a new segment, the terminology entry I want is automatically selected.</p>
<p>Thank you for your help!</p>

---
