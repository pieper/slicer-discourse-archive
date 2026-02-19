---
topic_id: 29002
title: "I Wrote A Python Extension How To Automatically Install The"
date: 2023-04-19
url: https://discourse.slicer.org/t/29002
---

# I wrote a python extension, how to automatically install the extension by python?

**Topic ID**: 29002
**Date**: 2023-04-19
**URL**: https://discourse.slicer.org/t/i-wrote-a-python-extension-how-to-automatically-install-the-extension-by-python/29002

---

## Post #1 by @derekcbr (2023-04-19 09:03 UTC)

<p>Below seems not to work.</p>
<pre><code class="lang-auto">import slicer
import os

# Path to your extension .py file
extension_file = "/path/to/YourExtension.py"

# Check if the extension is already installed
installed_extensions = slicer.app.extensionsManagerModel().installedExtensions()
if any(ext.name == "YourExtension" for ext in installed_extensions):
    print("YourExtension is already installed.")
else:
    # Install the extension
    slicer.app.extensionsManagerModel().installExtension(extension_file)
    print("YourExtension has been installed.")

# Enable the extension (optional)
extension_metadata = slicer.app.extensionsManagerModel().retrieveExtensionMetadataByName("YourExtension")
if extension_metadata:
    extension_id = extension_metadata["id"]
    slicer.app.extensionsManagerModel().setExtensionEnabled(extension_id, True)
    print("YourExtension has been enabled.")
</code></pre>

---

## Post #2 by @lassoan (2023-04-20 04:32 UTC)

<p>If you don’t want to build an extension package (because that would require you to build Slicer, or you need to carefully build an extension package zip file manually), then probably the simplest is to copy your .py file into a scripted module folder in Slicer.</p>
<p>If you want to keep your code better separated from Slicer then you can load it on-the-fly or add it to the additional module paths using Python scripting as it is shown <a href="https://github.com/Slicer/Slicer/blob/d1e0b86069aa6926b13c5aaf6f649577c75c1a00/Modules/Scripted/ExtensionWizard/ExtensionWizard.py#L357-L408">here</a>.</p>
<p>In recent Slicer Preview Releases you can just drag-and-drop the .py file to the application window to load/install it.</p>

---

## Post #3 by @derekcbr (2023-04-20 04:37 UTC)

<p>Thank you for the reply! It is installed through settings–Modules–Additional module paths. For this kind of Python extension, is it possible to install automatically by Python script? Thanks a lot!</p>

---
