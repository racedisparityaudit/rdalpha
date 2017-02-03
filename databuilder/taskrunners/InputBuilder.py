import csv, os, jsonpickle, json
from faker import Factory

from model.Pages import Page, Taxonomy, Homepage, TierOnePage, TierTwoPage, TierThreePage

class InputBuilder(object):

    output_directory = ""
    input_directory = ""
    nodes = []
    fake = Factory.create()

    """
    Create a taskrunner with an input directory and output directory
    At minimum input_directory should contain taxonomy.csv
    """
    def __init__(self, input_directory, output_directory):
        self.input_directory = input_directory
        self.output_directory = output_directory

    """
    Create a tier 1 page
    (e.g. Home > Education)
    """
    def build_tier_1_page(self, tier_1_page, all_tier_2_nodes):

        tier_2_children = [node for node in all_tier_2_nodes if node.uri.startswith(tier_1_page.uri)]

        return TierOnePage(uri=tier_1_page.uri,
                           name=tier_1_page.name,
                           description=tier_1_page.description,
                           tier_2_pages=tier_2_children,
                           taxonomy=tier_1_page.taxonomy)

    """
    Create a tier 2 page
    (e.g. Home > Education > Attainment)
    """
    def build_tier_2_page(self, tier_2_page, all_tier_3_nodes):

        tier_3_children = [node for node in all_tier_3_nodes if node.uri.startswith(tier_2_page.uri)]

        return TierTwoPage(uri=tier_2_page.uri,
                           name=tier_2_page.name,
                           description=tier_2_page.description,
                           tier_3_pages=tier_3_children,
                           taxonomy=tier_2_page.taxonomy)

    """
    Create a tier 3 page
    (e.g. Home > Education > Attainment > KS4)
    """
    def build_tier_3_page(self, tier_3_page, all_question_nodes):

        question_children = [node for node in all_question_nodes if node.uri.startswith(tier_3_page.uri)]

        return TierThreePage(uri=tier_3_page.uri,
                             name=tier_3_page.name,
                             description=tier_3_page.description,
                             data_landing_pages=question_children,
                             taxonomy=tier_3_page.taxonomy)


    """
    Save a page in pretty json format
    File is created at the path [output_root_directory]/[page.uri]/data.json
    """
    def pretty_save_page(self, output_root_directory, page):
        try:
            os.mkdir(output_root_directory + page.uri)
        except:
            pass

        try:
            json_value = jsonpickle.dumps(page, unpicklable=False)
            obj_value = json.loads(json_value)
            with open(output_root_directory + page.uri + "/data.json", 'w') as data_file:
                json.dump(obj_value, data_file, sort_keys=True,
                          indent=4, separators=(',', ': '))

        except:
            print("Could not print to " + page.uri)

    """
    """
    def build(self):
        self.nodes = self.read_nodes()

        #
        tier_1 = [node for node in self.nodes if node.level == 'T1']
        tier_2 = [node for node in self.nodes if node.level == 'T2']
        tier_3 = [node for node in self.nodes if node.level == 'T3']
        tier_4 = [node for node in self.nodes if node.level == 'T4']
        measures = [node for node in self.nodes if node.level == 'Measure']


        homepage = Homepage(tier_1)
        tier_1_pages = [self.build_tier_1_page(tier_1_page, tier_2) for tier_1_page in tier_1]
        tier_2_pages = [self.build_tier_2_page(tier_2_page, tier_3) for tier_2_page in tier_2]
        tier_3_pages = [self.build_tier_3_page(tier_3_page, tier_4) for tier_3_page in tier_3]

        self.save(homepage, tier_1_pages, tier_2_pages, tier_3_pages)

    def save(self, homepage, tier_1_pages, tier_2_pages, tier_3_pages):
        self.pretty_save_page(self.output_directory, homepage)
        [self.pretty_save_page(self.output_directory, tier_1_page) for tier_1_page in tier_1_pages]
        [self.pretty_save_page(self.output_directory, tier_2_page) for tier_2_page in tier_2_pages]
        [self.pretty_save_page(self.output_directory, tier_3_page) for tier_3_page in tier_3_pages]

    def read_nodes(self):
        nodes = []
        with open(self.input_directory + '/taxonomy.csv', 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                taxonomy=Taxonomy(tier_1=row[3],
                                  tier_2=row[4],
                                  tier_3=row[5])
                nodes.append(Page(uri=taxonomy.uri,
                                  name=row[0],
                                  level=row[2],
                                  description=row[1],
                                  taxonomy=taxonomy))
        return nodes


