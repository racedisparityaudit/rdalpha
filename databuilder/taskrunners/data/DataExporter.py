import csv
from databuilder.model.Data import DataSeries, DataPoint


class DataCSVExporter(object):

    """
    We will work on the principle that these Series represent a data frame and
    so that we can assume an equal set of points for each series
    """
    def export_to_table(self, filename, serieses):

        series = serieses[0]
        headers = series.category_columns + [s.measure for s in serieses]

        with open(filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(headers)

            for i in range(0, len(serieses[0].points)):
                point = series.points[i]
                filter = dict()
                for j in range(0, len(series.category_columns)):
                    filter[series.category_columns[j]] = point.categories[j]

                categories = point.categories
                values = [s.find(filter).value for s in serieses]
                writer.writerow(categories + values)
                print("complete: " + str(i))
