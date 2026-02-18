# How to get segment details for a specific frame

**Topic ID**: 40009
**Date**: 2024-11-04
**URL**: https://discourse.slicer.org/t/how-to-get-segment-details-for-a-specific-frame/40009

---

## Post #1 by @maniron (2024-11-04 06:51 UTC)

<p>Hi,<br>
I am trying to get the number of segmentations done for a frame using python. I am trying this out using the following code</p>
<blockquote>
<p>segmentationNodeName = “Segmentation”<br>
segmentationNode = slicer.mrmlScene.GetFirstNodeByName(segmentationNodeName)<br>
segVal = segmentationNode.GetSegmentation()</p>
</blockquote>

---

## Post #2 by @muratmaga (2024-11-04 18:44 UTC)

<aside class="quote no-group" data-username="maniron" data-post="1" data-topic="40009">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/ee7513/48.png" class="avatar"> maniron:</div>
<blockquote>
<p>segmentationNodeName = “Segmentation”<br>
segmentationNode = slicer.mrmlScene.GetFirstNodeByName(segmentationNodeName)<br>
segVal = segmentationNode.GetSegmentation()</p>
</blockquote>
</aside>
<p>And what’s the problem?</p>

---

## Post #3 by @maniron (2024-11-05 05:07 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> I want to get segment details for each frame , when ever I make getSegmentation call I get the total no of segmentation , and not the segment correspond to the frame which I want, How can I get segment details of a particular frame of my choice</p>

---

## Post #4 by @muratmaga (2024-11-05 15:43 UTC)

<aside class="quote no-group" data-username="maniron" data-post="3" data-topic="40009">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/ee7513/48.png" class="avatar"> maniron:</div>
<blockquote>
<p>not the segment correspond to the frame which I want,</p>
</blockquote>
</aside>
<p>I am not sure what you mean by that? You mean you want the segmentation from a specific slice?</p>

---

## Post #5 by @maniron (2024-11-05 15:51 UTC)

<p>Yes I want to find specific segment for a slice</p>

---

## Post #6 by @muratmaga (2024-11-05 15:54 UTC)

<p>There is an example of getting the segmentation as a specific point in the script repository. You can probably rework that;</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-segments-visible-at-a-selected-position" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-segments-visible-at-a-selected-position</a></p>

---

## Post #7 by @maniron (2024-11-06 05:07 UTC)

<p>Can I rephrase my question</p>
<p>consider I have a nrrd file with 100 frames<br>
Now I segment each frame/slice<br>
After segmenting each frame/slice , how to get a particular frame/slice segment details or mask</p>

---

## Post #8 by @muratmaga (2024-11-06 05:33 UTC)

<p>If you look at the script examples I shared above, you can probably put together something using <code>slicer.util.arrayFromSegmentBinaryLabelmap</code>, then you can extract the 2D mask using your slice number.</p>
<p>That will give you the whole</p>
<pre><code class="lang-auto">volumeNode = getNode('MRHead')
segmentationNode = getNode('Segmentation')
segmentId = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName('Segment_1')

# Get segment as numpy array
segmentArray = slicer.util.arrayFromSegmentBinaryLabelmap(segmentationNode, segmentId, volumeNode)
</code></pre>

---

## Post #9 by @maniron (2024-11-06 05:37 UTC)

<p>Thanks for replying , the thing here is that consider I dont know details of segment id, Actually I am trying to integrate a tracker model after using one model for segmentation, so for tracker model when we move from one slice to another , the last slice segmented (mask) will be utilised to get a segment for the current slice</p>
<p>For this scenario kindly provide some sample code which would be helpful</p>

---

## Post #10 by @mikebind (2024-11-06 18:46 UTC)

<p>Using the approach described by <a class="mention" href="/u/muratmaga">@muratmaga</a>, you get the array containing all slices, is there some reason you can’t choose the slice you want out of that?  Perhaps it would help if you gave a higher level overview of what you are trying to accomplish.  You now mention a tracker for the first time, for example.  Slicer IGT has many tools for working with real time tool tracking, and depending on what it is you are trying to accomplish, may make it unnecessary for you to find, for example, the slice corresponding to a tracked location.</p>

---

## Post #11 by @muratmaga (2024-11-06 22:22 UTC)

<aside class="quote no-group" data-username="maniron" data-post="9" data-topic="40009">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/ee7513/48.png" class="avatar"> maniron:</div>
<blockquote>
<p>Thanks for replying , the thing here is that consider I dont know details of segment id, Actually I am trying to integrate a tracker model after using one model for segmentation, so for tracker model when we move from one slice to another , the last slice segmented (mask) will be utilised to get a segment for the current slice</p>
</blockquote>
</aside>
<p>Before you start into it, you might need to understand how segmentation works in slicer. Segmentation is not slice by slice, but is in context of the whole volume. So if you have one segment (Segment_1) with only two slices, say one is at the very top, and the one at the very bottom, they will have the same exact ID, which is Segment_1. So perhaps experiment with segmenting with sample data and see how you can extract what you want to extract before you do the tracking.</p>

---

## Post #12 by @maniron (2024-11-07 07:02 UTC)

<p>In this case how can I get the mask of previous frame/slice and utilize it on the next frame/slice . As I could see the same segment id is being used for each slice</p>

---

## Post #13 by @muratmaga (2024-11-07 17:45 UTC)

<p>If you know the position you want the mask (from your description sounds like you do), you can use method I described above.</p>

---

## Post #14 by @maniron (2024-11-12 05:33 UTC)

<p>I dont know whether I am asking the question right, but what I want is that consider we segment a frame/slice , model gives a mask. When I move to a next frame/slice I want to utilize the mask to generate a new mask for that frame/slice. But I am not able to find the code to get the mask . As I could see the segmentation details are maintained in a same segment ID . Kindly help me out with this solution. The main aim here is to do a multi object segmentation</p>

---
