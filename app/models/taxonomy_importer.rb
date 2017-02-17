class TaxonomyImporter

  def import(path=nil)
    require 'csv'
    path ||= ENV["IMPORT_PATH"]
    path = Rails.root.join("./data/output/taxonomy.csv").to_s
    puts(ENV["IMPORT_PATH"])
    fail ArgumentError.new("import csv does not exist") unless File.exist?(path.to_s)

    csv = CSV.read(path, encoding: "ISO8859-1:utf-8")
    csv.shift

    TaxonomyLevel.delete_all

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
    subtitle = csv_row[7]
    _display = csv_row[8]
    white = csv_row[9]
    mixed = csv_row[10]
    asian = csv_row[11]
    black = csv_row[12]
    chinese = csv_row[13]
    national = csv_row[14]

    parent_id = TaxonomyLevel.find_by_uri(parent_uri).id if parent_uri

    TaxonomyLevel.create(name: taxonomy_name.downcase,
                         level: taxonomy_level,
                         parent_id: parent_id,
                         uri: uri,
                         description: description,
                         source: source,
                         display: _display,
                         subtitle: subtitle,
                         white: white,
                         asian: asian,
                         black: black,
                         chinese: chinese,
                         national: national
                         )
  end

end
