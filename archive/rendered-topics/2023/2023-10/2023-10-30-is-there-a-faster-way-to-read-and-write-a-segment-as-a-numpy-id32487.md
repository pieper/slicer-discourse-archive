# Is there a faster way to read and write a segment as a numpy array?

**Topic ID**: 32487
**Date**: 2023-10-30
**URL**: https://discourse.slicer.org/t/is-there-a-faster-way-to-read-and-write-a-segment-as-a-numpy-array/32487

---

## Post #1 by @abhilaksh_singh_reen (2023-10-30 17:08 UTC)

<p>Hi.<br>
My team is building a Python Scripted Slicer Module for an organ segmentation task. We have a Segmentation Model to which we are only giving a single slice as input (at a time) and the model outputs the mask for that slice. We then update the segmentation in Slicer with this mask (after postprocessing the model output) so the user can correct it, and then move on to segmenting the next slice.</p>
<p>To get the current segmentation mask from Slicer and then to update it with the output of the model, I am using the <code>slicer.util.arrayFromSegmentBinaryLabelmap</code> and <code>slicer.util.updateSegmentBinaryLabelmapFromArray</code> functions respectively.</p>
<p>For the Module we are building, speed is of prime importance and I find that the functions <code>slicer.util.arrayFromSegmentBinaryLabelmap</code> and<br>
<code>slicer.util.updateSegmentBinaryLabelmapFromArray</code> are slow, with the latter often taking <strong>up to 500 ms</strong> just to update the segmentation for a single slice. I suspect that is because the update occurs for the entire 3D segmentation. Please note that the time mentioned is just for the function call and does not include getting the segmentation node, segment id, or construction of the numpy array.</p>
<p>I have a couple of questions:</p>
<ol>
<li>Are there any faster alternatives to these functions?</li>
<li>Am I missing something and is there a better and faster approach to handling this kind of task (one slice at a time), maybe by doing things differently than I am?</li>
</ol>
<p>Thank you in advance.</p>

---

## Post #2 by @lassoan (2023-10-30 17:14 UTC)

<p>A lot needs to be done when you import or update a segment, most notably apply masking settings and manage overlap (e.g., move out the modified segment to a new layer if it now overlaps another segment and overlap is enabled; make sure you don’t modify any area of the segment that is protected by masking settings), and you also need to update all representations (e.g., if you update the labelmap but you have closed surface representation that is displayed in 3D then the update will take some more time).</p>
<p>These extra computations can be all bypassed. You can get the internal representation (shared labelmap) from the segmentation object. You can remove the closed surface representation to prevent losing time due to its update, or use the new experimental surface net based surface generation and smoothing.</p>

---

## Post #3 by @abhilaksh_singh_reen (2023-11-03 17:51 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thank you for your response.</p>
<p>I assume that <code>slicer.util.arrayFromSegmentInternalBinaryLabelmap</code> is the way to go for getting the internal shared labelmap. Please do correct me if I am wrong or if there is a better way. It took me a couple of days to make the changes to our module and <code>slicer.util.arrayFromSegmentInternalBinaryLabelmap</code> is definitely faster.</p>
<p>However, I find that the numpy array returned by <code>slicer.util.arrayFromSegmentInternalBinaryLabelmap</code> is not of the same shape as the slice itself. The dimensions are reduced so that the mask just fits in the array. Is there a way to get the segment array with the same dimensions as the slice? Or, is it possible to relate the two, perhaps by knowing which point of the slice corresponds to the first <code>[0,0]</code> point of the segment array?</p>

---

## Post #4 by @lassoan (2023-11-03 18:01 UTC)

<p><code>slicer.util.arrayFromSegmentInternalBinaryLabelmap</code> returns the actual internal data representation. We will not change this internal representation to use more memory than what is needed. However, you can modify the image any way you want (e.g., pad it to make it larger) and then set it as the new internal representation (for example by importing a labelmap volume into the segmentation). Once you set your arbitrarily large labelmap in the segmentation, you can get access to it as a numpy array using <code>slicer.util.arrayFromSegmentInternalBinaryLabelmap</code>.</p>

---

## Post #5 by @abhilaksh_singh_reen (2023-11-20 17:24 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks again for your response. Is it possible that you can provide a code snippet that updates the segmentation the way you have described?</p>

---

## Post #6 by @lassoan (2023-11-20 17:36 UTC)

<p>What part you had trouble implementing? Can you copy here (or post a link to) the code you have so far?</p>

---

## Post #7 by @abhilaksh_singh_reen (2023-11-26 12:11 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, please excuse me for the late response. Unfortunately, I will not be able to provide the code of the extension as the team has not released it publicly yet.</p>
<p>After a few tweaks, I did get what you suggested to work, but the problem I faced was as follows:</p>
<ol>
<li>I set the internal representation once to an empty numpy array of the same shape as the loaded volume.</li>
<li>Now, I could get and set the internal representation and it was of the same shape.</li>
<li>However, if the user makes a change to the segment, the internal representation changes to the compressed one again.</li>
</ol>
<p>Currently, I have implemented a makeshift workaround, that sets the segments in the first and last slice of the volume to 1 (so that Slicer cannot compress it), it works (unless you have to segment a slice at the end) but I need to change it to the appropriate logic.</p>
<pre><code class="lang-auto">  # Get the array
  segment1SegmentArrayFull[0, :, :] = 1
  segment1SegmentArrayFull[-1, :, :] = 1
  # Set the array
</code></pre>
<p>I also want to ask, is it necessary to import a <code>labelmap volume</code> for this purpose or can this be done another way?</p>

---
