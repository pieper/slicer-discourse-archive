# How to modify .py extension script and load it by defualt

**Topic ID**: 9142
**Date**: 2019-11-14
**URL**: https://discourse.slicer.org/t/how-to-modify-py-extension-script-and-load-it-by-defualt/9142

---

## Post #1 by @manjula (2019-11-14 08:30 UTC)

<p>Can someone please tell me how to load a extension with the defaults values i want ? I have no knowledge in python or 3D Slicer python scripts.</p>
<p>I need to load CMF surface registration module with landmark set to 1000 by default.</p>
<p>The python script is in</p>
<p>~/.config/NA-MIC/Extensions-28562/CMFreg/lib/Slicer-4.11/qt-scripted-modules</p>
<p>i tried edition SurfaceRegistration.py at that location</p>
<pre><code>    **self.numberOfLandmarksValueChanged = 200** and change it to  **self.numberOfLandmarksValueChanged = 1000** 
</code></pre>
<p>but i don’t know how to load this modified script to 3D Slicer</p>
<p>Also in the CMF registraion module maximum landmarks thta i can select is 2000. Is it possible to increase this value to 4000 ?</p>
<p>thanks</p>

---

## Post #2 by @manjula (2019-11-14 08:52 UTC)

<p>Figured it out…<img src="https://emoji.discourse-cdn.com/twitter/stuck_out_tongue.png?v=9" title=":stuck_out_tongue:" class="emoji" alt=":stuck_out_tongue:"></p>

---

## Post #3 by @lassoan (2019-11-14 14:40 UTC)

<p>If others come across this problem in the future: you can edit the .py file, save it, restart Slicer. If you enable Developer mode (in menu: Edit / Application settings / Developer) then developer tools appear at the top of scripted modules, which allow you to open the .py of the module by a single click and reload the module without restarting Slicer.</p>

---

## Post #4 by @manjula (2019-11-14 16:59 UTC)

<p>I did it via developer mode.  i asked the question when i edited and save the .py and restart the slicer, the changes i made did not take effect. It still does not in that way. But for me the developer mode solved my problem.<br>
i even uninstall the cmf reigstration module and manually installed it with the edited py file in place still it did not work.</p>
<p>Any ideas why saving and restarting the program does not work ?</p>

---

## Post #5 by @lassoan (2019-11-14 17:24 UTC)

<p>If changing a .py file does not have an effect then most likely you have added multiple versions of the same file to the module paths (e.g., files were already bundled with Slicer and you installed another copy manually or via extension manager). If you search for files with the exact same name on your entire computer then most likely you’ll find the duplicate.</p>

---

## Post #6 by @manjula (2019-11-14 23:11 UTC)

<p>Thank you for your reply. i think it worked.</p>

---
