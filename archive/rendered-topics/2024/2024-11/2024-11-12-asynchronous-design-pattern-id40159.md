# Asynchronous design pattern

**Topic ID**: 40159
**Date**: 2024-11-12
**URL**: https://discourse.slicer.org/t/asynchronous-design-pattern/40159

---

## Post #1 by @JASON (2024-11-12 20:55 UTC)

<p>Hello, I am developing UI for a few tasks in 3D Slicer that take a while to execute (remote database query, or some local compute task).</p>
<p>What are some common design patterns for handling these tasks in an asynchronous manner, where the call is initiated by some QT widget and I want to avoid locking the main thread while I wait for the task to complete.  Are there some 3D Slicer-specific conventions for this, or using python threading / QThread / QProcess / QTimer / some other method? Any recommendations for code examples demonstrating best-practices?</p>

---

## Post #2 by @pieper (2024-11-13 14:50 UTC)

<p>Hi Jason -</p>
<p>All the things you mentioned are possibilities.  The classic method in Slicer is the CLI module, which wraps a simple executable or specially compiled library to run in a separate process or thread and pass data back and forth to Slicer.  There’s a simple C++ template to follow and the GUI is generated automatically.  The GUI is somewhat simplistic, and the data type handled are limited, but it’s robust and simple.  Often people use a CLI for the heavy processing and write a custom python GUI (e.g. see CropVolume).</p>
<p>Another option I like is QProcess, which is wrapped in <a href="https://github.com/pieper/SlicerParallelProcessing">this extension</a> for spawning worker processes. This approach is used in the DICOM module to have an asynchronous “Listener” that communicates when it receives data from a DICOM push.</p>
<p>Native Python threading doesn’t work so well due to the GIL, but we did add GIL unlocking to SimpleFilters for long-running C++ code and it seems to work well.</p>
<p>In the WebServer, the QProcessNotifier is essential for mixing web transactions with the native GUI event loop.  This requires some state management but works well.  OpenIGTLink also integrates external data streams with the GUI, but with a slightly different approach.</p>
<p>So in the end a lot depends on what you are trying to do, what language you want to use, etc.</p>

---

## Post #3 by @JASON (2024-11-13 19:49 UTC)

<p>Steve, thanks so much for the helpful information. I’ve lost a couple of days to unfruitful experiments with this so appreciate the guidance.</p>
<p>For my case, I’m developing a python extension with several different use-cases for asynchronous calls. I like the idea of writing these as python code with argparse allowing for direct calls or via CLI.</p>
<p>Here’s a minimal working example, where I use a very basic script “<strong>CLI.py</strong>” that process over certain amount of time and reports progress via stdout, then returns some data (as you do in SlicerParallelProcessing).</p>
<pre><code class="lang-auto">import argparse
import sys
import time
import json

#--- example CLI function
def exampleJob(numsec, update_interval, isCLI=False):
    progress_values = []

    # Progress reporting
    start_time = time.time()
    while True:
        elapsed = time.time() - start_time
        progress = min(1.0, elapsed / numsec)
        progress_values.append(progress)
        print(f'PROGRESS {progress:.2f}')
        sys.stdout.flush()  # Ensure progress output is flushed immediately
        if progress &gt;= 1.0:
            break
        time.sleep(update_interval)

    # Mark completion and flush immediately
    print('COMPLETE')
    sys.stdout.flush()

    # Prepare output data
    output = {
        'total_seconds': numsec,
        'update_interval': update_interval,
        'progress_values': progress_values
    }

    # Output JSON data after 'COMPLETE' to avoid confusion, and flush immediately
    if isCLI:
        json_output = json.dumps(output)
        print(json_output)
        sys.stdout.flush()
    else:
        return output

# CLI Python script
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI for long-running operation with progress updates.")
    parser.add_argument('--numsec', type=int, required=True, help='Number of seconds to wait.')
    parser.add_argument('--updateInterval', type=float, required=True, help='Interval at which to provide progress updates.')
    args = parser.parse_args()

    exampleJob(args.numsec, args.updateInterval, isCLI=True)

</code></pre>
<p>Then I have my UI code that calls this via QProcess. I use a convention to differentiate the progress output from the final data output at the end.</p>
<pre><code class="lang-auto">import os
import sys
import qt
import slicer
import vtk
import json

class AsyncCLITest:
    def __init__(self):
        # Create a simple UI
        self.widget = qt.QWidget()
        self.layout = qt.QVBoxLayout()
        self.widget.setLayout(self.layout)

        self.startButton = qt.QPushButton("Run CLI Process")
        self.progressBar = qt.QProgressBar()
        self.progressBar.setRange(0, 100)
        self.progressBar.setValue(0)

        self.layout.addWidget(self.startButton)
        self.layout.addWidget(self.progressBar)
        self.widget.show()

        # Connect button to the start process method
        self.startButton.clicked.connect(self.runCLIProcess)

        # Set up the QProcess
        self.process = qt.QProcess()
        self.process.setProcessChannelMode(qt.QProcess.MergedChannels)
        self.process.readyReadStandardOutput.connect(self.onUpdate)
        self.process.finished.connect(self.onComplete)
        self.process.readyReadStandardError.connect(self.onError)

        # Buffer for accumulating process output
        self.output_buffer = b""

    def runCLIProcess(self):
        """Start the CLI script in a non-blocking way using QProcess."""
        CLIpath = r"CLI.py"
        python_executable = sys.executable  # Path to the current Python executable

        # Set arguments for the process
        numsec = "10"  # Duration of the process
        update_interval = "0.5"  # Update interval for progress

        # Start the process and log the command for debugging
        self.process.start(python_executable, [CLIpath, "--numsec", numsec, "--updateInterval", update_interval])
        self.startButton.setEnabled(False)
        self.progressBar.setValue(0)

    def onUpdate(self):
        """Read and process the standard output from the QProcess."""
        while self.process.canReadLine():
            output_line = self.process.readLine().data().decode('utf-8', errors='ignore').strip()
            print(f"Received output line: {output_line}")  # Diagnostic: print each received line
            if output_line.startswith("PROGRESS"):
                progress_value = float(output_line.split()[1]) * 100
                self.progressBar.setValue(int(progress_value))
            else:
                self.output_buffer += output_line.encode('utf-8') + b'\n'

    def onError(self):
        """Read and print error messages from the QProcess."""
        while self.process.canReadLine():
            error_line = self.process.readLine().data().decode('utf-8', errors='ignore').strip()
            print(f"Error output: {error_line}")

    def onComplete(self):
        """Handle the process completion and read the final JSON data."""
        self.startButton.setEnabled(True)
        self.progressBar.setValue(100)

        # Separate text data from binary
        marker = self.output_buffer.find(b'COMPLETE')
        if marker != -1:
            # Skip past the 'COMPLETE' marker and any newlines
            json_data_start = marker + len(b'COMPLETE')
            json_data = self.output_buffer[json_data_start:].lstrip()

            # Check if the JSON data is empty or malformed
            if not json_data:
                return
        else:
            return

        # Deserialize JSON data
        try:
            output = json.loads(json_data.decode('utf-8'))
            print("Received JSON output:")
            print(json.dumps(output, indent=4))
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Error deserializing JSON data: {e}")

# Create and show the UI
testApp = AsyncCLITest()

</code></pre>
<p>Does this look reasonable?<br>
This is working for me after much noodling, but I’m open to recommendations to make more robust, or possibly abstract the call for many possible CLI scripts that use the same conventions.</p>

---

## Post #4 by @pieper (2024-11-15 21:58 UTC)

<p>Hi Jason -</p>
<p>Yes, that looks reasonable.  With this approach you have the option to have multiple back-and-forth communications with the external process and can pass data back and forth using stdin/stdout.  It can be very useful for offloading tasks to dedicated processes and isolate the main app (e.g. if you are debugging code that may crash).  Also you can launch the subprocess through ssh to use a dedicated compute server if that fits your use case.</p>
<p>Cheers,<br>
Steve</p>

---
