# SlicerRT Defining Margins

**Topic ID**: 20776
**Date**: 2021-11-24
**URL**: https://discourse.slicer.org/t/slicerrt-defining-margins/20776

---

## Post #1 by @Maharshi_Panchal (2021-11-24 16:20 UTC)

<p>Hello,</p>
<p>Our team has been working to improve the delineation of tumors to guide better radiation planning. We have been looking at the 3DSlicer extension “SlicerRT” you created as a method of defining tumor margins, but were having trouble navigating the modules.</p>
<p>We reviewed the documentation and a module called “Segment Morphology” stood out to us as it allows the user to add and remove tumor margins. However, it seems this module is no longer a part of the extension. Has the module has since been updated, or if its features have been split up into other modules?</p>
<p>Thank you for your time, and we look forward to hearing back from you soon.</p>

---

## Post #2 by @cpinter (2021-11-25 14:39 UTC)

<p>Copying my answer to your question to me on LinkedIn:</p>
<p>“That module has become deprecated with the release of the new Segment Editor module in 3D Slicer core. Please download the latest preview version and see the “Logical operators” and “Margin” effects in said module.”</p>
<p>I understand that you want a quick answer but please in the future wait a bit before you post the same question to multiple places. Thank you.</p>

---

## Post #3 by @Maharshi_Panchal (2021-11-25 23:42 UTC)

<p>Hello Mr Pinter,</p>
<p>Sorry for posting in multiple places, I wasn’t sure how long my question would pend on here and thought it would be quicker to reach out over LinkedIn. My apologies!</p>
<p>I’ve downloaded the preview version and installed SlicerRT on this version as well. However, I’m still unable to access the “Segment Morphology” module. Our team is looking for a way to manually define tumor margins for delineation. For example, manually drawing on slices and then having that volume extend to cover a 3D region.</p>
<p>I tried playing around with the “Margin” effect in Segment Editor as well, but haven’t found a way to use it for our specific purposes. Do you have any advice on what my next steps should be?</p>
<p>Thank you for your time, we really appreciate your help!</p>
<p>Best,<br>
Maharshi</p>

---

## Post #4 by @lassoan (2021-11-26 00:01 UTC)

<aside class="quote no-group" data-username="Maharshi_Panchal" data-post="3" data-topic="20776">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/maharshi_panchal/48/13236_2.png" class="avatar"> Maharshi_Panchal:</div>
<blockquote>
<p>I tried playing around with the “Margin” effect in Segment Editor as well, but haven’t found a way to use it for our specific purposes.</p>
</blockquote>
</aside>
<p>Can you describe what your specific purpose is?</p>
<p>When you tried the Margin effect, what did you do? what did you expect to happen? what happened instead?</p>

---

## Post #5 by @Maharshi_Panchal (2021-12-03 21:47 UTC)

<p>Our goal is to have a radiation oncologist define tumor margins on CT scans loaded into Slicer. With the margin effect, I was hoping to find a way to manually annotate the scan and create a 3D “blob” that defines the margins of the tumor.</p>
<p>We have tried using the “draw” effect, but this annotation doesn’t allow us to create a 3D margin.</p>
<p>Any suggestions?<br>
Thank you.</p>

---

## Post #6 by @KSC_IA (2023-02-10 11:53 UTC)

<p>Hi <a class="mention" href="/u/maharshi_panchal">@Maharshi_Panchal</a></p>
<p>I understand your problem. 3DSlicer works a little differently compared to Treatment Planning Systems (TPS). To do what you want to do, follow the following steps:</p>
<ol>
<li>Make a segmentation in Segment Editor (ensure that you scroll down and check that in ‘Modify other segments’ - ‘Allow Overlap’ is selected) - For the purpose of this example, name it ‘Segment_1’.</li>
<li>Add another segmentation (Segment_2) and copy ‘Segment_1’ using Logical Operators using the ‘Copy’ function</li>
<li>Now you can add a margin of your choice using the ‘Margin’ function on Segment_2.</li>
</ol>
<p>This is a different workflow from most TPS’s, where we use a ‘create margin from…’ function to add a margin to an existing segmentation (we call them contours, but that’s just semantics).</p>
<p>FYI <a class="mention" href="/u/maharshi_panchal">@Maharshi_Panchal</a> …I can confirm that the margin addition function is a rolling-ball, isotropic  margin,</p>
<p>Hope that helps!</p>

---
