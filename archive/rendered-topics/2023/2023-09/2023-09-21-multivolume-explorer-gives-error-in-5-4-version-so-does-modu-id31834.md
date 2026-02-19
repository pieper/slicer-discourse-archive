---
topic_id: 31834
title: "Multivolume Explorer Gives Error In 5 4 Version So Does Modu"
date: 2023-09-21
url: https://discourse.slicer.org/t/31834
---

# Multivolume Explorer gives error in 5.4 version,  so does module "sequences" allows to plot time intensity charts from multivolume datasets? 

**Topic ID**: 31834
**Date**: 2023-09-21
**URL**: https://discourse.slicer.org/t/multivolume-explorer-gives-error-in-5-4-version-so-does-module-sequences-allows-to-plot-time-intensity-charts-from-multivolume-datasets/31834

---

## Post #1 by @Jakub.Otahal (2023-09-21 20:18 UTC)

<p>Hello everybody,<br>
I have used for long time Multivolume Importer and Explorer to view and analyse DCE datasets in Slicer 4.11. Today when I come back to that with new 5.4 version of Slicer I realized that the Multivolume module is not able to plot intensity/time charts for segmented volumes. It gives error in vtk… Thus I found discussion describing that module “Sequences” is successor of Multivolume and should give same functionality. However, I was unable to found the way how to plot intensity/time plots for segments outlined in Editor. Is it my fault or the Sequences module doesnot support it yet?  If this is the case is there some easy way to export data (region intensity statistics through all frames) for labeled segments within DCE time series?</p>
<p>Thank you Jakub</p>

---

## Post #2 by @lassoan (2023-09-21 21:00 UTC)

<p>Instead of fixing errors in the deprecated MultiVolume modules, we’ll spend the time with adding any missing feature to modules that use sequences. Can you describe exactly what you need? Time-intensity plot in only two volumes is sufficient (no need for more volumes)? Is plotting one segment is sufficient? Any operations on the plots (e.g., subtract one from the other, normalization, …)? Provide minimum required feature set and what you would like to ideal have (we will implement the minimum feature set first, but knowing the future needs will help us make design decisions).</p>

---

## Post #3 by @Jakub.Otahal (2023-09-22 05:41 UTC)

<p>Hi, thank you very much for great support. We usually have segmentation finished on structural data  prior DCE analysis. We would love to have oportunity to select for which segmented region (segment) we want to plot an intensity curve derived from avarage values within the region. What is really needed, is to have method to either export or copy&amp;paste the values of the curve into a spreadsheet for further analysis and comparison to other regions…  I do believe this is not that much work and it will be highly appreciated within the community.</p>
<p>Thank you very much<br>
Best regards<br>
Jakub</p>

---

## Post #4 by @lassoan (2023-09-22 13:33 UTC)

<p>Thank you for the information. I should be able to work on this in about a month. I’ve added a ticket to track the status of this work:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/7238">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/7238" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/7238" target="_blank" rel="noopener">Add Sequence Intensity Profile module</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-09-22" data-time="13:29:07" data-timezone="UTC">01:29PM - 22 Sep 23 UTC</span>
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
          type:enhancement
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Is your feature request related to a problem? Please describe.

MultiVolume<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> Explorer module can compute average time-intensity profile in a ROI vs. time.
We would like to deprecate MultiVolume modules, but for this we would need to make this functionality available using Sequences.

## Describe the solution you'd like

Add a new module that can do all the plotting that is now implemented in MultiVolume Explorer module.

## Describe alternatives you've considered

The feature could be built into Sequences module (similarly to how it was built into MultiVolume explorer), but Sequences module is already too complex.

## Additional context

See [discussion on the Slicer Forum](https://discourse.slicer.org/t/multivolume-explorer-gives-error-in-5-4-version-so-does-module-sequences-allows-to-plot-time-intensity-charts-from-multivolume-datasets/31834/2).</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>In the meantime, could you provide sample data sets that I can test with (preferably from a public data repository, such as TCIA). It would help if you could find two data sets that could be used for testing the dual image input.</p>

---

## Post #5 by @Elette (2025-06-10 15:50 UTC)

<p>Hi Andras, did you manage to solve this one?<br>
I am also in need of the ‘Chart’ function of the Segments signal change over time for DCE MRI. in version 4.8 you can plot as many as you like and it seems to create a latent DoubleArray to populate the chart. How is it now with Sequences? Even a table or csv file with the signal over time for each segment would be amazing!<br>
Otherwise it seems I can just trick it into giving me one pixel as a time by creating a Plot and PlotSeries with the 1st multivolume. But it just doesnt represent the entire segment, and there has to be a better way! Are there any options?</p>
<p>FYI, here is the error I get from Slicer 5.8.1:<br>
[CRITICAL][Stream] 11.06.2025 01:29:14 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “…AppData\Local\slicer.org\Slicer 5.8.1\lib\Slicer-5.8\qt-loadable-modules\Python\qSlicerMultiVolumeExplorerCharts.py”, line 412, in requestChartCreation<br>
[CRITICAL][Stream] 11.06.2025 01:29:14 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     self.calculateLabeledVoxelsMeanAndInitiateChartArray()<br>
[CRITICAL][Stream] 11.06.2025 01:29:14 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “…\AppData\Local\slicer.org\Slicer 5.8.1\lib\Slicer-5.8\qt-loadable-modules\Python\qSlicerMultiVolumeExplorerCharts.py”, line 444, in calculateLabeledVoxelsMeanAndInitiateChartArray<br>
[CRITICAL][Stream] 11.06.2025 01:29:14 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     self.dataNodes[k] = slicer.mrmlScene.AddNode(slicer.vtkMRMLDoubleArrayNode())<br>
[CRITICAL][Stream] 11.06.2025 01:29:14 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - AttributeError: module ‘slicer’ has no attribute ‘vtkMRMLDoubleArrayNode’</p>

---
