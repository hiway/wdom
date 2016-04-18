#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wdom.tag import NewTagClass as NewTag
from wdom.tag import *


css_files = [
    'https://cdn.jsdelivr.net/foundation/6.2.1/foundation.min.css',
]

js_files = [
    'https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js',
    'https://cdn.jsdelivr.net/foundation/6.2.1/foundation.min.js',
]

headers = []

Button = NewTag('Button', bases=Button, class_='button')
DefaultButton = NewTag('DefaultButton', 'button', Button, class_='hollow secondary')
PrimaryButton = NewTag('PrimaryButton', 'button', Button)
SuccessButton = NewTag('SuccessButton', 'button', Button, class_='success')
InfoButton = NewTag('InfoButton', 'button', Button, class_='success hollow')
WarningButton = NewTag('WarningButton', 'button', Button, class_='warning')
DangerButton = NewTag('DangerButton', 'button', Button, class_='alert')
LinkButton = NewTag('LinkButton', 'button', Button, class_='hollow')

Row = NewTag('Row', 'div', Row, class_='row')
Col = NewTag('Col', 'div', Col, class_='columns')
Col1 = NewTag('Col1', 'div', Col, class_='small-1 medium-1 large-1')
Col2 = NewTag('Col2', 'div', Col, class_='small-2 medium-2 large-2')
Col3 = NewTag('Col3', 'div', Col, class_='small-3 medium-3 large-3')
Col4 = NewTag('Col4', 'div', Col, class_='small-4 medium-4 large-4')
Col5 = NewTag('Col5', 'div', Col, class_='small-5 medium-5 large-5')
Col6 = NewTag('Col6', 'div', Col, class_='small-6 medium-6 large-6')
Col7 = NewTag('Col7', 'div', Col, class_='small-7 medium-7 large-7')
Col8 = NewTag('Col8', 'div', Col, class_='small-8 medium-8 large-8')
Col9 = NewTag('Col9', 'div', Col, class_='small-9 medium-9 large-9')
Col10 = NewTag('Col10', 'div', Col, class_='small-10 medium-10 large-10')
Col11 = NewTag('Col11', 'div', Col, class_='small-11 medium-11 large-11')
Col12 = NewTag('Col12', 'div', Col, class_='small-12 medium-12 large-12')
