# Ctk collapsible button in qt designer

**Topic ID**: 9955
**Date**: 2020-01-26
**URL**: https://discourse.slicer.org/t/ctk-collapsible-button-in-qt-designer/9955

---

## Post #1 by @Juicy (2020-01-26 09:49 UTC)

<p>Hi I am hoping someone can help me with how to use ctk collapsible buttons in qt designer when trying to design a UI for a scripted module.</p>
<p>I first drag and drop a ctk collasible button into the UI area. Then I have to increase the collapsed height setting to make it bigger in height to actually fit anything inside. I then drag buttons and drop down boxes etc into it.</p>
<p>My problem is when I load the module in slicer all the buttons etc in the collapsible button do not expand and contract when I drag the width of the module UI pane bigger and smaller. The buttons just stay the same size and either partially get hidden when I drag the module UI really small or there is lots of white space next to them when I drag the UI really wide.</p>
<p>This was never a problem for me when making a scripted module UI the old fashioned way with code instead of qt designer. All the buttons etc in my collapsible buttons would change size nicely when I dragged the slicer module UI pane wider and narrower.</p>
<p>I have tried playing around with settings in qt designer and cant get anything to work.</p>
<p>Hopefully my description makes sense.</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2020-01-26 12:12 UTC)

<p>After you placed a widget in the collapsible widget area, you need to right-click on the collapsible button and choose a layout. It used to require 1-2 lines of code, but now it takes just two clicks.</p>
<p>You can look for “Qt designer” tutorials on the web that should help you getting started. If you find good ones then you can post the links here so that others can learn, too.</p>

---

## Post #3 by @Juicy (2020-01-26 19:15 UTC)

<p>Thanks, it worked. Right clicked on the collapsible button and chose “Lay out in a form layout” and that worked how I wanted it to.</p>
<p>I will see if I can find any tutorials.</p>
<p>Thanks again</p>

---
