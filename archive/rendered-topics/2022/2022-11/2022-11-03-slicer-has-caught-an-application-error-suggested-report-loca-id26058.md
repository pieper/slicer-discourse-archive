---
topic_id: 26058
title: "Slicer Has Caught An Application Error Suggested Report Loca"
date: 2022-11-03
url: https://discourse.slicer.org/t/26058
---

# "Slicer has caught an application error" suggested report location

**Topic ID**: 26058
**Date**: 2022-11-03
**URL**: https://discourse.slicer.org/t/slicer-has-caught-an-application-error-suggested-report-location/26058

---

## Post #1 by @jamesobutler (2022-11-03 19:31 UTC)

<p>I’ve come across the following error display which says to report the issue following instructions available at <a href="https://slicer.org" rel="noopener nofollow ugc">https://slicer.org</a>, but it isn’t obviously clear what instructions at <a href="http://slicer.org" rel="noopener nofollow ugc">slicer.org</a> to follow.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0af88916a5c950fe1dc531a39000011c02a304b4.png" alt="image" data-base62-sha1="1z3g5KJORLt9yX2rfaclxoD7LRG" width="502" height="188"></p>
<p>The text about following instructions available at <a href="https://slicer.org" rel="noopener nofollow ugc">https://slicer.org</a> is found in these 2 places of the code (see below). Should it instead link to the <a href="https://github.com/Slicer/Slicer/issues/new?assignees=&amp;labels=type%3Abug&amp;template=bug_report.md&amp;title=" rel="noopener nofollow ugc">Bug Report</a> template for the Slicer GitHub repo which includes instructions for the user to write steps to reproduce, platform used, etc? Or should the user be sent to <a href="https://discourse.slicer.org/">https://discourse.slicer.org/</a> to write up the steps to reproduce? Whether GitHub or the forum, both require a user account to submit so I don’t think one has a smaller barrier of entry for reporting these errors.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/bcedcfc48d453051165ddbd46305c495262db875/Base/QTGUI/qSlicerApplication.cxx#L474-L477">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/bcedcfc48d453051165ddbd46305c495262db875/Base/QTGUI/qSlicerApplication.cxx#L474-L477" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/bcedcfc48d453051165ddbd46305c495262db875/Base/QTGUI/qSlicerApplication.cxx#L474-L477" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/bcedcfc48d453051165ddbd46305c495262db875/Base/QTGUI/qSlicerApplication.cxx#L474-L477</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="474" style="counter-reset: li-counter 473 ;">
          <li>  errorMessage += tr("Adding more RAM may fix this issue.\n\n");</li>
          <li>  }</li>
          <li>errorMessage += tr("If you have a repeatable sequence of steps that causes this message, ");</li>
          <li>errorMessage += tr("please report the issue following instructions available at https://slicer.org\n\n\n");</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/bcedcfc48d453051165ddbd46305c495262db875/Base/QTGUI/qSlicerApplication.cxx#L493-L496">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/bcedcfc48d453051165ddbd46305c495262db875/Base/QTGUI/qSlicerApplication.cxx#L493-L496" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/bcedcfc48d453051165ddbd46305c495262db875/Base/QTGUI/qSlicerApplication.cxx#L493-L496" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/bcedcfc48d453051165ddbd46305c495262db875/Base/QTGUI/qSlicerApplication.cxx#L493-L496</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="493" style="counter-reset: li-counter 492 ;">
          <li>errorMessage = tr("%1 has caught an application error, ").arg(this-&gt;applicationName());</li>
          <li>errorMessage += tr("please save your work and restart.\n\n");</li>
          <li>errorMessage += tr("If you have a repeatable sequence of steps that causes this message, ");</li>
          <li>errorMessage += tr("please report the issue following instructions available at https://slicer.org\n\n\n");</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @pieper (2022-11-03 20:20 UTC)

<p>Good catch <a class="mention" href="/u/jamesobutler">@jamesobutler</a>.  How about sending them here:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/get_help.html</a></p>

---

## Post #3 by @jamesobutler (2022-11-03 20:55 UTC)

<p>If the application is a Slicer custom app, does it make sense to still send to a Slicer documentation page? Maybe if the application name is not “Slicer” (aka <code>slicer.app.isCustomMainApplication</code>), then to use the <code>slicer.app.documentationBaseUrl</code> or <code>slicer.app.repositoryURL</code> (although I guess this could be a private repo).</p>

---

## Post #4 by @pieper (2022-11-03 22:47 UTC)

<p>Good point, the url should be configurable for a custom app.</p>

---

## Post #5 by @jamesobutler (2022-11-09 22:33 UTC)

<p>I’ve created the following issue so I don’t forget to come back to this:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6653">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6653" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6653" target="_blank" rel="noopener nofollow ugc">Improve where to report application error occurrence</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-11-09" data-time="22:33:08" data-timezone="UTC">10:33PM - 09 Nov 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
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

As original<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ly discussed in https://discourse.slicer.org/t/slicer-has-caught-an-application-error-suggested-report-location/26058, an application error display says to report at https://slicer.org, but it is unclear where to go from there. Slicer Documentation? Discourse? GitHub? 

https://github.com/Slicer/Slicer/blob/bcedcfc48d453051165ddbd46305c495262db875/Base/QTGUI/qSlicerApplication.cxx#L493-L496

## Possible Solutions

@pieper suggested linking to https://slicer.readthedocs.io/en/latest/user_guide/get_help.html which works for Slicer, but likely too Slicer specific for a custom application which may want to point to its own documentation about reporting issues.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
