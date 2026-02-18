# Change segment editor button layout

**Topic ID**: 18343
**Date**: 2021-06-25
**URL**: https://discourse.slicer.org/t/change-segment-editor-button-layout/18343

---

## Post #1 by @qiqi5210 (2021-06-25 06:42 UTC)

<p>Hello, I want to know how to realize the vertical tool panel. I hope you can give me the detailed code. Thank you very much</p>

---

## Post #2 by @qiqi5210 (2021-06-25 06:55 UTC)

<p>Hello, I like the improvement of segment editor, and I want to learn it. I want to ask if you have realized it, and if you can provide some code so that I can learn it better. Thank you very much！</p>

---

## Post #3 by @lassoan (2021-06-25 21:46 UTC)

<p>Can you write a bit about what you would like to achieve? Could you show a mock-up of the layout that you would like to have?</p>
<p>If you want to modify the Segment Editor widget then the first step is to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/index.html">build Slicer</a>.</p>

---

## Post #4 by @qiqi5210 (2021-06-26 09:10 UTC)

<p>Thank you very much for your reply. I have built 3dslicer. I want to realize the function of vertical toolbar in the figure below, but I don’t know how to start. I hope you can give me a direction. Thank you again<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f83d4bf58694e096fb15693dd13da9597afc8d3.png" alt="toolBar" data-base62-sha1="blqaltfusPXXKscARR9Pv8u1SAH" width="148" height="172"></p>

---

## Post #5 by @lassoan (2021-07-18 02:52 UTC)

<p>You can edit qMRMLSegmentEditorWidget.cxx/.h and qMRMLSegmentEditorWidget.ui (using QtDesigner - by running <code>Slicer.exe --designer</code>) to customize the layout. It is all just standard Qt. Keep us updated about your progress - your updated GUI looks very nice.</p>

---

## Post #6 by @lassoan (2021-09-13 19:56 UTC)

<p>Thanks to all the efforts of <a class="mention" href="/u/jamesobutler">@jamesobutler</a>, the new Segment Editor layout is now ready - see more information (and provide any feedback and suggestions) in this topic:</p>
<aside class="quote quote-modified" data-post="1" data-topic="19649">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-segment-editor-layout-vertical-effect-toolbar/19649">New Segment Editor layout - vertical effect toolbar</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Thanks to all the development efforts of <a class="mention" href="/u/jamesobutler">@jamesobutler</a> and feedback from the community, the new, more space-efficient Segment Editor user interface is now ready (available in latest Slicer Preview Release). The main difference is that the effect toolbar is vertical, with fixed number of columns and without icon labels. This layout makes it easier to remember where to find an effect (because the same effect always appears at the same place), and the space is used more efficiently (there is less n…
  </blockquote>
</aside>


---
