# Inquiry Regarding TotalSegmentator V2 Compatibility with Rabbit Micro-CT Images for Lung Segmentation

**Topic ID**: 32489
**Date**: 2023-10-30
**URL**: https://discourse.slicer.org/t/inquiry-regarding-totalsegmentator-v2-compatibility-with-rabbit-micro-ct-images-for-lung-segmentation/32489

---

## Post #1 by @cong_lu (2023-10-30 18:18 UTC)

<p>Dear TotalSegmentator Team,</p>
<p>Thank you for releasing the updated TotalSegmentator V2 software. I am a Master’s student in medical science, currently focused on the quantitative analysis of micro-CT images in a rabbit model.</p>
<p>I’m wondering if TotalSegmentator V2 is compatible with rabbit micro-CT images, specifically for lung segmentation?</p>
<p>Thank you for your time and assistance.</p>
<p>Best regards</p>

---

## Post #2 by @rbumm (2023-10-30 19:58 UTC)

<p>Not really - this is the output of Totalsegmentatoir in a rodent micro CT</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df7ff11d137bae9972579ea50780e1cd4744449f.jpeg" data-download-href="/uploads/short-url/vTaAAbFHRlebzlGj72Jz3KQdfJB.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df7ff11d137bae9972579ea50780e1cd4744449f_2_690x255.jpeg" alt="image" data-base62-sha1="vTaAAbFHRlebzlGj72Jz3KQdfJB" width="690" height="255" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df7ff11d137bae9972579ea50780e1cd4744449f_2_690x255.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df7ff11d137bae9972579ea50780e1cd4744449f_2_1035x382.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df7ff11d137bae9972579ea50780e1cd4744449f_2_1380x510.jpeg 2x" data-dominant-color="6B6B73"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×710 211 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @rbumm (2023-10-30 20:02 UTC)

<p>And this is the output after manual lung segmentation by defining seeds</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09dd3310e65be82d4194c25aa96ada46d5c2a856.jpeg" data-download-href="/uploads/short-url/1pgdkb7OXyLZshea8esUpt7me7c.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09dd3310e65be82d4194c25aa96ada46d5c2a856_2_690x338.jpeg" alt="image" data-base62-sha1="1pgdkb7OXyLZshea8esUpt7me7c" width="690" height="338" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09dd3310e65be82d4194c25aa96ada46d5c2a856_2_690x338.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09dd3310e65be82d4194c25aa96ada46d5c2a856_2_1035x507.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09dd3310e65be82d4194c25aa96ada46d5c2a856_2_1380x676.jpeg 2x" data-dominant-color="676772"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1402×687 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @cong_lu (2023-10-30 20:31 UTC)

<p>Dear rbumm,<br>
Thank you for your prompt reply. I have also tried LungCTSegmenter for lung segmentation for in micro-CT images, but the results are not satisfactory.<br>
Could you possible have any recommendations or suggestions that might improve the quality of the lung segmentation using micro-CT images?<br>
Best<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e15c73b2b5a39c966b974f3f760eeb520e001732.jpeg" data-download-href="/uploads/short-url/w9DvvDGKOsOnE00yF8GCkpT3oDE.jpeg?dl=1" title="Screenshot 2023-10-30 at 4.21.02 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e15c73b2b5a39c966b974f3f760eeb520e001732_2_690x430.jpeg" alt="Screenshot 2023-10-30 at 4.21.02 PM" data-base62-sha1="w9DvvDGKOsOnE00yF8GCkpT3oDE" width="690" height="430" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e15c73b2b5a39c966b974f3f760eeb520e001732_2_690x430.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e15c73b2b5a39c966b974f3f760eeb520e001732_2_1035x645.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e15c73b2b5a39c966b974f3f760eeb520e001732_2_1380x860.jpeg 2x" data-dominant-color="C3C3C3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-10-30 at 4.21.02 PM</span><span class="informations">1920×1198 203 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @muratmaga (2023-10-31 01:24 UTC)

<p>I would love to be wrong, but my understanding is without retraining or at the minimum finetuning them using your own segmented data, there is not much you can do with models trained on human clinical dataset.</p>

---

## Post #6 by @rbumm (2023-10-31 08:48 UTC)

<p>Maybe this link may help:</p>
<aside class="quote quote-modified" data-post="44" data-topic="15006">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/lungctanalyzer-extension-for-lung-ct-segmentation-and-analysis-for-covid-19-assessment/15006/44">LungCTAnalyzer extension for lung CT segmentation and analysis for COVID-19 assessment</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I think the only value hardcoded for human clinical CT is the preview image resolution of 2mm. This is probably too large for microCT. 
You can easily modify this value by editing this line in LungCTSegmenter.py file: 


Alternatively, you can modify the spacing value of the volume in Volumes module to be 10x larger. This does not change the image in any way, it just makes all length measurements 10x larger. 
<a class="mention" href="/u/rbumm">@rbumm</a> we could consider allowing users to edit this value in some advanced parameters …
  </blockquote>
</aside>


---

## Post #7 by @cong_lu (2023-11-01 19:59 UTC)

<p>Thanks dear rbumm. LungCT Segmenter works for the micro-CT images after changing the parameter from 2 to 0.2. but the result is not satisfied.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/679d9e35290c49e1ab53c170abaab271123939a7.jpeg" data-download-href="/uploads/short-url/eMCSdqwSokx1kOl2OCS8wAcSBLx.jpeg?dl=1" title="Screenshot 2023-10-31 at 10.04.13 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/679d9e35290c49e1ab53c170abaab271123939a7_2_690x448.jpeg" alt="Screenshot 2023-10-31 at 10.04.13 AM" data-base62-sha1="eMCSdqwSokx1kOl2OCS8wAcSBLx" width="690" height="448" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/679d9e35290c49e1ab53c170abaab271123939a7_2_690x448.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/679d9e35290c49e1ab53c170abaab271123939a7_2_1035x672.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/679d9e35290c49e1ab53c170abaab271123939a7_2_1380x896.jpeg 2x" data-dominant-color="A19C99"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-10-31 at 10.04.13 AM</span><span class="informations">1920×1249 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @rbumm (2023-11-01 20:47 UTC)

<p>Is this by manual placement of the segmentation seeds or by AI segmentation? Can you make a CT sample available?</p>

---

## Post #9 by @cong_lu (2023-11-01 21:00 UTC)

<p>Bot the manual seeds and AI work well for the Chest CT sample. My previous try was segmented by AI. Here is the manual placement seeds. The result still not good. And there is no change after placing more seeds on missing area.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59ae67967a38ba00db54a115734558c41b55f168.jpeg" data-download-href="/uploads/short-url/cNm9C9HJvLA9WFY4r8bRRkWBYfu.jpeg?dl=1" title="Screenshot 2023-11-01 at 4.57.55 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59ae67967a38ba00db54a115734558c41b55f168_2_690x363.jpeg" alt="Screenshot 2023-11-01 at 4.57.55 PM" data-base62-sha1="cNm9C9HJvLA9WFY4r8bRRkWBYfu" width="690" height="363" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59ae67967a38ba00db54a115734558c41b55f168_2_690x363.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59ae67967a38ba00db54a115734558c41b55f168_2_1035x544.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59ae67967a38ba00db54a115734558c41b55f168_2_1380x726.jpeg 2x" data-dominant-color="939298"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-11-01 at 4.57.55 PM</span><span class="informations">1920×1011 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @cong_lu (2023-11-01 21:13 UTC)

<p>Dear rbumm,<br>
After processing Lung CT Analyzer using the lung segmentation generated, I’ve got some color ball in the image. I don’t think the colour balls affect the statistics results.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e36e6e54669ea737ae92bb73326cf3d35f2642f8.jpeg" data-download-href="/uploads/short-url/wrWYWU1w1M5DtDb9pND3ZoA9AUw.jpeg?dl=1" title="Screenshot 2023-11-01 at 5.08.19 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e36e6e54669ea737ae92bb73326cf3d35f2642f8_2_690x355.jpeg" alt="Screenshot 2023-11-01 at 5.08.19 PM" data-base62-sha1="wrWYWU1w1M5DtDb9pND3ZoA9AUw" width="690" height="355" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e36e6e54669ea737ae92bb73326cf3d35f2642f8_2_690x355.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e36e6e54669ea737ae92bb73326cf3d35f2642f8_2_1035x532.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e36e6e54669ea737ae92bb73326cf3d35f2642f8_2_1380x710.jpeg 2x" data-dominant-color="B1ADAC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-11-01 at 5.08.19 PM</span><span class="informations">1920×989 159 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @diazandr3s (2023-11-02 11:57 UTC)

<p>I agree with <a class="mention" href="/u/muratmaga">@muratmaga</a> on this:</p>
<p><code>without retraining or at the minimum finetuning them using your own segmented data, there is not much you can do with models trained on human clinical dataset.</code></p>
<p><a class="mention" href="/u/cong_lu">@cong_lu</a> have you considered training an AI model for this task using <a href="https://github.com/Project-MONAI/MONAILabel/tree/main" rel="noopener nofollow ugc">MONAI Label</a>?</p>
<p>Here I showed how to organize the dataset and train a model: <a href="https://youtu.be/-HAryYAO5J4?si=uxJPxrDuTDUE-zHr&amp;t=560" rel="noopener nofollow ugc">https://youtu.be/-HAryYAO5J4?si=uxJPxrDuTDUE-zHr&amp;t=560</a></p>

---

## Post #12 by @cong_lu (2023-11-02 18:53 UTC)

<p>thanks for your suggestion. I’d like to use MONAI Label to train an AI model. I don’t have much experience in programming. I cannot understand the command part in your video. And I got the ERROR from MONAI Label when I start the module. Could you kindly guide me to solve the issue?</p>
<p>Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/Extensions-31938/MONAILabel/lib/Slicer-5.4/qt-scripted-modules/MONAILabel.py”, line 1072, in fetchInfo<br>
info = self.logic.info()<br>
File “/Applications/Slicer.app/Contents/Extensions-31938/MONAILabel/lib/Slicer-5.4/qt-scripted-modules/MONAILabel.py”, line 2263, in info<br>
return self._client().info()<br>
File “/Applications/Slicer.app/Contents/Extensions-31938/MONAILabel/lib/Slicer-5.4/qt-scripted-modules/MONAILabel.py”, line 2239, in _client<br>
if mc.auth_enabled():<br>
File “/Applications/Slicer.app/Contents/Extensions-31938/MONAILabel/lib/Slicer-5.4/qt-scripted-modules/MONAILabelLib/client.py”, line 83, in auth_enabled<br>
status, response, _, _ = MONAILabelUtils.http_method(“GET”, self._server_url, selector)<br>
File “/Applications/Slicer.app/Contents/Extensions-31938/MONAILabel/lib/Slicer-5.4/qt-scripted-modules/MONAILabelLib/client.py”, line 521, in http_method<br>
conn.request(method, selector, body=body, headers=headers)<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/http/client.py”, line 1285, in request<br>
self._send_request(method, url, body, headers, encode_chunked)<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/http/client.py”, line 1331, in _send_request<br>
self.endheaders(body, encode_chunked=encode_chunked)<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/http/client.py”, line 1280, in endheaders<br>
self._send_output(message_body, encode_chunked=encode_chunked)<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/http/client.py”, line 1040, in _send_output<br>
self.send(msg)<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/http/client.py”, line 980, in send<br>
self.connect()<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/http/client.py”, line 946, in connect<br>
self.sock = self._create_connection(<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/socket.py”, line 844, in create_connection<br>
raise err<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/socket.py”, line 832, in create_connection<br>
sock.connect(sa)<br>
ConnectionRefusedError: [Errno 61] Connection refused<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/9257cf8bd8da02ee3896294329932adbb85bfc9a.jpeg" data-download-href="/uploads/short-url/kSBQluMiKxqDdihzg2gyB9sgLHk.jpeg?dl=1" title="Screenshot 2023-11-02 at 2.52.20 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/9257cf8bd8da02ee3896294329932adbb85bfc9a_2_690x448.jpeg" alt="Screenshot 2023-11-02 at 2.52.20 PM" data-base62-sha1="kSBQluMiKxqDdihzg2gyB9sgLHk" width="690" height="448" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/9257cf8bd8da02ee3896294329932adbb85bfc9a_2_690x448.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/9257cf8bd8da02ee3896294329932adbb85bfc9a_2_1035x672.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/9257cf8bd8da02ee3896294329932adbb85bfc9a_2_1380x896.jpeg 2x" data-dominant-color="BAB7B6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-11-02 at 2.52.20 PM</span><span class="informations">1920×1249 162 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @diazandr3s (2023-11-02 23:24 UTC)

<p>Hi <a class="mention" href="/u/cong_lu">@cong_lu</a>,</p>
<p>MONAI Label comprises two parts: a server that hosts the AI models and a viewer part that connects to the server (i.e. 3DSlicer).</p>
<p>The server part can be installed and started following these instructions: <a href="https://github.com/Project-MONAI/MONAILabel#step-1-installation" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Project-MONAI/MONAILabel: MONAI Label is an intelligent open source image labeling and learning tool.</a></p>
<p>Unfortunately, the server part is being tested on Linux and Windows operating systems, not Apple OSs</p>
<p>I hope this helps,</p>

---

## Post #14 by @cong_lu (2023-11-03 03:14 UTC)

<p>Thank you <a class="mention" href="/u/diazandr3s">@diazandr3s</a> for your reply. I’ll find a Windows PC and try to install the server. I’ve no experience with Python, which is a big challenge. I’ll keep you update.</p>

---

## Post #15 by @cong_lu (2023-11-03 16:04 UTC)

<p>Hello <a class="mention" href="/u/diazandr3s">@diazandr3s</a> ,<br>
monailabel-0.8.1 was successfully installed, but I was stuck in downloading sample apps. Could you help me check the message from cmd?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a304bdaa073455c3f21aef608fb7b86db9f6b9b6.png" data-download-href="/uploads/short-url/ng7Z4c8zrPuGUWx6QkLL0uUgPlk.png?dl=1" title="Screenshot 2023-11-03 120107" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a304bdaa073455c3f21aef608fb7b86db9f6b9b6.png" alt="Screenshot 2023-11-03 120107" data-base62-sha1="ng7Z4c8zrPuGUWx6QkLL0uUgPlk" width="690" height="439" data-dominant-color="222222"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-11-03 120107</span><span class="informations">938×598 29.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #16 by @diazandr3s (2023-11-03 18:19 UTC)

<p>Hi <a class="mention" href="/u/cong_lu">@cong_lu</a>,</p>
<p>It seems you’ve installed monailabel but didn’t activate the Python env.<br>
Have you seen these instructions created by <a class="mention" href="/u/rbumm">@rbumm</a>?</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/MONAILabelLung/MONAILabel_Installation.html">
  <header class="source">
      <img src="https://projectweek.na-mic.org/assets/favicons/favicon.ico" class="site-icon" width="16" height="16">

      <a href="https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/MONAILabelLung/MONAILabel_Installation.html" target="_blank" rel="noopener nofollow ugc">NA-MIC Project Weeks</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/MONAILabelLung/MONAILabel_Installation.html" target="_blank" rel="noopener nofollow ugc">MONAI Label installation</a></h3>

  <p>Website for NA-MIC Project Weeks</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Please let us know</p>

---
