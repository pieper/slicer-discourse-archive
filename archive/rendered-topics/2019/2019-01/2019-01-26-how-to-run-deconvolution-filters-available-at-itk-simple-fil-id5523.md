---
topic_id: 5523
title: "How To Run Deconvolution Filters Available At Itk Simple Fil"
date: 2019-01-26
url: https://discourse.slicer.org/t/5523
---

# How to run deconvolution filters available at “itk Simple Filters” module from the command line in linux?

**Topic ID**: 5523
**Date**: 2019-01-26
**URL**: https://discourse.slicer.org/t/how-to-run-deconvolution-filters-available-at-itk-simple-filters-module-from-the-command-line-in-linux/5523

---

## Post #1 by @shahrokh (2019-01-26 13:40 UTC)

<p>Hello Dear Developers and Users</p>
<p>How can I run deconvolution filters available at “<strong>itk Simple Filters</strong>” module (such as  <em>RichardsonLucyDeconvolutionImageFilter</em> and <em>TikhonovDeconvolutionImageFilter</em>) from the command line of linux?</p>
<p>Please guide me,<br>
Shahrokh.</p>

---

## Post #2 by @lassoan (2019-01-26 18:52 UTC)

<p>You can run the code the same way as within Slicer. You can either provide the entire code that you would like to run on the command line (good for a short, simple cases, see examples <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Launching_Slicer" rel="nofollow noopener">here</a>) or put the code in a .py file and execute that with Slicer as shown <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_can_I_run_slicer_operations_from_a_batch_script.3F" rel="nofollow noopener">here</a>.</p>

---

## Post #3 by @shahrokh (2019-01-28 13:46 UTC)

<p>Dear Andras</p>
<p>Thanks a lot for your guidance. As mentioned you, I want to use your second method (put the code in a .py file and execute that with Slicer).</p>
<p>Where can I find the Python codes for these filters?</p>
<p>Please guide me,</p>
<p>Shahrokh.</p>

---

## Post #4 by @shahrokh (2019-01-29 12:11 UTC)

<p>Dear Andras</p>
<p>I solved my problem in another way. For example, I edit the file of <em>itkTikhonovDeconvolutionImageFilterTest.cxx</em> (in the path of <em>~/ITK/Modules/Filtering/Deconvolution/test</em>) as following:</p>
<p><strong>From:</strong><br>
int itkTikhonovDeconvolutionImageFilterTest(int argc, char * argv[])**</p>
<p><strong>To:</strong><br>
int main(int argc, char * argv[])**</p>
<p>and create the file of <em>CmakeLists.txt</em> Which includes the following lines:</p>
<p>project(itkTikhonovDeconvolutionImageFilterTest)<br>
find_package(ITK REQUIRED)<br>
include(<span class="math">{ITK_USE_FILE})
add_executable(itkTikhonovDeconvolutionImageFilterTest itkTikhonovDeconvolutionImageFilterTest.cxx)
target_link_libraries(itkTikhonovDeconvolutionImageFilterTest </span>{ITK_LIBRARIES})</p>
<p>and finally compile it with the commands of cmake and make. With doing it, at now I have a executable file with the name of itkTikhonovDeconvolutionImageFilterTest</p>
<p>I think that this is not the correct way and logical method.<br>
According to Andras’s guidance, where can I find the Python codes for these filters?</p>
<p>Please guide me.<br>
Shahrokh</p>

---

## Post #5 by @jamesobutler (2019-01-29 14:17 UTC)

<p>The following page has some python examples of using SimpleITK filters.<br>
<a href="http://insightsoftwareconsortium.github.io/SimpleITK-Notebooks/Python_html/300_Segmentation_Overview.html" class="onebox" target="_blank" rel="nofollow noopener">http://insightsoftwareconsortium.github.io/SimpleITK-Notebooks/Python_html/300_Segmentation_Overview.html</a></p>
<p>In general, it is usually in a workflow like:</p>
<pre><code class="lang-python">otsu_filter = sitk.OtsuThresholdImageFilter()
otsu_filter.SetInsideValue(0)
otsu_filter.SetOutsideValue(1)
seg = otsu_filter.Execute(img_T1)
</code></pre>
<p>You can review the <a href="https://github.com/SimpleITK/SimpleITK/blob/f086d11979d4dd2fd772d9e947fe7cce8c6a91a6/Code/BasicFilters/json/TikhonovDeconvolutionImageFilter.json" rel="nofollow noopener">TikhonovDeconvolutionImageFilter.json</a> which details the available members. You could also use the filter in Slicer using the Simple Filters module. It will usually print to the python console the parameters that were set to execute and you could use that as an example.</p>

---
