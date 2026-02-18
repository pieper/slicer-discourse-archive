# Making keyboard shortcuts to open modules

**Topic ID**: 21375
**Date**: 2022-01-10
**URL**: https://discourse.slicer.org/t/making-keyboard-shortcuts-to-open-modules/21375

---

## Post #1 by @hourglassnam (2022-01-10 05:05 UTC)

<p>Hi everyone!<br>
I have been writing a python script that allows opening specific modules using keyboard shortcuts.<br>
However, the script does not work quite right.<br>
Below is what I could put together based on the forum topics.</p>
<blockquote>
<p><span class="hashtag-raw">#Makes</span> selected module to popup as second module<br>
def openSegmentEditor():<br>
slicer.modules.segmenteditor.widgetRepresentation().setParent(None)<br>
slicer.modules.segmenteditor.widgetRepresentation().show()</p>
<p><span class="hashtag-raw">#setup</span> the short cut<br>
shortcut1 = qt.QShortcut(slicer.util.mainWindow())<br>
shortcut1.setKey(qt.QKeySequence(“Ctrl+n”))<br>
shortcut1.connect( ‘activated()’, openSegmentEditor)</p>
</blockquote>
<p>This script allowed me to open the segment module as a second panel using ctrl+n.<br>
However, the SegmentEditor hotkeys(numbers, shit+numbers) do not work when opened as a second module.</p>
<p>I am new to python, and I have been looking all over the forum but could not find the proper solution to this problem.<br>
I would be grateful if anyone could help me out with this.</p>
<p>So my questions are:</p>
<ol>
<li>Is there any way to open the module on the main panel?</li>
<li>I am currently planning to make a shortcut that would allow me to not only open the module but also lead me to the exact widget. For instance, I want to create a shortcut that would directly lead me to EraseInside of the Scissor from the main window. Would this be better, or should I just set up a toggle hotkey and switch around?</li>
</ol>
<p>Thank you always for sharing your knowledge!</p>

---

## Post #2 by @chir.set (2022-01-10 07:43 UTC)

<aside class="quote no-group" data-username="hourglassnam" data-post="1" data-topic="21375">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hourglassnam/48/11796_2.png" class="avatar"> hourglassnam:</div>
<blockquote>
<p>Is there any way to open the module on the main panel?</p>
</blockquote>
</aside>
<p>Try this :</p>
<pre><code class="lang-auto">#Makes selected module to popup as second module
def openSegmentEditor():
  mainWindow = slicer.util.mainWindow()
  mainWindow.moduleSelector().selectModule('SegmentEditor')

  
  
#setup the short cut
shortcut1 = qt.QShortcut(slicer.util.mainWindow())
shortcut1.setKey(qt.QKeySequence('Ctrl+n'))
shortcut1.connect('activated()', lambda: openSegmentEditor())
</code></pre>
<p>Use single quotes only :  <code>‘activated()’ -&gt; 'activated()'</code></p>

---

## Post #4 by @hourglassnam (2022-01-10 08:04 UTC)

<p>That worked beautifully! Thank you so much!!</p>

---

## Post #5 by @hourglassnam (2022-01-10 08:36 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="2" data-topic="21375">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Use single quotes only : <code>‘activated()’ -&gt; 'activated()'</code></p>
</blockquote>
</aside>
<p>May I ask one additional question?<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html</a><br>
In here, they used “activated()”.<br>
May I ask why I should only use single quote?</p>

---

## Post #6 by @chir.set (2022-01-10 08:45 UTC)

<aside class="quote no-group" data-username="hourglassnam" data-post="5" data-topic="21375">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hourglassnam/48/11796_2.png" class="avatar"> hourglassnam:</div>
<blockquote>
<p>May I ask why I should only use single quote?</p>
</blockquote>
</aside>
<p>In your first post, the ‘activated()’ signal is not between single quotes, but other similarly looking characters, at least the second ‘quote but not a quote’. By copy/paste in the python console, it won’t run. I did not try with double quotes, may be it’s OK. I meant : not other characters that look like single quote.</p>

---

## Post #7 by @hourglassnam (2022-01-10 09:02 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="6" data-topic="21375">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>In your first post, the ‘activated()’ signal is not between single quotes, but other similarly looking characters, at least the second ‘quote but not a quote’. By copy/paste in the python console, it won’t run. I did not try with double quotes, may be it’s OK. I meant : not other characters that look like single quote.</p>
</blockquote>
</aside>
<p>Aha! I understand now! Thank you for your reply!</p>

---

## Post #8 by @DIV (2022-01-18 05:30 UTC)

<p>The quotation issue may be an “auto-correct”/rendering issue with the discourse forum, for text outside of ‘code’ demarcation boundaries…</p>
<pre><code class="lang-auto"># [...] an "auto-correct" issue with the discourse forum, for text outside of 'code' demarcation boundaries....
dummy = "text"
</code></pre>
<p><strong>chir.set</strong> is right to warn about this, though, as it can lead to unexpected problems!</p><aside class="quote quote-modified" data-post="7" data-topic="20236">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/segment-editor-reduce-the-number-of-mouse-clicks-to-set-basic-colour-for-segment/20236/7">Segment Editor: reduce the number of mouse clicks to set basic colour for segment</a> <a class="badge-category__wrapper " href="/c/support/feature-requests/9"><span data-category-id="9" style="--category-badge-color: #F1592A; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="11" data-drop-close="true" class="badge-category --has-parent" title="This category is for submitting ideas about what enhancements or new features should be added to 3D Slicer. Make your voice heard by voting on feature requests - by opening the topic and clicking the Vote button or by creating a new topics. Slicer developers will make it a priority to work on feature requests that have more votes."><span class="badge-category__name">Feature requests</span></span></a>
  </div>
  <blockquote>
    Hello, James. 
My username is purely alphanumeric;  besides that, the file is exactly where I said:   C:/Users/[username]/.slicerrc.py. 
thinking… 
working… 
OK, I have found the cause of the error message. 
I had inserted the following into the start-up script file (on the last three lines): 
# Always use the “Basic” color picker
# https://discourse.slicer.org/t/segment-editor-reduce-the-number-of-mouse-clicks-to-set-basic-colour-for-segment/20236/3
ctk.ctkColorDialog().setDefaultTab(0)

If you…
  </blockquote>
</aside>
<p>
—DIV</p>

---
