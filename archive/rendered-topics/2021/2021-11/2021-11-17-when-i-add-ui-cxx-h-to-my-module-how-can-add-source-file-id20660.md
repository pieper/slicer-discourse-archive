# When I add ui , cxx, h to my module, how can add source file?

**Topic ID**: 20660
**Date**: 2021-11-17
**URL**: https://discourse.slicer.org/t/when-i-add-ui-cxx-h-to-my-module-how-can-add-source-file/20660

---

## Post #1 by @kookoo9999 (2021-11-17 13:45 UTC)

<p>Hello all.<br>
Is there a way to add these(.ui , .cxx , .h ) at once? Do you usually add .cxx and .h after adding ui by one click or easily way??<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a4fd15641bdf3d79cb19d169801aa0ce6699078.png" data-download-href="/uploads/short-url/3KLqdG4OrfC7EvFixgVv054LaUo.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1a4fd15641bdf3d79cb19d169801aa0ce6699078_2_357x500.png" alt="image" data-base62-sha1="3KLqdG4OrfC7EvFixgVv054LaUo" width="357" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1a4fd15641bdf3d79cb19d169801aa0ce6699078_2_357x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a4fd15641bdf3d79cb19d169801aa0ce6699078.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a4fd15641bdf3d79cb19d169801aa0ce6699078.png 2x" data-dominant-color="2E2D2E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">413×577 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
and I don’t know the roles of a and the rest of the project.(mymodule, mymoduleWidget ,Logic, LogicPython, etc…).<br>
For example I can add resouce and its class( test.cpp &amp; test.h) easy in MFC . I know  way like this.<br>
Or do I need to edit it and build it through CMAKE? I wonder if there is such a tutorial.</p>
<p>I tried the above-mentioned method, but I am not sure how to deal with the functions of ui that I randomly added in the module project.</p>
<p>Thanks for reading this.</p>

---

## Post #2 by @lassoan (2021-11-17 18:15 UTC)

<aside class="quote no-group" data-username="kookoo9999" data-post="1" data-topic="20660">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kookoo9999/48/12394_2.png" class="avatar"> kookoo9999:</div>
<blockquote>
<p>For example I can add resouce and its class( test.cpp &amp; test.h) easy in MFC . I know way like this.<br>
Or do I need to edit it and build it through CMAKE? I wonder if there is such a tutorial.</p>
</blockquote>
</aside>
<p>Maybe QtDesigner or QtCreator has wizards for creating ui/cxx/h/_p.h skeletons that is similar to Visual Studio’s MFC class wizards. These can be indeed useful for the first few classes when you create a new application from scratch. If you already have an application, then you would lose a lot of time making general-purpose skeletons created by the Wizard conform to your application’s conventions. Instead it is much faster and simpler to find another class in the application that is very similar to what you need and copy and rename it and adapt it to your needs.</p>
<aside class="quote no-group" data-username="kookoo9999" data-post="1" data-topic="20660">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kookoo9999/48/12394_2.png" class="avatar"> kookoo9999:</div>
<blockquote>
<p>Or do I need to edit it and build it through CMAKE? I wonder if there is such a tutorial.</p>
</blockquote>
</aside>
<p>You follow generic Qt application development process using CMake and Visual Studio. There is nothing specific to Slicer. All these tools are use by many people, so probably you can find tutorials out there, but you can also just learn by reading the code.</p>
<p>In the end, you will just copy files (.cxx, .h, .ui, …), rename them and rename the class contained in them, and add the new files to the CMakeLists.txt file.</p>

---

## Post #3 by @kookoo9999 (2021-11-18 01:01 UTC)

<p>Thanks for your kindness <a class="mention" href="/u/lassoan">@lassoan</a>  <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"> . I’ve been learning a lot from your kind explanation for a few days.<br>
One difficult part is the difference and function between mymodule.ui and mymodulewidget.ui. And if I look at the script module, I understand what logic does within python, but where should I define the function according to the event for the button or other tool in c++?</p>

---

## Post #4 by @lassoan (2021-11-18 14:26 UTC)

<p>Usually a module has a widget that appears on the left panel. It is always built using a .ui file.</p>
<p>Many modules offer reusable widgets that other modules can use. If such a widget is composed of many other widgets then it is often built using a .ui file, too.</p>

---

## Post #5 by @nnzzll (2022-08-30 11:31 UTC)

<p>I’d like to customize the extension using totally new ui designed by myself. However, as you said, the extension widget is inserted to the module panel widget. How to setup the widget ui in the main window?</p>

---

## Post #6 by @lassoan (2022-08-30 20:11 UTC)

<p>You can hide all built-in Slicer GUI components that you don’t want your users to see (using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#module-slicer.util">set…visible() functions in slicer.util</a> package, for example <code>slicer.util.setMenuBarsVisible(False)</code>), then add any widgets, docking windows, etc. anywhere you want using Qt. If you have any specific questions then let us know.</p>

---

## Post #7 by @nnzzll (2022-08-31 03:51 UTC)

<p>Thanks for the reply and I do have a question.<br>
setVisible() function works in python interactor, however , I’m working on a loadable extension. I called the setVisible() method of the module panel widget in the <code>enter()</code> method and it doesn’t work.<br>
Here is my code:</p>
<pre><code class="lang-auto">void qSlicerVelaTraumaModuleWidget::enter()
{
  Q_D(qSlicerVelaTraumaModuleWidget);
  this-&gt;Superclass::enter();
  auto app = qSlicerApplication::application();
  auto modulePanel = app-&gt;mainWindow()-&gt;findChildren&lt;QDockWidget*&gt;();
  qDebug() &lt;&lt; modulePanel.count();
  for(int i=0;i&lt;modulePanel.count();i++)
  {
    qDebug() &lt;&lt; modulePanel.at(i);
    modulePanel.at(i)-&gt;setVisible(false);
  }
}
</code></pre>
<p>The <code>qDebug() &lt;&lt; modulePanel.at(i);</code> line do return the right <code>QDockWidget</code> but the <code>setVisible(false)</code> call doesn’t work at all.</p>

---
