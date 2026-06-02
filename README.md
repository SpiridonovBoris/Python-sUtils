# Python-sUtils
A collection of syntactic sugar functions for Python

# Install
Add the following line to your ~/.bashrc:
```bash
# sUtils
if [ -d "${HOME}/Path/to/the/directory/containing/the/sUtils.py" ]; then
    PATH="${HOME}/Path/to/the/directory/containing/the/sUtils.py:${PATH}"
    PYTHONPATH="${HOME}/Path/to/the/directory/containing/the/sUtils.py:${PYTHONPATH}"
fi
```

# Usage
## As a Library
After the shebang, add the following line at the beginning of your Python script:
```Python
import sUtils
```
