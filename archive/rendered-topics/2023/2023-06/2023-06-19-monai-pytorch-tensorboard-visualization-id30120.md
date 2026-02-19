---
topic_id: 30120
title: "Monai Pytorch Tensorboard Visualization"
date: 2023-06-19
url: https://discourse.slicer.org/t/30120
---

# MONAI_Pytorch Tensorboard_Visualization

**Topic ID**: 30120
**Date**: 2023-06-19
**URL**: https://discourse.slicer.org/t/monai-pytorch-tensorboard-visualization/30120

---

## Post #1 by @Spiros_Karkavitsas (2023-06-19 12:57 UTC)

<p>Hello,</p>
<p>I am running MONAI Label using the radiology app. However, I would like to ask if someone knows here how to visualize the results of the training I am doing using MONAI with TensorBoard.</p>
<p>Thank you for your time</p>
<p>Spiros</p>

---

## Post #2 by @rbumm (2023-06-19 13:38 UTC)

<p>You know that you can access the status of your running MonaiLabel server by calling <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a> in a browser on that server system and that is not enough information?</p>

---

## Post #3 by @Spiros_Karkavitsas (2023-06-19 15:18 UTC)

<p>Hello</p>
<p>Thank you for your immediate response<br>
I ran a training task, went into a tab and copied your address , but the page cannot be reached.</p>
<p>To be more precise, I use the radiology app to segment the fat tissue out of 3D volumes. I have plugged in the MONAI app in Slicer and using the default Hyperparameters for the training.<br>
Also, I am running the MONAI in a Docker.</p>
<p>What I want to visualize are the training curves such as training loss ,validation loss graphs.</p>

---

## Post #4 by @rbumm (2023-06-19 15:28 UTC)

<p>You seem to be starting a revolution in adipose tissue.</p>
<p>So do you start your MONAILabel server with something like (in a shell):</p>
<pre><code class="lang-auto">monailabel start_server --app MONAILabel/sample-apps/radiology --studies c:/Data/Task06_Lung/imagesTr --conf models segmentation
</code></pre>
<p>?</p>
<p>Then the monailabel output should tell you which port it uses, use that port for your localhost:xxxx URL</p>
<aside class="quote no-group" data-username="Spiros_Karkavitsas" data-post="3" data-topic="30120">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/spiros_karkavitsas/48/18224_2.png" class="avatar"> Spiros_Karkavitsas:</div>
<blockquote>
<p>What I want to visualize are the training curves such as training loss ,validation loss graphs.</p>
</blockquote>
</aside>
<p>My GPT-4 consultation revealed:</p>
<p><a href="https://chat.openai.com/share/d4a4b141-af01-450e-ad0a-4095deed8b09" class="onebox" target="_blank" rel="noopener nofollow ugc">https://chat.openai.com/share/d4a4b141-af01-450e-ad0a-4095deed8b09</a><br>
Does this help?</p>
<p>Maybe <a class="mention" href="/u/diazandr3s">@diazandr3s</a> can comment too.</p>

---

## Post #5 by @Spiros_Karkavitsas (2023-06-19 15:53 UTC)

<p>Yes, exactly like this .</p>
<p>Very helpful answer, thank you .</p>
<p>I saw your GTP consultation and is helpful too. I suppose, the modifications must be made on the radiology / lib/ trainers / segmentation.py file.</p>
<p>Thank you again for your immediate responses</p>

---

## Post #6 by @Spiros_Karkavitsas (2023-06-20 09:30 UTC)

<p>Hello again,</p>
<p>Ok, I start my MONAILabel server with a command line like you described  :<br>
monailabel start_server --app /workspace/radiology --studies /workspace/Training/fat --conf models segmentationfat --conf multi_gpu true</p>
<p>Then by putting the correct port via web browser I have this :</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9eae9e4bbe01d8a61787277f560cc7ed682e0991.jpeg" data-download-href="/uploads/short-url/mDLyCvLrq0yFYOWdU2RN0iVUN7b.jpeg?dl=1" title="question_monai" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9eae9e4bbe01d8a61787277f560cc7ed682e0991_2_334x250.jpeg" alt="question_monai" data-base62-sha1="mDLyCvLrq0yFYOWdU2RN0iVUN7b" width="334" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9eae9e4bbe01d8a61787277f560cc7ed682e0991_2_334x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9eae9e4bbe01d8a61787277f560cc7ed682e0991_2_501x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9eae9e4bbe01d8a61787277f560cc7ed682e0991_2_668x500.jpeg 2x" data-dominant-color="F1F6F8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">question_monai</span><span class="informations">1585×1186 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>From this web interface I cannot take the training curves (image below) , and optimise the number of epochs (early stopping)</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/830b609fc41fd761c7751f651a0f3e06ad4b316d.jpeg" alt="question_monai2" data-base62-sha1="iHgVkspCuiyz3tOoiKBPSrdtMh7" width="340" height="215"></p>
<p>This is my goal in short. So far, for the fat delineation I use 50 number of epochs (default by MONAI). I want to avoid overfitting.</p>
<hr>
<p>Regarding the ChatGPT conversation :</p>
<p>These types of modifications</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f52715f6a407dda02f74a78d3adbf354ccd4b4b.jpeg" data-download-href="/uploads/short-url/dBfZxYDWxwG4J6iCvy9M7dSsDW3.jpeg?dl=1" title="question_monai2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f52715f6a407dda02f74a78d3adbf354ccd4b4b_2_263x249.jpeg" alt="question_monai2" data-base62-sha1="dBfZxYDWxwG4J6iCvy9M7dSsDW3" width="263" height="249" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f52715f6a407dda02f74a78d3adbf354ccd4b4b_2_263x249.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f52715f6a407dda02f74a78d3adbf354ccd4b4b_2_394x373.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f52715f6a407dda02f74a78d3adbf354ccd4b4b_2_526x498.jpeg 2x" data-dominant-color="0E0E10"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">question_monai2</span><span class="informations">605×574 83.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I do not know , in which script I have to do these modifications. I suppose in the .py file which is contained in the ‘’/radiology/lib/configs/segmentationfat.py’’ path?</p>
<p>Sorry for the long answer, kind of newbie here, so that is why I want to explain everything.</p>
<p>Thank you</p>

---

## Post #7 by @mangotee (2023-06-20 09:57 UTC)

<p>Hi Spiros,<br>
MONAI Label server automatically splits your dataset into a train and validation set - the default split is at 20% of the dataset, but you can manually change that split percentage or you can even define your own fixed validation set.<br>
Overfitting is avoided during training by only storing model weights if the validation Dice improves upon the previous iteration.<br>
You can still choose to visualize a Tensorboard on the current training run. Just start a Tensorboard and point it to the directory where your model is. In my radiology-app this looks something like this:<br>
<code>/path/to/apps/radiology/model/deepedit_dynunet/train_01</code><br>
There, you can see the Tensorboard folders <code>events_*</code> for each training run.</p>

---

## Post #8 by @Spiros_Karkavitsas (2023-06-20 10:43 UTC)

<p>Hello and thank you for your answer and time.</p>
<p>Yes, I know where the tensorboard files with a similar path like yours <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Okay, so before training do I type in the terminal a command like this :</p>
<p>‘’ tensorboard --logdir=path/to/log_directory ‘’ where the path points to the tensorboard files ?</p>
<p>And later type in the web : <a href="http://localhost:6006/" rel="noopener nofollow ugc">http://localhost:6006/</a> to monitor the process?</p>
<p>Thank you again,</p>
<p>Spiros</p>

---

## Post #9 by @mangotee (2023-06-20 12:29 UTC)

<p>Hi, yes, exactly, you can start the Tensorboard before or during training, pointing the logdir to the model folder, and it’ll be in the browser on port 6006 (either localhost or remote IP address). Let us know whether this works! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #10 by @Spiros_Karkavitsas (2023-06-20 12:51 UTC)

<aside class="quote no-group" data-username="mangotee" data-post="7" data-topic="30120">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/c57346/48.png" class="avatar"> mangotee:</div>
<blockquote>
<p>/path/to/apps/radiology/model/deepedit_dynunet/train_01</p>
</blockquote>
</aside>
<p>Ok, I understood the concept. Since to run MONAI I am connecting to a server I did the following:</p>
<p>Installed the tensorflow to my server and when I run the command</p>
<p>tensorboard --logdir=/path/to/project/radiology/model/segmentationfatex/train_01</p>
<p>I get the following message : tensorboard: command not found</p>
<p>Which means that I have to find the path of tensorboard to run it. Correct?</p>
<p>However, when I execute the command : pip show tensorboard in the command prompt I get the location of tensorboard like this:</p>
<p><strong>/home/MRuser/.local/lib/python3.8/site-packages</strong></p>
<p>Then I copy paste the path and run again the command . However, the output is :</p>
<p><strong>-bash: /home/MRuser/.local/lib/python3.8/site-packages/tensorboard: Is a directory</strong></p>
<p>As I understand I will have to find the path of the executable file to run it. But the location was given, why does it not run?</p>

---

## Post #11 by @mangotee (2023-06-20 13:06 UTC)

<p>Good question. How did you install monailabel? Via pip into a local python env?<br>
If so, you may have to still install tensorboard? Instructions can be found here: <a href="https://pytorch.org/tutorials/recipes/recipes/tensorboard_with_pytorch.html" class="inline-onebox" rel="noopener nofollow ugc">How to use TensorBoard with PyTorch — PyTorch Tutorials 2.0.1+cu117 documentation</a></p>
<p>This would be weird though, because if you pip install monailabel, it installs monai-core along with tensorboard: <a href="https://github.com/Project-MONAI/MONAILabel/blob/main/requirements.txt#L12" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel/requirements.txt at main · Project-MONAI/MONAILabel · GitHub</a><br>
Perhaps, you then need to find the binary and add its location to your <code>PATH</code> variable?</p>
<p>By the way, to avoid such environment and installation issues, I usually recommend everyone to run monailabel from a docker container, which can be started from one of the public image tags:<br>
<a href="https://hub.docker.com/r/projectmonai/monailabel/tags" class="onebox" target="_blank" rel="noopener nofollow ugc">https://hub.docker.com/r/projectmonai/monailabel/tags</a><br>
These images come with Tensorboard pre-installed, it can be run from console, and generally, the entire setup is very “clean”. It is also much easier to update or switch to a different monailabel version.</p>

---

## Post #12 by @rbumm (2023-06-20 13:15 UTC)

<p>In Windows, if “monailabel” command is not found from a powershell, this kind of thing solves by adding</p>
<pre><code class="lang-auto">$Env:PATH += ";C:\Users\yourname\MONAILabel\monailabel\scripts"
</code></pre>
<p>You could add a conda environment in your Linux and conda install tensorboard.</p>

---

## Post #13 by @Spiros_Karkavitsas (2023-06-20 13:35 UTC)

<p>Okay, i run the MONAI using docker (I start a MONAI Container). I connect to this server via the command prompt in my local machine.</p>
<p>Okay, after chatting with GPT I think I know the issue :</p>
<p>After, going to the directory where the tensorboard , I searched for the files and I found the main.py file which might be the one I am looking for. Thus, I entered the command line :</p>
<p><strong>~/.local/lib/python3.8/site-packages/tensorboard$ python3 main.py --logdir=logdir=/ptojectdata/path /to/radiology/model/segmentationfat/train_01</strong></p>
<p>and I get as an output this :</p>
<p>/home/MRuser/.local/lib/python3.8/site-packages/tensorboard_data_server/bin/server: /lib/x86_64-linux-gnu/libc.so.6: version <code>GLIBC_2.33' not found (required by /home/MRUser/.local/lib/python3.8/site-packages/tensorboard_data_server/bin/server) /home/MRuser/.local/lib/python3.8/site-packages/tensorboard_data_server/bin/server: /lib/x86_64-linux-gnu/libc.so.6: version </code>GLIBC_2.34’ not found (required by /home/MRuser/.local/lib/python3.8/site-packages/tensorboard_data_server/bin/server)<br>
/home/MRuser/.local/lib/python3.8/site-packages/tensorboard_data_server/bin/server: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.32’ not found (required by /home/mriuser/.local/lib/python3.8/site-packages/tensorboard_data_server/bin/server)</p>
<p>Then I use this : ldd --version | head -n to see the version and the answer is :</p>
<p><strong>ldd (Ubuntu GLIBC 2.31-0ubuntu9.9) 2.31</strong></p>
<p>which is not the required GLIBC version as I understand.</p>
<p>Lastly, the binary path in your case, where is it?<br>
Thank you again</p>

---

## Post #14 by @Spiros_Karkavitsas (2023-06-20 14:17 UTC)

<p>Maybe a solution would be to run the tensorboard to my local machine and copy the tensorboard log files from the server to my local machine instead?</p>

---

## Post #15 by @rbumm (2023-06-20 18:03 UTC)

<p>Please keep us updated and post the complete solution here.</p>

---

## Post #16 by @Spiros_Karkavitsas (2023-06-21 09:55 UTC)

<p>Okay, I finally managed to launch Tensorboard using my local machine.</p>
<p>More specifically, I installed tensorflow in my laptop and downloaded the log file from the server to my laptop.</p>
<p>Then I used the command line:<br>
tensorboard --logdir=C:\Users\path\to\events_20230620_192239</p>
<p>And it worked.</p>
<p>However, in tensorboard I get only the <strong>train accuracy</strong>, <strong>train loss</strong> and <strong>validation accuracy</strong>. But not the validation loss.</p>
<p>Thus, I suspect by default MONAI do not calculate this. Correct?</p>

---

## Post #17 by @diazandr3s (2023-06-22 00:23 UTC)

<p>Hi <a class="mention" href="/u/spiros_karkavitsas">@Spiros_Karkavitsas</a>,</p>
<p>There is no validation loss because MONAI Label doesn’t use the validation set for training.</p>
<p>Hope this makes sense,</p>

---

## Post #18 by @Spiros_Karkavitsas (2023-07-12 14:12 UTC)

<p>Hello after a long time and thank you in advance for your helpful reply.</p>
<p>However, I got some results using MONAI Label for automatic body fat segmentation in axial MR slices.</p>
<p>So far, the performance model (displayed from Slicer interface) is 89% which is basically the dice similarity for the validation data.</p>
<p>However, I used new testing data (not seen by the model) to evaluate the Dice Similarity for this group of data. I used 6 new patients and the testing Dice Similarity was 98% which is a lot higher than the corresponding validation metric.</p>
<p>Thus, I believe I will have to regroup my data to avoid bias selection.</p>
<p>My question is on how the MONAI selects the validation data ? I know the default settings is the 20% of the training data used for this calculation. But how can I change which data is used for this?</p>
<p>Thank you in advance for your time.</p>

---
