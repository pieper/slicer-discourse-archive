---
topic_id: 11394
title: "4 11 Module Panel Is Too Wide And Wont Resize"
date: 2020-05-04
url: https://discourse.slicer.org/t/11394
---

# 4.11 Module panel is too wide and won't resize

**Topic ID**: 11394
**Date**: 2020-05-04
**URL**: https://discourse.slicer.org/t/4-11-module-panel-is-too-wide-and-wont-resize/11394

---

## Post #1 by @Melodicpinpon (2020-05-04 07:38 UTC)

<p>Hello,</p>
<p>My 4.11 version keeps the module panel window at the same size, convering the 2/3 of my screen.</p>
<p>I guess I should use the 4.10 instead…</p>

---

## Post #2 by @jamesobutler (2020-05-04 12:23 UTC)

<p>Is this only when viewing a specific module in the left panel area? What does the volumes module look like? Can you provide a screenshot?</p>

---

## Post #3 by @muratmaga (2020-05-04 16:02 UTC)

<aside class="quote no-group" data-username="Melodicpinpon" data-post="1" data-topic="11394">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/melodicpinpon/48/3254_2.png" class="avatar"> Melodicpinpon:</div>
<blockquote>
<p>module</p>
</blockquote>
</aside>
<p>Do you have very long node names? I only encountered that issue when the node names are too long, which module panel expands automatically to accommodate.</p>

---

## Post #4 by @lassoan (2020-05-04 21:23 UTC)

<p>Can you post a screenshot?</p>

---

## Post #5 by @ond12 (2021-05-31 10:09 UTC)

<p>Hello,</p>
<p>VERSION : 4.11</p>
<p>I encountered the same problem. For me 3Dslicer is very hard to use on my laptop.<br>
the module panel window is fixed size, convering the 2/3 of my screen, and i can’t resize it smaller to the Left.</p>
<p>I have a small 13 inches screen.</p>
<p>Here a screenshot:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f918a0beccade1aaeb910eb5f8c58a5ed8a84e88.png" data-download-href="/uploads/short-url/zxBECAah9f1Gkwc2RHrrPviWTsQ.png?dl=1" title="panelsize" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f918a0beccade1aaeb910eb5f8c58a5ed8a84e88_2_690x388.png" alt="panelsize" data-base62-sha1="zxBECAah9f1Gkwc2RHrrPviWTsQ" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f918a0beccade1aaeb910eb5f8c58a5ed8a84e88_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f918a0beccade1aaeb910eb5f8c58a5ed8a84e88_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f918a0beccade1aaeb910eb5f8c58a5ed8a84e88_2_1380x776.png 2x" data-dominant-color="3B4146"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">panelsize</span><span class="informations">1920×1080 414 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Can you please give me an hint why it’s doing this ?</p>
<p>Thank you</p>

---

## Post #6 by @lassoan (2021-05-31 21:49 UTC)

<p>You can scale the text/button sizes of Slicer many ways:</p>
<ul>
<li>Reduce font size in Slicer in menu: Edit / Application settings / Appearance / Font and size</li>
<li>Reduce the font scaling by running <code>set QT_SCALE_FACTOR=0.5</code> in the command console and then starting Slicer in that console (you can make this permanent by adding this to your environment variables or creating a .bat file that sets this and then starts Slicer)</li>
<li>You can adjust text scaling settings on your computer</li>
<li>Drag-and-drop the module panel to a second monitor</li>
</ul>

---

## Post #7 by @DAT_Minh (2023-07-20 10:50 UTC)

<p>Dear <a class="mention" href="/u/lassoan">@lassoan</a>,<br>
Just reducing the font size is not enough for me. I typed the set QT_SCALE_FACTOR=0.5 command and it returned an error. I’m using version 5.0.2. Could you take a look at it? Thank you very much.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d5290db0cc10596a9f4da6cc9ac2e2547ba3476.png" data-download-href="/uploads/short-url/mrJRho2Qpzp3hROG2sjTuQz4hro.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d5290db0cc10596a9f4da6cc9ac2e2547ba3476_2_690x359.png" alt="image" data-base62-sha1="mrJRho2Qpzp3hROG2sjTuQz4hro" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d5290db0cc10596a9f4da6cc9ac2e2547ba3476_2_690x359.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d5290db0cc10596a9f4da6cc9ac2e2547ba3476_2_1035x538.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d5290db0cc10596a9f4da6cc9ac2e2547ba3476_2_1380x718.png 2x" data-dominant-color="DCDEE2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1914×998 259 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2023-07-20 12:56 UTC)

<p>You entered the command in Slicer’s Python console instead, which uses a different syntax, and setting the environment variable after the application has started is too late anyway.</p>
<p>Instead, the environment variable has to be set in the command terminal in Windows, before starting Slicer.</p>
<p>An even simpler method is to add <code>QT_SCALE_FACTOR=0.5</code> in the <code>[EnvironmentVariables]</code> section of the <code>SlicerLauncherSettings.ini</code> file (in the <code>bin</code> subfolder of the application):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97b584a3521d4f4ac491d2f70bd109087391a6e1.png" data-download-href="/uploads/short-url/lE4ZVqoWQ9GUmpHRuLwvWWInuM1.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97b584a3521d4f4ac491d2f70bd109087391a6e1_2_690x453.png" alt="image" data-base62-sha1="lE4ZVqoWQ9GUmpHRuLwvWWInuM1" width="690" height="453" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97b584a3521d4f4ac491d2f70bd109087391a6e1_2_690x453.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97b584a3521d4f4ac491d2f70bd109087391a6e1_2_1035x679.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97b584a3521d4f4ac491d2f70bd109087391a6e1.png 2x" data-dominant-color="29292A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1174×772 82.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @DAT_Minh (2023-07-20 13:35 UTC)

<p>Thank you for the clarification. I will try it.</p>

---
