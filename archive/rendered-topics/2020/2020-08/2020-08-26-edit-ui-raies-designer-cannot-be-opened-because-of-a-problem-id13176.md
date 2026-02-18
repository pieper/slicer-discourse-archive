# Edit UI raies 'Designer cannot be opened because of a problem' 

**Topic ID**: 13176
**Date**: 2020-08-26
**URL**: https://discourse.slicer.org/t/edit-ui-raies-designer-cannot-be-opened-because-of-a-problem/13176

---

## Post #1 by @Yusuke (2020-08-26 13:20 UTC)

<p>Hi,</p>
<p>I am following this tutorial; <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx?raw=true" rel="nofollow noopener">https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx?raw=true</a></p>
<p>‘Edit UI’ button was not working in my Slicer (page 36) and my understanding is that the button shows the qt designer window (page 39).</p>
<p>Clicking ‘Edit UI’ shows a popup saying <code>Designer cannot be opened because of a problem  </code> but after that, I couldn’t reproduce the popup window and nothing happens in clicking.</p>
<p>My slicer version is 4.11.0-2020-08-24.<br>
Any thoughts and comments are appreciated!</p>

---

## Post #2 by @lassoan (2020-08-26 15:12 UTC)

<p>What operating system this is?<br>
Have you built Slicer yourself?</p>

---

## Post #3 by @Yusuke (2020-08-26 15:15 UTC)

<p>I’m using macOS Mojave (10.14.6).<br>
I’ve noticed that there is error log which says ‘dyld: Library not loaded: /Volumes/D/Support/qt-everywhere-build-5.15.0/lib/QtDesignerComponents.framework/Versions/5/QtDesignerComponents<br>
Referenced from: /Applications/Slicer.app/Contents/bin/Designer.app/Contents/MacOS/Designer<br>
Reason: image not found<br>
error: [/Applications/Slicer.app/Contents/bin/Designer.app/Contents/MacOS/Designer] exit abnormally - Report the problem.’</p>
<p>In my mac, there is no /Volumes/D/ directly.<br>
I just downloaded Slicer and I don’t think I built it myself.</p>

---

## Post #4 by @lassoan (2020-08-26 15:20 UTC)

<p>You can start the designer on MacOS directly see:</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/4700#issuecomment-604689824" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/4700#issuecomment-604689824" target="_blank" rel="noopener">QT Designer does not start on MacOS</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-13" data-time="01:05:20" data-timezone="UTC">01:05AM - 13 Mar 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank" rel="noopener">
          <img alt="slicerbot" src="https://avatars3.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">This issue was created automatically from an original Mantis Issue. Further discussion may take place here.</p>
</div>

<div class="labels">
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #5 by @Yusuke (2020-08-26 15:52 UTC)

<p>Thank you for the link.<br>
I run $ /usr/local/opt/qt5/libexec/Designer.app/Contents/MacOS/Designer and it shows the following windows.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a9fa54b9f01fe418432526b3a0c376d321920bf.jpeg" data-download-href="/uploads/short-url/m3Rzk7SkZKgiZxaD5ATUN12VyEf.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9a9fa54b9f01fe418432526b3a0c376d321920bf_2_690x353.jpeg" alt="image" data-base62-sha1="m3Rzk7SkZKgiZxaD5ATUN12VyEf" width="690" height="353" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9a9fa54b9f01fe418432526b3a0c376d321920bf_2_690x353.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9a9fa54b9f01fe418432526b3a0c376d321920bf_2_1035x529.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9a9fa54b9f01fe418432526b3a0c376d321920bf_2_1380x706.jpeg 2x" data-dominant-color="5A5A5A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1825×936 268 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Is this what I’m supposed to see? I’m wondering if this is correct because I cannot see ‘MyFirstModule.ui’ window which the tutorial shows (page 39).</p>
<p>How can I proceed the tutorial after page 39 and 42?</p>

---

## Post #6 by @lassoan (2020-08-26 17:09 UTC)

<p>Yes, this is what you need to see. You need to load the .ui file.</p>
<p>The “Edit UI” button would load it for you automatically, but we need to fix that button on Mac.</p>

---

## Post #7 by @Yusuke (2020-08-26 17:26 UTC)

<p>I realized I have to open .ui file and yes, I could see other windows that the tutorial shows.<br>
I followed the further instruction but the apply button is not active. (also clicking input Markups button not show anything)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/707e06c05009d3ab3f3d806422a446f4e32355e8.png" data-download-href="/uploads/short-url/g39ubP5Bu51abliOsAGY2mQLqsM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/707e06c05009d3ab3f3d806422a446f4e32355e8_2_684x500.png" alt="image" data-base62-sha1="g39ubP5Bu51abliOsAGY2mQLqsM" width="684" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/707e06c05009d3ab3f3d806422a446f4e32355e8_2_684x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/707e06c05009d3ab3f3d806422a446f4e32355e8_2_1026x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/707e06c05009d3ab3f3d806422a446f4e32355e8.png 2x" data-dominant-color="3E3E3F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1122×820 29.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Could you give me some advice about why it’s not enabled?<br>
I changed all scripts based upon the tutorial but I couldn’t find “selectNodeUponCreation” in the property editor.(page 39)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff9e17badd25c8f3a7608ce3d5a339ed7d4f508b.png" data-download-href="/uploads/short-url/AtisX9y1XEja4obRe5HgRAtF1Oz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff9e17badd25c8f3a7608ce3d5a339ed7d4f508b_2_559x500.png" alt="image" data-base62-sha1="AtisX9y1XEja4obRe5HgRAtF1Oz" width="559" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff9e17badd25c8f3a7608ce3d5a339ed7d4f508b_2_559x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff9e17badd25c8f3a7608ce3d5a339ed7d4f508b_2_838x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff9e17badd25c8f3a7608ce3d5a339ed7d4f508b_2_1118x1000.png 2x" data-dominant-color="66675D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1153×1030 198 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> ’</p>
<p>UI looks different so I’m wondering if I am doing.</p>

---

## Post #8 by @lassoan (2020-08-26 17:34 UTC)

<p>Everything looks good. You need to select valid inputs if you want th Apply button to become active. This behavior (disable Apply button until valid inputs are selected) is implemented in your Python script and you can change it if you want.</p>

---

## Post #9 by @Yusuke (2020-08-26 17:57 UTC)

<p>I’m supposed to be able to select value for Input Markups, correct?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbcb4998fd44ae5587cea76ddd725edb62afc297.png" data-download-href="/uploads/short-url/vmo6F6JFRGluXgNPwZyF3q5FEsD.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbcb4998fd44ae5587cea76ddd725edb62afc297.png" alt="image" data-base62-sha1="vmo6F6JFRGluXgNPwZyF3q5FEsD" width="690" height="41" data-dominant-color="444444"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1110×66 4.23 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Clicking this button happen nothing. Could you tell me how and where I can select inputs?</p>
<p>In Python script, I believe onSelect func defines that.</p>
<pre><code>def onSelect(self):
  self.ui.applyButton.enabled = self.ui.inputSelector.currentNode()
</code></pre>
<p>changing <code>self.ui.applyButton.enabled = True</code> didn’t help.</p>

---

## Post #10 by @lassoan (2020-08-26 18:38 UTC)

<p>You need to create a markups node and then you can select it. You can use Markups module or the toolbar.</p>
<p><code>OnSelect</code> is called when selection changes. If you want the Apply button to be enabled by default then set it so in Qt Designer.</p>

---

## Post #11 by @Yusuke (2020-08-26 19:32 UTC)

<p>Do I have to create multiple markups?<br>
I put some markups but the apply button is still inactive. I tried to place various markups (like circle and plane) but the results are the same.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/4827efc8cc29d7538cd335f9dbbedc127433e4d6.jpeg" data-download-href="/uploads/short-url/aijWo9ouGw3ZSWYiqlrn5IeA6nI.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4827efc8cc29d7538cd335f9dbbedc127433e4d6_2_690x313.jpeg" alt="image" data-base62-sha1="aijWo9ouGw3ZSWYiqlrn5IeA6nI" width="690" height="313" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4827efc8cc29d7538cd335f9dbbedc127433e4d6_2_690x313.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4827efc8cc29d7538cd335f9dbbedc127433e4d6_2_1035x469.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4827efc8cc29d7538cd335f9dbbedc127433e4d6_2_1380x626.jpeg 2x" data-dominant-color="302F2F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2344×1066 314 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>and I was not sure how to place multiple same label markups. Seems like there was ‘Persistent’ checkbox  in the old versions but I cannot see that in the current version.<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html</a></p>

---

## Post #12 by @lassoan (2020-08-26 20:10 UTC)

<p>Markups look good now. As you can see, you have successfully selected them in the node selector.</p>

---

## Post #13 by @Yusuke (2020-08-26 20:16 UTC)

<p>Is the ‘apply’ button supposed to be become active when I select the markup?<br>
Can you tell me how to activate the apply button? The scripts are all changed based upon the tutorial.<br>
Tanks!</p>

---

## Post #14 by @Yusuke (2020-08-27 19:23 UTC)

<p>Even though I selected Input Markup, the Apply button didn’t become active.<br>
I also added print() in onSelect method in MyFirstModuleWidget class but nothing is printed in selecting markup.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c90b5cec0bc2b12fa0304ee605cb94f81207b43a.jpeg" data-download-href="/uploads/short-url/sGwjD6M3BZxP4ZbaZ24jPULYb7c.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c90b5cec0bc2b12fa0304ee605cb94f81207b43a_2_690x376.jpeg" alt="image" data-base62-sha1="sGwjD6M3BZxP4ZbaZ24jPULYb7c" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c90b5cec0bc2b12fa0304ee605cb94f81207b43a_2_690x376.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c90b5cec0bc2b12fa0304ee605cb94f81207b43a_2_1035x564.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c90b5cec0bc2b12fa0304ee605cb94f81207b43a_2_1380x752.jpeg 2x" data-dominant-color="474856"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3338×1820 544 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’m assuming that the onSelect method is not called when I change the markup.</p>
<p>I also tried to check enable box for apply button in qt designer but the apply button is still inactive.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42611f4f6ca96ce1709d9c8a4e90a97592d6c074.png" data-download-href="/uploads/short-url/9tdAZrBnmckCGTQFjdAiJxI4VEw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42611f4f6ca96ce1709d9c8a4e90a97592d6c074_2_588x500.png" alt="image" data-base62-sha1="9tdAZrBnmckCGTQFjdAiJxI4VEw" width="588" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42611f4f6ca96ce1709d9c8a4e90a97592d6c074_2_588x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42611f4f6ca96ce1709d9c8a4e90a97592d6c074_2_882x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42611f4f6ca96ce1709d9c8a4e90a97592d6c074_2_1176x1000.png 2x" data-dominant-color="54554E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1514×1286 303 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @lassoan (2020-08-27 20:36 UTC)

<p>Executing your script line-by-line in a debugger would let you see what exactly your script is doing. See setup instructions here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_can_I_use_a_visual_debugger_for_step-by-step_debugging">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_can_I_use_a_visual_debugger_for_step-by-step_debugging</a></p>

---

## Post #16 by @Yusuke (2020-08-27 22:18 UTC)

<p>Thank you for the link! I setup debugger in pycharm and slicer. I set egg files and it apparently worked correctly but once I set breakpoints and open the ‘MyFirstModule’ module, it didn’t stop at breakpoint…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2c8d60c906a5d4c015c27cd417ab0cfca263a36.jpeg" data-download-href="/uploads/short-url/yDLPUt8a4pdEaLyWtcz7AM0PlB4.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f2c8d60c906a5d4c015c27cd417ab0cfca263a36_2_690x353.jpeg" alt="image" data-base62-sha1="yDLPUt8a4pdEaLyWtcz7AM0PlB4" width="690" height="353" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f2c8d60c906a5d4c015c27cd417ab0cfca263a36_2_690x353.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f2c8d60c906a5d4c015c27cd417ab0cfca263a36_2_1035x529.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f2c8d60c906a5d4c015c27cd417ab0cfca263a36_2_1380x706.jpeg 2x" data-dominant-color="37383D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1831×937 353 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>In this screenshot, I set a breakpoint in <strong>init</strong> of MyFirstModuleWidget class and also put print() before and after it.<br>
As you can see the output, both of the print is exected and I assume the debugger is not working correctly…</p>
<p>I already confirmed that the print() put at the first row in the onSelect() was not printed so can you please tell me how onSelect() works?</p>
<p>I could not find any documentation for ScriptedLoadableModuleWidget.onSelect(). Do you have any documentation for it?</p>

---

## Post #17 by @Yusuke (2020-08-28 17:51 UTC)

<p>I was able to get PyCharm remote debug worked. It’s still unstable and they are often disconnected though.</p>
<p>I tried to use console in PyCharm and tried self.onApplyButton() but got the error.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/8545fff37eb053d1a2d2e5e952ce0ccdc8654152.png" data-download-href="/uploads/short-url/j0ZtBohQoyiqWenrGwJSXnmQIsW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/8545fff37eb053d1a2d2e5e952ce0ccdc8654152.png" alt="image" data-base62-sha1="j0ZtBohQoyiqWenrGwJSXnmQIsW" width="690" height="134" data-dominant-color="393233"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">869×170 21.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Seems like self.ui doesn’t have enableScreenshotsFlagCheckBox.</p>
<p>Is there any documentation that explains how the codes work step-by-step? Even though I would finish this tutorial I feel I would not be able to develop something I want.</p>
<p>If you have something that I can refer, that would be great and very helpful.</p>
<p>Thanks</p>

---
