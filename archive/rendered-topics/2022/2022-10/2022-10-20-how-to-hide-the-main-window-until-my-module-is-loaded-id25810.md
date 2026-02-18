# How to hide the main window until my module is loaded

**Topic ID**: 25810
**Date**: 2022-10-20
**URL**: https://discourse.slicer.org/t/how-to-hide-the-main-window-until-my-module-is-loaded/25810

---

## Post #1 by @Corain (2022-10-20 13:57 UTC)

<p>Operating system: Win 10<br>
Slicer version: Slicer 5.0.3<br>
Expected behavior: Directly show the GUI of my module when I open MyModule.exe.<br>
Actual behavior: It will show the Slicer welcome page for a second first and then jump to my GUI.</p>
<p>I write a module with its own interface for my project referring to the QuickSegment Slicelet example. And I clone the .exe and .ini files as stated <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets" rel="noopener nofollow ugc">here</a> so I can open my module by MyModule.exe. The problem is when I open it the original Slicer GUI will show first and then automatically switch to my GUI.</p>
<p>Is there a way to prevent the Slicer GUI from showing? Or can I hide the main window as default and then call mainWindow.show() in my module?</p>
<p>Thank you!</p>

---

## Post #2 by @cpinter (2022-10-20 15:07 UTC)

<p>You could play with the <code>--no-main-window</code> launcher option and see if you can display it again when your module is initialized.</p>
<p>However, you may want to look into <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate">Slicer Custom Apps</a>. All you need to do is generate your custom app skeleton with the cookie cutter, add your module and set it as home module. Then you’ll have more control about the application.</p>

---

## Post #3 by @Corain (2022-10-20 16:13 UTC)

<p>Thanks for your reply! The --no-main-window option doesn’t work because I cannot launch my module without the main window. I will try the Slicer Custom Apps.</p>

---

## Post #4 by @cpinter (2022-10-21 07:38 UTC)

<p>Yes this is why I used the word “play” with the option. When your module is up and its setup is called, you could try changing some setting of the main window then showing it for a moment before you hide it again… But the custom app is the hack-free way.</p>

---
