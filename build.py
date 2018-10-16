import subprocess
import os
import sys

cwd = os.getcwd()
try:
    os.chdir('docs')
    subprocess.check_call(['make', 'html'])
except Exception as e:
    print('error while making docs:', e, file=sys.stderr)
finally:
    os.chdir(cwd)

try:
    doc_text = open('cofan/cofan.py').read().split("'''", 2)[1]
    tutorial_text = '''
    --------
    Tutorial
    --------
    Check out cofan tutorial at http://cofan.readthedocs.io/
    '''
    
    tutorial_text = '\n'.join([c.strip() for c in tutorial_text.splitlines()])
    
    readme_text = doc_text.lstrip() + tutorial_text

    with open('README.txt', 'w') as f:
        print(readme_text, file=f)
except Exception as e:
    print('error while writing README.txt:', e, file=sys.stderr)

subprocess.check_call(['python', 'setup.py', 'sdist'])
