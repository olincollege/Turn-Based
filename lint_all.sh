#!/bin/bash

find . -type f -name "*.py" | while read -r file; do
  # Extract the base file name without the directory structure
  base_name=$(basename "${file%.py}")

  # Create a unique log file name based on the base name
  log_file="pylint_${base_name}.log"

  # Run Pylint on the file and redirect output to the log file
  pylint "$file" > "$log_file" 2>&1

  # Optional: Print a message to indicate that the file has been linted
  echo "Linted $file, output to $log_file"

done