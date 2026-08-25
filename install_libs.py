"""
Running this file should automatically install necessary libraries on
all Windows and MacOS systems. It will not work on most Linux systems
where users should install the 4 libraries below through their
package manager.
"""

import sys, subprocess
subprocess.run([
  sys.executable, 
  '-m', 'pip', 'install', '--user', 
  'pillow', 'pytest', 'requests', 'rich'
])
