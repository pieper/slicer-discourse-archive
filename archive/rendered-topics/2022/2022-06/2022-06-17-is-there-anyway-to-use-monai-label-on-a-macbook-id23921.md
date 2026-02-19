---
topic_id: 23921
title: "Is There Anyway To Use Monai Label On A Macbook"
date: 2022-06-17
url: https://discourse.slicer.org/t/23921
---

# Is there anyway to use MONAI LABEL on a Macbook?

**Topic ID**: 23921
**Date**: 2022-06-17
**URL**: https://discourse.slicer.org/t/is-there-anyway-to-use-monai-label-on-a-macbook/23921

---

## Post #1 by @Celina_Hallal (2022-06-17 20:48 UTC)

<p>Operating system: MacOS Monterey<br>
Slicer version: latest version (5.0)<br>
Python version: 3.10.5</p>
<p>I’m a totally newbie, so my questions may sound a little dumb. Is there anyway to use MONAI LABEL on a Mac M1? Probably will need some really basic explanations. Tks</p>

---

## Post #2 by @lassoan (2022-06-18 13:38 UTC)

<p>You can run the MONAILabel user interface in Slicer on a macbook. However, you need to connect to a MONAILabel server that runs on a GPU-equipped Linux or Windows system.</p>

---

## Post #3 by @Celina_Hallal (2022-06-18 15:38 UTC)

<p>Hmmmm… How I said earlier, I’m really newbie (Surgeon w almost no programming background trying to learn from scratch)… How exactly I do this? <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"></p>
<p>When I try to use MONAILabel on Slicer without specifying any server, this message appears (this happens even when I try to connect home without any proxy):</p>
<p>Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/Extensions-30822/MONAILabel/lib/Slicer-5.0/qt-scripted-modules/MONAILabel.py”, line 1030, in fetchInfo<br>
info = self.logic.info()<br>
File “/Applications/Slicer.app/Contents/Extensions-30822/MONAILabel/lib/Slicer-5.0/qt-scripted-modules/MONAILabel.py”, line 2121, in info<br>
return MONAILabelClient(self.server_url, self.tmpdir, self.client_id).info()<br>
File “/Applications/Slicer.app/Contents/Extensions-30822/MONAILabel/lib/Slicer-5.0/qt-scripted-modules/MONAILabelLib/client.py”, line 48, in info<br>
status, response, _ = MONAILabelUtils.http_method(“GET”, self._server_url, selector)<br>
File “/Applications/Slicer.app/Contents/Extensions-30822/MONAILabel/lib/Slicer-5.0/qt-scripted-modules/MONAILabelLib/client.py”, line 268, in http_method<br>
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
ConnectionRefusedError: [Errno 61] Connection refused</p>
<p>Sorry if is some really basic thing and thank you Andras!</p>

---

## Post #4 by @lassoan (2022-06-19 03:01 UTC)

<p>You need to have access to a computer with a strong GPU (NVIDIA GPU with at least 16GB, preferably 24GB RAM) and run MONAILabel server on it. You can configure and run the server by using the commands described <a href="https://github.com/Project-MONAI/MONAILabel#installation">here</a>. If the segmentation task is simple (for example, you need to segment large structure with simple shape and good contrast to surrounding structures) then you may use existing models developed for similar segmentations. However, if your segmentation task is not easy then most likely you need to experiment with network architecture and training parameters. This does not necessarily require programming background, but it could help if you can find someone who has some experience in deep learning to help you.</p>
<p>You might even find someone in the Slicer community who would be interested to collaborate. What is the clinical application - surgical planning? what procedure? What structures would you like to segment?</p>

---

## Post #5 by @pieper (2022-06-19 13:37 UTC)

<p>Also <a class="mention" href="/u/celina_hallal">@Celina_Hallal</a> you may look at what <a class="mention" href="/u/rbumm">@rbumm</a> has been doing.  He’s also a surgeon who has been working through MONAI Label and getting good results for his application.</p>
<aside class="quote quote-modified" data-post="88" data-topic="21063">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-start-with-monailabel-for-new-models/21063/88">How to start with monailabel for new models</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    After great meetings with <a class="mention" href="/u/diazandr3s">@diazandr3s</a> we were able to set the MONAILabel lung segmentation up from scratch, train a model, and autosegment lungs and airways. 
Windows: We recommend doing this in Windows 11 using Powershell. 
<a href="https://docs.monai.io/projects/label/en/latest/installation.html#windows">Follow the instructions from the ML Github</a> to install the prerequisites and ML itself. 
All in the above link: 

Test that CUDA is available.
Fork MONAILabel from Github
Download ML radiology app
Download lung dataset

Use Slicer 5.1 and ML extension 
We found that the Deepe…
  </blockquote>
</aside>


---

## Post #6 by @Celina_Hallal (2022-06-19 19:58 UTC)

<p>Great, guys! Thanks a lot!</p>

---

## Post #7 by @Celina_Hallal (2022-06-19 20:56 UTC)

<p>I’m trying to do better liver segmentations for surgical planning. I’ve been segmenting some cases manually. Most of the pre-trained models I’ve tried weren’t as good as I would need, mostly with surrounding structures like IVC, stomach, and spleen.</p>
<p>I’m a surgical resident from a Brazilian University with interest in Liver Surgery. Last year we had one difficult case that could benefit from a 3D model, and I found it was almost impossible to do it easily using the resources we had at our Radiology Dept…</p>
<p>Since then, I’ve been playing with some cases and studying a bit. Some of my attendings loved the idea, and I’m trying to do something with it for my conclusion thesis (Residency program thesis here in Br is not a big deal, generally we do something we can use later in M.S.c - things work a little different here).</p>
<p>My first idea was to do something like you and Yeo did in " Utility of 3D Reconstruction of 2D Liver Computed Tomography/ Magnetic Resonance Images as a Surgical Planning Tool for Residents in Liver Resection Surgery". But later we discussed and we wouldn’t have plenty of time to do that.</p>
<p>Besides, recently we had some trouble with our preoperative liver volumetry. So, my idea is to create an workflow to make parenchyma and vessel segmentation easier and more reliable (something a busy surgical resident that doesn’t even know what is “DICOM”, “Python” and “Neural networks” can do). I would train a model with a dataset, then try it with our pre and postoperative cases, both oncological and pre-LDLT.</p>
<p>But, as I said earlier, I’m a noob with little programming background (and most of my MD colleagues are way worse). So I may be wandering a bit… But, as they say, the best way to learn is doing it (and failing sometimes <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"> ). Tomorrow I will have a meeting with a guy from the medical physics at the hospital about my project and about using some of the Radiology Dept. computer as server.</p>
<p>Thank you a lot!!!</p>

---

## Post #8 by @pieper (2022-06-19 21:29 UTC)

<p>Thanks for providing more context, it sounds like a good project and it hopefully we can help out and answer any questions that come up in your work.  Be sure to check out some of the other ongoing work related to liver segmentation and surgery planning.  I’m sure additional testing and clinical input would be helpful.</p>
<p><a href="https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/SlicerLiver/">https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/SlicerLiver/</a></p>
<p><a href="https://discourse.slicer.org/t/new-extension-development-plan-self-supervised-learning-and-liver-segmentation/23714">https://discourse.slicer.org/t/new-extension-development-plan-self-supervised-learning-and-liver-segmentation/23714</a></p>

---
