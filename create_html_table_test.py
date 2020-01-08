import pandas as pd
import numpy as np
import subprocess
import platform

from create_html_table import create_html_table

rng = pd.date_range('1/1/2011', periods=10, freq='H')
ts = pd.DataFrame(np.random.randn(len(rng)), index=rng)
ts.index.name = 'date'

ts.to_csv(path_or_buf='ts.csv', sep=';')

html_table = create_html_table('ts.csv')

# check if code is running in windows or macos
if platform.system() == "Windows":
    # create html file
    subprocess.run('type NUL > ts.html', shell=True)

    # open url in standard browser
    subprocess.run('start {0}'.format('ts.html'), shell=True)
else:
    # create html file
    subprocess.run('touch ts.html', shell=True)
    html_text = open('ts.html', 'w', encoding='utf-8')
    html_text.write(html_table)
    html_text.close()
    
    # open url in chrome
    subprocess.run('open -a "Google Chrome" {0}'.format('ts.html'), shell=True)

subprocess.run('rm ts.csv', shell=True)

