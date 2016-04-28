#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wdom.tag import NewTagClass as NewTag
from wdom.tag import *

name = 'Blaze'
project_url = 'http://blazecss.com/'
project_repository = 'https://github.com/BlazeCSS/blaze'
license = 'MIT License'
license_url = 'https://github.com/BlazeCSS/blaze/blob/master/LICENSE'

css_files = [
    '//cdn.jsdelivr.net/blazecss/latest/blaze.min.css',
]

Button = NewTag('Button', bases=Button, class_='button')
DefaultButton = NewTag('DefaultButton', 'button', Button, class_='button--default', is_='default-button')
PrimaryButton = NewTag('PrimaryButton', 'button', Button, class_='button--primary', is_='primary-button')
SecondaryButton = NewTag('SecondaryButton', 'button', Button, class_='button--secondary', is_='secondary-button')
SuccessButton = NewTag('SuccessButton', 'button', Button, class_='button--success', is_='success-button')
InfoButton = NewTag('InfoButton', 'button', Button, class_='button--primary', is_='info-button')
WarningButton = NewTag('WarningButton', 'button', Button, class_='button--secondary', is_='warining-button')
DangerButton = NewTag('DangerButton', 'button', Button, class_='button--error', is_='danger-button')
ErrorButton = NewTag('ErrorButton', 'button', Button, class_='button--error', is_='error-button')
LinkButton = NewTag('LinkButton', 'button', Button, is_='link-button')

Input = NewTag('Input', 'input', Input, class_='field')
TextInput = NewTag('TextInput', 'input', TextInput, class_='field')
Textarea = NewTag('Textarea', 'textarea', Textarea, class_='field')
Select = NewTag('Select', 'select', Select, class_='choice')

Ul = NewTag('Ul', 'ul', Ul, class_='list')
Ol = NewTag('Ol', 'ol', Ol, class_='list--ordered')
Li = NewTag('Li', 'li', Li, class_='list__item')

Table = NewTag('Table', 'table', Table, class_='table')
Tr = NewTag('Tr', 'tr', Tr, class_='table__row')
Th = NewTag('Th', 'th', Th, class_='table__cell')
Td = NewTag('Td', 'td', Td, class_='table__cell')

H1 = NewTag('H1', 'div', H1, class_='heading heading--super')
H2 = NewTag('H2', 'div', H2, class_='heading heading--xlarge')
H3 = NewTag('H3', 'div', H3, class_='heading heading--large')
H4 = NewTag('H4', 'div', H4, class_='heading heading--medium')
H5 = NewTag('H5', 'div', H5, class_='heading heading--small')
H6 = NewTag('H6', 'div', H6, class_='heading heading--xsmall')

Row = NewTag('Row', 'div', Row, class_='gird')
Col = NewTag('Col', 'div', Col, class_='grid__cell')
Col1 = NewTag('Col1', 'div', Col, class_='grid__cell--width-10', is_='col1')
Col2 = NewTag('Col2', 'div', Col, class_='grid__cell--width-15', is_='col2')
Col3 = NewTag('Col3', 'div', Col, class_='grid__cell--width-25', is_='col3')
Col4 = NewTag('Col4', 'div', Col, class_='grid__cell--width-33', is_='col4')
Col5 = NewTag('Col5', 'div', Col, class_='grid__cell--width-40', is_='col5')
Col6 = NewTag('Col6', 'div', Col, class_='grid__cell--width-50', is_='col6')
Col7 = NewTag('Col7', 'div', Col, class_='grid__cell--width-60', is_='col7')
Col8 = NewTag('Col8', 'div', Col, class_='grid__cell--width-66', is_='col8')
Col9 = NewTag('Col9', 'div', Col, class_='grid__cell--width-75', is_='col9')
Col10 = NewTag('Col10', 'div', Col, class_='grid__cell--width-85', is_='col10')
Col11 = NewTag('Col11', 'div', Col, class_='grid__cell--width-90', is_='col11')
Col12 = NewTag('Col12', 'div', Col, class_='grid__cell--width-100', is_='col12')

extended_classes = [
    Button,
    DefaultButton,
    PrimaryButton,
    SecondaryButton,
    SuccessButton,
    InfoButton,
    WarningButton,
    DangerButton,
    ErrorButton,
    LinkButton,
    Input,
    TextInput,
    Textarea,
    Select,
    Ul,
    Ol,
    Li,
    Table,
    Tr,
    Th,
    Td,
    H1,
    H2,
    H3,
    H4,
    H5,
    H6,
    Row,
    Col,
    Col1,
    Col2,
    Col3,
    Col4,
    Col5,
    Col6,
    Col7,
    Col8,
    Col9,
    Col10,
    Col11,
]
