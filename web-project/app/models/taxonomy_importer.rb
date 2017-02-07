class TaxonomyImporter

  def import(path=nil)
    require 'csv'
    path ||= ENV["IMPORT_PATH"]
    path = Rails.root.join("../data/output/taxonomy.csv").to_s
    puts(ENV["IMPORT_PATH"])
    fail ArgumentError.new("import csv does not exist") unless File.exist?(path.to_s)
    csv = CSV.read(path)
    csv.shift
    csv.each{ |r| import_row r}
  end

  def import_row(csv_row)
    taxonomy_name = csv_row.first

    parent_name = csv_row.second.try(:downcase)
    uri         = csv_row.third
    parent_uri  = csv_row.fourth
    description = csv_row.fifth
    taxonomy_level = csv_row[5]
    source = csv_row[6]

    parent_id = TaxonomyLevel.find_by_uri(parent_uri).id if parent_uri

    TaxonomyLevel.create(name: taxonomy_name.downcase,
                         level: taxonomy_level,
                         parent_id: parent_id,
                         uri: uri,
                         description: description,
                         source: source)
  end

end
