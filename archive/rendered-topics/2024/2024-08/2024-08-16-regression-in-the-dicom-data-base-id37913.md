# Regression in the DICOM data base

**Topic ID**: 37913
**Date**: 2024-08-16
**URL**: https://discourse.slicer.org/t/regression-in-the-dicom-data-base/37913

---

## Post #1 by @rkikinis (2024-08-16 11:24 UTC)

<p>Loading the following data set in Slicer nightly 8-15 on Mac OS 14.6.1 fails.  The same data set works without problem in the stable release 5.6.2<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0bdd6595326fe7abf2420f74313587e74249526.jpeg" data-download-href="/uploads/short-url/ylHjGgOnWMJWe8bCWArkJp3hngy.jpeg?dl=1" title="Screenshot 2024-08-16 at 7.16.05 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f0bdd6595326fe7abf2420f74313587e74249526_2_308x500.jpeg" alt="Screenshot 2024-08-16 at 7.16.05 AM" data-base62-sha1="ylHjGgOnWMJWe8bCWArkJp3hngy" width="308" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f0bdd6595326fe7abf2420f74313587e74249526_2_308x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f0bdd6595326fe7abf2420f74313587e74249526_2_462x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f0bdd6595326fe7abf2420f74313587e74249526_2_616x1000.jpeg 2x" data-dominant-color="28251A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-08-16 at 7.16.05 AM</span><span class="informations">828×1344 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The data is from IDC and loads into slicer with the IDC viewer.<br>
SeriesInstanceUID to download: 1.3.6.1.4.1.14519.5.2.1.2932.1975.255072988367557196694880426160</p>

---

## Post #2 by @issakomi (2024-08-16 15:47 UTC)

<p>There is the strange value of <em>Spacing Between Slices</em> (0x0018, 0x0088) <code>-1</code>. BTW, there seems to be a bug (or “behavior change”) in recent GDCM IO that may be related, s. <a href="https://github.com/InsightSoftwareConsortium/ITK/issues/4794" rel="noopener nofollow ugc">ITK issue 4794</a>. <strong>But I am not sure</strong>, just FYI. cc <a class="mention" href="/u/dzenanz">@dzenanz</a></p>
<p>dciodvfy:<br>
<code>Error - Illegal negative value - SpacingBetweenSlices = -1</code></p>

---

## Post #3 by @issakomi (2024-08-16 16:03 UTC)

<p>I can confirm that <em>Spacing Between Slices</em> <code>-1</code> causes the problem. I have changed it to <code>1</code> (don’t know what the value should be, but AFAIK it should be taken from IPP/IOP) and the series loads (latest preview, Linux)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfc4ba2ba16b2ac6418d31b4a11dd1afe9214b2b.jpeg" data-download-href="/uploads/short-url/tE0jZMSHC62RzWKKbQtAL9dk999.jpeg?dl=1" title="Screenshot at 2024-08-16 17-59-44" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfc4ba2ba16b2ac6418d31b4a11dd1afe9214b2b_2_690x435.jpeg" alt="Screenshot at 2024-08-16 17-59-44" data-base62-sha1="tE0jZMSHC62RzWKKbQtAL9dk999" width="690" height="435" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfc4ba2ba16b2ac6418d31b4a11dd1afe9214b2b_2_690x435.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfc4ba2ba16b2ac6418d31b4a11dd1afe9214b2b_2_1035x652.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfc4ba2ba16b2ac6418d31b4a11dd1afe9214b2b.jpeg 2x" data-dominant-color="98969B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot at 2024-08-16 17-59-44</span><span class="informations">1281×809 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @rkikinis (2024-08-16 19:22 UTC)

<p>The same data set loads properly in the stable release. Something must have broken as the nightly build has a different version of the dicom module.</p>

---

## Post #5 by @jamesobutler (2024-08-16 20:04 UTC)

<p>Yes Slicer Stable (5.6.x) uses ITK 5.3.0 while Slicer Preview (5.7) is using ITK 5.4.0.</p>

---

## Post #6 by @fedorov (2024-08-29 20:27 UTC)

<p>For convenience, to download the series mentioned by <a class="mention" href="/u/rkikinis">@rkikinis</a>, you can do this:</p>
<pre data-code-wrap="bash"><code class="lang-bash">$ pip install --upgrade idc-index
$ idc download 1.3.6.1.4.1.14519.5.2.1.2932.1975.255072988367557196694880426160
</code></pre>
<p>Also for convenience, the BigQuery query below will select all series in Imaging Data Commons that have negative <code>SpacingBetweenSlices</code>.</p>
<pre data-code-wrap="sql"><code class="lang-sql">WITH
  temp_table AS (
  SELECT
    SeriesInstanceUID,
    Manufacturer,
    collection_id,
    Modality,
    SpacingBetweenSlices
  FROM
    `bigquery-public-data.idc_current.dicom_all`
  WHERE
    SAFE_CAST(SpacingBetweenSlices AS INT64)&lt;0)
SELECT
  SeriesInstanceUID, any_value(Manufacturer) as Manufacturer, any_value(collection_id) as collection_id, any_value(Modality) as Modality, any_value(SpacingBetweenSlices) as SpacingBetweenSlices
FROM
  temp_table
  group by SeriesInstanceUID
order by Modality
</code></pre>
<p>For the sake of convenience, the result of running the query is below. You can plug in <code>SeriesInstanceUID</code> into the instructions above to download any of those series.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Row</th>
<th><strong>SeriesInstanceUID</strong></th>
<th><strong>Manufacturer</strong></th>
<th><strong>collection_id</strong></th>
<th><strong>Modality</strong></th>
<th><strong>SpacingBetweenSlices</strong></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>1.3.6.1.4.1.32722.99.99.25384965558792938714037113526608989475</td>
<td>Philips</td>
<td>nsclc_radiomics_genomics</td>
<td>CT</td>
<td>-4</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>1.3.6.1.4.1.32722.99.99.100358904385730998553678259325908346054</td>
<td>Philips</td>
<td>nsclc_radiomics_genomics</td>
<td>CT</td>
<td>-4</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>1.3.6.1.4.1.32722.99.99.149205799948107127590297091243342465514</td>
<td>Philips</td>
<td>nsclc_radiomics_genomics</td>
<td>CT</td>
<td>-4</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>1.3.6.1.4.1.32722.99.99.28029226020345235950699297480918949957</td>
<td>Philips</td>
<td>nsclc_radiomics_genomics</td>
<td>CT</td>
<td>-4</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>1.3.6.1.4.1.32722.99.99.227649070570497400491575590741039272857</td>
<td>Philips</td>
<td>nsclc_radiomics_genomics</td>
<td>CT</td>
<td>-4</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>1.3.6.1.4.1.14519.5.2.1.7009.2401.242751552100019522164450359161</td>
<td>Philips Medical Systems</td>
<td>acrin_flt_breast</td>
<td>CT</td>
<td>-4</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>1.3.6.1.4.1.32722.99.99.87555546360421578566793618960733881338</td>
<td>Philips</td>
<td>nsclc_radiomics_genomics</td>
<td>CT</td>
<td>-4</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>1.3.6.1.4.1.14519.5.2.1.7009.2401.133294077881051013352649869844</td>
<td>Philips Medical Systems</td>
<td>acrin_flt_breast</td>
<td>CT</td>
<td>-4</td>
<td></td>
</tr>
<tr>
<td>9</td>
<td>1.3.6.1.4.1.32722.99.99.202497385511333427836173062690695671593</td>
<td>Philips</td>
<td>nsclc_radiomics_genomics</td>
<td>CT</td>
<td>-4</td>
<td></td>
</tr>
<tr>
<td>10</td>
<td>1.3.6.1.4.1.32722.99.99.234042609125631064514013492837366678413</td>
<td>Philips</td>
<td>nsclc_radiomics_genomics</td>
<td>CT</td>
<td>-4</td>
<td></td>
</tr>
<tr>
<td>11</td>
<td>1.3.6.1.4.1.14519.5.2.1.7009.2401.257448054826249901110797391087</td>
<td>Philips Medical Systems</td>
<td>acrin_flt_breast</td>
<td>CT</td>
<td>-4</td>
<td></td>
</tr>
<tr>
<td>12</td>
<td>1.3.6.1.4.1.14519.5.2.1.7009.2401.874419016376926649794615836826</td>
<td>Philips Medical Systems</td>
<td>acrin_flt_breast</td>
<td>CT</td>
<td>-4</td>
<td></td>
</tr>
<tr>
<td>13</td>
<td>1.3.6.1.4.1.14519.5.2.1.2857.3159.256409392788539989062455102657</td>
<td>Philips</td>
<td>cptac_cm</td>
<td>CT</td>
<td>-3</td>
<td></td>
</tr>
<tr>
<td>14</td>
<td>1.3.6.1.4.1.32722.99.99.316599411906020923226736902474087731150</td>
<td>Philips</td>
<td>nsclc_radiomics_genomics</td>
<td>CT</td>
<td>-4</td>
<td></td>
</tr>
<tr>
<td>15</td>
<td>1.3.6.1.4.1.32722.99.99.225570660272964280948169301188944152335</td>
<td>Philips</td>
<td>nsclc_radiomics_genomics</td>
<td>CT</td>
<td>-4</td>
<td></td>
</tr>
<tr>
<td>16</td>
<td>1.3.6.1.4.1.14519.5.2.1.7009.2401.158401284359401547777840263080</td>
<td>Philips Medical Systems</td>
<td>acrin_flt_breast</td>
<td>CT</td>
<td>-4</td>
<td></td>
</tr>
<tr>
<td>17</td>
<td>1.3.6.1.4.1.32722.99.99.315391434416455128958547012718014023683</td>
<td>Philips</td>
<td>nsclc_radiomics_genomics</td>
<td>CT</td>
<td>-4</td>
<td></td>
</tr>
<tr>
<td>18</td>
<td>1.3.6.1.4.1.14519.5.2.1.7009.2401.128272705827469658312679193419</td>
<td>Philips Medical Systems</td>
<td>acrin_flt_breast</td>
<td>CT</td>
<td>-4</td>
<td></td>
</tr>
<tr>
<td>19</td>
<td>1.3.6.1.4.1.32722.99.99.154854822987323366648376936102077390994</td>
<td>Philips</td>
<td>nsclc_radiomics_genomics</td>
<td>CT</td>
<td>-4</td>
<td></td>
</tr>
<tr>
<td>20</td>
<td>1.3.6.1.4.1.32722.99.99.53827318715475830435474154358410860035</td>
<td>Philips</td>
<td>nsclc_radiomics_genomics</td>
<td>CT</td>
<td>-4</td>
<td></td>
</tr>
</tbody>
</table>
</div><p>There is also a recent related issue in OHIF about this: <a href="https://github.com/OHIF/Viewers/issues/4352" class="inline-onebox">[Bug] Multiframe DICOM negatiive Spacing Between Slices not handled · Issue #4352 · OHIF/Viewers · GitHub</a></p>

---

## Post #7 by @fedorov (2024-08-29 20:36 UTC)

<p>If you would like to see any of the series in the IDC-hosted OHIF v3 instance, you can get series-specific URL using the code below (after installing <a href="https://github.com/ImagingDataCommons/idc-index"><code>idc-index</code></a> as discussed earlier):</p>
<pre data-code-wrap="python"><code class="lang-python">from idc_index import IDCClient

series_uid ="1.3.6.1.4.1.14519.5.2.1.2932.1975.255072988367557196694880426160"

c = IDCClient()

c.get_viewer_URL(seriesInstanceUID=series_uid, viewer_selector="ohif_v3")
</code></pre>
<p><a href="https://viewer.imaging.datacommons.cancer.gov/v3/viewer/?StudyInstanceUIDs=1.3.6.1.4.1.14519.5.2.1.2932.1975.277486652714623414151775226101&amp;SeriesInstanceUIDs=1.3.6.1.4.1.14519.5.2.1.2932.1975.255072988367557196694880426160">https://viewer.imaging.datacommons.cancer.gov/v3/viewer/?StudyInstanceUIDs=1.3.6.1.4.1.14519.5.2.1.2932.1975.277486652714623414151775226101&amp;SeriesInstanceUIDs=1.3.6.1.4.1.14519.5.2.1.2932.1975.255072988367557196694880426160</a></p>

---

## Post #8 by @pieper (2024-09-25 00:32 UTC)

<p>After looking at this in more detail, I’m not convinced that the new GDCM behavior about using the <code>SpacingBetweenSlices</code> is actually incorrect.  I’ll comment on why in <a href="https://github.com/InsightSoftwareConsortium/ITK/issues/4794">the ITK issue</a>.</p>
<p>For Slicer, the issue has something to do with how non-right-handed direction matrices are handled.  If I add this line</p>
<pre><code class="lang-auto">seriesReader-&gt;SetForceOrthogonalDirection(false);
</code></pre>
<p>in <code>vtkITKArchetypeImageSeriesReader::RequestInformation</code> then the volume loads correctly.  Without it the image loads upside down and the acquisition transform is not able to fix it.</p>
<p>But since that option about orthogonal directions <a href="https://github.com/InsightSoftwareConsortium/ITK/commit/23436a04c978d176b32775e97d2701d96d6d2dd6">has been around for six years</a> it seems that something else recently has broken the path when this flag is not set, and perhaps that is due to the negative spacing.</p>
<p>I’m not sure when I’ll have a chance to dig into this more so I thought I’d post this note in case <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/jcfr">@jcfr</a>, <a class="mention" href="/u/issakomi">@issakomi</a>, or others know more.</p>

---

## Post #9 by @lassoan (2024-09-25 00:43 UTC)

<p>If you suspect that the normalization to right-handed coordinate system causes issues then make sure you use the latest Slicer main version (there were a few versions that did not work correctly) and/or call <code>vtkMRMLVolumeArchetypeStorageNode.SetForceRightHandedIJKCoordinateSystem(False)</code> to disable this mechanism completely.</p>

---

## Post #10 by @pieper (2024-09-25 01:07 UTC)

<p>Yes, I’m testing with the current main branch and I tried removing commenting out the part of the ScalarVolumePlugin that forces the right-handed behavior and it didn’t change anything.  I think the issue is in ITK, because when I set <code>seriesReader-&gt;SetForceOrthogonalDirection(false);</code> I get an identity direction matrix which is correct for this LPS axial IS scan, but without it (the default <code>true</code> value) I get a minus one in the lower left.</p>

---

## Post #11 by @MikhayEeer (2024-10-04 06:08 UTC)

<p>I have also meet this problem.<br>
There is no problem using version 5.6.2. I built version 5.7.0 from the source code. This problem occurs after some DICOM files are imported.<br>
When I change the -1 of the direction matrix, the DICOM display will be normal, but after using the AI ​​generated model of lungCTsegmenter, the generated segmentation position is misplaced.<br>
I want to know which part of the source code should be modified to correct the problem when importing DICOM.</p>

---

## Post #12 by @MikhayEeer (2024-10-04 06:09 UTC)

<p>I don’t dare to roll back the code version directly to 5.6.2, because I want to use the py translation fixed in 5.7.0.<br>
If I roll back the itk version in superbuild to 5.3.0, there are still many related errors.</p>

---

## Post #13 by @pieper (2024-10-04 13:29 UTC)

<p><a class="mention" href="/u/mikhayeeer">@MikhayEeer</a> I added</p>
<pre><code class="lang-auto">seriesReader-&gt;SetForceOrthogonalDirection(false);
</code></pre>
<p>right after this line:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/9c0754c6741e8127c38691895d452d389ee3cd03/Libs/vtkITK/vtkITKArchetypeImageSeriesReader.cxx#L684">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/9c0754c6741e8127c38691895d452d389ee3cd03/Libs/vtkITK/vtkITKArchetypeImageSeriesReader.cxx#L684" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/9c0754c6741e8127c38691895d452d389ee3cd03/Libs/vtkITK/vtkITKArchetypeImageSeriesReader.cxx#L684" target="_blank" rel="noopener">Slicer/Slicer/blob/9c0754c6741e8127c38691895d452d389ee3cd03/Libs/vtkITK/vtkITKArchetypeImageSeriesReader.cxx#L684</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="674" style="counter-reset: li-counter 673 ;">
          <li>else</li>
          <li>{</li>
          <li>  //</li>
          <li>  // more than one file, use series reader</li>
          <li>  //</li>
          <li>  itk::OrientImageFilter&lt;ImageType,ImageType&gt;::Pointer orient =</li>
          <li>    itk::OrientImageFilter&lt;ImageType,ImageType&gt;::New();</li>
          <li>  itk::ImageSeriesReader&lt;ImageType&gt;::Pointer seriesReader =</li>
          <li>    itk::ImageSeriesReader&lt;ImageType&gt;::New();</li>
          <li>  seriesReader-&gt;SetFileNames(this-&gt;FileNames);</li>
          <li class="selected">  seriesReader-&gt;SetImageIO(imageIO);</li>
          <li>  if (this-&gt;UseNativeCoordinateOrientation)</li>
          <li>  {</li>
          <li>    filter = seriesReader;</li>
          <li>  }</li>
          <li>  else</li>
          <li>  {</li>
          <li>    orient-&gt;SetInput(seriesReader-&gt;GetOutput());</li>
          <li>    orient-&gt;UseImageDirectionOn();</li>
          <li>    orient-&gt;SetDesiredCoordinateOrientation(this-&gt;DesiredCoordinateOrientation);</li>
          <li>    filter = orient;</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It would be great if you could test it with your data and report back.  So far in limited testing it’s been working for me.</p>

---

## Post #14 by @MikhayEeer (2024-10-04 15:14 UTC)

<p>Thank you very much for your specific solution. I will test this method in the next few days and give you feedback later.</p>

---

## Post #15 by @MikhayEeer (2024-10-08 07:46 UTC)

<p>Thanks for your solution, I have solved the problem successfully.</p>

---

## Post #16 by @pieper (2024-10-08 12:15 UTC)

<p>Thanks for reporting <a class="mention" href="/u/mikhayeeer">@MikhayEeer</a> .  <a class="mention" href="/u/lassoan">@lassoan</a> let’s discuss in the dev meeting but I suggest we go ahead and make this change in the preview version of Slicer and see if we hear of other regressions.</p>

---

## Post #17 by @pieper (2024-10-08 20:26 UTC)

<p>After some more testing and discussion during today’s dev meeting I’m convinced adding this flag is a good way forward.  If anybody notices regressions in the preview builds please speak up since this fix will in the 5.8 release coming the the next few weeks.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7987">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7987" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7987" target="_blank" rel="noopener">BUG: Regression for scans with negative spacing in DICOM</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>pieper:7937-dicom-regression</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2024-10-08" data-time="20:22:15" data-timezone="UTC">08:22PM - 08 Oct 24 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/pieper" target="_blank" rel="noopener">
            <img alt="pieper" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
            pieper
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 1 additions and 0 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7987/files" target="_blank" rel="noopener">
            <span class="added">+1</span>
            <span class="removed">-0</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Fixes #7937

See original report here about a dataset being scrambled that loa<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7987" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ded well in the 5.6.2 release:

https://discourse.slicer.org/t/regression-in-the-dicom-data-base/37913

This corresponds to the change in behavior described here, where spacing from ITK that used to be 1 is now, for example 5 or -1:

https://github.com/InsightSoftwareConsortium/ITK/issues/4794

Which is believed to be due to the changes here, which was added so that for Secondary Capture files the spacing would be respected if present:

https://github.com/InsightSoftwareConsortium/ITK/pull/4521

However adding this code in GDCM meant that if the SpacingBetweenSlices tag is present, even in a CT, it is being used by ITK to calculate spacing, and also ITKToRAS transforms when trying to orthogonalize the transform.

Since Slicer doesn't rely on orthogonal IJKToRAS transforms, this change tells ITK to skip that step and instead it relies on the positions and orientations of the slices to calculate the IJKToRAS transform, which is compatible with what Slicer expects.

This code was tested on both the CT scan with the negative spacing that was reported in the original issue, and on other CT cans without that tag and the geometry matches what was obtained in 5.6.2.

This change was discussed in the Slicer developer meeting 2024-10-08 and determined to be the best course of action.  Further fixes in GDCM or ITK were not pursued because it was unclear whta the correct behavior should be at the library level considering that a negative spacing between slices is technically invalid for CT scans according to the DICOM standard.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
