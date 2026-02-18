# Slicer interact with external deep learning segmentation software

**Topic ID**: 18129
**Date**: 2021-06-14
**URL**: https://discourse.slicer.org/t/slicer-interact-with-external-deep-learning-segmentation-software/18129

---

## Post #1 by @bywbilly (2021-06-14 22:56 UTC)

<p>Hi,</p>
<p>I am new to the slicer. I would like to incorporate slicer with our own segmentation module.  Since our module is doing segmentation step-by-step (e.g., vertebrae by vertebrae), so we would like to show the user partial segmentation and they can help us improve the partial segmentation. Specificlly, the workflow is:</p>
<ol>
<li>Slicer sends the scans to the program</li>
<li>program computes the segmentation of the first part and sends it back to Slicer</li>
<li>Slicer shows this part to the user and the user refines it. Then Slicer sends refined segmentation to the program.</li>
<li>Program computes the segmentation of the next part and repeats steps 2-4.</li>
</ol>
<p>I am wondering what kind of stuff should we use for achieving the goal (maybe writing a module)? And also I am wondering is there something similar in the community that I can refer to?</p>
<p>Thanks!</p>

---

## Post #2 by @cpinter (2021-06-15 09:22 UTC)

<p>There may be many approaches.</p>
<ul>
<li>You can use OpenIGTLink to send/receive image data</li>
<li>You can use web sockets if for some reason the above is not possible</li>
<li>Migrate the auto-segmentation step to Slicer</li>
</ul>
<p>For more concrete suggestions more concrete information would be useful.</p>

---

## Post #3 by @bywbilly (2021-06-15 14:39 UTC)

<p>Hi Csaba,</p>
<p>Thanks for your reply! I want to migrate the auto-segmentation step to Slicer. I am looking for some suggestion or some similar extensions of Slicer to start.</p>

---

## Post #4 by @cpinter (2021-06-15 14:56 UTC)

<p>If your auto-segmentation is deep learning based, then currently the most future-proof choice in Slicer would be to use MONAI. The <a href="https://projectweek.na-mic.org/PW35_2021_Virtual/">project week</a> will take place in two weeks (a free online event) where you can get up-to-date information about that. I suggest joining for the MONAI day on Tuesday June 29.</p>

---

## Post #5 by @bywbilly (2021-06-15 22:37 UTC)

<p>Hi Csaba,</p>
<p>Thanks for the reply and pointing the MONAI. But I am not looking for a framework for deep learning, I am quite familiar with PyTorch but not the Slicer. So I am looking for some Slicer modules that are designed to interact with some custom modules.</p>

---

## Post #6 by @lassoan (2021-06-16 17:29 UTC)

<p><a href="https://github.com/Project-MONAI/MONAILabel">MONAILabel</a> is developed exactly for solving your use case. You don’t need to use MONAI at all (or even pytorch), you can use your own network. You can of course redevelop and maintain a similar feature independently, but you may save time overall if you use/extend/customize a module developed by others. Even if you end up implementing your own solution, you could learn a lot from it as an example.</p>

---

## Post #7 by @bywbilly (2021-06-16 17:38 UTC)

<p>Hi Andras,</p>
<p>This project seems perfectly solve my question. Thanks!</p>

---
