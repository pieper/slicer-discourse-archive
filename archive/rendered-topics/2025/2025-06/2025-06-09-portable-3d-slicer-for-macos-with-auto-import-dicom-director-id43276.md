# Portable 3D Slicer for macOS with Auto-Import DICOM Directory

**Topic ID**: 43276
**Date**: 2025-06-09
**URL**: https://discourse.slicer.org/t/portable-3d-slicer-for-macos-with-auto-import-dicom-directory/43276

---

## Post #1 by @Wyatt_Gray (2025-06-09 19:42 UTC)

<p><strong>Introduction</strong>:<br>
I’m an engineer and have been tasked with sharing a patient’s DICOM dataset with a macOS-based Dr. (expert). The imaging location provided a DICOM directory and an application but users report errors opening the exported media/application (e.g., crashes, “cannot open” messages). This is something I experience quite frequently and I would like to simply this.</p>
<p><strong>Objective</strong>:<br>
Create a self-contained macOS and Windows package that includes 3D Slicer and a DICOM directory (that I receive from imaging locations) where the user can download slicer from the folder and launching Slicer automatically imports and loads all valid DICOM series (e.g., CT/MRI, segmentations if present) from the directory into the scene, with visibility enabled, requiring no user interaction (e.g., no manual DICOM import or load steps).</p>
<p><strong>Folder Structure</strong>:</p>
<pre><code class="lang-auto">PATIENT IMAGING/
  ├── DICOM_INFO/ (*.dcm files)
  ├── Slicer.app/ (extracted from Slicer-5.8.1-macosx-amd64.dmg)
  └── README.txt
</code></pre>
<p><strong>Requirements</strong>:</p>
<ul>
<li><strong>Auto-Import</strong>: On Slicer launch, the <code>DICOM_INFO</code> directory is scanned, valid series are imported into the DICOM database, and loaded into the scene without user input.</li>
<li><strong>Error Handling</strong>: Common DICOM errors (e.g., “Invalid DICOM file,” “Missing metadata”) are handled silently, loading only valid data.</li>
<li><strong>Visibility</strong>: All loaded data (e.g., volumes, segmentations) is visible by default (eye icons enabled in Subject Hierarchy).</li>
<li><strong>Portability</strong>: Package includes <code>Slicer.app</code> and any required extensions (e.g., QuantitativeReporting for segmentations) offline, with no external downloads.</li>
<li><strong>macOS Compatibility</strong>: Supports Ventura/Sonoma, Intel/ARM, with macOS security warnings handled (e.g., Gatekeeper bypass instructions).</li>
<li><strong>HIPAA Compliance</strong>: Assumes anonymized DICOM files; package remains offline.</li>
</ul>
<p><strong>Questions</strong>:</p>
<ol>
<li>Does Slicer 5.8.1 have a built-in feature or configuration to auto-import a DICOM directory on launch and load all series into the scene?</li>
<li>Can a Python script automate this process (e.g., using <code>slicer.modules.dicom</code> to scan <code>DICOM_INFO</code> and load series)? If so, please share an example script or reference.</li>
</ol>
<p><strong>Additional Info</strong>:</p>
<ul>
<li>DICOM data likely includes CT/MRI; segmentations/RT objects possible but unconfirmed.</li>
<li>Anonymized sample DICOM files can be shared via secure link if needed.</li>
<li>Solution must minimize user interaction for non-technical macOS and Windows users.</li>
</ul>
<p><strong>Request</strong>:<br>
Seeking confirmation of an existing Slicer 5.8.1 feature or a script/workflow to create a portable macOS package that auto-imports and displays <code>DICOM_INFO</code> data on launch. Example scripts, configuration steps, or extension bundling instructions are appreciated. Willing to test solutions and provide feedback.</p>
<p>Thank you,<br>
Wyatt<br>
<a href="mailto:wyatt@earpengineering.com">wyatt@earpengineering.com</a></p>

---

## Post #2 by @pieper (2025-06-09 20:43 UTC)

<p>Hi - welcome. This all sounds very feasible with a (fairly) simple python script.  I don’t see anything on your list that doesn’t already exist, so it would just be a matter of putting the pieces together and iterating to make the behavior comfortable for your target users.</p>
<p>Are you able to make your solution open source?</p>

---

## Post #3 by @ctrueden (2025-06-10 14:01 UTC)

<p>The <a href="https://fiji.sc/" rel="noopener nofollow ugc">Fiji</a> project recently switched to a new launcher I’ve been developing called <a href="https://github.com/apposed/jaunch#readme" rel="noopener nofollow ugc">Jaunch</a>. It is designed to provide portable cross-platform launching, including a <a href="https://github.com/apposed/jaunch/blob/main/doc/MACOS.md#code-signing" rel="noopener nofollow ugc">code-signed+notarized</a> immutable .app bundle for macOS. It can be configured via TOML files to launch either Python or Java code (in this case probably a Python script). This could maybe be useful as the bootstrapping piece of a portable 3D Slicer bundle like this, to pass Gatekeeper including overcoming <a href="https://github.com/apposed/jaunch/blob/main/doc/MACOS.md#path-randomization" rel="noopener nofollow ugc">Path Randomization</a>.</p>

---
