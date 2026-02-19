---
topic_id: 35007
title: "Helper App To Manage Slicer Installations"
date: 2024-03-21
url: https://discourse.slicer.org/t/35007
---

# Helper app to manage slicer installations

**Topic ID**: 35007
**Date**: 2024-03-21
**URL**: https://discourse.slicer.org/t/helper-app-to-manage-slicer-installations/35007

---

## Post #1 by @pieper (2024-03-21 15:00 UTC)

<p>Here’s an idea people may want to comment on:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/7652">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/7652" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/7652" target="_blank" rel="noopener">"slicerizer" app to install and manage Slicer application versions</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-03-21" data-time="14:57:01" data-timezone="UTC">02:57PM - 21 Mar 24 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/pieper" target="_blank" rel="noopener">
          <img alt="pieper" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Priority: Medium
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          make-simple-things-simple
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Is your feature request related to a problem? Please describe.

As discusse<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">d in a recent dev meeting, a utility to manage downloads could be useful.  The current methods to install Slicer binaries require multiple user-actions and vary across platforms.  There is a lot of repetitive effort required, for example, to compare the behavior of an extension in, say, the stable and preview versions of Slicer on multiple platforms.

Here's a common current workflow on a fresh VM:
* install a browser
* go to download.slicer.org and click the correct button for your os / version choice
* open downloaded archive, (windows: run installer)
* launch slicer, go to extensions manager, seach and install each extension
* restart slicer
* repeat for each platform you want to test

## Describe the solution you'd like

A simple command that would download and install Slicer consistently across platforms.

Inspired by [this package that installs platform-specific executables via PyPi](https://pypi.org/project/s5cmd/), we could leverage pypi to distribute a program that performs the installation and manages executable paths.

Here's are some sample uses for bash (the exact command name is open for discussion).

### Install Slicerizer
```
pip install slicerizer
```

### install and run the latest stable
```
slicerizer install
Slicer
```
### install and run the latest preview
```
preview=$(slicerizer install --preview)
${preview}
```
### install and run the latest preview
```
preview=$(slicerizer install --preview)
${preview}
```
### install and run a specific version with extensions installed
```
slicer561=$(slicerizer install --version 5.6.1 --extensions SlicerDMRI,SlicerRT)
${slicer561}
```
### query the installed Slicer versions and their extensions 
```
slicerizer query --format json
[
  {"Version": "5.6.1",
   "InstallData": "2024-03-21",
   "Extensions": ["SlicerMorph", "MONAILabel"],
   "ExecPath": "/Users/pieper/app/Slicer-5.6.1.app/Contents/MacOS/Slicer"
  }
]
```

## Describe alternatives you've considered

We don't need to use pypi, but it seems convenient.  Instead we could provide a shell script for linux/mac and a .bat or powershell script for windows, but maintaining multiple versions would be a hassle.

Also this feature could be included in Slicer itself, so that once you've installed one version it helps you manage your isntallations of other versions.  But that wouldn't for installing a Slicer version on fresh VMs.

Depending on user feedback, we might also consider adding a GUI to select which Slicer to launch.

There are also lots of potentially useful command line options to consider adding:
* a command to update the preview or release if one is available
* an option to auto-launch when download and installation are complete'
* an option for windows to automate running the installer
* options to specify the installation directory
* options to save or not save the installer archive
* options to delete older versions
* options to query and list versions available for installation, and what extensions are available for them

Other name ideas:
* SlicerBuddy
* SlicerConfigurationManager
* slicer-apputil
* slicertool
* slicervalet

## Additional context

Use cases:
* Easy cross-platform cut-and-paste command to install a specific version of slicer
    * for recreating a debugging scenario
    * for quickly testing a feature of a preview build on multiple machines
    * for getting access to an older version where an extension is known to work
    * for using a specific version as part of an ongoing experiment
 * A graphical interface to pick among installed versions
 * An easy way to get the latest preview with bookmarked extensions auto-installed
 * A way for batch processing scripts to specify the required slicer and extensions without user interaction</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
