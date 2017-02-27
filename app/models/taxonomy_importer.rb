class TaxonomyImporter

  MEASURE_AVERAGE_PATH = Rails.root.join("./data/output/measure_averages.csv").to_s
  TOPIC_PATH           = Rails.root.join("./data/output/taxonomy.csv").to_s
  MEASURE_PATH         = Rails.root.join("./data/output/taxonomy.csv").to_s

  def import(path=nil)
    require 'csv'
    path ||= ENV["IMPORT_PATH"]
    path = Rails.root.join("./data/output/taxonomy.csv").to_s
    puts(ENV["IMPORT_PATH"])
    fail ArgumentError.new("import csv does not exist") unless File.exist?(path.to_s)

    taxonomy_csv = CSV.read(path, encoding: "ISO8859-1:utf-8")
    taxonomy_csv.shift

    import_topics
    import_measures
    TaxonomyLevel.delete_all

    taxonomy_csv.each{ |r| import_row r}

    measure_path =  Rails.root.join("./data/output/measure_averages.csv").to_s
    measure_csv = CSV.read(measure_path, encoding: "ISO8859-1:utf-8")
    measure_csv.shift

    MeasureAverage.delete_all
    measure_csv.each{ |r| import_measure_average r }
  end

  def import_measure_average(csv_row)
    taxonomy_id  = TaxonomyLevel.find_by_uri(csv_row[0]).id
    values = {
       uri:csv_row[0],
       subgroup_name:csv_row[1],
       group_name:csv_row[2],
       value:csv_row[3],
       national_value:csv_row[4],
       taxonomy_level_id: taxonomy_id

    }
    MeasureAverage.create(values)
  end

  def import_measures
    Measure.delete_all
    measure_csv = remove_headers MEASURE_PATH

    measure_csv.each do |m|
      import_measure(m)
    end
  end

  def import_measure(csv_row)
    if csv_row[5] == 'T4'
      Measure.create(name: csv_row.first,
        uri: csv_row.third,
        topic_id: get_topic_id_from_uri(csv_row.fourth),
        description: csv_row.fifth,
        source: csv_row[6],
        subtitle: csv_row[7],
        display: csv_row[8])
    end
  end

  def get_topic_id_from_uri(uri)
    Topic.find_by_uri(uri).try(:id)
  end


  def import_topics
    Topic.delete_all
    topic_csv = remove_headers TOPIC_PATH

    topic_csv.each do |t|
      import_topic(t)
    end
  end
  def import_topic(csv_row)
    unless csv_row[5] == 'T4'
      Topic.create(name: csv_row.first,
                  topic_id: get_topic_id_from_uri(csv_row.fourth),
                  description: csv_row.fifth,
                  uri: csv_row.third)
    end
  end

  def import_row(csv_row)

    taxonomy_name = csv_row.first

    parent_name = csv_row.second.try(:downcase)
    uri         = csv_row.third
    parent_uri  = csv_row.fourth
    description = csv_row.fifth
    taxonomy_level = csv_row[5]
    source = csv_row[6]
    subtitle = csv_row[7]
    _display = csv_row[8]


    parent_id = TaxonomyLevel.find_by_uri(parent_uri).id if parent_uri

    TaxonomyLevel.create(name: taxonomy_name.downcase,
                         level: taxonomy_level,
                         parent_id: parent_id,
                         uri: uri,
                         description: description,
                         source: source,
                         display: _display,
                         subtitle: subtitle
                         )
  end

  private

  def remove_headers(path)
    csv = CSV.read(path, encoding: "ISO8859-1:utf-8")
    csv.shift
    csv
  end

end
