---
topic_id: 14846
title: "How To Call Simplefilters Logic In My Python Module"
date: 2020-12-02
url: https://discourse.slicer.org/t/14846
---

# How to call simpleFilters logic in my python module?

**Topic ID**: 14846
**Date**: 2020-12-02
**URL**: https://discourse.slicer.org/t/how-to-call-simplefilters-logic-in-my-python-module/14846

---

## Post #1 by @ond12 (2020-12-02 09:22 UTC)

<p>Hello everyone,</p>
<p>I would like to use the SimpleFilter logic   in my python module to start a “SigmoidImageFilter” with set parameters.</p>
<p>I looked into : <a href="https://github.com/SimpleITK/SlicerSimpleFilters/blob/master/SimpleFilters/SimpleFilters.py" rel="noopener nofollow ugc">https://github.com/SimpleITK/SlicerSimpleFilters/blob/master/SimpleFilters/SimpleFilters.py</a> to get some ideas.</p>
<p>I tried this but, it seems i can’t get the module logic and run the “sigmoidImageFilter”</p>
<p>Here is my code :</p>
<pre><code>simplefilterLogic = slicer.modules.simplefilters.logic()
filterParameters["filter"] = "SigmoidImageFilter"
filterParameters["Alpha"] = 2.0
filterParameters["Beta"] = 1.0
filterParameters["OutputMaximum"] = 230.0
filterParameters["OutputMinimum"] = 10.0

simplefilterLogic.run(  filterParameters,  inputVolume, outputVolume)      
</code></pre>
<p>Can you help me ?</p>
<p>Thanks</p>

---

## Post #2 by @mikebind (2020-12-03 00:18 UTC)

<p>Try this for getting the logic instead:</p>
<pre><code>import SimpleFilters
simpleFiltersLogic = SimpleFilters.SimpleFiltersLogic()</code></pre>

---

## Post #3 by @ond12 (2020-12-03 10:18 UTC)

<p>No i have an error : invalid syntaxe   but now the run() function is the good one !</p>
<p>the function need “*inputs” as parameter but i don’t now what is it .</p>
<pre><code>  self.logic.run(self.filterParameters.filter,
                 self.filterParameters.output,
                 self.filterParameters.outputLabelMap,
                 *self.filterParameters.inputs)
</code></pre>
<p>the last parameter i find it in the source code of the module SimpleFilters</p>

---

## Post #4 by @mikebind (2020-12-03 20:23 UTC)

<p>Yes, I see that, unfortunately I don’t have time to dig into this much further and I haven’t used the SimpleFilters module from python before.  I did get far enough to see that it looks like that filterParameters.inputs argument is a list of the filter-specific parameters performing the same function as the filterParameters dictionary you constructed above. The relevant code is in these lines (I think) <a href="https://github.com/SimpleITK/SlicerSimpleFilters/blob/fb849201697f75d114d0f2803e145fb1196df9f8/SimpleFilters/SimpleFilters.py#L585-L633" rel="noopener nofollow ugc">https://github.com/SimpleITK/SlicerSimpleFilters/blob/fb849201697f75d114d0f2803e145fb1196df9f8/SimpleFilters/SimpleFilters.py#L585-L633</a>, but I haven’t been able to sort out what exactly goes in that list (i.e. whether parameter names are included somehow or whether the values just need to be supplied in an expected order (which I’m sure would match the order in which they appear in the auto-constructed GUI for the SimpleFilters module).  I’m sure there are others on this forum who have used SimpleFilters from python who should be able to quickly give you an answer, so hopefully one of them will weigh in soon.  Sorry I couldn’t be more help!</p>

---

## Post #5 by @lassoan (2020-12-04 01:05 UTC)

<p>SimpleFilters provide a GUI to run SimpleITK. If you want to use SimpleITK filters in Python scripting then the easiest is to use SimpleITK directly. See lots of examples here: <a href="http://insightsoftwareconsortium.github.io/SimpleITK-Notebooks/">http://insightsoftwareconsortium.github.io/SimpleITK-Notebooks/</a></p>
<p>There are only two Slicer-specific SimpleITK Python functions - for moving images between SimpleITK and Slicer. See complete examples in <a href="https://github.com/Slicer/SlicerNotebooks/blob/master/03_Image_Processing_using_SimpleITK.ipynb">03_Image_Processing_using_SimpleITK notebook </a> and complete specification here:</p>
<pre><code class="lang-python">&gt;&gt;&gt; import sitkUtils

&gt;&gt;&gt; help(sitkUtils.PushVolumeToSlicer)
Help on function PushVolumeToSlicer in module sitkUtils:

PushVolumeToSlicer(sitkimage, targetNode=None, name=None, className='vtkMRMLScalarVolumeNode')
    Given a SimpleITK image, push it back to slicer for viewing
    
    :param targetNode: Target node that will store the image. If None then a new node will be created.
    :param className: if a new target node is created then this parameter determines node class. For label volumes, set it to vtkMRMLLabelMapVolumeNode.
    :param name: if a new target node is created then this parameter will be used as basis of node name.
      If an existing node is specified as targetNode then this value will not be used.

&gt;&gt;&gt; help(sitkUtils.PullVolumeFromSlicer)
Help on function PullVolumeFromSlicer in module sitkUtils:

PullVolumeFromSlicer(nodeObjectOrName)
    Given a slicer MRML image node or name, return the SimpleITK
    image object.
</code></pre>

---
