---
topic_id: 21063
title: "How To Start With Monailabel For New Models"
date: 2021-12-14
url: https://discourse.slicer.org/t/21063
---

# How to start with monailabel for new models

**Topic ID**: 21063
**Date**: 2021-12-14
**URL**: https://discourse.slicer.org/t/how-to-start-with-monailabel-for-new-models/21063

---

## Post #1 by @muratmaga (2021-12-14 22:55 UTC)

<p>We would like to use monaiLabel to generate/refine existing segmentation of fetal mice. Given that there is no pre-existing model to do that, how does one go about this. We have about 20 or so already segmented scans.</p>
<p>At some point monaiLabel was very frequently updated. Due to the environment we work, frequent version changes and code updates is not feasible for us. Is it stable enough to use in a production environment on a regular basis?</p>

---

## Post #2 by @pieper (2021-12-14 23:44 UTC)

<p>I haven’t tried it all myself, but here are recent materials about MONAILabel with Slicer for segmentation.  We are arranging to hold a workshop on this material on January 12, 2022, 2-4pm EST as part of <a href="https://projectweek.na-mic.org/PW36_2022_Virtual/">project week</a> where at least a few projects will try to apply it.</p>
<p><a href="https://catalog.us-east-1.prod.workshops.aws/v2/workshops/ff6964ec-b880-45d4-bc1e-468b0c7fa854/en-US/" class="onebox" target="_blank" rel="noopener">https://catalog.us-east-1.prod.workshops.aws/v2/workshops/ff6964ec-b880-45d4-bc1e-468b0c7fa854/en-US/</a></p>

---

## Post #3 by @rbumm (2021-12-15 07:06 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> Steve is that date fixed? Not one week later because PW is from Jan 17th ?  Thanks</p>

---

## Post #4 by @pieper (2021-12-15 13:43 UTC)

<p>Yes, we scheduled it the week before Project Week on purpose so that we could block out 2 hours for it without cutting into other work.  Also we wanted people to get up to speed in advance so that they could apply it to their own data during PW.</p>

---

## Post #5 by @muratmaga (2021-12-15 21:29 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I haven’t tried it all myself, but here are recent materials about MONAILabel with Slicer for segmentation. We are arranging to hold a workshop on this material on January 12, 2022, 2-4pm EST as part of <a href="https://projectweek.na-mic.org/PW36_2022_Virtual/">project week </a> where at least a few projects will try to apply it.</p>
</blockquote>
</aside>
<p>Thanks Steve.  I managed to get the server running locally at some point, what I was actually for instructions on how to get started with a new model, as opposed to using a pretrained model (e.g., spleen segmentation). All the documentation I found so far refers to using existing models (e.g., <a href="https://docs.monai.io/projects/label/en/latest/quickstart.html" class="inline-onebox">Quickstart — MONAI Label 0.8.1 Documentation</a>)</p>

---

## Post #6 by @mangotee (2021-12-16 00:22 UTC)

<p>Hi Murat! Good point, the existing documentation so far assumes a pretrained model. However, in my case this was not a problem - I used MONAILabel for inner ear structure segmentation in microCT (128^3 cubic volumes). I started with 0 annotated volumes, but nonetheless, I used the pre-trained left-atrium DeepEdit model (different anatomy AND modality), because 1) I wanted a quick start without much fiddling with the DeepEdit app code, and 2) I thought it might beneficial that the early encoder layers already have some “clue” about atomic 3D patch geometries. Not sure whether point 2) actually was beneficial (didn’t try the corollary), but to my delight, the DeepEdit’s UNet model quickly started snapping to the anatomy. Already after 2-3 manual annotations, I got surprisingly good segmentation guesses by the model. In your case, you have already 20 pre-annotated volumes. You can indicate this in the <code>datastore.json</code> file. Upon first start of DeepEdit, instead of annotating right-away, you could manually trigger the first pre-training. The resulting model might already be quite “valuable”. Let me know if I can help.</p>

---

## Post #7 by @diazandr3s (2021-12-16 02:33 UTC)

<p>Hi <a class="mention" href="/u/muratmaga">@muratmaga</a>,</p>
<p>There are two ways of using a MONAI Label App (i.e. <a href="https://github.com/Project-MONAI/MONAILabel/tree/main/sample-apps/deepedit" rel="noopener nofollow ugc">DeepEdit</a>, <a href="https://github.com/Project-MONAI/MONAILabel/tree/main/sample-apps/deepgrow" rel="noopener nofollow ugc">DeepGrow</a>, <a href="https://github.com/Project-MONAI/MONAILabel/tree/main/sample-apps/segmentation" rel="noopener nofollow ugc">Segmentation</a>) without downloading/using the available pretrained models.</p>
<p>The first approach is adding the flag --conf use_pretrained_model false when starting the server. This means you should write something like this:</p>
<blockquote>
<p>monailabel start_server -a /PATH_2_APP/ -s /PATH_2_IMAGES/ --conf use_pretrained_model false</p>
</blockquote>
<p>The second approach and the secure one is by changing the flag directly in the main file of your App. So, if you want to use a DeepEdit App, change <a href="https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/deepedit/main.py#L99" rel="noopener nofollow ugc">this line</a> to false.</p>
<p>With regards to the already annotated images, there are two things to consider. First, images and corresponding labels should have the same name, and secondly, already annotated labels should be placed inside the subfolder <strong>/folder_images/labels/final</strong>.</p>
<p>Something like this</p>
<pre><code class="lang-auto">folder_images:
              - image_1
              - image_2
              - image_3
              labels:
                       final:
                             - image_1
                             - image_2
</code></pre>
<p>If this is not clear, in slide 9 of this <a href="https://docs.google.com/presentation/d/19YWH7J-WBGl9MLfrd8eybJ_Bhwio7lXQjsM8EKcOOhk/edit?usp=sharing" rel="noopener nofollow ugc">presentation</a> I did an example of how to organise the images and already annotated labels before starting the server.</p>
<p>Just out of curiosity, are the scans 3D? Which MONAI Label App are you planning to use (i.e. DeepEdit, DeepGrow, Segmentation)? How many segments have the labels? Is this a single label or multilabel task?</p>
<p>As <a class="mention" href="/u/mangotee">@mangotee</a> nicely commented, please don’t hesitate to ask, we’re happy to help <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #8 by @muratmaga (2021-12-16 03:37 UTC)

<p>Thanks <a class="mention" href="/u/diazandr3s">@diazandr3s</a>. Yes, images are 3D scans of fetal mice, and labels are multilabel (about ~30 labels). Volumes are about 200x400x400 voxels. Labels and volumes have identical prefix, but different formats. Volumes are in NRRD and labelmaps are in nii.gz (mostly because we want to keep the labelmaps compressed, but not necessarily the volumes). Is that an issue? Or do they have both same format?</p>

---

## Post #9 by @mau_igna_06 (2021-12-16 11:12 UTC)

<p>Hi <a class="mention" href="/u/diazandr3s">@diazandr3s</a>. Thank you for interesting work and your contribution to the Slicer community.</p>
<p>I have a question regarding MONAI-Label: Let’s say I have a few dozens of CTs of both feet, I have segment of the talus bone for each foot so there are two segments (labels) per CT, and I have a frame that defines the orientation and position (i.e. a linear transform) of each talus.</p>
<p>One way to imagine the usefulness of this transform information is that if you apply the inverse of this transform to the talus-segment you would have a zero-centered talus with a normalized orientation for comparing measurements between taluses of different CTs. And after this you can also mirror left-and-right for left-taluses and after that all the taluses (right ones and left-mirrored ones) would be oriented so that the lateral side of the bone is on the right.</p>
<p>Would it be possible to feed MONAI-Label the transform information, so when the model is trained per input CT it returns a label for each talus and the transform defining its position and orientation?</p>

---

## Post #10 by @diazandr3s (2021-12-16 11:50 UTC)

<p>This is a nice use-case for MONAI Label <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
Do you mean 30 segments in each label? Just for me to understand, which are the segments in each 3D scan?<br>
If the task is multilabel like <a href="https://www.synapse.org/#!Synapse:syn3193805/wiki/217789" rel="noopener nofollow ugc">this one</a>, then I recommend you to use the <a href="https://github.com/Project-MONAI/MONAILabel/tree/main/sample-apps/deepedit_multilabel" rel="noopener nofollow ugc">Multilabel DeepEdit App</a>.<br>
My suggestion is to not mix image/label formats. Is it difficult to have both images and labels in the same format?</p>

---

## Post #11 by @diazandr3s (2021-12-16 11:57 UTC)

<p>Thanks, <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a>!<br>
Yes, you should be able to use MONAI Label for this task. You can easily define transforms that can be applied to the images for training or performing inference.<br>
I’m happy to show you how you can do this. For instance, I’m currently creating custom transforms for a multilabel task. In <a href="https://github.com/Project-MONAI/MONAILabel/blob/multilabel_deepedit_preds/sample-apps/deepedit_multilabel_with_preds/lib/transforms.py#L29" rel="noopener nofollow ugc">here</a> I’m defining those transforms that I used for my App.</p>

---

## Post #12 by @muratmaga (2021-12-16 16:08 UTC)

<aside class="quote no-group" data-username="diazandr3s" data-post="10" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/diazandr3s/48/9973_2.png" class="avatar"> diazandr3s:</div>
<blockquote>
<p>Do you mean 30 segments in each label? J</p>
</blockquote>
</aside>
<p>Yes, it is a multi-label task exactly like the one you show, only in mice. We keep the labels and volumes together for our current workflow, so keeping them in separate formats with the same file name is a nice trick. It has gives us the benefit of compressing the labels (which does really well). But it is not a big deal, I can switch them to same format.</p>
<p>I will give a try, thanks for your pointers.I am excited to try.</p>

---

## Post #13 by @muratmaga (2021-12-16 20:59 UTC)

<p><a class="mention" href="/u/diazandr3s">@diazandr3s</a><br>
actually I got stuck at the beginning currently. I am following these instructions<br>
<a href="https://docs.monai.io/projects/label/en/latest/installation.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://docs.monai.io/projects/label/en/latest/installation.html</a></p>
<p>and at the monailabel --help step I am getting</p>
<p>maga@magalab-ML:~/.local/bin$ ./monailabel<br>
Using PYTHONPATH=/home/maga:<br>
Python 2.7.18<br>
/usr/bin/python: No module named monailabel</p>
<p>It is not finding the python3. I tried setting PYTHONPATH=/usr/bin/python3 in the shell prior to executing monailabel, but that didn’t have any effect.</p>
<p>Any suggestions</p>

---

## Post #14 by @muratmaga (2021-12-16 21:08 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="13" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>PYTHONPATH=/usr/bin/python3</p>
</blockquote>
</aside>
<p>The other issue I am having, it is not clear from this instruction set that whether the installation needs to be done as a priviledged user or it is possible to run it as normal user. I hardcoded the python3 path and now I can use the monailabel file, but when I do<br>
monailabel apps --download --name deepedit --output apps</p>
<p>it tries to write in /usr/monailabel, which as a normal user I can’t. Is there a major config file where I can specify these? Or all of these instructions assume that installation is done as the root (or admin)?</p>

---

## Post #15 by @muratmaga (2021-12-16 21:48 UTC)

<p>This is where I stand as a normal user install.</p>
<ol>
<li>Hard coded the monailabel script to<br>
PYEXE=python3</li>
<li>After this, when I type:<br>
<strong>~/.local/bin/monailabel apps --prefix ~/.local</strong><br>
this is what I get</li>
</ol>
<pre><code class="lang-auto">Using PYTHONPATH=/home/maga:
Python 2.7.18
Available Sample Apps are: (/home/maga/.local/monailabel/sample-apps)
----------------------------------------------------
Deepedit based Apps
----------------------------------------------------
  deepedit                      : /home/maga/.local/monailabel/sample-apps/deepedit
  deepedit_multilabel           : /home/maga/.local/monailabel/sample-apps/deepedit_multilabel

Deepgrow based Apps
----------------------------------------------------
  deepgrow                      : /home/maga/.local/monailabel/sample-apps/deepgrow

Standard Segmentation Apps
----------------------------------------------------
  segmentation                  : /home/maga/.local/monailabel/sample-apps/segmentation
  segmentation_left_atrium      : /home/maga/.local/monailabel/sample-apps/segmentation_left_atrium
  segmentation_spleen           : /home/maga/.local/monailabel/sample-apps/segmentation_spleen
</code></pre>
<ol start="3">
<li>Spleen dataset downloaded and installed fine:</li>
</ol>
<pre><code class="lang-auto">~/.local/bin/monailabel datasets --download --name Task09_Spleen --output datasets
Using PYTHONPATH=/home/maga:
Python 2.7.18
Directory already exists: datasets/Task09_Spleen
</code></pre>
<ol start="4">
<li>Can’t get the deepedit to download, nor can start the server</li>
</ol>
<pre><code class="lang-auto">~/.local/bin/monailabel apps --download --name deepedit --output apps
Using PYTHONPATH=/home/maga:
Python 2.7.18
Traceback (most recent call last):
  File "/usr/lib/python3.8/runpy.py", line 194, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/usr/lib/python3.8/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/home/maga/.local/lib/python3.8/site-packages/monailabel/main.py", line 333, in &lt;module&gt;
    Main().run()
  File "/home/maga/.local/lib/python3.8/site-packages/monailabel/main.py", line 108, in run
    self.action_apps(args)
  File "/home/maga/.local/lib/python3.8/site-packages/monailabel/main.py", line 161, in action_apps
    apps = os.listdir(apps_dir)
FileNotFoundError: [Errno 2] No such file or directory: '/usr/monailabel/sample-apps'

~/.local/bin/monailabel start_server --app apps/deepedit --studies datasets/Task09_Spleen/imagesTr
Using PYTHONPATH=/home/maga:
Python 2.7.18
APP Directory apps/deepedit NOT Found

</code></pre>

---

## Post #16 by @diazandr3s (2021-12-16 23:39 UTC)

<p>Hi <a class="mention" href="/u/muratmaga">@muratmaga</a>,</p>
<p>From what I can see, you’re working with Python 2.X (Python 2.7.18). As shown in the instructions, please use Python 3.X. My recommendation is you either create a virtual environment with a Python version 3.X or you work with the docker container.<br>
Once that is done, you could download the DeepEdit App as you’ve already tried:</p>
<blockquote>
<p>monailabel apps --download --name deepedit --output apps</p>
</blockquote>
<p>or directly download it from the main repo.</p>

---

## Post #17 by @muratmaga (2021-12-17 02:47 UTC)

<p>It is a python3 environment. I even setup the update-alternatives to make default python python3. But anyways, I am getting issues witht the docker too: This inside output after running the docker command:</p>
<blockquote>
<p>root@magalab-ML:/opt/monai# monailabel apps --download --name deepedit --output apps<br>
Using PYTHONPATH=/opt:<br>
Directory already exists: /opt/monai/apps/deepedit<br>
root@magalab-ML:/opt/monai# monailabel datasets --download --name Task09_Spleen --output datasets<br>
Using PYTHONPATH=/opt:<br>
Directory already exists: datasets/Task09_Spleen<br>
root@magalab-ML:/opt/monai# monailabel start_server --app apps\deepedit --studies datasets\Task09_Spleen\imagesTr<br>
Using PYTHONPATH=/opt:<br>
APP Directory appsdeepedit NOT Found<br>
root@magalab-ML:/opt/monai#</p>
</blockquote>

---

## Post #18 by @muratmaga (2021-12-17 04:06 UTC)

<p>server seems to work, if the full correct path  is provided in the command that invokes the server like this:</p>
<p><code>monailabel start_server --app /opt/monai/apps/deepedit --studies /opt/monai/datasets/Task09_Spleen/imagesTr</code></p>

---

## Post #19 by @diazandr3s (2021-12-17 11:26 UTC)

<p>Superb! Thanks for letting us know <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
Please remember that if you want to work with multilabel DeepEdit, you should use <a href="https://github.com/Project-MONAI/MONAILabel/tree/main/sample-apps/deepedit_multilabel" rel="noopener nofollow ugc">this App</a>.<br>
We are in the process of merging both single and multilabel into a single App so it is easier for users.<br>
When using the multilabel DeepEdit App, please change the label names here: <a href="https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/deepedit_multilabel/main.py#L43" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel/main.py at main · Project-MONAI/MONAILabel · GitHub</a></p>

---

## Post #20 by @muratmaga (2021-12-18 18:48 UTC)

<aside class="quote no-group" data-username="diazandr3s" data-post="19" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/diazandr3s/48/9973_2.png" class="avatar"> diazandr3s:</div>
<blockquote>
<p>Thanks for letting us know</p>
</blockquote>
</aside>
<p>I do have a comment about documentation.</p>
<p>It would be better if you specify the filepaths using the standard convention with slash <code>/</code>, as opposed to using windows convention of backslash <code>\</code>. Slash is more universal and most windows applications (like Python) will interpret the windows path with <code>C:/</code>  still correctly, whereas in Unix <code>\</code> is interpreted as an escape character. It took me a while to figure out that the path errors are not real path errors, but simply interpreted incorrectly because examples are probably written on windows platform and same instructions apply to both OSes.</p>

---

## Post #21 by @muratmaga (2021-12-18 20:56 UTC)

<p>I have successfully run the vanilla docker and the SlicerMonai. Server communicated and found the apps etc (I didn’t try to execute it). Now I am modifying the docker to do your requested changes to make it work with my data organized in the way requested above (labelmaps are in labels/final and have the identical name and format as the corresponding volumes).</p>
<ol>
<li>
<p>I ran the docker to map this directory which was mapped as /workspace/murat_data<br>
<code>sudo docker run -it --rm --gpus all --ipc=host --net=host -v $PWD:/workspace/murat_data projectmonai/monailabel:latest bash</code></p>
</li>
<li>
<p>Then I download the deepedit_multilabel apps to the docker via command<br>
<code>monailabel apps --download --name deepedit_multilabel --output /workspace/apps/</code></p>
</li>
<li>
<p>Then I edit the main.py in the /workshape/apps/deepedit_multilabel to match my label incides:</p>
</li>
</ol>
<pre><code class="lang-auto">self.label_names = {
                "left lung": 1,
                "cranial lobe": 2,
                "middle lobe": 3,
                "caudal lobe": 4,
                "accessory lobe": 5,
                "left kidney": 6,
                "right kidney": 7,
                "stomach wall": 8,
                "stomach lumen": 9,
                "medial lobe of liver": 10,
                "left lobe of liver ": 11,
                "right lobe of liver": 12,
                "caudate lobe of liver": 13,
                "left adrenal": 14,
                "right adrenal": 15,
                "rectum": 16,
                "bladder": 17,
                "left ventricle": 18,
                "right ventricle": 19,
                "left thymic rudiment": 20,
                "right thymic rudiment": 21,
                "third ventricle": 22,
                "mesencephalic vesicle": 23,
                "fourth ventricle": 24,
                "cerebral aqueduct": 25,
                "left lateral ventricle": 26,
                "right lateral ventricle": 27,
                "right olfactory bulb": 28,
                "left olfacotory bulb": 29,
                "right thalamus ": 30,
                "left thalamus": 31,
                "right hypothamalus ": 32,
                "left hypothalmus": 33,
                "right septal area": 34,
                "left septal area": 35,
                "left neopallial cortex abd amygdala": 36,
                "right neopallial cortex and amygdala": 37,
                "right striatum": 38,
                "left striatum ": 39,
                "right ventricular zone": 40,
                "left ventricular zone": 41,
                "pons": 42,
                "background ": 0,
}
</code></pre>
<ol start="4">
<li>Then I run the server via the command:<br>
<code>monailabel start_server --app /workspace/apps/deepedit_multilabel/ --studies /workspace/murat_data/</code>
</li>
</ol>
<p>which gives me an error about indentations. I created these with the tabs, but apparently it is not right. and also in some cases we have very different labels. I don’t think it makes too much sense to hard code these to the code itself. Can I request a revision such that the labels are read as like a parameter file, like csv or a json at the run time, so that we can possibly run multiple copies of multilabel for different tasks with minimal revision.</p>
<p>Our plan is to deploy this application for a number of biologists that will be using multilabel deepedit for different segmentations tasks. So that kind of flexibility will be important.</p>

---

## Post #22 by @diazandr3s (2021-12-19 00:05 UTC)

<p>Thanks for reporting this <a class="mention" href="/u/muratmaga">@muratmaga</a>. It helps us a lot to improve.<br>
This is definitely something we’ll work on. We’d also like to join the single and multilabel DeepEdit App so it is easier for the user.<br>
It may not the reason for the indentation error, but would it be possible to try this app removing the spaces after label names? (i.e. background, left striatum, right hypothamalus, right thalamus, left lobe of liver)<br>
Also, please try with 4 spaces instead of tabs. Some IDEs are difficult with this.</p>

---

## Post #23 by @muratmaga (2021-12-21 19:41 UTC)

<p>The server (via docker image) is up and seems to be running. I even get some results. However, documentation of the Slicer extension is very minimal. What are the next steps? How do I make use the existing labels to train the model?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c082e15f146ccd01462c51e018c68683424130f.jpeg" data-download-href="/uploads/short-url/8z4aMfShzpHpSaMgPq6BuL4YX6L.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3c082e15f146ccd01462c51e018c68683424130f_2_690x379.jpeg" alt="image" data-base62-sha1="8z4aMfShzpHpSaMgPq6BuL4YX6L" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3c082e15f146ccd01462c51e018c68683424130f_2_690x379.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3c082e15f146ccd01462c51e018c68683424130f_2_1035x568.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3c082e15f146ccd01462c51e018c68683424130f_2_1380x758.jpeg 2x" data-dominant-color="9FA3A1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1057 212 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #24 by @diazandr3s (2021-12-21 22:14 UTC)

<p>Thanks, <a class="mention" href="/u/muratmaga">@muratmaga</a>. I’m happy to see this working.<br>
You’re right, documentation of the Slicer module needs more work. This is something we’ll improve for the next version of MONAI Label along with the user interaction for DeepEdit Apps.</p>
<p>Could you please open an issue about this in the main repo? In this way, we can keep track of the most important bits.</p>
<p>Thanks in advance!</p>

---

## Post #25 by @rbumm (2022-05-19 16:47 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="14" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>The other issue I am having, it is not clear from this instruction set that whether the installation needs to be done as a priviledged user or it is possible to run it as normal user</p>
</blockquote>
</aside>
<p>Did you get this settled <a class="mention" href="/u/muratmaga">@muratmaga</a> , if yes - how ? Thanks.</p>

---

## Post #26 by @muratmaga (2022-05-19 18:00 UTC)

<p>We did manage to get it working eventually with <a class="mention" href="/u/diazandr3s">@diazandr3s</a> help, but it has been a while and I need to check my notes.</p>
<p>Where are you encountering the issue?</p>

---

## Post #27 by @muratmaga (2022-05-19 18:09 UTC)

<p>To clarify, I ended up using docker as it simplified everything:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/Project-MONAI/MONAILabel#docker">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Project-MONAI/MONAILabel#docker" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/b1f584f2fb3ec9851e06195e869a2ee86b41ef4fa5b50de90503b25be56832dc/Project-MONAI/MONAILabel" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/Project-MONAI/MONAILabel#docker" target="_blank" rel="noopener nofollow ugc">GitHub - Project-MONAI/MONAILabel: MONAI Label is an intelligent open source...</a></h3>

  <p>MONAI Label is an intelligent open source image labeling and learning tool. - GitHub - Project-MONAI/MONAILabel: MONAI Label is an intelligent open source image labeling and learning tool.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I used a command like this to specify the GPU for the docker instance to run on, as well as the map persistent folders between my host environment and the docker.</p>
<p><code>sudo docker run --cpus 32 -it --rm --gpus device=GPU-7fa21545-aa7c-728f-5925-0c0cf8f8f8a8 --ipc=host --net=host -v /home/maga/komp_monai/:/workspace/ projectmonai/monailabel:latest bash</code></p>
<p>Then, I would invoke the monai server within the docker shell with a command like</p>
<p><code>monailabel start_server --app /workspace/apps/komp_more/ --studies /workspace/mouse_fetus</code></p>
<p>In this case, <strong>komp_more</strong> is the multi-label app edited to match my label indices of the data (this is hard coded to the multi label deepedit python script), and <strong>mouse_fetus</strong> is where the volumes and associated label maps sits…</p>

---

## Post #28 by @rbumm (2022-05-19 18:13 UTC)

<p>I am installing monailabel with</p>
<pre><code class="lang-auto">pip install monailabel-weekly
</code></pre>
<p>but when downloading  “radiology”</p>
<pre><code class="lang-auto">monailabel apps --download --name radiology --output apps
</code></pre>
<p>I ran into</p>
<pre><code class="lang-auto">Using PYTHONPATH=/home/rbumm:
App radiology =&gt; /usr/monailabel/sample-apps/radiology not exists
</code></pre>
<p>which seems to be caused by the fact monailabel can not create subfolders in /usr/monailabel/ folder due to missing access rights.</p>

---

## Post #29 by @muratmaga (2022-05-19 18:15 UTC)

<p>Yes, that i why I gave up using directly on the host but going down the docker route. I didn’t want to modify my working environment.</p>

---

## Post #30 by @rbumm (2022-05-20 08:25 UTC)

<p>Thank you <a class="mention" href="/u/muratmaga">@muratmaga</a>. This would be a possible option if I can not get monailabel running via PIP install. However, I would prefer to find a valid pip install option for monailabel as it is described in the docs.</p>
<p>Where did you get the device = GPUxxx parameter from?</p>

---

## Post #31 by @rbumm (2022-05-20 12:37 UTC)

<p>For anyone interested:</p>
<p>Got monailabel install and server working in Windows 10 WSL Ubuntu by</p>
<pre><code class="lang-auto">git clone https://github.com/Project-MONAI/MONAILabel
pip install -r MONAILabel/requirements.txt
export PATH=$PATH:`pwd`/MONAILabel/monailabel/scripts
</code></pre>
<p>then</p>
<pre><code class="lang-auto"># download radiology app and sample dataset
monailabel apps --download --name radiology --output apps
monailabel datasets --download --name Task09_Spleen --output datasets
</code></pre>
<p>and then starting the monailabel server by</p>
<pre><code class="lang-auto"># start server using radiology app with deepedit model enabled
monailabel start_server --app apps/radiology --studies datasets/Task09_Spleen/imagesTr --conf models deepedit
</code></pre>
<p>The <code>pip install monailabel </code> process did not succeed, although it would probably be the better solution for new monailabel users.</p>

---

## Post #32 by @muratmaga (2022-05-20 16:13 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="30" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>Where did you get the device = GPUxxx parameter from?</p>
</blockquote>
</aside>
<p>you can either use the ordinal listed (0, 1, 2) in the nvidia-smi, but using UUID is more reliable (order may change based on which device gets initiated earlier during reboot, or driver change).</p>
<blockquote>
<p>PS C:\Users\murat&gt; nvidia-smi -q</p>
<p>==============NVSMI LOG==============</p>
<p>Timestamp                                 : Fri May 20 09:13:04 2022<br>
Driver Version                            : 510.06<br>
CUDA Version                              : 11.6</p>
<p>Attached GPUs                             : 1<br>
GPU 00000000:01:00.0<br>
Product Name                          : NVIDIA GeForce GTX 1650<br>
Product Brand                         : GeForce<br>
Product Architecture                  : Turing<br>
Display Mode                          : Disabled<br>
Display Active                        : Disabled<br>
Persistence Mode                      : N/A<br>
MIG Mode<br>
Current                           : N/A<br>
Pending                           : N/A<br>
Accounting Mode                       : Disabled<br>
Accounting Mode Buffer Size           : 4000<br>
Driver Model<br>
Current                           : WDDM<br>
Pending                           : WDDM<br>
Serial Number                         : N/A<br>
<strong>GPU UUID                              : GPU-7592dcbd-7989-64a5-f5e8-05730e7d713b</strong></p>
</blockquote>

---

## Post #33 by @rbumm (2022-05-20 17:26 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="31" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p><code>monailabel start_server --app apps/radiology --studies datasets/Task09_Spleen/imagesTr --conf models deepedit</code></p>
</blockquote>
</aside>
<p>Thanks, <a class="mention" href="/u/muratmaga">@muratmaga</a> and <a class="mention" href="/u/diazandr3s">@diazandr3s</a>. I probably have a couple of questions concerning monailabel later <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #34 by @rbumm (2022-05-22 12:21 UTC)

<p><a class="mention" href="/u/diazandr3s">@diazandr3s</a></p>
<p>Trying to train a model to detect “right lung”, “left lung” and “airways” with monailabel.<br>
This is my workflow, and most of this works:</p>
<ul>
<li>Set up a  “segmentation_lung” model by modifying “segmentation_spleen.py”, download the Task06_lung dataset, and start the monailabel server with</li>
</ul>
<pre><code class="lang-auto">monailabel start_server --app apps/radiology --studies datasets/Task06_Lung/imagesTr --conf models segmentation_lung
</code></pre>
<ul>
<li>Monailabel extension: Choose a “random” strategy and load random lung datasets into 3D Slicer with “next sample”.</li>
<li>Do a LungCTSegmenter segmentation and produce “right lung”, “left lung” and “airways” for 17 / 63 cases. The naming corresponds to the one used in my segmentation_lung.py file and prior to segmentation I see these as empty segments in monailabel´s segment editor instance.</li>
<li>After each segmentation: “Submit label” without error.</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/939fa51fe9bd8873e3cd9402d61c301cb98ca708.jpeg" data-download-href="/uploads/short-url/l3We0RhZKGWTto6oHpizfw1Erzi.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/939fa51fe9bd8873e3cd9402d61c301cb98ca708_2_557x500.jpeg" alt="image" data-base62-sha1="l3We0RhZKGWTto6oHpizfw1Erzi" width="557" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/939fa51fe9bd8873e3cd9402d61c301cb98ca708_2_557x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/939fa51fe9bd8873e3cd9402d61c301cb98ca708.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/939fa51fe9bd8873e3cd9402d61c301cb98ca708.jpeg 2x" data-dominant-color="767879"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">670×601 91.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>My - probably newbie - questions, sry:</p>
<p>Would this be a good workflow?<br>
When do I have to press “Train”?<br>
Why does accuracy stay zero after a “Train”?<br>
How can I see the performance of my newly trained monailabel model?<br>
Where is/is there a resulting *.pt file?<br>
or generally - where is the result of my training work when I finish the server - can I save or export it?</p>

---

## Post #35 by @pieper (2022-05-22 16:06 UTC)

<p>Hi <a class="mention" href="/u/rbumm">@rbumm</a> - thanks for sharing your experience.  I don’t have all the answers but hopefully I can answer some and others can also chip in.  My experiment was to try training on <a href="https://www.synapse.org/#!Synapse:syn22159468/wiki/603890">this brain data</a>.</p>
<aside class="quote no-group" data-username="rbumm" data-post="34" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>Would this be a good workflow?</p>
</blockquote>
</aside>
<p>As I understand it yes, this is what is intended.</p>
<aside class="quote no-group" data-username="rbumm" data-post="34" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>When do I have to press “Train”?</p>
</blockquote>
</aside>
<p>I understand you can click train at any point and continue to submit more labels as it goes.</p>
<aside class="quote no-group" data-username="rbumm" data-post="34" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>Why does accuracy stay zero after a “Train”?</p>
</blockquote>
</aside>
<p>Here I don’t know.  My experience with the pre-labeled images was that one round of training got to about 70% in a day on a mid-range GPU and another day of training got to 80%.</p>
<aside class="quote no-group" data-username="rbumm" data-post="34" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>How can I see the performance of my newly trained monailabel model?</p>
</blockquote>
</aside>
<p>I was able to load a new image that had not be labeled yet and click the Run button to see that result of the model.  The results were promising, but not really usable.</p>
<aside class="quote no-group" data-username="rbumm" data-post="34" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>Where is/is there a resulting *.pt file?</p>
</blockquote>
</aside>
<p>For me on ubuntu they are in ./.local/monailabel/sample-apps/deepedit_multilabel/model</p>
<aside class="quote no-group" data-username="rbumm" data-post="34" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>or generally - where is the result of my training work when I finish the server - can I save or export it?</p>
</blockquote>
</aside>
<p>I know the plan ultimately is to have MONAI Deploy as an option for this, but I haven’t seen it done yet.</p>

---

## Post #36 by @rbumm (2022-05-22 17:15 UTC)

<p>Thank you.</p>
<p>Probably this fails on my desktop because</p>
<pre><code class="lang-auto">&gt;&gt;&gt; import torch
&gt;&gt;&gt; torch.cuda.is_available()
False
</code></pre>

---

## Post #37 by @pieper (2022-05-22 17:18 UTC)

<p>That cold be it.  On my machine (ubuntu with an nvidia gpu) cuda is available, but I would have thought pytorch would fallback to cpu, even if that’s slower.</p>

---

## Post #38 by @diazandr3s (2022-05-23 11:33 UTC)

<p>Many thanks for sharing your experience, <a class="mention" href="/u/rbumm">@rbumm</a>. It’s great to see this working on your end.</p>
<blockquote>
<p>The <code>pip install monailabel </code> process did not succeed, although it would probably be the better solution for new monailabel users.</p>
</blockquote>
<p>I agree with this.</p>
<p>The radiology app is available from version 0.4.0 onwards. I suggest you install the release candidate 3 for version 0.4.0. This means, <code>pip install monailabel==0.4.0rc3</code></p>
<p>Sorry, I didn’t give you the correct version in the last message.</p>
<p>With regards to your questions:</p>
<blockquote>
<p>Would this be a good workflow?</p>
</blockquote>
<p>Yes, that’s a good workflow.</p>
<p>MONAI Label usage could be customized depending on the user type, though. We’re working on this for the next release (i.e. multi-user workflow)</p>
<blockquote>
<p>When do I have to press “Train”?</p>
</blockquote>
<p>This is a good question. You could trigger the training every time you add a new label. But is up to the user. You could also wait until you label 5 or 10 new labels.</p>
<blockquote>
<p>Why does accuracy stay zero after a “Train”?</p>
</blockquote>
<p>This shouldn’t be zero. You should see the accuracy obtained during training.</p>
<blockquote>
<p>How can I see the performance of my newly trained monailabel model?</p>
</blockquote>
<p>The idea is that the annotator will take less time to annotate/edit the predictions obtained for the new unlabeled images. You could use a percentage of the training images for validation.</p>
<blockquote>
<p>Where is/is there a resulting *.pt file?</p>
</blockquote>
<blockquote>
<p>or generally - where is the result of my training work when I finish the server - can I save or export it?</p>
</blockquote>
<p>You should see a folder called <code>model</code> under the radiology app folder.</p>
<p>Many thanks, <a class="mention" href="/u/pieper">@pieper</a> for your comments. They help a lot <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #39 by @rbumm (2022-05-24 13:41 UTC)

<p>Deeply hidden on the internet:</p>
<p>One needs to run a Windows Insider build 20145 or superior (-&gt;Windows 11) in order to use CUDA in WSL2. See <a href="https://stackoverflow.com/questions/64256241/found-no-nvidia-driver-on-your-system-error-on-wsl2-conda-environment-with-pytho">here</a> and <a href="https://docs.nvidia.com/cuda/wsl-user-guide/index.html">here</a>.<br>
After updating to Windows 11,</p>
<pre><code class="lang-auto">&gt;&gt;&gt; import torch
&gt;&gt;&gt; torch.cuda.is_available()
True
</code></pre>
<p><img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji only-emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
and monailabel training succeeded. Accuracy increases during training.</p>
<p><a class="mention" href="/u/diazandr3s">@diazandr3s</a> would I need to do an auto segmentation with each new dataset to see the improved monailabel capabilities/accuracy?</p>
<aside class="quote no-group" data-username="diazandr3s" data-post="38" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/diazandr3s/48/9973_2.png" class="avatar"> diazandr3s:</div>
<blockquote>
<p>The idea is that the annotator will take less time to annotate</p>
</blockquote>
</aside>
<p>The annotator ? Please explain.</p>

---

## Post #40 by @diazandr3s (2022-05-24 23:10 UTC)

<pre><code class="lang-auto">Deeply hidden on the internet:

One needs to run a Windows Insider build 20145 or superior (-&gt;Windows 11) in order to use CUDA in WSL2. See [here ](https://stackoverflow.com/questions/64256241/found-no-nvidia-driver-on-your-system-error-on-wsl2-conda-environment-with-pytho) and [here](https://docs.nvidia.com/cuda/wsl-user-guide/index.html).
After updating to Windows 11,

and monailabel training succeeded. Accuracy increases during training.
</code></pre>
<p>I’m glad this is working <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<pre><code class="lang-auto">
@diazandr3s would I need to do an auto segmentation with each new dataset to see the improved monailabel capabilities/accuracy?
</code></pre>
<p>If you have labels in the new dataset to compute Dice or another metric, then yes - that could be a way of checking model performance.</p>
<p>If you don’t have labels in the new dataset, a way you could evaluate the model is by computing the time taken by expert/clinician to segment new volumes/images.</p>
<p><code>The annotator ? Please explain.</code></p>
<p>I meant the radiologist/clinician using MONAI Label <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #42 by @rbumm (2022-05-25 08:03 UTC)

<aside class="quote no-group" data-username="diazandr3s" data-post="40" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/diazandr3s/48/9973_2.png" class="avatar"> diazandr3s:</div>
<blockquote>
<p>I meant the radiologist/clinician using MONAI Label</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/diazandr3s">@diazandr3s</a>  or that use case: How would the annotator benefit from monailabel and the monailabel model during segmenting without labels? Which buttons could he press or which functions would he use to create AI-assisted segmentation easier/faster than in the normal segment editor?</p>

---

## Post #43 by @muratmaga (2022-05-25 14:32 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="42" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>How would the annotator benefit from monailabel and the monailabel model during segmenting without labels?</p>
</blockquote>
</aside>
<p>MonaiLabel can be used both to infer and train. If your goal is to facilitate segmentation, first you train a model in say a small number of samples with labelmaps. You might even get something with 10-12 samples (not good but ok).</p>
<p>For inference you have two options, you can either use a dataset loaded into Slicer scene and can ask MonaiLabel to segment it. Or you can deploy the MonaiLabel server such that there are unsegmented volumes on the server side and that’s displayed in the dropdown menu in the monailabel extension and you can just load one after other and run inference on them.</p>
<p>Then there is even an option to push those segmentations back to the server and restart training with them (in addition to the first 10-12 samples you have trained the model on).</p>
<p>The UI is a bit complex, and as I mentioned to the <a class="mention" href="/u/diazandr3s">@diazandr3s</a> the inference and training option probably should be decoupled (mostly to avoid accidentally running the training). This might be done perhaps at the server side (e.g., a flag to deploy the server only for inference, or some sort of authentication for training)</p>

---

## Post #44 by @diazandr3s (2022-05-25 22:34 UTC)

<p>Thanks for the detailed explanation, <a class="mention" href="/u/muratmaga">@muratmaga</a></p>
<p><a class="mention" href="/u/rbumm">@rbumm</a> please let us know if there is anything else I can help with <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>All your feedback is valuable to making MONAI Label better and easier to use.</p>

---

## Post #45 by @rbumm (2022-05-26 13:10 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="43" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>MonaiLabel can be used both to infer and train. If your goal is to facilitate segmentation, first you train a model in say a small number of samples with labelmaps. You might even get something with 10-12 samples (not good but ok).</p>
</blockquote>
</aside>
<p>Thank you. Hope it is ok for the community to push that thread up again, if not, I could also DM <a class="mention" href="/u/diazandr3s">@diazandr3s</a> or <a class="mention" href="/u/muratmaga">@muratmaga</a>.</p>
<p>Probably best to try the train option. Is it correct that I would need to</p>
<ul>
<li>segment each of let’s say 12 of my 65 lung datasets and create “right lung”, “left lung” and “airways”</li>
<li>am I allowed to do this segmentation in a different segmentation program?</li>
<li>after segmentation of each dataset → switch back to monailabel extension and “submit Label”</li>
<li>After each “Submit” or after a few “Submits” do a “Train”</li>
</ul>
<p>Now comes the part which I do not understand:</p>
<p>At patient 12/65 I would like to check the performance of the trained monailabel model.<br>
So I load patient dataset 13.<br>
Expect to press a button in monailabel which makes the extension populate the labels “right lung”, left lung", “airways” in dataset 13 from what it has learned so far in patients 1-12. I could then improve and “Submit” again.</p>
<ul>
<li>Is there such a button / menu entry / python command in monailabel?</li>
<li>Do I have to place any markups/seeds for this?</li>
</ul>

---

## Post #46 by @pieper (2022-05-26 13:18 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="45" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>Thank you. Hope it is ok for the community to push that thread up again, if not, I could also DM <a class="mention" href="/u/diazandr3s">@diazandr3s</a> or <a class="mention" href="/u/muratmaga">@muratmaga</a>.</p>
</blockquote>
</aside>
<p>Let’s do keep this public - I find it very valuable and I hope everyone else does too!  It’s really important to learn, get feedback, and as needed improve the process or interface.</p>
<p>Your description of the workflow sounds right to me, and your expectation that 12 or 65 datasets should give a first pass model sounds consistent with expectations I have heard expressed.</p>
<aside class="quote no-group" data-username="rbumm" data-post="45" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<ul>
<li>Is there such a button / menu entry / python command in monailabel?</li>
<li>Do I have to place any markups/seeds for this?</li>
</ul>
</blockquote>
</aside>
<p>For me, once I had the model trained to 75-80% I was able to use the Run. button to apply to a new case (either one of the training set or a new similar volume loaded in Slicer).  No new seeds required.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75b564a075462f3a5d7db43b7aa863c58d4df224.png" data-download-href="/uploads/short-url/gNiuO7yag3jxRGNJedXaOiPnkxu.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75b564a075462f3a5d7db43b7aa863c58d4df224_2_690x103.png" alt="image" data-base62-sha1="gNiuO7yag3jxRGNJedXaOiPnkxu" width="690" height="103" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75b564a075462f3a5d7db43b7aa863c58d4df224_2_690x103.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75b564a075462f3a5d7db43b7aa863c58d4df224_2_1035x154.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75b564a075462f3a5d7db43b7aa863c58d4df224.png 2x" data-dominant-color="E8E8E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1164×174 30.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #47 by @muratmaga (2022-05-26 15:11 UTC)

<p>I will list my experience and hopefully <a class="mention" href="/u/diazandr3s">@diazandr3s</a> can chime in with more technical aspects.</p>
<ol>
<li>You can do the segmentations in any program, provided that you can export a labelmap and that labelmap and associated volume line up correctly in Slicer.</li>
<li>Sounds like you want to do multi-label segmentation. If that’s the case you really want to pay a lot of attention that each structure is label with identical label in each of the labels. If Left Lung is 2, and Right Lung is 3 in some segments and vice versa your training will fail.</li>
<li>I haven’t used the Active Learning paradigm yet, but what you describe sounds reasonable (meaning you push newly segmented volumes and associated labelmaps back to the MonaiServer, and then when you have a bunch more, retrain the model).</li>
<li>For how to parse the data automatically, you need to look at the data organization on the MonaiLabel server side. As I recall, you will organize such that 65 volumes in one folder and 12 ground truth label maps in sub folder called <strong>labels/final</strong> underneath it. File names and formats of volumes and labels has to match. Then, if you use the next sample button it should download automatically the 13th one (and other unsegmented ones), then you can hit the Run deep-edit_seg button and run the model on them (inference). This is of course after you train a model.</li>
</ol>

---

## Post #48 by @mikebind (2022-05-26 17:35 UTC)

<p>Please do keep this public.  I plan to try out MonaiLabel through Slicer in the next few weeks, and am trying to keep up with this discussion which I think will be very helpful when I get to starting!</p>

---

## Post #49 by @rbumm (2022-05-26 18:30 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="48" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>Please do keep this public</p>
</blockquote>
</aside>
<p>Ok guys, then this may also be a timesaver when you try to set up the monailabel server with a more recent NVIDIA graphics card (NV is mandatory for CUDA):</p>
<p>First and most importantly, one has to upgrade to Windows 11 to run WSL2 and CUDA with recent cards.<br>
Still ran into</p>
<pre><code class="lang-auto">GeForce RTX 3070 Ti with CUDA capability sm_86 is not compatible with the current PyTorch installation. The current PyTorch install supports CUDA capabilities sm_37 sm_50 sm_60 sm_61 sm_70 sm_75
</code></pre>
<p>shown in the monailabel server output and training sessions failed.<br>
torch.version.cuda showed:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; import torch
&gt;&gt;&gt; torch.version.cuda
'10.2'
</code></pre>
<p>So it appeared that two CUDA versions were on that computer simultaneously.<br>
Got this only solved by</p>
<pre><code class="lang-auto"># remove all CUDAs
sudo apt-get --purge remove "*cublas*" "cuda*" "nsight*"
sudo apt-get --purge remove "*cublas*" "*cufft*" "*curand*" 
# install torch 1.9 and CUDA 11.1
pip3 install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
</code></pre>
<p>After that</p>
<pre><code class="lang-auto">&gt;&gt;&gt; import torch
&gt;&gt;&gt; torch.version.cuda
'11.2'
</code></pre>
<p>and there was no more warning, monailabel training worked with that GTX 3070 Ti too.<br>
<img src="https://emoji.discourse-cdn.com/twitter/space_invader.png?v=12" title=":space_invader:" class="emoji only-emoji" alt=":space_invader:" loading="lazy" width="20" height="20"></p>

---

## Post #50 by @diazandr3s (2022-05-26 19:32 UTC)

<p>I think this is a great discussion. I’d keep it public <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Thanks again for sharing your experience, <a class="mention" href="/u/muratmaga">@muratmaga</a></p>
<p>You accurately highlighted the most important things:</p>
<p>1/ labels can be created/modified in any program and then submitted to MONAI Label server,<br>
2/ each structure should be consistently labeled with an identical label number, and<br>
3/ data organization in MONAI Label matters (i.e. when starting with already created labels, both images and labels should have the same name …)</p>
<p>Thanks, everyone!!</p>

---

## Post #51 by @muratmaga (2022-05-27 00:20 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="49" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>shown in the monailabel server output and training sessions failed.</p>
</blockquote>
</aside>
<p>İn my experience, matching all the tools and base libraries and drivers is half the challenge of setting up a deep learning environment. You took an extra step in doing all this under wsl2. But sounds like you are making progress.</p>

---

## Post #52 by @rbumm (2022-05-29 11:58 UTC)

<p>Would this part of the configuration be right for setting up a lung deepedit conf ?<br>
How could we start a model from scratch when you can not download a pretrained model (see → # Download PreTrained Model section) ?</p>
<pre><code class="lang-auto">...
        # Single label
        #self.labels = {
        #    "spleen": 1,
        #    "background": 0,
        #}
        # Single label
        self.labels = {
            "right lung": 1,
            "left lung": 2,
            "airways": 3,
            "background": 0,
        }

        # Number of input channels - 4 for BRATS and 1 for spleen
        self.number_intensity_ch = 4

        network = self.conf.get("network", "dynunet")

        # Model Files
        self.path = [
            os.path.join(self.model_dir, f"pretrained_{self.name}_{network}.pt"),  # pretrained
            os.path.join(self.model_dir, f"{self.name}_{network}.pt"),  # published
        ]

        # Download PreTrained Model
        if strtobool(self.conf.get("use_pretrained_model", "true")):
            url = f"{self.PRE_TRAINED_PATH}/deepedit_{network}_singlelabel.pt"
            download_file(url, self.path[0])
...
``</code></pre>

---

## Post #53 by @rbumm (2022-05-29 12:04 UTC)

<p>Assuming we load a “Next sample” in 3DSlicers monailabel extension after starting the monailabel server with</p>
<pre><code class="lang-auto">monailabel start_server --app ./apps/radiology --studies ./datasets/Task06_Lung/imagesTr --conf models deepedit
</code></pre>
<p>in which standard segmentations of the above labels are created ok by monailabel:<br>
Does preservation of segment color matter for the learning process if you switch to an external segmentation module and the back to monailabel ?</p>

---

## Post #54 by @rbumm (2022-05-29 15:42 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="53" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>in which standard segmentations</p>
</blockquote>
</aside>
<p>I ment “in which empty standard segments are created ok”</p>

---

## Post #55 by @rbumm (2022-05-31 13:03 UTC)

<p>There is very very slow progress in getting a monailabel lung CT segmentation server up and running.<br>
What I did:</p>
<p>Changed segmentation.py in ./apps/radiology/lib/conf/</p>
<pre><code class="lang-auto">        # Labels
        #self.labels = {
        #    "spleen": 1,
        #    "right kidney": 2,
        #    "left kidney": 3,
        #    "gallbladder": 4,
        #    "esophagus": 5,
        #    "liver": 6,
        #    "stomach": 7,
        #    "aorta": 8,
        #    "inferior vena cava": 9,
        #    "portal vein and splenic vein": 10,
        #    "pancreas": 11,
        #    "right adrenal gland": 12,
        #    "left adrenal gland": 13,
        #}

        # Labels
        self.labels = {
            "right lung": 1,
            "left lung": 2,
            "airways": 3,
        }
</code></pre>
<p>Then</p>
<pre><code class="lang-auto">monailabel start_server --app ./apps/radiology --studies ./datasets/Task06_Lung/imagesTr --conf models segmentation
</code></pre>
<p>resulted in multiple error messages and it took ages to find out that this was caused by monailabel using the multilabel pretrained_segmentation.pt that obviously has much more labels than the three I need for lung segmentation and thus - fails.</p>
<p>It turned out that changing the server startup code to</p>
<pre><code class="lang-auto">monailabel start_server --app ./apps/radiology --studies ./datasets/Task06_Lung/imagesTr --conf models segmentation --conf use_pretrained_model false
</code></pre>
<p>avoids the errors and enables training.</p>

---

## Post #56 by @muratmaga (2022-05-31 14:29 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="55" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>avoids the errors and enables training.</p>
</blockquote>
</aside>
<p>Alternatively, you can rename your app to something, create a separate folder for it and pass that to the monailabel start. İ found that approach i bit cleaner when i was experimenting.</p>

---

## Post #57 by @muratmaga (2022-05-31 17:21 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="53" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>Does preservation of segment color matter for the learning process if you switch to an external segmentation module and the back to monailabel ?</p>
</blockquote>
</aside>
<p>I actually don’t know the answer to that. I suspect it does a lot. MonaiLabel works on labelmaps, not segmentation. So the issue is how those segments are converted to labelmaps. I think use of a strict terminology is necessary to for correct conversion. I am trying to learn terminology myself as you can see <a href="https://discourse.slicer.org/t/tutorial-on-terminologies/23400/3">here</a></p>

---

## Post #58 by @mikebind (2022-06-02 20:42 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a>, was there a reason you chose to install monailabel in WSL2 rather than in Windows?</p>

---

## Post #59 by @rbumm (2022-06-03 08:13 UTC)

<p>This is a very good question <a class="mention" href="/u/mikebind">@mikebind</a>, for some reason and experience, I thought that this kind of server can only be set up on a Linux (sub)system, which is probably not the case.  Generally not good news, because I spent days adjusting CUDA in WSL2 (see above).</p>
<p>The monailabel server (Windows 11, WSL2) now runs without error messages here, I can train it, but I do not get usable segmentation results in 3D Slicer yet and I decided to put this on hold until the Monailabel workshop in June or until there are new bright ideas.</p>
<p>Are you using monailabel directly in Windows from the powershell?</p>

---

## Post #60 by @jamesobutler (2022-06-03 11:29 UTC)

<p>Yes MonaiLabel is supported on Windows. <a href="https://github.com/Project-MONAI/MONAILabel#installation" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Project-MONAI/MONAILabel: MONAI Label is an intelligent open source image labeling and learning tool.</a></p>

---

## Post #61 by @rbumm (2022-06-03 19:26 UTC)

<p>It can confirm that actually works in Windows 11 native too.</p>
<p>Needed to install Python 3.9, then</p>
<pre><code class="lang-auto">git clone https://github.com/Project-MONAI/MONAILabel
$Env:PATH += ";C:\Users\rudol\MONAILabel\monailabel\scripts"
monailabel apps --download --name radiology --output apps
# modify segmentation.py by hand, add the lung and airway labels
monailabel datasets --download --name Task06_Lung --output datasets
monailabel start_server --app ./apps/radiology --studies ./datasets/Task06_Lung/imagesTr --conf models segmentation --conf use_pretrained_model false
</code></pre>
<p>I train 7-8 datasets, but all I get from auto segmentation is something like</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/8225eefd7f4dda4c4d33f20e6047b19ea4d6ef92.jpeg" data-download-href="/uploads/short-url/izlli872WmGw3ISDCRsoKUYqzrc.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8225eefd7f4dda4c4d33f20e6047b19ea4d6ef92_2_440x500.jpeg" alt="image" data-base62-sha1="izlli872WmGw3ISDCRsoKUYqzrc" width="440" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8225eefd7f4dda4c4d33f20e6047b19ea4d6ef92_2_440x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8225eefd7f4dda4c4d33f20e6047b19ea4d6ef92_2_660x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/8225eefd7f4dda4c4d33f20e6047b19ea4d6ef92.jpeg 2x" data-dominant-color="4F4B46"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">686×779 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>where only the first segment carries the displayed data.</p>

---

## Post #62 by @mikebind (2022-06-03 22:33 UTC)

<p>I was able to install on Windows 10 by more or less following the installation instructions at<br>
<a href="https://docs.monai.io/projects/label/en/latest/installation.html" class="onebox" target="_blank" rel="noopener">https://docs.monai.io/projects/label/en/latest/installation.html</a></p>
<p>with the following modifications:</p>
<ul>
<li>I installed to a conda environment</li>
<li>I installed the weekly monailabel instead of the stable version because installing the stable failed due (I think) to this issue: <a href="https://github.com/Project-MONAI/MONAILabel/issues/719" class="inline-onebox">Unsuccessful `pip install monailabel&gt;=0.4*` on Windows platform · Issue #719 · Project-MONAI/MONAILabel · GitHub</a>, which is marked as resolved, but maybe hasn’t made it into the stable version yet</li>
</ul>
<pre><code class="lang-auto"># From an "Anaconda Prompt" console window
# Create conda environment named "monaiweekly"
conda create --name monaiweekly python=3.9
conda activate monaiweekly
# Follow install process steps from monailabel website
python -m pip install --upgrade pip setuptools wheel
pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio===0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
python -c "import torch; print(torch.cuda.is_available())" 
# ^^ above line should return true ^^
# Install monailabel
pip install monailabel-weekly 
# "pip install monailabel" failed due to SimpleCRF error, fixed in weekly
# Download radiology app for monailabel
monailabel apps --download --name radiology --output apps 
# Download sample data set (~27 GB, FYI)
monailabel datasets --download --name Task03_Liver --output datasets  
# Start monailabel server
monailabel start_server --app apps/radiology --studies datasets/Task03_Liver/imagesTr --conf models deepedit
</code></pre>
<p>Initially, I had some problems due, I think, to having installed previous versions of torch, monailabel, or some combination of the two, but these were resolved when I uninstalled the old versions and then reinstalled the new versions in this new clean conda environment.</p>
<p>In Slicer, I got the MONAILabel extension and restarted Slicer, then was able to connect to the locally running server (by just pressing the fetch/refresh button on the MONAI Label server line of the MONAILabel module in Slicer) . I think an initial image volume from the liver data set was automatically loaded when I connected to the server, but if not, one was loaded when I hit the Next Sample button.</p>
<p>So far, so good. For the next steps, I got a little lost in how things were supposed to work.  I have not been able to get a liver segmentation model working yet, but now that I think all the back end stuff is working, I am going to reread this thread and other similar ones to see if I can figure out how to do what I want. For reference, I have a dataset of 20 liver segmentations with corresponding images as a starting point as well as some more images without segmentations which I would like to begin to segment using MONAILabel, then refine those segmentations and contribute back to improve the training of the model.  I think this is exactly what MONAILabel is supposed to be for, but there is very very limited documentation, so it is not at all clear how to actually do this. If I figure it out, I’ll post back here, and if I can’t figure it out I will share the sticking points.</p>

---

## Post #63 by @pieper (2022-06-04 14:47 UTC)

<p>In case anyone on this thread didn’t know, <a href="https://projectweek.na-mic.org/PW37_2022_Virtual/">the upcoming virtual Project Week</a> June 27-July 1 2022 will be a good opportunity to work together on issues like this.  There will also be another MONIA Label tutorial/workshop on June 22 9-11 EDT that you can sign up for <a href="https://forms.gle/wGfXEg2nYe7PE73m7">with this form</a>.</p>

---

## Post #64 by @muratmaga (2022-06-05 05:04 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="62" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>I got a little lost in how things were supposed to work. I have not been able to get a liver segmentation model working yet, but now that I think all the back end stuff is working,</p>
</blockquote>
</aside>
<p>To train a new model first organize your data.</p>
<ol>
<li>Create a folder (e.g., myMonai) and put all your volumes in there.</li>
<li>Within this folder create a <strong>labels/original</strong> and  a <strong>labels/final</strong> subfolder</li>
<li>Put all your existing labelsmap (you need to export your segmentation as labelmaps) into <strong>labels/final</strong> folder</li>
</ol>
<p>Next step is to edit the segmentation script in the apps folder to match your labels as well as modify the UNET resolution. FOr example I have been working with the multilabel app, and I edited the <strong>main.py</strong> so to reflect my labelIDs, and the resolution/spacing I wanted to use:</p>
<pre><code class="lang-auto">class MyApp(MONAILabelApp):
    def __init__(self, app_dir, studies, conf):

        # Zero values are reserved to background. Non zero values are for the labels
        self.label_names = {
            "interparietal": 5,
            "nasal": 6,
            "maxilla_R": 7,
            "molars_R": 8,
            "incisors": 9,
            "premaxilla": 10,
            "palatine_R": 11,
            "jugal_R": 12,
            "squamosal_R": 13,
            "occipital": 14,
            "parietal_R": 15,
            "frontal_R": 16,
            "basisphenoid": 17,
            "presphenoid": 20,
            "background": 0,
        }

        network = conf.get("network", "dynunet")

        # Use Heuristic Planner to determine target spacing and spatial size based on dataset+gpu
        spatial_size = json.loads(conf.get("spatial_size", "[192, 192, 192]"))
        target_spacing = json.loads(conf.get("target_spacing", "[1.09, 1.55, 0.71]"))
</code></pre>
<p>After this, fire up the moniaLabel server with these option (obviously you need to modify these to match your app name as well as specific folder structure)</p>
<p><code>monailabel start_server --app /workspace/apps/skullModel --studies ~myMonai</code></p>
<p>If you can successfully connect to the server with your Slicer MonaiLabel client, all you have left to train the model is to hit the train button and wait a few hours to see the accuracy increasing. I have trained the models for about couple days (~50000 iterations or so), that worked quite well… There are also other training options you want to explore (such as how you want to split your data into training/test/validation etc). But this should get you started with “a model”.</p>
<p>Once you get an ok model and you are ready to use it in new volumes that do not have segmentations,  all you have to is to copy those volumes to the top level of the myMonai folder, and restart the monaiLabel server. Server will detect these new samples, and in the Slicer if you hit the Next Sample button it will automatically process them. If you like the segmentation, you can hit the upload label button to send it to the MonaiLabel server, and after a few more samples like that you can hit the train button again.</p>
<p>So far I only used the multiLabel deepedit app, so I am not sure how much of this carries over to other apps that are distributed with monaiLabel, but hopefully this will help you some…</p>

---

## Post #65 by @mikebind (2022-06-06 18:13 UTC)

<p>Thanks so much for all of these details, <a class="mention" href="/u/muratmaga">@muratmaga</a>!  One thing I wondered about was since I am starting on just a single label, is there a pretrained model that I can start from?  I read in <a class="mention" href="/u/mangotee">@mangotee</a> 's <a href="https://discourse.slicer.org/t/how-to-start-with-monailabel-for-new-models/21063/6">comment above</a> that it sounds like this might be both possible and more quickly effective than training a new model from scratch. Back then (about 6 months ago), it sounds like there was more of a distinction between single label and multilabel models, and that the approach has become more unified since then.  I understand that pretrained models are structured for a particular number of output labels, and that changing the number or labels means that a model needs to be trained from scratch.   However, I also understand that when possible, transfer learning, where a model pre-trained on one task undergoes subsequent training to adapt it to another somewhat similar task, often works quite well.  So, that’s why I’m interested in whether there is a way to start from some other single label model trained on another task (e.g. spleen segmentation).  I am also interested in multilabel segmentations, so I will certainly also use the tips about starting from scratch in the future. Thanks!</p>

---

## Post #66 by @rbumm (2022-06-06 18:53 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="64" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p><code>"interparietal": 5,</code></p>
</blockquote>
</aside>
<p>corresponds to a labelmap color or labelmap value?<br>
My inputs are segmentations - where would I encode the “5”?</p>
<aside class="quote no-group" data-username="muratmaga" data-post="64" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>all you have left to train the model is to hit the train button and wait a few hours</p>
</blockquote>
</aside>
<p>I press the train button with my 67 lung datasets, but this takes only 10 minutes, accuracy increases but results are not good.<br>
How do you train for hours or days ?</p>

---

## Post #67 by @muratmaga (2022-06-06 19:19 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="66" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>corresponds to a labelmap color or labelmap value?</p>
</blockquote>
</aside>
<p>They are the labelmap value. When you export the segmentation to labelmaps from the segmentation module, you can check what the assigned labelID to that segmentation. It should be consistent in all your samples.</p>
<p>The volume size as well as the UNET spatial size will defined for the segmentation model will determine how fast your training would go. In the end, I had about 70 full segmented volumes (they are about 400x600x300), and each labepmap had 50+ structures. The Unet I trained had the spatial size of 192x192x192 (I think originally deep edit was only something like 48x48x32). So it took a few days.</p>

---

## Post #68 by @diazandr3s (2022-06-06 20:47 UTC)

<p>Thanks all for participating in this thread. This is a great conversation.<br>
I haven’t replied to your comments as I just came back from a long weekend.</p>
<p>I’ll try to address the questions/comments.</p>
<p><strong>Regarding this:</strong></p>
<pre><code class="lang-auto">corresponds to a labelmap color or labelmap value?
My inputs are segmentations - where would I encode the “5”?
</code></pre>
<p>As <a class="mention" href="/u/muratmaga">@muratmaga</a> suggested, the user should make sure that segments/labels consistently use the same number for each segment in all volumes.</p>
<p>It seems that Slicer assigns different numbering to each segment. We found that issue when working on teeth segmentation: <a href="https://projectweek.na-mic.org/PW36_2022_Virtual/Projects/AutomaticSegmentationofTeethandAlveolarBone/" class="inline-onebox" rel="noopener nofollow ugc">NA-MIC Project Weeks | Website for NA-MIC Project Weeks</a></p>
<p>As there are several ways/software to create labels (i.e. 3D Slicer, ITK-SNAP, etc), having a standard is not easy. <a class="mention" href="/u/lassoan">@lassoan</a> opened an <a href="https://github.com/ome/ngff/issues/79" rel="noopener nofollow ugc">issue here</a> to see whether we can address that.</p>
<p>There is another conversation about this <a href="https://github.com/Project-MONAI/MONAILabel/issues/724" rel="noopener nofollow ugc">here</a>.</p>
<p><strong>Regarding this:</strong></p>
<pre><code class="lang-auto">I press the train button with my 67 lung datasets, but this takes only 10 minutes, accuracy increases but results are not good.
How do you train for hours or days ?
</code></pre>
<p>This is a good question <a class="mention" href="/u/rbumm">@rbumm</a>. This depends on many factors: number of volumes segmented, number of epochs, the difficulty of the segmentation, etc</p>
<p>There could also be the problem of having inconsistent numbering for the manual segmentations. I’d check whether that is the case. For this, I use ITK-SNAP or Python.</p>
<p><strong>Regarding this:</strong></p>
<pre><code class="lang-auto">
Back then (about 6 months ago), it sounds like there was more of a distinction between single label and
 multilabel models, and that the approach has become more unified since then. I understand that 
pretrained models are structured for a particular number of output labels, and that changing the number 
or labels means that a model needs to be trained from scratch. However, I also understand that when 
possible, transfer learning, where a model pre-trained on one task undergoes subsequent training to 
adapt it to another somewhat similar task, often works quite well.
</code></pre>
<p>Thanks, <a class="mention" href="/u/mikebind">@mikebind</a>.<br>
MONAI Label has changed a lot in the last weeks. We’re trying to make it as easy to use as possible. One of the things that we’ve updated is single and multiple label segmentation - they are now a single model that can work for both tasks.</p>
<p>Depending on the number of labels, you should first define the label names and numbering here: <a href="https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/lib/configs/deepedit.py#L45" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel/deepedit.py at main · Project-MONAI/MONAILabel · GitHub</a></p>
<p>Then, deactivate the downloading of the pretrained model here: <a href="https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/lib/configs/deepedit.py#L75" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel/deepedit.py at main · Project-MONAI/MONAILabel · GitHub</a></p>
<p>Regarding transfer learning, you can easily get a pretrained model with MONAI Label using one of the available datasets <a href="https://drive.google.com/drive/folders/1HqEgzS8BV2c7xYNrZdEAnrHk7osJJ--2" rel="noopener nofollow ugc">here</a> and then adjusted to the task you’re interested.</p>
<p>We agree the documentation needs more work. For this, we’re working on a MONAI Label tutorial that shows all the basic stuff. We’re creating short videos like this one: <a href="https://drive.google.com/file/d/14J_YhSGjTWCMEKmMmOfwEvxkwuw9gCF0/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">train-from-scratch.mp4 - Google Drive</a></p>
<p>Please let me know if there is I missed here.</p>
<p>Thanks again!!</p>

---

## Post #69 by @mikebind (2022-06-06 22:46 UTC)

<p>I tried to get started with training from scratch and training began, but failed with a GPU memory error:</p>
<pre><code class="lang-auto">[2022-06-06 15:19:24,930] [33996] [MainThread] [INFO] (monailabel.tasks.train.basic_train:591) - 0 - Load Path C:\Users\mikeb\apps\radiology\model\pretrained_deepedit_dynunet.pt
Loading dataset:   0%|          | 0/15 [00:00&lt;?, ?it/s]
Loading dataset:   7%|6         | 1/15 [00:01&lt;00:26,  1.90s/it]
Loading dataset:  13%|#3        | 2/15 [00:04&lt;00:30,  2.31s/it]
Loading dataset:  20%|##        | 3/15 [00:07&lt;00:32,  2.67s/it]
Loading dataset:  27%|##6       | 4/15 [00:08&lt;00:23,  2.13s/it]
Loading dataset:  33%|###3      | 5/15 [00:11&lt;00:22,  2.25s/it]
Loading dataset:  40%|####      | 6/15 [00:12&lt;00:18,  2.04s/it]
Loading dataset:  47%|####6     | 7/15 [00:15&lt;00:16,  2.10s/it]
Loading dataset:  53%|#####3    | 8/15 [00:17&lt;00:14,  2.01s/it]
Loading dataset:  60%|######    | 9/15 [00:18&lt;00:11,  1.89s/it]
Loading dataset:  67%|######6   | 10/15 [00:20&lt;00:09,  1.86s/it]
Loading dataset:  73%|#######3  | 11/15 [00:22&lt;00:07,  1.88s/it]
Loading dataset:  80%|########  | 12/15 [00:26&lt;00:07,  2.54s/it]
Loading dataset:  87%|########6 | 13/15 [00:28&lt;00:04,  2.31s/it]
Loading dataset:  93%|#########3| 14/15 [00:29&lt;00:02,  2.14s/it]
Loading dataset: 100%|##########| 15/15 [00:31&lt;00:00,  2.09s/it]
Loading dataset: 100%|##########| 15/15 [00:31&lt;00:00,  2.13s/it]
[2022-06-06 15:19:56,846] [33996] [MainThread] [INFO] (monailabel.tasks.train.basic_train:227) - 0 - Records for Training: 15
[2022-06-06 15:19:56,850] [33996] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:696) - Engine run resuming from iteration 0, epoch 0 until 50 epochs
[2022-06-06 15:19:57,257] [33996] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:138) - Restored all variables from C:\Users\mikeb\apps\radiology\model\pretrained_deepedit_dynunet.pt
2022-06-06 15:20:00,406 - INFO - Number of simulated clicks: 6
[2022-06-06 15:20:04,627] [33996] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:269) - Epoch: 1/50, Iter: 1/15 -- train_loss: 1.7812
[2022-06-06 15:20:05,039] [33996] [MainThread] [ERROR] (ignite.engine.engine.SupervisedTrainer:853) - Current run is terminating due to exception: CUDA out of memory. Tried to allocate 128.00 MiB (GPU 0; 4.00 GiB total capacity; 2.68 GiB already allocated; 0 bytes free; 2.93 GiB reserved in total by PyTorch)
[2022-06-06 15:20:05,040] [33996] [MainThread] [ERROR] (ignite.engine.engine.SupervisedTrainer:178) - Exception: CUDA out of memory. Tried to allocate 128.00 MiB (GPU 0; 4.00 GiB total capacity; 2.68 GiB already allocated; 0 bytes free; 2.93 GiB reserved in total by PyTorch)
</code></pre>
<p>Here is the command used to start the server:</p>
<pre><code class="lang-auto">monailabel start_server --app apps/radiology --studies datasets/liver_test_from_scratch/ --conf models deepedit --conf use_pretrained_model false --conf heuristic_planner true
</code></pre>
<p>Also, despite the <code>use_pretrained_model false</code>, inference seems to be using a pretrained model (I get a spleen segmentation when I press Next Sample, which must be coming from a pretrained model).    I tried the <code>heuristic_planner true</code> option because it sounded like this would choose an appropriate image grid size/spacing to use for training, based on the available GPU memory.</p>
<p>However, I see this section in the output:</p>
<pre><code class="lang-auto">[2022-06-06 15:19:14,021] [33996] [MainThread] [INFO] (monailabel.utils.others.generic:147) - Using nvidia-smi command
[2022-06-06 15:19:14,345] [33996] [MainThread] [INFO] (monailabel.utils.others.planner:71) - Available GPU memory: {0: 2100} in MB
[2022-06-06 15:19:14,345] [33996] [MainThread] [INFO] (monailabel.utils.others.generic:147) - Using nvidia-smi command
[2022-06-06 15:19:14,393] [33996] [MainThread] [INFO] (monailabel.utils.others.planner:75) - Spacing: [1. 1. 2.]; Spatial Size: [1, 1, 256]
</code></pre>
<p>I see the default spatial size is [48,48,32], which makes me wonder if [1,1,256], presumably generated by the heuristics planner, is reasonable.</p>
<p>I am encouraged that training began (and that epoch 0 may have finished?), but am not sure how to go about troubleshooting this GPU memory error. I have an NVIDIA GeForce GTX 1050 Ti with Max-Q with 4 GB of memory on the GPU. If this is far too low specs for a segmentation problem like this, what would be a reasonable size down-sampled image volume I could try which would be able to run?</p>

---

## Post #70 by @diazandr3s (2022-06-07 00:56 UTC)

<p>Thanks, <a class="mention" href="/u/mikebind">@mikebind</a>.</p>
<p>My reply inline:</p>
<blockquote>
<p>Also, despite the ‘use_pretrained_model false’, inference seems to be using a pretrained model (I get a spleen segmentation when I press Next Sample, which must be coming from a pretrained model).</p>
</blockquote>
<p>This could be because there is a .pt file downloaded in the model folder. Please make sure there is nothing in there.</p>
<blockquote>
<p>I tried the ‘heuristic_planner true’ option because it sounded like this would choose an appropriate image grid size/spacing to use for training, based on the available GPU memory.</p>
</blockquote>
<p>That’s right. It selects the image size based on the available GPU. From what you’ve shared, the actual available GPU is 2100 MB:</p>
<pre><code class="lang-auto">Available GPU memory: {0: 2100} in MB
</code></pre>
<blockquote>
<p>I see the default spatial size is [48,48,32], which makes me wonder if [1,1,256], presumably generated by the heuristics planner, is reasonable.</p>
</blockquote>
<p>Yes, <code>[1, 1, 256]</code> is what the heuristic planner recommends. However, this spatial size isn’t reasonable <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=12" title=":confused:" class="emoji" alt=":confused:" loading="lazy" width="20" height="20"></p>
<blockquote>
<p>I have an NVIDIA GeForce GTX 1050 Ti with Max-Q with 4 GB of memory on the GPU. If this is far too low specs for a segmentation problem like this, what would be a reasonable size down-sampled image volume I could try which would be able to run?</p>
</blockquote>
<p>As I mentioned before, the actual GPU memory available is 2100 MB. MONAI Label could train a model with a minimum ~3200 MB of memory and on an image size of <code>[64, 64, 32]</code>. However, this size could be too small for some segmentation tasks.</p>
<p>Then, my suggestion is to try the Segmentation model instead. Different to DeepEdit model, the Segmentation model works on patches instead of the whole volume.</p>
<p>For the Segmentation model, you should first update the label name <a href="https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/lib/configs/segmentation.py#L33" rel="noopener nofollow ugc">here</a>, change <a href="https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/lib/configs/segmentation.py#L64-L65" rel="noopener nofollow ugc">these values</a> to <code>(32, 32, 32)</code> and then run the following command:</p>
<pre><code class="lang-auto">monailabel start_server --app apps/radiology --studies datasets/liver_test_from_scratch/ --conf models segmentation --conf use_pretrained_model false
</code></pre>
<p>Hope the patch size fits into 2100 MB. You could also try reducing the network size <a href="https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/lib/configs/segmentation.py#L68" rel="noopener nofollow ugc">here</a></p>
<p>Please keep us posted.</p>

---

## Post #71 by @mikebind (2022-06-07 05:59 UTC)

<p>Thank you <a class="mention" href="/u/diazandr3s">@diazandr3s</a>!  I have taken your suggestions to use the <code>segmentation</code> model instead of <code>deepedit</code> and changed the spatial size to <code>(32,32,32)</code> and was able to successfully train a model through 50 epochs with a reported accuracy of 91%.  This created <code>segmentation.pt</code> in <code>apps/radiology/model/</code>.  However, I now get <code>Failed to run inference in MONAI Label Server</code> errors when trying to load a new image volume using “Next Sample”.  When this failed, I tried closing out Slicer and shutting down the monailabel server and restarting them (because I had changed a file name and thought that the problem might have been due to a cached list of file names).   I copied the full output of the monailabel server into this gist: <a href="https://gist.github.com/mikebind/618d56013c67ac449c225a322d2e7af3" class="inline-onebox">Troubleshooting output of monailabel when inference failed · GitHub</a><br>
That seems like it might be complaining about using .nii.gz extension instead of .seg.nrrd for multichannel 4D label, but I’m not sure whether this actually is relevant or not.  I am using a single label, and it trained fine using .nii.gz label image volumes. The “Result File” listed at the end is not present in the listed AppData/Local/Temp/ folder, but I’m not sure whether this is because it was never generated or because it was temporary and was cleaned up. The log for the associated Slicer session is available at this gist: <a href="https://gist.github.com/mikebind/d24f1c2891d0dedb91274fbb7c66364a" class="inline-onebox">Slicer error/info log associated with failed MONAILabel inference · GitHub</a></p>
<p>My interpretation is that something went wrong when generating the inference segmentation, but I don’t see a clear error message indicating where things went wrong.  The monailabel sever seems to report that it created a temporary nii.gz file which I assume is the inferred segmentation volume, but Slicer seems to report 404 errors when trying to retrieve the inferred volume from the server (I assume the “original” tag for labels is the inferred one? whereas the “final” tag for labels is the gold-standard one for model performance evaluation).</p>
<p>Thanks everyone for the help so far!  Any suggestions about how to troubleshoot this error?</p>

---

## Post #72 by @mau_igna_06 (2022-06-07 09:06 UTC)

<p>Maybe the tags are not correct</p>

---

## Post #73 by @diazandr3s (2022-06-07 10:23 UTC)

<p>Glad to hear you’ve trained a model, <a class="mention" href="/u/mikebind">@mikebind</a>. Thanks for sharing your experience.<br>
Regarding your questions/comments:</p>
<pre><code class="lang-auto">However, I now get `Failed to run inference in MONAI Label Server` errors when trying 
to load a new image volume using “Next Sample”.
</code></pre>
<p>This is a bit strange <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=12" title=":confused:" class="emoji" alt=":confused:" loading="lazy" width="20" height="20"><br>
Are you using the latest Slicer version? (i.e. 5.X.X)<br>
From what I can see in the logs, inference ran fine and the prediction has been created.</p>
<pre><code class="lang-auto">[2022-06-06 22:24:24,386] [13192] [MainThread] [INFO] (monailabel.interfaces.tasks.infer:294) - ++ Latencies =&gt; Total: 39.8244; Pre: 9.6867; Inferer: 7.8800; Invert: 0.0000; Post: 1.8089; Write: 19.5964

[2022-06-06 22:24:24,386] [13192] [MainThread] [INFO] (monailabel.interfaces.tasks.infer:318) - Result File: C:\Users\mikeb\AppData\Local\Temp\tmpz1nqaonu.nii.gz

[2022-06-06 22:24:24,388] [13192] [MainThread] [INFO] (monailabel.interfaces.tasks.infer:319) - Result Json Keys: ['label_names', 'latencies']
</code></pre>
<p>Regarding this:</p>
<p><code>That seems like it might be complaining about using .nii.gz extension instead of .seg.nrrd for multichannel 4D label, but I’m not sure whether this actually is relevant or not.</code></p>
<p>That’s just a warning. It is not causing any issue <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p><code>The “Result File” listed at the end is not present in the listed AppData/Local/Temp/ folder, but I’m not sure whether this is because it was never generated or because it was temporary and was cleaned up.</code></p>
<p>Exactly, the temp (<code>C:\Users\mikeb\AppData\Local\Temp\</code>) is created and cleaned up after Slicer reads it.</p>
<p><code>My interpretation is that something went wrong when generating the inference segmentation, but I don’t see a clear error message indicating where things went wrong.</code></p>
<p>I don’t see errors in the logs. Inference went well</p>
<p><code>The monailabel sever seems to report that it created a temporary nii.gz file which I assume is the inferred segmentation volume, but Slicer seems to report 404 errors when trying to retrieve the inferred volume from the server</code></p>
<p>Please try the latest Slicer version and let us know</p>
<p><code>(I assume the “original” tag for labels is the inferred one? whereas the “final” tag for labels is the gold-standard one for model performance evaluation).</code></p>
<p>That’s right, <code>final</code> tag is used for ground-truth and <code>original</code> for model prediction.</p>
<p>There is another way of checking that inference is running well. For this, do batch inference from the browser and check the generated files in original folder. <a href="https://drive.google.com/file/d/1FodMF3p9fFW60csoBZJft-YDJgxOPsck/view?usp=sharing" rel="noopener nofollow ugc">In this video,</a> I show how you can do that using the segmentation model. It takes a bit more time than usual to perform inference as the liver images I used for the video are quite big.</p>
<p>Hope that helps,</p>

---

## Post #74 by @mikebind (2022-06-07 15:29 UTC)

<p>Yes, I am using a very recent Slicer (5.1.0-2022-06-01), downloaded at the same time as I got the weekly MONAILabel.  <a class="mention" href="/u/diazandr3s">@diazandr3s</a>, I followed your video using the same monailabel server I had been using, and the inference ran successfully and created an image volume in the <code>labels/original</code> subfolder.<br>
I tried to get this to load in Slicer by using the “Tools” → “Import label” function of the MONAILabel extension in Slicer, but got the following error:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "C:/Users/mikeb/AppData/Local/NA-MIC/Slicer 5.1.0-2022-06-01/NA-MIC/Extensions-30987/MONAILabel/lib/Slicer-5.1/qt-scripted-modules/MONAILabel.py", line 1360, in onImportLabel
    self.updateSegmentationMask(self.ui.labelPathLineEdit.currentPath, self.info["labels"])
  File "C:/Users/mikeb/AppData/Local/NA-MIC/Slicer 5.1.0-2022-06-01/NA-MIC/Extensions-30987/MONAILabel/lib/Slicer-5.1/qt-scripted-modules/MONAILabel.py", line 1658, in updateSegmentationMask
    labelImage = sitk.ReadImage(in_file)
  File "C:\Users\mikeb\AppData\Local\NA-MIC\Slicer 5.1.0-2022-06-01\lib\Python\lib\site-packages\simpleitk-2.2.0rc2.post15-py3.9-win-amd64.egg\SimpleITK\extra.py", line 357, in ReadImage
    return reader.Execute()
  File "C:\Users\mikeb\AppData\Local\NA-MIC\Slicer 5.1.0-2022-06-01\lib\Python\lib\site-packages\simpleitk-2.2.0rc2.post15-py3.9-win-amd64.egg\SimpleITK\SimpleITK.py", line 8126, in Execute
    return _SimpleITK.ImageFileReader_Execute(self)
RuntimeError: Exception thrown in SimpleITK ImageFileReader_Execute: D:\D\P\S-0-build\SimpleITK\Code\IO\src\sitkImageReaderBase.cxx:105:
sitk::ERROR: Unable to determine ImageIO reader for "C:/Users/mikeb/datasets/liver_test_from_scratch/labels/original/test_ircad_e20_liver.nii.gz"
</code></pre>
<p>A separate Slicer instance also cannot open this file.  When I tried to take a look at the nifti header information by un-gzipping the file using 7zip, 7zip reports that it is not a gzipped file.  If I take a look at the original file with Notepad++, I can see that it is actually an NRRD file created by pynrrd, not a nii.gz file.  So, it appears that perhaps monailabel created an NRRD label file, but because the source image was named with an nii.gz extension the created file was given the same name, creating a mismatch between the extension and the actual file type.  If I change the extension to <code>.seg.nrrd</code>, then Slicer can load it.  If I change the extension to <code>.nrrd</code>, Slicer complains that it has 2 components when only 1 is allowed (<code>sizes</code> in the header is <code>2 512 512 225</code>, though there is only one segment)</p>
<p>Do I need to change the monailabel configuration in some way to fix or compensate for the mismatch between input and output formats here?</p>

---

## Post #75 by @diazandr3s (2022-06-07 15:48 UTC)

<p>Thanks for the detailed info, <a class="mention" href="/u/mikebind">@mikebind</a>.</p>
<p>Last week I fixed an issue similar to/related to this one.</p>
<p>Let’s make sure you don’t have a weekly version that still has that issue.</p>
<p>Please check that the infer transforms in the segmentation model are exactly like these ones: <a href="https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/lib/infers/segmentation.py#L74-L75" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel/segmentation.py at main · Project-MONAI/MONAILabel · GitHub</a></p>
<p>If they’re not, that’s the issue. Changed those, remove the original folder and run inference again.</p>
<p>Please let us know.</p>

---

## Post #76 by @mikebind (2022-06-07 16:55 UTC)

<p>Yes, that fixed the issue!  I was able to re-run the inference successfully and get a segmentation.  I was able to edit that segmentation using scribbles and segment editor tools and submit the new label.  I ran the training again and that also completed successfully and increased the overall accuracy to 95%.  Thanks so much for your quick help!!</p>

---

## Post #77 by @diazandr3s (2022-06-07 17:40 UTC)

<p>Superb! Glad to hear this <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
Thanks for letting us know, <a class="mention" href="/u/mikebind">@mikebind</a></p>

---

## Post #78 by @rbumm (2022-06-08 07:44 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="76" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>I was able to re-run the inference</p>
</blockquote>
</aside>
<p>How did you re-run the inference <a class="mention" href="/u/mikebind">@mikebind</a>?</p>

---

## Post #79 by @rbumm (2022-06-08 08:00 UTC)

<aside class="quote no-group" data-username="diazandr3s" data-post="68" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/diazandr3s/48/9973_2.png" class="avatar"> diazandr3s:</div>
<blockquote>
<p>the user should make sure that segments/labels consistently use the same number for each segment in all volumes</p>
</blockquote>
</aside>
<p>Still not clear to me how the user should do this. Would be great if you could post your workflow on how to check/modify the “segment number”. You do not mean number of segments? It is clear that we should use always use the same segment count and should not modify the segment order or names.</p>

---

## Post #80 by @diazandr3s (2022-06-08 12:54 UTC)

<p>This is a great question, <a class="mention" href="/u/rbumm">@rbumm</a></p>
<p>I meant the number associated with each segment/label, not the number of segments. The number of segments you define or know when you start (i.e. only liver or lungs + airways, etc).</p>
<p>There is no single way of verifying this and it is not easy to thoroughly check all labels.</p>
<p>I see there are ‘label sources’:</p>
<p>1/ User has the segmentations already created</p>
<p>This case covers the use of publicly available datasets such as <a href="http://medicaldecathlon.com/" rel="noopener nofollow ugc">Medical Segmentation Decathlon</a>, <a href="https://www.synapse.org/#!Synapse:syn3193805/wiki/217789" rel="noopener nofollow ugc">BTCV</a>, or labels created by a different software than 3D Slicer</p>
<p>2/ User manually creates the labels using Slicer</p>
<p>3/ User creates more labels using MONAI Label + manual tools in 3D Slicer</p>
<p>The way I quickly verify this is by using:</p>
<p>1/ A Python algorithm that reads and lists the unique values in the label files, AND<br>
2/  Use ITK-SNAP to check that a certain organ has the same value in different images</p>
<p>This is how I discover that teeth labels (<a href="https://projectweek.na-mic.org/PW36_2022_Virtual/Projects/AutomaticSegmentationofTeethandAlveolarBone/" class="inline-onebox" rel="noopener nofollow ugc">NA-MIC Project Weeks | Website for NA-MIC Project Weeks</a>) were not consistently segmented using the same number.</p>
<p><a href="https://drive.google.com/file/d/14iYDv4zaDADM0AbEWg02XLwzNymzmYuJ/view?usp=sharing" rel="noopener nofollow ugc">Here is a short video</a> showing how I checked the label numbers in ITK-SNAP.</p>
<p>There should be a more efficient way of checking this.</p>
<p>I think the most important thing here is to make sure we consistently annotate the volumes in the first place.</p>
<p>Hope this helps. Please let me know.</p>

---

## Post #81 by @mikebind (2022-06-08 15:25 UTC)

<p>Before starting, I deleted all the previously created label images in the <code>labels/original/</code> folder (in my case this was just one image because I only had one unlabeled image I had added so far). To re-run the inference, I used the web browser interface to the server by going to <a href="http://127.0.0.1:8000/" rel="noopener nofollow ugc">http://127.0.0.1:8000/</a> in the browser URL bar.</p>
<p>I clicked on the<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79b2975048f3bfd77eafed8bd5d862141bbaf590.png" alt="image" data-base62-sha1="hmAp19cGqPbbfWb7fBP8VgWQbSg" width="561" height="78"><br>
line, clicked on “Try it out”, and filled out “segmentation” as the model (because the server I started is using the “segmentation” rather than “deepedit” model, and then selected “unlabeled” to run inference on just all unlabeled images from the source folder (which, for me, was again just one image), and then clicked “Execute”.</p>
<p>I got this procedure from following along on this video that <a class="mention" href="/u/diazandr3s">@diazandr3s</a>  shared above: <a href="https://drive.google.com/file/d/1FodMF3p9fFW60csoBZJft-YDJgxOPsck/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">batch-inference.mp4 - Google Drive</a></p>

---

## Post #82 by @rbumm (2022-06-08 18:59 UTC)

<aside class="quote no-group" data-username="diazandr3s" data-post="80" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/diazandr3s/48/9973_2.png" class="avatar"> diazandr3s:</div>
<blockquote>
<p>Hope this helps. Please let me know.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/diazandr3s">@diazandr3s</a>  Not yet <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> Have been trying this now on/off for more than two weeks and I would like to get this running before the <a href="https://github.com/NA-MIC/ProjectWeek/blob/master/PW37_2022_Virtual/MONAILabel_Workshop.md">workshop</a> locally in order to be able to assist other people.</p>
<p>What I have done so far:<br>
Set up Monailabel on two different systems (laptop 6 GB GPU memory, desktop 16 GB GPU memory) and now switched to the desktop completely due to inconsistent results and -9 server error messages on the laptop.<br>
Set ML up in WSL Ubuntu, enabled CUDA, did a parallel setup in Windows 11 native, trained, infered, technically it seems to work in both worlds without error messages.</p>
<p>The goal is to train ML with the Lung CT Segmenter to detect “right lung” in total, “left lung” in total, and kind of an airway. It never worked so far. Tried this with lung CT segmenter input as well as with manual segmentations using the ML predefined segments.</p>
<p>All I get is an <a href="https://discourse.slicer.org/t/how-to-start-with-monailabel-for-new-models/21063/61">ugly block segmentation</a> when I use the ML auto segmentation upon “Next sample”…<br>
This is my start_server line:</p>
<pre><code class="lang-auto">monailabel start_server --app ./apps/radiology --studies ./datasets/Task06_Lung/imagesTr --conf models segmentation
</code></pre>
<p>Could you provide a complete and working application that I could start training with the Task06_Lung dataset before the <a href="https://github.com/NA-MIC/ProjectWeek/blob/master/PW37_2022_Virtual/MONAILabel_Workshop.md">MONAILabel workshop</a>?</p>
<p>Kind regards<br>
Rudolf</p>

---

## Post #84 by @diazandr3s (2022-06-08 19:30 UTC)

<p>Thanks for your time on this, <a class="mention" href="/u/rbumm">@rbumm</a> and sorry for the inconvenience.</p>
<p>The first thing I’d like you to check is the labels in the Task06_Lung dataset. What I see as labels in that dataset are actually lung tumors, not lungs and airway segmentation. See the following image:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec185aa7f885e1f46fe6c8bf808d470a7878d45b.jpeg" data-download-href="/uploads/short-url/xGARpBoQSzXBtiL9cEm4Cyo0RUT.jpeg?dl=1" title="sample-lung-dataset.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ec185aa7f885e1f46fe6c8bf808d470a7878d45b_2_690x373.jpeg" alt="sample-lung-dataset.PNG" data-base62-sha1="xGARpBoQSzXBtiL9cEm4Cyo0RUT" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ec185aa7f885e1f46fe6c8bf808d470a7878d45b_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ec185aa7f885e1f46fe6c8bf808d470a7878d45b_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ec185aa7f885e1f46fe6c8bf808d470a7878d45b_2_1380x746.jpeg 2x" data-dominant-color="3D3D3D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sample-lung-dataset.PNG</span><span class="informations">1917×1039 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I might be using a different version of that dataset.</p>
<p>I’m happy to meet on Teams/Zoom early Monday if you’re available.</p>
<p>Please let me know.</p>

---

## Post #85 by @rbumm (2022-06-08 19:46 UTC)

<aside class="quote no-group" data-username="diazandr3s" data-post="84" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/diazandr3s/48/9973_2.png" class="avatar"> diazandr3s:</div>
<blockquote>
<p>I’m happy to meet on Teams/Zoom early Monday if you’re available</p>
</blockquote>
</aside>
<p>Great, absolutely. Monday is fine.</p>

---

## Post #86 by @rbumm (2022-06-08 19:48 UTC)

<aside class="quote no-group" data-username="diazandr3s" data-post="84" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/diazandr3s/48/9973_2.png" class="avatar"> diazandr3s:</div>
<blockquote>
<p>What I see as labels in that dataset are actually lung tumors</p>
</blockquote>
</aside>
<p>Noticed that too and thought that I had not used those labels, but will check again</p>

---

## Post #87 by @diazandr3s (2022-06-08 22:28 UTC)

<p>Superb! Just sent you the Teams link for next Monday at 13:30 UK time. Please confirm.</p>

---

## Post #88 by @rbumm (2022-06-15 09:15 UTC)

<p>After great meetings with <a class="mention" href="/u/diazandr3s">@diazandr3s</a> we were able to set the MONAILabel lung segmentation up from scratch, train a model, and autosegment lungs and airways.</p>
<p>Windows: We recommend doing this in Windows 11 using Powershell.<br>
<a href="https://docs.monai.io/projects/label/en/latest/installation.html#windows">Follow the instructions from the ML Github</a> to install the prerequisites and ML itself.</p>
<p>All in the above link:</p>
<ul>
<li>Test that CUDA is available.</li>
<li>Fork MONAILabel from Github</li>
<li>Download ML radiology app</li>
<li>Download lung dataset</li>
</ul>
<p>Use Slicer 5.1 and ML extension<br>
We found that the Deepedit model is best suited for our task.<br>
We modified  the deepedit.py in /apps/lib/conf as follows:</p>
<pre><code class="lang-auto">        # Single label
        self.labels = {
            "right lung-1": 1,
            "left lung-2": 2,
            "airways-3": 3,
            "background": 0,
        }

        # Number of input channels - 4 for BRATS and 1 for spleen
        self.number_intensity_ch = 1

        network = self.conf.get("network", "dynunet")

        # Model Files
        self.path = [
            os.path.join(self.model_dir, f"pretrained_{self.name}_{network}.pt"),  # pretrained
            os.path.join(self.model_dir, f"{self.name}_{network}.pt"),  # published
        ]

        # Download PreTrained Model
        if strtobool(self.conf.get("use_pretrained_model", "false")):
            url = f"{self.conf.get('pretrained_path', self.PRE_TRAINED_PATH)}/deepedit_{network}_singlelabel.pt"
            download_file(url, self.path[0])

        self.target_spacing = (1.0, 1.0, 1.0)  # target space for image
        self.spatial_size = (128, 128, 64)  # train input size

</code></pre>
<p>Then we started the ML server with:</p>
<pre><code class="lang-auto">monailabel start_server --app apps/radiology --studies datasets/Task06_Lung/imagesTr --conf models deepedit
</code></pre>
<p>In 3D Slicer, we connected to ML Server in the ML extension and pressed “Next sample”.<br>
Then we made a couple of lung and airway segmentation <em><a href="https://github.com/rbumm/SlicerLungCTAnalyzer">with Lung CT Segmenter</a></em> and “submit Label” for each in ML.</p>
<p>We trained a test model with only 50 epochs, and did an autosegmentation on the “next sample”.<br>
The result was still suboptimal, so I produced 9 more labels in Lung CT Segmenter, uploaded them via “submit Label” to ML one by one, then trained the model with CUDA on my GTX 3070 Ti for 1000 epochs (10 hours)<br>
After that, autosegmentation was very fast and shows promising results:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/111532765a521ee4b2c8222245997dd0fbb3520e.jpeg" data-download-href="/uploads/short-url/2r7wXwAZXA2fCsYl0Gu8unnc5KC.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/111532765a521ee4b2c8222245997dd0fbb3520e_2_690x408.jpeg" alt="image" data-base62-sha1="2r7wXwAZXA2fCsYl0Gu8unnc5KC" width="690" height="408" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/111532765a521ee4b2c8222245997dd0fbb3520e_2_690x408.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/111532765a521ee4b2c8222245997dd0fbb3520e.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/111532765a521ee4b2c8222245997dd0fbb3520e.jpeg 2x" data-dominant-color="4E4A4C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">928×550 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #89 by @diazandr3s (2022-06-15 09:22 UTC)

<p>Many thanks for the detailed message, <a class="mention" href="/u/rbumm">@rbumm</a> <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #90 by @deboshree_roy (2022-10-25 12:29 UTC)

<p>Currently, my goal is to use my pre-trained model in 3DSlicer for interactive segmentation. The discussions in the group seem to be in the same line and illuminating. I am looking for suggestions in my work. The procedure that I followed is -<br>
I have generated a pre-trained model and added the path of the .pth file to the lib → conf → deepedit.py file. I edited the labels accordingly.</p>
<p>On starting the monailabel server and loading the model, I run the autosegment. I can see the same .pth file being loaded in the cmd window.</p>
<p>The model developed (.pth) has been tested to generate accurate results. On running in 3D Slicer it generates completely odd results.</p>
<p>My doubt is that my procedure to load the .pth file into the module is correct ? Do I need to do anything more ? Perhaps in the infer folder ?</p>
<p>Thanks</p>

---

## Post #92 by @Spiros_Karkavitsas (2023-02-10 21:56 UTC)

<p>Hello, I have a similar problem with this ‘‘CUDA error’’ when I am using the App radiology app and the spleen dataset which was used in an example in a tutorial.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9d7ebcc541cfdede040c1cec58d986b4c74d4e5.jpeg" data-download-href="/uploads/short-url/zEduVUtpMbGTPSX2tZ9ls8DcxAp.jpeg?dl=1" title="Screenshot_10" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9d7ebcc541cfdede040c1cec58d986b4c74d4e5_2_690x21.jpeg" alt="Screenshot_10" data-base62-sha1="zEduVUtpMbGTPSX2tZ9ls8DcxAp" width="690" height="21" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9d7ebcc541cfdede040c1cec58d986b4c74d4e5_2_690x21.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9d7ebcc541cfdede040c1cec58d986b4c74d4e5_2_1035x31.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9d7ebcc541cfdede040c1cec58d986b4c74d4e5_2_1380x42.jpeg 2x" data-dominant-color="222222"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_10</span><span class="informations">1600×50 29.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #93 by @rbumm (2023-02-11 12:22 UTC)

<p>This indicates that the GPU of your computer has insufficient dedicated video RAM - at least 6 GB is recommended to run the server. Please check your NVIDIA control panel → System Information.<br>
You may consider upgrading your GPU to a more recent model or running the server in the cloud.</p>

---

## Post #94 by @Spiros_Karkavitsas (2023-02-11 12:40 UTC)

<p>Hello and thank you very much for your answer !!</p>
<p>Actually,I checked all that when I was installing MONAI.</p>
<p>My GPU is GeForce MX450 and as I was searching it is compatible with CUDA 10.0 to 10.2.</p>
<p>What GPU in your opinion I should install so that MONAI can work ?</p>
<p>Στις Σάβ, 11 Φεβ 2023, 13:23 ο χρήστης Rudolf Bumm via 3D Slicer Community &lt;<a href="mailto:notifications@slicer.discoursemail.com">notifications@slicer.discoursemail.com</a>&gt; έγραψε:</p>

---

## Post #95 by @rbumm (2023-02-11 13:21 UTC)

<p>We would <a href="https://discourse.slicer.org/t/new-extension-fully-automatic-whole-body-ct-segmentation-in-2-minutes-using-totalsegmentator/26710/51">recommend a RTX 3060</a> (12 GB RAM)  or RTX 3090 (24 GB)  for current CUDA based deep learning purposes. Got a MONAILabel server running on a GTX 1060 (6 GB) but this is the very low limit.</p>

---

## Post #96 by @Spiros_Karkavitsas (2023-02-11 15:34 UTC)

<p>Thank you a lot for your answers, you saved me valuable time for this issue.</p>
<p>Judging from the prices of these graphic cards,</p>
<p>Do you believe running MONAI in the cloud as you said would be a valid solution to this situation ?</p>

---

## Post #97 by @Spiros_Karkavitsas (2023-02-11 15:40 UTC)

<p>If yes, which cloud do you suggest for AI procedures such as this?</p>

---

## Post #98 by @pieper (2023-02-11 16:57 UTC)

<p>The <a href="https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/SlicerCloud/">instructions here for AWS</a> are convenient for windows users.  And linux instructions are <a href="https://learn.canceridc.dev/cookbook/virtual-machines/idc-desktop">here for Google</a> but similar techniques can be used on other cloud providers.  The nice thing about these environments is that there are many GPU options and you only pay for the time you need.</p>

---

## Post #99 by @Spiros_Karkavitsas (2023-02-11 17:16 UTC)

<p>Thank you very much:) Kind of basic question, Docker for Windows cannot work in this case?</p>

---

## Post #100 by @pieper (2023-02-11 17:22 UTC)

<p>You can use docker on any of these platforms if you find it useful.  Personally I find that for the cloud it’s more convenient just to use the native OS so there’s only one layer of GPU drivers to worry about.</p>

---

## Post #101 by @Spiros_Karkavitsas (2023-02-13 14:52 UTC)

<p>Hello again</p>
<p>I just created an account on AWS for window users. However, I cannot download the template you provided in a link to use it in the stack…</p>
<p>Also, I have a question regarding the cost of the AWS. If the MONAILabel is under the free use of AWS or not.</p>
<p>Thank you a lot for your valuable time and help<br>
Best<br>
Spiros</p>

---

## Post #102 by @Spiros_Karkavitsas (2023-02-13 15:14 UTC)

<p>My bad…I downloaded it.</p>

---

## Post #103 by @Spiros_Karkavitsas (2023-02-13 15:29 UTC)

<p>Hello again</p>
<p>I followed the instructions for AWS and tried to create a cloud for MONAI using the already template.</p>
<p>However, I got this ROLLBACK_COMPLETE message:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2242451185da5e574fa38f852e528cba24be19b.jpeg" data-download-href="/uploads/short-url/rHs3TAXX1pvjq64jGWPEMkmGgZ5.jpeg?dl=1" title="Screenshot_20" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2242451185da5e574fa38f852e528cba24be19b_2_690x225.jpeg" alt="Screenshot_20" data-base62-sha1="rHs3TAXX1pvjq64jGWPEMkmGgZ5" width="690" height="225" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2242451185da5e574fa38f852e528cba24be19b_2_690x225.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2242451185da5e574fa38f852e528cba24be19b_2_1035x337.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2242451185da5e574fa38f852e528cba24be19b_2_1380x450.jpeg 2x" data-dominant-color="F6F7F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20</span><span class="informations">1833×598 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>What am I doing wrong here ?</p>
<p>Best and thank you all for your time,<br>
Spiros.</p>

---

## Post #104 by @rbumm (2023-02-13 15:46 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> maybe we should split this into a new topic? If you agree thanks</p>

---

## Post #105 by @rbumm (2023-02-13 15:54 UTC)

<p>There are more messages in the CloudFormation log and probably you already got something like</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec665967f70331114d089820cf5e3ed7e07af485.png" data-download-href="/uploads/short-url/xJhXQu9mb6dKVzP1Si57XdhikJL.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec665967f70331114d089820cf5e3ed7e07af485_2_689x108.png" alt="image" data-base62-sha1="xJhXQu9mb6dKVzP1Si57XdhikJL" width="689" height="108" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec665967f70331114d089820cf5e3ed7e07af485_2_689x108.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec665967f70331114d089820cf5e3ed7e07af485_2_1033x162.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec665967f70331114d089820cf5e3ed7e07af485.png 2x" data-dominant-color="FBFBFB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1181×185 19.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>further down?</p>
<p>In any case, during setting this up there were two main hurdles that we identified, and afterward fine. You would probably need to contact an amazon representative to get advice on which region (see top right in your Amazon console) you should set up the server  - you´ll get a recommendation for one with high availability of server GPU - and the GPU instance quota of your Amazon account will need to get raised for being able to use them at all.</p>

---

## Post #106 by @Spiros_Karkavitsas (2023-02-13 20:41 UTC)

<p>Prof.Dr. Rudolf Bumm</p>
<p>Thank you very much for your information. I followed the procedure again and I received a similar message like this putting the IP address correctly this time.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3f1995f47e9957cae1274380cdad50860bd9f5e.jpeg" data-download-href="/uploads/short-url/pFR5DtXDWekUOAzthhuS2W5tnCC.jpeg?dl=1" title="Screenshot_21.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3f1995f47e9957cae1274380cdad50860bd9f5e_2_690x148.jpeg" data-base62-sha1="pFR5DtXDWekUOAzthhuS2W5tnCC" alt="Screenshot_21.jpg" width="690" height="148" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3f1995f47e9957cae1274380cdad50860bd9f5e_2_690x148.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3f1995f47e9957cae1274380cdad50860bd9f5e_2_1035x222.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3f1995f47e9957cae1274380cdad50860bd9f5e_2_1380x296.jpeg 2x" data-dominant-color="F8F9F9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_21.jpg</span><span class="informations">1841×396 66.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>So, according to you, I will have to update my current limit of vCPU to create the EC2Instance. For MONAILabel to run, which type of vCPU and how many do you need ?</p>
<p>And kind of basic ( and hoping a valid one…) question, but every time I want to launch and use MONAI I will have to request vCPU to run it ?</p>
<p>Best.<br>
Spiros.</p>

---

## Post #107 by @rbumm (2023-02-14 07:46 UTC)

<p>Hi Spiros,</p>
<p>Yes, you will need to request a raise of your vCPU instance quota to 16 or 32, in particular, the G and VT instance types (last page on the “Limit” Webpage,  and select a good region with high availability of GPUs on AWS. An option as of Feb 2023 is to use Ireland from Europe.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce04d933ebf033e80700cfe5d50cf670e66d0c27.png" data-download-href="/uploads/short-url/towKibiMOgqu6Z16jTNUsx9nfhl.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce04d933ebf033e80700cfe5d50cf670e66d0c27_2_690x277.png" alt="image" data-base62-sha1="towKibiMOgqu6Z16jTNUsx9nfhl" width="690" height="277" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce04d933ebf033e80700cfe5d50cf670e66d0c27_2_690x277.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce04d933ebf033e80700cfe5d50cf670e66d0c27_2_1035x415.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce04d933ebf033e80700cfe5d50cf670e66d0c27_2_1380x554.png 2x" data-dominant-color="E8E8EA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×771 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The limit increase will probably be rejected the first time you try it yourself, here is where you need a regional AWS solution architect to assist you. And it is good to create an institutional AWS account.</p>
<p>Concerning your other question (start GPU whenever run MONAILabel server) please see <a href="https://github.com/Project-MONAI/MONAILabel/discussions/761#discussioncomment-2676897">here</a>.</p>
<p>Maybe <a class="mention" href="/u/diazandr3s">@diazandr3s</a> is aware of a different solution, and in your particular case, the comfort of having a dedicated GPU-powered Windows instance with the option to run 3D Slicer on it is maybe not necessary if you just want to run the MONAILabel server in the cloud.</p>

---

## Post #108 by @evaherbst (2023-06-27 08:31 UTC)

<p>Hi all,</p>
<p>Thanks for this very informative thread, I look forward to testing this on my clinical datasets in the future.</p>
<p>I do not have NVIDIA and therefore do not have CUDA, does this prevent me from using MonaiLabel?</p>
<p>Thank you,<br>
Eva</p>

---

## Post #109 by @rbumm (2023-06-27 10:11 UTC)

<p>Installing MONAILabel is possible, you could use slow inference from pre-trained models and label your data. Training requires CUDA and an NVIDIA GPU.<br>
Please <a href="https://github.com/Project-MONAI/MONAILabel/discussions/761#discussioncomment-2676897">see this thread</a>.</p>

---

## Post #110 by @evaherbst (2023-06-27 10:47 UTC)

<p>Thank you, that is really helpful.<br>
My personal computer does have NVIDIA (my work one has a different GPU) so that approach could work well for me, thanks!</p>

---

## Post #111 by @muratmaga (2023-09-25 04:30 UTC)

<aside class="quote no-group" data-username="diazandr3s" data-post="10" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/diazandr3s/48/9973_2.png" class="avatar"> diazandr3s:</div>
<blockquote>
<p>If the task is multilabel like <a href="https://www.synapse.org/#!Synapse:syn3193805/wiki/217789">this one </a>, then I recommend you to use the <a href="https://github.com/Project-MONAI/MONAILabel/tree/main/sample-apps/deepedit_multilabel">Multilabel DeepEdit App </a>.</p>
</blockquote>
</aside>
<p>I am trying to build a tutorial for multilabel segmentation using MonaiLabel. It has been a while I used monailabel, but the deepedit link above gives 404.</p>
<p>Is it renamed or discontinued?</p>

---

## Post #112 by @rbumm (2023-09-25 05:18 UTC)

<p><a class="mention" href="/u/diazandr3s">@diazandr3s</a> could you comment please?</p>

---

## Post #113 by @diazandr3s (2023-09-25 14:04 UTC)

<p>Hi <a class="mention" href="/u/muratmaga">@muratmaga</a>,</p>
<p>It’s been a while since we changed this model to be DeepEdit only - I think it was on June 13 2022 (<a href="https://github.com/Project-MONAI/MONAILabel/releases/tag/0.4.0" class="inline-onebox" rel="noopener nofollow ugc">Release MONAI Label 0.4.0 · Project-MONAI/MONAILabel · GitHub</a>).</p>
<p>Previously we had one DeepEdit for binary segmentation and another DeepEdit for multilabel (<a href="https://github.com/Project-MONAI/MONAILabel/tree/0.3.2/sample-apps" rel="noopener nofollow ugc">https://github.com/Project-MONAI/MONAILabel/tree/0.3.2/sample-apps</a>). Now it is just DeepEdit - this updated version can do both binary and multilabel segmentation: <a href="https://github.com/Project-MONAI/MONAILabel/tree/main/sample-apps/radiology#deepedit" rel="noopener nofollow ugc">https://github.com/Project-MONAI/MONAILabel/tree/main/sample-apps/radiology#deepedit</a></p>
<p>I’d suggest using the latest MONAI Label version: <a href="https://github.com/Project-MONAI/MONAILabel/releases/tag/0.7.0" class="inline-onebox" rel="noopener nofollow ugc">Release MONAI Label 0.7.0 · Project-MONAI/MONAILabel · GitHub</a></p>
<p>Please let me know if there is anything I can help with.</p>

---

## Post #114 by @muratmaga (2023-09-25 15:11 UTC)

<aside class="quote no-group" data-username="diazandr3s" data-post="113" data-topic="21063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/diazandr3s/48/9973_2.png" class="avatar"> diazandr3s:</div>
<blockquote>
<p>It’s been a while since we changed this model to be DeepEdit only - I think it was on June 13 2022 (<a href="https://github.com/Project-MONAI/MONAILabel/releases/tag/0.4.0">Release MONAI Label 0.4.0 · Project-MONAI/MONAILabel · GitHub </a>).</p>
</blockquote>
</aside>
<p>Thanks, I found the deepedit folder under apps. Last time I had to train a multilabel model from scratch, I had to manually edit the deepedit.py with the label indices and define the spatial resolution of the model (see below). I am not seeing a deepeditp.py, but two other scripts called interaction.py and transform.py. But I still haven’t managed to figure out where to put the new label incides in.</p>
<pre><code class="lang-auto">
class MyApp(MONAILabelApp):
    def __init__(self, app_dir, studies, conf):

        # Zero values are reserved to background. Non zero values are for the labels
        self.label_names = {
            "left lung": 1,
            "cranial lobe": 2,
            "middle lobe": 3,
            "caudal lobe": 4,
            "accessory lobe": 5,
            "left kidney": 6,
            "right kidney": 7,
            "stomach wall": 8,
            "stomach lumen": 9,
            "medial lobe of liver": 10,
            "left lobe of liver": 11,
            "right lobe of liver": 12,
            "caudate lobe of liver": 13,
            "left adrenal": 14,
            "right adrenal": 15,
            "rectum": 16,
            "bladder": 17,
            "left ventricle": 18,
            "right ventricle": 19,
            "left thymic rudiment": 20,
            "right thymic rudiment": 21,
            "third ventricle": 22,
            "mesencephalic vesicle": 23,
            "fourth ventricle": 24,
            "cerebral aqueduct": 25,
            "left lateral ventricle": 26,
            "right lateral ventricle": 27,
            "right olfactory bulb": 28,
            "left olfacotory bulb": 29,
            "right thalamus": 30,
            "left thalamus": 31,
            "right hypothamalus": 32,
            "left hypothalmus": 33,
            "right septal area": 34,
            "left septal area": 35,
            "left neopallial cortex abd amygdala": 36,
            "right neopallial cortex and amygdala": 37,
            "right striatum": 38,
            "left striatum": 39,
            "right ventricular zone": 40,
            "left ventricular zone": 41,
            "pons": 42,
            "left cerebellar primordium ": 43,
            "right cerebellar primordium": 44,
            "midbrain": 45,
            "medulla oblongata": 46,
            "spinal cord": 47,
            "vertebrae": 48,
            "left ventricle chamber": 102,
            "right ventricle chamber": 103,
            "background": 0,
        }

        network = conf.get("network", "dynunet")

        # Use Heuristic Planner to determine target spacing and spatial size based on dataset+gpu
        spatial_size = json.loads(conf.get("spatial_size", "[128, 128, 128]"))
        target_spacing = json.loads(conf.get("target_spacing", "[1.0, 1.0, 1.0]"))
        self.heuristic_planner = strtobool(conf.get("heuristic_planner", "false"))
        self.planner = HeuristicPlanner(spatial_size=spatial_size, target_spacing=target_spacing)
</code></pre>
<p>Again the goal is to train a new multilabel network scratch from a handful of segmented samples.</p>

---

## Post #115 by @diazandr3s (2023-09-25 15:38 UTC)

<p>Hi <a class="mention" href="/u/muratmaga">@muratmaga</a>,</p>
<p>All of this is now located under the <strong>configs</strong> folder. For the deepedit, you can edit the <strong>deepedit.py file</strong>: <a href="https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/lib/configs/deepedit.py#L42" rel="noopener nofollow ugc">https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/lib/configs/deepedit.py#L42</a></p>
<p>Here you can change the spatial size: <a href="https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/lib/configs/deepedit.py#L77" rel="noopener nofollow ugc">https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/lib/configs/deepedit.py#L77</a></p>
<p>Hope this helps,</p>

---

## Post #116 by @muratmaga (2023-09-25 16:15 UTC)

<p>I am working off the docker installation, and having a hard time matching the repos source code structure to what I am seeing under the <code>/opt/monai</code> in docker. Should I be looking somewhere else?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48cbeea09cf2572bd909b778247ffbce7e64b6b8.jpeg" data-download-href="/uploads/short-url/anZiCYRuAdMK2Owua0cVY92wYCk.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48cbeea09cf2572bd909b778247ffbce7e64b6b8_2_431x500.jpeg" alt="image" data-base62-sha1="anZiCYRuAdMK2Owua0cVY92wYCk" width="431" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48cbeea09cf2572bd909b778247ffbce7e64b6b8_2_431x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48cbeea09cf2572bd909b778247ffbce7e64b6b8_2_646x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48cbeea09cf2572bd909b778247ffbce7e64b6b8_2_862x1000.jpeg 2x" data-dominant-color="F6F4F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1053×1220 159 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #117 by @muratmaga (2023-09-25 16:19 UTC)

<p>nevermind, I missed the radiology sample app download step in docker.</p>

---

## Post #118 by @diazandr3s (2023-09-25 17:14 UTC)

<p>Thanks for the update <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #119 by @muratmaga (2023-09-25 17:34 UTC)

<p>Well I am stuck at another level though <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"></p>
<p>I am trying to rearrange the workspace with persistent shares in docker. These are the commands I used to check out the vanilla radiology app and the Spleen dataset:</p>
<pre><code class="lang-auto">monailabel apps --download --name radiology --output /workspace/rad2
monailabel datasets --download --name Task09_Spleen --output /workspace/
</code></pre>
<p>then when I start the server with command:</p>
<pre><code class="lang-auto">monailabel start_server --app /workspace/rad2/radiology/ --studies /workspace/Task09_Spleen/
</code></pre>
<p>I am getting this error:</p>
<pre><code class="lang-auto">---------------------------------------------------------------------------------------
Provide --conf models &lt;name&gt;
Following are the available models.  You can pass comma (,) seperated names to pass multiple
    all, deepedit, deepgrow_2d, deepgrow_3d, localization_spine, localization_vertebra, segmentation, segmentation_spleen, segmentation_vertebra
---------------------------------------------------------------------------------------

[2023-09-25 17:34:14,253] [861] [MainThread] [ERROR] (uvicorn.error:123) - Traceback (most recent call last):
  File "/usr/local/lib/python3.8/dist-packages/starlette/routing.py", line 677, in lifespan
    async with self.lifespan_context(app) as maybe_state:
  File "/usr/local/lib/python3.8/dist-packages/starlette/routing.py", line 566, in __aenter__
    await self._router.startup()
  File "/usr/local/lib/python3.8/dist-packages/starlette/routing.py", line 654, in startup
    await handler()
  File "/usr/local/lib/python3.8/dist-packages/monailabel/app.py", line 108, in startup_event
    instance = app_instance()
  File "/usr/local/lib/python3.8/dist-packages/monailabel/interfaces/utils/app.py", line 50, in app_instance
    app = c(app_dir=app_dir, studies=studies, conf=conf)
  File "/workspace/rad2/radiology/main.py", line 65, in __init__
    exit(-1)
  File "/usr/lib/python3.8/_sitebuiltins.py", line 26, in __call__
    raise SystemExit(code)
SystemExit: -1

[2023-09-25 17:34:14,253] [861] [MainThread] [ERROR] (uvicorn.error:59) - Application startup failed. Exiting.
</code></pre>
<p>any suggestions?</p>

---

## Post #120 by @diazandr3s (2023-09-25 18:19 UTC)

<p>The radiology app has evolved a lot and has now more models than before. For this reason we added a mandatory argument:</p>
<p><code>--conf models</code></p>
<p>In this case, for deepedit it should be something like this:</p>
<pre><code class="lang-auto">monailabel start_server --app /workspace/rad2/radiology/ --studies /workspace/Task09_Spleen/ --conf models deepedit
</code></pre>
<p>Please see here for more examples: <a href="https://github.com/Project-MONAI/MONAILabel/tree/main/sample-apps/radiology#how-to-use-the-app" rel="noopener nofollow ugc">https://github.com/Project-MONAI/MONAILabel/tree/main/sample-apps/radiology#how-to-use-the-app</a></p>

---

## Post #121 by @rbumm (2023-09-26 05:52 UTC)

<p>Maybe time for a new workshop <a class="mention" href="/u/diazandr3s">@diazandr3s</a>? Will there be one next month?</p>

---

## Post #122 by @diazandr3s (2023-09-27 00:23 UTC)

<p>Hi <a class="mention" href="/u/rbumm">@rbumm</a>,</p>
<p>Yes, there will be one for MICCAI: <a href="https://monai.io/monai-tutorial-miccai-2023/" class="inline-onebox" rel="noopener nofollow ugc">Project MONAI - MICCAI 2023 - Tutorial</a></p>
<p>Do you have another event in mind? <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #123 by @ag_gan (2023-11-13 01:26 UTC)

<p>Hi,</p>
<p>I have successfully trained a new model and infer unseen images through 3D Slicer.</p>
<p>But I wondered if it was possible to run inference from command line commands or a Python script. Is it possible to download the output label mask using either commands or a Python script? The reason behind this is so that I don’t have to start the 3D-Slicer application after the model has been trained.</p>
<p>Please let me know if there is a way! Thank you for your help in advance.</p>

---

## Post #124 by @xiang_yao (2023-12-14 07:55 UTC)

<p>Could you please provide more specific information on the differences between Deepedit and Segmentation models？I am not very clear about the differences between these two in practical application.Thanks</p>

---

## Post #125 by @rbumm (2023-12-15 12:41 UTC)

<p>ChatGPT´s response to your question is:</p>
<p>MonaiLabel, an open-source tool focused on medical imaging AI, provides various functionalities including annotation and AI-assisted segmentation. Two key models in MonaiLabel are DeepEdit and Segmentation, and understanding their differences is crucial for their effective application.</p>
<ol>
<li>
<p><strong>DeepEdit Models</strong>:</p>
<ul>
<li><strong>Purpose</strong>: DeepEdit is designed for interactive annotation and editing. It’s particularly useful in scenarios where manual annotation is challenging or time-consuming.</li>
<li><strong>Functionality</strong>: It combines the strengths of AI models and human expertise. Users can provide sparse annotations (like a few clicks), and the model iteratively refines the segmentation based on this input.</li>
<li><strong>Use Cases</strong>: DeepEdit is ideal for complex cases where detailed, precise annotations are required, and where a fully automated approach might not be sufficient. It’s often used in scenarios where the anatomy or pathology varies significantly between patients.</li>
</ul>
</li>
<li>
<p><strong>Segmentation Models</strong>:</p>
<ul>
<li><strong>Purpose</strong>: These models are tailored for automated segmentation tasks. They are designed to work with minimal to no human intervention.</li>
<li><strong>Functionality</strong>: Once trained, segmentation models can automatically segment images based on the learned patterns from the training dataset. They don’t require or usually allow for interactive user input during segmentation.</li>
<li><strong>Use Cases</strong>: Segmentation models are suitable for tasks with well-defined patterns and where the variance between cases is relatively low. They are used in high-throughput environments where manual annotation is impractical.</li>
</ul>
</li>
</ol>
<p>In practical application, the choice between DeepEdit and Segmentation models depends on the specific requirements of your task. If your work requires detailed, user-guided annotation in complex or highly variable images, DeepEdit is the better choice. On the other hand, if you are dealing with a large volume of images with consistent patterns, a Segmentation model would be more efficient and effective.</p>
<p>Remember that the success of both models heavily depends on the quality and representativeness of the training data. For specialized medical imaging tasks, it’s crucial to have a well-curated dataset that reflects the diversity and complexity of the cases you intend to handle.</p>
<p><a href="https://chat.openai.com/share/d5b1b3fd-141a-47bc-9e42-7f17dbf516f6">Link to ChatGPT response</a></p>

---

## Post #126 by @sfat (2023-12-19 04:53 UTC)

<p>Hi I’m running to a strange problem with my monai label on ubuntu. After successfully pip installing it, whatever command i pass to monailabel in command line I get the same response |</p>
<p>Using PYTHONPATH=/home/xxx::/home/xxx/yy/packages_zzzl:/home/xxx/yyy/packages_zzz</p>
<p>I’ve tried installing from git repo but still getting the same response. Can someone help with this please ?</p>

---

## Post #127 by @sfat (2023-12-19 07:59 UTC)

<p>I figured it  … needed to set python alias pointing it to python3</p>

---

## Post #128 by @diazandr3s (2023-12-20 21:16 UTC)

<p>This is amazing! Thanks for sharing this, <a class="mention" href="/u/rbumm">@rbumm</a></p>

---

## Post #129 by @xiang_yao (2024-01-15 08:34 UTC)

<p>Thank you for your professional explanation.This will be of great help to me.</p>
<p>Now I am using MONIAILabel to train a segmentation model for the 1-5 segments of the lumbar spine, which removes the bone cortex.<br>
However, after using Segmentation, the training results were not satisfactory. Later, I switched to Deepedit for training from scratch. When the training accuracy was 80%, I noticed that my dataset’s train loss was around 0.0010, and the accuracy no longer improved, And I don’t know how to use smartEdit and Scribbles for interactive annotation and editing.<br>
The comparison between manually annotated images for training and images automatically segmented by models trained through Deepedit is as follows.<br>
It can be seen that the automatically segmented images have a lot of jagged edges and are not very accurate. I would like to ask if the segmentation model can achieve the level of my own manual segmentation, how to improve segmentation quality, and how to solve jagged edges. <img src="https://emoji.discourse-cdn.com/twitter/face_with_monocle.png?v=12" title=":face_with_monocle:" class="emoji" alt=":face_with_monocle:" loading="lazy" width="20" height="20"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45ff41c5976816becf0cbf1eeaa78e1c3c3806ef.png" data-download-href="/uploads/short-url/9ZdPvWXKxbhEKslEQrkqhIxeqSj.png?dl=1" title="Manual annotation" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45ff41c5976816becf0cbf1eeaa78e1c3c3806ef_2_690x369.png" alt="Manual annotation" data-base62-sha1="9ZdPvWXKxbhEKslEQrkqhIxeqSj" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45ff41c5976816becf0cbf1eeaa78e1c3c3806ef_2_690x369.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45ff41c5976816becf0cbf1eeaa78e1c3c3806ef.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45ff41c5976816becf0cbf1eeaa78e1c3c3806ef.png 2x" data-dominant-color="50515A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Manual annotation</span><span class="informations">846×453 256 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d44bac4eac86d0b7d2718d713f581ac7455d35e.jpeg" data-download-href="/uploads/short-url/6ssJN8oZtT3yyOgccaXw26KF6Vw.jpeg?dl=1" title="MONAILabel Deepedit Segmention" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d44bac4eac86d0b7d2718d713f581ac7455d35e_2_690x371.jpeg" alt="MONAILabel Deepedit Segmention" data-base62-sha1="6ssJN8oZtT3yyOgccaXw26KF6Vw" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d44bac4eac86d0b7d2718d713f581ac7455d35e_2_690x371.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d44bac4eac86d0b7d2718d713f581ac7455d35e_2_1035x556.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d44bac4eac86d0b7d2718d713f581ac7455d35e_2_1380x742.jpeg 2x" data-dominant-color="42414C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">MONAILabel Deepedit Segmention</span><span class="informations">1920×1034 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #130 by @rbumm (2024-01-15 12:42 UTC)

<p>How many training datasets did you use to achieve this result?</p>

---

## Post #131 by @xiang_yao (2024-01-16 01:40 UTC)

<p>There are only four, but I have increased some by copying and rotating the angle, but I am not sure if it is effective. May I ask if it is necessary to have at least 20 different training datasets like the sample datasets.</p>

---

## Post #132 by @muratmaga (2024-01-16 04:59 UTC)

<p>With that such low number of samples, that’s probably what you can expect. Also, I believe MonaiLabel does automatic augmentation (random rotations, and other transformations of the training data), so you don’t have to manually do it.</p>
<p>Is there a reason you are not using TotalSegmentator to do this?</p>

---

## Post #133 by @xiang_yao (2024-01-16 08:50 UTC)

<p>Thank you very much for your answer.</p>
<p>I will increase the amount of data in my training datasets in the future.</p>
<p>The TotalSegmentator can automatically and high-quality divide many organs, but I need to segment the lumbar spine L1-5 in a cylindrical shape like the one in the picture, without including the cortical bone. My understanding of the Total Segmenter is that it cannot achieve the desired effect. Perhaps I should try the segmentation effect.</p>

---

## Post #134 by @mangotee (2024-01-16 17:41 UTC)

<p>Please note that when using the deepedit model, your entire volume will be resampled to the target <code>spatial_size</code> (e.g. 128x128x128 by default). You would need to change that in the configuration in <a href="https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/lib/configs/deepedit.py#L77" rel="noopener nofollow ugc">this line</a>.</p>
<p>By the way, even though ChatGPT’s answer is helpful, it omits an important disctinction between the deepedit and segmentation model <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> In the deepedit model, the <code>target_spacing</code> parameter is ignored, the entire volume is resampled to a voxel grid of <code>spatial_size</code>, which can lead to weird anisotropy issues if the volume is much larger in one of the spatial directions.</p>
<p>To account for that, e.g. as in your case of torso CT scans, I would probably try sth like 128x128x192, to account for the larger FOV in axial direction. Of course, you will need much more VRAM on your GPU to train the model.</p>
<p>Alternatively, to avoid staircase artifacts, you can use the segmentation model, and specify both <code>spatial_size</code> and a target resolution, e.g. 1x1x1mm. Hope that helps <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>(Side note: I agree with <a class="mention" href="/u/muratmaga">@muratmaga</a> - 4 volumes is probably not sufficient to train this problem)</p>

---

## Post #135 by @xiang_yao (2024-01-17 02:09 UTC)

<p>Thank you for making me realize what you said.<br>
This has given me a deeper understanding of the difference between Deepedit and Segmentation.<br>
It also taught me the meaning and purpose of the parameters target_spacing and spatial_size, even though they were originally set to 1.0 * 1.0 * 1.0 and 128 * 128 * 128.<br>
Next, I will try to increase the number of volumes and try Segmentation and Deepedit separately, and modify some of their parameters, such as changing spatial_size to 128x128x192 or 256<em>256</em>384. Then study the effects achieved by both of them, hoping to improve the jagged image.<br>
Another small issue is that I found that there seems to be no parameter spatial_size in the Segmentation model, but a parameter called roi_size. This should be the difference between the two you mentioned, right?</p>

---

## Post #136 by @evaherbst (2024-01-17 09:35 UTC)

<p>Thank you for mentioning this distinction between the settings for deepedit and the segmentation model. I have a question - if I work with scans that are roughly the same volume (but slightly different), is that a problem? I assume the “spatial size” parameter in the segmentation model sets it for the whole model (rather than a scan per scan basis).</p>
<p>I am planning on using MonaiLabel for a future project to train segmentation of CT images, and the cropping of the images might vary slightly.</p>
<p>Is it necessary to crop all training volumes to the same size?</p>
<p>Best,<br>
Eva</p>

---
