---
topic_id: 20941
title: "How To Add A Gui Panel To The Slicer Vr Scene"
date: 2021-12-07
url: https://discourse.slicer.org/t/20941
---

# How to add a GUI panel to the Slicer VR scene

**Topic ID**: 20941
**Date**: 2021-12-07
**URL**: https://discourse.slicer.org/t/how-to-add-a-gui-panel-to-the-slicer-vr-scene/20941

---

## Post #1 by @CharlesChen (2021-12-07 02:55 UTC)

<p>Hi there,</p>
<p>I’m a beginner in 3D Slicer and I am learning how to develop modules to implement my own workflow.<br>
Currently, I use the ‘Extension Wizard’ to create a simple module for extracting the surface of image data (Other features are still in development).<br>
What I’d like to do next is to transfer my module from the desktop mode to the VR scene created by Slicer VR.<br>
However, I’m still not sure about the feasibility of adding Qt components/widgets or GUI panels to the VR scene to achieve the same functions as my desktop module.<br>
In other words, the following figure is the module (a python scripted module) I have created so far. How can I transfer it to the VR scene next?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64d14378e97c7449622aa4e440364dfbfbc30d56.png" data-download-href="/uploads/short-url/enS5IgT4WcEpBLP4EWnybwSUAqq.png?dl=1" title="My scripted module" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64d14378e97c7449622aa4e440364dfbfbc30d56.png" alt="My scripted module" data-base62-sha1="enS5IgT4WcEpBLP4EWnybwSUAqq" width="517" height="206" data-dominant-color="F7F8F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">My scripted module</span><span class="informations">784×313 4.32 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
What should I do, do you have any suggestions or useful tutorials about my question?<br>
Thank you very much in advance!!!</p>
<p>Best regards,<br>
Charles</p>

---

## Post #2 by @CharlesChen (2021-12-07 04:09 UTC)

<p>Or Is it possible to add VTKWidgets(like the ‘vtkSliderWidget’ and the ‘vtkSliderRepresentation3D’ for creating a slider) to the VR scenes created by Slicer VR:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/034613f9d9642e33bcb14d8fb90f85dcb3e5057d.png" alt="VTKwidgets" data-base62-sha1="sXzA4AzCepoSUJib2kGUjPGqzr" width="293" height="234"></p>
<p>and the above VTKwidgets need to achieve the same function as the widgets in the UI of desktop mode?</p>
<blockquote>
<p>In other words, the following figure is the module (a python scripted module) I have created so far. How can I transfer it to the VR scene next?</p>
</blockquote>
<p>Because the module I created will only include the sliders/buttons/combo boxes/checkboxes, so are there any suggestions to achieve/transfer these to the VR scene?</p>

---

## Post #3 by @pieper (2021-12-07 13:08 UTC)

<p>I recall that <a class="mention" href="/u/cpinter">@cpinter</a> and others were working on this, but I’m not sure of the status.</p>
<p>If you are interested in collaborating on these topics, Project Week is coming up.  On Jan 11 there’s going to be a discussion of VR/AR related topics at the prep call (10 am EST).</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://projectweek.na-mic.org/PW36_2022_Virtual/">
  <header class="source">
      <img src="https://projectweek.na-mic.org/assets/favicons/favicon.ico" class="site-icon" width="16" height="16">

      <a href="https://projectweek.na-mic.org/PW36_2022_Virtual/" target="_blank" rel="noopener">NA-MIC Project Weeks</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://projectweek.na-mic.org/PW36_2022_Virtual/" target="_blank" rel="noopener">Welcome to the web page for the 36th Project Week!</a></h3>

  <p>Website for NA-MIC Project Weeks</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @cpinter (2021-12-07 14:44 UTC)

<p>W have made good progress with the widget, you can see it in <a href="https://github.com/cpinter/SlicerVirtualReality/tree/gui-widgets-module">this branch</a>. Now we’re working on the interactions with this widget using a laser pointer (propagating move events, clicks, etc.). <a class="mention" href="/u/dgmato">@dgmato</a> is currently working on it, let us know if you’d like to contribute in some way.</p>

---

## Post #5 by @CharlesChen (2021-12-07 18:00 UTC)

<p>Hello Piper and Pinter,<br>
Thank you for your quick reply!<br>
That’s good to know that Project week is coming soon! I’d like to join in then.<br>
And I also notice from GitHub that you are making a lot of effort for this.<br>
I learned from the following link:<br>
<a href="https://github.com/KitwareMedical/SlicerVirtualReality/issues/43" rel="noopener nofollow ugc">https://github.com/KitwareMedical/SlicerVirtualReality/issues/43</a></p>
<p><a href="https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/VirtualReality/Resources/UI/qSlicerVirtualRealityModuleWidget.ui" rel="noopener nofollow ugc">https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/VirtualReality/Resources/UI/qSlicerVirtualRealityModuleWidget.ui</a></p>
<p><a href="https://github.com/cpinter/VtkQWidgetTest" rel="noopener nofollow ugc">https://github.com/cpinter/VtkQWidgetTest</a></p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/cpinter/SlicerVirtualReality/commit/93baf29913a35e9469776b59845538480769089d">
  <header class="source">

      <a href="https://github.com/cpinter/SlicerVirtualReality/commit/93baf29913a35e9469776b59845538480769089d" target="_blank" rel="noopener nofollow ugc">github.com/cpinter/SlicerVirtualReality</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/cpinter/SlicerVirtualReality/commit/93baf29913a35e9469776b59845538480769089d" target="_blank" rel="noopener nofollow ugc">ENH: Add VR optimized Qt Style Sheet</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2019-05-21" data-time="17:51:14" data-timezone="UTC">05:51PM - 21 May 19 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/mohammadrashid0917" target="_blank" rel="noopener nofollow ugc">
          <img alt="mohammadrashid0917" src="https://avatars.githubusercontent.com/u/46090514?v=4" class="onebox-avatar-inline" width="20" height="20">
          mohammadrashid0917
        </a>
      </div>

      <div class="lines" title="changed 1 files with 35 additions and 58 deletions">
        <a href="https://github.com/cpinter/SlicerVirtualReality/commit/93baf29913a35e9469776b59845538480769089d" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+35</span>
          <span class="removed">-58</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This style sheet makes the text in the VR menu widget bigger, and gives the butt<span class="show-more-container"><a href="https://github.com/cpinter/SlicerVirtualReality/commit/93baf29913a35e9469776b59845538480769089d" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">ons and slider handles different colors for unpressed, hover, and pressed statuses.
KitwareMedical#43</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
And I also notice that there is indeed a folder called ‘Widgets’<br>
Does it mean that there are already available VR menu widgets here?<br>
How can I see these menu widgets (like the widgets you’ve implemented for the segment editor module) in the VR scene?<br>
For example, as shown in the figure below, is this menu can be seen in the VR scene? How can I activate it in VR？ Thank you so much!<br>
<a href="https://github.com/cpinter/SlicerVirtualReality/pull/5" rel="noopener nofollow ugc">https://github.com/cpinter/SlicerVirtualReality/pull/5</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0ad7145dc6bc5dd64372ec0442fdb3c13c2381dc.png" data-download-href="/uploads/short-url/1xTzZy289wP26HOvOlunkaqnmTa.png?dl=1" title="VR Menu" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0ad7145dc6bc5dd64372ec0442fdb3c13c2381dc_2_465x375.png" alt="VR Menu" data-base62-sha1="1xTzZy289wP26HOvOlunkaqnmTa" width="465" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0ad7145dc6bc5dd64372ec0442fdb3c13c2381dc_2_465x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0ad7145dc6bc5dd64372ec0442fdb3c13c2381dc_2_697x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0ad7145dc6bc5dd64372ec0442fdb3c13c2381dc.png 2x" data-dominant-color="EEEEEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">VR Menu</span><span class="informations">829×668 86.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @cpinter (2021-12-07 19:02 UTC)

<p>Not sure if you have seen the branch I linked to above. That is the latest work we have in this topic.</p>
<aside class="quote no-group" data-username="CharlesChen" data-post="5" data-topic="20941">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/charleschen/48/8444_2.png" class="avatar"> CharlesChen:</div>
<blockquote>
<p>And I also notice that there is indeed a folder called ‘Widgets’<br>
Does it mean that there are already available VR menu widgets here?</p>
</blockquote>
</aside>
<p>These are prototypes.</p>
<aside class="quote no-group" data-username="CharlesChen" data-post="5" data-topic="20941">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/charleschen/48/8444_2.png" class="avatar"> CharlesChen:</div>
<blockquote>
<p>How can I see these menu widgets (like the widgets you’ve implemented for the segment editor module) in the VR scene?<br>
For example, as shown in the figure below, is this menu can be seen in the VR scene? How can I activate it in VR？ Thank you so much!</p>
</blockquote>
</aside>
<p>This is work in progress. Please hang on or if you’d like to contribute let us know.</p>

---

## Post #7 by @CharlesChen (2021-12-07 19:55 UTC)

<p>Hello Pinter,<br>
Yes, I really want to learn how to add some widgets to the VR scene and achieve the same function as the widgets in desktop mode.<br>
If possible, can I test the latest work you’ve done (The UI widgets available in the VR scene so far)? How to do/run it?<br>
I notice that there’s a building instruction:<br>
<a href="https://github.com/cpinter/SlicerVirtualReality/blob/gui-widgets-module/DeveloperGuide.md" rel="noopener nofollow ugc">https://github.com/cpinter/SlicerVirtualReality/blob/gui-widgets-module/DeveloperGuide.md</a></p>
<p>Just to make sure: Does it mean that if I follow it to build this VR module locally, then I can see/activate the menu widgets you’ve implemented so far? Or in this way, can I also make some adjustments/modifications to it? Am I correct?<br>
Because when I install the Slicer VR and run it in 3D Slicer, there is no menu widgets in the VR scene.<br>
And could you please describe the feasibility of adding some widgets such as buttons and sliders to the VR scene to realize the function of a custom module?<br>
For example, adding a slider to the VR scene of Slicer VR to adjust the threshold of the volume rendering image? I think this is a good practice for me to learn how to contribute to Slicer VR.<br>
Thank you so much!</p>

---

## Post #8 by @PhilipDavis (2021-12-08 01:46 UTC)

<p>Hello <a class="mention" href="/u/cpinter">@cpinter</a> ,<br>
This discussion is very exciting!<br>
I am new to 3D Slicer, and I also have a similar demand as <a class="mention" href="/u/charleschen">@CharlesChen</a>.<br>
I’ve learned that Slicer supports VTK, and it seems that we can call any VTK classes and abilities in Slicer. Meanwhile, I also noticed that some useful VTK  classes like ‘vtkOpenVRMenuWidget’ and ‘vtkQWidgetRepresentation’ can be used to create 3D widgets to display a menu in VR.<br>
Therefore, I’d like to know is it possible to create and add a widget like a button to the VR scene by running python script in Slicer?  How can I learn this and reach this goal? Where should I start?<br>
Thank you!</p>

---

## Post #9 by @cpinter (2021-12-09 09:41 UTC)

<aside class="quote no-group" data-username="CharlesChen" data-post="7" data-topic="20941">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/charleschen/48/8444_2.png" class="avatar"> CharlesChen:</div>
<blockquote>
<p>can I test the latest work you’ve done (The UI widgets available in the VR scene so far)? How to do/run it?</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="PhilipDavis" data-post="8" data-topic="20941">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/philipdavis/48/14142_2.png" class="avatar"> PhilipDavis:</div>
<blockquote>
<p>I’d like to know is it possible to create and add a widget like a button to the VR scene</p>
</blockquote>
</aside>
<p>It is work in progress, please keep an eye on the above issue and branch.</p>

---

## Post #10 by @Chinmay_Satish_Raut (2022-09-21 07:30 UTC)

<p>Hello <a class="mention" href="/u/cpinter">@cpinter</a><br>
I am new to slicer. Is there any progress on adding UI widgets in the VR scene? If not, could you point to any resources/ documentation so that I can do it on my own?</p>
<p><a class="mention" href="/u/charleschen">@CharlesChen</a> If you could find some workaround, please let me know.</p>

---
