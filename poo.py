#!/usr/bin/env python3
# -*- coding: utf-8 -*-

history = '''Buy
35.0000
CCAR
$16.68
0.0368 BNB
$25.07
27/10/2021 23:49:57
0xdb76
Buy
523.0000
CCAR
$248.72
0.5135 BNB
$374.60
26/10/2021 17:44:14
0x7a53
Sell
25.0000
CCAR
$11.43
0.0236 BNB
$17.91
25/10/2021 21:02:33
0xdddd
Sell
50.0000
CCAR
$22.79
0.0473 BNB
$35.81
23/10/2021 16:29:37
0x01a3
Sell
42.4204
CCAR
$15.46
0.0309 BNB
$30.38
20/10/2021 21:04:38
0x9072
Sell
42.0000
CCAR
$13.50
0.0286 BNB
$30.08
18/10/2021 00:50:21
0xeb60
Sell
200.0000
CCAR
$64.24
0.1374 BNB
$143.25
14/10/2021 18:28:26
0x5ad8
Sell
7.5796
CCAR
$2.53
0.0055 BNB
$5.43
13/10/2021 18:04:28
0xd4fa
Sell
76.0000
CCAR
$24.57
0.0539 BNB
$54.43
13/10/2021 16:52:07
0x2879
Buy
620.0000
CCAR
$135.90
0.3879 BNB
$444.07
25/09/2021 18:21:36
0x62ab'''

import numpy as np


list_h = history.split('\n')

buys = []
sells = []
for i, item in enumerate(list_h):
    if item == 'Buy':
        buys.append(float(list_h[i+3].replace('$', '')))
    if item == 'Sell':
        sells.append(float(list_h[i+3].replace('$', '')))

dolarreal = 5.6
buyed_usd = np.sum(buys)
buyed_brl = buyed_usd * dolarreal

selled_usd = np.sum(sells)
selled_brl = selled_usd * dolarreal

diff_usd = selled_usd - buyed_usd


if diff_usd >= 0:
    label = 'Lucro'
else:
    label = 'Prejuízo'

print('Total comprado: ${:0.02f} (R${:0.02f})'.format(buyed_usd, buyed_usd * dolarreal))
print('Total vendido: ${:0.02f} (R${:0.02f})'.format(selled_usd, selled_usd * dolarreal))
print('{}: ${:0.02f} (R${:0.02f})'.format(label, diff_usd, diff_usd * dolarreal))
