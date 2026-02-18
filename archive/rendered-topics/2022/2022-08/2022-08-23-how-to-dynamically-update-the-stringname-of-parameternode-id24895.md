# How to dynamically update the StringName of ParameterNode?

**Topic ID**: 24895
**Date**: 2022-08-23
**URL**: https://discourse.slicer.org/t/how-to-dynamically-update-the-stringname-of-parameternode/24895

---

## Post #1 by @sunshine (2022-08-23 21:26 UTC)

<p>Hi everyone,</p>
<p>I am trying to design my first extension module, similar to the module “Sequences” but with real-time frame annotations from AI image processing for live ultrasound sequence collection.</p>
<p>My first question is about the StringName of ParameterNode of each SequenceBrowser. Due to the fact that there could be multiple SequenceBrowsers with multiple CurrentSlider-Index, and the users may even rename the name of a SequenceBrowser, how should I remove/update the “StringName<br>
of ParameterNode” when the user deletes one SequenceBrowser, and how should I update/rename the “StringName of ParameterNode” to avoid redundantly adding new “StringName<br>
of ParameterNode” even the user just renames the SequenceBrowser?</p>
<p>My second question, which may not be possible, instead of creating a new module, is it possible to get the python script source code of module “Sequences” thus I can modify it directly?</p>
<p>Thank you so much in advance!</p>

---

## Post #2 by @lassoan (2022-08-24 07:37 UTC)

<p>To refer to a node from any other node, you must use node references (SetNodeReferenceID, GetNode Reference, etc. methods).</p>

---

## Post #3 by @sunshine (2022-08-25 00:52 UTC)

<p>Hi Andras,</p>
<p>Thank you so much for your help!</p>
<p>I found the attribute “selectedItemNumber” from vtkMRMLSequenceBrowserNode in the scene file, which solved my problem.<br>
As you can see in the screenshot below, I am now able to retrieve SequenceBrowser and show the FrameIndex in my own module, and I should also be able to do <strong>offline</strong> annotation now.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/377dc8ab7965659ecc9efe1fbd99745a6898e18b.png" data-download-href="/uploads/short-url/7UTKB1ankRruXMSJv5BISQYs3Uf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/377dc8ab7965659ecc9efe1fbd99745a6898e18b.png" alt="image" data-base62-sha1="7UTKB1ankRruXMSJv5BISQYs3Uf" width="690" height="298" data-dominant-color="A09F9F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">998×432 96 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, it might be impossible for me to complete a new “Sequences” module for the new sequence recording, and it seems that the existing “Sequences” module does not support PyQt5 script source code.</p>
<p>What should I do to make the annotation <strong>online</strong>?<br>
E.g., after I click the recording button in the “Sequences” module to record a sequence of ultrasound data, as the real-time raw image shown in the red widget, how should I annotate a “Yes” notation in the center of the raw image and show the annotated image in the yellow widget lively?</p>
<p>Assume this problem can be solved in three steps:<br>
1. How can I add a new short-cut button in the toolbar to trigger the annotation?<br>
2. How should I retrieve the real-time raw image?<br>
3. How should I display the annotated image in the yellow widget?</p>
<p>Thank you again for your valuable time!</p>

---

## Post #4 by @sunshine (2022-08-25 19:28 UTC)

<p>Not able to edit the last post now.</p>
<p>Since the last post is kind of a problem different from the topic, I made a new topic below to ask for help:</p><aside class="quote quote-modified" data-post="1" data-topic="24923">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/3ec8ea/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-do-online-real-time-annotation-when-recording-a-new-sequence-of-ultrasound-stream-using-the-module-sequences/24923">How to do online (real-time) annotation when recording a new sequence of ultrasound stream using the module "Sequences"?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi everyone, 
This topic is to continue a question from 
<a href="https://discourse.slicer.org/t/how-to-dynamically-update-the-stringname-of-parameternode/24895/3" class="onebox" target="_blank" rel="noopener">https://discourse.slicer.org/t/how-to-dynamically-update-the-stringname-of-parameternode/24895/3?u=sunshine</a> 
I am trying to design my first extension module, similar to the module “Sequences” but with real-time frame annotations from AI image processing for live ultrasound sequence collection. 
As you can see in the screenshot below, I am now able to retrieve SequenceBrowser and show the FrameIndex in my own module, and I should also be ab…
  </blockquote>
</aside>

<p>Please help remove my last post if necessary.</p>
<p>Thank you so much in advance!</p>
<p>Please help remove the</p>

---
