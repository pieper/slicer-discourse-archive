# How, from python-scritps, to trigger the click-function of "center of the 3D view on the scene"?

**Topic ID**: 8181
**Date**: 2019-08-26
**URL**: https://discourse.slicer.org/t/how-from-python-scritps-to-trigger-the-click-function-of-center-of-the-3d-view-on-the-scene/8181

---

## Post #1 by @aiden.zhu (2019-08-26 18:34 UTC)

<p>Hi all,<br>
I am lazy to try to click on the “Center of the 3D view on the scene” each time after I have a 3D-view there. So based on python codes, how to trigger the click-function to get “Center of the 3D view on the scene”?<br>
Thanks in advance!</p>

---

## Post #2 by @lassoan (2019-08-26 18:55 UTC)

<p>This should help: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Center_the_3D_View_on_the_Scene" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Center_the_3D_View_on_the_Scene</a></p>
<p>What is your workflow? Would you re-center the 3D view the first time you show something in the 3D view or each time you load some data, each time you show/hide something, …?</p>

---

## Post #3 by @pieper (2019-08-26 19:04 UTC)

<p>This kind of question comes up from time to time and it can be a good way for ne developers to learn about the architecture of Slicer by looking through the source code.  One way is to look for the tooltip (e.g. use <code>git grep</code>) and find either the code or <code>.ui</code> file where the GUI element is declared.  From there you can get the name of the widget (in this case <code>CenterButton</code>) and find where it is used in the code.  Here the <code>triggered()</code> signal is connected to the <code>resetFocalPoint()</code> slot.  As you look at the code you can get an appreciation of the separation of GUI from Logic and MRML operations that support the scriptability.</p>

---

## Post #4 by @aiden.zhu (2019-08-26 19:16 UTC)

<p>Hi Andras, Thanks a lot.<br>
What I do is that, load a grey image and a labeled-like image, then convert the label-like image to be segments, then those selected segments shown in 3D view to take a movie. So each time I do not want to click it again and again to adjust all those properties/features, that means, I would set all same settings for my movie.<br>
I will follow your instruction site to go ahead. Thanks again.<br>
Aiden</p>

---

## Post #5 by @aiden.zhu (2019-08-26 19:34 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> Thank you. You are right about the point you mentioned. As a new (potential) developer, I was always confused by how to control the scene/slice stuff existing there now, a good starting line for me at least. So if you guys may get a better summarized tutorial focusing on how to control the settings (existing there as we see while we open slicer), that will be really helpful for us to get started on Slicer development/application.<br>
Thanks again.<br>
Aiden</p>

---

## Post #6 by @aiden.zhu (2019-08-26 20:29 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks a lot. It works while I use this resetFocalPoint().</p>
<p>In my mind if inside slicer.qMRMLSegmentEditorWidget() there might be a signal emitted out while we click “Show 3D”, that will be more helpful since from there I could right away set up the 3D-view and observe the 3D-view before I may take a movie.</p>
<p>Now since I canNOT get to “Show 3D” in the segment-editor, so after I click “Show 3D”,  I have to do the settings on the time I open the new module of “Screen Capture” where I add the following there. It works!</p>
<p>layoutManager = slicer.app.layoutManager()<br>
threeDWidget = layoutManager.threeDWidget(0)<br>
threeDView = threeDWidget.threeDView()<br>
threeDView.resetFocalPoint()</p>
<p>Thanks a lot again.</p>

---

## Post #7 by @lassoan (2019-08-26 23:55 UTC)

<aside class="quote no-group" data-username="aiden.zhu" data-post="6" data-topic="8181">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f19dbf/48.png" class="avatar"> aiden.zhu:</div>
<blockquote>
<p>Now since I canNOT get to “Show 3D” in the segment-editor</p>
</blockquote>
</aside>
<p>What do you mean? You would like to know how to create 3D representation for a segmentation node? There are examples in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">script repository</a> for most commonly raised questions, including this one.</p>

---

## Post #8 by @aiden.zhu (2019-08-27 12:44 UTC)

<p>Hi Good morning, <a class="mention" href="/u/lassoan">@lassoan</a><br>
Here I show what I do using screen shots:</p>
<ol>
<li>load a grey image and its label-like image<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e46f825ab591d1d82303d813f279bf98824239c.png" alt="image" data-base62-sha1="i16dahPreETYNOPMrzCcwGRkDaA" width="381" height="329"></li>
<li>With  a  modified “segment Editor”, I use “threshold” to have segments from the label-like image.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07d225eaf45560074875dddcc265c9d7a9fff2df.png" data-download-href="/uploads/short-url/17bA7loU7uJrJ3htaoqj6HYQZxJ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07d225eaf45560074875dddcc265c9d7a9fff2df_2_690x450.png" alt="image" data-base62-sha1="17bA7loU7uJrJ3htaoqj6HYQZxJ" width="690" height="450" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07d225eaf45560074875dddcc265c9d7a9fff2df_2_690x450.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07d225eaf45560074875dddcc265c9d7a9fff2df_2_1035x675.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07d225eaf45560074875dddcc265c9d7a9fff2df.png 2x" data-dominant-color="F0F2F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1035×675 43.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
<li>Click “Show 3D”<br>
for the Step-3, I would like to see 3D-view ready for my movie right away after my clicking, but right now I do not see anything inside the view1 (3D). So have to (A) click that “Center the 3D view on the scene”<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d11786b8dfbd99e99452de4e5d4333e6cb53354.png" alt="image" data-base62-sha1="1RBDvC0A6fPhZOnlqVLLGHXMDAM" width="223" height="91"><br>
and then I have to (B) scroll the mouse middle-button to zoom-in to see my segments<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b2037f3b4bc1e94f509cf8f6ec67bbebf9f2dad.jpeg" data-download-href="/uploads/short-url/1AqhmNZXW9bhdvFvkYo8zyvXQu1.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b2037f3b4bc1e94f509cf8f6ec67bbebf9f2dad_2_437x500.jpeg" alt="image" data-base62-sha1="1AqhmNZXW9bhdvFvkYo8zyvXQu1" width="437" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b2037f3b4bc1e94f509cf8f6ec67bbebf9f2dad_2_437x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b2037f3b4bc1e94f509cf8f6ec67bbebf9f2dad.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b2037f3b4bc1e94f509cf8f6ec67bbebf9f2dad.jpeg 2x" data-dominant-color="84A28B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">530×606 75.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
So in my mind I would like to get (A) and (B) done by scripts. My question is how to get (A) and (B) using python codes.<br>
Thanks a lot.<br>
Best,<br>
Aiden</li>
</ol>

---

## Post #9 by @lassoan (2019-08-27 13:15 UTC)

<p>Posts above should have answered these questions. If you would like us to write parts of your script then please upload your current script to github and post the link here so that we can work on it together (and we may put the end result into the the script repository)</p>

---

## Post #10 by @aiden.zhu (2019-08-27 13:41 UTC)

<p>Please let me have some time to get to know how to use github. <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=9" title=":sweat_smile:" class="emoji" alt=":sweat_smile:"></p>

---

## Post #11 by @lassoan (2019-08-27 13:41 UTC)

<p>This should help: <a href="https://guides.github.com/activities/hello-world/" rel="nofollow noopener">https://guides.github.com/activities/hello-world/</a></p>

---

## Post #12 by @aiden.zhu (2019-08-27 16:54 UTC)

<p>Thanks a lot. It really helps.</p>
<p>Here is my file loaded here:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/AidenZhu186/fromSegmentEditor2Set3DView/blob/master/SegmentEditorAiden.py" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/AidenZhu186/fromSegmentEditor2Set3DView/blob/master/SegmentEditorAiden.py" target="_blank" rel="nofollow noopener">AidenZhu186/fromSegmentEditor2Set3DView/blob/master/SegmentEditorAiden.py</a></h4>
<pre><code class="lang-py">import os
#import sys
import unittest
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
from slicer.util import VTKObservationMixin

# 
def get_class_members(klass):
    ret = dir(klass)
    if hasattr(klass,'__bases__'):
        for base in klass.__bases__:
            ret = ret + get_class_members(base)
    return ret

def uniq( seq ): 
    """ the 'set()' way ( use dict when there's no set ) """
    return list(set(seq))

def get_object_attrs( obj ):
</code></pre>

  This file has been truncated. <a href="https://github.com/AidenZhu186/fromSegmentEditor2Set3DView/blob/master/SegmentEditorAiden.py" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #13 by @rimaaaak (2023-12-14 20:03 UTC)

<p>Hi. I wanted to create a button to bring the 3D view back to its original position. How can I do that?</p>

---

## Post #14 by @aiden.zhu (2024-01-19 16:52 UTC)

<p>you need a have module (class ScriptedLoadableModule) and then inside its widget pat to add your button.</p>
<p>You may start with how to create a GUI module.</p>

---
