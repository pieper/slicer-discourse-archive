# MONAILABEL plugin | pelvis segmentation in MRI

**Topic ID**: 22283
**Date**: 2022-03-03
**URL**: https://discourse.slicer.org/t/monailabel-plugin-pelvis-segmentation-in-mri/22283

---

## Post #1 by @Mahdis_Khodadadi (2022-03-03 11:48 UTC)

<p>Operating system: Windows 10<br>
Slicer version: latest version</p>
<p>I want to segment pelvic in MRI from the SMIR dataset using the MONAILABEL plugin. I have read relatively a lot about this plugin. However, I can’t perform the segmentation well enough yet.</p>
<p>These are the steps I take to do so:<br>
1- connecting the server using the anaconda prompt<br>
2- enabling the plugin in Slicer and loading one image<br>
3- labeling the pelvis manually using the paint button in the scribbles part and the updating<br>
4- click “submit label”<br>
and then repeating the process for some other images while the network is being trained.</p>
<p>After the training process, I actually could not see anything when opening the mask files.<br>
I also encounter these two errors:<br>
" AssertionError: Not a valid Label "<br>
" TypeError: object of type ‘NoneType’ has no len() "</p>
<p>Is it the correct way of using MONAI or am I missing something?<br>
Which aspects should I take into account before starting the process?</p>
<p>I would appreciate your help and suggestions.<br>
Thank you</p>

---

## Post #2 by @pieper (2022-03-07 19:45 UTC)

<p>If you don’t get an answer here you might try the repository issue tracker.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/Project-MONAI/MONAILabel/issues">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Project-MONAI/MONAILabel/issues" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/67bb63f079afbb24f2bef3930c92e6f5038d8cfcfbe0e38fd470739d926c4715/Project-MONAI/MONAILabel" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/Project-MONAI/MONAILabel/issues" target="_blank" rel="noopener">Issues · Project-MONAI/MONAILabel</a></h3>

  <p>MONAI Label is an intelligent open source image labeling and learning tool. - Issues · Project-MONAI/MONAILabel</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @diazandr3s (2022-03-07 22:50 UTC)

<p>Hi <a class="mention" href="/u/mahdis_khodadadi">@Mahdis_Khodadadi</a>, sorry I just saw this.<br>
Can I ask you which MONAI Label app are you using (deepedit, deepgrow, or segmentation)?<br>
Can you see the masks you’ve generated in the labels-&gt;final folder?<br>
Can you also please share the log file (app.log) you have in the logs folder? It is easier for me to check what could happen.</p>
<p>Looking forward to hearing from you.</p>

---

## Post #4 by @Mahdis_Khodadadi (2022-03-09 16:21 UTC)

<p>Hi. no problem.</p>
<p>I am using deepedit app.</p>
<p>I tried doing the segmentation like this:<br>
1-labeling the image using segment editor in Slicer<br>
2-submitting the label<br>
3-using fore/background scribbles to edit the label and pressing the update button so training could start</p>
<p>it actually worked pretty fine so far. there are still some problems:<br>
1- I can see the mask files from labels-&gt;final folder in Slicer but they are the very first labels that I submitted. Is it correct?<br>
2- I was able to run the training for 3 images, for the 4th image, after one time fine tunning the labels using scribbles, all the values of the mask were lost and now I can’t see anything when I open the mask file of that image from labels-&gt;original folder<br>
3- after the second problem, 3D slicer keeps not responding when I try to connect it to the server again.</p>
<p>here is the log file . <a href="https://drive.google.com/file/d/1eTc9sgCs_2E99WFMaNSz6AqGuyq5-1j9/view?usp=sharing" rel="noopener nofollow ugc">click</a></p>
<p>I’d appreciate it if you could guide me.<br>
thank you</p>

---

## Post #5 by @diazandr3s (2022-03-10 01:30 UTC)

<p>Thanks for your prompt reply, <a class="mention" href="/u/mahdis_khodadadi">@Mahdis_Khodadadi</a>.</p>
<p>Regarding this point:</p>
<blockquote>
<p>1- I can see the mask files from labels-&gt;final folder in Slicer but they are the very first labels that I submitted. Is it correct?</p>
</blockquote>
<p>The labels that you’ll see in labels-&gt;final are the ones you submit only.</p>
<blockquote>
<p>3- after the second problem, 3D slicer keeps not responding when I try to connect it to the server again.</p>
</blockquote>
<p>This might be related to the use of scribbles to fine-tune the predicted label?</p>
<p>Currently, scribbles functionality works best only when creating a label from scratch and not to modify/edit a predicted mask. If you’d like to modify the predicted mask, please use the smart edit in MONAI Label (clicks) or the Slicer segment editor.</p>
<p>My recommendations are:</p>
<p>1/ I see from the logs that you’re using an outdated MONAI Label. Please update the monai label version by pulling the latest changes from the GitHub repo (if working directly from the repo) or create a clean virtual env and install the monailabel-weekly (<a href="https://pypi.org/project/monailabel-weekly/" class="inline-onebox" rel="noopener nofollow ugc">monailabel-weekly · PyPI</a>)<br>
2/ Use scribbles functionality only to create labels from scratch … Not to modify a predicted mask</p>
<p>Please let us know how that goes … I’m also happy to meet and talk more about this</p>

---

## Post #6 by @Mahdis_Khodadadi (2022-03-10 14:38 UTC)

<p>Thank you for the response.</p>
<p>I used the scribbles to fine-tune the masks. I’ll try what you suggested.</p>
<blockquote>
<p>1/ I see from the logs that you’re using an outdated MONAI Label.</p>
</blockquote>
<p>This is actually weird to me. Because I have already installed the monailabel-weekly. But I will try to update it anyway.</p>

---

## Post #7 by @diazandr3s (2022-03-10 15:42 UTC)

<p>Good. Please keep us updated <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #8 by @Mahdis_Khodadadi (2022-03-11 18:54 UTC)

<p>Hi,</p>
<p>thank you for your time. It was very helpful talking to you.</p>
<p>So, since I am working with MR images, I’ll continue using “deepedit” app.<br>
I have a few images already manually labeled. So, I use them to train the model and after training is done, I will work on labeling the images which have no mask files.</p>
<p>I will update this conversation in case I face any errors.</p>

---

## Post #9 by @Mahdis_Khodadadi (2022-03-24 20:40 UTC)

<p>CORRECTION:</p>
<p>I have unfortunately made a big mistake in this thread but I couldn’t edit it anymore.<br>
My images are actually CT scans.<br>
But this doesn’t make the thread unreliable I guess. Except for the fact, that with CT scans I can also use the “segmentation” app.</p>

---
