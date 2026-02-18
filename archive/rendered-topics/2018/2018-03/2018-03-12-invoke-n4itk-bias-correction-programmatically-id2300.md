# Invoke N4ITK Bias Correction Programmatically

**Topic ID**: 2300
**Date**: 2018-03-12
**URL**: https://discourse.slicer.org/t/invoke-n4itk-bias-correction-programmatically/2300

---

## Post #1 by @zjx1805 (2018-03-12 16:33 UTC)

<p>Hello All,</p>
<p>Is there a way to programmatically invoke the N4ITKBiasCorrection module through the python interpreter? I was trying to figure out what parameters as well as their types I need to provide by looking at the source code <a href="https://github.com/Slicer/Slicer/blob/master/Modules/CLI/N4ITKBiasFieldCorrection/N4ITKBiasFieldCorrection.cxx" rel="nofollow noopener">here</a> but I am not very familiar with C++ code. I assume it should be something like slicer.modules.n4itkbiasfieldcorrection.something (but I could not find a function that sets the input) or using SlicerExecutionModule. More generally this question would be how to figure out the input parameters and their types that should be provided to other built-in modules and how to invoke them through the python interpreter. Any help would be greatly appreciated!</p>

---

## Post #2 by @pieper (2018-03-12 17:07 UTC)

<p>Hi - This info should be what you need: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python</a></p>

---

## Post #3 by @zjx1805 (2018-03-12 18:35 UTC)

<p>Thank you for your prompt reply!</p>

---
