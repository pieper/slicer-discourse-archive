# Accessing SlicerElastix from within python module

**Topic ID**: 9410
**Date**: 2019-12-06
**URL**: https://discourse.slicer.org/t/accessing-slicerelastix-from-within-python-module/9410

---

## Post #1 by @Alex_Vergara (2019-12-06 13:39 UTC)

<p>I am trying to use SlicerElastix module from my module as a cli call. However, all these fails</p>
<pre><code class="lang-auto">slicer.cli.run(module=slicer.modules.slicerelastix, None,
                                parameters, wait_for_completion=True, update_display=False)
&gt;&gt;&gt; module 'modules' has no attribute 'slicerelastix'

slicer.cli.run(module=slicer.modules.elastix, None,
                                parameters, wait_for_completion=True, update_display=False)
&gt;&gt;&gt; module 'modules' has no attribute 'elastix'
</code></pre>
<p>any way to call elastix registration from the module? I have the module installed and running.</p>

---

## Post #2 by @cpinter (2019-12-06 14:08 UTC)

<p>After I install SlicerElastix, the second way you tried allows me to access the module:</p>
<pre><code>&gt;&gt;&gt; slicer.modules.elastix
qSlicerScriptedLoadableModule (qSlicerScriptedLoadableModule at: 0x0000026B63E3A8F0)
</code></pre>
<p>But then I got a different error when trying to run the module with an existing parameter node:</p>
<pre><code>&gt;&gt;&gt; slicer.cli.run(slicer.modules.elastix, paramNode)
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "C:\Program Files\Slicer 4.11.0-2019-06-11\bin\Python\slicer\cli.py", line 78, in run
    logic.SetDeleteTemporaryFiles(1 if delete_temporary_files else 0)
AttributeError: 'SlicerBaseLogicPython.vtkSlicerScriptedLoadableMod' object has no attribute 'SetDeleteTemporaryFiles'
</code></pre>
<p>SetDeleteTemporaryFiles is a function in vtkSlicerCLIModuleLogic, so it is strange that the ‘logic’ variable in cli.py is a vtkSlicerScriptedLoadableModuleNode instance. Not sure how it can happen.</p>
<p>(Note: I used an old nightly, so it may be different on a newer one)</p>

---

## Post #3 by @Alex_Vergara (2019-12-06 14:24 UTC)

<p>I have figure out a way to invoke it as</p>
<pre><code class="lang-auto">slicer.cli.run(module=slicer.util.getModule("Elastix"), parameters=parameters, 
                                    wait_for_completion=True, update_display=False)
</code></pre>
<p>not the usual way but it get invoked, now the parameter set is a bit awkward and the results I got are not the ones from the module itself (The outputTransformNode is not updated at all)</p>
<p>The error I am getting is</p>
<pre><code class="lang-auto">&gt;&gt;&gt;'SlicerBaseLogicPython.vtkSlicerScriptedLoadableMod' object has no attribute 'CreateNodeInScene'
</code></pre>

---

## Post #4 by @lassoan (2019-12-06 14:34 UTC)

<p>You cannot call SlicerElastix as a CLI module because it is not a CLI module but a (Python) loadable module. At the time I’ve added this module, Python CLI option was not available and I would not switch, because loadable module allows creating a more user-friendly GUI.</p>
<p>You can use <a href="https://github.com/moselhy/SlicerSequenceRegistration/blob/e9ac5c24e30ecee6a0f8dfee472aa54ff11497cf/SequenceRegistration/SequenceRegistration.py#L557-L562">Sequence registration</a> module as an example of using Elastix from another module.</p>

---

## Post #5 by @cpinter (2019-12-06 14:53 UTC)

<p>I didn’t even bother checking <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"> Right, if it’s not a CLI then it cannot be called like that.</p>

---

## Post #6 by @Alex_Vergara (2019-12-06 14:54 UTC)

<p>OK, made it as</p>
<pre><code class="lang-python">        try:
            import Elastix
            elastixLogic = Elastix.ElastixLogic()
            parameterFilenames = elastixLogic.getRegistrationPresets()[0][Elastix.RegistrationPresets_ParameterFilenames]
            useelastix = True
        except Exception as e:
            print(e)
            useelastix = False
</code></pre>
<p>and then</p>
<pre><code class="lang-python">                    elastixLogic.registerVolumes(
                                densRnode['node'], densnode['node'],
                                parameterFilenames = parameterFilenames,
                                outputTransformNode = transformNode
                                )
</code></pre>
<p>now it is running as the GUI, Thanks so much!!!</p>

---

## Post #7 by @Saima (2020-04-28 06:46 UTC)

<p>Hi Andras,<br>
Is it possible to use elastix as clil module from another module. if not what are the other options.</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #8 by @lassoan (2020-04-28 15:17 UTC)

<p>See an example how Elastix is used by another module here: <a href="https://github.com/moselhy/SlicerSequenceRegistration/blob/master/SequenceRegistration/SequenceRegistration.py">https://github.com/moselhy/SlicerSequenceRegistration/blob/master/SequenceRegistration/SequenceRegistration.py</a></p>

---
