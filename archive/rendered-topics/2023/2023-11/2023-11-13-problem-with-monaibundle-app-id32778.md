---
topic_id: 32778
title: "Problem With Monaibundle App"
date: 2023-11-13
url: https://discourse.slicer.org/t/32778
---

# Problem with Monaibundle app

**Topic ID**: 32778
**Date**: 2023-11-13
**URL**: https://discourse.slicer.org/t/problem-with-monaibundle-app/32778

---

## Post #1 by @franbuemi (2023-11-13 12:34 UTC)

<p>I have a problem with MonaiBundle. I just started trying to use the models from the Monailabel Zoo through the MonaiBundle app. When I click on ‘run’ in ‘auto segmentation,’ I get the following error message: ‘Failed to run inference in MONAI Label Server. Message: Status: 500; Response: Internal Server Error’</p>
<p>Traceback (most recent call last): File “C:/Users/franb/AppData/Local/slicer.org/Slicer 5.4.0/slicer.org/Extensions-31938/MONAILabel/lib/Slicer-5.4/qt-scripted-modules/MONAILabel.py”, line 1524, in onClickSegmentation result_file, params = self.logic.infer(model, image_file, params, session_id=self.getSessionId()) File “C:/Users/franb/AppData/Local/slicer.org/Slicer 5.4.0/slicer.org/Extensions-31938/MONAILabel/lib/Slicer-5.4/qt-scripted-modules/MONAILabel.py”, line 2296, in infer result_file, params = client.infer(model, image_in, params, label_in, file, session_id) File “C:\Users\franb\AppData\Local\slicer.org\Slicer 5.4.0\slicer.org\Extensions-31938\MONAILabel\lib\Slicer-5.4\qt-scripted-modules\MONAILabelLib\client.py”, line 344, in infer raise MONAILabelClientException(MONAILabelLib.client.MONAILabelClientException: (1, ‘Status: 500; Response: Internal Server Error’)</p>
<p>How can I solve it?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63c10d00312f064dd36195c0a49f6f0bdf7f384f.jpeg" data-download-href="/uploads/short-url/eesSuLDTbKJn90cRv1XyOTRqTyn.jpeg?dl=1" title="screen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63c10d00312f064dd36195c0a49f6f0bdf7f384f_2_690x369.jpeg" alt="screen" data-base62-sha1="eesSuLDTbKJn90cRv1XyOTRqTyn" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63c10d00312f064dd36195c0a49f6f0bdf7f384f_2_690x369.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63c10d00312f064dd36195c0a49f6f0bdf7f384f_2_1035x553.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63c10d00312f064dd36195c0a49f6f0bdf7f384f_2_1380x738.jpeg 2x" data-dominant-color="9999A1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screen</span><span class="informations">1920×1028 256 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @rbumm (2023-11-13 13:44 UTC)

<p>Please refer to the Monao Bundle <a href="https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/MONAIBundleIntegrationTutorial/">How To</a> that we have recently made.</p>

---

## Post #3 by @franbuemi (2023-12-16 17:35 UTC)

<p>I tried to install MONAI 1.20.rc6, but it seems like this version doesn’t exist. I couldn’t find it during the installation attempt, and I received the following message in the terminal.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac94958df547de159c983e72757ccfc05b06993d.png" data-download-href="/uploads/short-url/oCIsPOqkyhZiXrliqnq0gnqCBFH.png?dl=1" title="a" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac94958df547de159c983e72757ccfc05b06993d.png" alt="a" data-base62-sha1="oCIsPOqkyhZiXrliqnq0gnqCBFH" width="690" height="64" data-dominant-color="1A0F10"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">a</span><span class="informations">1107×103 5.79 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @rbumm (2023-12-17 19:22 UTC)

<p>You can use:</p>
<pre><code class="lang-auto">pip install monai==1.2.0
</code></pre>
<p>(tested)</p>
<p>Will change it in the documentation.</p>

---

## Post #5 by @franbuemi (2023-12-18 10:46 UTC)

<p>Solved, it works! Thank you very much!</p>

---

## Post #6 by @klc (2024-03-06 16:39 UTC)

<p>Hi Professor, I just followed the instructions of this article to set up monaibundle and it works like a charm. I am using the command <em>monailabel start_server --app apps/monaibundle --studies Desktop --conf models lung_nodule_ct_detection</em> to start the server and can produce satisfactory results. May I know what is the purpose of Setting up an AWS EC2 Windows server in the cloud?</p>
<p>I am using the LIDC-IDRI dataset to do the lung nodule segmentation and the right hand side the ground truth label while the left side is the label produced by monai zoo model</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b561328b943cfadedead10955cba821c8bf8841.jpeg" data-download-href="/uploads/short-url/1ChFkFZCgOcU8JuKA9xI9DX9fWN.jpeg?dl=1" title="WhatsApp Image 2024-03-07 at 00.16.53_1b18bef4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b561328b943cfadedead10955cba821c8bf8841_2_690x355.jpeg" alt="WhatsApp Image 2024-03-07 at 00.16.53_1b18bef4" data-base62-sha1="1ChFkFZCgOcU8JuKA9xI9DX9fWN" width="690" height="355" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b561328b943cfadedead10955cba821c8bf8841_2_690x355.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b561328b943cfadedead10955cba821c8bf8841_2_1035x532.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b561328b943cfadedead10955cba821c8bf8841.jpeg 2x" data-dominant-color="A1A1A0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">WhatsApp Image 2024-03-07 at 00.16.53_1b18bef4</span><span class="informations">1082×558 89.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you</p>

---

## Post #7 by @rbumm (2024-03-06 19:58 UTC)

<p>Great that it works</p>
<p>Best<br>
Rudolf</p>

---

## Post #8 by @lassoan (2024-03-07 04:16 UTC)

<aside class="quote no-group" data-username="klc" data-post="6" data-topic="32778">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/klc/48/68248_2.png" class="avatar"> klc:</div>
<blockquote>
<p>May I know what is the purpose of Setting up an AWS EC2 Windows server in the cloud?</p>
</blockquote>
</aside>
<p>If you want to get segmentation results quickly and you don’t want to buy a computer that has a GPU then you can rent virtual machines from AWS or other cloud providers. If you already have a computer with a good GPU then this is not necessary.</p>

---
