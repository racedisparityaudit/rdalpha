import csv
from model.Taxonomy import Taxonomy
from model.Uri import Uri
from model.Pages import Page, TierOnePage, TierTwoPage, TierThreePage, DataPage, Homepage

input_file = ''

class TaxonomyImporter(object):

    def __init__(self, input_file):
        self.input_file = input_file

    """
    Create a tier 1 page
    (e.g. Home > Education)
    """

    def build_tier_1_page(self, tier_1_page, all_tier_2_nodes):
        tier_2_children = [node for node in all_tier_2_nodes if node.is_child_of(tier_1_page)]

        return TierOnePage(uri=tier_1_page.uri,
                           name=tier_1_page.name,
                           description=tier_1_page.description,
                           tier_2_pages=tier_2_children)


    """
    Create a tier 2 page
    (e.g. Home > Education > Attainment)
    """

    def build_tier_2_page(self, tier_2_page, all_tier_3_nodes):
        tier_3_children = [node for node in all_tier_3_nodes if node.is_child_of(tier_2_page)]

        return TierTwoPage(uri=tier_2_page.uri,
                           name=tier_2_page.name,
                           description=tier_2_page.description,
                           tier_3_pages=tier_3_children)


    """
    Create a tier 3 page
    (e.g. Home > Education > Attainment > KS4)
    """

    def build_tier_3_page(self, tier_3_page, all_question_nodes):
        question_children = [node for node in all_question_nodes if node.is_child_of(tier_3_page)]

        return TierThreePage(uri=tier_3_page.uri,
                             name=tier_3_page.name,
                             description=tier_3_page.description,
                             data_pages=question_children)


    """

    """

    def import_taxonomy(self):
        self.nodes = self.read_nodes()

        #
        tier_1 = [node for node in self.nodes if node.level == 'T1']
        tier_2 = [node for node in self.nodes if node.level == 'T2']
        tier_3 = [node for node in self.nodes if node.level == 'T3']
        data_landing_pages = [node for node in self.nodes if node.level == 'T4']
        measures = [node for node in self.nodes if node.level == 'Measure']
        slices = [node for node in self.nodes if node.level == 'Slice']

        taxonomy = Taxonomy()
        taxonomy.homepage = Homepage(tier_1)
        taxonomy.tier_1 = [self.build_tier_1_page(tier_1_page, tier_2) for tier_1_page in tier_1]
        taxonomy.tier_2 = [self.build_tier_2_page(tier_2_page, tier_3) for tier_2_page in tier_2]
        taxonomy.tier_3 = [self.build_tier_3_page(tier_3_page, data_landing_pages) for tier_3_page in tier_3]
        taxonomy.data_landing_pages = []
        taxonomy.measures = []
        taxonomy.slices = []

        return taxonomy


    def read_nodes(self):
        nodes = []
        with open(self.input_file, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)

            for row in csv_reader:
                uri = Uri(tier_1=row[3],
                          tier_2=row[4],
                          tier_3=row[5])
                nodes.append(Page(uri=uri,
                                  name=row[0],
                                  level=row[2],
                                  description=row[1]))
        return nodes
