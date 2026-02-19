---
topic_id: 21746
title: "Qt Switch Button In Slicer"
date: 2022-02-02
url: https://discourse.slicer.org/t/21746
---

# Qt switch button in Slicer

**Topic ID**: 21746
**Date**: 2022-02-02
**URL**: https://discourse.slicer.org/t/qt-switch-button-in-slicer/21746

---

## Post #1 by @chz31 (2022-02-02 05:10 UTC)

<p>Hi all,</p>
<p>I am thinking about using the qt switch button in Slicer as shown here <a href="https://doc.qt.io/qt-5/qml-qtquick-controls2-switch.html" rel="noopener nofollow ugc">Switch QML Type | Qt Quick Controls 5.15.8</a>. However, I could not find it in Slicer. Does Slicer incorporate the qt switch button function as python script?</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2022-02-02 13:07 UTC)

<p>I’ve often thought we should be able to use Qt Quick in Slicer but it was never obvious how to do it.  If someone has time to explore this it could be fun to try but for now I’d suggest using a <code>QCheckBox</code> instead.</p>

---

## Post #3 by @chz31 (2022-02-02 17:31 UTC)

<p>Thank you for letting me know! I was thinking about using the switch button to toggle displaying some results. I’ll use QRadioButton or QCheckbox instead.</p>

---

## Post #4 by @muratmaga (2022-02-02 17:36 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="21746">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>but it was never obvious how to do it.</p>
</blockquote>
</aside>
<p>I think it looks more modern and clear in places where you need to toggle visibility of something (see below). Of course checkbox or radio buttons can do the job, but I think it Switch is far more intuitive then explaining what that checkbox does in a tool tip.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0bc00047321d3c91056310228aa652cff4980366.png" data-download-href="/uploads/short-url/1FWBYQZF5lTslZli9iXS8rpBXLg.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0bc00047321d3c91056310228aa652cff4980366_2_690x137.png" alt="image" data-base62-sha1="1FWBYQZF5lTslZli9iXS8rpBXLg" width="690" height="137" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0bc00047321d3c91056310228aa652cff4980366_2_690x137.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0bc00047321d3c91056310228aa652cff4980366.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0bc00047321d3c91056310228aa652cff4980366.png 2x" data-dominant-color="515151"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">921×184 38.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @jamesobutler (2022-02-02 17:41 UTC)

<p>^In your case <a class="mention" href="/u/muratmaga">@muratmaga</a> it would seem like some re-wording could be done where it would be:</p>
<p>"Show Mean point label: [ ] "</p>
<p>The checkbox shouldn’t require any additional tooltip. Should be intuitive that a checked field here would show the mean point label and an unchecked field would mean that it is not showing.</p>
<p>Just a suggestion considering the Switch object is not available to use.</p>

---

## Post #6 by @muratmaga (2022-02-02 17:46 UTC)

<p>We used to have checkboxes in there, with a label that read <strong>toggle mean shape visibility</strong> followed by a checkbox. Surprisingly it wasn’t clear to the people. I think the checkboxes and stuff are going out of favor in UI design.</p>
<p>That’s why we now have button, which unfortunately don’t work really well in dark mode due to low contrast, when it is in pressed down state. Having sliding on/off switches would have been nice.</p>

---

## Post #7 by @Sam_Horvath (2022-02-02 17:49 UTC)

<p>With Qt stylesheets, you can replace the rendered checkbox with an arbitrary image to create the switch look and feel</p>
<aside class="onebox stackexchange" data-onebox-src="https://stackoverflow.com/questions/5962503/qt-checkbox-toolbutton-with-custom-distinct-check-unchecked-icons">
  <header class="source">

      <a href="https://stackoverflow.com/questions/5962503/qt-checkbox-toolbutton-with-custom-distinct-check-unchecked-icons" target="_blank" rel="noopener">stackoverflow.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://stackoverflow.com/users/229686/eda-qa-mort-ora-y" target="_blank" rel="noopener">
    <img alt="edA-qa mort-ora-y" src="https://www.gravatar.com/avatar/e6ce612702a34f9bcebee2f34139c3f1?s=256&amp;d=identicon&amp;r=PG" class="thumbnail onebox-avatar" width="256" height="256">
  </a>

<h4>
  <a href="https://stackoverflow.com/questions/5962503/qt-checkbox-toolbutton-with-custom-distinct-check-unchecked-icons" target="_blank" rel="noopener">Qt checkbox/toolbutton with custom/distinct check/unchecked icons</a>
</h4>

<div class="tags">
  <strong>c++, qt</strong>
</div>

<div class="date">
  asked by
  
  <a href="https://stackoverflow.com/users/229686/eda-qa-mort-ora-y" target="_blank" rel="noopener">
    edA-qa mort-ora-y
  </a>
  on <a href="https://stackoverflow.com/questions/5962503/qt-checkbox-toolbutton-with-custom-distinct-check-unchecked-icons" target="_blank" rel="noopener">10:06AM - 11 May 11 UTC</a>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>To do this:</p>
<ul>
<li>Add the images to your module as resources</li>
<li>Create a stylesheet (.qss) for the checkbox design and add as a resource</li>
<li>Add <code>checkbox.setStylesheet({the contents of the qss file})</code>
<ul>
<li>You can also just embed the qss as a string in the .py file instead of using a separate .qss</li>
</ul>
</li>
<li><a href="https://github.com/PerkLab/SlicerSandbox/blob/c6ade46bf1dc284ec00d404218d477f817c4dd87/StyleTester/StyleTester.py#L120">Example</a></li>
</ul>

---

## Post #8 by @jamesobutler (2022-02-02 17:49 UTC)

<p>Yeah the term “Toggle” implies a switch type. Which is why my terminology of “Show” may be the better term for now.</p>

---

## Post #9 by @chz31 (2022-02-02 18:13 UTC)

<p>This looks great. Thank you!</p>

---

## Post #10 by @keri (2022-02-03 18:18 UTC)

<p>Hi,</p>
<p>I wanted to ask did you encounter a segmentation fault when using any stylesheet applied (even through <a href="https://github.com/PerkLab/SlicerSandbox" rel="noopener nofollow ugc">SlicerSandbox</a>) and you go to the Transform module and then switch to some other module?</p>
<p>I already <a href="https://discourse.slicer.org/t/segmentation-fault-with-any-applied-qt-stylesheet-when-switch-off-from-transform-module/21584">asked this question</a> but got no feedback. Currently I’m unable to test it on Windows (slow PC and internet connection).</p>

---
