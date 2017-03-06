import json
from databuilder.model.Page import MeasurePage
from databuilder.model.Measure import MeasureSet
from databuilder.factories.MeasureSetFactory import MeasureSetFactory


class MeasurePageFactory(object):
    measure_set = MeasureSet()

    def __init__(self, data_file: str = ''):
        if data_file != '':
            self.measure_set = MeasureSetFactory().build_measure_set(data_file)

    def build_measure_page(self, file: str) -> MeasurePage:
        with open(file) as jsonfile:
            dict = json.load(jsonfile)
            page = MeasurePage(uri=dict['uri'], name=dict['name'], measure_name=dict['measure_name'])
            page = self.add_more_content(page, dict)
            return page
        return None

    def add_more_content(self,page, dict) -> MeasurePage:
        page.source = self.tricep(dict, 'source')
        page.last_updated = self.tricep(dict, 'last_updated')
        page.first_published = self.tricep(dict, 'first_published')
        page.introduction = self.tricep(dict, 'introduction')
        page.summary = self.tricep(dict, 'summary')
        page.download = self.tricep(dict, 'download')
        return page

    def add_data_content(self, page):
        data = self.measure_set.get_measure(page.measure_name)

    def tricep(self, dict, key, alternative = ''):
        try:
            return dict[key]
        except:
            return ''
