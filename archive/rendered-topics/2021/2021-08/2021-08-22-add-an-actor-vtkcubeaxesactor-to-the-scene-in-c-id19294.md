# Add an actor (vtkCubeAxesActor) to the scene in C++

**Topic ID**: 19294
**Date**: 2021-08-22
**URL**: https://discourse.slicer.org/t/add-an-actor-vtkcubeaxesactor-to-the-scene-in-c/19294

---

## Post #1 by @keri (2021-08-22 00:28 UTC)

<p>Hi,</p>
<p>I have some understanding how to add <code>vtkObject</code> inherited objects as described <a href="https://slicer.readthedocs.io/en/latest/developer_guide/mrml_overview.html#mrml-nodes" rel="noopener nofollow ugc">here</a> via MRML nodes but I can’t find a way to add <a href="https://kitware.github.io/vtk-examples/site/Cxx/Visualization/CubeAxesActor/" rel="noopener nofollow ugc">vtkCubeAxesActor</a> (and in general <code>vtkActor</code>).</p>
<p>Though I have found some information on that in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#access-vtk-actor-properties" rel="noopener nofollow ugc">script repository</a> but when I by analogy do:</p>
<pre><code class="lang-cpp">  vtkMRMLAbstractDisplayableManager* modelDisplayableManager =
      LayoutManager-&gt;threeDWidget(0)
          -&gt;threeDView()
          -&gt;displayableManagerByClassName("vtkMRMLModelDisplayableManager");
</code></pre>
<p>I cannot somehow cast <code>vtkMRMLAbstractDisplayableManager</code> to <code>vtkMRMLModelDisplayableManager</code> as there is no <code>vtkMRMLModelDisplayableManager.h</code> header (neither there is <code>vtkMRMLAbstractDisplayableManager.h</code>).</p>

---

## Post #2 by @lassoan (2021-08-22 04:35 UTC)

<p>Slicer uses <code>vtkMRML...DisplayableManager</code> classes to create actors and add them to renderers. So, if you want to add actors that none of the existing displayable managers support then you need to add your own displayable manager and you may also add MRML classew (to store data and display options in the scene).</p>
<p>What would you like to use a cube axis actor for? If you just want to display orientation then you can enable orientation marker display, which can use a box or arrows axis actor or an arbitrary 3D model (by default a human body). You can specify the style and size and customize the axis letters in the view node.</p>

---

## Post #3 by @keri (2021-08-22 11:57 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="19294">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What would you like to use a cube axis actor for? If you just want to display orientation then you can enable orientation marker display, which can use a box or arrows axis actor or an arbitrary 3D model (by default a human body). You can specify the style and size and customize the axis letters in the view node.</p>
</blockquote>
</aside>
<p>I wanted to display coordinates in 3d view. Not only the directions (wich is good by the way) but also XYZ values, like scales. I work in geographic coordinates so I would like to check correctness of my code. Usually the main object should be <code>vtkImageData</code> and display scales around it would be fine. Probably there are another options to achieve my goal?</p>
<p>If I create <code>vtkMRMLCubeAxesActorDisplayableManager</code> (I guess I would need to inherit from some base class) and create a button on 3d view toolbar that shows/hides <code>vtkCubeAxesActor</code> around chosen object would that be enough? Or the task is more difficult than I think?</p>

---

## Post #4 by @keri (2021-08-22 15:11 UTC)

<p>With the <a href="https://discourse.slicer.org/t/independent-zoom-along-different-axes/19263/14">recent knowlegde about vtkCubeAxesActor transform problem</a> I still want to have something like visualized coordinate system in 3D view but now I’m not much sticked to the <code>vtkCubeAxesActor</code>. Probably there are some options to achieve the goal without using <code>vtkCubeAxesActor</code>?<br>
Maybe I could create 8 points at <code>vtkImageData</code>'s corners and display coordinates only at these points…</p>
<p>Also is it ok that if I add <code>vtkCubeAxesActor</code> then the interaction perfomance noticeably decreases? Any movements becomes much slower</p>

---

## Post #5 by @keri (2021-08-24 01:07 UTC)

<p>I’m getting known with <code>DisplayableManager</code>.<br>
From SlicerAstro I took <code>vtkMRMLAstroTwoDAxesDisplayableManager</code> as an example and simplified it.<br>
According to the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/DisplayableManagers" rel="noopener nofollow ugc">documentation</a>  and SlicerAstro too I need to register my disp manager:</p>
<pre><code class="lang-cpp">void qSlicerStackLoadModule::setup()
{
  this-&gt;Superclass::setup();
  ...
  vtkMRMLSliceViewDisplayableManagerFactory::GetInstance()-&gt;
    RegisterDisplayableManager("vtkMRMLColadaCubeAxesDisplayableManager");
}
</code></pre>
<p>But I noticed that generated <code>vtkSlicerStackLoadModuleMRMLDisplayableManagerObjectFactory.cxx</code> does some checks and the debugging helped me to understand that <code>bool vtkMRMLDisplayableManagerGroup::IsADisplayableManager(const char* displayableManagerName)</code> returns false:</p>
<pre><code class="lang-cpp">bool vtkMRMLDisplayableManagerGroup
::IsADisplayableManager(const char* displayableManagerName)
{
  // Check if displayableManagerName is a valid displayable manager
  vtkSmartPointer&lt;vtkObject&gt; objectSmartPointer;
  objectSmartPointer.TakeReference(vtkObjectFactory::CreateInstance(displayableManagerName));
  if (objectSmartPointer.GetPointer() &amp;&amp;
      objectSmartPointer-&gt;IsA("vtkMRMLAbstractDisplayableManager"))
    {
    return true;    // the execution can't reach there as `objectSmartPointer` is NULL
    }
#ifdef VTK_DEBUG_LEAKS
  vtkDebugLeaks::DestructClass(displayableManagerName);
#endif
#ifdef MRMLDisplayableManager_USE_PYTHON
  // Check if vtkClassOrScriptName is a python script
  if (std::string(displayableManagerName).find(".py") != std::string::npos)
    {
    // TODO Make sure the file exists ...
    return true;
    }
#endif
  return false;
}
</code></pre>
<p>The var <code>displayableManagerName</code> is <code>vtkMRMLColadaCubeAxesDisplayableManager</code>.<br>
It seems that I my disp manager doesn’t follow some conditions of a disp manager but I don’t understand what are these conditions…</p>
<p>It is late night and tomorrow I will try to investigate the problem more precisely. But probably you have experience and already know where to look…</p>
<p>Here is the header file of my disp manager:</p>
<pre><code class="lang-cpp">#ifndef __vtkMRMLColadaCubeAxesDisplayableManager_h
#define __vtkMRMLColadaCubeAxesDisplayableManager_h

// MRMLDisplayableManager includes
#include "vtkMRMLAbstractDisplayableManager.h"
#include &lt;vtkSlicerStackLoadModuleMRMLDisplayableManagerExport.h&gt;

// Qt declaration
class QColor;

/// \brief Displayable manager that displays 2D WCS axes in 2D view
class VTK_MRMLDISPLAYABLEMANAGER_COLADA_EXPORT vtkMRMLColadaCubeAxesDisplayableManager
  : public vtkMRMLAbstractDisplayableManager
{
  friend class vtkColadaCubeAxesRendererUpdateObserver;

public:
  static vtkMRMLColadaCubeAxesDisplayableManager* New();
  vtkTypeMacro(vtkMRMLColadaCubeAxesDisplayableManager,vtkMRMLAbstractDisplayableManager);
  void PrintSelf(ostream&amp; os, vtkIndent indent) override;

  /// Get vtkMarkerRenderer
  vtkRenderer* vtkMarkerRenderer();

  /// Set annotation color
  void SetAnnotationsColor(double red,
                           double green,
                           double blue);

  /// Set font style
  void SetAnnotationsFontStyle(const char* font);

  /// Set font size
  void SetAnnotationsFontSize(int size);

protected:

  vtkMRMLColadaCubeAxesDisplayableManager();
  virtual ~vtkMRMLColadaCubeAxesDisplayableManager();

  /// Observe the View node and initialize the renderer accordingly.
  virtual void Create() override;

  /// Called each time the view node is modified.
  /// Internally update the renderer from the view node
  /// \sa UpdateFromMRMLViewNode()
  virtual void OnMRMLDisplayableNodeModifiedEvent(vtkObject* caller) override;

  /// Update the renderer from the view node properties.
  void UpdateFromViewNode();

  /// Update the renderer based on the master renderer (the one that the orientation marker follows)
  void UpdateFromRenderer();

private:

  vtkMRMLColadaCubeAxesDisplayableManager(const vtkMRMLColadaCubeAxesDisplayableManager&amp;);// Not implemented
  void operator=(const vtkMRMLColadaCubeAxesDisplayableManager&amp;); // Not Implemented

  class vtkInternal;
  vtkInternal * Internal;
};

#endif
</code></pre>

---

## Post #6 by @keri (2021-08-24 13:35 UTC)

<p>I have found the problem.<br>
When VTK iterates over the factories (in <code>vtkObject* vtkObjectFactory::CreateInstance(const char* vtkclassname, bool)</code>), none of them is able to create instance of <code>vtkMRMLColadaCubeAxesDisplayableManager</code>.</p>
<p>The solution I have not found yet…</p>

---

## Post #7 by @keri (2021-08-24 18:25 UTC)

<p>I noticed that <code>vtkSlicerStackLoadModuleMRMLDisplayableManagerObjectFactory</code> object factory is not registered even I use <code>SlicerConfigureDisplayableManagerObjectFactory(...)</code> cmake macro and there is <code>vtkSlicerStackLoadModuleMRMLDisplayableManagerObjectFactory.h</code> and <code>vtkSlicerStackLoadModuleMRMLDisplayableManagerObjectFactory.cxx</code> generated files in build dir.</p>

---

## Post #8 by @keri (2021-08-25 12:59 UTC)

<p>Finally I have found my drawback. I should have been put these two lines of code:</p>
<pre><code class="lang-cpp">// DisplayableManager initialization
#include &lt;vtkAutoInit.h&gt;
VTK_MODULE_INIT(vtkSlicerStackLoadModuleMRMLDisplayableManager)
</code></pre>
<p>to the <code>qSlicer${MODULE_NAME}Module.cxx</code>.<br>
Now both <code>...DisplayableManagerObjectFactory</code> and <code>...DisplayableManager</code> are registered.</p>
<p><strong>As a summary to register <code>DisplayableManager</code> I needed:</strong></p>
<ul>
<li>copy <code>MRMLDM</code> folder from any built-in Slicer module (I used <code>Transforms</code> module) to my module and customize <code>CMakeLists.txt</code> (and of course customize <code>.cxx</code> and <code>.h</code> files);</li>
<li>add this MRMLDM target to <code>MODULE_TARGET_LIBRARIES</code> of the main module <code>CMakeLists.txt</code>;</li>
</ul>
<p>and in <code>qSlicer...Module.cxx</code>:</p>
<ul>
<li>
<span class="hashtag">#include</span> “vtkMRMLSliceViewDisplayableManagerFactory.h”    // for registering Disp Manager in SliceView</li>
<li>
<span class="hashtag">#include</span> “vtkMRMLThreeDViewDisplayableManagerFactory.h”    // for registering Disp Manager in Three D view</li>
<li>
<span class="hashtag">#include</span> &lt;vtkAutoInit.h&gt;</li>
<li>VTK_MODULE_INIT(…DisplayableManager)    // without this the <code>...ObjectFactory</code> won’t be registered</li>
</ul>
<p>in <code>setup()</code> method:</p>
<ul>
<li>bool val = vtkMRMLThreeDViewDisplayableManagerFactory::GetInstance()-&gt;RegisterDisplayableManager("…DisplayableManager");</li>
</ul>

---

## Post #9 by @lassoan (2021-08-25 15:18 UTC)

<p>Thank you for sharing your progress and solution. In general, it is a good idea to clone an existing working module or component and modify it.</p>
<p>VTK9’s build system became really complicated, so you need to do “magic” things like these VTK_MODULE_INIT macros (magic = more complicated than most people, including myself, would want to spend time with to understand).</p>

---

## Post #10 by @keri (2021-08-28 01:13 UTC)

<p>I need now to get current node (the last node the user interacted with and that is displayed) and create around it <code>vtkCubeAxesActor</code>. Thus I need to retrieve bounds from the node.</p>
<p>To achieve that I think I could do something like (in class inherited from <code>vtkMRMLAbstractThreeDViewDisplayableManager</code>):</p>
<pre><code class="lang-cpp">  vtkMRMLVolumeNode* volumeNode = vtkMRMLVolumeNode::SafeDownCast(GetSelectionNode());  // this gives me an error 
  if (!volumeNode)
    return;
  
  double bounds[6];
  volumeNode-&gt;GetBounds(bounds);
</code></pre>
<p>but I get the error when I’m trying to downcast:</p>
<p><code>error: C2440: 'initializing': cannot convert from 'vtkObject *' to 'T *' with [T=vtkMRMLVolumeNode]</code></p>
<p>I have looked to other modules and it seems they do almost exactly the same for example in<br>
<code>Slicer\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx</code><br>
line 503<br>
<code>vtkMRMLVolumeNode* volumeNode = vtkMRMLVolumeNode::SafeDownCast(     displayNode-&gt;GetDisplayableNode());</code>.</p>

---

## Post #11 by @keri (2021-10-14 15:23 UTC)

<p>Hi,</p>
<p>Is there any difference of developping custom node that adds some <code>vtkActor</code> (<code>vtkCubeAxesActor</code>) to the scene  and node that adds objects like volume, polydata, lines, points etc…?</p>
<p>As I know <code>vtkActor</code> should be added directly to renderer, would <code>Scene-&gt;addNode(actorNode)</code> work properly in this case?</p>

---

## Post #12 by @lassoan (2021-10-17 21:18 UTC)

<p>To add an actor to the renderer, you need to create a new displayable manager class. Responsibility of this class is to observe the MRML scene and add actors to the renderer accordingly. Usually it adds one actor per display node. You register the new displayable manager class in the the displayable manager factory so that the layout manager can add it to each created view.</p>

---

## Post #13 by @keri (2021-10-17 21:54 UTC)

<p>Thank you, this is the way how I implemented it. It works.</p>

---
