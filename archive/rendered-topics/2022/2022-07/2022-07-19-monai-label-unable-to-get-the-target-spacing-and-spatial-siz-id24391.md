---
topic_id: 24391
title: "Monai Label Unable To Get The Target Spacing And Spatial Siz"
date: 2022-07-19
url: https://discourse.slicer.org/t/24391
---

# MONAI Label - unable to get the target_spacing and spatial_size using heuristic_planner

**Topic ID**: 24391
**Date**: 2022-07-19
**URL**: https://discourse.slicer.org/t/monai-label-unable-to-get-the-target-spacing-and-spatial-size-using-heuristic-planner/24391

---

## Post #1 by @hourglassnam (2022-07-19 12:00 UTC)

<p>Dear Slicer community,<br>
I have a few minor questions and one big question on MONAI Label as I try to train from scratch.<br>
So let me start by stating the big question first.<br>
Because I do not know the target_spacing and spatial_size, I tried using the --conf heuristic_planner true command as mentioned in this <a href="https://discourse.slicer.org/t/how-to-start-with-monailabel-for-new-models/21063/69">forum</a>.</p>
<blockquote>
<p>monailabel start_server --app /sample-apps/histology --studies /datasets/Task11_BR/imagesTr --conf models deepedit --conf heuristic_planner true  --port 8000 --host 127.0.0.1</p>
</blockquote>
<p>When I use the command, it gives me the following error message.</p>
<blockquote>
<p>[2022-07-19 19:44:29,031] [11632] [MainThread] [INFO] (monailabel.utils.others.planner:35) - Reading datastore metadata for heuristic planner…<br>
0%|                                                                                                                                                                                     | 0/10 [00:00&lt;?, ?it/s]<br>
[2022-07-19 19:44:29,812] [11632] [MainThread] [ERROR] (uvicorn.error:119) - Traceback (most recent call last):<br>
File “C:\ProgramData\Anaconda3\lib\site-packages\starlette\routing.py”, line 635, in lifespan<br>
async with self.lifespan_context(app):<br>
File “C:\ProgramData\Anaconda3\lib\site-packages\starlette\routing.py”, line 530, in <strong>aenter</strong><br>
await self._router.startup()<br>
File “C:\ProgramData\Anaconda3\lib\site-packages\starlette\routing.py”, line 612, in startup<br>
await handler()<br>
File “USERSITE\MONAILabel\monailabel\app.py”, line 103, in startup_event<br>
instance = app_instance()<br>
File “USERSITE\MONAILabel\monailabel\interfaces\utils\app.py”, line 51, in app_instance<br>
app = c(app_dir=app_dir, studies=studies, conf=conf)<br>
File “USERSITE\MONAILabel\sample-apps\histology\main.py”, line 89, in <strong>init</strong><br>
super().<strong>init</strong>(<br>
File “USERSITE\MONAILabel\monailabel\interfaces\app.py”, line 90, in <strong>init</strong><br>
self._datastore: Datastore = self.init_datastore()<br>
File “USERSITE\MONAILabel\sample-apps\histology\main.py”, line 100, in init_datastore<br>
self.planner.run(datastore)<br>
File “USERSITE\MONAILabel\monailabel\utils\others\planner.py”, line 58, in run<br>
if mtdt[“pixdim”][4] &gt; 0:<br>
KeyError: ‘pixdim’</p>
<p>[2022-07-19 19:44:29,813] [11632] [MainThread] [ERROR] (uvicorn.error:56) - Application startup failed. Exiting.</p>
</blockquote>
<p>The histology mentioned above is the copy of the radiology app I created to change labels.<br>
The server works fine without the heuristic planer, and I could not figure out why this might be.<br>
How can I figure out the target_spacing and spatial_size?<br>
Is there any other way?</p>
<p>And here are my minor curiosities.</p>
<ol>
<li>The data I used were in *.nrrd format. At first, I saved the volumes as Seg##.nrrd and the segmentations as Seg##.seg.nrrd. In return, it gave me the following message. [2022-07-19 14:23:36,675] [13136] [MainThread] [WARNING] (monailabel.datastore.local:583) - IGNORE:: No matching image exists for ‘Seg01.seg’ to add [Seg01.seg.nrrd] I figured this could be due to the .seg part of the naming, so I changed the volume file names to include .seg, just like the segmentation files. Am I allowed to do this? Will this cause any problems during the training process?</li>
<li>Also, when I copied the radiology folder to make the histology folder, the server did not start right when I deleted the segmentation_spleen subclass. I was just curious why this may happen.</li>
<li>Lastly, the changes I made, such as labels and use_pretrained_model false, were not reflected until I made a separate histology folder. Is there any reason behind this?</li>
</ol>

---

## Post #2 by @rbumm (2022-07-19 12:24 UTC)

<p>There is a new and interesting <a href="https://www.youtube.com/watch?v=Jy5VTqX4_jo&amp;t=8s">MONAI Label pathology video</a> available on Youtube. Does this solve your problem?</p>
<p>In your special case</p>
<pre><code class="lang-auto">monailabel start_server --app /sample-apps/histology --studies /datasets/Task11_BR/imagesTr --conf models deepedit 
</code></pre>
<p>would probably work out of the box.</p>
<p>Concerning the other questions could maybe <a class="mention" href="/u/diazandr3s">@diazandr3s</a> comment?</p>

---

## Post #3 by @hourglassnam (2022-07-19 13:28 UTC)

<p>Hello!! Thank you so much for your reply!</p>
<p>The file I am working with is a micro-CT of a plant seed sample, and I am trying to separate the morphology inside to get the volumetric data of each part.</p>
<p>So the pathology app did not fit my purpose.</p>
<p>I needed to change the labels and disable the use_pretrained_model so it would not use the given labels.</p>
<p>When I changed the labels and disable the use_pretrained_model so it would not use the given labels in “MONAILabel/monailabel/deepedit/multilabel/transforms.py” and “MONAILabel/sample-apps/radiology/lib/configs/deepedit.py”, the changes weren’t reflected on the 3D Slicer and gave me the original label such as spleen, liver and etc.</p>
<p>That is why I had to copy the radiology folder and make a new one.</p>
<p>I think the term histology may have caused the confusion.</p>
<p>Sorry about that.</p>
<p>I started the server(big thanks to you) and successfully changed the labels using the given information from the <a href="https://discourse.slicer.org/t/how-to-start-with-monailabel-for-new-models/21063/64">forum</a>.</p>
<blockquote>
<p>$Env:PATH += “;C:\Users\njy95\MONAILabel\monailabel\scripts”</p>
<p>monailabel start_server --app C:/Users/njy95/MONAILabel/sample-apps/histology --studies C:/Users/njy95/datasets/Task11_BR/imagesTr --conf models deepedit --port 8000 --host 127.0.0.1</p>
</blockquote>
<p>However, I don’t know my dataset’s target spacing and spatial size for the pretraining process.</p>
<p>To be honest, I don’t clearly understand what target_spacing and spatial_size are. I am assuming this is different from the actual pixel value and was hoping that the heuristic planner would give be recommended value.</p>
<p>That is why I used --conf heuristic_planner true, but it did not work.</p>
<p>Can you give me a advise on what the problem could be?</p>

---

## Post #4 by @rbumm (2022-07-19 16:03 UTC)

<aside class="quote no-group" data-username="hourglassnam" data-post="3" data-topic="24391">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hourglassnam/48/11796_2.png" class="avatar"> hourglassnam:</div>
<blockquote>
<p>micro-CT of a plant seed sample</p>
</blockquote>
</aside>
<p>That sounds interesting <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>I can only describe our recent approach, <a class="mention" href="/u/diazandr3s">@diazandr3s</a> from the MONAI dev team or others will hopefully provide more technical background. As I understood the parameters relate to resizing ML training data in RAM.</p>
<p>For the training of a lung &amp; airway model from CT we have used:</p>
<pre><code class="lang-auto">self.target_spacing = (1.0, 1.0, 1.0)  # target space for image
</code></pre>
<p>was set to 1.0 and never changed,</p>
<pre><code class="lang-auto">self.spatial_size = (128, 128, 64)  # train input size
</code></pre>
<p>was initially set to (32,32,32) and later increased by multiplying those values with 2 and 3. Higher values require more video RAM and increased training time, but changed the lung inference from a minecrafty to a more realistic resolution and look. Our goal is to do the next training on a cloud server with (256,256,256) settings. You should probably start out with (32,32,32).</p>
<p>Hope that helps.</p>

---

## Post #5 by @diazandr3s (2022-07-19 22:38 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a>, thanks for sharing your experience <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
<a class="mention" href="/u/hourglassnam">@hourglassnam</a>, thanks for opening this thread. It is an interesting use case for MONAI Label.<br>
The heuristic planner uses image metadata and available GPU memory to define spacing and image size for training the deep learning model. It seems the images you’re using don’t have “pixdim” in the metadata.<br>
As <a class="mention" href="/u/rbumm">@rbumm</a> suggested, you could start with a spacing of <code>(1.0, 1.0, 1.0)</code> and spatial size to <code>(128, 128, 64)</code> and see how that goes, or even the default values as I show in this video: <a href="https://www.youtube.com/watch?v=3HTh2dqZqew&amp;list=PLtoSVSQ2XzyD4lc-lAacFBzOdv5Ou-9IA&amp;index=3" class="inline-onebox" rel="noopener nofollow ugc">MONAI Label - Training from Scratch - YouTube</a></p>
<p>You could explore other values after seeing the results you get.</p>
<p>I’m off this week with limited access to the internet. So I’m slow replying. If you want to get help faster, I’d suggest you open a discussion directly in the MONAI Label repo: <a href="https://github.com/Project-MONAI/MONAILabel/discussions" class="inline-onebox" rel="noopener nofollow ugc">Discussions · Project-MONAI/MONAILabel · GitHub</a></p>

---
