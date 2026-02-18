# How to modify Slicer's style

**Topic ID**: 25300
**Date**: 2022-09-16
**URL**: https://discourse.slicer.org/t/how-to-modify-slicers-style/25300

---

## Post #1 by @miniminic (2022-09-16 08:39 UTC)

<p>I want to change the style of the whole Slice person, I guess Slicer should have a QSS file, or change the style in a unified place</p>

---

## Post #2 by @Sam_Horvath (2022-09-16 16:07 UTC)

<p>While Slicer does not currently use QSS for styling (QStyles are used), you can still apply stylesheets to the slicer app through Python.</p>
<aside class="quote quote-modified" data-post="1" data-topic="15509">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-developer-feature-styletester/15509">New Developer Feature - StyleTester</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    We’ve added a new utility module to the SlicerSandbox extension,  <a href="https://github.com/PerkLab/SlicerSandbox/tree/master/StyleTester">StyleTester</a>.  StyleTester allows you to test modifying the appearance of the Slicer GUI using <a href="https://doc.qt.io/qt-5/stylesheet.html">Qt Style Sheets</a>.  Qt Style Sheets provide an very powerful method for customizing every aspect of the appearance of a Qt-based application like Slicer. 
QSS code can be entered into the editor, or loaded from / saved to .qss files.  The module provides a set of example widgets that can be used to view effects of stylesheets on the most wi…
  </blockquote>
</aside>

<aside class="onebox githubblob" data-onebox-src="https://github.com/PerkLab/SlicerSandbox/blob/0039772ccfff02dd59bf376d463094d480992fcb/StyleTester/StyleTester.py#L123">
  <header class="source">

      <a href="https://github.com/PerkLab/SlicerSandbox/blob/0039772ccfff02dd59bf376d463094d480992fcb/StyleTester/StyleTester.py#L123" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/PerkLab/SlicerSandbox/blob/0039772ccfff02dd59bf376d463094d480992fcb/StyleTester/StyleTester.py#L123" target="_blank" rel="noopener">PerkLab/SlicerSandbox/blob/0039772ccfff02dd59bf376d463094d480992fcb/StyleTester/StyleTester.py#L123</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="113" style="counter-reset: li-counter 112 ;">
          <li>  with open(stylesheetfile,"r") as fh:</li>
          <li>    self.ui.plainTextEdit.plainText = fh.read()</li>
          <li></li>
          <li>def onSaveFileSelected(self, stylesheetfile):</li>
          <li>  with open(stylesheetfile,"w") as fh:</li>
          <li>    fh.write( self.ui.plainTextEdit.plainText)</li>
          <li></li>
          <li>def onApply(self):</li>
          <li>  styleSheet = self.ui.plainTextEdit.plainText</li>
          <li>  if self.ui.slicerRadio.isChecked():</li>
          <li class="selected">    slicer.app.styleSheet = styleSheet</li>
          <li>  else:</li>
          <li>    self.ui.Examples.setStyleSheet(styleSheet)</li>
          <li></li>
          <li>def onClear(self):</li>
          <li>  if self.ui.slicerRadio.isChecked():</li>
          <li>    slicer.app.styleSheet = ""</li>
          <li>  else:</li>
          <li>    self.ui.Examples.setStyleSheet("")</li>
          <li></li>
          <li>def cleanup(self):</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @miniminic (2022-09-17 06:15 UTC)

<p>But after you restart the program, the style goes back to the default</p>

---
