# -*- coding: utf-8 -*-
import logging
import unittest
from collections import OrderedDict

from schleppy.json_utils import (convert_list, to_snake_case,
                                 to_camel_case, convert_dict)

logging.basicConfig()
log = logging.getLogger('logger')
log.setLevel(logging.DEBUG)


class TestModelUtils(unittest.TestCase):
    def setUp(self):
        log.info("==================================================")
        log.info("======   Test: %s, SetUp", self.id())
        log.info("==================================================")

    def tearDown(self):
        log.info("--------------------------------------------------")
        log.info("------   Test: %s, TearDown", self.id())
        log.info("--------------------------------------------------")

    def test_convert_dict(self):
        model = {'count_of_cats': 100, 'count_of_people': 10, 'is_valid': False}
        result = convert_dict(model, to_camel_case)
        self.assertEqual(result, {'countOfCats': 100, 'countOfPeople': 10, 'isValid': False})

    def test_convert_nested_dict(self):
        model = {'count_of_cats': 1,
                 'count_of_people': 2,
                 'is_valid': True,
                 'food_info': {
                     'number_of_cat_food_cans': 12,
                     'rotations_to_open': 3
                 }}
        result = convert_dict(model, to_camel_case)
        self.assertEqual(result,
                         {'countOfCats': 1, 'countOfPeople': 2, 'isValid': True,
                          'foodInfo': {'numberOfCatFoodCans': 12,
                                       'rotationsToOpen': 3}})

    def test_convert_nested_list(self):
        model = {'count_of_cats': 1,
                 'count_of_people': 2,
                 'is_valid': True,
                 'food_info': [{
                     'number_of_cat_food_cans': 12,
                     'rotations_to_open': 3
                 }]}
        result = convert_dict(model, to_camel_case)
        self.assertEqual(result,
                         {'countOfCats': 1, 'countOfPeople': 2, 'isValid': True,
                          'foodInfo': [{'numberOfCatFoodCans': 12,
                                        'rotationsToOpen': 3}]})

    def test_convert_list(self):
        # A list with mixed item types
        source = ['mix_list', [1, 2], {'countOfCats': 1, 'countOf_Dogs': 2}]
        result = convert_list(source, to_snake_case)
        # Expect the item with type dict will be converted to OrderedDict and
        # key will be converted to snake_case, item with other types keep intact
        self.assertEqual(result,
                         ['mix_list', [1, 2],
                          OrderedDict([('count_of_cats', 1),
                                       ('count_of_dogs', 2)])])


if __name__ == '__main__':
    unittest.main()
