---
topic_id: 23757
title: "Monai Server Launch Failing"
date: 2022-06-07
url: https://discourse.slicer.org/t/23757
---

# Monai server launch failing

**Topic ID**: 23757
**Date**: 2022-06-07
**URL**: https://discourse.slicer.org/t/monai-server-launch-failing/23757

---

## Post #1 by @Nayra_Pumar (2022-06-07 20:00 UTC)

<p>I’ve cloned the MONAIlabel github repository (<a href="https://github.com/Project-MONAI/MONAILabel" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Project-MONAI/MONAILabel: MONAI Label is an intelligent open source image labeling and learning tool.</a>), set up a python 3.9 python environment, installed cuda and then installed all the dependencies listed in the dependencies.txt from the github repository (by running<code> pip install -r requirements.txt</code> in the terminal).</p>
<p>When I try to start the server it fails to run, and I get this error message:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc3ec1d59af3d032d78d816f25b017bd1836f1ab.png" data-download-href="/uploads/short-url/t8PRm41IA9hwVOXni5Xj958JMUz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc3ec1d59af3d032d78d816f25b017bd1836f1ab.png" alt="image" data-base62-sha1="t8PRm41IA9hwVOXni5Xj958JMUz" width="690" height="388" data-dominant-color="202020"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1398×788 36.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It’s running on a computer running windows 10. A ‘twin’ of this computer runs the MONAIlabel server flawlessly, and even a laptop (without cuda possibilities) has managed to start the server. All of these instalations following the same procedure.</p>

---

## Post #2 by @mikebind (2022-06-08 02:39 UTC)

<p>It looks like you might be missing the <code>segmentation.py</code> file in <code>apps/radiology/lib/configs/</code>.  Does that file exist in that location?</p>

---

## Post #3 by @Nayra_Pumar (2022-06-08 07:33 UTC)

<p>Yes, the file segmentation.py exists in the folder. I’ve just checked taking he segmentation.py from the laptop where the server worked, and replacing the one in the computer where it doesn’t work, and no success.</p>

---

## Post #4 by @mikebind (2022-06-08 15:43 UTC)

<p>I’m quite a beginner with MONAILabel, so I don’t really have other ideas about the best way to troubleshoot.  My thought was based on trying to interpret the error stack trace you shared.  It looks like it was in the middle of loading a series of subclasses and successfully got through ones for deepedit, deepgrow_2d, deepgrow_3d, then ran into an error trying to load the same kind of thing for “segmentation”.  It looks like the error message is suggesting that it is failing to find a <code>segmentation.py</code> file in <code>lib/configs/</code> which has a <code>Segmentation</code> class defined in it derived from <code>TaskConfig</code>.  If that file is there, then I wonder if perhaps some other configuration is pointing it to a different place or if something was renamed.  For example, might you have renamed one of the models in order to customize it? Or, did you clone the github repo at different times on the two different computers?  Might the repo have changed in between?  Those are the only ideas I have which might be helpful.<br>
<a class="mention" href="/u/diazandr3s">@diazandr3s</a> do you have any suggestions?</p>

---

## Post #5 by @rbumm (2022-06-08 16:12 UTC)

<p>In WSL Ubuntu I always cd to my home dir to which I forked MONAILabel and do a</p>
<pre><code class="lang-auto">export PATH=$PATH:`pwd`/MONAILabel/monailabel/scripts
</code></pre>
<p>in the home directory before I start monailabel server.<br>
Does this maybe help?</p>

---

## Post #6 by @diazandr3s (2022-06-08 19:18 UTC)

<p>Thanks for your comments, <a class="mention" href="/u/mikebind">@mikebind</a>, <a class="mention" href="/u/rbumm">@rbumm</a><br>
<a class="mention" href="/u/nayra_pumar">@Nayra_Pumar</a> please set the path as <a class="mention" href="/u/rbumm">@rbumm</a> suggested and let us know how that goes.</p>

---

## Post #7 by @Nayra_Pumar (2022-06-09 12:09 UTC)

<aside class="quote no-group quote-modified" data-username="rbumm" data-post="5" data-topic="23757">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p><code>export PATH=$PATH:</code>pwd<code>/MONAILabel/monailabel/scripts</code></p>
</blockquote>
</aside>
<p>I tried installing, on a different computer, with a cuda capable GPU, following the same instructions. I launched the server using the same command and everything worked fine at the first time.<br>
So I figured the error was related to the computer. I reinstalled windows 11 from scratch, and in that fresh installation, I tried to install again the monai label (installing git, anaconda, creating a new environment…).<br>
Again I still get the same error. I don’t think it’s a path problem, because I haven’t had to set it on the other two different computers where I tried to do the installation.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83a1d22d5fa78f89efe9628ef6d51bbf944a2fdf.png" data-download-href="/uploads/short-url/iMtfpmjo2dhEvHpkyCwR1b1VpIH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83a1d22d5fa78f89efe9628ef6d51bbf944a2fdf.png" alt="image" data-base62-sha1="iMtfpmjo2dhEvHpkyCwR1b1VpIH" width="690" height="383" data-dominant-color="222222"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1403×780 68.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Also I’ve tried to find info about the uvicorn error 56 and had no luck.</p>

---

## Post #8 by @rbumm (2022-06-09 14:46 UTC)

<p>Thanks, Nayra.<br>
I did the same process a few days ago in windows 11 without using anaconda.</p>
<p>Install a Python 3.9 (important, not 3.10)  from the Windows store.<br>
Please try to install MONAILabel and its prerequisites [as outlined here]<br>
(<a href="https://docs.monai.io/projects/label/en/latest/installation.html#windows" class="inline-onebox">Installation — MONAI Label 0.7.0rc1 Documentation</a>) using pip in the PowerShell as admin.</p>
<pre><code class="lang-auto">python -m pip install --upgrade pip setuptools wheel
</code></pre>
<p>then refer <a href="https://pytorch.org/get-started/locally/">to this page</a> to get the current PyTorch and Cuda script and run it</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/589655f921e882f41f3554ec5164ed5194b90711.png" data-download-href="/uploads/short-url/cDG6QvTP4YdL5sJEPuFcUuyyU7L.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/589655f921e882f41f3554ec5164ed5194b90711_2_690x286.png" alt="image" data-base62-sha1="cDG6QvTP4YdL5sJEPuFcUuyyU7L" width="690" height="286" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/589655f921e882f41f3554ec5164ed5194b90711_2_690x286.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/589655f921e882f41f3554ec5164ed5194b90711.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/589655f921e882f41f3554ec5164ed5194b90711.png 2x" data-dominant-color="F5E1DE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">875×363 19.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<pre><code class="lang-auto">pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113
</code></pre>
<p>Change to your user home directory and  run</p>
<pre><code class="lang-auto">pip install git+https://github.com/Project-MONAI/MONAILabel#egg=monailabel
</code></pre>
<p>to install the latest version of ML.<br>
Download ML apps and dataset as outlined in the documentation link above and run the start_server script line.<br>
Hope that helps …</p>

---

## Post #9 by @Nayra_Pumar (2022-06-10 13:49 UTC)

<p>Thank you <a class="mention" href="/u/rbumm">@rbumm</a></p>
<p>Following your advice I installed python 3.9 from the Microsoft Store, followed the instructions from the <a href="http://monai.io" rel="noopener nofollow ugc">monai.io</a> page, installed the custom version of PyTorch+Cuda all of that using the PowerShell as admin.<br>
To install the monail label, I cloned the github repository and, in the home directory, ran:</p>
<p><code> pip install -r requirements.txt</code></p>
<p>to get all the needed packages installed.<br>
Downloaded the dataset and I was able to run the server and connect to it from Slicer!</p>
<p>I think what did the trick was not to use anaconda.</p>
<p>Thank you very much for your help!</p>

---
