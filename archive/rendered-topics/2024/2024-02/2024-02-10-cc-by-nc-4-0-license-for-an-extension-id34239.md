# CC BY-NC 4.0 License for an Extension

**Topic ID**: 34239
**Date**: 2024-02-10
**URL**: https://discourse.slicer.org/t/cc-by-nc-4-0-license-for-an-extension/34239

---

## Post #1 by @zafryldz (2024-02-10 15:08 UTC)

<p>We want to create an extension for our recent <a href="https://github.com/mazurowski-lab/SegmentAnyBone" rel="noopener nofollow ugc">SegmentAnyBone</a> (fine-tuned version of SAM) model as an alternative to generic SAM since it can offer a better segmentation performance than SAM when it comes to bones. However, our model’s license is CC BY-NC 4.0.</p>
<p>In this sense, can we release an extension for SegmentAnyBone on 3D Slicer’s Extension Index with CC BY-NC 4.0 license? If we cannot, can we create a public repository on GitHub so that people can install our new extension manually (by cloning the repository and introducing it to 3D Slicer) on 3D Slicer?</p>
<p>Thanks in advance for your support!</p>

---

## Post #2 by @pieper (2024-02-10 16:25 UTC)

<p>Yes, you may provide an extension that has non-commercial restrictions, but please make it explicit in the readme so that it’s clear what this implies for users (not everyone will instantly recognize the license abbreviation).  You can refer to the <a href="https://github.com/lassoan/SlicerTotalSegmentator">TotalSegmentator</a> extension and the way Slicer’s <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/screencapture.html#setting-up-ffmpeg">ScreenCapture</a> module handle installation of code with different licenses.</p>
<p>In any case it’s best not to bundle the model weights with the extension, and instead install them on first-use.  It would also be nice if your extension could support other SAM-derived models so others might add models in the future using the same infrastructure.  In that sense it would be nice if you could integrate SAM-related extensions for generality and maximal reuse (as discussed in <a href="https://github.com/Slicer/ExtensionsIndex/pull/1954">this thread</a>, also with you, I believe?).</p>

---

## Post #3 by @zafryldz (2024-02-13 04:36 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> Yes, we have discussed SegmentWithSAM extension before. I can try to set up an infrastructure which allows users to add a different SAM based model. On the other hand, I am not sure I integrate SegmentWithSAM extension to the extension I am going to develop soon since their licenses are different. SegmentWithSAM has Apache 2.0, and the new extension will have CC BY-NC 4.0 license.</p>

---

## Post #4 by @pieper (2024-02-13 14:10 UTC)

<p>Like in TotalSegmentator, it’s possible to mix models with different licenses while sharing the same Slicer integration code.  As discussed, the ideal situation is to share the common elements so that it’s less confusing for users to try different models and approaches.</p>

---

## Post #5 by @zafryldz (2024-02-23 22:30 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> Instead of serving different models with different licenses, can we change the existing license (Apache 2.0) of our SegmentWithSAM extension repository to CC BY-NC 4.0? We are afraid that people might not be able to realize that we have different licenses for different models. In this way, we can have one license (CC BY-NC 4.0) for both of generic SAM and our SegmentAnyBone model within one extension.</p>

---

## Post #6 by @jamesobutler (2024-02-23 23:27 UTC)

<p><a class="mention" href="/u/zafryldz">@zafryldz</a> Is there a specific reason why you all have moved from Apache 2.0 to CC BY-NC 4.0?</p>
<p>Since 3D Slicer supports commercialized 3D Slicer Custom Applications, then the change to the new license would prevent integration of your work into a commercial solution. That commercial solution may be using funds to pay for user support for the feature especially if you all as the original developers are no longer supporting/maintaining the code sometime in the future.</p>

---

## Post #7 by @lassoan (2024-02-24 17:10 UTC)

<p>Keeping distributing the module with permissive license would make sense, as we currently do not have a mechanism to give strong warningsl to the user that the extension has restrictive license.</p>
<p>At runtime when the user chooses a model that comes with a restrictive license, you can display a popup to make the user confirm that he is aware of the limitations. This is already how TotalSegmentator works (it even asks for a registration key that non-commercial users can request for free).</p>
<p>However, in the long term, you may be better off financially if you make your models available without restrictions. Modules that are distributed with restrictive license are largely ignored by companies (except extremely rare cases when nothing similar exists with permissive license that has comparable performance and the task is not important enough for the company to solve it with internal development). In contrast, if you use a permissive license then companies can build your segmentation model into their products and if it turns out to work well then when they need improvements, customizations, and long-term maintenance then most likely they will pay you to do it. This is why SAM, MedSAM, most MONAI and nn-unet models are distributed with permissive license.</p>

---

## Post #8 by @zafryldz (2024-02-29 04:50 UTC)

<p>Our leadership is not ready to release it under a permissive license because of commercialization reasons. This is the reason why we want to either change the license of our previously released extension (from Apache 2.0 to CC BY-NC 4.0) or release a seperate extension for SegmentAnyBone with CC BY-NC 4.0 license.</p>

---

## Post #9 by @rkikinis (2024-02-29 06:11 UTC)

<p>Hi Zafer<br>
Changing the license on an already released extension is a bait and switch maneuver. Having a NC license on a new extension is acceptable as long as you make sure that potential users understand this.<br>
Best<br>
Ron</p>
<p>This email is intended for non-work related messages</p>

---

## Post #10 by @jamesobutler (2024-02-29 17:49 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="34239">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>At runtime when the user chooses a model that comes with a restrictive license, you can display a popup to make the user confirm that he is aware of the limitations. This is already how TotalSegmentator works (it even asks for a registration key that non-commercial users can request for free).</p>
</blockquote>
</aside>
<p>Ultimately <a class="mention" href="/u/zafryldz">@zafryldz</a> it appears the above will need to be implemented whether it is a separate extension or contained in the existing SegmentWithSAM extension. This being that the license in the GitHub source repository is not known to users interacting within the Slicer UI. Based on Steve’s previous comments and the success of TotalSegmentator, it would seem that the preference is to maintain the various SAM-derived models in the same extension for better maintenance support in the future. TotalSegmentator has the apache license for the extension, with the more restrictive non-commercial license key required to run inference on additional tasks.</p>

---
