# Adding fiducial marks and determining RAS coordinates

**Topic ID**: 13421
**Date**: 2020-09-10
**URL**: https://discourse.slicer.org/t/adding-fiducial-marks-and-determining-ras-coordinates/13421

---

## Post #1 by @Anish_Basnet (2020-09-10 12:58 UTC)

<p>Hello everyone,<br>
Is there anyway to add fiducial markers to a stl data without the markups module? I want to add fiducial markers manually to the module I am working on. I’d like to display the RAS coordinates to the module GUI.</p>

---

## Post #2 by @ungi (2020-09-11 19:24 UTC)

<p>Hi,<br>
You can take advantage of the markups module in your own module, without using the markups module in a visible way. There are examples in the script repository how to use module functions (including markups) from your module: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Switching_to_markup_fiducial_placement_mode" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Switching_to_markup_fiducial_placement_mode</a><br>
I hope this helps,<br>
Tamas</p>

---

## Post #3 by @Anish_Basnet (2020-09-12 10:47 UTC)

<p>Hello Tamas,<br>
Thank you for your reply! This is written in python but I am extending a cxx file. Can the same thing be done in C++ along with the QT framework? If it can be done, I am really counting on your suggestions.</p>
<p>Best regards,<br>
Anish</p>

---

## Post #4 by @ungi (2020-09-12 15:17 UTC)

<p>Yes, the Markups module is written in C++, so you should be able to use the same functions in a C++ loadable module too.<br>
I think it is very rare that people use C++ to write Slicer modules nowadays. If an application-specific workflow needs to be supported by a custom Slicer module, Python seems to be a more efficient choice.</p>

---

## Post #5 by @Anish_Basnet (2020-09-14 07:33 UTC)

<p>Thank you for your reply. Is there any example to do that? Cause I researched on the internet but I did not find a solution.</p>

---

## Post #6 by @ungi (2020-09-14 13:29 UTC)

<p>If you are looking for an example C++ module that uses fiducials for registration, this one comes to mind:<br>
</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="15" height="15">
      <a href="https://github.com/SlicerIGT/SlicerIGT/tree/master/FiducialRegistrationWizard" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars1.githubusercontent.com/u/2845029?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/SlicerIGT/SlicerIGT/tree/master/FiducialRegistrationWizard" target="_blank" rel="noopener nofollow ugc">SlicerIGT/SlicerIGT</a></h3>

<p>Modules supporting image-guided interventions in 3D Slicer. - SlicerIGT/SlicerIGT</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
This is a convenience module that keeps track of two fiducial lists and computes registration between them. The result is stored in a transform node that can be used by other modules.

---

## Post #7 by @Anish_Basnet (2020-09-14 17:37 UTC)

<p>Thank you very much for your reply! I really had a hard time understanding the module. As I said earlier, I’d only want to display the fiducial point with RAS coordinates. I am new to VTK and 3D slicer. Therefore, I’d really appreciate your help.</p>

---

## Post #8 by @ungi (2020-09-14 17:42 UTC)

<p>Why don’t you use the Markups module? If you expand the “Control Points” section of the Markups module widget, you can see the RAS coordinates there.</p>

---

## Post #9 by @jamesobutler (2020-09-14 17:43 UTC)

<p>I think what you are wanting is exactly what the qSlicerSimpleMarkupsWidget provides.</p>
<pre data-code-wrap="python"><code class="lang-python">simple_markups = slicer.qSlicerSimpleMarkupsWidget()
simple_markups.setMRMLScene(slicer.mrmlScene)
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77c9a636a6663879e8bdad26ab29e72300129db0.png" alt="image" data-base62-sha1="h5GQJx2Op6aWK4gq1jhZHZ11n6U" width="294" height="234"></p>
<p>Or the Markups module<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da1183e2cce09b778ed913538524d5afd2e47e6b.png" data-download-href="/uploads/short-url/v77C6JVhPqluxlBmAaP7X2BWI55.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da1183e2cce09b778ed913538524d5afd2e47e6b_2_345x375.png" alt="image" data-base62-sha1="v77C6JVhPqluxlBmAaP7X2BWI55" width="345" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da1183e2cce09b778ed913538524d5afd2e47e6b_2_345x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da1183e2cce09b778ed913538524d5afd2e47e6b_2_517x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da1183e2cce09b778ed913538524d5afd2e47e6b.png 2x" data-dominant-color="EDF1F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">528×573 31.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @lassoan (2020-09-14 17:51 UTC)

<aside class="quote no-group" data-username="Anish_Basnet" data-post="7" data-topic="13421">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/anish_basnet/48/7988_2.png" class="avatar"> Anish_Basnet:</div>
<blockquote>
<p>I am new to VTK and 3D slicer.</p>
</blockquote>
</aside>
<p>In this case I would strongly recommend to use Python while you are getting to know the libraries (VTK, ITK, Qt, CTK, Slicer, etc.). Once you know how things work and what exactly you need, you can easily switch back to C++. We often use Python, even for prototyping new Slicer core features that are in the end ported to C++.</p>

---

## Post #11 by @Anish_Basnet (2020-09-15 07:01 UTC)

<p>Thank you very much for your reply! I wanted to deliver the same functionality as control points section of the markups module widget.</p>

---

## Post #12 by @Anish_Basnet (2020-09-15 07:02 UTC)

<p>Thank you very much for your reply! I will try it and let you know.</p>

---

## Post #13 by @Anish_Basnet (2020-09-15 07:04 UTC)

<p>Thank you very much for your suggestions. I have basic knowledge of C++ programming and the project that I am working on right now demands the use of C++. Therefore, I’d like to have a good grasp of development of a module with c++. It’d be nice if you could recommend me some resources that I can rely on.</p>

---

## Post #14 by @lassoan (2020-09-15 17:26 UTC)

<p>Majority of Slicer core is implemented in C++ and there are a number of extensions that use C++ (SlicerRT, SlicerIGT, SlicerOpenIGTLink, SlicerIGSIO, SlicerDMRI, SlicerAstro, SlicerFreeSurfer, GelDosimetry, PerkTutor, etc.) that you can use as examples.</p>

---

## Post #15 by @Anish_Basnet (2020-09-28 11:24 UTC)

<p>Hello everyone,<br>
I am now able to put fiducial points with mouse click. I have used QTableWidget to write the fiducial points in the widget. But I’d like to display the points in real time in the widget. Whenever I place the fiducial point I need it to display in the widget. I went through the Markpus Module but did not understand how they achieved the functionality.</p>

---

## Post #16 by @lassoan (2020-09-28 13:37 UTC)

<p>Instead of redeveloping a table widget for displaying markups control points from scratch, I would recommend to use the widget as <a class="mention" href="/u/jamesobutler">@jamesobutler</a> suggested <a href="https://discourse.slicer.org/t/adding-fiducial-marks-and-determining-ras-coordinates/13421/9">above</a>. It is quite configurable, so it should be able to do exactly what you need, but if you cannot figure out how to achieve something then let us know.</p>

---

## Post #17 by @Anish_Basnet (2020-09-30 09:13 UTC)

<p>Hi Andras,<br>
I am trying to access the class qslicerSimpleMarkupsWidget. As I am doing it with c++, I am now confused about accessing the widget. I suppose James called it using scripted module. Can I convert the scripted code to c++ code somehow?</p>
<p>Best regards,<br>
Anish</p>

---

## Post #18 by @Anish_Basnet (2020-10-05 15:00 UTC)

<p>Hello,<br>
I have found that the fiducial points can be placed with the help of a button using scripted module. But how can I achieve the same functionality using the loadable module?</p>
<pre><code class="lang-python">w=slicer.qSlicerMarkupsPlaceWidget()
w.setMRMLScene(slicer.mrmlScene)
markupsNodeID = slicer.modules.markups.logic().AddNewFiducialNode()
w.setCurrentNode(slicer.mrmlScene.GetNodeByID(markupsNodeID))
# Hide all buttons and only show place button
w.buttonsVisible=False
w.placeButton().show()
w.show()
</code></pre>
<p>Best regards,<br>
Anish</p>

---

## Post #19 by @lassoan (2020-10-08 21:17 UTC)

<p>Do you mean that you would like to translate the Python code above to C++?</p>

---

## Post #20 by @Anish_Basnet (2020-10-09 08:25 UTC)

<p>Hello Andras,<br>
Thank you for the reply. Yes exactly! I read somewhere in the forum that I can add an observer to the fiducial node to monitor the changes and display it in the table widget. But I do not know how to proceed it with c++ code. Therefore, it would be easy for me to display by accessing the qSlicerSimpleMarkupsModule with c++ from my module.</p>
<p>Best regards,<br>
Anish</p>

---

## Post #21 by @lassoan (2020-10-09 13:47 UTC)

<p>Most of Slicer core is implemented in C++ and most module widgets are composed of various Qt, CTK, and Slicer widgets. You can edit the GUI using Qt designer. You can use any of the C++ loadable modules in Slicer core as an example of adding observers and connections.</p>

---
