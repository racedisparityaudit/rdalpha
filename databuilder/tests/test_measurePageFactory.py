import unittest
from unittest import TestCase
from databuilder.factories.MeasurePageFactory import MeasurePageFactory
from databuilder.model.Page import MeasurePage

class TestMeasurePageFactory(TestCase):

    def test_build_measure_page_returns_measure_object(self):
        page = MeasurePageFactory().build_measure_page(file="test_data/example_t4.json")
        assert(isinstance(page, MeasurePage))

    def test_build_measure_page_loads_measure_object(self):
        page = MeasurePageFactory().build_measure_page(file="test_data/example_t4.json")

        self.assertEqual(page.name, "Attainment 8")
        self.assertEqual(page.measure_name, "Attainment8")
        self.assertEqual(page.uri, "education/progress/attainment8")

    def test_build_measure_page_loads_extra_data(self):
        page = MeasurePageFactory().build_measure_page(file="test_data/example_t4.json")

        self.assertEqual(page.first_published, "26/08/1978")
        self.assertEqual(page.last_updated, "26/08/2016")
        self.assertEqual(page.source, "Department for Education")
        self.assertEqual(page.introduction , "lorem ipsum")
        self.assertEqual(page.summary, "dolor non sequesit")


if __name__ == '__main__':
    unittest.main()