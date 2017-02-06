import csv
from taskrunners.TaxonomyImporter import TaxonomyImporter
from model.Taxonomy import Taxonomy

class CsvStructureBuilder(object):

    output_csv_file = ""
    input_file = ""

    """
    Create a taskrunner with an input file and output file
    At minimum input_directory should contain taxonomy.csv and datasets.csv
    """
    def __init__(self, input_file, output_csv_file):
        self.input_file = input_file
        self.output_csv_file = output_csv_file

    """
    Build a csv structure
    """
    def build(self):
        taxonomyImporter = TaxonomyImporter(self.input_file)
        taxonomy = taxonomyImporter.import_taxonomy()

        self.save_as_csv(taxonomy, self.output_csv_file)

    """
    Save as a csv file
    """
    def save_as_csv(self, taxonomy: Taxonomy, filename: str):

        with open(filename, 'w') as f:
            writer = csv.writer(f)

            headers = ["name", "parent name", "uri", "parent uri", "description", "level"]
            writer.writerow(headers)

            writer.writerow(self.csv_row_for_home_page(taxonomy))
            writer.writerows(self.csv_rows_for_tier_1(taxonomy))
            writer.writerows(self.csv_rows_for_tier_2(taxonomy))
            writer.writerows(self.csv_rows_for_tier_3(taxonomy))

    def csv_row_for_home_page(self, taxonomy):
        page = taxonomy.homepage
        row = ["Homepage", "", "/", "", page.description]
        return row

    def csv_rows_for_tier_1(self, taxonomy):
        rows = []
        for page_uri in taxonomy.homepage.subpages:

            page = next(p for p in taxonomy.tier_1 if p.uri.full == page_uri['uri'])

            row = [page.name, taxonomy.homepage.name,
                   page.uri.full, taxonomy.homepage.uri.full,
                   page.description, page.level]
            rows.append(row)
        return rows


    def csv_rows_for_tier_2(self, taxonomy):
        rows = []
        for parent in taxonomy.tier_1:
            for page_uri in parent.subpages:
                page = next(p for p in taxonomy.tier_2 if p.uri.full == page_uri['uri'].full)
                row = [page.name, parent.name,
                       page.uri.full, parent.uri.full,
                       page.description, page.level]
                rows.append(row)
        return rows


    def csv_rows_for_tier_3(self, taxonomy):
        rows = []
        for parent in taxonomy.tier_2:
            for page_uri in parent.subpages:
                page = next(p for p in taxonomy.tier_3 if p.uri.full == page_uri['uri'].full)
                row = [page.name, parent.name,
                       page.uri.full, parent.uri.full,
                       page.description, page.level]
                rows.append(row)
        return rows