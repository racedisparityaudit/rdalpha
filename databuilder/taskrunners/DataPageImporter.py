import csv
from taskrunners.TaxonomyImporter import TaxonomyImporter
from model.Uri import Uri
from model.Pages import DataPage, Measure

class DataPageImporter(object):
    measures = []
    datapages = []

    def __init__(self, taxonomy_file, data_pages_file):
        self.data_pages_file = data_pages_file
        self.taxonomy_file = taxonomy_file

    def import_data_pages(self, filename):
        return filename

    def import_taxonomy(self):
        taxonomy_importer = TaxonomyImporter(self.taxonomy_file)
        self.taxonomy = taxonomy_importer.import_taxonomy()

        self.read_csv()
        self.add_measures_to_datapages()
        self.add_datapages_to_tier_3_pages()

        self.taxonomy.measures = self.measures
        self.taxonomy.tier_4 = self.datapages

        return self.taxonomy

    def add_measures_to_datapages(self):

        for datapage in self.datapages:
            children = [child for child in self.measures if child.is_child_of(datapage)]
            datapage.measures = [{'uri': measure.uri.full, 'name':measure.name}
                                 for measure in children]

    def add_datapages_to_tier_3_pages(self):
        for tier_3_page in self.taxonomy.tier_3:
            children = [child for child in self.datapages if child.is_child_of(tier_3_page)]
            tier_3_page.datapages = [{'uri': datapage.uri.full, 'name':datapage.name}
                                     for datapage in children]

    def read_csv(self):
        with open(self.data_pages_file, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            self.measures = []
            self.datapages = []

            next(csv_reader)
            for row in csv_reader:
                uri = Uri(tier_1=row[0],
                          tier_2=row[1],
                          tier_3=row[2],
                          tier_4=row[3])
                self.datapages.append(DataPage(uri=uri,name=row[3],
                                      question=row[4],
                                          department=row[5],
                                      measures=[]))

                uri = Uri(tier_1=row[0],
                          tier_2=row[1],
                          tier_3=row[2],
                          tier_4=row[3],
                          measure=row[6])
                self.measures.append(Measure(uri=uri,
                                        name=row[6],
                                        description=row[7],
                                        department=row[5]))