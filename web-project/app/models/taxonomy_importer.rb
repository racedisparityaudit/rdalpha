class TaxonomyImporter

  def import(path=nil)
    require 'csv'
    path ||= ENV["IMPORT_PATH"]
    path = Rails.root.join("../data/taxonomy.csv").to_s
    puts(ENV["IMPORT_PATH"])
    fail ArgumentError.new("import csv does not exist") unless File.exist?(path.to_s)
    csv = CSV.read(path)
    csv.shift
    csv.each{ |r| import_row r}
  end

  def import_row(csv_row)
    taxonomy_name = csv_row.third
    taxonomy_level = csv_row.second
    parent_name =
      if taxonomy_level == "T0"
        nil
      elsif taxonomy_level == "T1"
        "homepage"
      elsif taxonomy_level == "T2"
        csv_row.fourth
      end


    if parent_name && parent_name != "homepage"
      parent_id = TaxonomyLevel.find_by_name(parent_name.downcase).id
    else
      parent_id = nil
    end

    TaxonomyLevel.create(name: taxonomy_name.downcase,
                         level: taxonomy_level,
                         parent_id: parent_id)
  end

end
