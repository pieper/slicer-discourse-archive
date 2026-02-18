# Safe way to handle QT events

**Topic ID**: 41686
**Date**: 2025-02-13
**URL**: https://discourse.slicer.org/t/safe-way-to-handle-qt-events/41686

---

## Post #1 by @DouSam (2025-02-13 18:32 UTC)

<p>We are working on the <a href="https://github.com/SlicerLatinAmerica/SlicerTutorialMaker/" rel="noopener nofollow ugc">TutorialMaker</a> extension. One of the processes is to execute the tutorial, you can see one <a href="https://github.com/SlicerLatinAmerica/TestSlicerTutorials/blob/main/Tutorials/FourMinuteTutorial/FourMinuteTutorial.py" rel="noopener nofollow ugc">here</a>.<br>
The idea is to recreate the steps like a user normally does and take a screenshot after this step, but we are having problems with the qt events. For example:<br>
Simulate that click to open the Red Slice Controller<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f174c58469a8bd70cc8daadbaa670f172fca76e.png" data-download-href="/uploads/short-url/i8iypfTdNm0lVjhZ5Y6MMHeS4mW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f174c58469a8bd70cc8daadbaa670f172fca76e.png" alt="image" data-base62-sha1="i8iypfTdNm0lVjhZ5Y6MMHeS4mW" width="690" height="86" data-dominant-color="633833"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">798×100 7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
We have tried to use the click event on the pin button and the show event directly on the SlicerController and we have the same problem. Sometimes in the screenshot, that event was processed and appears on the screenshot and sometimes not.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/1857c45421deaa7d61017d418490edb35a16ef93.png" alt="image" data-base62-sha1="3tluWfLkVZr37SNa6YX46fnMbV9" width="283" height="52"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99b795ff7b95df5490fb6528e0f9d2155fcdcb63.png" alt="image" data-base62-sha1="lVQnOarN59pY367CTfzgpiCzR19" width="281" height="50"><br>
The problem is, that we don’t have control if the event is processed or not, and that variable from OS to OS, on MAC, tends to be more broken, and the event is processed two or three screenshots later.</p>
<p>We have to use .update() on the widget after and before the event and the slicer.app.processEvents() before taking the screenshot, but that makes our extension slow.</p>
<p>My question here is, how we should replicate these events? Like this click to open the Slicer Controller on the screenshot. Is there a way to control that?<br>
Something like:</p>
<pre><code class="lang-auto">clickEvent = await widget.click()
</code></pre>
<p>So we know when we call the <code>Tutorial.nextScreenshot()</code> this popout will appear on the screenshot.</p>
<p>Obs: We know that is possible to manipulate the model using the slicer API, and we do that, but it’s important to show the Slicer Controller so the user who is reading the Tutorial knows where he clicks to manipulate the red slice.</p>

---

## Post #2 by @lassoan (2025-02-13 20:21 UTC)

<p>The slice view controller widget is displayed with a quick animation. You may need to wait a bit to get it fully displayed.</p>
<p>I would recommend to try to execute the tutorial script with a QTimer. This way, instead your Python script of taking over the the applicaiton and then trying to give some time to the application to process events; the application would run as normal. The actions you need to do would be performed one by one, in the timer callback.</p>

---
