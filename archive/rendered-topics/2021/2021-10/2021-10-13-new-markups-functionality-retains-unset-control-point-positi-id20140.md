# New Markups functionality retains unset control point positions

**Topic ID**: 20140
**Date**: 2021-10-13
**URL**: https://discourse.slicer.org/t/new-markups-functionality-retains-unset-control-point-positions/20140

---

## Post #1 by @mikebind (2021-10-13 19:27 UTC)

<p>I was trying out using the new landmark workflow outlined by <a class="mention" href="/u/smrolfe">@smrolfe</a> here: <a href="https://discourse.slicer.org/t/changes-to-the-markups-module/19871" class="inline-onebox">Changes to the Markups Module</a></p>
<p>Specifically, manually create a set of labeled fiducial points on one case, then to use on the next case as a template, load the saved markup and unset all of the positions (by highlighting them on the control point list in the MarkupsModule and clicking the “Undefine position for the selected control points” button). The position coordinates disappear as expected, as do the glyphs.  However, until new positions are chosen, the old point positions are still stored, and GetNthControlPointPosition() returns the old point position. I discovered this when I accidentally ran further processing without placing all the points.  The measurements came out very odd, and I realized that there were measurements which involved a point which I hadn’t placed.  This seems like a pretty serious bug. Once a position has been unset, requests for that point’s position definitely shouldn’t return an old position.</p>

---

## Post #2 by @smrolfe (2021-10-13 19:36 UTC)

<p>Thanks, GetNthControlPointPosition() should be updated so it’s checking the point position status before returning the position. Could open a GH issue to document this?</p>

---

## Post #3 by @ezgimercan (2021-10-13 20:06 UTC)

<p>I thought about this too, it is nice that they remember their old position in case you mistakenly unset them by toggling the status icon - I do (one really wishes there was an undo/redo in markups). But the python interface should not return their old position, of course.</p>

---

## Post #4 by @mikebind (2021-10-13 20:14 UTC)

<p>Posted this here:</p><aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5948">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5948" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5948" target="_blank" rel="noopener nofollow ugc">Markups: GetNthControlPointPosition() returns positions for unset points</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-10-13" data-time="20:14:25" data-timezone="UTC">08:14PM - 13 Oct 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/mikebind" target="_blank" rel="noopener nofollow ugc">
          <img alt="mikebind" src="https://avatars.githubusercontent.com/u/3981795?v=4" class="onebox-avatar-inline" width="20" height="20">
          mikebind
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">When a control point has a position set, then unset, getting the position of the<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> unset control point returns the old position (from before being unset).  See discussion here:

https://discourse.slicer.org/t/new-markups-functionality-retains-unset-control-point-positions/20140


## Steps to reproduce

Create fiducial markup node, place a point.  In the Markups module, select that control point, and click to unset it's position. From the python interactor, use GetNthControlPointPosition() to get the point's position. The assigned position is the originally placed position, as if it had not been unset. 

## Expected behavior

I would expect the requesting the position of an unset point to either throw an exception or return a value indicating that the point has no position, such as None.

## Environment
- Slicer version: Slicer-4.13.0-2021-09-26
- Operating system: Windows 10</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @smrolfe (2021-10-13 20:27 UTC)

<p><a class="mention" href="/u/ezgimercan">@ezgimercan</a> the previous position will still be accessible using RestoreNthControlPointPosition(), but should not be returned through GetNthControlPointPosition().</p>

---

## Post #6 by @lassoan (2021-10-13 20:27 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="1" data-topic="20140">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>The measurements came out very odd, and I realized that there were measurements which involved a point which I hadn’t placed. This seems like a pretty serious bug</p>
</blockquote>
</aside>
<p>To me, inability to get and set the position (temporarily making the position appear/disappear depending on some other properties of the control point) would be a much more serious bug. Why did you assume that the state of the control point blocks setting/getting the associated position value?</p>
<p>I see that crosstalk between position and status can is problematic. We had similar issues with “number of control points”. It is not obvious if the number includes skipped, previewed, undefined points or not.</p>
<p>I agree that something need to be done to make the API simple and bulletproof, but since markups classes got many features, offering a simple API has become a hard task.</p>

---

## Post #7 by @lassoan (2021-10-13 20:39 UTC)

<p>We have introduced some crosstalk between position and status and various other methods, see:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/f6a77810dcb4df32c933ceb6d6571407af60e74d/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsNode.h#L305-L308">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/f6a77810dcb4df32c933ceb6d6571407af60e74d/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsNode.h#L305-L308" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/f6a77810dcb4df32c933ceb6d6571407af60e74d/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsNode.h#L305-L308" target="_blank" rel="noopener">Slicer/Slicer/blob/f6a77810dcb4df32c933ceb6d6571407af60e74d/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsNode.h#L305-L308</a></h4>



  <pre class="onebox">    <code class="lang-h">
      <ol class="start lines" start="305" style="counter-reset: li-counter 304 ;">
          <li>/// Return the number of control points that are already placed (not being previewed or undefined).</li>
          <li>int GetNumberOfDefinedControlPoints(bool includePreview=false);</li>
          <li>/// Return the number of control points that have not been placed (not being previewed or skipped).</li>
          <li>int GetNumberOfUndefinedControlPoints(bool includePreview = false);</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/f6a77810dcb4df32c933ceb6d6571407af60e74d/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsNode.h#L406-L426">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/f6a77810dcb4df32c933ceb6d6571407af60e74d/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsNode.h#L406-L426" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/f6a77810dcb4df32c933ceb6d6571407af60e74d/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsNode.h#L406-L426" target="_blank" rel="noopener">Slicer/Slicer/blob/f6a77810dcb4df32c933ceb6d6571407af60e74d/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsNode.h#L406-L426</a></h4>



  <pre class="onebox">    <code class="lang-h">
      <ol class="start lines" start="406" style="counter-reset: li-counter 405 ;">
          <li>/// Set of the Nth control point position from a pointer to an array</li>
          <li>/// \sa SetNthControlPointPosition</li>
          <li>void SetNthControlPointPositionFromPointer(const int pointIndex, const double *pos);</li>
          <li>/// Set of the Nth control point position from an array</li>
          <li>/// \sa SetNthControlPointPosition</li>
          <li>void SetNthControlPointPositionFromArray(const int pointIndex, const double pos[3], int positionStatus = PositionDefined);</li>
          <li>/// Set of the Nth control point position from coordinates</li>
          <li>/// \sa SetNthControlPointPositionFromPointer, SetNthControlPointPositionFromArray</li>
          <li>void SetNthControlPointPosition(const int pointIndex, const double x, const double y, const double z, int positionStatus = PositionDefined);</li>
          <li>/// Set of the Nth control point position using World coordinate system</li>
          <li>/// Calls SetNthControlPointPosition after transforming the passed in coordinate</li>
          <li>/// \sa SetNthControlPointPosition</li>
          <li>void SetNthControlPointPositionWorld(const int pointIndex, const double x, const double y, const double z);</li>
          <li>/// Set of the Nth control point position from an array using World coordinate system</li>
          <li>/// \sa SetNthControlPointPosition</li>
          <li>void SetNthControlPointPositionWorldFromArray(const int pointIndex, const double pos[3], int positionStatus = PositionDefined);</li>
          <li>/// Set of the Nth control point position and orientation from an array using World coordinate system.</li>
          <li>/// Orientation: x (0, 3, 6), y (1, 4, 7), z (2, 5, 8)</li>
          <li>/// \sa SetNthControlPointPosition</li>
          <li>void SetNthControlPointPositionOrientationWorldFromArray(const int pointIndex,</li>
          <li>  const double pos[3], const double orientationMatrix[9], const char* associatedNodeID, int positionStatus = PositionDefined);</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Along these lines, we could add more flags to the <code>GetNthControlPointPosition...</code> methods.</p>
<p>However, the API is already quite complicated, and may not even fulfill the need of all use cases and doesn’t distinguish between all states (undefined, skipped, previewed, defined). So, I’m not sure that just adding a few flags would be sufficient.</p>

---

## Post #8 by @mikebind (2021-10-13 20:50 UTC)

<p>What was a serious problem to me was that an old position was used when I thought it had been removed.  This means that by missing a step (accidentally skipping a point that was supposed to be placed), and then running downstream processing, I got results that were almost reasonable, instead of getting an error or a more obviously unreasonable result.  This happened because the position of the old point is not a terrible guess for the position of the new point (and more generally, the relationships among landmarks will be similar in the template case and the new case).  This is a much more subtle kind of error than if unsetting positions reset them to be at (0,0,0) and not shown.  If that happened, all distances between unplaced points would come out zero, ratios would throw errors, angles would have problems, etc.  You would know something was wrong.  In the current system, if you placed no points and ran your downstream processing you would get the exact same measurements as in the template case.</p>
<p>Anyway, now that I know that this is how it works, it is of course possible to add a check to make sure the point status is appropriate before using its position value. I think the primary reason I expected that the old position had been eliminated was that the position disappeared from the Markups module.  If the position is just “dormant”, perhaps it would make sense to italicize and gray out the position?  This might be confusing to users who expect it to disappear, but it better reflects the actual state of the point, and would make it clear that the unset position can be restored.</p>

---

## Post #9 by @lassoan (2021-10-13 20:56 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="8" data-topic="20140">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>If the position is just “dormant”, perhaps it would make sense to italicize and gray out the position? This might be confusing to users who expect it to disappear, but it better reflects the actual state of the point, and would make it clear that the unset position can be restored.</p>
</blockquote>
</aside>
<p>Graying out position of undefined points is a great idea. It would eliminate a hidden state variable, thereby making the actual behavior of the software more clear for users and developers. It is also consistent with what is written to files.</p>

---

## Post #10 by @ezgimercan (2021-10-13 21:50 UTC)

<p>Even in previous version of markups module, when we were recording “missing” landmarks as (0,0,0), I had added a check in my custom read functions (even if there is one, I would wrap it in a new one to add this check) where I set the coordinates of any point at (0,0,0) as (NA, NA, NA) or (None, None, None) depending on the downstream language. I was expecting something similar with the skip button and add empty point (+*) , rather than a 0,0,0 or retaining old position. But as I said, in the absence of an undo functionality, retaining old values make sense. I just updated my downstream readers in R and python to do this check and set the values to NA for missing landmarks.<br>
I can imagine a scenario in other Slicer modules using markups, like PCA in SlicerMorph, this check again should be done if there is support for missing points. But if these downstream modules take the output of functions without any check, as in <a class="mention" href="/u/mikebind">@mikebind</a> 's scenario, they may produce incorrect results. So I am in support of updating these functions to return either an equivalent of NA or 0,0,0. Or update the API.</p>

---

## Post #11 by @lassoan (2021-10-14 13:02 UTC)

<aside class="quote no-group" data-username="ezgimercan" data-post="10" data-topic="20140">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ezgimercan/48/4584_2.png" class="avatar"> ezgimercan:</div>
<blockquote>
<p>But as I said, in the absence of an undo functionality, retaining old values make sense.</p>
</blockquote>
</aside>
<p>Actually, the undo functionality is already available in Slicer. You can enable undo/redo for fiducial nodes by copy-pasting these lines into the Python console:</p>
<pre data-code-wrap="python"><code class="lang-python"># Enable undo for the scene

slicer.mrmlScene.SetUndoOn()

# Enable undo for markups fiducial nodes

defaultMarkupsNode = slicer.mrmlScene.GetDefaultNodeByClass("vtkMRMLMarkupsFiducialNode")
if not defaultMarkupsNode:
    defaultMarkupsNode = slicer.vtkMRMLMarkupsFiducialNode()
    slicer.mrmlScene.AddDefaultNode(defaultMarkupsNode)

defaultMarkupsNode.UndoEnabledOn()

# Add standard keyboard shortcuts for scene undo/redo

redoKeyBindings = qt.QKeySequence.keyBindings(qt.QKeySequence.Redo)
for redoBinding in redoKeyBindings:
    redoShortcut = qt.QShortcut(slicer.util.mainWindow())
    redoShortcut.setKey(redoBinding)
    redoShortcut.connect("activated()", slicer.mrmlScene.Redo)

undoKeyBindings = qt.QKeySequence.keyBindings(qt.QKeySequence.Undo)
for undoBinding in undoKeyBindings:
    undoShortcut = qt.QShortcut(slicer.util.mainWindow())
    undoShortcut.setKey(undoBinding)
    undoShortcut.connect("activated()", slicer.mrmlScene.Undo)
</code></pre>
<p>It is not enabled by default because historically it was attempted to be enabled for all nodes by default, which was too complicated. Since undo was disabled, developers did not pay attention to properly calling <code>markupsNode-&gt;SaveStateForUndo()</code> before all user actions, all those need to be added (without that, an undo reverts multiple user interactions), may be duplicated at a few places (requiring hitting undo/redo shortcuts multiple times to get a visible change), and of course some display update issues or other small bugs may be uncovered. Without these fixes, undo/redo will not feel very robust, but these should be all fairly easy to address.</p>
<p>If you want to further discuss of undo/redo then please create a new topic.</p>
<aside class="quote no-group" data-username="ezgimercan" data-post="10" data-topic="20140">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ezgimercan/48/4584_2.png" class="avatar"> ezgimercan:</div>
<blockquote>
<p>I can imagine a scenario in other Slicer modules using markups, like PCA in SlicerMorph, this check again should be done if there is support for missing points.</p>
</blockquote>
</aside>
<p>Both mask based (separate column specifies if an entry is missing or not) and special placeholder value based approaches are commonly used for dealing with missing values.</p>
<p>Slicer’s table infrastructure already supports both techniques. In table properties, the user can set any placeholder value as null value (0, -1, 1e6, nan, inf, …). This placeholder value is stored in the table schema.</p>
<p>For example, table exported from markups fiducial node:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5ccdd466a3cd1785acb05594646468788f13477e.png" data-download-href="/uploads/short-url/deYUKE6QTI2sF0hlqeoMdEkYYRo.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5ccdd466a3cd1785acb05594646468788f13477e_2_307x500.png" alt="image" data-base62-sha1="deYUKE6QTI2sF0hlqeoMdEkYYRo" width="307" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5ccdd466a3cd1785acb05594646468788f13477e_2_307x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5ccdd466a3cd1785acb05594646468788f13477e_2_460x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5ccdd466a3cd1785acb05594646468788f13477e_2_614x1000.png 2x" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">759×1235 51.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Written to csv file (<code>table.csv</code>):</p>
<pre><code class="lang-plaintext">"label","r","a","s","defined","selected","visible","locked","description"
"F_1-1",-17.3607,-30.2059,-10.2143,1,1,1,0,""
"F_1-2",-12.0642,5.98722,-10.2143,1,1,1,0,""
"F_1-3",-67.678,6.9286,7.38225,0,1,1,0,""
"F_1-4",83.4364,-7.27105,-175.25,0,1,1,0,""
"F_1-5",-111.564,11.9882,-175.25,1,1,1,0,""
</code></pre>
<p>Schema file (<code>Table.schema.csv</code>) written out along with the table file:</p>
<pre><code class="lang-plaintext">"columnName","nullValue","type","componentNames"
"label","","string",""
"r","nan","double",""
"a","nan","double",""
"s","nan","double",""
"defined","","bit",""
"selected","","bit",""
"visible","","bit",""
"locked","","bit",""
"description","","string",""
</code></pre>
<p>Currently, markups module’s “Export/import table” feature uses only the masking technique (via a separate “defined” Boolean column), but we could add an option to replace point coordinates of undefined points with a null placeholder value.</p>
<p>This refactoring would be a good opportunity to switch to standard csv format from the limited and broken fcsv format (multi-line header, hardcoded columns, no way to specify column type, null and default values, etc.).</p>

---

## Post #12 by @jamesobutler (2021-11-30 02:25 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="8" data-topic="20140">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>If the position is just “dormant”, perhaps it would make sense to italicize and gray out the position? This might be confusing to users who expect it to disappear, but it better reflects the actual state of the point, and would make it clear that the unset position can be restored.</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="20140">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Graying out position of undefined points is a great idea. It would eliminate a hidden state variable, thereby making the actual behavior of the software more clear for users and developers. It is also consistent with what is written to files.</p>
</blockquote>
</aside>
<p>PR issued to gray out the position when it is marked to skip placement</p><aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6049">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6049" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/6049" target="_blank" rel="noopener nofollow ugc">ENH: Mark control point coordinate items disabled when skipping</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>jamesobutler:5948-skip-display</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2021-11-29" data-time="23:34:29" data-timezone="UTC">11:34PM - 29 Nov 21 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
            <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
            jamesobutler
          </a>
        </div>

        <div class="lines" title="2 commits changed 1 files with 133 additions and 100 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/6049/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+133</span>
            <span class="removed">-100</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">As discussed at https://discourse.slicer.org/t/new-markups-functionality-retains<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6049" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">-unset-control-point-positions/20140/8, marking the control point coordinate items as disabled (grayed out) instead of not displaying the position is a better visual to indicate that a skipped state control point still has a position defined.

I guess control point name could also be set to the disabled look as well if we wanted.

re: #5948

| | Current | This PR|
|-|---------|---------|
|Skip placement | ![image](https://user-images.githubusercontent.com/15837524/143974135-ed4a39e4-8206-4394-b862-6cf583677038.png)|![image](https://user-images.githubusercontent.com/15837524/143959385-2ceb3c25-85bc-4fab-9eec-422f245098f6.png)|
|Restore position | ![image](https://user-images.githubusercontent.com/15837524/143974095-824c502e-2cb0-456d-89b2-ec94c39b6cef.png)|![image](https://user-images.githubusercontent.com/15837524/143974418-40994a8b-702e-4c35-918b-c36d63d867ea.png)|</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
