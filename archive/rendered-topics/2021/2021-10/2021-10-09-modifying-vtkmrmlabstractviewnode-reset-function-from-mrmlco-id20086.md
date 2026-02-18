# Modifying `vtkMRMLAbstractViewNode::Reset(...)` function from MRMLCore

**Topic ID**: 20086
**Date**: 2021-10-09
**URL**: https://discourse.slicer.org/t/modifying-vtkmrmlabstractviewnode-reset-function-from-mrmlcore/20086

---

## Post #1 by @keri (2021-10-09 23:22 UTC)

<p>Hi,</p>
<p>Here is the implementation of <code>vtkMRMLAbstractViewNode::Reset(...)</code> function:</p>
<pre><code class="lang-cpp">void vtkMRMLAbstractViewNode::Reset(vtkMRMLNode* defaultNode)
{
  // The LayoutName is preserved by vtkMRMLNode::Reset, however the layout
  // label (typically associated with the layoutName) is not preserved
  // automatically.
  // This require a custom behavior implemented here.
  std::string layoutLabel = this-&gt;GetLayoutLabel() ? this-&gt;GetLayoutLabel() : "";
  int viewGroup = this-&gt;GetViewGroup();
  this-&gt;Superclass::Reset(defaultNode);
  this-&gt;DisableModifiedEventOn();
  this-&gt;SetLayoutLabel(layoutLabel.c_str());
  this-&gt;SetViewGroup(viewGroup);
  this-&gt;AxisLabels-&gt;Reset();
  for (int i=0; i&lt;vtkMRMLAbstractViewNode::AxisLabelsCount; i++)
    {
    this-&gt;AxisLabels-&gt;InsertNextValue(DEFAULT_AXIS_LABELS[i]);
    }
  this-&gt;DisableModifiedEventOff();
}
</code></pre>
<p>Why <code>this-&gt;AxisLabels</code> are set to some default medical values instead of copying them from the <code>defaultNode</code> node?</p>
<p>For custom application that works with axis labels <code>XYZ</code> for example this function brings a lot of problems as after calling <code>Reset(...)</code> axes labels will be changed to medical values <code>APSI etc</code> no matter what labels the <code>defaultNode</code> have.</p>
<p>Probably it is better to cast the <code>defaultNode</code> to <code>vtkMRMLAbstractViewNode</code> and if casting returns non <code>NULL</code> pointer then use <code>GetAxisLabel()</code> to set axes labels and if not then use the default medical values?</p>
<p>For example for now <code>ViewControllers</code> module uses the <code>Reset()</code> function and it thus I can’t use it in my custom app without some tricks that I do.</p>

---

## Post #2 by @keri (2021-10-09 23:55 UTC)

<p>Maybe modify it this way:</p>
<pre><code class="lang-cpp">void vtkMRMLAbstractViewNode::Reset(vtkMRMLNode* defaultNode)
{
  // The LayoutName is preserved by vtkMRMLNode::Reset, however the layout
  // label (typically associated with the layoutName) is not preserved
  // automatically.
  // This require a custom behavior implemented here.
  std::string layoutLabel = this-&gt;GetLayoutLabel() ? this-&gt;GetLayoutLabel() : "";
  int viewGroup = this-&gt;GetViewGroup();
  this-&gt;Superclass::Reset(defaultNode);
  this-&gt;DisableModifiedEventOn();
  this-&gt;SetLayoutLabel(layoutLabel.c_str());
  this-&gt;SetViewGroup(viewGroup);
  this-&gt;AxisLabels-&gt;Reset();
  vtkMRMLAbstractViewNode* defaultViewNode = vtkMRMLAbstractViewNode::SafeDownCast(defaultNode);
  if (defaultViewNode){
    for (int i=0; i&lt;vtkMRMLAbstractViewNode::AxisLabelsCount; i++)
    {
      this-&gt;AxisLabels-&gt;InsertNextValue(defaultViewNode-&gt;GetAxisLabel(i));
    }
  } else {
  for (int i=0; i&lt;vtkMRMLAbstractViewNode::AxisLabelsCount; i++)
    {
    this-&gt;AxisLabels-&gt;InsertNextValue(DEFAULT_AXIS_LABELS[i]);
    }
  }
  this-&gt;DisableModifiedEventOff();
}
</code></pre>

---

## Post #3 by @lassoan (2021-10-10 12:28 UTC)

<p>I don’t see why this additional resetting of the axis labels would be needed (node reset and copy from the default node should take care of this). Would removing AxisLabels Reset and InsertNextValue calls fix the behavior?</p>

---

## Post #4 by @keri (2021-10-10 15:39 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="20086">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Would removing AxisLabels Reset and InsertNextValue calls fix the behavior?</p>
</blockquote>
</aside>
<p>Yes that would be enough. I just tested that while relying on <code>ViewControllers</code> module and by enabling/disabling this module (i.e. enabling disabling <code>Reset(defaultNode)</code>) I can say that if you change the code as you proposed (by removing everything connected with <code>AxisLabels</code> var) axes labels will be copied from the default node.</p>
<p><strong>Related question:</strong></p>
<p>There is one thing I’m not sure about yet is <code>void vtkMRMLNode::Reset(vtkMRMLNode* defaultNode)</code> calls <code>CopyWithScene</code> and the latter calls <code>Copy</code> and it calls <code>CopyContent</code>. Here it is:</p>
<pre data-code-wrap="cpp"><code class="lang-cpp">void vtkMRMLNode::CopyContent(vtkMRMLNode* node, bool vtkNotUsed(deepCopy)/*=true*/)
{
  MRMLNodeModifyBlocker blocker(this);
  vtkMRMLCopyBeginMacro(node);
  vtkMRMLCopyStringMacro(Description);
  vtkMRMLCopyBooleanMacro(Selectable);
  vtkMRMLCopyEndMacro();
  this-&gt;Attributes = node-&gt;Attributes;
}
</code></pre>
<p><code>CopyContent</code> uses some macros that I can’t understand now but these macros somehow adds medical orientation presets to my default <code>XY, YZ, XZ</code>. I removed medical orientation presets (<code>Sagittal, Axial, Coronal</code>) from all already created slice nodes and from the default nodes but when <code>ViewControllers</code> is enabled the mentionned above macros adds those medical presets.<br>
Maybe I do something wrong but if you have something to say (maybe some key words about these macros) I would appreciate:</p>
<pre data-code-wrap="cpp"><code class="lang-cpp">  std::vector&lt;std::string&gt; axesNames({"X", "-X", "-Y", "Y", "-Z", "Z"});
  std::vector&lt;std::string&gt; orientationPresetOld({"Axial", "Sagittal", "Coronal"});
  std::vector&lt;std::string&gt; orientationPresetNew({"XY", "YZ", "XZ"});
  std::vector&lt;std::string&gt; defaultOrientation({"XY", "YZ", "XZ"});

  for (size_t i = 0; i &lt; orientationPresetOld.size(); i++){
    if (defaultSliceNode-&gt;HasSliceOrientationPreset(orientationPresetOld[i])){
      defaultSliceNode-&gt;RemoveSliceOrientationPreset(
            orientationPresetOld[i]);
    }

    if (!defaultSliceNode-&gt;HasSliceOrientationPreset(orientationPresetNew[i])){
      defaultSliceNode-&gt;AddSliceOrientationPreset(
            orientationPresetNew[i],
            GenerateOrientationMatrix(orientationPresetNew[i]));
      defaultSliceNode-&gt;SetDefaultOrientation(defaultOrientation[i].c_str());
    }
  }
</code></pre>
<p>On the picture you can see that vtk macros from <code>CopyContent</code> add medical presets:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94dada94010dfc0569e7681046fec2f0de68a72d.png" alt="image" data-base62-sha1="lePyA5r4lAH1WeAMd0Kbs4n6uqF" width="433" height="287"></p>

---

## Post #5 by @lassoan (2021-10-10 17:01 UTC)

<p>You can update the slice node reset and copy methods to initialize the orientation presets from the default slice node.</p>
<p>The default orientation name for each slice view is specified in the view layout description. Therefore, if you change the orientation preset names then you may need to update the layout descriptions, too.</p>

---

## Post #6 by @lassoan (2021-10-11 00:02 UTC)

<p>When you are done with these changes then please submit them in a pull request so that we can review and merge them into Slicer core.</p>

---

## Post #7 by @keri (2021-10-11 01:07 UTC)

<p>From Slicer Astro I have found an example how to modify <code>vtkMRMLLayoutNode</code> description and I applied it to my case but still I can see the default slicer <code>Axial</code> <code>Sagittal</code> and <code>Coronal</code> presets:</p>
<pre><code class="lang-cpp">  vtkMRMLLayoutNode* layoutNode =  vtkMRMLLayoutNode::SafeDownCast(
    this-&gt;LayoutManager-&gt;mrmlScene()-&gt;GetSingletonNode("vtkMRMLLayoutNode","vtkMRMLLayoutNode"));
  if(!layoutNode)
    {
    qCritical() &lt;&lt; "qSlicerAstroVolumeModule::setup() : layoutNode not found!";
    return;
    }

  for(int i = 1 ; i &lt; 36; i++)
    {
    if (i == 5 || i == 11 || i == 13 || i == 18 || i == 20)
      {
      continue;
      }

    std::string layoutDescription = layoutNode-&gt;GetLayoutDescription(i);
    std::vector&lt;std::string&gt;::const_iterator it;
    std::vector&lt;std::string&gt;::const_iterator jt;
    for(it = orientationPresetOld.begin(), jt = orientationPresetNew.begin();
        it != orientationPresetOld.end() &amp;&amp; jt != orientationPresetNew.end(); ++it, ++jt)
      {
      size_t found = layoutDescription.find(*it);
      while (found!=std::string::npos)
        {
        layoutDescription.replace(found, it-&gt;size(), *jt);
        found = layoutDescription.find(*it);
        }
      }
    layoutNode-&gt;SetLayoutDescription(i, layoutDescription.c_str());
    }
</code></pre>
<p>I don’t understand yet some things especially how node’s description influences on app behaviour and why Slicer’s astro authors use numbers like 36, 5, 11, 13, 18, 20 in this code…</p>
<p>If possible please take a look at <a href="https://github.com/tierra-colada/Colada/blob/1a91d0d2d6c3b8627a29e82ff069d26103a305e9/Applications/ColadaApp/qColadaAppMainWindow.cxx#L187-L296" rel="noopener nofollow ugc">dirty source code</a></p>

---

## Post #8 by @lassoan (2021-10-11 04:55 UTC)

<p>I had a look at orientation presets, and it all looks good. Orientation presets are already stored in the deafult slice node, initialized by <code>AddDefaultSliceOrientationPresets</code>. If you want to change the defaults just make sure you update the defaults after <code>AddDefaultSliceOrientationPresets</code> method is called and before you add your new presets, clear the old ones.</p>
<aside class="quote no-group" data-username="keri" data-post="7" data-topic="20086">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>I don’t understand yet some things especially how node’s description influences on app behaviour and why Slicer’s astro authors use numbers like 36, 5, 11, 13, 18, 20 in this code…</p>
</blockquote>
</aside>
<p>As you can see <code>i</code> refers to layout indices. Instead of 5, 11, etc. the developer should have written <code>SlicerLayoutOneUpSliceView</code>, <code>SlicerLayoutLightboxView</code>, etc. (see <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLLayoutNode.h#L88-L130">complete list</a>).</p>

---

## Post #9 by @keri (2021-10-11 14:14 UTC)

<p>Thank you for reply,</p>
<p>I took a look at <code>AddDefaultSliceOrientationPresets</code> implementation and the idea pretty clear and now I understand why I need to overwrite presets after this function is called.</p>
<p>From the IDE I can find all references to <code>AddDefaultSliceOrientationPresets</code> and only <a href="https://github.com/Slicer/Slicer/blob/03e913587bf7b78990f0224bc77818e3ed31d5d3/Modules/Loadable/ViewControllers/qSlicerViewControllersModule.cxx#L205-L221" rel="noopener nofollow ugc">qSlicerViewControllersModule.cxx</a> references to that function. I tried to comment these lines and rebuilt the target but still <code>Reset(...)</code> function adds medical orientation presets.</p>

---

## Post #10 by @lassoan (2021-10-11 14:29 UTC)

<p>You can add a breakpoint in <code>AddDefaultSliceOrientationPresets</code> to see what calls it.</p>

---

## Post #11 by @keri (2021-10-11 15:24 UTC)

<p>You were right, it was my carelessness: I commented <code>AddDefaultSliceOrientationPresets</code> from <code>qSlicerViewControllersModule.cxx</code> but I used to rebuild the <code>...Logic</code> target instead of <code>...Module</code> target. There is no any problem if I comment the section with <code>AddDefaultSliceOrientationPresets</code> from that module and the rebuild the correct target.</p>
<p><strong>Proposition:</strong><br>
Does <code>ViewControllers</code> module really need to add orientation presets and make other settings with <code>defaultViewNode</code>? That makes this module difficult to use in custom application.</p>
<p>I think the main purpose of this module is to use controller widgets from module tab and if so then this module can be useful not only in medical software.</p>
<p>I propose to modify this module (if possible of course, I haven’t precisely looked at its implementation yet) in a way that it won’t do any settings with default nodes.</p>

---

## Post #12 by @lassoan (2021-10-11 19:11 UTC)

<p>Default view presets need to be set <em>somewhere</em>. The View Controllers module seems to be a reasonable place for that. Where else would you put it?</p>
<p>Note that the preset is already customizable without any Slicer core code change, but if you have a preferred way of making it simpler then let us know. For example the View Controllers module could have a flag to control its behavior or could emit a signal after setting the defaults so that other modules can override those, or default orientation presets could be read from the application settings, etc.</p>

---

## Post #13 by @keri (2021-10-11 20:32 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="20086">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Default view presets need to be set <em>somewhere</em> . The View Controllers module seems to be a reasonable place for that. Where else would you put it?</p>
</blockquote>
</aside>
<p>I agree that presets should be set somwhere but in my opinion they should be set somwhere in medical module.<br>
It is very difficult to guess that module named <code>ViewControllers</code> and that is aimed at some widget manipulation brings some medical staff to SlicerCAT.<br>
To figure that out I started launching SlicerCAT with disabled modules. The first module to disable was <code>Endoscopy</code> (though I don’t know how I included it to app) because it is very obvious to think that medical modules makes medical changes and I was very surprised when I discovered that at <code>ViewControllers</code> <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>I’m not familiar with most medical modules that Slicer uses but I think such things should be implemented there (I can’t tell where exactly). Or probably make some GUI-less module where one does especially medical customization like manipulation with presets. Then those developers who work on SlicerCAT could disable this module and create his own (though I couldn’t do GUI-less module that is completely hidden yet but believe that is possible, I remember I created topic on that on this forum).</p>
<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="20086">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>For example the View Controllers module could have a flag to control its behavior or could emit a signal after setting the defaults so that other modules can override those, or default orientation presets could be read from the application settings, etc.</p>
</blockquote>
</aside>
<p>I think this would bring some complexity for developers. Slicer already has well structured philosophy with scene, views, slices, nodes, modules, superbuild etc and I think adding signals to <em>control such things</em> is like using insulating tape to weld metall.</p>
<p>The only solution I can see is to try to keep medical staff in medical modules.</p>
<p>P.S.<br>
Sometimes I need to make changes in Slicer core that is not appropriate for medical goals (like <a href="https://discourse.slicer.org/t/resizing-slice-view-doesnt-preserve-field-of-view/19636">resizing slice view while preserving field of view or aspect ratio</a>) and for this I use <a href="https://github.com/tierra-colada/cppguts" rel="noopener nofollow ugc">cpp tool</a> or <a href="https://github.com/tierra-colada/pythonguts" rel="noopener nofollow ugc">python tool</a> that replaces selected function implementation during build time and thus allowing to use it in superbuild. Of course I’m trying to make core changes as less as possible</p>

---

## Post #14 by @lassoan (2021-10-11 21:30 UTC)

<aside class="quote no-group" data-username="keri" data-post="13" data-topic="20086">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>The first module to disable was <code>Endoscopy</code> (though I don’t know how I included it to app) because it is very obvious to think that medical modules makes medical changes</p>
</blockquote>
</aside>
<p>This is not a medical module at all. Endoscopy just means that you visualize from inside. It is used commonly in medical imaging but just as well for inspection of pipelines, tunnels, etc.</p>
<aside class="quote no-group" data-username="keri" data-post="13" data-topic="20086">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>I agree that presets should be set somwhere but in my opinion they should be set somwhere in medical module.</p>
</blockquote>
</aside>
<p>While more than 99.9% of Slicer development has been funded for medical applications, nothing is hardcoded in Slicer for medical applications and there is no module that would only be applicable to medical imaging - all modules can be used for various industrial, engineering, etc. applications. Of course defaults must be set to something, and since medical imaging is the primary application area, the defaults are set accordingly. This should not be an issue, as Slicer core developers are willing to make things more generic and configurable, even if that means slightly increasing complexity.</p>
<aside class="quote no-group" data-username="keri" data-post="13" data-topic="20086">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>I think adding signals to <em>control such things</em> is like using insulating tape to weld metall.</p>
</blockquote>
</aside>
<p>Things that would be considered as workarounds in Slicer core are completely acceptable, good solutions in custom applications. For example, in a custom application you will know that no other modules will change the view preset names, so changing the default in response to a signal would be completely fine, nice and clear solution. However, if you don’t like this then you can propose a change in Slicer core to read default view presets from the application settings.</p>
<aside class="quote no-group" data-username="keri" data-post="13" data-topic="20086">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>Sometimes I need to make changes in Slicer core that is not appropriate for medical goals</p>
</blockquote>
</aside>
<p>In general, source code changes are probably the best done using git, because all code changes are automatically synchronized (or you are prompted to resolve conflicts manually) whenever you rebase your Slicer core version. It is much simpler and more robust compared to patching files.</p>
<p>Of course these should only be used temporarily, while you are validating some ideas and once things are mature then you get them merged into the Slicer core (or make Slicer core configurable so that you can inject your custom behavior).</p>

---

## Post #15 by @keri (2021-10-11 22:40 UTC)

<p>Thank you for the information, I’m slightly ashamed about not knowing about Endoscopy module <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p><strong>About ViewControllers:</strong><br>
The default presets are lodaded in file <code>vtkMRMLApplicationLogic.cxx</code> in function <code>void vtkMRMLApplicationLogic::SetMRMLSceneInternal(vtkMRMLScene* newScene)</code>.<br>
As I see <code>void qSlicerViewControllersModule::readDefaultSliceViewSettings(vtkMRMLSliceNode* defaultViewNode)</code> handles <code>PatientRightIsScreenLeft</code> and <code>PatientRightIsScreenRight</code>.<br>
I thought that we could added property like <code>IsAxesMedical</code> to default node and display it as a checkbox in <code>Edit-&gt;Application Settings-&gt;Views</code> and if this checkbox is uncheked then <code>View orientation</code> combobox should be greyed out and <code>ViewController</code> don’t have to do any manipulations with orientation presets. How do you think?</p>
<p><strong>EDIT:</strong><br>
I just remembered that you already proposed to set default preset from application properties - Yes that I also like.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/814688a8b27cb12bf7be66a0ad9ebbd754073f90.png" data-download-href="/uploads/short-url/irCI7OdtlmGJRD2YPPPfPwfDo0U.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/814688a8b27cb12bf7be66a0ad9ebbd754073f90_2_690x132.png" alt="image" data-base62-sha1="irCI7OdtlmGJRD2YPPPfPwfDo0U" width="690" height="132" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/814688a8b27cb12bf7be66a0ad9ebbd754073f90_2_690x132.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/814688a8b27cb12bf7be66a0ad9ebbd754073f90.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/814688a8b27cb12bf7be66a0ad9ebbd754073f90.png 2x" data-dominant-color="C9CBCB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">842×162 55.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>About signal in this case:</strong><br>
If emitting signal directly from <code>vtkMRMLSliceNode::AddDefaultSliceOrientationPresets(newScene)</code> was possible I would like to do that. But instead of emitting it from <code>ViewControllers</code> I would prefer the method proposed in the upper paragraph with attribute.</p>

---
