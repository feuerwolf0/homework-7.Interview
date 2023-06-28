# -*- coding: utf-8 -*-
from main import sequence_check, Stack
import pytest


params = [
    ('(((([{}]))))', 'Строка сбалансирована'),
    ('[([])((([[[]]])))]{()}', 'Строка сбалансирована'),
    ('{{[()]}}', 'Строка сбалансирована'),
    ('}{}', 'Строка не сбалансирована'),
    ('{{[(])]}}', 'Строка не сбалансирована'),
    ('[[{())}]', 'Строка не сбалансирована'),
    ('((d(ffd(gggg[{dfffddf}56565])ff)))3434', 'Строка сбалансирована'),
    ('[(sssdw[])egewg(((geed[[[gwgewgwege]]])54545))]fefe{(44)53535}', 'Строка сбалансирована'),
    ('@[[gegwegwe{(ggwegewg)3432424)}!!!gewgwgwg]', 'Строка не сбалансирована')
]


@pytest.mark.parametrize('input, result', params)
def test_sequence_check(input, result):
    stack = Stack()
    assert sequence_check(stack, input) == result, 'Тест не пройден'