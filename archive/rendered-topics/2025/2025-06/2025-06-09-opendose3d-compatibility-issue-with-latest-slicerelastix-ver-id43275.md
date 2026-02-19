---
topic_id: 43275
title: "Opendose3D Compatibility Issue With Latest Slicerelastix Ver"
date: 2025-06-09
url: https://discourse.slicer.org/t/43275
---

# OpenDose3D Compatibility Issue with Latest SlicerElastix Version (AttributeError on Registration)

**Topic ID**: 43275
**Date**: 2025-06-09
**URL**: https://discourse.slicer.org/t/opendose3d-compatibility-issue-with-latest-slicerelastix-version-attributeerror-on-registration/43275

---

## Post #1 by @Kumar_Abhishek (2025-06-09 19:42 UTC)

<p>Hi team,</p>
<p>I’m using OpenDose3D version <code>d73d832 (2025-01-12)</code> on Slicer 5.6, and facing an issue when executing the <strong>Registration</strong> step. Upon clicking <strong>Execute</strong> in the Registration tab, I get the following error:</p>
<pre><code class="lang-auto">AttributeError: module 'Elastix' has no attribute 'RegistrationPresets_ParameterFilenames'
</code></pre>
<p>I checked the available attributes in the <code>Elastix</code> module and indeed, <code>RegistrationPresets_ParameterFilenames</code> is missing. My installed version of <strong>SlicerElastix</strong> is <code>93c57ae (2025-01-18)</code>, which seems to have introduced this change.</p>
<p>Can you confirm if:</p>
<ul>
<li>OpenDose3D depends on a specific version of SlicerElastix?</li>
<li>There’s a recommended SlicerElastix version compatible with OpenDose3D <code>d73d832</code>?</li>
<li>Any workaround or patch is available for this?</li>
</ul>
<p>Thanks in advance!</p>

---
