# Extracting data from multiple JSON files.

**Topic ID**: 28115
**Date**: 2023-03-01
**URL**: https://discourse.slicer.org/t/extracting-data-from-multiple-json-files/28115

---

## Post #1 by @Paul_Rothwell (2023-03-01 15:13 UTC)

<p>I have multiple (14 to be exact) closed curve measurements for each scan (measurement of artery lumen). I ideally would like to extract the length, curvature mean, curvature max and area from each JSON file into excel.</p>
<p>I can do this manually as seen in the attached picture but doing so for each measurement takes 14 clicks so for each scan that will be 196 clicks with each bit of data on a separate sheet. Then I work out the averages.</p>
<p>I’m fine getting the data the long winded way already explained here and youtube. I was hoping there might be a quicker was to extract this data with a power query maybe but I have tried to search and attempt my own but with no luck.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58acecfc0c49b6479a687fc817ea30c9f521fcf0.png" data-download-href="/uploads/short-url/cEsvyMnEu0iFylq3hVFjX0SkpY4.png?dl=1" title="Excel Power Query" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58acecfc0c49b6479a687fc817ea30c9f521fcf0_2_690x278.png" alt="Excel Power Query" data-base62-sha1="cEsvyMnEu0iFylq3hVFjX0SkpY4" width="690" height="278" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58acecfc0c49b6479a687fc817ea30c9f521fcf0_2_690x278.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58acecfc0c49b6479a687fc817ea30c9f521fcf0_2_1035x417.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58acecfc0c49b6479a687fc817ea30c9f521fcf0_2_1380x556.png 2x" data-dominant-color="F2F5F3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Excel Power Query</span><span class="informations">2511×1015 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-03-01 15:28 UTC)

<p>Yes, unfortunately Excel’s json support is quite poor (requires lots of clicks).</p>
<p>If you want to copy measurements from many markups at once then you can write a short Python code snippet to scan for all the markups in the scene and copy all its measurements to the clipboard, so that you can paste them into Excel.</p>
<p>There is a <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#copy-all-measurements-in-the-scene-to-excel">full example in the script repository</a> that you can customize it a bit (e.g., for getting curves, change it to <code>getNodesByClass('vtkMRMLMarkupsCurveNode')</code> and you can enable <code>curvature mean</code> and <code>curvature max</code> measurements in addition to <code>length</code>), and then copy-paste it to the Python console in Slicer.</p>
<p>To run this script automatically instead of manual copy-pasting, you can put it in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#application-startup-file">application startup script</a>.</p>

---

## Post #3 by @Paul_Rothwell (2023-03-01 18:24 UTC)

<p>Many thanks for the quick reply. I did like the fact the JSON file is still connected to the data if it is updated it can be refreshed but your option will save me a huge amount of time. I have hundreds of patients to do quite quickly.</p>
<p>Thanks so much <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
