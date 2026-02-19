---
topic_id: 1477
title: "Cli Module Widget Internationalization"
date: 2017-11-17
url: https://discourse.slicer.org/t/1477
---

# CLI Module widget internationalization

**Topic ID**: 1477
**Date**: 2017-11-17
**URL**: https://discourse.slicer.org/t/cli-module-widget-internationalization/1477

---

## Post #1 by @Ted_Chen (2017-11-17 02:40 UTC)

<p>Hello,</p>
<p>We are translating the 3D slicer and the loadable module can be done well but seems there is no good explanation document about CLI module internationalization.</p>
<p>As my understanding, SlicerExecutionModel defined a xml module description to the widget creation. But is there any official way to do the widget internaltionlization ?</p>
<p>Ted</p>

---

## Post #2 by @pieper (2017-11-17 17:15 UTC)

<p>I think you would just make sure the CLI widget is internationalizable itself, and then provide translations for all the text that appears in the XML descriptions of the CLI modules.  Are there any complications with that approach?</p>

---

## Post #3 by @Ted_Chen (2017-11-20 01:08 UTC)

<p>Pieper,</p>
<p>What I mean is, Can we translate CLI module like the approach described below?</p>
<p>“We provide the translated version xml, BRAINSFit_zh_tw.xml and also keep the original BRAINSFit.xml file.  When user select his language in system setting. the 3d Slicer will auto load the corresponded translation.”</p>
<p>I have read the source code of 3d Slicer CLI loader and saw the xml description will be loaded in</p>
<p>qSlicerAbstractCoreModule* qSlicerCLIExecutableModuleFactoryItem::instanciator()</p>
<p>but cannot see the same i18n translation loading logic as loadable module. I am wondering if there exist any official dynamic i18n loading support for CLI ?</p>

---

## Post #4 by @lassoan (2017-11-20 01:41 UTC)

<p>You can try applying Qt translator to get localized string from the string specified in the xml files. It would be probably just a little change in the CLI GUI helper class.</p>

---

## Post #5 by @Ted_Chen (2017-11-20 02:55 UTC)

<p>Andras,</p>
<p>I cannot undertand exactly,  I have tried lupdate to extract BRAINSFit module and got nothing, meanwhile the QT linguist doesn’t support the BRAINSFit.xml translation either.</p>
<p>My thought is to implement the dynamic xml loading myself(load BRAINSFit_zh_tw.xml or BRAINSFit_fr.xml corresponding current ui language setting), but don’t know if it’s a correct way or there is any official CLI i18n suppport i don’t know?</p>

---

## Post #6 by @Ted_Chen (2017-11-20 03:00 UTC)

<p>The translation i mentioned is as below (some real codes in BRAINSFit.xml), and my current understand is slicer will parse out the description “Transform Initialization Settings” in xml and generated the widget. I want to translate generated widget.</p>
<pre><code>&lt;parameters&gt;
    &lt;label&gt;Transform Initialization Settings&lt;/label&gt;
    &lt;description&gt;Options for initializing transform parameters.&lt;/description&gt;
    &lt;transform fileExtensions=".h5,.hdf5,.mat,.txt"&gt;
      &lt;name&gt;initialTransform&lt;/name&gt;
      &lt;longflag&gt;initialTransform&lt;/longflag&gt;
      &lt;label&gt;Initialization transform&lt;/label&gt;
      &lt;description&gt;Transform to be applied to the moving image to initialize the registration.  This can only be used if Initialize Transform Mode is Off.&lt;/description&gt;
      &lt;channel&gt;input&lt;/channel&gt;
    &lt;/transform&gt;
    &lt;string-enumeration&gt;
      &lt;name&gt;initializeTransformMode&lt;/name&gt;
      &lt;longflag&gt;initializeTransformMode&lt;/longflag&gt;
      &lt;label&gt;Initialize Transform Mode&lt;/label&gt;
      &lt;description&gt;Determine how to initialize the transform center.  useMomentsAlign assumes that the center of mass of the images represent similar structures.  useCenterOfHeadAlign attempts to use the top of head and shape of neck to drive a center of mass estimate. useGeometryAlign on assumes that the center of the voxel lattice of the images represent similar structures.  Off assumes that the physical space of the images are close.  This flag is mutually exclusive with the Initialization transform.&lt;/description&gt;
      &lt;default&gt;Off&lt;/default&gt;
      &lt;element&gt;Off&lt;/element&gt;
      &lt;element&gt;useMomentsAlign&lt;/element&gt;
      &lt;element&gt;useCenterOfHeadAlign&lt;/element&gt;
      &lt;element&gt;useGeometryAlign&lt;/element&gt;
      &lt;element&gt;useCenterOfROIAlign&lt;/element&gt;
    &lt;/string-enumeration&gt;
  &lt;/parameters&gt;</code></pre>

---

## Post #7 by @lassoan (2017-11-20 04:32 UTC)

<p>There could be many internationalization solutions, but the approach I think would be the simplest:</p>
<ul>
<li>do <em>not</em> translate any CLI module descriptor XML files</li>
<li>update qSlicerCLIModuleUIHelper.cxx to translate strings that are retrieved from CLI module descriptor XML  files before setting them in a widget</li>
<li>provide translations for strings in the CLI module descriptor XML files (Qt linguist will not collect text from CLI XML files but if you provide translation then they will be applied)</li>
</ul>
<p>For example, to translate a parameter’s tooltip, change this line:</p>
<pre><code>QString description = QString::fromStdString(moduleParameter.GetDescription());
</code></pre>
<p>to this:</p>
<pre><code>QString description = tr(moduleParameter.GetDescription().c_str());</code></pre>

---

## Post #8 by @Ted_Chen (2017-11-21 01:12 UTC)

<p>Ah, I finally understand what you all mean.</p>
<p>I will think about it in advance… seems this approach will pollute the translated vocabulary space, especially when some same phrases may have to be translated into diff semantic translations.</p>

---

## Post #9 by @lassoan (2017-11-21 01:51 UTC)

<p>To translate each CLI module independently, you can use <code>QCoreApplication::translate</code> method and use the CLI module name as translation context.</p>

---

## Post #10 by @Ted_Chen (2017-11-21 01:59 UTC)

<p>Andras,</p>
<p>I will give it a shot and thanks for your clear explanation.</p>

---

## Post #11 by @lassoan (2017-11-21 02:16 UTC)

<p>Let us know if you find a solution that works. Also, we are happy to integrate pull requests that help internationalization.</p>

---
