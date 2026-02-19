---
topic_id: 26628
title: "How To Add My Own Module Widget To Another Module"
date: 2022-12-07
url: https://discourse.slicer.org/t/26628
---

# How to add my own module widget to another module?

**Topic ID**: 26628
**Date**: 2022-12-07
**URL**: https://discourse.slicer.org/t/how-to-add-my-own-module-widget-to-another-module/26628

---

## Post #1 by @drobny (2022-12-07 14:59 UTC)

<p>Hi all,<br>
I have been using Slicer for some basic tasks in the past and just now have started developing my own module. My concept was to simplify the workflow for a clinician to annotate several images. The module should do the communication with an XNAT server to pull the images and push the annotation files (markup JSON files).</p>
<p>Initially, my concept was to create a new GUI that mirrors and wraps the relevant functionality of the Markups module. Learning more about the concept of reusable widgets, I tried to include the widgets I need from Markups. The widget I am missing would be what is in the Control Points collapsible button - mainly the functions on the <code>activeMarkupTableWidget</code>. It seems to have not been made available as a widget or the function logic made accessible from outside so that I could easily replicate the functionality.</p>
<p>I then used <code>slicer.modules.markups.createNewWidgetRepresentation()</code> to include the Markups module into my module but still was missing the functionality of the <code>activeMarkupTableWidget</code>. I tried replicating the setup according to the <code>.cxx</code> file but seem to not understand enough of it to connect the data node and actually display the control points in the table.</p>
<p>My next approach was to add my new functionality as a widget into the markups module (and hide all the UI elements not needed). This might actually make the most sense design wise, according to my current understanding. I managed to clean up and simplify the markups module as desired but struggle to see what needs to be done to instantiate my module as a widget.</p>
<p>Trying this command:</p>
<pre><code class="lang-python">slicer.util.getModuleGui("Markups").layout().addWidget(MyModuleWidget())
</code></pre>
<p>I get the following error:</p>
<pre><code class="lang-auto">'MyModuleWidget' object has no attribute 'createNewWidgetRepresentation'
</code></pre>
<p>I am a bit confused here. Starting from the wizard to create a scriptable module, I end up with a python file containing the following classes: <code>MyModule</code>, <code>MyModuleWidget</code>, <code>MyModuleLogic</code>, <code>MyModuleTest</code>, as well as the GUI file. I would have expected to be able to intantiate the widget as it is. Do I need to implement <code>createNewWidgetRepresentation</code> or add some other bits? I couldn’t find examples for this.</p>
<p>I mentioned my path to arrive at this question as any advice/ comment on this would be appreciated as well and might allow a better approach.<br>
The main question is though: How to add my own module widget to another module?</p>

---

## Post #2 by @drobny (2022-12-07 15:02 UTC)

<p>Here seems to be a related issue with the Markups module:</p><aside class="quote" data-post="6" data-topic="10880">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/would-it-be-possible-to-have-more-then-one-module-panel/10880/6">Would it be possible to have more then one module panel?</a> <a class="badge-category__wrapper " href="/c/support/feature-requests/9"><span data-category-id="9" data-parent-category-id="11" data-drop-close="true" class="badge-category --has-parent" title="This category is for submitting ideas about what enhancements or new features should be added to 3D Slicer. Make your voice heard by voting on feature requests - by opening the topic and clicking the Vote button or by creating a new topics. Slicer developers will make it a priority to work on feature requests that have more votes."><span class="badge-category__name">Feature requests</span></span></a>
  </div>
  <blockquote>
    Actually, while this popups up the module, the module itself is not functional. I am trying particularly with the Markups module, and you can’t see the control points, nor modify their color/size etc with the popup Markups module, while the docked one in the main module panel works fine.
  </blockquote>
</aside>


---

## Post #3 by @lassoan (2022-12-07 22:20 UTC)

<p><code>slicer.qSlicerSimpleMarkupsWidget()</code> is a reusable widget for managing markup control points. For example, it is used in <code>Fiducial registration wizard</code> module of SlicerIGT extension.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2b3295d4261dd10967ec931e5468cc22082db99.png" data-download-href="/uploads/short-url/rMotPELl4I5cJ6BVoqKUvaFzQwh.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2b3295d4261dd10967ec931e5468cc22082db99_2_422x500.png" alt="image" data-base62-sha1="rMotPELl4I5cJ6BVoqKUvaFzQwh" width="422" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2b3295d4261dd10967ec931e5468cc22082db99_2_422x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2b3295d4261dd10967ec931e5468cc22082db99_2_633x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2b3295d4261dd10967ec931e5468cc22082db99_2_844x1000.png 2x" data-dominant-color="3A3D3F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1067×1262 83.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can also create simple custom widget for landmarking, such as in <a href="https://github.com/OrthodonticAnalysis/SlicerOrthodonticAnalysis">OrthodonticAnalysis</a> extension:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42847ebb0b599da5cc8d663af6477897ec8e7065.png" data-download-href="/uploads/short-url/9urnHOLpQBMPlo8pNgMAnV3H9jL.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42847ebb0b599da5cc8d663af6477897ec8e7065_2_690x380.png" alt="image" data-base62-sha1="9urnHOLpQBMPlo8pNgMAnV3H9jL" width="690" height="380" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42847ebb0b599da5cc8d663af6477897ec8e7065_2_690x380.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42847ebb0b599da5cc8d663af6477897ec8e7065_2_1035x570.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42847ebb0b599da5cc8d663af6477897ec8e7065_2_1380x760.png 2x" data-dominant-color="5D5E4E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1245 489 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>We plan to factor out the control point list that you see in Markups module (with all the landmarking features):</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6452">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6452" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6452" target="_blank" rel="noopener">Add reusable widget for markups control point list</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-06-28" data-time="03:26:55" data-timezone="UTC">03:26AM - 28 Jun 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Enhancement
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Is your feature request related to a problem? Please describe.

qSlicerSimp<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">leMarkupsWidget does not support any of the new features that are available in the Markups module's control point table widget.

## Describe the solution you'd like

We would need to create a new qSlicerMarkupsControlPointTableView+Model that could replace both these widgets.

## Additional context

I've started to work on this at some point but then ran out of time. The development branch is available here: https://github.com/lassoan/Slicer/tree/attic/markups-control-points-table-view</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I’m not sure if there is any funded project that requires this feature, so you need to wait for a while - or contribute time or funding to make it happen sooner.</p>

---

## Post #4 by @drobny (2022-12-08 14:31 UTC)

<p>Thank you a lot, Andras. These are very useful recommendations! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Do you also have an advice or a pointer towards how to make one’s widget available to be added to other modules? What has to be done to create an actual widget, not just a full module, from the MyModuleWidget() class?</p>

---

## Post #5 by @lassoan (2022-12-08 16:47 UTC)

<aside class="quote no-group" data-username="drobny" data-post="4" data-topic="26628">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/5daacb/48.png" class="avatar"> drobny:</div>
<blockquote>
<p>Do you also have an advice or a pointer towards how to make one’s widget available to be added to other modules?</p>
</blockquote>
</aside>
<p>You can import the widget in a separate class (if you work in Python you can put it into a separate file, but it may also stay in the single module .py file) and import and use it in another module.</p>
<p>Most of the reusable widgets are implemented in Slicer core in C++, but there are a few examples in Python in extensions, for example in <a href="https://github.com/SlicerHeart/SlicerHeart/tree/master/CardiacDeviceSimulator/CardiacDeviceSimulatorUtils">Cardiac Device Simulator module in SlicerHeart</a>.</p>

---

## Post #6 by @drobny (2022-12-14 16:56 UTC)

<p>I wanted to create two widgets in my module, one widget with the main functionality and the second widget that modifies the markup module GUI (to only show the control points table) and attaches the first widget to the markup layout. This is a hack to go around re-implementing the markup control point table.</p>
<p>The problem with this approach is, that I cannot create two widgets using <code>ScriptedLoadableModuleWidget</code> and .ui files. When setting up the module and two widget classes in the following way:</p>
<pre><code class="lang-auto">class MyModule(ScriptedLoadableModule):...

class MyModuleWidget(ScriptedLoadableModuleWidget, VTKObservationMixin):...

class MyModuleSecondWidget(ScriptedLoadableModuleWidget, VTKObservationMixin):...
</code></pre>
<p>I get the following error when calling <code>ScriptedLoadableModuleWidget.setup(self)</code> for the second widget:</p>
<pre><code class="lang-auto">AttributeError: module 'modules' has no attribute 'mymodulesecond'
</code></pre>
<p>I didn’t manage to understand how to create the second widget without slicer expecting a corresponding module.</p>
<p>I then tried to follow the example of the Cardiac Device Simulator module and used <code>qt.QWidget</code> instead of <code>ScriptedLoadableModuleWidget</code>. To be able to load and use the second .ui file, I had to replace the function <code>self.layout.addWidget(uiWidget)</code> with</p>
<pre><code class="lang-auto">layout = qt.QVBoxLayout()
layout.addWidget(uiWidget)
self.setLayout(layout)
</code></pre>
<p>This has worked for me but I wanted to report my process for future reference and to mention the issue with using two widget classes based on <code>ScriptedLoadableModuleWidget</code>.</p>

---

## Post #7 by @lassoan (2022-12-14 21:46 UTC)

<p>Only the <code>&lt;ModuleName&gt;Widget</code> class is special in the sense that Slicer discovers and instantiates that automatically. You can create all other widgets as regular Python classes and instantiate them as usual. If you create a new widget <code>MyCustomWidget</code> then you can access it from another module like this:</p>
<pre><code class="lang-python">import MyModule
w = MyModule.MyCustomWidget()
</code></pre>

---

## Post #8 by @drobny (2022-12-15 13:56 UTC)

<p>Ok, understood.</p>
<p>I think it threw me off, that it doesn’t seem possible to have multiple widget classes using <code>ScriptedLoadableModuleWidget</code> in the same module. It took me a while to identify the problem (though I still don’t understand why it behaves like this) and to find the workaround going back to  <code>QWidget</code>. If this is the intended behaviour of widgets, it could be useful including a second widget setup in the module wizard/ demo module.</p>

---

## Post #9 by @lassoan (2022-12-15 14:39 UTC)

<p>You can add any number of widgets from .ui files using <code>loadUI</code> - see documentation and example <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.childWidgetVariables">here</a>.</p>

---

## Post #10 by @drobny (2022-12-15 16:03 UTC)

<p>When creating two widget classes (in the same module file) as in the wizard demo file using<br>
<code>class MyModuleWidget(ScriptedLoadableModuleWidget, VTKObservationMixin):...</code>,<br>
I am not able to add both widgets to the module. Both widgets would be expected to be in a accordingly named module.<br>
Thus, following the module wizard and tutorial, I am not offered the tools for creating a widget that can be reused. I think it would be great extending the demo module by a second widget (that is not a <code>ScriptedLoadableModuleWidget</code>) and which is then added to the main <code>ScriptedLoadableModuleWidget</code>. For me, as someone new to Slicer development and without experience in QT, it took quite some effort to find a way to do what I wanted.</p>
<p>You provided a lot of useful information that helped me move forward, but the essential step was using <code>qt.QWidget</code> for the widget creation which I haven’t seen directly in other modules I was looking at. This knowledge seems key to developing reusable widgets which is a core aim for the widget concept as I understand it.</p>

---

## Post #11 by @lassoan (2022-12-15 16:54 UTC)

<p>You have only one <em>module widget</em>, i.e., the widget that is shown in the left panel when you switch to the module. But you can create many widgets in Qt designer, save each in a ui file, and at runtime instantiate the widgets from the ui files and add them to the module widget.</p>
<p>Creating reusable widgets is an advanced topic, not covered by wizards or tutorials. If you are new to Qt then I would recommend to not start with creating reusable widgets, but use and customize the already existing reusable widgets provided by Qt, CTK, and Slicer.</p>
<p>It is usually not needed to create reusable widgets in Python, because scripting is just used for putting together the end-user workflow from existing components. You rarely if ever need to develop new GUI components in Python.</p>
<p>Can you write a bit about your overall task and plan to implement your solution? We could then probably provide more directly useful answers.</p>

---
