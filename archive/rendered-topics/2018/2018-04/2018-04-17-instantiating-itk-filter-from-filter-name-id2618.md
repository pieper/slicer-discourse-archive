---
topic_id: 2618
title: "Instantiating Itk Filter From Filter Name"
date: 2018-04-17
url: https://discourse.slicer.org/t/2618
---

# Instantiating ITK filter from filter name

**Topic ID**: 2618
**Date**: 2018-04-17
**URL**: https://discourse.slicer.org/t/instantiating-itk-filter-from-filter-name/2618

---

## Post #1 by @EricWilson (2018-04-17 21:57 UTC)

<p>I am having some difficulties with writing some code to take in a string and use that data to select and execute a SimpleITK filter. There doesn’t appear to be any way to access a filter object from sitk other than doing sitk. which won’t work with a string.</p>
<p>instead I am creating a dictionary with all the filters in the SimpleFilters widget and saving their id with their name. then I set the id as the current filter for the widget and apply the filter, but if i have more than one filter to apply, the app will crash since both are trying to run at the same time.</p>
<p>is this an error with slicer, which will normally wait until the execution of a filter is complete before continuing to the next line, or is there an error with my code that requires some kind of flag to know that the filter has completed?</p>
<p>also, is there a better way I should be doing this?</p>
<p>any help is appreciated, thanks.</p>

---

## Post #2 by @ihnorton (2018-04-18 02:19 UTC)

<p>Regarding:</p>
<aside class="quote no-group" data-username="EricWilson" data-post="1" data-topic="2618">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ericwilson/48/1513_2.png" class="avatar"> EricWilson:</div>
<blockquote>
<p>There doesn’t appear to be any way to access a filter object from sitk other than doing sitk. which won’t work with a string.</p>
</blockquote>
</aside>
<p>You can do:</p>
<pre><code class="lang-auto">In [6]: filter = 'AbsImageFilter'

In [7]: sitk.__getattribute__(filter)
Out[7]: SimpleITK.SimpleITK.AbsImageFilter
</code></pre>
<p>Not sure I follow the rest of the question (a short code snippet demonstrating the app crash might help).</p>

---

## Post #3 by @EricWilson (2018-04-18 14:50 UTC)

<p>ok, that was what just what I was looking for, thanks. I would like to add that what you sent returns the class for the filter, rather than the filter itself though. so if you wanted to get the same reference as you would with sitk.AbsImageFilter(), you need to add the parenthesis to the end of the call like this:<br>
sitk.__getattribute__(filter)()</p>
<p>as for the second part it isn’t really necessary anymore, but the method i was using was this:</p>
<pre><code class="lang-auto">filtersDict = {}
slicer.util.selectModule('SimpleFilters')
filtersWidget = slicer.modules.SimpleFiltersWidget
filtersJSON = filtersWidget.jsonFilters
for filterIdx in range(filtersWidget.filterSelector.count):
        filtersDict[filtersJSON[filterIdx]['name']] = filterIdx

customFilters = ['RecursiveGaussianImageFilter', 'LaplacianSharpeningImageFilter']
for filterName in customFilters:
        filtersWidget.filterSelector.setCurrentIndex(filtersDict[filterName])
        filtersWidget.onApplyButton()
</code></pre>
<p>this doesn’t really have a return for when the filter is complete, so the script would just keep running when a filter was going and crash the app.</p>

---

## Post #4 by @lassoan (2018-04-18 15:39 UTC)

<p>When you use a module from another module, you should never use a module’s GUI (…Widget class) but its logic (…Logic class). So, don’t call <code>onApplyButton</code> but instead <code>logic.run</code>.</p>
<p>SimpleFilters module creates a background thread to not block the GUI (so that you can abort filter execution). You can have a look at the <a href="https://github.com/SimpleITK/SlicerSimpleFilters/blob/master/SimpleFilters/SimpleFilters.py">Simple Filter module’s source code</a> to see which events you need to observe to get completion notification. However, if you don’t need this background execution feature then everything becomes really simple: you just instantiate a filter directly and run it on the main thread. The filter will not return until execution is completed.</p>

---
