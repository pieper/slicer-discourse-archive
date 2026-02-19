---
topic_id: 24674
title: "Shapevariationanalyzer In 3D Slicer"
date: 2022-08-08
url: https://discourse.slicer.org/t/24674
---

# ShapeVariationAnalyzer in 3D Slicer

**Topic ID**: 24674
**Date**: 2022-08-08
**URL**: https://discourse.slicer.org/t/shapevariationanalyzer-in-3d-slicer/24674

---

## Post #1 by @Suji_L_Lee (2022-08-08 08:32 UTC)

<p>Hi, expert</p>
<p>I’d like to use ‘computation of mean group’ function of ‘ShapeVariationAnalyzer’ in a 3D slicer (version 4.11) for making the template of my data.</p>
<p>But I couldn’t find that extension after completing the installation.</p>
<p>I could see only the ‘population analysis’ like that.<br>
Can you give me some advice?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/6535f18afefe26014c2568bd527b42226276df70.png" data-download-href="/uploads/short-url/erlNttbI5OxUUZFw4355nh8it7W.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/6535f18afefe26014c2568bd527b42226276df70_2_690x274.png" alt="image" data-base62-sha1="erlNttbI5OxUUZFw4355nh8it7W" width="690" height="274" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/6535f18afefe26014c2568bd527b42226276df70_2_690x274.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/6535f18afefe26014c2568bd527b42226276df70_2_1035x411.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/6535f18afefe26014c2568bd527b42226276df70_2_1380x548.png 2x" data-dominant-color="747379"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1850×735 112 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks</p>

---

## Post #2 by @cpinter (2022-08-08 08:45 UTC)

<p>Please check it in the latest stable version 5.0.3</p>

---

## Post #3 by @Suji_L_Lee (2022-08-08 11:13 UTC)

<p>Hi Pinter,</p>
<p>Thank you for your answer!</p>
<p>I installed the 5.3.0 version in the Windows 10,<br>
but I met that error.</p>
<p>Can you give me a comment?</p>
<h2><a name="p-81854-thanks-suji-1" class="anchor" href="#p-81854-thanks-suji-1" aria-label="Heading link"></a>Thanks<br>
Suji</h2>
<p>Traceback (most recent call last):<br>
File “C:/Users/EBI/AppData/Local/NA-MIC/Slicer 5.1.0-2022-08-04/NA-MIC/Extensions-31103/SPHARM-PDM/lib/Slicer-5.1/qt-scripted-modules/RigidAlignmentModule.py”, line 28, in <strong>init</strong><br>
from RigidAlignmentModuleMetadata import TITLE, CATEGORY<br>
ModuleNotFoundError: No module named ‘RigidAlignmentModuleMetadata’</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9da58943037726bf5454d1c1aa81898aa7c192a5.png" data-download-href="/uploads/short-url/muBCAQikJNYUw6DseVHMUYgR3w1.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9da58943037726bf5454d1c1aa81898aa7c192a5.png" alt="image" data-base62-sha1="muBCAQikJNYUw6DseVHMUYgR3w1" width="690" height="350" data-dominant-color="FEF4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">828×421 15.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @jamesobutler (2022-08-08 11:36 UTC)

<aside class="quote no-group" data-username="Suji_L_Lee" data-post="1" data-topic="24674">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/suji_l_lee/48/4231_2.png" class="avatar"> Suji_L_Lee:</div>
<blockquote>
<p>I’d like to use ‘computation of mean group’ function of ‘ShapeVariationAnalyzer’ in a 3D slicer</p>
</blockquote>
</aside>
<p>This CLI tool was turned off in the ShapeVariationAnalyzer extension many years ago on 2017-11-29 in this <a href="https://github.com/DCBIA-OrthoLab/ShapeVariationAnalyzer/commit/ff0340405ca8b164af516029496dc8c4bf6e34cf" rel="noopener nofollow ugc">commit</a> by <a class="mention" href="/u/juanprietob">@juanprietob</a>. Selecting a new tool for your operation will likely be required.</p>

---

## Post #5 by @Suji_L_Lee (2022-08-08 12:10 UTC)

<p>oh I got it.</p>
<p>I really appreciate your help.</p>
<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a></p>
<p>Best,<br>
Sujie</p>

---
